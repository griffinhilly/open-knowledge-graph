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

## Questions

```yaml
- question: "After 5 items, a CAT algorithm estimates an examinee's ability at θ = 1.5. Which item should it select next?"
  type: multiple-choice
  options:
    - "The item with the highest difficulty parameter in the bank, regardless of θ"
    - "The item whose information function peaks nearest θ = 1.5"
    - "A randomly selected item to prevent systematic bias"
    - "The item that was most informative for a previous examinee with similar ability"
  answer: 1
  explanation: "Maximum information item selection works by identifying the item that provides the most statistical information at the current ability estimate. Each item's information function peaks at the ability level where the item is most discriminating — where a small difference in ability produces the largest difference in the probability of a correct response. Selecting the item whose peak is at θ = 1.5 means asking the most diagnostic possible question given what the test knows so far. Option A (highest difficulty) ignores where the item is informative; a very hard item has its information peak at a high θ and provides almost nothing at θ = 1.5."

- question: "Why does a pure maximum-information algorithm create practical problems for real-world CAT programs?"
  type: multiple-choice
  options:
    - "It makes real-time ability estimation computationally intractable on modern hardware"
    - "It repeatedly selects the same small set of highly informative items, enabling memorization and score inflation"
    - "It systematically ignores the Bayesian prior over the ability distribution"
    - "It consistently underestimates ability at the high and low ends of the scale"
  answer: 1
  explanation: "The maximum information algorithm, applied without constraints, will repeatedly select whichever items are most informative — and since item information functions are stable, this tends to be the same items across examinees. Examinees who take the test on different days share experiences, enabling item content to spread and allowing coached candidates to inflate scores. Real CAT programs therefore impose exposure controls (limiting how often any item is administered) and content constraints (ensuring coverage of specified topics). This transforms item selection into a constrained optimization problem, not pure information maximization."

- question: "A CAT system that selects items purely by maximum information — with no content or exposure constraints — is fully optimized for operational testing use."
  type: true-false
  answer: false
  explanation: "Pure maximum-information selection is theoretically elegant but operationally flawed. Without constraints, a small set of highly informative items gets selected repeatedly, making those items vulnerable to memorization and enabling score inflation. Content constraints are also needed to ensure the test covers the full domain as specified by the test blueprint — a test that happens to measure only a subset of content is not a valid measure of the full construct, regardless of how efficient its item selection is. Real CAT systems solve a constrained optimization problem that balances information, content representation, and item security."

- question: "A well-calibrated Bayesian prior over the ability distribution can improve early item selection in a CAT by preventing the algorithm from committing fully to a badly wrong initial ability estimate."
  type: true-false
  answer: true
  explanation: "When a CAT begins, the algorithm has no response data to work with and must start with some ability estimate. A Bayesian approach incorporates a prior — typically based on the population distribution — that pulls early estimates toward the typical range. This prevents the algorithm from chasing a fluke first response down an extreme ability level, which would select very easy or very hard items that contribute little useful information for typical examinees. As responses accumulate, the likelihood from the data comes to dominate the prior, and the two approaches converge. The prior is most valuable in the first few items."

- question: "Explain why an item provides maximum statistical information at the ability level where its characteristic curve is steepest. How does the CAT algorithm exploit this to achieve measurement efficiency?"
  type: short-answer
  answer: "An item's information function peaks where its characteristic curve is steepest because that is the region where a small difference in ability produces the largest difference in the probability of a correct response — making each response maximally diagnostic about the examinee's true ability. A CAT exploits this by maintaining a running ability estimate and always selecting the item whose information peaks nearest that estimate, effectively asking the most discriminating question possible at each step. Because every item is targeted to the individual's current estimated ability, a CAT achieves the same measurement precision as a much longer fixed-form test."
  explanation: "Technically, information I(θ) = P'(θ)² / [P(θ)(1−P(θ))], which is maximized where the slope P'(θ) is large relative to response uncertainty. The CAT's efficiency gain comes from targeting: a fixed test must be designed for the 'average' examinee, so it provides sub-optimal information for people far from the mean. A CAT dynamically adjusts to each person, keeping them at the most informative region of their personal item bank at every step — which is why 20 adaptive items can outperform 60 fixed items in measurement precision."
```

## Explainer

From your study of item response functions, you know that each item has a characteristic curve — a function that relates a person's latent ability (θ) to their probability of answering correctly. Crucially, every item also has an **information function**: a curve that describes how much statistical information that item provides at each ability level. An item contributes the most information near the ability level where there is maximum uncertainty about whether the person will pass or fail it — roughly, where the item characteristic curve is steepest. A CAT algorithm's core job is to exploit this structure: at every step, select the item that will reduce uncertainty about the examinee's true ability as much as possible.

The **maximum information** algorithm does exactly this. After each response, the algorithm updates its estimate of θ (the examinee's ability) and then selects the item from the bank with the highest information at that current estimate. Think of it as always asking the question that would be most diagnostic right now — not too hard, not too easy, but right at the edge of the examinee's current estimated ability. Because each item is targeted to the individual, a CAT using 20 items can achieve the same precision as a conventional test with 40–60 items. The savings in test time and examinee fatigue are substantial.

The **Bayesian maximum expected information** approach adds a prior distribution over θ — a belief about where examinees' abilities tend to cluster in the population — and selects items that maximize the expected reduction in posterior variance. This matters most at the beginning of a test, when few responses have been collected and the estimate is imprecise. A good prior prevents the algorithm from chasing a wildly wrong early estimate down a dead end. As responses accumulate, the data dominate the prior and the two approaches converge.

Pure information maximization has a practical flaw: it tends to overuse a small set of highly informative items, exposing them frequently and enabling **item memorization** and score inflation. Real CAT systems add **content and exposure constraints** to the item selection algorithm: items must cover specified content areas in required proportions, no item may be selected too many times across the examinee pool, and sometimes enemy items (items whose correct answer reveals another) must be kept apart. These constraints mean the algorithm is not purely optimizing information — it is solving a constrained optimization problem that balances efficiency, fairness, and test security. The design of these constraints is as much a policy decision as a psychometric one.
