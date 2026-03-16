---
id: method-validation-and-acceptance-criteria
title: Method Validation and Acceptance Criteria
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: method-validation
  type: hard
- id: limit-of-detection-loq
  type: hard
tags:
- validation
- acceptance criteria
- performance parameters
stage: advanced
status: draft
---

# Method Validation and Acceptance Criteria

## Core Idea
Method validation ensures analytical methods reliably produce accurate, precise results within defined scope. Validation protocols evaluate selectivity, linearity, accuracy, precision, range, and robustness, with acceptance based on regulatory or organizational requirements.

## How It's Best Learned
Review ICH Q2 guidelines and compare validation approaches across different analytical techniques and regulatory contexts.

## Explainer

From your earlier study of method validation fundamentals and detection limits, you understand that an analytical method must be tested to prove it works before it can be trusted for routine use. Method validation and acceptance criteria take this concept to its rigorous conclusion: they define exactly *what* must be tested, *how* the testing must be performed, and *what numbers* constitute a pass or fail. Without predefined acceptance criteria, validation becomes subjective — a scientist could unconsciously cherry-pick favorable results or declare a method "good enough" without evidence. The acceptance criteria transform validation from an opinion into a decision rule.

The core **validation parameters** are selectivity, linearity, accuracy, precision, range, detection and quantitation limits, and robustness. You have encountered most of these individually, but validation requires evaluating all of them systematically within a single study. **Selectivity** demonstrates that the method measures only the target analyte and not interferences. **Linearity** establishes the range of concentrations over which detector response is proportional to analyte concentration, typically requiring a correlation coefficient (r²) of 0.999 or better. **Accuracy** — how close the measured value is to the true value — is assessed through spike-and-recovery experiments or comparison with a reference method. **Precision** — how reproducible the results are — is evaluated at three levels: repeatability (same analyst, same day), intermediate precision (different analysts, different days), and reproducibility (different laboratories).

**Acceptance criteria** are the numerical thresholds that each parameter must meet. These are not arbitrary — they come from regulatory guidelines (ICH Q2 for pharmaceuticals, EPA methods for environmental, ISO 17025 for testing labs) or from the intended use of the data. For example, a pharmaceutical assay method might require accuracy within 98–102% of label claim, precision with RSD ≤ 2%, and linearity with r² ≥ 0.999 over 80–120% of the target concentration. An environmental screening method for trace pollutants might accept wider accuracy limits (70–130% recovery) because the concentrations are much lower and the matrix more variable. The criteria must be established *before* validation begins — setting them after seeing the data is scientific misconduct.

**Robustness** testing deserves special attention because it reveals how fragile the method is in practice. Small, deliberate variations are introduced — changing the mobile phase pH by ±0.2 units, adjusting column temperature by ±5°C, using columns from different manufacturing lots — and the effect on results is measured. A robust method tolerates these variations without failing acceptance criteria; a fragile method requires such precise control of conditions that routine use in different laboratories becomes impractical. Robustness testing is essentially a stress test that predicts whether the method will survive the inevitable small variations of real-world analytical practice. Together, the full validation package provides documented, quantitative evidence that the method is fit for its intended purpose — not a matter of trust, but a matter of proof.
