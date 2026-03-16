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

## Explainer

Health systems face a fundamental allocation problem: resources are finite, but potential interventions are not. Cost-effectiveness analysis provides a structured framework for comparing the value of different interventions on a common metric, enabling more rational priority-setting. You already know DALYs and QALYs — the currency of health gain. CEA uses them as the denominator. The core output of any CEA is the **incremental cost-effectiveness ratio (ICER)**: the extra cost of the new intervention divided by the extra health it produces, compared to the best existing alternative.

ICER = (Cost_new − Cost_comparator) / (Effect_new − Effect_comparator)

The denominator can be expressed in QALYs gained or DALYs averted. If a new HIV treatment costs $50,000 more per patient over a lifetime and generates 2 additional QALYs compared to standard of care, the ICER is $25,000/QALY. Whether that is "worth it" depends on the **willingness-to-pay (WTP) threshold** — the maximum a decision-maker is willing to spend per unit of health gain. The WHO's 1–3× GDP per capita rule of thumb is widely cited but increasingly contested; high-income countries often use thresholds of $50,000–$150,000/QALY. Interventions below the threshold are deemed cost-effective; those above are generally not recommended, though cost is not the only consideration in policy.

The most important methodological tool in CEA is the **Markov model**. Real diseases don't unfold in a single decision moment — they involve transitions among health states over time. A Markov model represents disease progression as a set of discrete **states** (e.g., HIV-negative, HIV-positive untreated, on ART, AIDS, dead) and **transition probabilities** (derived from epidemiological studies) governing movement between states at each time cycle. The model is run over a defined **time horizon** (often lifetime) for both the intervention and comparator arms, accumulating costs and QALYs in each state along the way. This allows CEA to capture delayed costs and benefits that would be invisible in a simple clinical trial. Parameters feeding the model come from diverse sources: incidence and mortality from your epidemiological studies, utility weights (QALYs) from preference studies, costs from health system accounting.

Because many model parameters are uncertain, **sensitivity analysis** is not optional — it is a core deliverable. **One-way sensitivity analysis** varies each parameter across its plausible range while holding others fixed, identifying which parameters most influence the ICER. **Probabilistic sensitivity analysis (PSA)** simultaneously varies all parameters according to their probability distributions (beta for probabilities, gamma for costs, etc.) in thousands of Monte Carlo simulations, generating a distribution of ICERs. The output — the **cost-effectiveness acceptability curve (CEAC)** — shows the probability that the intervention is cost-effective at any given WTP threshold. This is the honest answer to "how confident are we?" and is essential for policy-makers who must act under uncertainty. A final distinction: **budget impact analysis** is not the same as CEA. An intervention can be highly cost-effective (low ICER) but still be unaffordable at scale if applied to a large population. Both analyses are needed for complete health technology assessment.
