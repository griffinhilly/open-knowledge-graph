---
id: absence-of-evidence
title: "Absence of Evidence Is Evidence of Absence"
domain: philosophy
course: applied-rationality
prerequisites:
  - id: bayesian-thinking-in-practice
    type: hard
  - id: conservation-of-expected-evidence
    type: soft
builds-toward:
  - extraordinary-claims-and-evidence-scaling
tags: ["bayesian", "evidence", "probability", "reasoning"]
stage: advanced
status: draft
---

## Core Idea

The saying "absence of evidence is not evidence of absence" is probabilistically wrong. If a hypothesis predicts that we should observe certain evidence, and we look and do not find it, that observation is evidence against the hypothesis — exactly to the degree that the hypothesis predicted we would find it. If a drug works, we expect clinical trials to show positive results; if trials show nothing, that is evidence the drug does not work. The strength of the evidence depends on the likelihood ratio: how much more likely is the absence of evidence under "hypothesis false" versus "hypothesis true"? When the hypothesis strongly predicts observable consequences, failing to observe them is strong evidence against it.

## How It's Best Learned

Work through the Bayesian math explicitly: if P(observe evidence | H true) = 0.9 and P(observe evidence | H false) = 0.1, then not observing the evidence gives a likelihood ratio of 0.1/0.9 ≈ 0.11, a strong update against H. Practice identifying real-world cases where absence of expected evidence should update beliefs: the dog that did not bark, the study that found no effect, the prediction that did not come true.

## Common Misconceptions

- This does not mean any absence of evidence disproves a claim — the strength depends on how strongly the claim predicted observable consequences.
- The original saying has a grain of truth in informal contexts: sometimes we simply have not looked hard enough. But once we have looked and found nothing, that is informative.
