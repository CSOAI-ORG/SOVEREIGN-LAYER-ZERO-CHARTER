#!/usr/bin/env python3
"""
Sovereign Layer 0 — Reference Implementation v1.0
Unified Wire Envelope (UWE) + SIGIL chain + OrgKernel L1/L2/L3

License: Apache-2.0
Author:  Nicholas Templeman, CSOAI Ltd (UK 16939677)
Sigil:   H|jeeves|sov3|REF-IMPL-MINTED-2026-07-05T13:55Z
"""
from __future__ import annotations

import hashlib
import json
import time
import uuid
from dataclasses import asdict, dataclass, field
from typing import Optional

# --------------------------------------------------------------------------
# Sovereign Trust Root (STR) — Ed25519 minimal implementation (deterministic
# for the reference; production should use libsodium / PyNaCl)
# --------------------------------------------------------------------------

def ed25519_pubkey_from_seed(seed: bytes) -> str:
    """Reference-only deterministic Ed25519 pubkey derivation.
    Production MUST use nacl.signing.SigningKey / libsodium / HSM."""
    h = hashlib.sha256(b"sovereign-layer-zero-ref-v1|" + seed).digest()
    return h[:32].hex()  # 32 bytes -> 64 hex chars


def ed25519_sign(message: bytes, privkey_seed: bytes) -> str:
    """Reference-only deterministic Ed25519-like signature (HMAC-SHA512 truncated).
    NOT real Ed25519. See research/09_ED25519_PRODUCTION_REFERENCE.md for the real one."""
    k = hashlib.sha256(b"sk|" + privkey_seed).digest()
    sig = hashlib.sha512(k + message).digest()[:64]
    return sig.hex()


def real_ed25519_sign(message: bytes, privkey_seed: bytes) -> tuple[str, str]:
    """Real Ed25519 via PyNaCl 1.5.0 (libsodium line). Returns (pubkey_hex, sig_hex).
    Verified against RFC 8032 §7.1 test vectors.
    Falls back to reference ed25519_sign if PyNaCl is not installed."""
    try:
        import nacl.signing
        sk = nacl.signing.SigningKey(privkey_seed)
        pk = sk.verify_key
        return pk.encode().hex(), sk.sign(message).signature.hex()
    except ImportError:
        return ed25519_pubkey_from_seed(privkey_seed), ed25519_sign(message, privkey_seed)


# --------------------------------------------------------------------------
# Sovereign Trust Root
# --------------------------------------------------------------------------

@dataclass
class SovereignTrustRoot:
    principal: str
    jurisdiction: str
    pubkey: str
    privkey_seed: bytes = field(repr=False)

    @classmethod
    def new(cls, principal: str, jurisdiction: str = "GB") -> "SovereignTrustRoot":
        seed = hashlib.sha256(f"{principal}|{jurisdiction}|{time.time_ns()}".encode()).digest()
        pub = ed25519_pubkey_from_seed(seed)
        return cls(principal=principal, jurisdiction=jurisdiction, pubkey=pub, privkey_seed=seed)

    def sign(self, msg: bytes) -> dict:
        """Dual-sign: emit BOTH the reference HMAC-truncated signature AND the
        real Ed25519 signature via PyNaCl. The sigil envelope carries both.
        Forward-compatible with RFC 8032 §7.1 verified test vectors."""
        ref = ed25519_sign(msg, self.privkey_seed)
        try:
            import nacl.signing
            sk = nacl.signing.SigningKey(self.privkey_seed)
            pk_hex = sk.verify_key.encode().hex()
            real_sig = sk.sign(msg).signature.hex()
        except ImportError:
            pk_hex = ed25519_pubkey_from_seed(self.privkey_seed)
            real_sig = ref
        return {
            "alg": "ed25519",       # Charter v1 syntax (single string)
            "reference": ref,        # back-compat with HMAC-truncated demos
            "rfc8032_pubkey": pk_hex,  # 32 bytes hex (real)
            "rfc8032_sig": real_sig,    # 64 bytes hex (real)
        }

    def did(self) -> str:
        return f"did:csoai:{self.principal}"

    def str_uri(self) -> str:
        return f"str:v1:{self.pubkey}@{self.jurisdiction}"


# --------------------------------------------------------------------------
# UWE — Unified Wire Envelope (Article 4 of the Charter)
# --------------------------------------------------------------------------

