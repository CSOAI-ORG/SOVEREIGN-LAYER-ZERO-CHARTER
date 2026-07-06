# AGNTCY Internet-of-Agents — Interoperability Review Request

**To:** AGNTCY Technical Steering Committee, Linux Foundation
**From:** Nicholas Templeman, CSOAI Ltd (UK 16939677)
**Date:** 2026-07-05
**Subject:** Interop review request — Sovereign Layer Zero Charter v1.0

## Background

AGNTCY was established in 2025 under Linux Foundation governance with Cisco and
other industry leaders as the public agent-registry standard. The Sovereign
Layer Zero Charter v1.0 is complementary and interoperable with AGNTCY
manifests. It does not fork or compete.

## What we propose

1. **AGNTCY manifest → UWE envelope mapping**: any AGNTCY-registered agent can
   wrap its manifest as a UWE `via[0]="agntcy"` payload and emit a SIGIL receipt
   per registry event.

2. **Joint reference implementation**: an Apache-2.0 `agntcy-uwe-bridge` that
   exposes AGNTCY manifests through a Sovereign Layer 0 endpoint, with the
   bridge itself L1/L2/L3 audited.

3. **Cross-recognition of SOVEREIGN-SEAL + AGNTCY Trust Tier**: agents passing
   AGNTCY Level-2 trust may submit evidence toward Sovereign Layer 0 Tier-4
   without re-audit.

## Charter availability

- Canonical URL: https://csoai.org/charters/layer-zero/v1.0
- GitHub: https://github.com/CSOAI/SOVEREIGN-LAYER-ZERO-CHARTER
- License: CC0 1.0 (document), Apache-2.0 (reference implementation)
- SIGIL anchor: H|jeeves|sov3|LAYER-ZERO-CHARTER-v1.0-MINTED-2026-07-05
- OrgKernel L1 custodian: agent-f8c3f34772e0

## Requested outcomes

(a) Co-marketing of AGNTCY + Sovereign Layer 0 as complementary public layers.
(b) AGNTCY SIG review of the UWE-to-AGNTCY mapping table in Article 5.
(c) A joint webinar in Q3 2026.

No representation of endorsement is implied absent a signed letter from the
AGNTCY TSC.
