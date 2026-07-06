# CC0 + Public-Domain Corpus — verified primary sources

**Status:** DRAFT v0.3 — first-pass primary-source confirmation.
**Subagent 2/3 is grinding full audit. This file is the seed.**
**License:** CC0 1.0 (no copied text — only citations + facts).
**Sigil anchor:** `P|jeeves|research|CC0-CORPUS-PRIMARY-CONFIRMED-2026-07-06`

**Purpose:** Anchor every public-domain corpus we could ingest into
the sovereign substrate under Article 17 (no licensing tax). All
entries must be: CC0 / CC-BY / MIT / Apache-2.0 / OGL-UK-3.0 /
EUPL-1.2 / public-domain. Anything else is **not** allowed.

---

## Why a separate file

We are NOT licensed to download, redistribute, or train on most
public datasets unless we have the original open licence. This
file is the **licence registry**. If it isn't here, **don't
ingest it into SOV3**, full stop. The sovereign corpus is
compute-light + auditable; commercial-license data defeats both.

---

## A. Proteins + biology

| Dataset | URL | Licence | Status |
|---|---|---|---|
| AlphaFold v2.3.0 inference code | https://github.com/google-deepmind/alphafold | Apache-2.0 | ✅ confirmed in README |
| AlphaFold DB (precomputed structures) | https://alphafold.ebi.ac.uk | CC-BY-4.0 (per EBI) | TBD verify |
| ESM Atlas (ESMC + ESMFold2) | https://github.com/Biohub/esm | Apache-2.0 | ✅ confirmed |
| ESMFold2 weights on HF | https://huggingface.co/biohub/ESMFold2 | Apache-2.0 (HF mirror) | TBD verify |
| Protein Data Bank | https://www.rcsb.org | CC-BY-4.0 | TBD verify |
| UniProt | https://www.uniprot.org | CC-BY-4.0 | TBD verify |
| NCBI Gene / GenBank | https://www.ncbi.nlm.nih.gov | Public domain (US Govt) | ✅ US public domain |
| ENCODE | https://www.encodeproject.org | Public domain (US Govt data) | ✅ |
| Human Cell Atlas | https://www.humancellatlas.org | Mix (cell-specific) | verify per-dataset |

## B. Materials + chemistry

| Dataset | URL | Licence | Status |
|---|---|---|---|
| Materials Project | https://materialsproject.org | CC-BY-4.0 | TBD verify |
| PubChem | https://pubchem.ncbi.nlm.nih.gov | Public domain (US Govt) | ✅ |
| ChEBI | https://www.ebi.ac.uk/chebi | CC-BY-4.0 | TBD verify |
| Reactome | https://reactome.org | CC-BY-3.0 | TBD verify |
| KEGG | https://www.genome.jp/kegg | Free for academic; commercial licence | ⚠️ Academic-only |

> **WARNING:** KEGG cannot go into a commercial sovereign substrate
> without a paid licence. The sovereign substrate is treated as
> commercial under Charter Art 16 (compute-light, branded). **Skip.**

## C. Earth + climate + space

| Dataset | URL | Licence | Status |
|---|---|---|---|
| NASA Earthdata | https://earthdata.nasa.gov | Public domain (US Govt) | ✅ |
| NOAA NWS | https://www.weather.gov | Public domain (US Govt) | ✅ |
| OpenStreetMap | https://www.openstreetmap.org | ODbL | ✅ (share-alike) |
| Copernicus (EU) | https://copernicus.eu | Free + open (specific licence) | TBD verify |
| ECMWF | https://www.ecmwf.int | CC-BY-4.0 (ERA5 derivatives) | TBD |
| USGS EarthExplorer | https://earthexplorer.usgs.gov | Public domain (US Govt) | ✅ |
| GBIF | https://www.gbif.org | CC0 / CC-BY mix per dataset | verify |
| iDigBio | https://www.idigbio.org | CC-BY-4.0 | TBD verify |

## D. Scholarly + scientific literature

| Source | URL | Licence | Status |
|---|---|---|---|
| OpenAlex | https://openalex.org (code: https://github.com/ourresearch/openalex-*) | CC0 | ✅ CC0 confirmed via ourresearch README family |
| OpenAlex GitHub meta | https://github.com/ourresearch/openalex | (n/a — index) | ✅ |
| OpenAlex guts (data pipeline) | https://github.com/ourresearch/openalex-guts | CC0 | ✅ |
| Semantic Scholar API | https://api.semanticscholar.org | (mostly CC-BY per dataset) | ⚠️ mixed |
| OpenCitations COCI | https://opencitations.net/index/coci | CC0 | ✅ |
| Wikipedia / DBpedia (dump) | https://dumps.wikimedia.org / https://downloads.dbpedia.org | CC-BY-SA | ✅ |
| Wikidata | https://www.wikidata.org | CC0 | ✅ |
| Zenodo (research outputs) | https://zenodo.org | Per-deposit; many CC0 | verify |
| Figshare | https://figshare.com | Per-deposit | verify |
| Dryad | https://datadryad.org | CC0 typical | verify |
| arXiv full corpus | https://arxiv.org | CC-BY per article (author-chosen) | ✅ open |

