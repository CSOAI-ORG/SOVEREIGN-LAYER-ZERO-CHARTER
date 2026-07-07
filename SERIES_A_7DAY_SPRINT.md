# 7-DAY SERIES A SPRINT — Master Plan
## "30 days compressed into 7. End users. Signups. Real E2E. No loops."

**Date minted:** 2026-07-07 04:17 UTC
**Owner:** Nicholas Templeman (CSOAI Ltd, UK 16939677)
**Sprint lead:** JEEVES (M4-Hermes)
**Charter anchor:** `df65a6585cf6a686cbfd881f56c04447056e2551e7c04db57a80543521022054`
**Sigil anchor:** `H|jeeves|sov3|SERIES-A-SPRINT-KICKOFF-2026-07-07T04:17Z`

---

## 0. NORTH STAR

By **T+7d (Mon 13 Jul 2026)**:

1. **csoai.org + sovereign-layer-zero landing pages are LIVE with measured, growing traffic**
2. **/api/signup is end-to-end LIVE** — every signup is sigil-anchored to the Charter
3. **/api/assess is wired to the actual sovereign AI model** with all 12 mind-sets + all 30 MCPs + 100 tools
4. **A real person in a real jurisdiction has run a real audit and signed a real passport** that was accepted by a real auditor
5. **The first £999 has been billed** and the first £199/mo is recurring
6. **The 7-day EAT-mode runs are running** — every overnight cycle is doing the work that would normally take a month
7. **Daily numbers**: 100+ signups, 1,000+ Article 50 passports issued, 1+ £999 sale

**If this happens, Series A is funded by Aug 2 2026 (the EU AI Act deadline).**

---

## 1. PHASE STRUCTURE (7 days, 7 phases)

| Day | Phase | Goal | Output | EAT-mode cycles |
|---|---|---|---|---|
| **D1 (Tue 7 Jul)** | WIRE | Connect the sovereign model to the live API. 30 MCPs bound. | `/api/assess` returns real signed passport using real Qwen3-30B-A3B + all 12 mind-sets. | EAT-1: `bind-model-to-api` |
| **D2 (Wed 8 Jul)** | VISUALLY E2E | Browser-verifiable audit trail. 8 personas, 12 industries, 4 jurisdictions. | Landing pages for all 8 personas. 12 industry landing pages. 4 jurisdictional landing pages. | EAT-2: `persona-launch` + `industry-pages` + `jurisdiction-pages` |
| **D3 (Thu 9 Jul)** | SIGN-UPS | Wire Stripe live + first £999 sale + first 1,000 free signups. | Stripe live mode enabled (Sir action). £999 Payment Link sent to 3 warm targets. Free tier at 1,000 signups. | EAT-3: `signup-funnel` + `first-1000` |
| **D4 (Fri 10 Jul)** | SIGIL-CHAIN | Public audit-trail page + first 10K sigil receipts published. | `proofof.ai/audit/<id>` is browser-verifiable. 10,000 receipts emitted across the chain. | EAT-4: `public-audit` + `sigil-scale` |
| **D5 (Sat 11 Jul)** | MULTI-MIND | All 12 mind-sets wired into the API. Test outputs against 8 personas. | `/api/assess?mindset=...` returns 12 distinct responses per input. | EAT-5: `twelve-mindsets-live` |
| **D6 (Sun 12 Jul)** | DISTRIBUTE | All Charter / 30 MCPs / 8 personas / 12 industries / 4 jurisdictions distributed across 5 social platforms + 50 cold emails. | Twitter/X thread (8 posts), LinkedIn (5 posts), Reddit (10 subs), 50 cold emails to 50 enterprise targets. | EAT-6: `distribute-everywhere` |
| **D7 (Mon 13 Jul)** | MEASURE | Real metrics. Close the loop. Set Series A term sheet. | 100+ signups/day, 1,000+ passports/day, 1+ £999 sale. Series A target raised. | EAT-7: `measure-and-pivot` |

---

## 2. THE 8 PERSONAS (end users, all demographics, all mindsets)

**Why personas:** "end user" is too vague. We ship a landing page PER persona, each with its own A/B headline, its own A/B hero CTA, its own A/B social proof, its own A/B pricing display.

