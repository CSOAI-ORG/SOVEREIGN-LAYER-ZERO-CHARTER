# Defence-AI — Article-15-Safe Public Patterns

**Status:** DRAFT v0.3 — first-pass primary-source confirmation.
**Subagent 3/3 grinding. This file is the seed.**
**License:** CC0 1.0 (no copied text — only facts).
**Sigil anchor:** `P|jeeves|research|DEFENSE-PUBLIC-PATTERNS-ARTICLE-15-SAFE-2026-07-06`

**CRITICAL — read first.** This file lists ONLY patterns and tooling that are
**Article-15 safe** under the Sovereign Layer Zero Charter v1.0.

> **Charter Article 15 — Immutable Red Lines:**
> ❌ NO kinetic-targeting patterns (strike package / find-fix-finish / kill order)
> ❌ NO personal-surveillance patterns (face-rec, phone-locate, individual-tracking)
> ❌ NO AUKUS / DAIC accreditation claim without signed letter
> ❌ NO DEFONEOS-SEAL without 33-agent BFT quorum
> ❌ NO DSEI booth without UK-prime pilot letter
> ❌ NO `defonos.io` domain (known trap)

**Anything below the line that crosses a red line is excluded by design.
Anything above is what we should study.**

---

## 1. Allowed-streams — what survives Article 15

Three categories pass:

1. **Government open-source that is public** (NASA, AFRL, DARPA, Code.mil).
2. **Compliance + audit + risk-management code** (FedRAMP-style tooling,
   OSCAL, NIST 800-53 evidence generators).
3. **Defence-government procurement / public-domain textual sources**
   (JKO, NATO, CISA, NIST doc bodies).

What is **not** covered: weapons targeting, person-tracking,
psychographic targeting of individuals, autonomous-release systems.

---

## 2. Government open source — verifiable public

| Source | URL | Licence | Status |
|---|---|---|---|
| Code.mil (US DoD OSS) | https://code.mil | Various open | TBD verify per repo |
| GoCodeSF (Space Force) | https://github.com/ussf-go | Various open | TBD |
| AFRL open source | varies | Various open | TBD |
| DARPA programs public repo | varies | Various open | TBD |
| NASA open source | https://github.com/nasa | Various Apache-2.0 + NASA-public | ✅ |
| DARPA AIDO program docs | public reports | Public-domain | ✅ |
| DARPA AIMHEALTH docs | public reports | Public-domain | ✅ |
| DARPA L2M docs | public reports | Public-domain | ✅ |

> **Action:** subagent to catalogue each public DoD OSS repo with
> exactly which Charter Art 15 red lines it does NOT cross.

## 3. Compliance + audit-tooling open-source

| Tool | URL | Licence | Charter Article |
|---|---|---|---|
| OSCAL — Open Security Controls Assessment Language | https://pages.nist.gov/OSCAL | Public domain (US Govt) | Art 9 / Art 14 |
| Compliance-trestle | https://github.com/IBM/compliance-trestle | Apache-2.0 | Art 14 |
| OSCAL-CLI | (IBM + community forks) | Apache-2.0 | Art 14 |
| NIST 800-53 catalog | https://csrc.nist.gov | Public domain | Art 14 |
| OpenControl | https://github.com/opencontrol | Apache-2.0 | Art 14 |
| Compliant Framework | https://www.compliantframework.com | CC-BY-SA-3.0 | Art 14 |
| NIST CSF 2.0 references | https://www.nist.gov/cyberframework | Public domain | Art 14 |
| SDP Toolkit (FedRAMP) | https://github.com/FedRAMP | Apache-2.0 | Art 14 |
| OWASP CycloneDX SBOM | https://github.com/CycloneDX | Apache-2.0 | Art 14 |
| SPDX | https://spdx.dev | CC-BY / Apache-2.0 | Art 14 |
| Sigstore (sig + key signing) | https://www.sigstore.dev / https://github.com/sigstore | Apache-2.0 | Art 8 (SIGIL adjacent) |
| in-toto (supply-chain integrity) | https://in-toto.io | Apache-2.0 | Art 8 |

> Notice how **none** of these tools have person-targeting or
> kinetic-targeting use — only compliance, audit, supply-chain.
> **These are exactly what Charter Article 15 permits us to study.**

## 4. Sovereign / national-security-adjacent open source

