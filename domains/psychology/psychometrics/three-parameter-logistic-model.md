---
id: three-parameter-logistic-model
title: Three-Parameter Logistic IRT Model (3PL)
domain: psychology
course: psychometrics
prerequisites:
- id: two-parameter-logistic-model
  type: hard
builds-toward:
- irt-model-fit-comparison
- differential-item-functioning
tags:
- 3pl
- guessing-parameter
- multiple-choice
- item-response-theory
stage: advanced
status: draft
---

# Three-Parameter Logistic IRT Model (3PL)

## Core Idea
The 3PL model adds a pseudo-guessing parameter to item difficulty and discrimination, accounting for the possibility that low-ability examinees answer difficult items correctly by chance. This is particularly valuable for multiple-choice tests but introduces estimation challenges and interpretive complexities.

## How It's Best Learned
Compare 3PL parameter estimates across items and examine how estimated guessing parameters vary. Understand when 3PL complexity adds practical value versus when 2PL or Rasch models suffice.

## Common Misconceptions
All multiple-choice data require 3PL modeling. Sometimes 2PL fits adequately, especially for well-designed items. Confusing the guessing parameter with careless mistakes; the parameter reflects systematic chance-level performance.

## Explainer

From the two-parameter logistic model, you already have two parameters describing each item: **difficulty** (*b*, the ability level where a person has a 50% chance of answering correctly) and **discrimination** (*a*, how steeply the item characteristic curve rises around *b*, indicating how well the item distinguishes between adjacent ability levels). The item characteristic curve (ICC) in a 2PL model is an S-shaped logistic function that starts at 0 for very low ability and asymptotes at 1.0 for very high ability. This works well for constructed-response or short-answer items, where guessing is negligible. But for multiple-choice tests, the 2PL's lower asymptote of 0 is unrealistic.

The **3PL model** adds a third parameter, *c*, called the **pseudo-guessing parameter** (or lower asymptote parameter). It represents the probability that a person with very low ability answers the item correctly — essentially, the floor below which correct responses can't go regardless of how low ability is. For a four-option multiple-choice item, even an examinee who knows nothing has roughly a 25% chance of selecting the correct answer by random guessing. The *c* parameter captures this, shifting the lower asymptote of the ICC upward from 0 to some value near (but not necessarily equal to) 1/k, where k is the number of options. The ICC for a 3PL item is: P(θ) = c + (1 − c) × logistic(a(θ − b)). As θ increases, the probability of a correct response rises from *c* toward 1, with the slope and midpoint governed by *a* and *b* as before.

Why not always use 3PL? Estimation. Adding a third parameter increases model complexity and requires substantially larger samples to get stable estimates — typically 1,000+ examinees for reliable *c* estimation, compared to a few hundred for 1PL or 2PL. The *c* parameter is also notoriously difficult to estimate precisely; it is correlated with *b* in the likelihood surface, creating flat regions where many combinations of *c* and *b* fit the data nearly equally well. In practice, *c* parameters are often fixed at a theoretical value (1/k) or constrained during estimation to reduce instability.

The practical question is always: does the added complexity pay off? For well-designed items with effective distractors, examinees with low ability may not guess randomly — they may systematically choose an attractive wrong answer, resulting in empirical lower asymptotes near zero even on multiple-choice items. In such cases, a 2PL fits adequately and provides cleaner parameter estimates. The 3PL earns its complexity when items are susceptible to systematic chance-level performance — typically speeded tests, items with obviously wrong distractors, or situations where test-takers with no relevant knowledge can exploit item-writing flaws. The key diagnostic is examining the lower tail of the empirical ICC: if low-ability examinees are performing at chance levels above what the 2PL predicts, the 3PL's *c* parameter is doing useful work.