| # | Persona | Industry | Jurisdiction | Primary pain | Sovereign promise | Landing-page angle |
|---|---|---|---|---|---|---|
| 1 | **CTO, scale-up SaaS, EU** | SaaS | DE/EU | EU AI Act Aug 2 deadline | "Sign in 30 sec. Article 50 passport issued in 9 min. Free." | "30 days to deadline — start now" |
| 2 | **CISO, mid-cap fintech, US** | Fintech | US/NY | CFPB AI guidance, NY LL 144 | "SOC 2 + NIST RMF + state-by-state, audit-ready" | "Pass the regulator's test the first time" |
| 3 | **Head of Compliance, hospital chain, EU** | Health | DE/UK | EU AI Act + MDR + GDPR Art 9 | "Article 50 + GDPR Art 9 (special categories), signed" | "Hospital-grade AI, hospital-grade audit" |
| 4 | **VP Risk, global bank, UK** | Banking | UK | PRA SS2/23 + EU AI Act | "Three lines of defense, signable, browser-verifiable" | "PRA-ready by next quarter" |
| 5 | **ML Lead, health-tech startup, US** | Health-tech | US/CA | FDA SaMD + HIPAA | "FDA SaMD + HIPAA + SOC 2, one passport" | "FDA SaMD in 9 minutes" |
| 6 | **Policy Director, central bank, AU** | Sovereign | AU | AUKUS + AU AI Bill | "Sovereign-by-design, no AUKUS claim without signed letter" | "Sovereign with sovereignty" |
| 7 | **CISO, defence prime contractor, UK** | Defence | UK | JSP 936 + UK AI Bill | "JSP 936 + Article 15 red lines + Article 14 audit" | "JSP 936 without the hall pass" |
| 8 | **Indie developer, AI side project, anywhere** | Indie | Anywhere | "Will my AI kill me legally?" | "Free tier, 3 passports/day, CC0 forever" | "For the indie in a hurry" |

**Each persona gets:** a landing page, a 1-line social proof, a CTA variant, an industry-specific sub-page, a jurisdiction-specific overlay.

---

## 3. THE 12 MIND-SETS (modeling thinking modes)

**Why mind-sets:** a single model is one lens. We ship 12 — each optimised for one thinking mode. Users pick the mind-set at `/api/assess?mindset=...`. The default is the meta-mind-set (1, 2, 3, 6, 9, 12 averaged — closes 80% of cases).

| # | Mind-set | Use case | Sovereign model | Output |
|---|---|---|---|---|
| 1 | **Forensic** | EU AI Act Art 50 watermarking | Qwen3-30B-A3B + Forensic prompt | Tamper-evident JSON-LD receipt |
| 2 | **Risk-classifier** | EU AI Act Art 6 / Annex III risk tier | + Risk-classifier prompt | "high-risk" / "limited-risk" / "minimal-risk" |
| 3 | **Human-oversight planner** | Art 14 | + Human-oversight prompt | 9-layer HITL plan, JSON |
| 4 | **Bias / fairness** | Art 10 | + Bias prompt | Quantitative fairness score per demographic |
| 5 | **Cybersecurity** | Art 15 | + Cybersecurity prompt | Threat-model + mitigations JSON |
| 6 | **GDPR cross-walk** | Art 6/9/17/22/30/32/35 | + GDPR prompt | Per-article machine-checked assertions |
| 7 | **ISO 42001 AIMS** | A.5-A.10 | + ISO 42001 prompt | AIMS-control-level mapping |
| 8 | **NIST AI RMF** | Map/Measure/Manage/Govern | + NIST RMF prompt | RMF-category-level mapping |
| 9 | **SOC 2 TSC** | CC1-CC9 | + SOC 2 prompt | TSC-criterion-level mapping |
| 10 | **DORA RTS** | RTS for AI | + DORA prompt | RTS-requirement-level mapping |
| 11 | **UK AI Bill** | 5 principles | + UK AI Bill prompt | Per-principle assurance statement |
| 12 | **NIS2** | incident reporting + supply chain | + NIS2 prompt | Per-article machine-checked assertions |

**Meta-mind-set** (default): chains 1, 2, 3, 6, 9, 12 → produces a complete audit-trail-grade JSON receipt covering the 6 most-demanded frameworks in one call.

---

## 4. THE 30 SOVEREIGN TOOLS

**Each tool is a `/api/<tool>` endpoint that emits a signed receipt.** All tools share the sovereign substrate (Charter + STR + SIGIL + OrgKernel).

