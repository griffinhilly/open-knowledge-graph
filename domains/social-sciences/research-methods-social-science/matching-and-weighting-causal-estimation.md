---
id: matching-and-weighting-causal-estimation
title: 'Matching, Stratification, and Weighting: Creating Comparable Groups'
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: propensity-score-methods
  type: hard
- id: causal-inference-from-observation
  type: soft
- id: probability-mass-functions
  type: soft
- id: optimization-multivariable-basics
  type: soft
tags:
- matching
- stratification
- weighting
- covariate-balance
stage: expert
status: validated
---

# Matching, Stratification, and Weighting: Creating Comparable Groups

## Core Idea
Matching, stratification, and weighting create comparable groups by balancing covariate distributions between treated and control units. Propensity score methods use a summary of confounders for balance. These identify causal effects under unconfoundedness.

## Questions

```yaml
- question: "A researcher uses propensity score matching to compare earnings outcomes between participants and non-participants in a job training program. After matching, the treated and control groups are nearly identical on age, education, prior earnings, and region. The researcher concludes she has obtained an unbiased causal estimate. What is the most serious threat to this conclusion?"
  type: multiple-choice
  options:
    - "The propensity score model might be misspecified, assigning slightly wrong weights"
    - "Unmeasured confounders — such as motivation or employer discrimination — could still differ between groups, causing bias that matching on observed covariates cannot remove"
    - "The sample size is too small to detect effects reliably"
    - "Propensity score matching cannot be used for labor market studies; it is designed for medical trials"
  answer: 1
  explanation: "Matching and weighting methods identify causal effects only under the unconfoundedness assumption: all variables that jointly influence treatment selection and the outcome must be measured and conditioned on. Even perfect covariate balance on observed covariates does not help if important confounders — like motivation, social networks, or employer attitudes — were never measured. These unmeasured variables remain as selection bias. This is the fundamental limitation these methods cannot overcome by design: they are as good as the covariate set you bring to them. Options A, C, and D identify real concerns but are less severe than unmeasured confounding."

- question: "Inverse probability weighting (IPW) and exact matching both aim to estimate causal effects from observational data. What is the key difference in how they create comparability?"
  type: multiple-choice
  options:
    - "IPW requires a randomized experiment; exact matching works on observational data"
    - "Exact matching selects a subset of similar paired units; IPW reweights the full sample so the control group's covariate distribution resembles the treated group"
    - "IPW can only be used for binary outcomes; matching works for continuous outcomes"
    - "Exact matching uses the propensity score as a summary; IPW requires matching on each covariate individually"
  answer: 1
  explanation: "Exact matching and IPW differ in strategy, not goal. Exact matching finds individual control units who are similar to each treated unit and pairs them — discarding unmatched cases. IPW keeps the entire sample but assigns weights so that control units who 'look like' treated units receive high weight in the analysis and those who don't receive low weight. Both rest on the same identifying assumption (unconfoundedness), but they use different portions of the data and make different trade-offs between efficiency and bias. Option D reverses the description — propensity score matching uses the propensity score as a summary, while exact matching matches on individual covariates."

- question: "After successfully matching treated and control units on all measured covariates using propensity score matching, the resulting estimate may still be biased if important confounders were not measured before the study."
  type: true-false
  answer: true
  explanation: "This is the central limitation of all observational matching methods. Covariate balance after matching confirms that the groups are comparable on *measured* variables, but unmeasured confounders remain unaffected. The unconfoundedness assumption — that conditioning on observed covariates is sufficient to remove selection bias — cannot be tested from the data; it is a substantive claim about the data-generating process. If a researcher forgot to measure motivation, social networks, or any variable correlated with both treatment and outcome, the causal estimate absorbs that bias regardless of how well the matching performed on measured variables."

- question: "Achieving good covariate balance after propensity score matching is sufficient to verify that the unconfoundedness assumption holds."
  type: true-false
  answer: false
  explanation: "Covariate balance (treated and control groups being similar on measured covariates) is a diagnostic for the *quality of the matching*, not a test of unconfoundedness. Unconfoundedness requires that *all* confounders — measured and unmeasured — are balanced. Balance checks can only speak to measured variables. The unconfoundedness assumption is fundamentally untestable from observed data alone: you cannot check whether an unmeasured variable you didn't collect is unbalanced. Good balance after matching is necessary but not sufficient — it must be supplemented by substantive arguments that the measured covariate set is complete."

- question: "Why is the unconfoundedness assumption (also called ignorability) the central identifying assumption in matching and weighting methods, and why can it not be tested using the observed data?"
  type: short-answer
  answer: "Unconfoundedness requires that all variables jointly influencing treatment selection and the outcome have been measured and included in the covariate set. Without this, selection bias remains in the comparison even after perfect covariate balance on measured variables — unmeasured confounders still create systematic differences between groups. It cannot be tested from observed data because testing it would require knowing the potential outcomes for units under conditions they did not experience (the fundamental problem of causal inference). You can check balance on measured covariates, conduct sensitivity analyses, or argue substantively that the covariate set is complete, but no statistical test can verify the assumption from the data alone."
  explanation: "Students often think that a good propensity score model and post-matching balance checks are sufficient validation of the causal design. The key insight is that matching 'buys' comparability only on what was measured — it cannot help with what was never observed. The assumption is substantive, not statistical, and its plausibility depends entirely on domain knowledge about what drives treatment selection."
```

