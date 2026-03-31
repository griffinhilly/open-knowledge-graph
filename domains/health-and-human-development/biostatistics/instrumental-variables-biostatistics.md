---
id: instrumental-variables-biostatistics
title: Instrumental Variables in Biostatistics
domain: health-and-human-development
course: biostatistics
prerequisites:
- id: causal-inference-methods-biostatistics
  type: hard
- id: propensity-score-methods-biostatistics
  type: soft
builds-toward:
- difference-in-differences-biostatistics
tags:
- instrumental-variables
- Mendelian-randomization
- LATE
- exclusion-restriction
- two-stage
stage: expert
status: validated
---

# Instrumental Variables in Biostatistics

## Core Idea
Instrumental variables (IV) in biostatistics provide causal estimates when unmeasured confounding is present — the situation where propensity scores fail. An instrument Z must satisfy three conditions: (1) relevance — Z is associated with the treatment X, (2) independence — Z is not associated with unmeasured confounders, and (3) the exclusion restriction — Z affects the outcome Y only through X. In biostatistics, the most prominent application is Mendelian randomization, which uses genetic variants as instruments: genetic variants are randomly allocated at conception (natural randomization), are generally not confounded by lifestyle or socioeconomic factors, and affect outcomes only through the biological pathway they influence. IV estimates a Local Average Treatment Effect (LATE) — the causal effect for "compliers" whose treatment is shifted by the instrument, not for the entire population.

## Questions

```yaml
- question: "Mendelian randomization uses genetic variants associated with alcohol consumption to estimate the causal effect of alcohol on cardiovascular disease. Why are genetic variants considered better instruments than, say, alcohol taxation levels?"
  type: multiple-choice
  options:
    - "Genetic variants have larger effect sizes on alcohol consumption"
    - "Genetic variants are allocated randomly at conception (Mendel's second law), making them independent of the socioeconomic, behavioral, and environmental confounders that plague observational studies of alcohol use"
    - "Genetic variants directly affect cardiovascular disease, providing a more accurate estimate"
    - "Taxation levels are too unstable over time to be useful as instruments"
  answer: 1
  explanation: "The strength of Mendelian randomization is that genetic variants satisfy the independence condition naturally — they are randomly allocated during meiosis and are fixed at conception, before any lifestyle confounders develop. This means they are not confounded by socioeconomic status, diet, or other behaviors that confound observational studies of alcohol. Taxation could satisfy relevance but may violate independence (tax rates correlate with region, which correlates with health outcomes through many pathways). The key caveat is that the exclusion restriction must still hold — the genetic variant must affect CVD only through alcohol, not through other biological pathways (pleiotropy)."

- question: "An IV analysis of the effect of BMI on diabetes uses a genetic risk score for BMI as the instrument. The exclusion restriction requires that the genetic risk score affects diabetes only through BMI. If some of the genetic variants in the score directly affect insulin sensitivity (pleiotropy), the exclusion restriction is violated."
  type: true-false
  answer: true
  explanation: "Pleiotropy — when a genetic variant affects the outcome through pathways other than the exposure of interest — is the primary threat to the exclusion restriction in Mendelian randomization. If genetic variants that raise BMI also directly affect insulin resistance (not through BMI but through shared metabolic pathways), the IV estimate will be biased because the instrument has a direct effect on the outcome. Methods like MR-Egger regression and weighted median estimation can detect and partially correct for pleiotropy, but they require additional assumptions."

- question: "IV estimates a Local Average Treatment Effect (LATE) rather than the Average Treatment Effect (ATE). Explain this limitation and who the 'local' population is in a Mendelian randomization study."
  type: short-answer
  answer: "LATE is the causal effect for 'compliers' — the subpopulation whose treatment is actually influenced by the instrument. In Mendelian randomization of alcohol and CVD, the LATE estimates the causal effect of alcohol for people whose drinking is changed by the genetic variant. People who would drink heavily regardless of their genotype (always-takers) or abstain regardless (never-takers) are not included. This means the estimate may not generalize to the entire population if the treatment effect differs across subgroups. The LATE is a valid causal estimate for compliers but may not represent the effect of a universal policy change."
  explanation: "The LATE interpretation is often overlooked in applied IV studies. If the genetic variant shifts moderate drinkers to drink slightly less, the LATE captures the effect of a small reduction in alcohol for moderate drinkers — not the effect of heavy drinking versus abstinence, and not the effect for the entire population. This can lead to apparently paradoxical results where the IV estimate differs dramatically from the observational estimate, even after accounting for confounding, because they apply to different subpopulations."
```

## Explainer

Propensity score methods assume that all confounders are measured — a strong assumption that is often implausible. If physician prescribing decisions are based partly on clinical judgment that is not captured in the data, propensity scores cannot eliminate this confounding. **Instrumental variables** offer an alternative approach that can produce causal estimates even with unmeasured confounders, provided a valid instrument exists.

The logic of IV is intuitive: find a source of variation in treatment that is "as good as random" — independent of the confounders. If the instrument shifts treatment assignment quasi-randomly, comparing outcomes between those who were shifted toward treatment and those shifted away provides a causal estimate. The instrument acts as a natural experiment embedded within the observational data. The classic biostatistical example is **Mendelian randomization** (MR), which exploits the random assortment of genetic variants during meiosis. A genetic variant that affects alcohol metabolism creates natural variation in alcohol consumption that is independent of the socioeconomic and behavioral factors that confound observational studies.

The three IV assumptions must all hold. **Relevance** (the instrument predicts treatment) is testable — regress treatment on the instrument and check the F-statistic. **Independence** (the instrument is not confounded with the outcome) is supported by the biology of Mendelian inheritance but can be violated by population stratification or dynastic effects. The **exclusion restriction** (the instrument affects the outcome only through the treatment) is the untestable and most controversial assumption. In MR, this is violated by **pleiotropy** — when the genetic variant affects the outcome through biological pathways other than the exposure of interest.

The IV estimate has a specific causal interpretation: the **Local Average Treatment Effect** (LATE). It applies to "compliers" — the subpopulation whose treatment would change if the instrument changed. In MR, these are people whose alcohol consumption is actually modified by the genetic variant. The LATE may differ from the ATE if treatment effects are heterogeneous. A genetic variant that slightly reduces moderate drinking yields a LATE for moderate drinkers, which may not match the effect of moving from heavy drinking to abstinence. Understanding what population your IV estimate describes is as important as getting the mechanics right.
