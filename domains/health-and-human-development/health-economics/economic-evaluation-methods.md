---
id: economic-evaluation-methods
title: Economic Evaluation Methods in Health
domain: health-and-human-development
course: health-economics
prerequisites:
- id: cost-effectiveness-analysis
  type: hard
- id: cost-utility-analysis
  type: hard
- id: cost-benefit-analysis-health
  type: hard
builds-toward: []
tags:
- economic-evaluation
- perspective
- discounting
- sensitivity-analysis
- modeling
- decision-tree
- Markov-model
stage: advanced
status: validated
---

# Economic Evaluation Methods in Health

## Core Idea
Economic evaluation in health encompasses the set of analytical methods used to compare the costs and consequences of alternative health interventions. The three primary types — cost-effectiveness analysis (CEA), cost-utility analysis (CUA), and cost-benefit analysis (CBA) — share a common analytical framework but differ in how outcomes are measured. All economic evaluations require defining the perspective (whose costs and benefits count?), the comparator (what is the alternative?), the time horizon (how far into the future?), and the discount rate (how are future costs and benefits valued relative to present ones?). Decision-analytic models — decision trees for short-term outcomes and Markov models for chronic diseases — project costs and outcomes beyond the trial period using the best available evidence. Sensitivity analysis tests whether conclusions are robust to uncertainty in key parameters.

## Questions

```yaml
- question: "An economic evaluation of a new diabetes drug uses a 5-year time horizon, even though diabetes is a lifelong condition. Why might this underestimate the drug's value, and what would be a more appropriate approach?"
  type: multiple-choice
  options:
    - "5 years is always sufficient for chronic diseases"
    - "A 5-year horizon misses long-term benefits (reduced cardiovascular events, preserved kidney function) and long-term cost offsets that accrue over decades. A lifetime Markov model with annual health state transitions would capture the full trajectory of costs and outcomes"
    - "The time horizon does not affect the ICER"
    - "Longer time horizons always favor the new treatment"
  answer: 1
  explanation: "For chronic diseases, many benefits (and costs) accrue over decades. A 5-year evaluation of a diabetes drug captures early effects on blood sugar control but misses the downstream prevention of retinopathy, nephropathy, and cardiovascular events that develop over 10-30 years. A Markov model simulates annual transitions between health states (controlled diabetes → complications → death) over a lifetime horizon, projecting the full cost and health consequences of each treatment strategy. Most HTA bodies require a lifetime horizon for chronic diseases."

- question: "An economic evaluation discounts future costs and health outcomes at 3% per year. This means a QALY gained 20 years from now is worth less than a QALY gained today. Why is this appropriate?"
  type: short-answer
  answer: "Discounting reflects time preference — both individuals and society prefer benefits sooner rather than later and costs later rather than sooner. A dollar invested today grows over time, so a future dollar is worth less in present terms. The same logic is applied to health outcomes: given a choice, most people prefer to be healthy now rather than in 20 years. Without discounting, interventions with upfront costs and distant benefits (like childhood vaccination) would always look favorable, regardless of how far in the future the benefits occur. The 3% rate is a convention that balances time preference with the ethical concern that future people's health should not be excessively devalued."
  explanation: "There is ongoing debate about whether health outcomes should be discounted at the same rate as costs. Some argue that health does not depreciate like money and should be discounted at a lower rate (or not at all). This is more than an academic question: differential discounting dramatically favors preventive interventions (high upfront cost, benefits decades later). The convention of equal discounting at 3% is a pragmatic compromise used by most major HTA agencies."

- question: "Probabilistic sensitivity analysis (PSA) is superior to one-way sensitivity analysis for decision-making because it simultaneously varies all uncertain parameters according to their probability distributions, reflecting the true uncertainty in the model."
  type: true-false
  answer: true
  explanation: "One-way sensitivity analysis varies one parameter at a time while holding others constant — useful for identifying which parameters drive the result but unrealistic because multiple parameters are uncertain simultaneously. PSA draws thousands of random values from each parameter's distribution, runs the model for each draw, and produces a distribution of ICERs. This generates a cost-effectiveness acceptability curve showing the probability that each intervention is cost-effective at different willingness-to-pay thresholds. PSA captures the full uncertainty in the decision, including parameter correlations, and is required by most HTA agencies."
```

## Explainer

Economic evaluation provides the analytical backbone for health resource allocation decisions. While the three main types (CEA, CUA, CBA) have different outcome measures, they share a common analytical framework that involves several key methodological choices.

The **perspective** determines whose costs and benefits are counted. A healthcare system perspective includes only direct medical costs (drugs, hospitalizations, physician visits). A societal perspective adds patient costs (transportation, lost wages), caregiver costs, and productivity losses. The same intervention can look cost-effective from a healthcare perspective but not from a societal perspective (or vice versa) depending on how non-medical costs distribute. Most HTA bodies specify a required perspective; the US Second Panel on Cost-Effectiveness recommends reporting both healthcare and societal perspectives.

The **comparator** is what the new intervention replaces. An intervention must be compared to the relevant alternative — typically the current standard of care, not placebo. A drug that beats placebo may not beat an existing generic; evaluating it against placebo would overstate its added value. The choice of comparator profoundly affects the ICER: if the comparator is ineffective, the new intervention looks excellent; if the comparator is already good, incremental gains are small and the ICER rises.

**Decision-analytic models** extend the analysis beyond the evidence directly observed in trials. A **decision tree** maps short-term decision points and their probabilistic outcomes (e.g., surgery succeeds or fails, with different downstream costs and health states). A **Markov model** adds time: patients transition between health states (e.g., well → mild disease → severe disease → death) at each time cycle (typically annual), accumulating costs and QALYs in each state. Markov models are standard for chronic diseases where long-term outcomes matter. Parameters come from clinical trials, observational studies, administrative databases, and expert opinion, each with uncertainty.

**Sensitivity analysis** is the critical quality control step. **One-way analysis** varies each parameter individually to identify which drives the result. **Threshold analysis** finds the value at which the conclusion changes. **Probabilistic sensitivity analysis** (PSA) simultaneously varies all parameters according to their probability distributions across thousands of Monte Carlo simulations, producing a distribution of ICERs that reflects the full uncertainty in the model. The results are displayed as cost-effectiveness scatter plots (cloud of simulated ICERs) and cost-effectiveness acceptability curves (probability of cost-effectiveness at each WTP threshold). PSA transforms the analysis from a point estimate ("the ICER is $50,000/QALY") into a probabilistic statement ("there is a 75% probability that the intervention is cost-effective at a $50,000 threshold").
