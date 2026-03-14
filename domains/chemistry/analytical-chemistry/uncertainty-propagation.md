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
