---
id: uncertainty-propagation
title: Uncertainty Propagation
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: statistical-methods-analytical
  type: hard
- id: accuracy-precision-error
  type: soft
- id: partial-derivatives
  type: soft
tags:
- error propagation
- uncertainty
- absolute uncertainty
- relative uncertainty
- GUM
- combined uncertainty
stage: formal-systems
status: validated
---

# Uncertainty Propagation

## Core Idea
When a final result is calculated from multiple measured quantities — each carrying its own uncertainty — the uncertainties combine according to mathematical rules that depend on how the quantities enter the calculation. For addition and subtraction, absolute uncertainties add in quadrature; for multiplication and division, relative uncertainties add in quadrature. The Guide to the Expression of Uncertainty in Measurement (GUM) provides a systematic framework for identifying all uncertainty sources, quantifying each contribution, and combining them into a single expanded uncertainty with a stated confidence level. Reporting a result without its uncertainty is incomplete because the number alone does not communicate whether it is reliable to one part per thousand or one part per ten.

## How It's Best Learned
Take a concrete gravimetric or volumetric calculation — such as determining the mass percent of an analyte from multiple weighings and a dilution — and propagate the uncertainty from each balance reading and volumetric transfer through to the final answer. Compare the dominant uncertainty source to see which step limits overall precision.

## Common Misconceptions
- Uncertainties do not simply add; they add in quadrature (root-sum-of-squares), which means one large uncertainty source tends to dominate the total even when several small ones are present.
- The GUM framework applies to all measurement disciplines, not just chemistry — its principles are universal, and regulatory agencies increasingly require GUM-style uncertainty budgets.

## Questions

```yaml
- question: "A chemist weighs a crucible (±0.0002 g), adds a sample, then weighs again (±0.0002 g), and subtracts to find the sample mass. What is the uncertainty of the mass difference?"
  type: multiple-choice
  options:
    - "±0.0004 g — absolute uncertainties simply add"
    - "±0.0002 g — only one weighing contributes to the difference"
    - "±0.00028 g — absolute uncertainties add in quadrature"
    - "±0.0001 g — the average of the two uncertainties"
  answer: 2
  explanation: "For subtraction, absolute uncertainties add in quadrature: √(0.0002² + 0.0002²) = √(0.00000004 + 0.00000004) = √0.00000008 ≈ 0.00028 g. The common mistake (option A) is to add uncertainties directly; this overestimates the combined uncertainty because the errors are statistically independent and partially cancel on average. The quadrature rule is not a convention — it follows from the mathematical behavior of independent random variables."

- question: "A final concentration C is computed as C = n/V, where n has a relative uncertainty of 1.0% and V has a relative uncertainty of 0.1%. What is the approximate combined relative uncertainty of C?"
  type: multiple-choice
  options:
    - "±1.1% — relative uncertainties add directly for multiplication and division"
    - "±0.9% — subtract the smaller uncertainty from the larger"
    - "±0.1% — only the smaller source matters since it is more precise"
    - "±1.005% — relative uncertainties add in quadrature, and the larger source dominates"
  answer: 3
  explanation: "For multiplication and division, relative uncertainties add in quadrature: √(1.0² + 0.1²) = √(1.0 + 0.01) ≈ √1.01 ≈ 1.005%. The 0.1% contribution barely changes the total because quadrature addition is dominated by the largest term. This is the key practical insight: when one uncertainty source is much larger than others, improving the smaller sources is essentially wasted effort. Option A (direct addition) overestimates; option C underestimates by ignoring the dominant source."

- question: "When a ±1% uncertainty source is combined with a ±0.1% source, the combined uncertainty is approximately ±1.1%, since both contributions are meaningful."
  type: true-false
  answer: false
  explanation: "Quadrature addition gives √(1.0² + 0.1²) ≈ 1.005%, not 1.1%. The ±0.1% contribution adds only 0.5% to the total, not 10%. This is the practical message of quadrature rules: smaller sources of uncertainty become negligible once a larger source dominates. Improving the 0.1% step would have virtually no effect on the combined uncertainty. The effort should go to reducing the 1.0% source first."

- question: "An uncertainty budget that identifies one measurement step as the dominant contributor reveals where effort to improve the method will be most effective."
  type: true-false
  answer: true
  explanation: "This is precisely the diagnostic value of the uncertainty budget. Because uncertainties combine in quadrature, the largest source dominates the total — and reducing smaller sources while the dominant source remains unchanged barely improves the overall uncertainty. If the volumetric step contributes ±0.5% and the weighing step contributes ±0.01%, investing in a more precise balance is wasted until the volumetric step is addressed. The budget turns uncertainty propagation from a reporting requirement into a rational guide for method improvement."

- question: "Why do uncertainties combine in quadrature (root-sum-of-squares) rather than adding directly? What practical consequence does this have for identifying the limiting step in an analysis?"
  type: short-answer
  answer: "Quadrature addition follows from the statistical independence of measurement errors — if errors in two measurements are uncorrelated, the variance of their sum or difference is the sum of their variances, and standard deviation (uncertainty) is the square root of variance. Because each term is squared before adding, the largest uncertainty dominates the total; smaller uncertainties contribute negligibly once a larger source is present. The practical consequence is that the dominant uncertainty source determines overall quality, so improvement efforts should focus there — improving other steps has diminishing returns."
  explanation: "This is why the uncertainty budget is a tool for rational resource allocation, not just bookkeeping. A chemist who improves balance precision from ±0.0002 g to ±0.00001 g while still using a ±0.5% volumetric flask will see essentially no improvement in the final uncertainty — the flask dominates. Only by identifying and attacking the largest contributor can overall precision be meaningfully improved."
```

