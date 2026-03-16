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
status: draft
---

# Uncertainty Propagation

## Core Idea
When a final result is calculated from multiple measured quantities — each carrying its own uncertainty — the uncertainties combine according to mathematical rules that depend on how the quantities enter the calculation. For addition and subtraction, absolute uncertainties add in quadrature; for multiplication and division, relative uncertainties add in quadrature. The Guide to the Expression of Uncertainty in Measurement (GUM) provides a systematic framework for identifying all uncertainty sources, quantifying each contribution, and combining them into a single expanded uncertainty with a stated confidence level. Reporting a result without its uncertainty is incomplete because the number alone does not communicate whether it is reliable to one part per thousand or one part per ten.

## How It's Best Learned
Take a concrete gravimetric or volumetric calculation — such as determining the mass percent of an analyte from multiple weighings and a dilution — and propagate the uncertainty from each balance reading and volumetric transfer through to the final answer. Compare the dominant uncertainty source to see which step limits overall precision.

## Common Misconceptions
- Uncertainties do not simply add; they add in quadrature (root-sum-of-squares), which means one large uncertainty source tends to dominate the total even when several small ones are present.
- The GUM framework applies to all measurement disciplines, not just chemistry — its principles are universal, and regulatory agencies increasingly require GUM-style uncertainty budgets.

## Explainer

Every measurement you have ever made carries uncertainty. From your work with accuracy, precision, and error, you know the difference between systematic bias and random scatter, and from statistics you know how to quantify that scatter using standard deviations and confidence intervals. **Uncertainty propagation** answers the next question: when you combine several uncertain measurements in a calculation, how uncertain is the final answer?

The core insight is that uncertainties do not simply add up — they combine in **quadrature**, meaning you square each contribution, sum the squares, and take the square root. This is not an arbitrary convention; it follows from the statistical independence of the individual measurement errors. If you weigh a crucible (±0.0002 g), add a sample, and weigh again (±0.0002 g), the uncertainty in the mass difference is not 0.0004 g but √(0.0002² + 0.0002²) = 0.00028 g. The quadrature rule means that unless two uncertainties are nearly equal, the larger one dominates. A ±1% uncertainty combined with a ±0.1% uncertainty gives about ±1.005% — the small one barely matters.

The rules split into two cases based on how quantities enter the calculation. For **addition and subtraction**, you propagate absolute uncertainties in quadrature. For **multiplication and division**, you propagate relative (percentage) uncertainties in quadrature. If your formula mixes both operations, you work through the calculation step by step, propagating at each stage. For more complex functions — logarithms, exponentials, powers — you use partial derivatives from calculus: the uncertainty contribution from each variable equals the partial derivative with respect to that variable, multiplied by that variable's uncertainty, and then all contributions add in quadrature. This is the general formula at the heart of the GUM framework.

The practical payoff is the **uncertainty budget** — a table listing every source of uncertainty, its magnitude, and its contribution to the total. Building this table forces you to identify which step in your procedure limits overall quality. If the balance contributes ±0.01% and the volumetric flask contributes ±0.5%, improving the balance is pointless — your effort belongs on the volumetric step. This diagnostic power makes uncertainty propagation not just a reporting requirement but a genuine tool for improving analytical methods. Regulatory bodies increasingly expect GUM-style uncertainty statements alongside results, because a number without its uncertainty is, in a real sense, incomplete — it tells you the answer but not whether you should trust it.
