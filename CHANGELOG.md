# Changelog — Sovereign Layer Zero Charter

All notable changes to this Charter are documented here. The SHA-256 of the
canonical CC0 file is published in `SOV/CHARTER.sha256` on the SIGIL chain
every time a version is minted.

## v1.0.0 — 2026-07-05

### Minted

- Initial public release under CC0 1.0 (document) + Apache-2.0 (reference impl).
- SIGIL anchor: `H|jeeves|sov3|LAYER-ZERO-CHARTER-v1.0-MINTED-2026-07-05`
- OrgKernel L1 custodian identity: `did:csoai:nicholas-001`
- SHA-256: `df65a6585cf6a686cbfd881f56c04447056e2551e7c04db57a80543521022054`
- 11 protocols unified: MCP, A2A, ACP, AGNTCY, x402, L2B (newly defined), L2L
  (newly defined), plus OIDC / JWT / WebSocket / gRPC / ANP / IBC / DID as
  transports and identity.

### Added

- Article 0 — Purpose
- Article 1 — Definitions
- Article 2 — 10 design principles
- Article 3 — Sovereign Trust Root (STR)
- Article 4 — Unified Wire Envelope (UWE) — full JSON schema
- Article 5 — Protocol mapping table
- Article 6 — L2B formal definition
- Article 7 — L2L formal definition
- Article 8 — SIGIL event chain
- Article 9 — OrgKernel L1/L2/L3 three-layer audit
- Article 10 — DEFONEOS compatibility
- Article 11 — 6-tier adoption ladder
- Article 12 — Governance (CNI working group)
- Article 13 — Versioning + deprecation
- Article 14 — 8-framework compliance proof
- Article 15 — Red lines (no kinetic, no surveillance)
- Article 16 — Compute-light doctrine
- Article 17 — 8-channel first-mover publication
- Article 18 — Single subsidiarity rule
- Article 19 — No representation
- Article 20 — Minting contact

### Signed

- Charter author: `did:csoai:nicholas-001` (CSOAI Ltd, UK 16939677)
- Ed25519 pubkey: `QD595cz6iQaEaYOjwwgLmMdoz1mtm1pzKBb9ygvMvf3xhQ28`
- OrgKernel identity: `agent-f8c3f34772e0`

### Pending (within 7 days)

- DOI mint via Zenodo
- GitHub repo creation (this repo)
- arXiv cs.AI + cs.CR + cs.DC submission
- IETF `draft-templeman-sovereign-layer-zero-00` submission
- AGNTCY interop review request to LF TSC
- W3C DID namespace registration request
- OECD AI Policy Observatory submission

### v1.0.1 — 2026-07-06 (gogogo sprint)

Added under CC0 in `/research/`:

- `04_A2A_AGENT_CARD_SCHEMA.md` — verbatim A2A v1.0 spec JSON shape + transport bindings (JSON-RPC / HTTP+JSON / gRPC). **CORRECTION:** canonical A2A repo is `a2aproject/A2A`, not `a2a-mesh`.
- `05_ARTICLE14_FRAMEWORK_PROOFS.md` — 8 frameworks × URL × licence × Charter-clause cross-walk.
- `06_OPEN_WEIGHTS_REGISTRY.md` — Qwen3-30B-A3B canonical for Art 16.
- `07_GOV_OPEN_SOURCE_INDEX.md` — gov OSS, Article-15 safe only.
- `08_PQC_BRIDGE_FOR_CHARTER.md` — NIST FIPS 203 / 204 / 205; `str:v2:` hybrid Ed25519+ML-DSA-65.
- `09_ED25519_PRODUCTION_REFERENCE.md` — RFC 8032 §7.1 verified against PyNaCl 1.5.0.

Upgraded `ref-impl/uwe.py`:
- `SovereignTrustRoot.sign()` now dual-signs: emits BOTH reference HMAC-truncated (back-compat) AND real RFC 8032 Ed25519 via `nacl.signing.SigningKey`.
- Sigil envelope carries `signature` (= real Ed25519 64-byte hex), `reference_sig` (= back-compat), `rfc8032_pubkey` (= real 32-byte hex), `alg = ed25519`.
- `SigilChain.append` integrates same dual-sign.

Demo re-run: PASS.
RFC 8032 §7.1 Test 1 verification: **PUBKEY match + SIG match = True**.
