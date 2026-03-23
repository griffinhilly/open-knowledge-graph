---
id: competing-risks-analysis
title: Competing Risks Analysis
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: cox-proportional-hazards
  type: hard
- id: kaplan-meier-estimator
  type: hard
tags:
- survival-analysis
- competing-events
- cumulative-incidence
stage: expert
status: draft
---

# Competing Risks Analysis

## Core Idea
Competing risks occur when individuals may experience one of several mutually exclusive events. Standard Kaplan-Meier and Cox methods are inappropriate because censoring is not independent. Cumulative incidence functions and competing risk regression properly estimate the probability of each event.

## Questions

```yaml
- question: "In a study of cancer mortality among elderly patients, 30% of participants die of heart disease before the study ends. If researchers treat heart disease deaths as censored in a Kaplan-Meier analysis of cancer mortality, what will happen to their estimated cancer mortality probability?"
  type: multiple-choice
  options:
    - "It will be unbiased, because KM handles censoring correctly by design"
    - "It will be underestimated, because removing heart disease deaths reduces the effective sample size"
    - "It will be overestimated, because censored patients are assumed to continue facing cancer mortality risk they no longer actually face"
    - "It will be correct only if heart disease and cancer risks are uncorrelated in the population"
  answer: 2
  explanation: "When a patient dies of heart disease, they can never subsequently die of cancer — the competing event eliminates the cancer risk entirely. KM treats these patients as if they were merely lost to follow-up, implicitly assuming they continue to face the same cancer mortality risk as surviving patients. This inflates the estimated probability because the denominator of 'surviving and at risk' patients is too large. In elderly populations with high competing mortality, this overestimation can be dramatic — sometimes double the true probability."

- question: "A trialist wants to know: 'Does treatment A reduce the probability that a patient will eventually die of cardiovascular disease?' A statistician recommends Fine-Gray subdistribution hazard regression rather than cause-specific Cox regression. Why?"
  type: multiple-choice
  options:
    - "Fine-Gray handles non-proportional hazards better than cause-specific Cox regression"
    - "Fine-Gray directly models the cumulative incidence function, so its coefficients reflect the treatment effect on the observable probability of the event"
    - "Cause-specific Cox regression cannot be used when competing events are present"
    - "Fine-Gray requires fewer modeling assumptions than cause-specific Cox regression"
  answer: 1
  explanation: "The key is what each model estimates. Cause-specific Cox regression models the hazard among those still at risk — it answers 'does treatment affect the underlying cardiovascular disease process?' Fine-Gray directly models a covariate's effect on the CIF — the probability a patient will experience the event — which is exactly what the trialist wants. The choice is scientific, not statistical: both models make proportional hazards assumptions; neither handles non-proportionality better. Cause-specific regression can absolutely be used when competing events are present."

- question: "The sum of the cumulative incidence functions for all competing events at any time point t equals 1."
  type: true-false
  answer: false
  explanation: "The CIFs for all competing events sum to 1 − S(t), where S(t) is the overall survival probability. This is less than 1 because survival is always possible — at time t, some individuals have not yet experienced any event. The CIFs partition the probability of having had some event by time t, not the total probability mass. Only as t → ∞ (and assuming everyone eventually experiences an event) would the sum approach 1."

- question: "When competing risks are present, Fine-Gray subdistribution regression is statistically superior to cause-specific Cox regression because it uses more of the data."
  type: true-false
  answer: false
  explanation: "This framing misunderstands the relationship. Fine-Gray and cause-specific Cox regression are not competitors where one is 'better' — they answer fundamentally different scientific questions. Fine-Gray asks how a covariate affects the probability of experiencing this event, accounting for competing events. Cause-specific asks how a covariate affects the biological hazard of this event among those still at risk. The choice depends on the research question, not on statistical efficiency. Choosing between them is a scientific decision, not a modeling one."

- question: "Explain why treating competing events as censored in Kaplan-Meier analysis violates the independent censoring assumption, and what the practical consequence is."
  type: short-answer
  answer: "Independent censoring requires that the reason a subject leaves observation tells you nothing about their underlying event risk. When a patient dies of a competing cause, their removal is informative: they faced real mortality risk and experienced a different real event. Unlike administrative censoring (end of study, moved away), a competing event permanently eliminates the possibility of the primary event. Treating these deaths as censored implicitly assumes they continue to face the primary event risk at the same rate as survivors, which is false. The practical consequence is that 1 − KM(t) overstates the cumulative incidence of the primary event, because the risk pool is treated as larger than it actually is."
  explanation: "The distinction is between 'lost to follow-up' (potentially random) and 'competing event occurred' (a definitive, informative outcome). Independent censoring is violated because subjects censored by a competing event are systematically different from truly at-risk subjects — they are no longer alive to experience the primary event."
```

## Explainer

From Kaplan-Meier and Cox regression you know the fundamental survival analysis setup: individuals enter a study, some experience the event of interest, and those who don't are **censored** at their last follow-up time. The crucial assumption in that framework is **independent censoring** — the reason a person leaves observation (moves away, withdraws, study ends) tells you nothing about their underlying event risk. Competing risks arise when that assumption fails in a particular structural way: a person can be removed from risk not by administrative censoring but by experiencing a *different, real event* that makes the first event permanently impossible.

The canonical example: in a study of cause-specific mortality from cancer, a patient who dies of a heart attack can never subsequently die of cancer. The heart attack death is not administrative censoring — it is an informative event that eliminates the cancer death risk entirely. If you treat competing events as censored (the naïve KM approach), you implicitly assume the censored person continues to face the same hazard as the survivors, which is false. The result is that 1 − KM(t) overstates the probability of the event of interest, sometimes dramatically. In a population of elderly patients with many competing causes of death, a KM-based "cancer mortality probability" of 40% might actually correspond to a true probability of 20%, because the KM estimate ignores that many patients will die of something else first.

The correct tool is the **cumulative incidence function (CIF)**, sometimes called the **subdistribution function**. The CIF for event type k is defined as the probability of experiencing event k by time t, allowing for the fact that competing events can occur first: CIF_k(t) = P(T ≤ t, event type = k). Notice that the sum of all cause-specific CIFs equals 1 − S(t), where S(t) is the overall survival probability. This is the right way to partition risk: the CIFs for all competing events add up to the probability of having experienced *any* event by time t. They do not add up to 1 because surviving is always a possibility.

For regression, two distinct approaches exist and answer different questions. **Cause-specific Cox regression** models the hazard of event k among those still at risk (having experienced neither k nor any competing event). This is appropriate when you want to understand the biological or mechanistic relationship between a covariate and one particular event process. **Fine and Gray's subdistribution hazard regression** directly models a covariate's effect on the CIF — it keeps individuals who experienced a competing event in the risk set (with a downweighted contribution), making the model directly linked to the observable cumulative probability. When the question is "how does treatment affect the probability a patient will experience this specific event," Fine-Gray answers it directly. When the question is "does treatment affect the underlying disease process," cause-specific hazards are more appropriate. Choosing between them is a scientific question about what you want to estimate, not a statistical one about which model fits better.

