---
id: power-and-sample-size
title: Statistical Power and Sample Size Determination
domain: health-and-human-development
course: biostatistics
prerequisites:
- id: hypothesis-testing-intro
  type: hard
- id: study-design-biostatistics
  type: hard
- id: normal-distribution
  type: soft
builds-toward:
- clinical-trial-design-intro
- adaptive-trial-designs
tags:
- power
- sample-size
- type-II-error
- effect-size
- alpha
stage: advanced
status: validated
---

# Statistical Power and Sample Size Determination

## Core Idea
Statistical power is the probability of correctly rejecting a false null hypothesis — equivalently, the probability of detecting a real effect when one exists. Power depends on four interconnected quantities: the significance level (alpha), the sample size (n), the effect size (the magnitude of the true difference), and the variability of the outcome. Sample size calculations performed before a study begins determine how many subjects are needed to achieve adequate power (conventionally 80% or higher) for a clinically meaningful effect size. An underpowered study wastes resources by being unable to detect effects that matter; an overpowered study wastes resources by enrolling more subjects than necessary and potentially detecting effects too small to be clinically relevant.

## Questions

```yaml
- question: "A clinical trial is designed with 80% power to detect a 5-point difference in blood pressure between drug and placebo groups. The trial enrolls the planned sample but finds a non-significant result (p = 0.12). A colleague says: 'The study was adequately powered, so this proves the drug doesn't work.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — 80% power guarantees detection of a 5-point difference if it exists"
    - "80% power means there is still a 20% chance of failing to detect a true 5-point difference; absence of significance does not prove absence of effect"
    - "The power calculation is irrelevant because the p-value alone determines the conclusion"
    - "The study must have been underpowered because it failed to reach significance"
  answer: 1
  explanation: "Power of 80% means that if the true effect is exactly 5 points, the study has a 20% probability of failing to detect it (Type II error). A non-significant result is consistent with both 'no effect' and 'real effect that the study missed.' This is why non-significance is never proof of no effect — it is an absence of evidence, not evidence of absence. To quantify the range of plausible effects, examine the confidence interval rather than relying solely on the p-value."

- question: "Holding alpha, effect size, and variability constant, doubling the sample size will double the statistical power of a study."
  type: true-false
  answer: false
  explanation: "Power does not scale linearly with sample size. Power depends on the square root of n (because standard errors decrease proportionally to 1/sqrt(n)), so doubling n increases the test statistic by a factor of sqrt(2) ≈ 1.41, not 2. If a study at n = 50 has 50% power, doubling to n = 100 might raise power to roughly 70%, not 100%. The relationship is nonlinear, and the marginal gain from additional subjects diminishes as power approaches 100%."

- question: "A researcher calculates that she needs 200 subjects per group to detect a 10-point difference with 80% power. She can only recruit 100 per group. Rather than reducing the study, she decides to increase alpha from 0.05 to 0.10 to compensate. Is this a valid strategy?"
  type: multiple-choice
  options:
    - "Yes — increasing alpha directly increases power, fully compensating for the smaller sample"
    - "Partially valid — it increases power but at the cost of doubling the Type I error rate, which must be explicitly justified"
    - "No — alpha has no effect on power; only sample size matters"
    - "No — changing alpha after the sample size calculation invalidates the entire study"
  answer: 1
  explanation: "Increasing alpha does increase power (a less stringent threshold is easier to cross), but the cost is a higher probability of a false positive. Moving from alpha = 0.05 to 0.10 doubles the false-positive rate. This tradeoff may be acceptable in exploratory or screening contexts where missing a true effect is more costly than a false alarm, but in confirmatory trials it is generally not acceptable. The decision to adjust alpha must be pre-specified and scientifically justified — it is not a free lunch."

- question: "Explain why effect size is the most important input to a sample size calculation and why researchers should base it on clinical significance rather than statistical convenience."
  type: short-answer
  answer: "Effect size determines the minimum difference the study is designed to detect. If chosen too large, the study will be small and cheap but will miss smaller real effects. If chosen too small, the study will require an enormous sample to detect trivially small differences that have no clinical importance. The effect size should reflect the smallest difference that would change clinical practice — a 1 mmHg blood pressure reduction might be statistically detectable with 50,000 subjects but is clinically meaningless. Basing effect size on clinical significance ensures the study answers a question worth asking."
  explanation: "Sample size is most sensitive to effect size because it enters the formula as a squared term (n is proportional to 1/d²). Halving the target effect size quadruples the required sample. This is why inflating the expected effect size to reduce enrollment is dangerous — if the true effect is smaller than assumed, the study will be underpowered. Conversely, choosing a clinically anchored effect size protects against both underpowering and overpowering."
```

## Explainer

From your study of hypothesis testing, you know that every test carries two types of error: Type I (rejecting a true null, controlled by alpha) and Type II (failing to reject a false null, denoted beta). Power is simply 1 minus beta — the probability that the test correctly rejects the null when the alternative is true. A study with 80% power and alpha = 0.05 will detect a true effect 80% of the time while maintaining a 5% false-positive rate. The 20% miss rate is the cost of doing science with finite samples.

The four determinants of power are tightly linked. **Alpha** sets the rejection threshold — a more lenient alpha increases power but increases false positives. **Sample size** reduces the standard error of the estimate, making it easier to distinguish signal from noise. **Effect size** is the magnitude of the true difference — larger effects are easier to detect. **Variability** (the standard deviation of the outcome) is noise — more variability obscures the signal and requires more subjects to detect it. A sample size calculation solves for n given fixed values of the other three quantities: "How many subjects do I need to detect this effect size at this alpha with this power, given the expected variability?"

The most consequential decision in a sample size calculation is the choice of **effect size**. This should reflect the minimum clinically important difference (MCID) — the smallest effect that would change clinical practice or patient outcomes. A blood pressure drug that lowers systolic pressure by 0.5 mmHg might be statistically significant with 100,000 subjects, but no clinician would change prescribing behavior for such a trivial effect. Conversely, a study powered to detect only a 20 mmHg difference will miss a real 10 mmHg effect that genuinely matters. The effect size should come from clinical judgment, prior literature, or pilot data — never from statistical convenience.

Sample size calculations must be performed and reported **before** data collection begins. Post-hoc power calculations — computing the power of a completed study using the observed effect size — are widely recognized as uninformative and circular. If the study found a non-significant result, the observed effect will always yield low post-hoc power, telling you nothing you did not already know. The proper way to interpret a non-significant result is through the confidence interval: a wide interval that includes both clinically important and null effects indicates the study was uninformative, while a narrow interval tightly centered on zero provides genuine evidence of no meaningful effect.
