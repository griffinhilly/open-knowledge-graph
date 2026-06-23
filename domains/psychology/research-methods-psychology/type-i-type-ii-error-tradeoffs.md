---
id: type-i-type-ii-error-tradeoffs
title: Type I and Type II Error Trade-offs in Decision Making
domain: psychology
course: research-methods-psychology
prerequisites:
- id: inferential-statistics-psychology
  type: hard
- id: effect-size-reporting-interpretation
  type: soft
builds-toward:
- multiple-comparisons-and-corrections
tags:
- statistics
- errors
- decision
stage: formal-systems
status: validated
---

# Type I and Type II Error Trade-offs in Decision Making

## Core Idea
Type I errors (false positives) reject a true null hypothesis; Type II errors (false negatives) fail to reject a false null hypothesis. These errors are inversely related: lowering the threshold for Type I error increases Type II error risk. Research design choices (sample size, effect size magnitude, alpha level) involve explicit trade-offs between false positive and false negative risks guided by research context.

## Questions

```yaml
- question: "Designers of a cancer screening test want to minimize the risk of telling a sick patient they are healthy. To achieve this, they lower the detection threshold — making it easier to flag a positive result. What is the trade-off?"
  type: multiple-choice
  options:
    - "Fewer false negatives, but no change in false positives since the threshold only affects one direction"
    - "Fewer false negatives (Type II errors), but more false positives (Type I errors) — more healthy people will be incorrectly flagged"
    - "Fewer false positives and fewer false negatives simultaneously — a lower threshold always improves both"
    - "Higher statistical power with no increase in Type I error rate"
  answer: 1
  explanation: "Lowering the detection threshold (effectively raising α) reduces the chance of missing a real case (Type II error / false negative) but simultaneously increases the chance of flagging a healthy person as potentially sick (Type I error / false positive). The two error types are inversely related through the threshold: moving the threshold in either direction reduces one error while increasing the other. The only way to reduce both simultaneously is to increase sample size or test accuracy, not to adjust the threshold."

- question: "A psychology study with 25 participants finds p = .11 and concludes 'no effect was found.' A replication with 250 participants on the same question finds p = .02. What is the most likely explanation?"
  type: multiple-choice
  options:
    - "The smaller study used a flawed measure that the larger study corrected"
    - "The larger study is probably a false positive — more participants increases the Type I error rate"
    - "The smaller study was underpowered — too few participants to reliably detect a real effect — making its null result likely a Type II error"
    - "Effect sizes are always smaller in small samples and larger in large samples, making the comparison invalid"
  answer: 2
  explanation: "Underpowered studies miss real effects not because the effect isn't there, but because small samples produce high variance, making it hard to distinguish a real signal from noise. A null result from a study with 25 participants and a small-to-medium effect size tells you almost nothing — the probability of detecting the effect even if it existed (the power) may have been only 20-30%. The replication with 250 participants had enough power to detect the effect. This is why 'absence of evidence is not evidence of absence' in underpowered studies."

- question: "A null result (p > .05) from an adequately powered study — one designed with enough participants to detect a plausible effect — provides meaningful evidence that the true effect is small or absent."
  type: true-false
  answer: true
  explanation: "When a study is adequately powered, it could have detected a real effect if one existed. In that case, failing to find significance is genuinely informative: it suggests the effect is either absent or smaller than the minimum detectable size. This is 'evidence of absence' — a meaningful finding, not a non-result. The problem arises only with underpowered studies, where a null result is nearly uninterpretable because the study couldn't have detected the effect anyway."

- question: "The conventional α = .05 threshold optimally balances Type I and Type II error risks for most research contexts."
  type: true-false
  answer: false
  explanation: "α = .05 is a historical convention, not a principled optimum. The correct α depends on the relative costs of the two error types in the specific research context. A cancer screening test may warrant α = .10 or higher to minimize missed cases. A study justifying a costly new policy may warrant α = .01 to minimize false positives. A preliminary exploratory study may tolerate α = .10. The costs of false positives and false negatives vary enormously by domain, and α should reflect those costs — not default to a universal convention."

- question: "Why is 'absence of evidence is not evidence of absence' particularly important when interpreting a null result from a small study?"
  type: short-answer
  answer: "A small study typically has low statistical power — it has a low probability of detecting a real effect even if one exists. When such a study fails to find significance, the null result is ambiguous: it could mean the effect is absent, or it could mean the study simply couldn't see it. Because the false-negative rate (β) is high in underpowered studies, a null result carries little information about whether the effect is real. By contrast, a null result from a large, well-powered study is informative because the study had a high probability of detecting an effect if one existed."
  explanation: "The practical implication is that before interpreting any null result, you should ask: what was the power of this test? A p > .05 in a study with 80% power means something; a p > .05 in a study with 25% power tells you almost nothing. This skill — reading power alongside p-values — is one of the most important habits in evaluating psychological research."
```

## Explainer

From inferential statistics, you know that hypothesis testing produces a binary decision — reject or fail to reject the null — and that this decision is made by comparing a test statistic to a threshold set by α. The threshold is a choice, and like all choices, it has consequences in both directions. Setting α = .05 means you accept a 5% chance of rejecting a true null hypothesis. But that choice has a less visible flip side: it also determines how often you *miss* real effects.

A **Type I error** (false positive) occurs when you conclude an effect exists when it does not. The null hypothesis is actually true — there is no difference, no relationship — but your sample's data, through random variation, produced a test statistic that crossed the threshold. Your Type I error rate is directly controlled by α: it is exactly the probability you set. A **Type II error** (false negative) occurs when a real effect exists but you fail to detect it. The null is false, but your data didn't reach the threshold. The Type II error rate is β, and statistical **power** (1 − β) is the probability of detecting a real effect when one exists. The two errors are inversely related through the threshold: a stricter α (say, .01) means fewer false positives, but the narrower rejection region also misses more real effects, increasing β.

The tradeoff is not abstract — it has stakes that vary by context. Consider a screening test for a rare but serious disease. A **Type I error** means a healthy person is told they might be sick — unnecessary anxiety, follow-up tests, possible invasive procedures. A **Type II error** means a sick person is cleared — they don't receive treatment they need, and the disease progresses. Which error is worse? In this context, most people would rather risk false positives than miss real cases, so the threshold should be set to favor sensitivity (low α for the null that the person is healthy). Now flip to a drug trial: a **Type I error** means approving an ineffective drug, which patients take instead of effective treatments. A **Type II error** means rejecting an effective drug, denying benefit to patients. The relative costs shift again. There is no universally correct α — it is a value judgment about the relative costs of the two error types.

The key lever that reduces *both* errors simultaneously is **sample size**. Larger samples reduce random sampling error, making the test more sensitive to real effects (higher power) without changing α. This is why power analysis is a design requirement, not optional. If a study is underpowered — too small to detect a reasonable effect — a null result is nearly uninformative: you couldn't have detected the effect even if it was there. The critical distinction is between **absence of evidence** and **evidence of absence**. A p > .05 in a well-powered study is informative; a p > .05 in a study with 30 participants detecting a small effect tells you almost nothing. Learning to ask "what was the power of this test?" before interpreting a null result is one of the most important skills in reading psychological research.
