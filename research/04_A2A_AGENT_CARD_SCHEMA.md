# A2A Agent Card schema — primary-source verified

**Status:** DRAFT v1.0 — verified against canonical sources.
**Sigil anchor:** `P|jeeves|research|A2A-AGENT-CARD-SCHEMA-VERIFIED-2026-07-06`

---

## 0. UPDATE TO `01_AGENT_INTEROP_FRONTIER.md`

**CORRECTION:** `01` listed `a2a-mesh/a2a` as the A2A Apache mirror. **Wrong.**
The canonical home is **`a2aproject/A2A`** at https://github.com/a2aproject/A2A
(Apache-2.0). Google originally launched the protocol; the canonical Apache
mirror today is under `a2aproject`. The Python reference SDK is
`a2aproject/a2a-python`. The Go SDK is `a2aproject/a2a-go`. Etc.

Sir Nick: please remove the `a2a-mesh/a2a` line from
`research/01_AGENT_INTEROP_FRONTIER.md` and replace with the table below.

---

## 1. Primary sources (curl-verified)

| Field | Value | URL | Verified |
|---|---|---|---|
| Canonical spec URL | https://a2a-protocol.org/v1.0.0/specification/ | yes |
| Markdown of the spec | https://raw.githubusercontent.com/a2aproject/A2A/main/docs/specification.md | ✅ 200, full file fetched |
| Apache-2.0 repo | https://github.com/a2aproject/A2A | ✅ Apache-2.0 badge in README |
| Python SDK | https://github.com/a2aproject/a2a-python | ✅ Apache-2.0 badge |
| PyPI | https://pypi.org/project/a2a-sdk/ | ✅ Apache-2.0 |
| Spec version | **1.0** (with 0.3 compat) | ✅ stated in a2a-python README |
| Transport options | **JSON-RPC, HTTP+JSON/REST, gRPC** | ✅ confirmed in a2a-python README |
| Compatibility table | `1.0 × JSON-RPC / HTTP+JSON / gRPC` | ✅ all three ✅ |

## 2. AgentCard JSON shape (verbatim from spec § 4.4.1)

```json
{
  "name": "Research Assistant Agent",
  "description": "AI agent for academic research and fact-checking",
  "supportedInterfaces": [
    {
      "url": "https://research-agent.example.com/a2a/v1",
      "protocolBinding": "HTTP+JSON",
      "protocolVersion": "0.3"
    }
  ],
  "capabilities": {
    "streaming": false,
    "pushNotifications": false,
    "extensions": [
      {
        "uri": "https://standards.org/extensions/citations/v1",
        "description": "Provides citation formatting and source verification",
        "required": false
      }
    ]
  },
  "defaultInputModes": ["text/plain"],
  "defaultOutputModes": ["text/plain"],
  "skills": [
    {
      "id": "academic-research",
      "name": "Academic Research Assistant",
      "description": "Provides research assistance with citations",
      "tags": ["research", "citations", "academic"],
      "examples": ["Find peer-reviewed articles on climate change"],
      "inputModes": ["text/plain"],
      "outputModes": ["text/plain"]
    }
  ]
}
```

## 3. Field-by-field MANDATORY vs OPTIONAL

| Field | Required | Charter mapping |
|---|---|---|
| `name` | **MANDATORY** | `audit.l1_identity` display label |
| `description` | **MANDATORY** | `audit.l3_compliance: eu-ai-act, Art 50` transparency |
| `supportedInterfaces` | **MANDATORY** (at least one) | `via[0]="a2a"` UWE field |
| ↳ `url` | **MANDATORY** | endpoint binding |
| ↳ `protocolBinding` | **MANDATORY** | `JSON-RPC` / `HTTP+JSON` / `gRPC` |
| ↳ `protocolVersion` | **MANDATORY** | e.g. `"0.3"`, `"1.0"` |
| `capabilities` | OPTIONAL but recommended | `policy` block in UWE |
| ↳ `streaming` | OPTIONAL | `L2_execution` correlation |
| ↳ `pushNotifications` | OPTIONAL | `L2_execution` async |
| ↳ `extensions` | OPTIONAL (drives v2.0+ hook) | Art 5 extensibility |
| `defaultInputModes` | RECOMMENDED | `input_schema` for L2B |
| `defaultOutputModes` | RECOMMENDED | `output_schema` for L2B |
| `skills` | OPTIONAL | Charter Art 5 capability graph |
| `securitySchemes` | OPTIONAL (recommended in prod) | `policy` security block |
| `security` | OPTIONAL | Tied to securitySchemes |
| `signatures` | OPTIONAL (AgentCardSignature) | **Charter Art 8 SIGIL fill-in** |
| `provider` | OPTIONAL (AgentProvider) | Care-floor ties to org |

## 4. Transport bindings (the three real ones)

From `a2aproject/a2a-python/README.md` compatibility table:

| Spec ver | Transport | Client | Server |
|---|---|:---:|:---:|
| **1.0** | **JSON-RPC** | ✅ | ✅ |
| **1.0** | **HTTP+JSON/REST** | ✅ | ✅ |
| **1.0** | **gRPC** | ✅ | ✅ |
| 0.3 (compat) | JSON-RPC | ✅ | ✅ |

> **Charter integration:** the UWE `via[0]="a2a"` payload is the A2A
> envelope. **Transport selection** is a negotiation between the
> client and server at L3 of the A2A stack (per the spec's
> 3-layer model). The sovereign substrate defaults to JSON-RPC
> for thin clients, promotes HTTP+JSON for browser-based agents,
> and uses gRPC when transporting SLIM (AGNTCY).

## 5. Signatures (the Charter's SIGIL fit-in)

A2A defines `AgentCardSignature` for cryptographically signed cards. **This
is where the Sovereign Layer 0 Charter's SIGIL bus slots in:** a server can
sigil-anchor its A2A AgentCard into the unified hash chain (Charter Art 8 +
Art 4). Once a subagent ingests the A2A cardinality:

- emit one SIGIL receipt per `sign` op on AgentCard boot,
- hash-chain it onto the realm's prior head,
- the L3 assertion in `proofof.ai/audit/<exec_id>` shows the AgentCard
  signature + SIGIL digest together.

## 6. Operations that survive under our `via[0]="a2a"`

(From spec § 3.1 / python SDK compatibility)

1. `SendMessage`  2. `SendStreamingMessage`  3. `GetTask`
4. `ListTasks`  5. `CancelTask`  6. `GetAgentCard`
7. `GetExtendedAgentCard` (optional)
8. `SubscribeToTask`  9. `PushNotificationConfig`

All of these bind into the UWE envelope as a single request, with one
SIGIL receipt per request-response round-trip.

## 7. Provenance (Charter Art 18)

> "Where the Sovereign Layer Zero Charter v1.0 is silent, the vendor protocol
> controls." For A2A, the spec at a2a-protocol.org governs wire behaviour;
> the Charter's UWE merely subsumes the surface to emit one SIGIL receipt.

## 8. Open items

- SPDX 0.3 → 1.0 migration guide at
  https://github.com/a2aproject/a2a-python/blob/main/docs/migrations/v1_0/README.md
  not yet curl-verified.
- The CANONICAL JSON schema (built from spec/a2a.proto) is dynamically
  generated per spec; pin to proto as normative source per §1.4.
- Future Charter amendment Art 5 should ADD a row that the `signatures` field
  of A2A AgentCards MUST be a Sovereign STR §25519 signature chainable to
  one SIGIL receipt.

---