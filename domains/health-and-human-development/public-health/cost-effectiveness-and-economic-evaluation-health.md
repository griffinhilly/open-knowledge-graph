---
id: cost-effectiveness-and-economic-evaluation-health
title: Cost-Effectiveness Analysis and Economic Evaluation of Health Interventions
domain: health-and-human-development
course: public-health
prerequisites:
- id: cost-benefit-analysis-epidemiology
  type: hard
- id: burden-of-disease-and-comparative-health-assessment
  type: soft
tags:
- economic-evaluation
- cost-effectiveness
- program-evaluation
stage: advanced
status: draft
---

# Cost-Effectiveness Analysis and Economic Evaluation of Health Interventions

## Core Idea
Cost-effectiveness analysis compares intervention costs to health benefits (measured in QALYs or DALYs averted) to estimate the cost per unit health gain. Analyses require careful definition of perspective (individual, healthcare system, societal), identification of all relevant costs and benefits, and sensitivity analysis on key assumptions. Willingness-to-pay thresholds (often set as 1-3× GDP per capita) guide policy decisions.

## How It's Best Learned
Build a cost-effectiveness model for an intervention (vaccination, screening, treatment) comparing costs and health outcomes against a comparator.

## Common Misconceptions
- Cost-effectiveness analysis is objective; it requires value judgments about perspective, what outcomes to count, and what threshold is acceptable.
- Dominated interventions (more costly and less effective) should never be used; some dominated options are preferred for equity reasons.

## Questions

```yaml
- question: "A new oncology drug costs $300,000 per year and extends life by 4 months at full quality. Its ICER is calculated at $900,000 per QALY. A country's willingness-to-pay threshold is $50,000 per QALY. Which conclusion is most accurate?"
  type: multiple-choice
  options:
    - "The drug should be approved because any life extension has inherent value regardless of cost"
    - "The drug is not cost-effective by this threshold — each QALY it produces costs far more than alternative uses of that health budget"
    - "The drug is clinically ineffective because its ICER exceeds the threshold"
    - "The ICER is invalid because no threshold can appropriately value human life"
  answer: 1
  explanation: "Cost-effectiveness analysis does not judge whether the drug works — it judges whether it represents good value relative to what else the budget could buy. An ICER of $900,000/QALY against a threshold of $50,000/QALY means that 18 times more health could theoretically be produced by spending that money elsewhere. Option A conflates clinical and economic evaluation. Option C confuses ICER (a value-for-money measure) with efficacy (a clinical measure). Option D is a real philosophical position but doesn't answer the question."

- question: "A mental health intervention has an ICER of $90,000 per QALY from a healthcare system perspective, but only $12,000 per QALY from a societal perspective. The country's WTP threshold is $50,000 per QALY. What best explains this large discrepancy?"
  type: multiple-choice
  options:
    - "The societal analysis contains errors because perspective should not affect the ratio of costs to health gains"
    - "The healthcare perspective only counts medical costs while missing substantial benefits outside that system — reduced productivity losses, lower criminal justice costs, reduced caregiver burden — that the societal perspective captures"
    - "The societal perspective artificially inflates QALYs by counting benefits to third parties"
    - "The intervention has different clinical effects in different populations, explaining the different cost estimates"
  answer: 1
  explanation: "Perspective is one of the most consequential methodological choices in CEA. A healthcare system perspective counts only direct medical costs and health outcomes measured within the system. A societal perspective adds productivity gains, informal caregiver time, reduced criminal justice costs, education impacts, and other downstream effects. Mental health interventions often look far more cost-effective from a societal perspective because they prevent large non-medical costs. This is not an error — it is a different answer to a different question."

- question: "A cost-effectiveness analysis that reports a single ICER value without sensitivity analyses is providing an incomplete and potentially misleading result."
  type: true-false
  answer: true
  explanation: "Every input to a CEA model — disease incidence, treatment efficacy, quality-of-life weights, discount rates, time horizon — carries uncertainty. A single ICER is a point estimate that gives a false impression of precision. Sensitivity analysis (one-way or probabilistic via Monte Carlo) reveals how the conclusion changes as assumptions vary. If modest changes in key inputs flip the conclusion from 'cost-effective' to 'not cost-effective,' the policy recommendation is fragile and should not drive decision-making."

- question: "The willingness-to-pay threshold used in cost-effectiveness analysis is a scientific parameter derived from empirical data about the value of health, making it objective and comparable across countries."
  type: true-false
  answer: false
  explanation: "The WTP threshold is a value judgment — a policy choice about how much a society is willing to spend for an additional unit of health. It is not derived from any natural fact. The WHO's suggestion of 1–3× GDP per capita is a heuristic, not a scientific finding. Different countries use very different thresholds (the UK's NICE uses roughly £20,000–30,000/QALY; some middle-income countries use $2,000–3,000/DALY). Even within countries, thresholds are contested and sometimes violated — rare disease treatments are frequently funded above the stated threshold."

- question: "Why is sensitivity analysis considered essential rather than optional in cost-effectiveness analysis, and what does it reveal that a single ICER cannot?"
  type: short-answer
  answer: "Sensitivity analysis is essential because every parameter in a CEA model — incidence rates, effectiveness estimates, quality-of-life weights, discount rates, time horizons — rests on assumptions that carry uncertainty. A single ICER gives the false impression of a precise answer. Sensitivity analysis reveals the robustness of the conclusion: if the ICER remains well below the WTP threshold across all plausible parameter values, the recommendation is solid; if it crosses the threshold with modest changes in key inputs, the recommendation is fragile. Probabilistic sensitivity analysis (Monte Carlo simulation) produces a distribution of possible ICERs rather than a point estimate, showing decision-makers the probability that the intervention is cost-effective — which is the information actually needed for policy."
  explanation: "The practical consequence is that a CEA without sensitivity analysis should not drive coverage decisions. The analysis answers a specific question (is this cost-effective under these assumptions?) but policy requires knowing how sensitive that answer is to the assumptions. A drug that appears cost-effective only under optimistic assumptions about efficacy may not justify coverage once uncertainty is fully characterized."
```

