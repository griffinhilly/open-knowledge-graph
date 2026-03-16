---
id: polytomous-irt-models
title: Polytomous Item Response Theory Models
domain: psychology
course: psychometrics
prerequisites:
- id: item-response-functions
  type: hard
- id: two-parameter-logistic-model
  type: hard
builds-toward:
- dimensional-assessment-and-bifactor-models
tags:
- irt
- ordered-responses
- rating-scales
- partial-credit
- graded-response
stage: advanced
status: draft
---

# Polytomous Item Response Theory Models

## Core Idea
Polytomous IRT models extend the binary right/wrong framework to ordered categorical responses, such as Likert-scale ratings, partial-credit items on math tests, or confidence judgments. Models like the Graded Response Model (GRM) and Generalized Partial Credit Model (GPCM) extract more information from each item response than classical test theory and provide nuanced item-level diagnostics.

## How It's Best Learned
Work with real rating-scale data from personality or attitude measures. Fit GRM and GPCM models and interpret item threshold parameters (step difficulties) and discrimination parameters. Compare results to classical item statistics to understand what additional information polytomous IRT provides.

## Common Misconceptions
- Assuming that all ordered response categories contribute equally to measurement precision; middle categories often have lower information.
- Treating polytomous responses as interval-scaled when they are ordinal; IRT models respect the ordering without assuming equal intervals.
- Using classical item-total correlations for category-level analysis when polytomous IRT is more appropriate.

## Explainer

In the binary IRT framework you know from the 2PL model, every item has one **item response function (IRF)**: a sigmoid curve showing the probability of a correct response as a function of latent trait θ. The 2PL parameterizes this curve with two numbers — difficulty (b) and discrimination (a). Now consider a 5-point Likert item ("Strongly Disagree" to "Strongly Agree") assessing conscientiousness. There is no single "correct" response, but there are *ordered* responses, and each step up the scale should become more likely as θ increases. Polytomous IRT handles exactly this structure.

Instead of one IRF, a polytomous item generates a family of **category response functions (CRFs)** — one curve per response option. Each CRF shows the probability of endorsing *exactly* that category as a function of θ. For a well-functioning 5-point item, the "Strongly Disagree" curve peaks at low θ, the "Disagree" curve peaks slightly higher, and so on, with "Strongly Agree" dominating only at high θ. The parameters separating adjacent categories are called **threshold parameters** (or step difficulties) — the θ level at which adjacent categories are equally probable. A model with k response categories has k-1 thresholds.

The two most important polytomous IRT models differ in a key assumption. The **Graded Response Model (GRM)** models cumulative probabilities — the probability of responding at category k *or higher* — using a separate 2PL-like function for each boundary. It imposes an ordered structure and allows categories to differ only in their thresholds while sharing a single discrimination parameter. The **Generalized Partial Credit Model (GPCM)** models adjacent-category transitions directly and is more flexible, allowing the discrimination to vary across items. In practice, GRM is common for personality and attitude scales where the ordered-category assumption is firm; GPCM is common for partial-credit academic items where different steps may be qualitatively different in difficulty.

The payoff over classical approaches is richer item diagnostics. In CTT, a Likert item yields a single item-total correlation. In polytomous IRT, you can inspect whether each *category* is functioning: are some response categories never endorsed? Do adjacent categories have nearly identical thresholds, making them redundant? Is the middle category attracting both low- and high-θ respondents (non-monotonic CRF), suggesting it represents "indecision" rather than a true midpoint? These diagnostics often reveal that 5-category scales should be collapsed to 4 or even 3 because the middle categories aren't providing distinct information. This is the measurement precision advantage that polytomous IRT delivers over classical item analysis.
