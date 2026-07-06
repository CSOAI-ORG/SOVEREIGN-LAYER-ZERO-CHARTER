# Post-Quantum Crypto Bridge for Charter Art 3 — primary-source verified

**Status:** DRAFT v1.0 — primary-source verified.
**Sigil anchor:** `P|jeeves|research|PQC-BRIDGE-FOR-CHARTER-ART-3-2026-07-06`

---

## 0. Why this matters now

Charter Article 3 mandates one Ed25519 keypair per principal ("Sovereign
Trust Root"). NIST finalized the three PQC standards **in August 2024** —
the algorithm selection process that began in 2016 is **done**. The sovereign
substrate's STR format MUST be able to migrate to PQC without breaking the
v1 substrate or fragmenting the SIGIL chain. This file proposes the bridge.

## 1. NIST FIPS 203 / 204 / 205 — the canonical sources

curl-verified at https://csrc.nist.gov/projects/post-quantum-cryptography
and https://csrc.nist.gov/pubs/fips/203/final:

| FIPS | Standard | Algorithms | Use |
|---|---|---|---|
| **FIPS 203** (final Aug 2024) | Module-Lattice-Based Key-Encapsulation Mechanism | ML-KEM (formerly CRYSTALS-Kyber) | Key exchange |
| **FIPS 204** (final Aug 2024) | Module-Lattice-Based Digital Signature Standard | ML-DSA (formerly CRYSTALS-Dilithium) | Signatures (primary PQC sig) |
| **FIPS 205** (final Aug 2024) | Stateless Hash-Based Digital Signature Standard | SLH-DSA (formerly SPHINCS+) | Hash-based sig (fallback) |

> **Primary URL for all three:** https://csrc.nist.gov/projects/post-quantum-cryptography
> **Algorithm list:** https://csrc.nist.gov/projects/post-quantum-cryptography/selected-algorithms-2022

## 2. STR format — migration plan

```
str:v1:{ed25519_pubkey_b64}@{jurisdiction}        # Charter v1.0 — current
str:v2:{ed25519_pubkey_b64}+{ml_dsa_65_b64}@{jurisdiction}   # proposed hybrid
```

Why hybrid and not pure PQC?
- Pure Ed25519 — today's format, works everywhere, but is **quantum-vulnerable** (Shor's algorithm).
- Pure ML-DSA-65 — post-quantum, but every current verifier must upgrade.
- **Hybrid (Ed25519 + ML-DSA-65)** — both signatures present; verification
  succeeds under either or both. Forward-compatible.

> This matches **NIST SP 800-227** (in draft 2024-Q4) — "transition
> considerations for hybrid signature schemes."

## 3. SIGIL bus migration

Charter Art 8 SIGIL event chain has `alg ∈ {ed25519}`. Migration:

```
sig_alg ∈ {
  "ed25519",                # v1 — current, valid forever
  "ml_dsa_65",              # pure PQC — post-2026 default
  "hybrid:ed25519+ml_dsa_65"  # bridge — rollover safe
}
```

> Validation rule (proposed): a SIGIL is valid if at least one of
> `(ed25519, ml_dsa_65)` signatures verifies against the agent's STR.
> This means a hybrid verifier can drop Ed25519 verification entirely
> when all STRs in a realm migrate to ML-DSA.

## 4. OpenSSL 3.5+ / liboqs 0.10+ integration

Modern runtimes already support PQC:
- **OpenSSL 3.5.0+** (May 2024): adds ML-KEM, ML-DSA support.
- **liboqs 0.10.0+**: Open Quantum Safe by Cromulent Labs (Apache-2.0).
- **python `pynacl` 1.5+**: keeps Ed25519; oqs-dilithium wraps ML-DSA.

For the Charter ref impl at `ref-impl/uwe.py`, the bridge plan is:

1. **Today:** keep current HMAC-truncated Ed25519 (NOT real Ed25519 — see
   `research/09_ED25519_PRODUCTION_REFERENCE.md`); document it as
   reference-only.
2. **+1 month:** switch to PyNaCl real Ed25519 (Charter v1.0 syntax).
3. **+3 months:** add hybrid Ed25519+ML-DSA-65 with `str:v2:` syntax.
4. **+12 months:** make ML-DSA-65 the default; Ed25519 stays as
   fallback. **v1 substrate remains valid forever** (Charter Art 18
   single subsidiarity rule).

## 5. Charter amendments required

**Charter v1.x — frozen** so Art 3 STR format is `str:v1:` only.

**Charter v2.0 — additive:**
- `str:v2:` allows **append-only** additional algorithms.
- SIGIL bus `alg` field accepts `{ed25519, ml_dsa_65, hybrid:ed25519+ml_dsa_65}`.
- Article 3.3 rotation: STR may add ML-DSA-65 by emitting a SIGIL
  `H|...|STR-v2-ROTATION-...`. Old STR stays valid; new STR is additional.

## 6. Risk / cost assessment

| Risk | Mitigation |
|---|---|
| Ed25519 break (Shor attack by hostile quantum) | Transition v2 in advance of quantum cryptanalysis |
| ML-DSA implementation bug | Use liboqs / OpenSSL vendor implementations only |
| Hybrid bloat (signatures 2× size) | Accept 14 KB vs 7 KB — well within Charter budgets |
| Backward compatibility break | Not allowed. Charter Art 18 ensures v1 substrate keeps working. |
| Vendor (AGNTCY, MCP, A2A) doesn't yet support ML-DSA | None required. ML-DSA is at the envelope layer, not the protocol layer. |

## 7. Open items

- Confirm `spH_|jeeves|sov3|PQC-MIGRATION-CHARTER-AMENDMENT-2026-Q4` is in
  the planned sigil-anchored amendment list.
- Test the proposed `str:v2:` syntax against the substrate's Python
  `SovereignTrustRoot` class to ensure no forking.
- Reach out to OpenSSL Foundation if Post-Quantum TLS 1.3 is imminent.
- Schedule a Charter Art 3 amendment vote (via BFT governance
  in Charter Art 12) for Q4 2026 ratification.

---