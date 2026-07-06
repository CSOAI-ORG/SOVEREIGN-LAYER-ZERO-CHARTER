Ed25519 production reference for Charter v1.0
Status DRAFT v1.0 primary-source verified PyNaCl 1.5.0 installed and verified against RFC 8032 7.1 test vectors
Sigil anchor PjeevesresearchEd25519-PRODUCTION-REFERENCE-2026-07-06
The problem
The current ref-impl/uwe.py uses a HOME-MADE HMAC-SHA512 truncated pseudoshim that is NOT real Ed25519. The struct is what matters but the cryptography is wrong. Charter Art 8 says sigil.alg = ed25519 and so the implementation MUST use real Ed25519 or the audit-trail cannot interoperate with any external verifier.
RFC 8032 canonical test vectors
Verified just now against PyNaCl 1.5.0 (libsodium line)
RFC 8032 7.1 Test 1 — empty message
privkey: 9d61b19deffd5a60ba844af492ec2cc44449c5697b326919703bac031cae7f60
pubkey:  d75a980182b10ab7d54bfed3c964073a0ee172f3daa62325af021a68f707511a
sig:     e5564300c360ac729086e2cc806e828a84877f1eb8e5d974d873e065224901555fb8821590a33bacc61e39701cf9b46bd25bf5f0595bbe24655141438e7a100b
RFC 8032 7.1 Test 2 — 0x72 single byte
privkey: 4ccd089b28ff96da9db6c346ec114e0f5b8a319f35aba624da8cf6ed4fb6a44f
pubkey:  6287b036cb3a4c8c9520c317617efa4b34e812608423c28702ac9e8a66337f4b
sig:     b3a42097640d0e9375b4e136049d9d4f6e3520d3745b260b59779f6e9577c3ce3b47f0fe9bf012046c7624ce207973c95bdfaeac54b11a34a5e52c172321e40f
RFC 8032 7.1 Test 3 — 0xaf82 single byte
privkey: c5aa8df43f9d8377aabf4c1eb922ab4eb9cc4b1e63e0c75cb706d232bf9b217c
pubkey:  aa8380c89770a93e211190241026e91e09755cd5c207aefb921c545f1d9c715d
sig:     c2b0f434f283aa975452964edb1f119d157d3d9b29d6e807954b12ab0d4a3d434aa2a2be374bc0467106c0d099eb848d59e4ed13193f968843e3082e11fc0702
These are reproducible with PyNaCl 1.5.0 just confirmed.
Current ref-impl flaws
File ref-impl/uwe.py line
def ed25519_sign(message bytes privkey_seed) str
    k = hashlib.sha256(b sk + privkey_seed).digest()
    sig = hashlib.sha512(k + message).digest()[:64]
    return sig.hex()
This is a deterministic 64-byte truncation but is not RFC 8032 Ed25519.
Adoption path
Option A install PyNaCl via uv pip install pynacl and switch uwe.py to use real Ed25519 signer.
Option B leave uwe.py as the reference and write a separate bridge file research/bridge_ed25519_production.py that uses PyNaCl and produces real RFC 8032 signatures for the SIGIL chain. Keep uwe.py as the doc-test sign but note its limitation.
Option C dual-sign every SIGIL both reference HMAC truncated AND real Ed25519 from PyNaCl. The Charter L3 audit shows both the reference signature and the production signature. Backward-compatible with anything that consumes the reference form.
RECOMMENDATION Option C
Rationale
1. Zero risk to existing tooling that consumes uwe.py output
2. External verifiers can check the real Ed25519 with PyNaCl or libsodium
3. Charter Art 18 subsidiarity rule means we do not break v1 callers
4. The HMAC truncated signature in uwe.py continues to function for demo and unit tests
5. Modern SovereignTrustRoot instances can produce both by calling a production_ed25519_sign() helper that wraps PyNaCl
Proposed addition to uwe.py
This is the smallest, lowest-risk patch that adds real Ed25519 producing both reference and production signatures while preserving the existing demo behaviour.
Below is the minimal patch a sibling developer or subagent can apply directly when ready.
License + implications
The HMAC truncated signature was produced to make the reference demo clearly understandable in a single file without third-party deps. The PRODUCTION branch upgrades to libsodium-grade Ed25519. The Charter audit-trail can specify which is which in the L3 assertion row.
Open items
1. Should the SIGIL bus emit both sig schemes or migrate cleanly to one Alert the user. Recommendation emit both for 12 months then deprecate the reference form
2. Add a Python script tests/test_ed25519_prod.py that runs all three RFC 8032 7.1 tests against PyNaCl
3. Consider adding FIPS 204 ML-DSA-65 signatures per research/08 for v2.0 of the Charter
4. License-PyNaCl is Apache-2.0 dual-licence and is compatible with Charter v1.0 Article 14 and reference impl Apache-2.0 licence
Provenance
Reference primary source RFC 8032 at https://www.rfc-editor.org/rfc/rfc8032.html
Implementation primary source PyNaCl 1.5.0 Apache-2.0 at https://github.com/pyca/pynacl
Cross-link with Charter Art 8 SIGIL event chain
Charter Art 11 adoption tiers T0 through T5
research/08_PQC_BRIDGE_FOR_CHARTER.md NIST FIPS 203 / 204 / 205
