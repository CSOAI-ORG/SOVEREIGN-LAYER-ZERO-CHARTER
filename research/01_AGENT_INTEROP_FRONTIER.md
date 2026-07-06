# Agent-Interop Frontier 2024-2026 — verified primary sources

**Status:** DRAFT v0.3 — first-pass primary-source confirmation.
**Subagent 1/3 is grinding full audit. This file is the seed; final will replace it.**
**License:** CC0 1.0 (no copied text from primary sources — only citations + facts).
**Sigil anchor:** `P|jeeves|research|AGENT-INTEROP-FRONTIER-PRIMARY-CONFIRMED-2026-07-06`

**Purpose:** Anchor every Charter Article 5 protocol and its neighbour
frameworks to a primary source URL. No re-derivation. If a fact is here,
do not re-research. If a fact is missing, ping jeeves.

---

## 1. MCP — Model Context Protocol

| Field | Value | Source |
|---|---|---|
| Spec schema | `schema/2025-11-25/schema.ts` (.ts first, .json mirror) | https://github.com/modelcontextprotocol/modelcontextprotocol — README confirmed |
| Docs | modelcontextprotocol.io (Mintlify) | https://modelcontextprotocol.io |
| License | MIT | https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/LICENSE |
| Authorship | David Soria Parra, Justin Spahr-Summers | README confirmed |
| Charter Article | **Art 5 — maps "mcp" via[0]** | /Users/nicholas/CSOAI/SOVEREIGN-LAYER-ZERO-CHARTER/CHARTER.md |
| Notes | Pin to schema dated 2025-11-25 (latest stable). Watch v2 quarterly. | — |

## 2. A2A — Agent-to-Agent (Google + Linux Foundation, 2025)

| Field | Value | Source |
|---|---|---|
| Canonical repo | `a2aproject/A2A` (Apache-2.0) | https://github.com/a2aproject/A2A — verified by curl |
| Reference site | https://a2a-protocol.org | curl OK (redirects to /latest/) |
| Spec canonical | https://a2a-protocol.org/v1.0.0/specification/ | markup rendered from `a2aproject/A2A/docs/specification.md` |
| Spec source-of-truth | https://raw.githubusercontent.com/a2aproject/A2A/main/docs/specification.md | curl OK |
| Apache-2.0 badge | YAML front-matter README | ✅ |
| Spec version | **1.0** | stated in a2a-python README, +0.3 compat |
| Transport options | **JSON-RPC · HTTP+JSON/REST · gRPC** (all three are 1.0-compatible per a2a-python README) | ✅ confirmed |
| Python SDK | `a2aproject/a2a-python` (Apache-2.0) | https://github.com/a2aproject/a2a-python |
| Other SDKs | `a2aproject/a2a-{go,dotnet,js,java,rs,itk,samples,tck}` | confirmed via github.com/a2aproject |
| IANA / IETF draft | Not yet at IANA; under LF incubation | TBD |
| AGNTCY binding | `agntcy/slim-a2a-python` (SLIM transport for A2A) | https://github.com/agntcy/slim-a2a-python |
| Charter Article | **Art 5 — maps "a2a" via[0]** + **Art 8 (signatures slot)** | CHARTER.md |
| Verbatim AgentCard JSON | See `research/04_A2A_AGENT_CARD_SCHEMA.md` section 2 | updated 6 Jul 2026 |

> **CORRECTION** (logged 6 Jul 2026 during gogogo sprint):
> The `a2a-mesh/a2a` mirror is **NOT** canonical. The Apache-2.0
> canonical home is `a2aproject/A2A`. Spec is published at
> `https://a2a-protocol.org/v1.0.0/specification/` and rendered
> from `a2aproject/A2A/docs/specification.md`. Verified end-to-end
> with curl just now — see `research/04_A2A_AGENT_CARD_SCHEMA.md`
> for the full corrective log.

## 3. ACP — IBM Research "Agent Communication Protocol"

| Field | Value | Source |
|---|---|---|
| Research blog | https://research.ibm.com/blog/agent-communication-protocol | 404 at curl time |
| Practical definition | REST-native agent messaging | per our Charter Art 5 |
| Charter Article | **Art 5 — maps "acp" via[0]** | CHARTER.md |
| Status | IBM has not (yet) shipped an OSS reference kit at the URL above. The Charter's ACP envelope definition is the live canonical until IBM publishes reference. | — |

## 4. AGNTCY — Linux Foundation / Cisco / Outshift, 2025

| Field | Value | Source |
|---|---|---|
| Org | agntcy (LF/Cisco/Outshift) | https://github.com/agntcy |
| Manifest schema | OASF (Open Agentic Schema Framework) | https://github.com/agntcy/oasf — Apache-2.0? (Apache-2.0 confirmed) |
| Transport | SLIM (Secure Low- Latency Interactive Messaging) | https://github.com/agntcy/slim — Apache-2.0 |
| SLIM-to-A2A | `agntcy/slim-a2a-python` | confirmed in slim README |
| SLIM-to-MCP | `agntcy/slim-mcp-python` | confirmed in slim README |
| SLIM-bindings | Python / Go / .NET / Java / Kotlin | https://github.com/agntcy/slim-bindings |
| Docs | https://docs.agntcy.org (rendered) | curl OK |
| Schema site | https://schema.oasf.outshift.com | curl OK |
| Charter Article | **Art 5 — maps "agntcy" via[0]** (manifest-as-envelope) | CHARTER.md |
| Subsumes | Charter is compatible, NOT a fork. SLIM is the transport we run UWE on. | — |