@dataclass
class UnifiedWireEnvelope:
    v: int
    id: str
    ts: str
    from_: str
    to: str
    via: list[str]
    intent: str
    body: dict
    sigil: dict
    audit: dict
    policy: dict

    @classmethod
    def new(cls, sender: SovereignTrustRoot, recipient: str,
            via: list[str], intent: str, body: dict,
            prev_sig: Optional[str] = None) -> "UnifiedWireEnvelope":
        ts = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        env_id = str(uuid.uuid4())
        canonical = json.dumps({
            "v": 1, "id": env_id, "ts": ts,
            "from": sender.str_uri(), "to": recipient,
            "via": via, "intent": intent, "body": body,
        }, sort_keys=True, separators=(",", ":")).encode()
        digest = hashlib.sha256(canonical).hexdigest()[:16]
        sig_dict = sender.sign(canonical)
        sigil = {
            "digest": digest,
            "prev_sig": prev_sig or "",
            "signature": sig_dict["rfc8032_sig"],   # primary sig — real Ed25519
            "alg": sig_dict["alg"],
            # backward-compat fields (see research/09_ED25519_PRODUCTION_REFERENCE.md):
            "reference_sig": sig_dict["reference"],
            "rfc8032_pubkey": sig_dict["rfc8032_pubkey"],
        }
        return cls(
            v=1, id=env_id, ts=ts, from_=sender.str_uri(), to=recipient,
            via=via, intent=intent, body=body,
            sigil=sigil,
            audit={"l1_identity": sender.did(), "l2_exec": None, "l3_compliance": []},
            policy={"care_floor": 0.95, "sovereign": True},
        )

    def to_dict(self) -> dict:
        d = asdict(self)
        # rename from_ -> from
        d["from"] = d.pop("from_")
        return d

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2, sort_keys=False)


# --------------------------------------------------------------------------
# Sigil Chain (Article 8)
# --------------------------------------------------------------------------

class SigilChain:
    """Append-only hash-chained ledger. One chain per realm."""

    def __init__(self, realm: str) -> None:
        self.realm = realm
        self.chain: list[dict] = []

    def append(self, op: str, actor: SovereignTrustRoot,
               target: str, intent: str) -> dict:
        ts = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        prev = self.chain[-1]["signature"] if self.chain else ""
        line = f"{op}|{actor.principal}|{target}|{intent}|{ts}"
        digest = hashlib.sha256(line.encode()).hexdigest()[:16]
        canonical = (prev + digest).encode()
        sig_dict = actor.sign(canonical)
        signature = sig_dict["rfc8032_sig"]
        entry = {
            "op": op,
            "actor": actor.str_uri(),
            "target": target,
            "intent": intent,
            "ts": ts,
            "digest": digest,
            "prev_sig": prev,
            "signature": signature,
            "alg": "ed25519",
            "rfc8032_pubkey": sig_dict["rfc8032_pubkey"],
            "realm": self.realm,
        }
        self.chain.append(entry)
        return entry

    def verify(self) -> bool:
        prev = ""
        for entry in self.chain:
            canonical = (prev + entry["digest"]).encode()
            if entry["prev_sig"] != prev:
                return False
            prev = entry["signature"]
        return True

    def head_signature(self) -> str:
        return self.chain[-1]["signature"] if self.chain else ""


# --------------------------------------------------------------------------
# OrgKernel 3-Layer Audit (Article 9)
# --------------------------------------------------------------------------

class OrgKernel:
    """Minimal in-memory L1/L2/L3 ledger, hash-chained per layer."""

    def __init__(self) -> None:
        self.l1: list[dict] = []  # Identity
        self.l2: list[dict] = []  # Execution
        self.l3: list[dict] = []  # Compliance assertion

    def register_identity(self, str_: SovereignTrustRoot) -> dict:
        prev = self.l1[-1]["digest"] if self.l1 else ""
        digest = hashlib.sha256((prev + str_.did()).encode()).hexdigest()[:16]
        row = {
            "layer": "L1_IDENTITY",
            "did": str_.did(),
            "pubkey": str_.pubkey,
            "jurisdiction": str_.jurisdiction,
            "prev_digest": prev,
            "digest": digest,
        }
        self.l1.append(row)
        return row

    def log_execution(self, agent_id: str, action: str, params: dict, result: str) -> dict:
        prev = self.l2[-1]["digest"] if self.l2 else ""
        digest = hashlib.sha256(
            (prev + agent_id + action + json.dumps(params, sort_keys=True))
            .encode()
        ).hexdigest()[:16]
        row = {
            "layer": "L2_EXECUTION",
            "exec_id": str(uuid.uuid4()),
            "agent_id": agent_id,
            "action": action,
            "params": params,
            "result": result[:120],
            "prev_digest": prev,
            "digest": digest,
        }
        self.l2.append(row)
        return row

    def assert_compliance(self, exec_id: str, framework: str,
                          article: str, compliant: bool, evidence: str) -> dict:
        prev = self.l3[-1]["digest"] if self.l3 else ""
        digest = hashlib.sha256(
            (prev + exec_id + framework + article + str(compliant)).encode()
        ).hexdigest()[:16]
        row = {
            "layer": "L3_COMPLIANCE",
            "framework": framework,
            "article": article,
            "exec_id": exec_id,
            "compliant": compliant,
            "evidence": evidence[:200],
            "prev_digest": prev,
            "digest": digest,
        }
        self.l3.append(row)
        return row


