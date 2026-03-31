---
id: propensity-score-methods-biostatistics
title: Propensity Score Methods
domain: health-and-human-development
course: biostatistics
prerequisites:
- id: causal-inference-methods-biostatistics
  type: hard
- id: logistic-regression-biostatistics
  type: hard
builds-toward:
- instrumental-variables-biostatistics
tags:
- propensity-score
- matching
- IPTW
- stratification
- observational
- confounding
stage: expert
status: validated
---

# Propensity Score Methods

## Core Idea
The propensity score is the probability of receiving treatment given observed covariates: e(X) = P(Treatment = 1 | X). Rosenbaum and Rubin (1983) proved that conditioning on the propensity score balances all observed covariates between treatment groups, reducing a high-dimensional confounding adjustment problem to a single dimension. Propensity scores can be used via matching (pairing treated and control subjects with similar scores), stratification (grouping subjects into propensity score strata), inverse probability of treatment weighting (IPTW, weighting each subject by the inverse of their probability of receiving their actual treatment), or covariate adjustment. All approaches assume no unmeasured confounding (strongly ignorable treatment assignment): after conditioning on observed covariates, treatment assignment is independent of potential outcomes. This assumption is untestable and is the primary limitation of all propensity score methods.

## Questions

```yaml
- question: "A propensity score model for statin use includes age, sex, cholesterol, diabetes, and smoking. After matching, treated and control groups have excellent balance on all five variables. Does this guarantee an unbiased treatment effect estimate?"
  type: multiple-choice
  options:
    - "Yes — if all included covariates are balanced, the comparison is as good as a randomized trial"
    - "No — balance on observed covariates does not ensure balance on unmeasured confounders (e.g., health consciousness, diet quality) that may still bias the estimate"
    - "Yes — propensity score matching eliminates all confounding by design"
    - "No — propensity score methods can never produce valid causal estimates"
  answer: 1
  explanation: "Propensity score methods achieve balance on observed covariates included in the propensity model. They cannot address unmeasured confounders — variables that affect both treatment and outcome but were not measured. If health-conscious people are more likely both to take statins and to have better outcomes (through diet, exercise, etc.), this confounding persists even after perfect propensity score matching. The no-unmeasured-confounders assumption is the fundamental limitation and is not testable from the data alone."

- question: "IPTW creates a pseudo-population where treatment is independent of measured confounders. A treated subject with propensity score 0.9 receives a weight of 1/0.9 ≈ 1.11, while a treated subject with propensity score 0.1 receives a weight of 1/0.1 = 10. Why does the subject with the lower propensity get a higher weight?"
  type: short-answer
  answer: "A treated subject with propensity score 0.1 is unusual — most similar people did not receive treatment. This subject is underrepresented among the treated relative to the overall population. Weighting by 1/0.1 = 10 means this subject 'represents' 10 similar people in the population, most of whom would not have been treated. The weighting creates a pseudo-population where treatment assignment is independent of the covariates, mimicking randomization. Subjects who are uncommon in their treatment group receive higher weights because they carry more information about what would happen if treatment assignment were random."
  explanation: "The intuition is analogous to survey weighting: if a demographic group is undersampled, each observed member of that group gets a higher weight to represent the unobserved members. IPTW does the same for treatment groups — making each group representative of the full population by upweighting subjects whose treatment status is surprising given their characteristics. Extreme weights (very high or very low propensity scores) can cause instability, which is why weight trimming or stabilized weights are often used."

- question: "Propensity score matching and IPTW estimate the same causal effect."
  type: true-false
  answer: false
  explanation: "Propensity score matching typically estimates the Average Treatment Effect on the Treated (ATT) — the effect among those who actually received treatment — because treated subjects are matched to similar controls. IPTW with standard weights estimates the Average Treatment Effect (ATE) — the effect if the entire population were treated versus untreated. With ATT weighting, IPTW can also estimate the ATT. The choice between ATT and ATE depends on the research question: ATT is relevant when you want to know whether treatment helped those who received it; ATE is relevant for policy decisions about treating everyone."
```

## Explainer

Randomized trials balance confounders by design, but many important clinical questions cannot be studied with randomization (it is unethical to randomize patients to smoking or not). Observational data are abundant but confounded — patients who receive treatment differ systematically from those who do not. If patients prescribed statins are older, sicker, and have higher cholesterol, a naive comparison of outcomes between statin users and non-users conflates the treatment effect with the confounding effects of age, severity, and cholesterol.

The **propensity score** collapses all measured confounders into a single number: the estimated probability of receiving treatment. Two patients with the same propensity score may differ on individual covariates but are equally likely to have been treated, given their observed characteristics. Comparing outcomes between treated and untreated subjects with similar propensity scores is analogous to comparing within strata of a randomized trial (where treatment probability is 0.5 for everyone). The key theorem (Rosenbaum and Rubin, 1983) proves that balancing on the propensity score is sufficient to balance all the observed covariates that went into its estimation.

The four implementation strategies have different practical tradeoffs. **Matching** pairs treated and untreated subjects with similar propensity scores, creating a balanced sample but potentially excluding subjects without good matches (reducing sample size and generalizability). **Stratification** divides the sample into propensity score quantiles and estimates the treatment effect within each stratum. **IPTW** weights each subject by the inverse of their probability of receiving the treatment they actually received, creating a pseudo-population where treatment is independent of observed confounders — it uses all subjects but can be unstable when propensity scores are extreme. **Covariate adjustment** includes the propensity score as a covariate in a regression model, which is the simplest approach but relies on correct specification of the outcome model.

The critical limitation is that propensity scores address only **measured** confounders. If an important confounder is not included in the propensity model — because it was not measured or not recognized as a confounder — the treatment effect estimate remains biased. This is why sensitivity analyses (e.g., Rosenbaum bounds, E-values) are essential: they quantify how strong an unmeasured confounder would need to be to explain away the observed effect. A large, robust effect that survives sensitivity analysis is more credible than a small effect that could be explained by even modest unmeasured confounding.