## Explainer

From your study of cost-benefit analysis in epidemiology and burden-of-disease measurement, you know that health resources are finite and that interventions have measurable effects on health outcomes. **Cost-effectiveness analysis (CEA)** is the method health economists use to formalize the tradeoff: given a fixed budget, which interventions produce the most health for the money spent? Unlike a simple cost-benefit analysis that converts everything to dollars, CEA keeps health gains in natural units — most commonly **quality-adjusted life years (QALYs)** (life years weighted by health-related quality of life) or **disability-adjusted life years (DALYs)** averted.

The central output of a CEA is the **incremental cost-effectiveness ratio (ICER)**: the additional cost divided by the additional health benefit of the new intervention compared to the current standard of care. If a new vaccine costs $5 million more per year than the existing approach and prevents 1,000 additional DALYs, its ICER is $5,000 per DALY averted. Whether this represents good value depends on the **willingness-to-pay (WTP) threshold** — the maximum a payer is willing to spend for one additional unit of health gain. The World Health Organization has historically suggested 1–3× a country's GDP per capita as a reasonable threshold; richer countries use higher thresholds (the UK's NICE uses roughly £20,000–30,000 per QALY). Interventions with ICERs below the threshold are considered cost-effective; those above it are not — though "cost-effective" never means "affordable" or "recommended."

The **perspective** of analysis is one of the most consequential methodological choices. A healthcare system perspective counts only medical costs and health outcomes; a societal perspective adds productivity losses, informal caregiver costs, and downstream economic effects. These can differ dramatically: a mental health intervention might appear only modestly cost-effective from a healthcare perspective (it uses expensive clinical resources) but highly cost-effective from a societal perspective (it prevents years of lost work and reduces criminal justice costs). Analysts must declare their perspective explicitly, because changing it can flip a conclusion from "not cost-effective" to "highly cost-effective."

Because every model rests on assumptions — about disease incidence, intervention effectiveness, quality-of-life weights, discount rates — **sensitivity analysis** is not optional; it is the core of honest economic evaluation. One-way sensitivity analyses vary each input individually; probabilistic sensitivity analyses vary all inputs simultaneously using Monte Carlo simulation, producing a distribution of ICER estimates rather than a single point. A policy decision based on a single ICER without sensitivity analysis is fragile. The final nuance — captured in the Common Misconceptions — is that the cost-effectiveness threshold is itself a value judgment, not a scientific finding. Societies routinely fund interventions above the threshold for equity reasons (rare diseases, pediatric conditions) and sometimes defund effective interventions below the threshold for budget reasons. CEA is a decision aid, not a decision rule.