## 5. x402 — Coinbase / x402 Foundation

| Field | Value | Source |
|---|---|---|
| Old repo | coinbase/x402 (now a dev fork) | https://github.com/coinbase/x402 README confirmed |
| New canonical | x402-foundation/x402 | https://github.com/x402-foundation/x402 |
| License | MIT (per Coinbase OSS convention; verify) | coinbase/x402 README |
| SKD | `@x402/core` + `evm`, `svm`, `stellar`, plus `axios`, `fastify`, `fetch`, `express`, `hono`, `next`, `paywall`, `extensions` | coinbase/x402 README |
| Charter Article | **Art 5 — maps "x402" via[0]** | CHARTER.md |

## 6. Microsoft Agent Framework (MAF) — successor to AutoGen

| Field | Value | Source |
|---|---|---|
| Repo | microsoft/agent-framework | https://github.com/microsoft/agent-framework |
| Status | Production v1.0 (replaces AutoGen) | README confirmed |
| License | MIT | inferred badge |
| Support | A2A + MCP interop built-in | README confirmed |
| Charter Article | **Art 5 — maps "mcp" and "a2a" via[0]** (cross-language bind) | CHARTER.md |
| AutoGen | maintenance mode → migrate to MAF | README confirmed |

## 7. Microsoft AutoGen (legacy)

| Field | Value | Source |
|---|---|---|
| Repo | microsoft/autogen | https://github.com/microsoft/autogen |
| Status | **Maintenance mode.** Banner at top of README. | confirmed |
| Action | DO NOT fork AutoGen for new work. Use MAF. | — |
| Charter Article | n/a (do not redup) | — |

## 8. LangGraph (LangChain)

| Field | Value | Source |
|---|---|---|
| Repo | langchain-ai/langgraph | https://github.com/langchain-ai/langgraph |
| License | MIT | badge confirmed |
| Positioning | Low-level orchestration for stateful agents | README confirmed |
| Charter Article | **Art 11 T2+** (adoption tier ladder) | CHARTER.md |

## 9. CrewAI

| Field | Value | Source |
|---|---|---|
| Repo | crewAIInc/crewAI | https://github.com/crewAIInc/crewAI |
| License | MIT | inferred |
| Open source | Yes (with cloud trial upsell) | README |
| Charter Article | **Art 11 T2+** | CHARTER.md |

## 10. HuggingFace SmolAgents

| Field | Value | Source |
|---|---|---|
| Repo | huggingface/smolagents | https://github.com/huggingface/smolagents |
| License | Apache-2.0 | badge confirmed |
| Docs | https://huggingface.co/docs/smolagents | README |
| Charter Article | **Art 11 T2+** | CHARTER.md |

## 11. Qwen3 — open weights (CC0-equivalent / Apache)

| Field | Value | Source |
|---|---|---|
| Repo | QwenLM/Qwen3 | https://github.com/QwenLM/Qwen3 |
| License | Apache 2.0 (typical for Qwen) | check LICENSE |
| Sizes (Qwen3-Instruct-2507) | 235B-A22B, 30B-A3B, 4B | README confirmed |
| Long-context | 256K, extendable to 1M | README confirmed |
| Compute-light doctrine | **Qwen3 30B-A3B = 3B active = runs on M2 MacBook Air** | matches Charter Art 16 |
| Charter Article | **Art 16 Compute-light** (canonical model) | CHARTER.md |

## 12. DeepSeek R1 — open weights (MIT)

| Field | Value | Source |
|---|---|---|
| Repo | deepseek-ai/DeepSeek-R1 | https://github.com/deepseek-ai/DeepSeek-R1 |
| License | MIT | LICENSE badge |
| Variants | R1-Zero, R1, six distilled (Llama + Qwen) | README confirmed |
| Paper | DeepSeek_R1.pdf | README |
| Charter Article | **Art 14 frameworks** (open-weights benchmark reference) | CHARTER.md |

## 13. Stripe AI — MCP server + Stripe-hosted

| Field | Value | Source |
|---|---|---|
| Repo | stripe/agent-toolkit | https://github.com/stripe/agent-toolkit |
| Stripe MCP server | mcp.stripe.com (OAuth) | README confirmed |
| Status | Backup for our old Stripe account — Stripe's own MCP server works without depending on acct verification. | — |
| Charter Article | **Art 5** — could slot in as an MCP server in `via[0]="mcp"` payload. | CHARTER.md |

---

## 14. Open items (waiting for subagent 1 + browser refresh)

1. Exact IBM ACP repo URL (if OSS at all).
2. Canonical A2A Apache mirror — `a2a-mesh` vs Google's own.
3. License of OSS Qwen weights — Apache-2.0 inferred, confirm.
4. Latest x402-Foundation license (MIT or Apache-2.0).
5. Adobe / Microsoft Magentic-One license + repo.
6. OpenAI Operator / Swarm repo (likely closed).
7. DeepMind AlphaAgents (likely closed).
8. Tencent Yuanbao / Baidu AppBuilder / Moonshot Kimi public repo status.
9. ByteDance/doubao agent framework license.
10. Latest AGNTCY SIG (Special Interest Group) charter — when chartered.

When subagent returns, item-by-item confirm + add SHA-256 to each row.

---
