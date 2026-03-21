---
id: margin-of-error-and-sample-size
title: Margin of Error and Sample Size
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: confidence-intervals-framework
  type: hard
builds-toward:
- confidence-intervals-means
- confidence-intervals-proportions
tags:
- inference
- planning
- sample-size
stage: formal-systems
status: draft
---

# Margin of Error and Sample Size

## Core Idea
The margin of error is the half-width of a confidence interval: ME = (critical value) × (standard error). It quantifies precision. To achieve desired margin of error m: n = (z/m)² · σ² or n = z² · p(1-p)/m² for proportions.

## How It's Best Learned
Calculate required sample sizes for various scenarios. Verify that doubling sample size reduces margin of error by √2. Understand the tradeoff between sample size and precision in practice.

## Questions

```yaml
- question: "A pollster runs a survey and gets a margin of error of ±6 percentage points. She wants to cut the margin of error to ±3 percentage points. By what factor must she increase the sample size?"
  type: multiple-choice
  options:
    - "2 — she needs twice as many respondents"
    - "3 — she needs three times as many respondents"
    - "4 — she needs four times as many respondents"
    - "6 — she needs six times as many respondents"
  answer: 2
  explanation: "The margin of error scales as 1/√n. To cut ME in half (from ±6 to ±3), you need to multiply 1/√n by 1/2, which means increasing n by a factor of 4. In general, halving the margin of error requires quadrupling the sample size. This counterintuitive result — the 'square root penalty' — is one of the most practically important facts in survey design. Option A (doubling) is the common misconception."

- question: "A researcher is designing a survey to estimate the proportion of voters who support a candidate. She has no prior data on what the proportion might be. What value of p should she use in the sample size formula, and why?"
  type: multiple-choice
  options:
    - "p = 0.5, because it maximizes p(1−p) and gives the largest, most conservative required sample size"
    - "p = 0.5, because polls always assume 50-50 races for fairness"
    - "p = 0.1, because underestimating support is safer than overestimating it"
    - "She should use any p between 0 and 1 — the sample size formula is insensitive to the choice of p"
  answer: 0
  explanation: "The sample size formula for proportions is n = z²p(1−p)/m². The factor p(1−p) is maximized when p = 0.5, giving p(1−p) = 0.25. Using p = 0.5 therefore produces the largest n — the most conservative estimate — guaranteeing sufficient precision regardless of the true proportion. Option B gives the right answer but the wrong reason; it has nothing to do with fairness and everything to do with worst-case coverage."

- question: "Doubling the sample size reduces the margin of error by a factor of √2 (approximately 1.41)."
  type: true-false
  answer: true
  explanation: "Since ME = z*(σ/√n), doubling n replaces √n with √(2n) = √2 · √n. The margin of error becomes ME/√2 — a reduction by the factor √2 ≈ 1.41. For example, a study with n=100 and ME=±5% that doubles to n=200 would have ME ≈ ±5%/√2 ≈ ±3.5%. This is the precise quantitative expression of the 1/√n relationship."

- question: "Doubling the sample size will cut the margin of error in half."
  type: true-false
  answer: false
  explanation: "This is the most common misconception about sample size planning. Because ME ∝ 1/√n, doubling n reduces ME by only 1/√2 ≈ 29%, not by 50%. To cut the margin of error in half, you need to multiply n by 4. The confusion likely comes from thinking the relationship is linear (double the input, double the output), when it is actually a square-root relationship."

- question: "Why does reducing margin of error from ±4% to ±2% require four times the sample size rather than twice the sample size?"
  type: short-answer
  answer: "The margin of error is proportional to 1/√n. Halving ME means setting 1/√(n_new) = (1/2) × 1/√(n_old), which gives √(n_new) = 2√(n_old), so n_new = 4 × n_old. The square-root relationship means sample size must grow as the square of the desired precision improvement. Doubling n only improves precision by √2, not by 2."
  explanation: "This derivation is worth tracing explicitly. Start from ME = z*(σ/√n). If you want ME_new = ME_old/2, you need σ/√n_new = (1/2)(σ/√n_old), so √n_new = 2√n_old, meaning n_new = 4n_old. The practical upshot is that high precision is disproportionately expensive: going from ±4% to ±2% to ±1% requires sample sizes in the ratio 1:4:16."
```

## Explainer

The **margin of error** (ME) is the ± part you see in poll results — the half-width of a confidence interval. If a survey reports "52% support, margin of error ±3 points," the confidence interval runs from 49% to 55%. From your study of confidence intervals, you know an interval is built as (point estimate) ± (critical value × standard error). The margin of error is precisely that second part: ME = z* × SE. Everything else in this topic follows from understanding what controls that quantity.

Two levers control ME: the critical value z* (set by your chosen confidence level) and the standard error SE (set by population variability and sample size). Raising confidence from 95% to 99% increases z* from 1.96 to 2.576, which widens ME. To shrink ME, you can reduce σ (rarely under your control) or increase n. Since SE = σ/√n, the ME scales as 1/√n. This is the key relationship: to cut the margin of error in half, you need four times as many observations, not twice as many.

For means, solving ME = z*(σ/√n) for n gives the sample size planning formula: n = (z*σ/m)², where m is your target margin of error. For proportions, use SE = √(p(1-p)/n) and the corresponding formula n = z²p(1-p)/m². When the true proportion p is unknown, plug in p = 0.5, which maximizes p(1-p) = 0.25 and gives the most conservative (largest) required sample size — guaranteeing you achieve your target precision regardless of the actual proportion. This worst-case approach is standard in survey design.

The √n relationship has a stark practical consequence: precision is expensive. Halving the margin of error requires 4× the sample; reducing it to one-fifth requires 25×. In practice, researchers specify an acceptable margin of error first, then compute the required sample size and budget accordingly. The formula is the planning tool; the √n rule is the intuition behind why high-precision studies cost so much more than moderate-precision ones.
