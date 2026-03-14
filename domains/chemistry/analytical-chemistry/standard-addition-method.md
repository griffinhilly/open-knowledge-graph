---
id: standard-addition-method
title: Standard Addition Method
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: calibration-curve-methods
  type: hard
- id: matrix-effects
  type: soft
tags:
- standard addition
- matrix effects
- graphical extrapolation
- calibration
- matrix-matched
- method of additions
stage: formal-systems
status: draft
---

# Standard Addition Method

## Core Idea
The standard addition method quantifies an analyte by spiking known amounts of the analyte directly into aliquots of the sample, measuring the signal at each spike level, and extrapolating the resulting line back to the x-intercept to determine the original concentration. Because all measurements are made in the actual sample matrix, the calibration slope inherently reflects any matrix-induced signal enhancement or suppression, eliminating the bias that external calibration with matrix-free standards would introduce. The method assumes a linear relationship between signal and concentration over the range of additions, and it requires a minimum of three to four addition levels (plus the unspiked sample) to establish the line reliably. Standard addition is more labor-intensive than external calibration but is the preferred approach whenever matrix effects are significant and matrix-matched standards are unavailable.

## How It's Best Learned
Determine a metal ion (e.g., Pb or Cu) in a real water or soil extract by both external calibration and standard addition using AAS or ICP-OES. Compare the two results — any discrepancy directly quantifies the matrix effect, making the motivation for standard addition unmistakably clear.

## Common Misconceptions
- Standard addition does not work if the signal-concentration relationship is nonlinear over the range of additions; the method fundamentally requires linearity, so the spike levels must be chosen to stay within the linear dynamic range.
- The method compensates for multiplicative matrix effects (those that change the slope) but not for additive interferences (a constant background signal); additive interferences must still be identified and corrected separately, such as by blank subtraction.
