---
id: health-technology-assessment
title: Health Technology Assessment
domain: health-and-human-development
course: health-economics
prerequisites:
- id: cost-effectiveness-analysis
  type: hard
- id: cost-utility-analysis
  type: hard
- id: cost-effectiveness-analysis-health-econ
  type: soft
builds-toward: []
tags:
- HTA
- NICE
- reimbursement
- appraisal
- value-framework
stage: advanced
status: validated
---

# Health Technology Assessment

## Core Idea
Health technology assessment (HTA) is the systematic evaluation of a health technology's (drug, device, procedure, or program) clinical effectiveness, cost-effectiveness, and broader impact to inform coverage, reimbursement, and pricing decisions. HTA bodies like the UK's NICE, Australia's PBAC, and Canada's CADTH review manufacturer-submitted evidence and independent analyses to determine whether a technology provides sufficient value for money to warrant public funding. The HTA process integrates clinical evidence (does it work?), economic evaluation (is the ICER acceptable?), budget impact analysis (can we afford it?), and broader considerations (equity, innovation incentives, patient preferences). HTA institutionalizes the economic principle that healthcare resources are scarce and allocation decisions should be informed by systematic evidence assessment rather than political lobbying or marketing.

## Questions

```yaml
- question: "A pharmaceutical company submits evidence to NICE showing that its new cancer drug extends median survival by 3 months at a cost of $150,000 per patient. The ICER is $200,000/QALY, well above NICE's standard threshold of £20,000-30,000/QALY. Under what circumstances might NICE still recommend the drug?"
  type: multiple-choice
  options:
    - "Never — if the ICER exceeds the threshold, the drug is rejected"
    - "NICE may apply end-of-life criteria (short life expectancy, life-extending treatment, small patient population) that allow a higher effective threshold, or negotiate a confidential price discount that brings the ICER below threshold"
    - "Only if the manufacturer lobbies Parliament successfully"
    - "If patient advocacy groups generate sufficient media pressure"
  answer: 1
  explanation: "NICE uses modified criteria for end-of-life treatments: if the condition is terminal (life expectancy < 24 months), the treatment extends life by ≥ 3 months, and the patient population is small, NICE may weight QALYs gained by up to 1.7×, effectively allowing ICERs up to about £50,000/QALY. Additionally, confidential patient access schemes (managed access, outcome-based contracts) can reduce the effective price. The process is flexible within principled boundaries — it does not mechanically reject everything above threshold, but any exception must be justified through explicit criteria."

- question: "HTA bodies evaluate the same drug and reach different conclusions in different countries (e.g., approved in the UK but rejected in Canada). This inconsistency proves that HTA is arbitrary."
  type: true-false
  answer: false
  explanation: "Different conclusions reflect different thresholds, different healthcare system contexts, and different societal values — not arbitrariness. Countries set different willingness-to-pay thresholds reflecting their wealth, healthcare budgets, and political preferences. The evidence base may also differ (different comparators in different markets, different patient populations). Furthermore, budget impact — the total cost relative to the national health budget — varies by country. HTA is a structured decision process within a specific national context; different contexts legitimately produce different decisions."

- question: "Explain why budget impact analysis is a necessary complement to cost-effectiveness analysis in HTA, even when the ICER is favorable."
  type: short-answer
  answer: "An intervention can be highly cost-effective (low ICER) but still unaffordable if the eligible patient population is large. A treatment costing $50,000/QALY is cost-effective by most thresholds, but if 1 million patients are eligible, the total budget impact is $50 billion — potentially unaffordable. Budget impact analysis evaluates whether the healthcare system can absorb the total cost of adopting the technology over a defined time horizon (typically 3-5 years), considering the existing budget, displacement of other spending, and the rate of uptake. Both cost-effectiveness and affordability must be assessed for a responsible coverage decision."
  explanation: "This is why HTA bodies consider budget impact separately from cost-effectiveness. A breakthrough gene therapy might be cost-effective per patient but have a total budget impact that crowds out other valuable care. Some systems use budget impact thresholds or installment-based payment models (annuity payments for gene therapies) to manage affordability while preserving access to cost-effective innovations."
```

## Explainer

The development of a new drug or medical device involves billions of dollars in R&D, clinical trials, and regulatory approval. But regulatory approval (FDA, EMA) certifies only that the technology is safe and efficacious — it does not determine whether it is worth paying for with public money. **Health technology assessment** fills this gap by systematically evaluating whether the health gains justify the cost, given the reality of finite healthcare budgets.

The HTA process typically involves four components. **Clinical effectiveness assessment** reviews the evidence that the technology works — what is the magnitude of benefit, how certain is the evidence, and how does it compare to current standard of care? **Economic evaluation** estimates the ICER, usually in cost per QALY, using a decision-analytic model that projects costs and outcomes over the relevant time horizon (often lifetime). **Budget impact analysis** estimates the total cost to the healthcare system of adopting the technology, given the size of the eligible population and expected uptake. **Broader considerations** include equity (does the technology serve disadvantaged groups?), innovation (does rejecting it discourage future R&D?), and patient preferences.

**NICE** (the UK's National Institute for Health and Care Excellence) is the most influential HTA body globally. Its standard cost-effectiveness threshold of £20,000-30,000 per QALY means that technologies with ICERs below this range are normally recommended, those above are normally rejected, and those near the boundary require additional justification. NICE publishes its methods, evidence reviews, and decisions transparently, creating a body of precedent that influences HTA practice worldwide.

HTA is fundamentally about making explicit the tradeoffs that every healthcare system makes implicitly. Without HTA, coverage decisions are driven by political pressure, pharmaceutical marketing, or historical precedent — none of which systematically considers value for money. With HTA, a new drug that costs $300,000 per patient for 2 months of additional survival is evaluated against the same framework as a preventive screening program that costs $50 per person. This does not eliminate difficult choices — it ensures they are informed by evidence and made transparently.
