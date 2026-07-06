# W3C DID Working Group — Namespace Submission

**To:** W3C DID Working Group Chairs
**From:** Nicholas Templeman, CSOAI Ltd (UK 16939677)
**Date:** 2026-07-05
**Subject:** Decentralized Identifier namespace `did:csoai` registration request

## Background

`did:csoai` is the method-namespace reserved for identifiers issued by CSOAI Ltd
under the Sovereign Layer Zero Charter v1.0. Conforming identifiers use:

```
did:csoai:<agent-or-human-name>
```

The Charter's Article 3.2 (Sovereign Trust Root Namespacing) defines four
sub-namespaces:

| Prefix | Reserved to |
|---|---|
| `did:csoai:human:` | Verified human (eIDAS / Apple / GOV.UK Verify) |
| `did:csoai:eurnet:` | EU data-residency-bounded agents |
| `did:csoai:auknz:` | Australia / NZ AUKUS-compatible |
| `did:csoai:` (default) | Public layer |

## Cryptographic binding

All `did:csoai:` identifiers are bound to a 32-byte Ed25519 public key. The
verification method is `Ed25519VerificationKey2020` (W3C CCG-2020).

## Examples

- `did:csoai:nicholas-001` — author of the Charter
- `did:csoai:eurnet:sovereign-agent-alpha` — EU-residency agent
- `did:csoai:auknz:defence-sovereign-council` — AUKUS-compatible

## Public verification endpoint

Any DID resolves via `https://csoai.org/did/<method-specific-id>` returning a
W3C-format DID document. Live audit-trail: `proofof.ai/audit/<did>`.

## License

Specification: CC0 1.0.
Reference DID resolver (Apache-2.0) bundled with the Charter reference impl.

## Request

Inclusion of `did:csoai` in the W3C DID Method Registry, alongside the existing
methods (`did:key`, `did:web`, `did:ion`, `did:jwk`, etc.). All Charter
implementation details at https://github.com/CSOAI/SOVEREIGN-LAYER-ZERO-CHARTER.
