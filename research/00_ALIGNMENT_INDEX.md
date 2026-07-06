# Sovereign Layer Zero — Research Alignment Index

**Status:** ACTIVE — this is the single source of truth preventing duplicate work.
**Last update:** 2026-07-06 (auto-incremented by sigil-anchored commits)
**Sigil anchor:** `H|jeeves|sov3|RESEARCH-ALIGNMENT-v1.0-OPEN-2026-07-06`

---

## 0. Purpose (read first)

This is the **anti-duplication ledger** for everything we build on top of the
Sovereign Layer Zero Charter v1.0. Before any agent — human or LLM — adds a
new document, dataset, MCP server, or framework to the corpus, they MUST
check this index. If it's already here, do not rebuild. If it's not, add it
before shipping.

Every entry here is anchored to one or more Charter Articles so we can
audit "what we built, what we skipped, and why."

---

## 1. The Charter's existing footprint (DO NOT RE-DUPLICATE)

| Source | Path | Status |
|---|---|---|
| Sovereign Layer Zero Charter v1.0 | `/Users/nicholas/CSOAI/SOVEREIGN-LAYER-ZERO-CHARTER/CHARTER.md` | ✅ MINTED |
| Reference implementation | `/Users/nicholas/CSOAI/SOVEREIGN-LAYER-ZERO-CHARTER/ref-impl/uwe.py` | ✅ PASSES E2E DEMO |
| GitHub-ready repo | `/Users/nicholas/CSOAI/SOVEREIGN-LAYER-ZERO-CHARTER/` (13 files) | ✅ READY TO PUSH |
| SIGIL anchor on chain | digest `77ab0e6f9d6c77e8` (mint), `1b2a34ac6e064a6f` (publish), `efccde5f495558cb` (cargo) | ✅ SIGNED |
| OrgKernel L1 identity | `agent-f8c3f34772e0` | ✅ MINTED |
| OrgKernel L2 execution row | `exec-6e5447f3a422` | ✅ APPENDED |
| OrgKernel L3 compliance | `assert-e275d15b5067`, 100% rate | ✅ ASSERTED |

**If your contribution overlaps with these, it is a duplicate.** Stop. Pivot.

---

## 2. Charter Articles → research alignment (THE MAP)

| Charter Article | What the Charter already covers | What research is allowed to extend | What research MUST NOT re-define |
|---|---|---|---|
| Art 0 — Purpose | Sets public-sublayer objective | n/a | n/a |
| Art 1 — Definitions | Defines STR / UWE / L1/L2/L3 | n/a | n/a |
| Art 2 — 10 design principles | One trust root, no breakage, etc. | n/a | n/a |
| Art 3 — Sovereign Trust Root | One Ed25519 keypair per principal | Format spec for non-Ed25519 PQC migration MUST append `str:v2:` not rewrite | MUST NOT change STR v1 |
| Art 4 — Unified Wire Envelope | JSON envelope shape | Wire-shape variations per protocol stay inside `body` | MUST NOT add a competing envelope |
| **Art 5 — Protocol mapping** | List of MCP/A2A/ACP/AGNTCY/x402/L2B/L2L | **THIS IS WHERE research findings GO** | n/a |
| **Art 6 — L2B** | LLM→Backend formal def | Any backend adapter as a UWE `via[0]="l2b"` payload | MUST NOT fork L2B into "L2B-fork" |
| **Art 7 — L2L** | LLM↔LLM formal def | Any model-to-model hop as `via[0]="l2l"` payload | MUST NOT fork L2L |
| Art 8 — SIGIL event chain | Op codes P,V,M,Q,C,H,S,A,E | New event types append `S|E|…`, not replace | MUST NOT rewire chain |
| Art 9 — OrgKernel L1/L2/L3 | Three-layer audit | Additional framework pickers in L3 | MUST NOT collapse layers |
| Art 10 — DEFONEOS compat | Three compartments rule | n/a | MUST NOT cross-link compartments |
| Art 11 — 6-tier adoption | T0–T5 ladder | Vendor-specific tier example docs | MUST NOT invent tier 6 |
| Art 12 — Governance | CNI working group | Draft bylaws | MUST NOT move authority away from CSOAI |
| Art 13 — Versioning | v1 frozen, v2 additive | New protocol bindings | MUST NOT break v1 wire |
| Art 14 — 8-framework profile | EU/GDPR/ISO/NIST/SOC2/DORA/UK-AI-Bill/NIS2 | Additional frameworks as L3 assertions | MUST NOT drop an existing one |
| **Art 15 — Red lines** | No kinetic, no surveillance | n/a | **MUST NOT cross any red line** |
| **Art 16 — Compute-light** | 1 e2-micro + Qwen 30B-A3B | Mac/CPU deploy guides | MUST NOT propose GPU-required design |
| Art 17 — 8-channel publish | 8 channels drafted | Refine each channel copy | n/a |
| Art 18 — Single subsidiarity rule | Vendor protocols silent = vendor wins | Map EU AI Act's downstream acts | MUST NOT override vendor protocol when Charter is silent |
| Art 19 — No representation | Don't claim endorsement | n/a | MUST NOT claim AUKUS endorsement |
| Art 20 — Minting contact | CSOAI Ltd, UK 16939677 | n/a | n/a |

---

## 3. Incoming research (auto-populated by subagent outputs)

### 3.1 Agent-interop frontier (2024-2026)

**Status: SUBAGENT_RUNNING.** Output will land in
`research/01_AGENT_INTEROP_FRONTIER.md` within minutes.

### 3.2 CC0 + public-domain science corpora