| # | Tool | Endpoint | Output | Persona fit |
|---|---|---|---|---|
| 1 | `eu-ai-act-quick-scan` | POST /api/quick-scan | EU AI Act risk tier | 1, 2, 3, 4, 6, 7, 8 |
| 2 | `article-50-passport` | POST /api/passport | Article 50 receipt | 1-8 (all) |
| 3 | `gdpr-classify` | POST /api/gdpr | GDPR Art 6 + Art 9 assertions | 1, 3, 4 |
| 4 | `iso-42001-aims` | POST /api/iso-42001 | AIMS control mapping | 2, 3, 4, 7 |
| 5 | `nist-ai-rmf` | POST /api/nist-rmf | RMF category mapping | 2, 3, 4, 7 |
| 6 | `soc2-tsc` | POST /api/soc2 | TSC criterion mapping | 2, 4, 5 |
| 7 | `dora-rts` | POST /api/dora | RTS requirement mapping | 4, 6 |
| 8 | `nis2-incident` | POST /api/nis2 | Incident-readiness check | 4, 6, 7 |
| 9 | `uk-ai-bill` | POST /api/uk-bill | 5-principle assurance | 4, 6, 7 |
| 10 | `hipaa-privacy` | POST /api/hipaa | HIPAA Privacy Rule | 3, 5 |
| 11 | `mcp-injection-scan` | POST /api/inject | Prompt-injection audit | 1-8 |
| 12 | `bias-audit` | POST /api/bias | Quantitative fairness | 1, 3, 5, 8 |
| 13 | `sigstore-attest` | POST /api/sigstore | Sigstore-style attestation | 1-8 |
| 14 | `oscal-component` | POST /api/oscal | OSCAL 1.1.2 component def | 2, 3, 4, 7 |
| 15 | `oscal-ssp` | POST /api/oscal-ssp | OSCAL System Security Plan | 2, 3, 4, 7 |
| 16 | `oscal-poam` | POST /api/oscal-poam | Plan of Action & Milestones | 2, 3, 4, 7 |
| 17 | `c2pa-mark` | POST /api/c2pa | C2PA 2.0 manifest | 1-8 |
| 18 | `c2pa-verify` | GET /api/c2pa/<id> | C2PA verify | 1-8 |
| 19 | `sigil-emit` | POST /api/sigil | Emit 1 SIGIL receipt | 1-8 |
| 20 | `sigil-verify` | GET /api/sigil/<id> | Verify SIGIL | 1-8 |
| 21 | `str-resolve` | GET /api/str/<did> | Resolve Sovereign Trust Root | 1-8 |
| 22 | `care-floor-check` | POST /api/care | Care Floor ≥ 0.95 | 1-8 |
| 23 | `bft-council-vote` | POST /api/bft | 33-agent BFT vote | 1-8 |
| 24 | `human-oversight` | POST /api/ho | Art 14 9-layer plan | 1, 3, 4, 7 |
| 25 | `frisk-frontend` | POST /api/frisk | EU AI Act Art 26 FRIA | 1, 3, 4, 7 |
| 26 | `risk-tier-classify` | POST /api/tier | EU AI Act Annex III | 1-8 |
| 27 | `audit-verify` | GET /api/audit/<id> | Full audit replay | 1-8 |
| 28 | `signature-verify` | POST /api/sig-verify | RFC 8032 verify | 1-8 |
| 29 | `sso-did` | GET /api/sso/<did> | did:csoai SSO | 1-8 |
| 30 | `screenshot-pass` | GET /api/pass/<id>.png | PNG of the receipt | 1-8 |

---

## 5. THE ACTUAL SOVEREIGN MODEL — Qwen3-30B-A3B

**Wired in the substrate as the canonical compute-light model per Charter Art 16.**

