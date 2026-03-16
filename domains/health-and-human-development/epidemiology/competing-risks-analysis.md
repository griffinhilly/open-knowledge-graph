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
stage: advanced
status: draft
---

# Competing Risks Analysis

## Core Idea
Competing risks occur when individuals may experience one of several mutually exclusive events. Standard Kaplan-Meier and Cox methods are inappropriate because censoring is not independent. Cumulative incidence functions and competing risk regression properly estimate the probability of each event.

## Explainer

From Kaplan-Meier and Cox regression you know the fundamental survival analysis setup: individuals enter a study, some experience the event of interest, and those who don't are **censored** at their last follow-up time. The crucial assumption in that framework is **independent censoring** — the reason a person leaves observation (moves away, withdraws, study ends) tells you nothing about their underlying event risk. Competing risks arise when that assumption fails in a particular structural way: a person can be removed from risk not by administrative censoring but by experiencing a *different, real event* that makes the first event permanently impossible.

The canonical example: in a study of cause-specific mortality from cancer, a patient who dies of a heart attack can never subsequently die of cancer. The heart attack death is not administrative censoring — it is an informative event that eliminates the cancer death risk entirely. If you treat competing events as censored (the naïve KM approach), you implicitly assume the censored person continues to face the same hazard as the survivors, which is false. The result is that 1 − KM(t) overstates the probability of the event of interest, sometimes dramatically. In a population of elderly patients with many competing causes of death, a KM-based "cancer mortality probability" of 40% might actually correspond to a true probability of 20%, because the KM estimate ignores that many patients will die of something else first.

The correct tool is the **cumulative incidence function (CIF)**, sometimes called the **subdistribution function**. The CIF for event type k is defined as the probability of experiencing event k by time t, allowing for the fact that competing events can occur first: CIF_k(t) = P(T ≤ t, event type = k). Notice that the sum of all cause-specific CIFs equals 1 − S(t), where S(t) is the overall survival probability. This is the right way to partition risk: the CIFs for all competing events add up to the probability of having experienced *any* event by time t. They do not add up to 1 because surviving is always a possibility.

For regression, two distinct approaches exist and answer different questions. **Cause-specific Cox regression** models the hazard of event k among those still at risk (having experienced neither k nor any competing event). This is appropriate when you want to understand the biological or mechanistic relationship between a covariate and one particular event process. **Fine and Gray's subdistribution hazard regression** directly models a covariate's effect on the CIF — it keeps individuals who experienced a competing event in the risk set (with a downweighted contribution), making the model directly linked to the observable cumulative probability. When the question is "how does treatment affect the probability a patient will experience this specific event," Fine-Gray answers it directly. When the question is "does treatment affect the underlying disease process," cause-specific hazards are more appropriate. Choosing between them is a scientific question about what you want to estimate, not a statistical one about which model fits better.

