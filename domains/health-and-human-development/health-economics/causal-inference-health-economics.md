---
id: causal-inference-health-economics
title: Causal Inference in Health Economics
domain: health-and-human-development
course: health-economics
prerequisites:
- id: healthcare-market-structure
  type: hard
- id: moral-hazard-health-insurance
  type: hard
- id: economic-evaluation-methods
  type: soft
- id: grossman-model
  type: soft
builds-toward: []
tags:
- causal-inference
- RAND-HIE
- Oregon-experiment
- difference-in-differences
- regression-discontinuity
- instrumental-variables
- natural-experiments
stage: advanced
status: validated
---

# Causal Inference in Health Economics

## Core Idea
Health economics relies on causal claims — insurance reduces financial risk, cost-sharing reduces utilization, hospital competition lowers prices — but healthcare markets make causal inference exceptionally difficult because people select into insurance, treatments, and providers based on unobservable characteristics correlated with outcomes. The field has developed a distinctive toolkit of research designs to address this endogeneity. Randomized experiments (the RAND Health Insurance Experiment, the Oregon Medicaid lottery) provide the cleanest evidence but are rare, expensive, and ethically constrained. Quasi-experimental methods exploit natural experiments: difference-in-differences (comparing changes in outcomes before and after a policy change between affected and unaffected groups), regression discontinuity (exploiting eligibility cutoffs where assignment is as-if random), and instrumental variables (using an exogenous source of variation in the endogenous variable). Every major empirical finding in health economics — from the price elasticity of healthcare demand to the effects of insurance expansion — rests on the credibility of a specific causal identification strategy.

## Questions

```yaml
- question: "The Oregon Health Insurance Experiment (2008) used a lottery to assign Medicaid coverage to low-income adults. Two years later, Medicaid coverage significantly increased emergency room usage, contrary to the prediction that insurance would shift care from ERs to primary care. This finding was controversial. Why is the lottery design so valuable despite producing an unexpected result?"
  type: short-answer
  answer: "The lottery created true random assignment to Medicaid eligibility, eliminating selection bias — the fundamental problem that people who choose to enroll in Medicaid differ systematically from those who do not (sicker, lower income, more health-aware). Without randomization, observational comparisons between Medicaid enrollees and non-enrollees confound the effect of insurance with the characteristics of people who seek insurance. The lottery also had high internal validity: the comparison group (lottery losers) was identical in expectation to the treatment group (lottery winners) on all observed and unobserved characteristics. The unexpected ER finding is precisely why the design is valuable — it overturned a widely held but empirically untested assumption. Prior quasi-experimental studies could not credibly distinguish whether insurance reduced ER use (substitution to primary care) or increased it (newly insured people use more of everything, including ERs)."
  explanation: "The Oregon experiment also found that Medicaid significantly reduced financial strain and depression, increased preventive care use, and increased diabetes detection — but did not produce statistically significant improvements in measured physical health outcomes (blood pressure, cholesterol, HbA1c) after two years. This null finding on physical health was heavily debated: the study may have been underpowered for health outcomes, two years may be too short to detect health improvements, or the effect of insurance on health may genuinely be small in the short run. The study illustrates both the power of randomization (credible causal estimates) and its limitations (finite sample size, limited follow-up, local average treatment effect for compliers only)."

- question: "A researcher wants to estimate the effect of hospital competition on quality. She uses a difference-in-differences design, comparing changes in mortality at hospitals that experienced a nearby hospital closure (treatment group) with hospitals that did not (control group), before and after the closure. The key identifying assumption of this design is:"
  type: multiple-choice
  options:
    - "Hospital closures are randomly assigned"
    - "The treatment and control hospitals had identical mortality levels before the closure"
    - "In the absence of the closure, mortality trends at treatment hospitals would have been parallel to those at control hospitals (the parallel trends assumption)"
    - "All patients at treatment hospitals are identical to patients at control hospitals"
  answer: 2
  explanation: "Difference-in-differences does not require equal levels — it allows treatment and control groups to differ permanently, as long as their time trends would have been the same absent the treatment. The parallel trends assumption states: whatever factors were driving mortality changes over time affected treatment and control hospitals equally. The method removes time-invariant differences between groups (the 'first difference' in a cross-sectional comparison) and common time trends (the 'second difference' in a before-after comparison), isolating the treatment effect. This assumption is not directly testable (we cannot observe the counterfactual), but researchers assess its plausibility by checking whether pre-treatment trends were parallel over multiple prior periods. If treatment hospitals already showed diverging trends before the closure, the design is not credible."

- question: "Instrumental variables (IV) methods in health economics require an instrument that is correlated with the endogenous treatment variable but affects the outcome only through the treatment — the exclusion restriction. In the context of estimating the effect of insurance on health, geographic distance to a hospital has been proposed as an instrument for insurance coverage."
  type: true-false
  answer: false
  explanation: "Distance to a hospital is a poor instrument for insurance coverage because it likely violates the exclusion restriction — distance affects health outcomes through channels other than insurance. People living far from hospitals may have less access to care regardless of insurance status, may differ in socioeconomic characteristics (rural vs. urban), and may face different environmental health risks. A valid instrument must affect the outcome ONLY through the endogenous variable. Better instruments for insurance include lottery-based assignment (Oregon experiment), age-based eligibility cutoffs (Medicare at 65, used in RD designs), and employer mandate thresholds (firms above vs. below a size cutoff, used in DiD designs). The exclusion restriction is the most important and most commonly violated assumption in applied IV work."
```