## Explainer

Every measurement you have ever made carries uncertainty. From your work with accuracy, precision, and error, you know the difference between systematic bias and random scatter, and from statistics you know how to quantify that scatter using standard deviations and confidence intervals. **Uncertainty propagation** answers the next question: when you combine several uncertain measurements in a calculation, how uncertain is the final answer?

The core insight is that uncertainties do not simply add up — they combine in **quadrature**, meaning you square each contribution, sum the squares, and take the square root. This is not an arbitrary convention; it follows from the statistical independence of the individual measurement errors. If you weigh a crucible (±0.0002 g), add a sample, and weigh again (±0.0002 g), the uncertainty in the mass difference is not 0.0004 g but √(0.0002² + 0.0002²) = 0.00028 g. The quadrature rule means that unless two uncertainties are nearly equal, the larger one dominates. A ±1% uncertainty combined with a ±0.1% uncertainty gives about ±1.005% — the small one barely matters.

The rules split into two cases based on how quantities enter the calculation. For **addition and subtraction**, you propagate absolute uncertainties in quadrature. For **multiplication and division**, you propagate relative (percentage) uncertainties in quadrature. If your formula mixes both operations, you work through the calculation step by step, propagating at each stage. For more complex functions — logarithms, exponentials, powers — you use partial derivatives from calculus: the uncertainty contribution from each variable equals the partial derivative with respect to that variable, multiplied by that variable's uncertainty, and then all contributions add in quadrature. This is the general formula at the heart of the GUM framework.

The practical payoff is the **uncertainty budget** — a table listing every source of uncertainty, its magnitude, and its contribution to the total. Building this table forces you to identify which step in your procedure limits overall quality. If the balance contributes ±0.01% and the volumetric flask contributes ±0.5%, improving the balance is pointless — your effort belongs on the volumetric step. This diagnostic power makes uncertainty propagation not just a reporting requirement but a genuine tool for improving analytical methods. Regulatory bodies increasingly expect GUM-style uncertainty statements alongside results, because a number without its uncertainty is, in a real sense, incomplete — it tells you the answer but not whether you should trust it.