## Explainer

The core problem these methods address is one you already understand from causal inference: in observational data, treatment and control groups differ not just in their treatment status but in the background characteristics that led to treatment in the first place. People who receive a job training program tend to be more motivated than those who don't; countries that adopt a policy tend to differ systematically from those that don't. Naive comparisons produce **confounding bias** — the treatment effect is mixed up with the effect of these background differences. Matching, stratification, and weighting all attack this problem by constructing comparison groups that are as similar as possible to the treated group on observed confounders.

**Exact matching** is the most intuitive approach: for each treated unit, find a control unit with identical values on all confounders. A 45-year-old woman with a college degree who lives in a urban county gets matched to another 45-year-old woman with a college degree who lives in an urban county but did not receive treatment. The treatment effect estimate is the average difference in outcomes across matched pairs. The problem is the **curse of dimensionality** — with many confounders, exact matches become impossible because no two units share the same profile across ten or twenty variables. This is why propensity score methods, which you studied in your prerequisite, are so useful: they collapse all the confounders into a single number (the predicted probability of treatment), so matching on one dimension achieves approximate balance on all.

**Stratification** divides the sample into strata (blocks) with similar propensity scores and estimates the treatment effect within each stratum, then averages across strata. **Inverse probability weighting (IPW)** takes a different approach: rather than selecting matched pairs, it reweights the entire sample so that the covariate distribution in the control group resembles the treated group. Units in the control group who look like treated units receive high weights; those who don't look like treated units receive low weights. Both approaches rest on the same mathematical insight — that under **unconfoundedness** (all confounders observed and measured), the propensity score is sufficient to remove selection bias.

The assumptions underlying these methods deserve scrutiny. Unconfoundedness — also called **ignorability** or "no unmeasured confounders" — is the key identifying assumption, and it cannot be tested from the data itself. It requires that you have measured every variable that jointly influences treatment assignment and the outcome. In practice this means that these methods are only as good as your covariate set: variables you forgot to measure or cannot measure (parental motivation, employer discrimination) remain as unmeasured confounders. The other assumption is **overlap** (or common support) — for every value of the covariates, there must be some probability of being in either treatment or control. If a certain type of person *always* receives treatment and *never* doesn't, there is no valid counterfactual for them. Diagnostics like checking propensity score distributions and testing covariate balance after matching — not before — are how you evaluate whether these assumptions hold in practice and whether your comparison groups are genuinely comparable.


