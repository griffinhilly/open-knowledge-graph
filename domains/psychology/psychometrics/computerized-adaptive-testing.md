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
stage: expert
status: draft
---

# Computerized Adaptive Testing and Dynamic Assessment

## Core Idea
Computerized adaptive testing selects items based on continuously updated ability estimates, presenting harder items after correct responses and easier items after incorrect responses. This substantially reduces test length while maintaining measurement precision. CAT requires large calibrated item banks, sophisticated selection algorithms, and IRT parameter estimates.

## How It's Best Learned
Simulate CAT selection algorithms or participate in actual CAT assessments. Understand item exposure control and stopping rule design.

## Common Misconceptions
CAT always reduces testing time. Poor stopping rules can result in lengthy tests. CAT requires perfect item bank calibration; biased or poorly calibrated items propagate through the adaptive algorithm.

## Questions

```yaml
- question: "A CAT system's item bank was calibrated using only 50 responses per item rather than the recommended 300–1,000. What is the most likely consequence for the adaptive algorithm?"
  type: multiple-choice
  options:
    - "The test will consistently overestimate examinees' true ability since small calibration samples inflate discrimination parameters"
    - "The algorithm will default to fixed-length behavior, selecting items non-adaptively until calibration is refreshed"
    - "Biased IRT parameter estimates will cause the algorithm to misestimate θ from early items, with each subsequent selection compounding the error"
    - "The test will automatically lengthen to compensate for the reduced precision of each item selection"
  answer: 2
  explanation: "CAT efficiency depends entirely on the accuracy of the IRT parameters stored in the item bank. If parameters are estimated from small samples, they carry substantial error — an item's true difficulty or discrimination may differ significantly from its calibrated value. When the algorithm selects items based on these wrong parameters, the θ estimate starts diverging from the examinee's true ability. Because each subsequent item selection uses the current θ estimate, errors propagate and compound rather than self-correcting. This is why large calibration samples are a non-negotiable requirement for CAT, not an efficiency concern."

- question: "Why might a CAT administration take as many items as a fixed-length test, even though CAT is generally described as more efficient?"
  type: multiple-choice
  options:
    - "CAT is only more efficient for average-ability examinees; high- and low-ability examinees always require more items"
    - "Poorly designed stopping rules — such as requiring the standard error to drop below an overly stringent threshold — can require many more items than necessary before the test terminates"
    - "Item exposure control forces the algorithm to use low-information items for security reasons, increasing the total items needed"
    - "CAT is more efficient only when the ability distribution is known in advance; otherwise it defaults to fixed-length length"
  answer: 1
  explanation: "CAT's efficiency advantage is real but conditional. Stopping rules determine when enough information has been gathered. A rule that terminates when the standard error of θ falls below 0.20 will require far more items than one that terminates at 0.30 — and for examinees near decision boundaries (in pass/fail tests), precision requirements can demand many more items than average. A naive stopping rule (e.g., always administer exactly 20 items) ignores these dynamics. Efficient CAT design requires matching the stopping rule to the precision needs of the testing purpose."

- question: "CAT always produces shorter tests than fixed-length tests measuring the same construct with the same precision."
  type: true-false
  answer: false
  explanation: "CAT typically achieves the same precision as a fixed-length test with 50–60% of the items — but only under good conditions: a well-calibrated item bank, appropriate stopping rules, and sufficient item diversity. Poor stopping rules can require more items than necessary; a small or poorly calibrated item bank limits the algorithm's options. In practice, CAT produces shorter tests than fixed-length tests only when designed and maintained carefully. The efficiency is conditional, not guaranteed."

- question: "In a CAT system, a correct response to a difficult item provides more information about a high-ability examinee than the same correct response provides about a low-ability examinee."
  type: true-false
  answer: true
  explanation: "This follows directly from item response theory. Each item's information function peaks at the ability level where the item is most discriminating — typically near the item's difficulty parameter. A difficult item has near-zero information for a low-ability examinee because they would almost certainly get it wrong regardless of small θ differences. For a high-ability examinee whose θ is near the item's difficulty, a correct response substantially narrows the ability estimate. This is why CAT routes hard items to examinees with high current θ estimates: those items carry maximal information there."

- question: "Why does overexposure of high-discrimination items in a CAT system threaten test validity, and how does item exposure control address this?"
  type: short-answer
  answer: "High-discrimination items are the algorithm's first choice for nearly every examinee because they provide maximum Fisher information across a wide ability range. Without constraints, a small subset of items would be selected repeatedly while most of the bank sits unused. Overexposed items become known to test-takers through item-sharing networks, allowing coached candidates to answer correctly regardless of true ability — inflating scores and destroying the validity of the measurement. Exposure control algorithms (like Sympson-Hetter) cap the probability that any item is selected at each administration, forcing the algorithm to use a broader range of items. This trades a small reduction in optimal efficiency for security and long-term validity."
  explanation: "Test security and measurement efficiency are in fundamental tension in CAT. The most efficient algorithm exploits the highest-information items every time; a secure algorithm distributes usage across the bank. Exposure control formalizes this tradeoff. The result is that real-world CAT systems are never operating at theoretical maximum efficiency — they are optimizing the combination of efficiency and item security within operational constraints."
```

## Explainer

Your prerequisites on item response functions and the two-parameter logistic model established that each test item has a characteristic curve — a function that maps a person's latent ability (θ) to the probability of a correct response, shaped by the item's difficulty (b) and discrimination (a). The key insight now is that this model makes items *individually informative at particular ability levels*: a very hard item tells you almost nothing about a low-ability examinee (they'll get it wrong regardless), and an easy item tells you almost nothing about a high-ability examinee (they'll get it right regardless). **Computerized adaptive testing (CAT)** exploits this property: instead of giving everyone the same fixed set of items, it continuously selects items that are maximally informative for each individual's *current* ability estimate.

The algorithm works as a feedback loop. The test begins with an item of moderate difficulty (or a routing item to establish a rough starting estimate). After the examinee responds, the system updates its estimate of θ using maximum likelihood estimation or Bayesian methods applied to the IRT model. It then selects the next item from a **calibrated item bank** — a large pool of items with known IRT parameters — choosing the item that provides the most Fisher information at the current θ estimate. Correct response → estimate moves up → next item is harder. Incorrect response → estimate moves down → next item is easier. This process converges on an accurate estimate far faster than a fixed-length test because every item is optimally targeted.

The efficiency gains are substantial but conditional. CAT typically achieves the same measurement precision as a fixed-length test using roughly 50–60% as many items — a major advantage in high-stakes testing (fewer fatigue effects) and screening contexts (shorter administration time). However, this efficiency depends entirely on the quality of the item bank. **Item bank calibration** — the process of estimating IRT parameters for each item in the pool — requires large samples (often 300–1,000 responses per item) and must be periodically refreshed. Biased or poorly calibrated items cause the algorithm to misestimate θ from the first error, and subsequent selections compound the problem rather than correcting it.

Two additional design problems define CAT in practice. **Stopping rules** determine when the test ends: you can stop after a fixed number of items, when the standard error of the θ estimate drops below a threshold, or when a classification decision (pass/fail) reaches sufficient certainty. Weak stopping rules can produce unnecessarily long tests or premature termination with low precision. **Item exposure control** is a security concern: without constraints, the algorithm selects the most discriminating items for nearly every examinee, causing a small subset of items to be overexposed — memorized and shared — while most of the item bank sits unused. Modern CAT systems use exposure control algorithms (like the Sympson-Hetter method) that probabilistically cap item selection rates, trading a small amount of efficiency for test security.