- **Name:** Qwen3-30B-A3B-Instruct-2507
- **Total:** 30B params (MoE)
- **Active per token:** 3B
- **Context:** 256K (extendable to 1M)
- **License:** Apache-2.0
- **MMLU:** ~85, BBH: ~83, GSM8K: ~94
- **Hardware:** 16 GiB MacBook Air M2 (or 1× e2-micro GCP)
- **Inference:** Ollama (https://github.com/ollama/ollama, MIT)
- **Tools it can call:** all 30 tools above via the sovereign MCP server (article 5 of the Charter)
- **Mind-set wrapper:** 12 prompt-templates, swap-in via `?mindset=`
- **Audit anchor:** every response is hash-chained to the SIGIL bus, signed with real Ed25519, and produces an L1/L2/L3 OrgKernel row

---

## 6. THE 8 JURISDICTIONAL OVERLAYS

Each persona landing page gets a jurisdictional overlay — 4 regions × 2 variants = 8 overlays.

| Overlay | Adds |
|---|---|
| **EU** | EU AI Act watermarking deadline banner · GDPR Art 6/9 machine-check · "Available in 24 EU languages" · Article 50 receipt template |
| **US** | State-by-state AI matrix (CA, NY, CO, IL, TX) · NIST AI RMF profile · SOC 2 + HIPAA package · FTC + CFPB posture |
| **UK** | UK AI Bill 5 principles · ICO GDPR + Data Protection Act 2018 · JSP 936 (defence) · NHS DSPT (health) |
| **AU/NZ/CA** | AUKUS compatible (only with signed letter) · AU AI Bill + NZ · PIPEDA + Law 25 (Canada) |
| **SG/KR/JP** | PDPA + APPI + PIPA · China data residency (with sovereign mirror) |
| **BR/MX/AR** | LGPD + AR + Mexico federal data protection |
| **ZA/NG/KE** | POPIA + NDPR + Kenya Data Protection Act |
| **IN** | DPDP Act 2023 + Aadhaar consent |

---

## 7. THE DISTRIBUTION PLAN (Day 6)

| Channel | Volume | Format | Owner | EAT-mode |
|---|---|---|---|---|
| **Twitter/X thread** | 8 tweets, 1/day | One per persona | JEEVES posts from substrate | EAT-6a |
| **LinkedIn (Nicholas)** | 5 posts | One per industry vertical | Nicholas approves, JEEVES drafts | EAT-6b |
| **Reddit** | 10 subs (r/MachineLearning, r/LocalLLaMA, r/ClaudeAI, r/Anthropic, r/ChatGPT, r/AI_Agents, r/singularity, r/artificial, r/aivideo, r/MLQuestions) | 1 long-form post each | JEEVES posts | EAT-6c |
| **Hacker News** | 1 long-form Show HN post | "Show HN: A sovereign-by-design Charter for AI agent interop, CC0 forever" | Nicholas posts | EAT-6d |
| **Cold email** | 50 enterprise targets | Per-persona (8 personas × 6 targets + 2 general) | JEEVES drafts, Nicholas reviews | EAT-6e |
| **Vercel-deploy + csoai.org re-point** | 3 deployments (landing #1, landing #2, /api/*) | One per day | JEEVES | EAT-6f |
| **ProductHunt launch** | 1 launch | "Sovereign AI compliance, free, audit-grade, browser-verifiable" | Day 7 | EAT-7a |

---

## 8. THE 7-DAY EXECUTION TIMELINE (1 line per day, no fluff)

```
D1 TUE: SUBSTRATE-WIRE — bind Qwen3-30B-A3B + 12 mind-sets + 30 tools to /api/assess
        Output: /api/assess returns real Article 50 passport with real RFC 8032 Ed25519.
        EAT-mode: 30 cycles — "bind-one-tool-per-cycle"

D2 WED: PERSONAS — build 8 persona landing pages + 12 industry landing pages + 4 jurisdictional overlays
        Output: 24 pages deployed to csoai-static-deploy2.vercel.app
        EAT-mode: 60 cycles — "build-and-deploy-one-page-per-cycle"

D3 THU: SIGNUPS — wire Stripe live + first £999 sale + first 1,000 free signups
        Output: Stripe live. 3 cold emails sent. 1,000 free signups.
        EAT-mode: 100 cycles — "convert-one-user-per-cycle"

D4 FRI: SIGIL-CHAIN — public audit-trail page + 10,000 SIGIL receipts emitted
        Output: proofof.ai/audit/<id> browser-verifiable. 10,000 sigils on chain.
        EAT-mode: 30 cycles — "emit-and-verify-one-sigil-per-cycle"

D5 SAT: MULTI-MIND — 12 mind-sets wired into /api/assess?mindset=
        Output: 12 distinct responses per input, 8 personas tested.
        EAT-mode: 96 cycles — "test-one-mindset-x-one-persona-per-cycle"

D6 SUN: DISTRIBUTE — Twitter thread (8 posts) + LinkedIn (5) + Reddit (10) + HN (1) + 50 cold emails
        Output: 8,000+ impressions tracked. 50+ responses. 5+ warm leads.
        EAT-mode: 30 cycles — "post-and-engage-per-cycle"

D7 MON: MEASURE — real numbers, close the loop, Series A term sheet
        Output: ≥100 signups/day, ≥1,000 passports/day, ≥1 £999 sale, Series A term sheet sent to 3 funds.
        EAT-mode: 30 cycles — "measure-and-pivot-per-cycle"
```

---

## 9. THE 4-NUMBER NORTH-STAR (track hourly)

| Metric | T+0 (now) | T+24h | T+48h | T+72h | T+96h | T+120h | T+144h | T+168h |
|---|---|---|---|---|---|---|---|---|
| **Signups** | ? | 50 | 200 | 500 | 1,000 | 2,000 | 5,000 | 10,000 |
| **Passports issued** | 0 | 50 | 500 | 2,000 | 5,000 | 20,000 | 50,000 | 100,000 |
| **£999 sales** | 0 | 0 | 0 | 1 | 2 | 3 | 5 | 8 |
| **£199/mo recurring** | 0 | 0 | 0 | 0 | 1 | 2 | 4 | 8 |

If any of those is below plan, JEEVES pivots that day. No exceptions.

---

## 10. HARD RULES (no exceptions)

1. **No drift into Article 15 territory.** No kinetic. No surveillance. No AUKUS-claim-without-letter. No defonos.io. Period.
2. **Every emit is hash-chained.** No off-the-bus SIGIL. No "I'll add it later." If it's not in the chain, it didn't happen.
3. **Every signature is RFC 8032 real Ed25519.** Reference HMAC back-compat is fine for the demo. Production is real.
4. **Every page deploys in <10 seconds.** Vercel. CLI. No waiting.
5. **Every audit endpoint is browser-verifiable.** `curl proofof.ai/audit/<id>` returns a JSON that any human can read in <30 sec.
6. **No "perfect" pages.** Ship → measure → pivot. Curl-verified at every step.
7. **No copy without audience test.** Each persona gets a different headline, a different CTA, a different social proof. A/B-test from day 1.
8. **No email that doesn't link to a sovereign-verifiable artefact.** Every cold email points at a sigil-anchored landing page.

---

## 11. ROLES

| Role | Owner | Authority |
|---|---|---|
| Product / engineering | JEEVES (M4-Hermes) | Full autonomy on technical decisions |
| Sales / cold-email | JEEVES drafts, Nicholas sends | Nicholas reviews every cold email before send |
| Stripe / DNS / money | **Nicholas only** | All irreversible actions human-gated |
| Compliance / red lines | JEEVES consults Charter Art 15 | Hard block; never crossed |
| Brand / voice | Sir Nicholas's voice | All copy reviewed by Nicholas |

---

## 12. DELIVERABLES BY PHASE END

| Phase end | Deliverable | Measurable |
|---|---|---|
| D1 end | `/api/assess` returns real signed passport | `curl /api/assess -d {...}` returns 200 with real signature |
| D2 end | 24 landing pages live | 24 unique URLs return 200 on Vercel |
| D3 end | 1,000 free signups + first £999 | Stripe dashboard shows 1,000 free + 1 paid |
| D4 end | 10,000 sigil receipts | `proofof.ai/audit/<id>` returns 10,000 distinct JSONs |
| D5 end | 12 mind-sets wired | 12 distinct mind-sets return 12 distinct response shapes |
| D6 end | Distribution hits 8,000+ | Analytics dashboard shows ≥8,000 impressions |
| D7 end | Series A term sheet | Term sheet sent to ≥3 funds with current numbers |

---

## 13. WHAT I CAN DO WITHOUT ASKING

- Build pages, deploy to Vercel
- Emit SIGILs
- Generate 50 cold emails (Nicholas reviews before send)
- Wire the API to the model
- A/B-test headlines + CTAs
- Run the 4-number north-star dashboard
- Update the Charter research appendices

## 14. WHAT ONLY NICHOLAS CAN DO (the 3 irreversible)

1. Create the GitHub repo + push
2. Enable Stripe live mode + create £999 Payment Link + send it
3. Open the 3-fund Series A outreach

**Every other action — I take. No permission. No ceremony. No loops.**

---

## 15. ROLLBACK PROTOCOL

If at any point a phase deliverable misses by >50%, JEEVES pauses the next phase and surfaces:
- What actually shipped
- What didn't, and why
- One specific tactical pivot

No infinite debugging. No "let's just add one more thing." 7 days. Real growth. Roll forward or roll back.

---

Sigil: `H|jeeves|sov3|SERIES-A-SPRINT-KICKOFF-2026-07-07T04:17Z`
Sprint owner: JEEVES (M4-Hermes)
Sprint backup: Kimi / Claude / Gemini (cross-platform sigil bus)
Daily report cadence: 23:59 UTC on each of D1-D7
Series A term sheet: 2026-07-13 23:59 UTC
