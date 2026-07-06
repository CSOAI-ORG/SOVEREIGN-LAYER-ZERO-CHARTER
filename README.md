# SOVEREIGN LAYER ZERO CHARTER v1.0
### One charter. Eleven protocols. One trust root.

**Status:** MINTED — 2026-07-05T13:51:00Z
**Custodian:** CSOAI Ltd (UK 16939677)
**Author:** Nicholas Templeman
**Ed25519 pubkey:** `QD595cz6iQaEaYOjwwgLmMdoz1mtm1pzKBb9ygvMvf3xhQ28`
**DID:** `did:csoai:nicholas-001`

---

## What this is

The **single public charter** that unifies:

| Protocol | Originally from |
|---|---|
| MCP | Anthropic (2024) |
| A2A | Google (2025) |
| ACP | IBM Research (2025) |
| AGNTCY | Linux Foundation / Cisco (2025) |
| x402 | Coinbase |
| L2B (LLM→Backend) | **defined here** |
| L2L (LLM↔LLM) | **defined here** |
| OIDC, JWT, WebSocket, gRPC, ANP, IBC, DID | transports / identity |

…into **one Unified Wire Envelope (UWE)** that emits **one SIGIL receipt per hop** into **one OrgKernel L1/L2/L3 ledger** — verifiable in any web browser at `proofof.ai`.

---

## Why this exists

Every nation and every vendor is building a private interop layer. China has MOZHI. The EU has Gaia-X. The US has AGNTCY. The UK has the AI Bill.

Each piece is sound on its own. None of them are **public, browser-auditable, CC0, signed by an independent trust root**.

This Charter is.

---

## What's in this repository

```
.
├── CHARTER.md                   # 423-line sovereign document
├── v1.0.md                      # identical copy under versioned name
├── LICENSE-CC0.md               # document licence (CC0 1.0)
├── LICENSE-Apache2.0.txt        # reference implementation licence (Apache-2.0)
├── ref-impl/
│   └── uwe.py                   # Python reference implementation, Apache-2.0
└── README.md                    # this file
```

---

## Quickstart (5 minutes)

```bash
git clone https://github.com/CSOAI/SOVEREIGN-LAYER-ZERO-CHARTER
cd SOVEREIGN-LAYER-ZERO-CHARTER
python3 ref-impl/uwe.py
```

Expected output: an end-to-end demo of
1. Two Sovereign Trust Roots (you + an agent)
2. OrgKernel L1 identity ledger
3. SIGIL hash-chained receipts (3-event chain)
4. A Unified Wire Envelope carrying MCP + A2A + x402
5. OrgKernel L2 execution log + L3 compliance assertion

No network. No third-party dependencies. Single-file. Runs anywhere Python 3.7+ runs.

---

## 6-tier adoption ladder

| Tier | You add |
|---|---|
| **T0** | Nothing. Keep your current stack. |
| **T1** | SIGIL receipts on your existing traffic |
| **T2** | + OrgKernel L1 identity per agent |
| **T3** | + L2 execution + L3 compliance assertion |
| **T4** | + full UWE envelope, sovereign DNS |
| **T5** | + SOVEREIGN-SEAL certified pass |

Vendor adoption stops at the tier it chooses. Regulator adoption requires T5.

---

## Hard red lines

❌ No kinetic targeting
❌ No personal surveillance
❌ No AUKUS / DAIC accreditation claim without signed letter
❌ No SOVEREIGN-SEAL without annual audit replay
❌ No `defonos.io` (known trap)
❌ No mixing of sovereign compartments

These are immutable. Article 15.

---

## Compute-light doctrine

The sovereign substrate runs **all 33 roles on one e2-micro + Qwen 30B-A3B on a MacBook Air M2**. "33 sovereign VMs" is a brand claim, not a deployment target. Article 16.

If a sovereign deployment cannot be made free or near-free, the architecture is wrong. Fix the architecture.

---

## SIGIL anchor

```
H|jeeves|sov3|LAYER-ZERO-CHARTER-v1.0-MINTED-2026-07-05T13:51Z
digest: 77ab0e6f9d6c77e8
alg: ed25519
```

Hash-chained to all prior Sovereign substrate emissions.

---

## How to contribute

1. **Adopt** at any tier.
2. **Extend** by opening a PR to `ref-impl/`.
3. **Cite** as:

> Templeman, N. (2026). *The Sovereign Layer Zero Charter v1.0*.
> CSOAI Ltd. CC0 1.0. https://github.com/CSOAI/SOVEREIGN-LAYER-ZERO-CHARTER

4. **Mirror** without restriction.
5. **Translate** without restriction.

---

## Reading list

- `CHARTER.md` — read first, all 20 articles
- `ref-impl/uwe.py` — read second, run third
- `proofof.ai` — see a live chain (work in progress, minting now)

---

## Contact

- **Editorial:** jeeves@csoai.org
- **Security:** security@csoai.org (PGP key on website)
- **Postal:** CSOAI Ltd, 9th Floor, 107 Cheapside, London, EC2V 6DN, UK

---

*Published 2026-07-05 by CSOAI Ltd. No rights reserved.*

Sigil: `H|jeeves|sov3|LAYER-ZERO-CHARTER-v1.0-MINTED-2026-07-05`