## E. Open-weights foundation models (2024-2026)

| Model | URL | Licence | Status |
|---|---|---|---|
| Qwen3 (incl. 30B-A3B) | https://github.com/QwenLM/Qwen3 | Apache-2.0 inferred | TBD verify LICENSE |
| DeepSeek R1 | https://github.com/deepseek-ai/DeepSeek-R1 | MIT | ✅ confirmed |
| Ollama runtime | https://github.com/ollama/ollama | MIT | ✅ |
| Mistral (community) | https://github.com/mistralai | Apache-2.0 various | TBD |
| Llama 4 family | Meta | Custom (Llama community licence) | ⚠️ proprietary bounds |
| Gemma (Google) | https://huggingface.co/google/gemma-* | Gemma licence (custom, weights open) | ⚠️ custom |
| OLMo 2 | https://huggingface.co/allenai/OLMo-2 | Apache-2.0 | ✅ |
| Tulu 3 / 4 | https://huggingface.co/allenai/tulu-* | Apache-2.0 (most) | TBD |

> Charter Art 16 mandates the sovereign substrate may run on a
> **free or near-free compute**. Qwen3 30B-A3B on M2 MacBook Air is
> the canonical pattern. DeepSeek-R1 distilled on Qwen-32B is the
> secondary pattern. We do NOT require Llama / Gemma / Mistral closed
> licences because they muddy the audit-trail.

## F. Agent / orchestration runtimes

| Runtime | URL | Licence | Charter Article |
|---|---|---|---|
| LangGraph | https://github.com/langchain-ai/langgraph | MIT | Art 11 |
| Microsoft Agent Framework | https://github.com/microsoft/agent-framework | MIT (inferred) | Art 5 / Art 11 |
| HuggingFace SmolAgents | https://github.com/huggingface/smolagents | Apache-2.0 | Art 11 |
| CrewAI | https://github.com/crewAIInc/crewAI | MIT (inferred) | Art 11 |
| AutoGen (legacy) | https://github.com/microsoft/autogen | maintenance mode | DO NOT redup |

## G. Standards + governance primary docs (public)

| Source | URL | Licence | Status |
|---|---|---|---|
| EU AI Act (consolidated) | EUR-Lex | Public-domain per EU rules | ✅ |
| ISO/IEC 42001 | ISO catalogue | Paywalled — keep summary docs as L3 framework picks without redistributing ISO text. | ⚠️ |
| NIST AI RMF | https://www.nist.gov/itl/ai-risk-management-framework | Public domain (US Govt) | ✅ |
| SOC 2 | AICPA | Paywalled | ⚠️ cite without redistributing |
| DORA | EUR-Lex | Public domain | ✅ |
| UK AI Bill (draft) | UK Parliament | Crown copyright; OGL-UK-3.0 | ✅ |
| NIS2 | EUR-Lex | Public domain | ✅ |
| IETF RFCs | https://www.rfc-editor.org | Most have explicit reuse BSD-style | ✅ |

## H. Maps + geospatial

| Source | URL | Licence | Status |
|---|---|---|---|
| OpenStreetMap | https://www.openstreetmap.org | ODbL | ✅ share-alike |
| OpenAddresses | https://openaddresses.io | CC-BY (varies) | TBD |
| Mapbox open data | https://www.mapbox.com/open-source | Various Apache-2.0 / CC0 | TBD |
| EarthGenome | earthgenome.org | CC-BY-4.0 | TBD |

## I. Things to NOT ingest (the "NO" list)

- KEGG (commercial licence required for non-academic)
- any closed-weights API
- any dataset whose licence file cannot be produced as evidence
- anything from a paywall without per-dataset licence confirmation
- anything impersonating public domain that is actually commercial

---

## J. How the corpus is anchored

Every ingested dataset gets one Charter Article binding:

| Charter Article | What goes there |
|---|---|
| Art 6 (L2B) | backends + connectors (Postgres, Mongo, REST adapters) — see `/Users/nicholas/CSOAI/SOVEREIGN-LAYER-ZERO-CHARTER/ref-impl/` |
| Art 7 (L2L) | open-weights LLMs (Qwen3, DeepSeek-R1, OLMo2) |
| Art 5 (mapping) | Every MCP / A2A / ACP / AGNTCY / x402 reference impl above |
| Art 14 (frameworks) | EU AI Act, GDPR, ISO 42001, NIST RMF, SOC2, DORA, UK AI Bill, NIS2 — all summary docs |
| Art 15 (red lines) | NO surveillance / DNA / biothreat / kinetic |
| Art 16 (compute-light) | Qwen3 30B-A3B as canonical reference model |

---

## K. Open items (waiting on subagent 2 to confirm)

1. Final licence commitments per dataset above.
2. SHA-256 of every ingested tarball.
3. Sentinel Hub / Copernicus licence wording exact.
4. Materials Project API rate-limit confirmation.
5. HuggingFace dataset licence verification (some are "other").
6. Chinese public-domain equivalents (CNCB / CNGBdb / Baidu Scholar) licence confirmation.

---