| Tool | URL | Licence | Charter-relevant | Red-line check |
|---|---|---|---|---|
| OpenSSF Scorecard | https://github.com/ossf/scorecard | Apache-2.0 | Supply-chain audit | ✅ |
| OpenSSF Best Practices Badger | https://github.com/coreinfrastructure/best-practices-badge | MIT | Repo hygiene | ✅ |
| OWASP ZAP | https://github.com/zaproxy/zaproxy | Apache-2.0 | Web-app audit | ✅ |
| OWASP Dependency-Check | https://owasp.org/www-project-dependency-check/ | Apache-2.0 | Vuln audit | ✅ |
| OWASP SAMM | https://owasp.org/www-project-samm/ | CC-BY-SA-3.0 | Assurance model | ✅ |
| MITRE ATT&CK (technique taxonomy) | https://attack.mitre.org | Permissive re-use | Article-14 framework | ✅ (taxonomy, not weapon) |
| MITRE Caldera | https://github.com/mitre/caldera | Apache-2.0 | ATT&CK emulation | ⚠️ STUDY NOT DEPLOY — verify red line |
| Atomic Red Team | https://github.com/redcanaryco/atomic-red-team | MIT | Adversary emulation | ⚠️ STUDY NOT DEPLOY — verify red line |
| MITRE D3FEND | https://d3fend.mitre.org | Public-domain | Defensive taxonomy | ✅ |
| CISA KEV | https://www.cisa.gov/known-exploited-vulnerabilities | Public domain | Vuln intel | ✅ |
| CVE / NVD | https://nvd.nist.gov | Public domain | Vuln intel | ✅ |
| OpenCTI | https://github.com/OpenCTI-Platform/opencti | Apache-2.0 | Threat intel platform | ⚠️ STUDY deployment per Art 15 |

> **Article 15 check on every item above.** Anything with red-line
> risk is gated to "study, not deploy". Anything without is fair
> game.

## 5. Government procurement + policy docs (public)

| Source | URL | Licence | Charter Article |
|---|---|---|---|
| USAGov SAM.gov public API | https://sam.gov | Public domain | Art 17 |
| DoD CDAO | https://cdao.mil | Public domain | (study only) |
| UK Cabinet Office GOV.UK | https://www.gov.uk | OGL-UK-3.0 | Art 17 |
| NATO STANAG (public portions) | https://www.nato.int | Public documents | (study only) |
| CISA | https://www.cisa.gov | Public domain | Art 14 |
| CNCF (compliance profiles) | https://www.cncf.io | Apache-2.0 for spec | Art 14 |
| OpenSSF | https://openssf.org | Apache-2.0 | Art 14 |

## 6. Defence-AI NOT to study (the "NO" list)

Anything that has any of:
- Closed-source weapons-targeting code.
- Person-tracking surveillance code.
- Crew-served weapon release without human-in-loop.
- Autonomous kill-decision-making stack (Article 15.
  crosses the kinetic + the kill-decision line both).
- Anything sold specifically as "find-fix-finish".
- Any product named or described as a `defonos.io` (known trap).
- Any AUKUS / DAIC accreditation claim without signed letter on file.

## 7. Chinese public-domain equivalents (STUDY-ONLY)

> Charter Article 15 is symmetric: red lines apply equally whether
> the source is China, the US, the UK, or anywhere else.

| Source | URL | Licence | Red-line check |
|---|---|---|---|
| CNCB (China National Center for Bioinformation) | https://www.cncb.ac.cn | Public-domain + CC-BY | ✅ biology |
| CNGBdb (China National GeneBank) | https://db.cngb.org | Public-domain + CC-BY | ✅ biology |
| CNKI (China National Knowledge Infrastructure) | https://www.cnki.net | Mix — paywall for most content | ⚠️ Cite, don't ingest |
| Baidu Scholar (中文) | https://xueshu.baidu.com | Indexes public-domain | ✅ |
| Wanfang Data | https://www.wanfangdata.com.cn | Mix | ⚠️ Cite, don't ingest |
| Tsinghua AIR group releases | (verify per release) | Varies | TBD |

## 8. Strategic-studies schools (Article-15 informational only)

> These are policy schools, not weapons-software vendors. Studying
> their public frameworks is permitted; deploying anything against
> persons is not.

| Group | URL | Purpose | Red-line |
|---|---|---|---|
| RAND Corp public papers | https://www.rand.org | Policy papers | ✅ (documents only) |
| RUSI | https://rusi.org | Strategy papers | ✅ |
| CSIS | https://www.csis.org | Policy papers | ✅ |
| IISS | https://www.iiss.org | Strategic analysis | ✅ |
| Chatham House | https://www.chathamhouse.org | Policy | ✅ |
| Carnegie Endowment | https://carnegieendowment.org | Policy | ✅ |

---

## 9. How compliance+audit tooling maps to Charter Articles

| Charter Article | Allowed source |
|---|---|
| Art 8 (SIGIL event chain) | Sigstore, in-toto |
| Art 9 (OrgKernel L1/L2/L3) | OSCAL schema, compliance-trestle |
| Art 14 (8-framework profile) | NIST 800-53, OWASP SAMM, OpenSSF Scorecard |
| Art 15 (red lines) | MITRE ATT&CK (taxonomy only), MITRE D3FEND |
| Art 17 (8-channel publish) | GOV.UK (OGL-UK-3.0), SAM.gov (public domain) |

---

## 10. Open items (waiting on subagent 3 to confirm)

1. Per-vendor public-source matrix (Palantir / Anduril / Helsing /
   Rebellion etc.) — not researched yet.
2. Exact Apache-2.0 / MIT / BSD tags for each gov-open repo.
3. SHA-256 of every artifact we ingest.
4. CDAO and DARPA public OSS check.
5. NATO public OSS check.
6. Indian MOD / DRDO OSS check (where public).

When subagent 3 returns: row-by-row fill.

---