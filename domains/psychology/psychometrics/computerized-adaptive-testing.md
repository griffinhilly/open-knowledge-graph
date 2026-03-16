---
id: computerized-adaptive-testing
title: Computerized Adaptive Testing and Dynamic Assessment
domain: psychology
course: psychometrics
prerequisites:
- id: two-parameter-logistic-model
  type: hard
- id: item-response-functions
  type: hard
tags:
- cat
- adaptive-testing
- item-bank
- efficiency
stage: advanced
status: draft
---

# Computerized Adaptive Testing and Dynamic Assessment

## Core Idea
Computerized adaptive testing selects items based on continuously updated ability estimates, presenting harder items after correct responses and easier items after incorrect responses. This substantially reduces test length while maintaining measurement precision. CAT requires large calibrated item banks, sophisticated selection algorithms, and IRT parameter estimates.

## How It's Best Learned
Simulate CAT selection algorithms or participate in actual CAT assessments. Understand item exposure control and stopping rule design.

## Common Misconceptions
CAT always reduces testing time. Poor stopping rules can result in lengthy tests. CAT requires perfect item bank calibration; biased or poorly calibrated items propagate through the adaptive algorithm.

## Explainer

Your prerequisites on item response functions and the two-parameter logistic model established that each test item has a characteristic curve — a function that maps a person's latent ability (θ) to the probability of a correct response, shaped by the item's difficulty (b) and discrimination (a). The key insight now is that this model makes items *individually informative at particular ability levels*: a very hard item tells you almost nothing about a low-ability examinee (they'll get it wrong regardless), and an easy item tells you almost nothing about a high-ability examinee (they'll get it right regardless). **Computerized adaptive testing (CAT)** exploits this property: instead of giving everyone the same fixed set of items, it continuously selects items that are maximally informative for each individual's *current* ability estimate.

The algorithm works as a feedback loop. The test begins with an item of moderate difficulty (or a routing item to establish a rough starting estimate). After the examinee responds, the system updates its estimate of θ using maximum likelihood estimation or Bayesian methods applied to the IRT model. It then selects the next item from a **calibrated item bank** — a large pool of items with known IRT parameters — choosing the item that provides the most Fisher information at the current θ estimate. Correct response → estimate moves up → next item is harder. Incorrect response → estimate moves down → next item is easier. This process converges on an accurate estimate far faster than a fixed-length test because every item is optimally targeted.

The efficiency gains are substantial but conditional. CAT typically achieves the same measurement precision as a fixed-length test using roughly 50–60% as many items — a major advantage in high-stakes testing (fewer fatigue effects) and screening contexts (shorter administration time). However, this efficiency depends entirely on the quality of the item bank. **Item bank calibration** — the process of estimating IRT parameters for each item in the pool — requires large samples (often 300–1,000 responses per item) and must be periodically refreshed. Biased or poorly calibrated items cause the algorithm to misestimate θ from the first error, and subsequent selections compound the problem rather than correcting it.

Two additional design problems define CAT in practice. **Stopping rules** determine when the test ends: you can stop after a fixed number of items, when the standard error of the θ estimate drops below a threshold, or when a classification decision (pass/fail) reaches sufficient certainty. Weak stopping rules can produce unnecessarily long tests or premature termination with low precision. **Item exposure control** is a security concern: without constraints, the algorithm selects the most discriminating items for nearly every examinee, causing a small subset of items to be overexposed — memorized and shared — while most of the item bank sits unused. Modern CAT systems use exposure control algorithms (like the Sympson-Hetter method) that probabilistically cap item selection rates, trading a small amount of efficiency for test security.