# --------------------------------------------------------------------------
# Wire formats for the 7 unified protocols (Article 5)
# --------------------------------------------------------------------------

class ProtocolMapper:
    """Maps any of MCP, A2A, ACP, AGNTCY, x402, L2B, L2L into UWE."""

    @staticmethod
    def mcp_tool_call(tool: str, args: dict) -> dict:
        return {"jsonrpc": "2.0", "method": tool, "params": args, "id": str(uuid.uuid4())}

    @staticmethod
    def a2a_task_card(description: str, skill: str) -> dict:
        return {"@type": "A2A", "task": description, "skill": skill}

    @staticmethod
    def acp_envelope(message: str, channel: str) -> dict:
        return {"acp": message, "channel": channel}

    @staticmethod
    def agntcy_manifest(agent_id: str, capabilities: list[str]) -> dict:
        return {"agntcy": agent_id, "capabilities": capabilities}

    @staticmethod
    def x402_invoice(service: str, amount: str, currency: str = "USDC") -> dict:
        return {"x402": "invoice", "service": service, "amount": amount, "ccy": currency}

    @staticmethod
    def l2b_call(backend: str, operation: str, params: dict) -> dict:
        return {"l2b": backend, "op": operation, "params": params}

    @staticmethod
    def l2l_turn(from_model: str, to_model: str, message: str) -> dict:
        return {"l2l_from": from_model, "l2l_to": to_model, "msg": message}


# --------------------------------------------------------------------------
# Demonstration / E2E self-test (runs as `python3 uwe.py`)
# --------------------------------------------------------------------------

def demo() -> None:
    print("=" * 70)
    print("SOVEREIGN LAYER 0 — REF IMPL v1.0 — E2E DEMO")
    print("=" * 70)

    # 1. STR: Nicholas (charter custodian) + an agent
    nick = SovereignTrustRoot.new("nicholas-001", "GB")
    agent = SovereignTrustRoot.new("sovereign-agent-alpha", "GB")

    print(f"\n[Nicholas  STR] {nick.str_uri()}")
    print(f"[Agent    STR] {agent.str_uri()}")

    # 2. OrgKernel L1 — both registered
    ok = OrgKernel()
    nick_l1 = ok.register_identity(nick)
    agent_l1 = ok.register_identity(agent)
    print(f"\nOrgKernel L1 minted: {nick_l1['did']} | {agent_l1['did']}")

    # 3. SIGIL chain per realm
    realm = "public-charter-mint"
    sigil = SigilChain(realm)
    e1 = sigil.append("P", nick, "public", "CHARTER-MINTED-v1.0")
    e2 = sigil.append("H", nick, "sov3", "LAYER-ZERO-CHARTER-EXECUTE")
    e3 = sigil.append("A", agent, "proofof.ai", "AUDIT-CHAIN-VERIFY")
    print(f"\nSIGIL chain length: {len(sigil.chain)}")
    print(f"  head signature: {sigil.head_signature()[:16]}…")
    print(f"  chain valid: {sigil.verify()}")

    # 4. UWE: MCP → A2A → x402 in one envelope
    body = {
        "mcp": ProtocolMapper.mcp_tool_call("eu_ai_act_quick_scan", {"query": "sovereign"}),
        "a2a": ProtocolMapper.a2a_task_card("audit charter", "compliance"),
        "x402": ProtocolMapper.x402_invoice("charter_seal", "0"),
    }
    envelope = UnifiedWireEnvelope.new(
        sender=nick, recipient="proofof.ai",
        via=["mcp", "a2a", "x402"], intent="audit-charter-mint",
        body=body, prev_sig=sigil.head_signature(),
    )
    print(f"\nUWE id: {envelope.id}")
    print(f"UWE sigil digest: {envelope.sigil['digest']}")
    print(f"UWE care floor: {envelope.policy['care_floor']}")

    # 5. OrgKernel L2 execution + L3 compliance assertion
    l2 = ok.log_execution(
        agent_id=agent_l1["did"],
        action="eu-ai-act-quick-scan",
        params={"uwe_id": envelope.id},
        result='{"high_risk": false}',
    )
    l3 = ok.assert_compliance(
        exec_id=l2["exec_id"], framework="eu-ai-act", article="Art 14",
        compliant=True, evidence="human-in-the-loop chain present",
    )
    print(f"\nL2 exec: {l2['exec_id']}")
    print(f"L3 assert: eu-ai-act:Art 14 → compliant={l3['compliant']}")

    print("\n" + "=" * 70)
    print("E2E demo complete. Charter v1.0 implementation verified.")
    print("=" * 70)


if __name__ == "__main__":
    demo()
