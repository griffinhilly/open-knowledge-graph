---
id: type-i-type-ii-errors-tradeoff
title: Type I and Type II Errors and Power
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: type-i-and-type-ii-errors
  type: hard
builds-toward:
- power-and-sample-size
tags:
- hypothesis-testing
- errors
- power
stage: formal-systems
status: validated
---

# Type I and Type II Errors and Power

## Core Idea
Type I error (α) is rejecting H₀ when it's true; Type II error (β) is failing to reject H₀ when H₁ is true. Power = 1 - β is the ability to detect a true effect. These errors trade off: decreasing α typically increases β. Sample size and effect size influence power.

## How It's Best Learned
Visualize error regions under both null and alternative distributions. Calculate power using software. Explore how sample size and effect size change the tradeoff between error types.

## Common Misconceptions
Confusing Type I and Type II errors. Thinking we can minimize both errors simultaneously without changing sample size. Assuming α and β are equally important in all contexts.

## Questions

```yaml
- question: "A researcher tightens their significance threshold from α = 0.05 to α = 0.01 without changing anything else about their study. What happens to Type I and Type II error rates?"
  type: multiple-choice
  options:
    - "Both Type I and Type II error rates decrease, since a stricter threshold improves the test overall"
    - "Type I error rate decreases, but Type II error rate increases (and power falls), since more of the alternative distribution now falls on the fail-to-reject side"
    - "Type II error rate decreases because the test is now more conservative"
    - "Neither error rate changes; only the p-value threshold changes"
  answer: 1
  explanation: "Moving the threshold right (stricter α) puts less of the null distribution in the rejection region — Type I error falls. But simultaneously, more of the alternative distribution falls outside the rejection region — β rises and power falls. Visualize two overlapping curves: the threshold line sits between them. Slide it right: less false-alarm area under the null curve, but more miss-area under the alternative curve. The two error rates are coupled through the shared threshold — you cannot reduce one without enlarging the other, holding all else fixed."

- question: "A medical screening test for a serious disease has α = 0.10 and β = 0.20. A statistician recommends lowering α to 0.01 to make the test more rigorous. A clinician objects. Why might the clinician be right?"
  type: multiple-choice
  options:
    - "Reducing α is always the wrong choice in medical contexts regardless of the disease"
    - "In screening contexts, missing a true case (Type II error) is often more harmful than a false positive; lowering α raises β, meaning more sick patients go undetected — the cost of the error being minimized may be lower than the cost of the error being inflated"
    - "Significance levels cannot be changed once a study has been designed"
    - "The clinician prefers a higher false positive rate because it increases treatment revenue"
  answer: 1
  explanation: "The choice between error types is a substantive judgment, not a statistical one. In screening for a serious disease, false negatives (missing a case) typically carry catastrophic consequences — the patient goes untreated. False positives (flagging a healthy patient) lead to follow-up tests, which is costly and stressful but usually recoverable. Lowering α from 0.10 to 0.01 reduces false alarms but increases missed cases (β rises). For this application, raising β is likely the worse tradeoff. The relative costs of the two errors depend on what happens downstream."

- question: "Increasing sample size is the primary way to simultaneously achieve lower Type I error and higher power, because it narrows both distributions and reduces their overlap."
  type: true-false
  answer: true
  explanation: "This is the key escape from the Type I/Type II tradeoff. With fixed distributions, moving the threshold always trades one error for the other. But a larger sample makes both the null and alternative distributions narrower (by the Central Limit Theorem, standard errors shrink). If the two distributions are narrow enough and far enough apart, the threshold can sit in a gap between them — delivering low α and high power simultaneously. Power analysis before a study asks exactly this question: how large must n be to achieve acceptable error rates on both sides?"

- question: "A researcher who raises their significance threshold from α = 0.05 to α = 0.10 will thereby increase their Type II error rate."
  type: true-false
  answer: false
  explanation: "Raising α (moving the rejection threshold left) expands the rejection region — more of the alternative distribution now falls on the rejection side. This means fewer misses: β decreases and power increases. The tradeoff runs in both directions: tightening α (moving threshold right) decreases Type I but increases Type II; loosening α (moving threshold left) decreases Type II but increases Type I. The student who memorizes 'strict α is good' without understanding the geometry will get this backwards."

- question: "Explain the mechanism by which reducing Type I error by tightening α increases Type II error, and describe what must change in a study design to escape this tradeoff."
  type: short-answer
  answer: "Tightening α moves the rejection threshold to a more extreme position, so fewer observations from the null distribution trigger rejection (Type I error falls). But the same threshold shift means more observations from the alternative distribution now fall on the non-rejection side — more true effects are missed (Type II error rises, power falls). The two error rates share one threshold: there is no position that minimizes both simultaneously. The escape is increasing sample size, which narrows both distributions (reducing standard errors), pushing them apart until the threshold can sit in the gap between them rather than in a region of overlap — achieving low α and high power simultaneously."
  explanation: "The geometric picture is essential: two bell curves partially overlapping, with a threshold line. Every threshold position produces a specific (Type I, Type II) pair. Moving the line trades one for the other. The only way to improve both simultaneously is to reduce the overlap itself — which means larger samples. This is why 'we need a bigger study' is a principled statistical claim, not just a hedge."
```

## Explainer

Picture two overlapping distributions: one showing what test statistics look like when H₀ is true, and another showing what they look like when some specific alternative H₁ is true. Your significance threshold α draws a vertical line. Everything to the right of that line gets labeled "reject H₀." **Type I error** (rate α) is the probability that a statistic from the null distribution falls to the right of the line anyway — a false alarm. **Type II error** (rate β) is the probability that a statistic from the alternative distribution falls to the left of the line — a miss. **Power** (1 − β) is the probability that a statistic from the alternative distribution correctly lands on the rejection side.

The tradeoff is immediate once you visualize it: if you move the threshold to the right to make false alarms rarer (lower α), more of the alternative distribution now falls on the "accept" side, so β increases and power falls. If you move the threshold left to catch more true effects (lower β, higher power), you also admit more of the null distribution into the rejection region, inflating α. You cannot simultaneously reduce both error types by adjusting the threshold — with fixed distributions, they move in opposite directions.

The escape from this tradeoff is **sample size**. A larger sample makes both distributions narrower and more separated, so the overlap between them shrinks. With enough data, you can achieve low α and high power simultaneously — the distributions are far apart enough that the threshold line sits in a gap between them rather than in a region of overlap. This is why power analysis before a study matters: it asks "how many observations do I need so that both error types are acceptably small?"

The relative costs of the two errors depend on context, and the right balance is a substantive judgment, not a statistical one. In medical screening, false negatives (missing a disease) may be catastrophic, so you accept a higher false positive rate to ensure near-perfect sensitivity. In criminal justice, the norm is "beyond reasonable doubt" — accepting many false negatives to keep false positives (wrongful convictions) very rare. **Effect size** also matters: a small true effect means the alternative distribution is only slightly shifted from the null, creating heavy overlap and requiring large samples to achieve adequate power. Understanding this geometry — two distributions, one threshold, and the four cells it creates — gives you a principled mental model for every inference decision you will encounter.