## Explainer

The central problem of empirical health economics is that you cannot simply compare people with insurance to people without insurance and attribute any health or utilization difference to the effect of insurance. People who have insurance differ from people who do not in ways that independently affect health outcomes — they tend to be employed, higher income, more health-conscious, and less chronically ill. This **selection bias** contaminates naive observational comparisons, and it pervades every important question in the field: the effect of insurance on health, the effect of competition on hospital quality, the effect of pharmaceutical patents on innovation, the effect of physician supply on costs.

The **RAND Health Insurance Experiment** (1974-1982) addressed this problem definitively for one key question — the effect of cost-sharing on utilization — by randomly assigning 2,000 families to insurance plans with different coinsurance rates. Random assignment guaranteed that the groups were identical in expectation on all characteristics, observed and unobserved. The result — a price elasticity of demand for healthcare around -0.2, meaning a 10% increase in out-of-pocket price reduces utilization by about 2% — remains the benchmark estimate forty years later. But the RAND experiment cost over $300 million in current dollars and took a decade. Health economists cannot run randomized experiments for most policy questions.

**Quasi-experimental methods** exploit naturally occurring variation that mimics randomization. **Difference-in-differences** (DiD) compares the change in outcomes over time between a group affected by a policy and a group not affected. The Medicaid expansion studies exemplify this: states that expanded Medicaid under the ACA (treatment) vs. states that did not (control), comparing outcomes before and after 2014. The identifying assumption is parallel trends — absent the expansion, outcomes would have evolved similarly in both groups. **Regression discontinuity** (RD) exploits sharp eligibility cutoffs: Medicare eligibility at age 65 creates a discontinuity where 64-year-olds and 65-year-olds are nearly identical in all respects except insurance coverage, allowing credible estimation of the effect of Medicare on utilization, spending, and health outcomes. **Instrumental variables** (IV) use an exogenous source of variation in the treatment variable — for example, a state-level policy change that affected insurance coverage but plausibly had no direct effect on health.

Each design has its strengths and weaknesses. RCTs provide the highest internal validity but are expensive, often ethically infeasible, and measure effects only for the specific population and setting studied (limited external validity). DiD is flexible and widely applicable but relies on the untestable parallel trends assumption. RD provides highly credible local estimates but only at the cutoff — the effect of Medicare at age 65 may not generalize to the effect of insurance at age 40. IV estimates are only as good as the instrument's validity, and the exclusion restriction (the instrument affects the outcome only through the treatment) is never provable. The credibility of any empirical finding in health economics rests on the credibility of its identification strategy — and the field's methodological sophistication has advanced precisely because the stakes of getting causal claims wrong in health policy are so high.
