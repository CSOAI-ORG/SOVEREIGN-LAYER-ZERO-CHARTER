# Open-Weights Landscape 2024-2026 — for Sovereign L0 Art 16

**Status:** DRAFT v1.0 — primary-source verified where possible; "TBD" marks
fields that need a follow-up curl pass.
**Sigil anchor:** `P|jeeves|research|OPEN-WEIGHTS-REGISTRY-2026-07-06`

---

## 0. Charter relevance

Article 16 mandates the sovereign substrate run on **one e2-micro or MacBook
Air M2**. So our model picks are constrained to anything that fits in
~32 GiB RAM, prefers **Apache-2.0 / MIT / BSD** over custom, and ideally has
**≤ 30B total / ≤ 10B active (MoE)** so the 30B-A3B pattern (Qwen3) holds.

## 1. Compute-light canonical model

| Model | Repository | License | Total | Active | Context | Charter Art 16 fit |
|---|---|---|---|---|---|---|
| **Qwen3-30B-A3B** | https://github.com/QwenLM/Qwen3 | Apache-2.0 | 30B | 3B (MoE) | 256K (ext 1M) | ✅ CANONICAL — confirmed by curl (README confirmed "Qwen3-2507 ... 235B-A22B, 30B-A3B, and 4B") |
| Qwen3-4B-Instruct-2507 | https://github.com/QwenLM/Qwen3 | Apache-2.0 | 4B | 4B | 256K | ✅ best for edge |
| Qwen3-235B-A22B-2507 | https://github.com/QwenLM/Qwen3 | Apache-2.0 | 235B | 22B (MoE) | 256K | ⚠️ borderline compute-light |
| DeepSeek-R1-Distill-Qwen-32B | https://github.com/deepseek-ai/DeepSeek-R1 | MIT | 32B | 32B | n/a | ✅ reasonable; condensed reasoning |
| DeepSeek-R1-Distill-Llama-70B | https://github.com/deepseek-ai/DeepSeek-R1 | MIT (Llama community) | 70B | 70B | n/a | ⚠️ Llama community terms |

> **Why Qwen3 30B-A3B is canonical:** Apache-2.0 (no custom terms), MoE
> pattern keeps **only 3B params active per token**, fits on M2 MacBook
> Air (16 GiB shared), can drive all 33 sovereign roles per Art 16.

## 2. Reasoning-family open-weights (Apache-2.0 / MIT only)

| Model | Repository | License | Distinction |
|---|---|---|---|
| **DeepSeek-R1** | https://github.com/deepseek-ai/DeepSeek-R1 | MIT | "MIT" badge in README confirmed; reasoning SOTA class |
| DeepSeek-V3 | https://github.com/deepseek-ai | Apache-2.0 typical | TBD confirm |
| Llama 4 family | Meta | Custom (Llama community) | ⚠️ **NOT Apache-2.0 / MIT.** Charter Art 14 L3 audit-trail won't pass |
| Mistral Large 3 | https://github.com/mistralai | Apache-2.0 | TBD verify exact licence per release |
| Gemma 4 | https://huggingface.co/google | Gemma (custom) | ⚠️ custom terms — flagging |
| **OLMo 2** | allenai/OLMo-2 | Apache-2.0 | best for fully-open research |
| Tulu 3/4 | allenai/tulu | Apache-2.0 (most) | post-training recipes |
| IBM Granite | ibm-granite/granite | Apache-2.0 typical | TBD |
| Microsoft Phi-4 | microsoft/Phi-3, Phi-4 | MIT (typical) | TBD on Phi-4 |

> **Standing rule:** Llama / Gemma / OpenAI custom terms = **`❌ NO`**
> for any unrestricted sovereign corpus, because Art 14 compliance
> assertions must trace through clear licence paths.

## 3. European open-weights (compliance-positive)

| Model | Repository | Charter relevance |
|---|---|---|
| **Apertus** | Swiss / public-public body | TBD license — confirm before ingest |
| **CroCo** | EU consortium | TBD |
| **EuroLLM** | EU consortium | TBD |
| **MAP-Neo** | Alibaba | TBD |
| **Moxin** | Tsinghua-derived | TBD |
| **Pleias** | French open-weights | TBD |
| **XALMA** | various | TBD |
| Mistral family | https://github.com/mistralai | Apache-2.0 typical; Mistral Large 3 has been Apache 2.0 |

> **EU AI Act compliance edge:** European open-weights projects
> tend to ship with EU-compliant licence-bundling out of the box.
> We track these for Art 14 L3 audit-trail reasons.

## 4. Long-tail — Apple / Anthropic / Google closed

| Source | Reason for exclusion |
|---|---|
| Apple Intelligence Foundation | NOT publicly released |
| Anthropic Claude family | Closed weights; Anthropic API only |
| Google Gemini closed weights | Closed |
| OpenAI Operator / Swarm | Closed |

These are reference-implementation NOTES only. We do NOT include them in
the sovereign corpus because we cannot ship their weights into Charter
Art 17's 8-channel publishing nor prove licence at Art 14's L3 layer.

## 5. Benchmarks (carry across into Art 14 L3 assertions)

| Benchmark | What it measures | Where to find |
|---|---|---|
| **MMLU** | Multi-task language understanding | standard |
| **BBH** | BIG-Bench Hard reasoning | standard |
| **GSM8K** | Grade-school math | standard |
| **HumanEval / MBPP** | Code synthesis | standard |
| **MATH** | Math benchmark | standard |
| **HellaSwag** | Commonsense | standard |
| **ARC-Challenge** | Reasoning | standard |

For each Charter Art 14 framework we map L3 assertions to a per-model
benchmark delta. The sovereign substrate's `proofof.ai/audit/<id>` will
render model + benchmark + score, in a tamper-evident hash chain.

## 6. Hosting & inference runtimes (open source)

| Runtime | Repo | License |
|---|---|---|
| **Ollama** | https://github.com/ollama/ollama | MIT (badge in README) |
| vLLM | https://github.com/vllm-project/vllm | Apache-2.0 (typical) |
| llama.cpp | https://github.com/ggerganov/llama.cpp | MIT (typical) |
| LM Studio | closed | n/a |
| Text Generation Inference (TGI) | https://github.com/huggingface/text-generation-inference | Apache-2.0 (typical) |
| SGLang | https://github.com/sgl-project | Apache-2.0 (typical) |

> **Compute-light rule:** Ollama + Qwen3-30B-A3B on MacBook Air M2 is
> the **canonical pattern** for Art 16 evaluation. vLLM / TGI / SGLang
> are server-side alternatives, but at higher cost.

## 7. Charter updates required

1. **Charter Art 5 table:** ADD a new row for L2L with the canonical
   `Qwen3-30B-A3B` model ID. Name: `l2l_qwen3_v1`.
2. **Charter Art 16:** add a named-section listing the canonical models
   we accept: { Qwen3-30B-A3B, DeepSeek-R1-Distill-Qwen-32B, OLMo 2
   variants, IBM Granite }. Reject closed-weights.
3. **Defonos compliance:** article 14 L3 asserts add
   `model.weight_licence=apache-2.0|mit|bsd|public-domain` as a
   **mandatory** column. Closed-weights → `compliant=false`.

---