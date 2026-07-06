# proofof.ai — Sovereign Layer Zero — Live audit trail

**Status:** LIVE — accepts `curl proofof.ai/audit/<exec_id>`

## What a citizen can verify, in any browser, in 30 seconds

```bash
curl https://proofof.ai/audit/c468e3ec-366f-5766-adad-43fd0eb197eb
```

Expected output (JSON):

```json
{
  "episode_id": "c468e3ec-366f-5766-adad-43fd0eb197eb",
  "subject": "Sovereign Layer Zero Charter v1.0 mint",
  "issuer": "did:csoai:nicholas-001",
  "str": "str:v1:QD595cz6iQaEaYOjwwgLmMdoz1mtm1pzKBb9ygvMvf3xhQ28@GB",
  "sigils": [
    {
      "op": "P",
      "ts": "2026-07-05T13:51:00Z",
      "intent": "CHARTER-MINTED-v1.0-SOVEREIGN-LAYER-ZERO-2026-07-05T13:51Z-CSOAI-Ltd",
      "digest": "77ab0e6f9d6c77e8",
      "prev_sig": "ace2941d9a1ee2a7...",
      "signature": "776c4feda3f112c3...",
      "alg": "ed25519"
    },
    {
      "op": "A",
      "ts": "2026-07-05T13:52:33Z",
      "intent": "ORG_KERNEL_L1_IDENTITY_REGISTRATION-charter_custodian",
      "agent_id": "agent-f8c3f34772e0",
      "digest": "...",
      "alg": "ed25519"
    }
  ],
  "orgkernel": {
    "l1_identity": {
      "did": "did:csoai:nicholas-001",
      "jurisdiction": "GB",
      "pubkey_b64": "QD595cz6iQaEaYOjwwgLmMdoz1mtm1pzKBb9ygvMvf3xhQ28"
    },
    "l2_execution_count": 0,
    "l3_compliance_count": 0,
    "compliance_rate": 0
  },
  "charter": {
    "title": "Sovereign Layer Zero Charter v1.0",
    "version": "1.0.0",
    "protocols_unified": [
      "MCP", "A2A", "ACP", "AGNTCY", "x402", "L2B", "L2L",
      "OIDC", "JWT", "WebSocket", "gRPC", "ANP", "IBC", "DID"
    ],
    "license": "CC0 1.0 (document); Apache-2.0 (reference impl)",
    "canonical_url": "https://csoai.org/charters/layer-zero/v1.0",
    "github": "https://github.com/CSOAI/SOVEREIGN-LAYER-ZERO-CHARTER"
  },
  "verify_chain": "PASS"
}
```

## What this proves

A citizen in any country, with no install, no wallet, no nation-state trust, can verify that:

1. The Charter exists.
2. The Ed25519 signature is valid.
3. The OrgKernel L1 identity is bound to a published pubkey.
4. The chain is unbroken since the prior sovereign emission.

This is what "browser-verifiable" means. **No nation-sovereign barrier.**

## Public mirror endpoints

| Region | URL |
|---|---|
| UK primary | `https://proofof.ai/audit/...` |
| EU mirror | `https://proofof.eu/audit/...` |
| AU/NZ | `https://proofof.au/audit/...` |
| US | `https://proofof.us/audit/...` |

(Sovereign mirrors operated by sovereign coalition. No single jurisdiction controls.)

---

## Sovereign Layer 0 — at a glance

```
MCP     ┐
A2A     │
ACP     │
AGNTCY  ├─→  UWE  ─→  SIGIL  ─→  OrgKernel L1/L2/L3
x402    │        ↑
L2B     │     audit-trail public at proofof.ai/audit/<id>
L2L     │
```

**One charter. Eleven protocols. One trust root.**
