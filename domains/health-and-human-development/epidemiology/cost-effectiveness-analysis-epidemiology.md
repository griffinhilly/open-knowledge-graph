---
id: cost-effectiveness-analysis-epidemiology
title: Cost-Effectiveness Analysis in Public Health
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: disability-adjusted-life-years
  type: hard
- id: quality-adjusted-life-years
  type: hard
- id: health-systems-and-financing
  type: soft
tags:
- economic-evaluation
- health-economics
- decision-analysis
stage: advanced
status: draft
---

# Cost-Effectiveness Analysis in Public Health

## Core Idea
Cost-effectiveness analysis (CEA) compares the cost per unit of health gain (per DALY averted or per QALY gained) to determine whether an intervention provides acceptable value. CEA requires (1) epidemiological evidence for intervention effectiveness, (2) comprehensive cost data, (3) natural history and disease modeling, and (4) specification of willingness-to-pay thresholds. Decision analysis and Markov modeling integrate epidemiological parameters into economic models. Sensitivity analysis tests robustness to parameter uncertainty and identifies key drivers of cost-effectiveness.

## Questions

```yaml
- question: "A new antiretroviral regimen costs $80,000 more per patient over a lifetime than standard care and generates 4 additional QALYs. The national willingness-to-pay threshold is $30,000/QALY. What is the correct conclusion?"
  type: multiple-choice
  options:
    - "The regimen is cost-effective because it generates meaningful health gains"
    - "The regimen is not cost-effective because its ICER ($20,000/QALY) exceeds the WTP threshold"
    - "The regimen is not cost-effective because its ICER ($20,000/QALY) falls below the WTP threshold"
    - "The regimen is cost-effective because its ICER ($20,000/QALY) falls below the WTP threshold"
  answer: 3
  explanation: "ICER = $80,000 / 4 QALYs = $20,000/QALY. Since $20,000 < $30,000 (WTP threshold), the intervention is cost-effective. Option A is wrong because generating 'meaningful health gains' is not the criterion — the ICER vs. threshold comparison is. The common trap here is confusing total cost ($80,000) with cost per QALY ($20,000)."

- question: "A cost-effectiveness analysis reports an ICER of $15,000/QALY, well below the WTP threshold. A health ministry nonetheless declines to fund the intervention nationally. What economic concept best explains this apparent contradiction?"
  type: multiple-choice
  options:
    - "The willingness-to-pay threshold was set incorrectly"
    - "Budget impact: the intervention may be cost-effective but unaffordable at scale across a large population"
    - "The ICER should have used DALYs, not QALYs, for this type of disease"
    - "Probabilistic sensitivity analysis would show the ICER is unreliable"
  answer: 1
  explanation: "Cost-effectiveness and affordability are distinct. An ICER below the WTP threshold means each QALY is 'worth' the price — but if millions of patients are eligible, the aggregate cost may strain the health budget even at $15,000/QALY. Budget impact analysis, not CEA, captures this population-level cost. Options A, C, and D address methodology but do not explain the scenario described."

- question: "An intervention with an ICER below the willingness-to-pay threshold may still be unaffordable for a health system to implement at scale."
  type: true-false
  answer: true
  explanation: "Cost-effectiveness and budget impact are separate analyses. A low ICER means each unit of health gain is purchased at acceptable value, but if the eligible population is large, the total expenditure can still overwhelm a health budget. Both CEA (is it worth it per QALY?) and budget impact analysis (can the system afford it?) are needed for complete health technology assessment."

- question: "A cost-effectiveness acceptability curve (CEAC) shows the probability that an intervention is cost-effective at a given threshold. This output comes from one-way sensitivity analysis varying each parameter in turn."
  type: true-false
  answer: false
  explanation: "The CEAC comes from probabilistic sensitivity analysis (PSA), which simultaneously varies all parameters according to their probability distributions across thousands of Monte Carlo simulations. One-way sensitivity analysis varies a single parameter at a time, producing a tornado diagram showing which parameters most influence the ICER — not a probability of cost-effectiveness across thresholds."

- question: "Why is a Markov model used in cost-effectiveness analysis rather than a simple comparison of intervention cost against comparator cost?"
  type: short-answer
  answer: "A Markov model simulates transitions among health states over time, allowing CEA to capture costs and QALYs that accrue at different stages of disease progression across a lifetime horizon. Real diseases involve delayed outcomes — a preventive intervention may cost more now but avert expensive late-stage disease decades later. A simple before/after cost comparison cannot capture these temporal dynamics and would misrepresent the true economic value of interventions with long-term benefits."
  explanation: "The model also allows the analyst to incorporate epidemiological parameters (transition probabilities from incidence and mortality studies) alongside cost and utility data, integrating clinical evidence into a single economic framework. This is why CEA is sometimes called 'decision analysis' — it is a structured approach to choices under uncertainty across time."
```

## Explainer

Health systems face a fundamental allocation problem: resources are finite, but potential interventions are not. Cost-effectiveness analysis provides a structured framework for comparing the value of different interventions on a common metric, enabling more rational priority-setting. You already know DALYs and QALYs — the currency of health gain. CEA uses them as the denominator. The core output of any CEA is the **incremental cost-effectiveness ratio (ICER)**: the extra cost of the new intervention divided by the extra health it produces, compared to the best existing alternative.

ICER = (Cost_new − Cost_comparator) / (Effect_new − Effect_comparator)

The denominator can be expressed in QALYs gained or DALYs averted. If a new HIV treatment costs $50,000 more per patient over a lifetime and generates 2 additional QALYs compared to standard of care, the ICER is $25,000/QALY. Whether that is "worth it" depends on the **willingness-to-pay (WTP) threshold** — the maximum a decision-maker is willing to spend per unit of health gain. The WHO's 1–3× GDP per capita rule of thumb is widely cited but increasingly contested; high-income countries often use thresholds of $50,000–$150,000/QALY. Interventions below the threshold are deemed cost-effective; those above are generally not recommended, though cost is not the only consideration in policy.

The most important methodological tool in CEA is the **Markov model**. Real diseases don't unfold in a single decision moment — they involve transitions among health states over time. A Markov model represents disease progression as a set of discrete **states** (e.g., HIV-negative, HIV-positive untreated, on ART, AIDS, dead) and **transition probabilities** (derived from epidemiological studies) governing movement between states at each time cycle. The model is run over a defined **time horizon** (often lifetime) for both the intervention and comparator arms, accumulating costs and QALYs in each state along the way. This allows CEA to capture delayed costs and benefits that would be invisible in a simple clinical trial. Parameters feeding the model come from diverse sources: incidence and mortality from your epidemiological studies, utility weights (QALYs) from preference studies, costs from health system accounting.

Because many model parameters are uncertain, **sensitivity analysis** is not optional — it is a core deliverable. **One-way sensitivity analysis** varies each parameter across its plausible range while holding others fixed, identifying which parameters most influence the ICER. **Probabilistic sensitivity analysis (PSA)** simultaneously varies all parameters according to their probability distributions (beta for probabilities, gamma for costs, etc.) in thousands of Monte Carlo simulations, generating a distribution of ICERs. The output — the **cost-effectiveness acceptability curve (CEAC)** — shows the probability that the intervention is cost-effective at any given WTP threshold. This is the honest answer to "how confident are we?" and is essential for policy-makers who must act under uncertainty. A final distinction: **budget impact analysis** is not the same as CEA. An intervention can be highly cost-effective (low ICER) but still be unaffordable at scale if applied to a large population. Both analyses are needed for complete health technology assessment.