**Status: SUBAGENT_RUNNING.** Output will land in
`research/02_CC0_CORPUS_HITCHHIKERS_GUIDE.md` within minutes.

### 3.3 Defence-AI public patterns (Article-15-safe)

**Status: COMPLETED.** `research/03_DEFENSE_AI_PUBLIC_PATTERNS.md` (175 lines,
8.7 KB) — MITRE ATT&CK (taxonomy only), MITRE D3FEND, OSCAL, OpenSSF,
NIST CSF, OWASP SAMM, OpenSSF Scorecard, sigstore, in-toto.

### 3.4 A2A AgentCard schema (verbatim, primary-source)

**Status: COMPLETED.** `research/04_A2A_AGENT_CARD_SCHEMA.md` (154 lines,
6.3 KB) — full verbatim AgentCard JSON shape + every field's
required/optional + transport bindings (JSON-RPC/HTTP+JSON/gRPC) +
**CORRECTION**: a2aproject is canonical, not a2a-mesh.

### 3.5 Article 14 framework proofs

**Status: COMPLETED (subagent).** `research/05_ARTICLE14_FRAMEWORK_PROOFS.md`
(142 lines, 14.7 KB) — 8 frameworks each mapped to URL + licence + L3
assertion tuple + Charter-clause cross-reference. Includes honest licence
notes (ISO 42001 / SOC 2 paywalled; UK AI Bill private member's bill).

### 3.6 Open-weights registry

**Status: COMPLETED.** `research/06_OPEN_WEIGHTS_REGISTRY.md` (119 lines,
6.0 KB) — **Qwen3-30B-A3B** canonical for Art 16. Llama / Gemma /
OpenRAIL closed-weights EXCLUDED for Art 14 L3 audit-trail reasons.

### 3.7 Government open-source catalogue (Article-15-safe)

**Status: COMPLETED.** `research/07_GOV_OPEN_SOURCE_INDEX.md` (73 lines,
3.5 KB) — NASA, AFRL, DARPA programs (study-only), NCSC, CISA, NIST,
Oscal, sigstore, MITRE D3FEND; hard NO list of weapon-tracking
code under Charter Art 15.

### 3.8 PQC migration bridge (NIST FIPS 203/204/205)

**Status: COMPLETED.** `research/08_PQC_BRIDGE_FOR_CHARTER.md` (110 lines,
4.9 KB) — `str:v2:` hybrid Ed25519+ML-DSA-65 syntax proposed; SIGIL
chain migration path preserves v1 forever.

### 3.9 Ed25519 production reference (RFC 8032 verified)

**Status: COMPLETED + REFERENCE-IMPL UPGRADED.** `research/09_ED25519_PRODUCTION_REFERENCE.md` +
`ref-impl/uwe.py` patched to dual-sign (reference HMAC truncated +
real RFC 8032 Ed25519 via PyNaCl 1.5.0). RFC 8032 §7.1 Test 1 verified
byte-for-byte against the canonical pubkey/sig.

---
   - `csoai-defoneos/certifies/...` (CERTIFIES, public framing: csoai-defoneos.org)
   - `sovereign-layer-zero/...` (the Charter's own namespace, public)

2. **Never use the legacy stripe-account names.** They are known traps.

3. **Never claim AUKUS / DAIC accreditation.** This is in Charter Art 15 and Art 19.

4. **Never use the `defonos.io` domain.** Known trap (Art 15 red line).

5. **Single Trust Root per principal.** All keys live under one STR per Article 3.

---

## 5. Cross-references — what we don't redup

Already shipped and audit-anchored (DO NOT REBUILD):

- Materials/data/signals: **49 GB on GCP VM `/data/hive-data`** (organic) +
  synth + extracts as of 17 Jun 2026.
- MCP estate: **371 servers catalogued** on SOV3 bridge.
- Sigil receipts on chain: **1,833+** as of probe-1.
- OrgKernel identity: `agent-f8c3f34772e0`.
- Charter artefacts: SHA-256 `df65a658...22054`.

If research uncovers something already represented in these, the answer
is **import, link, sigil, don't re-write.**

---

## 6. Contribution pattern (the only way new docs get added)

1. Search this index first.
2. If absent, draft in `research/<NN>_<TOPIC>.md` with:
   - License (must be one of: CC0, CC-BY, MIT, Apache-2.0, BSD-2/3, public-domain, OGL-UK-3.0, EUPL-1.2).
   - Primary URL(s).
   - Anchor: which Charter Article(s) it extends.
   - SHA-256 of any artifact (if you ingested it).
   - Sigil anchor (golden pattern: `H|jeeves|sov3|<TAG>-<DATE>`).
3. Append row in this index.
4. Push only after a SIGIL emit + OrgKernel L1 ack.

---

## 7. SHA-256 register (every annex gets one)

Will be populated as subagent outputs land.

---

## 8. Sigil log (research-only appends)

This file is the "I opened something new" log. When you add a research
file, you emit one sigil. Format:

```
P|jeeves|research|RESEARCH-OPENED-<TOPIC>-<DATE>-<DIGEST>
```

(Will be populated by subagent outputs as they complete.)

---

## 9. Reading list (start here)

- `CHARTER.md` (20 articles)
- `research/00_ALIGNMENT_INDEX.md` (this file)
- `research/01_AGENT_INTEROP_FRONTIER.md` (when subagent returns)
- `research/02_CC0_CORPUS_HITCHHIKERS_GUIDE.md`
- `research/03_DEFENSE_AI_PUBLIC_PATTERNS.md`

---

## 10. ONE-LINE MISSION

**"One charter, eleven protocols, one trust root, one free corpus."**
The charter is minted. The corpus is being assembled. Duplication ends now.
