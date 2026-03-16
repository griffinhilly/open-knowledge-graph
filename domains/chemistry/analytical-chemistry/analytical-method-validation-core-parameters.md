---
id: analytical-method-validation-core-parameters
title: 'Analytical Method Validation: Core Performance Parameters'
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: method-validation
  type: hard
- id: analytical-method-development-workflow
  type: hard
- id: statistical-methods-analytical
  type: soft
builds-toward:
- analytical-selectivity-and-specificity
tags:
- validation
- parameters
- accuracy
- precision
- regulatory
stage: advanced
status: draft
---

# Analytical Method Validation: Core Performance Parameters

## Core Idea
Method validation systematically demonstrates that an analytical method is suitable for its intended use. This requires characterizing specificity, accuracy (bias and recovery), precision (repeatability and reproducibility), linearity, range, and robustness in accordance with ICH Q2(R2) and USP/EP guidelines.

## How It's Best Learned
Design and execute a complete validation study for a real analytical method, measuring each parameter and documenting results according to ICH guidelines.

## Common Misconceptions
Thinking validation is a one-time checklist rather than an ongoing process. Assuming equipment performance data is sufficient without method-specific validation.

## Explainer

From your work on method development, you know how to build an analytical method that separates and detects an analyte. Validation is the structured process of proving — with documented evidence — that the method actually does what you claim it does, reliably and reproducibly. Think of it as the difference between a prototype that works on your bench and a product that works in any qualified laboratory. The ICH Q2(R2) guideline and pharmacopeial chapters (USP <1225>, EP 2.2) define the specific **performance parameters** you must characterize, and each one answers a distinct question about method fitness.

**Specificity** asks whether the method measures only the analyte of interest in the presence of other components — degradation products, excipients, matrix interferences. **Accuracy** (sometimes called trueness) quantifies systematic error: how close your measured value is to the true or accepted value, typically expressed as percent recovery from spiked samples or comparison to a reference method. **Precision** characterizes random error at three levels: **repeatability** (same analyst, same instrument, same day), **intermediate precision** (different analysts, different days, same laboratory), and **reproducibility** (different laboratories entirely). These levels map directly onto the statistical concepts of within-run and between-run variance you encountered in your statistics prerequisite.

**Linearity** demonstrates that the detector response is proportional to analyte concentration across a defined range, typically assessed by regression analysis with acceptance criteria for the correlation coefficient and residual pattern. The validated **range** is the interval between the lowest and highest concentrations for which the method has acceptable accuracy, precision, and linearity — it is not simply the calibration range but the proven operating space. **Robustness** testing deliberately introduces small, realistic perturbations to method parameters (mobile phase pH ± 0.2 units, column temperature ± 2°C, flow rate ± 5%) and checks whether results remain within specification. A robust method tolerates normal lab-to-lab variation; a fragile one produces out-of-spec results from trivial changes.

The critical insight is that these parameters are not independent checkboxes — they form an interconnected picture of method capability. A method can be precise but inaccurate (consistently wrong), accurate on average but imprecise (scattered around the true value), or linear over a range too narrow for your samples. Validation forces you to characterize all of these dimensions simultaneously and document the evidence so that any qualified analyst can reproduce your results. When a method is later transferred to another laboratory or a regulatory inspector audits your data, the validation report is the foundation of confidence in every result the method has produced.
