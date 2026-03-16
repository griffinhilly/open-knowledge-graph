---
id: adaptive-testing-algorithms
title: Algorithms for Computerized Adaptive Testing
domain: psychology
course: psychometrics
prerequisites:
- id: computerized-adaptive-testing
  type: hard
- id: item-response-functions
  type: hard
tags:
- cat
- computerized-adaptive
- item-selection
- algorithms
- maximum-information
stage: advanced
status: draft
---

# Algorithms for Computerized Adaptive Testing

## Core Idea
Computerized Adaptive Testing (CAT) algorithms dynamically select items based on examinee responses to efficiently estimate ability while maintaining high measurement precision. Key algorithms include maximum information (selects items that maximally reduce posterior variance), maximum expected information gain (Bayesian approach), and balanced approaches that consider both information and content constraints. Algorithm choice affects test efficiency and fairness.

## Explainer

From your study of item response functions, you know that each item has a characteristic curve — a function that relates a person's latent ability (θ) to their probability of answering correctly. Crucially, every item also has an **information function**: a curve that describes how much statistical information that item provides at each ability level. An item contributes the most information near the ability level where there is maximum uncertainty about whether the person will pass or fail it — roughly, where the item characteristic curve is steepest. A CAT algorithm's core job is to exploit this structure: at every step, select the item that will reduce uncertainty about the examinee's true ability as much as possible.

The **maximum information** algorithm does exactly this. After each response, the algorithm updates its estimate of θ (the examinee's ability) and then selects the item from the bank with the highest information at that current estimate. Think of it as always asking the question that would be most diagnostic right now — not too hard, not too easy, but right at the edge of the examinee's current estimated ability. Because each item is targeted to the individual, a CAT using 20 items can achieve the same precision as a conventional test with 40–60 items. The savings in test time and examinee fatigue are substantial.

The **Bayesian maximum expected information** approach adds a prior distribution over θ — a belief about where examinees' abilities tend to cluster in the population — and selects items that maximize the expected reduction in posterior variance. This matters most at the beginning of a test, when few responses have been collected and the estimate is imprecise. A good prior prevents the algorithm from chasing a wildly wrong early estimate down a dead end. As responses accumulate, the data dominate the prior and the two approaches converge.

Pure information maximization has a practical flaw: it tends to overuse a small set of highly informative items, exposing them frequently and enabling **item memorization** and score inflation. Real CAT systems add **content and exposure constraints** to the item selection algorithm: items must cover specified content areas in required proportions, no item may be selected too many times across the examinee pool, and sometimes enemy items (items whose correct answer reveals another) must be kept apart. These constraints mean the algorithm is not purely optimizing information — it is solving a constrained optimization problem that balances efficiency, fairness, and test security. The design of these constraints is as much a policy decision as a psychometric one.
