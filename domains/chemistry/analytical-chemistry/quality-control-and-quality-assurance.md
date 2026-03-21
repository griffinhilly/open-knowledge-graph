---
id: quality-control-and-quality-assurance
title: Quality Control and Quality Assurance in Analytical Labs
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: quality-assurance-analytical
  type: hard
- id: statistical-methods-analytical
  type: hard
tags:
- QA
- QC
- lab management
stage: advanced
status: draft
---

# Quality Control and Quality Assurance in Analytical Labs

## Core Idea
Quality assurance and quality control programs ensure analytical laboratories deliver reliable, defensible results through method validation, analyst training, equipment maintenance, and statistical monitoring. Control charts and proficiency testing verify ongoing performance and identify drift.

## Questions

```yaml
- question: "A laboratory analyzes a control sample alongside every batch. The last eight consecutive control results have all fallen on the same side of the mean — but none have exceeded the ±2 standard deviation warning limit. According to Westgard rules, what should the analyst do?"
  type: multiple-choice
  options:
    - "Accept the batch — all results are within warning limits so the system is in statistical control"
    - "Reject the batch immediately — seven or more consecutive results on one side signals systematic drift requiring investigation"
    - "Re-analyze only the control sample to confirm the pattern is real"
    - "Document the pattern and continue until a result exceeds the action limit"
  answer: 1
  explanation: "Westgard rules include pattern-based triggers, not just threshold-based ones. A run of seven or more consecutive results on one side of the mean — even within ±2σ — indicates systematic drift (a shift in the method's baseline) rather than random variation. The probability of this occurring by chance is less than 1%, so it signals a real problem such as reagent degradation or instrument drift. Accepting the batch because 'no result exceeded the warning limit' misses this. This is the classic mistake of checking only individual rules while ignoring run patterns."

- question: "A laboratory processes a real groundwater sample spiked with a known concentration of lead alongside unspiked samples. Recovery is 78%. What is the most accurate interpretation?"
  type: multiple-choice
  options:
    - "The method has a contamination problem — the spike is contributing excess signal"
    - "There is a systematic bias or matrix effect: the sample matrix is suppressing recovery relative to the calibration standard"
    - "The instrument is out of calibration and must be recalibrated before results can be reported"
    - "The spike result is within acceptable limits and indicates the blank is clean"
  answer: 1
  explanation: "Spiked sample recovery tests for matrix effects and systematic bias: does the analyte behave the same in a real sample matrix as in a calibration standard made in clean solvent? Recovery of 78% suggests matrix suppression — the sample matrix interferes with detection or extraction of the analyte, causing it to read low. This is distinct from contamination (which would inflate the result) or calibration error (which would affect all samples equally). Matrix-matched standards or standard addition can correct for this. Method blanks — not spikes — detect contamination."

- question: "A single control result that falls within ±2 standard deviations of the established mean proves the batch is in statistical control and all results are acceptable."
  type: true-false
  answer: false
  explanation: "False. A single within-limit result is necessary but not sufficient. Statistical control also requires the absence of non-random patterns: systematic trends, runs of consecutive results on one side of the mean, or gradual drift can all indicate a system drifting out of control even when no individual result has crossed a threshold. Westgard rules codify these pattern-based triggers specifically because single-result checks miss systematic problems that develop over successive batches."

- question: "Certified reference materials (CRMs) serve a different QC function than spiked samples: CRMs provide an independent accuracy check for the method as a whole, while spikes primarily test for matrix effects within a specific sample."
  type: true-false
  answer: true
  explanation: "True. CRMs have compositions established by authoritative bodies using multiple independent methods — they represent the gold standard for accuracy verification. If your method gives the right answer on a CRM, your entire analytical chain (reagents, calibration, instrument, procedure) is working. Spikes test whether a known amount of analyte added to a specific real sample is recovered correctly, which targets matrix effects and extraction efficiency but does not verify absolute accuracy in the same way. Both are needed: CRMs catch method-level errors, spikes catch sample-specific matrix problems."

- question: "What is the fundamental distinction between quality assurance (QA) and quality control (QC), and why does a laboratory need both rather than one or the other?"
  type: short-answer
  answer: "QA is the system of policies, procedures, documentation, and management practices that creates an environment where reliable data can consistently be produced — SOPs, training records, equipment maintenance logs, calibration documentation, and proficiency testing. QC is the set of specific technical checks performed during each analytical batch — control charts, blanks, duplicates, spikes, and reference materials — that verify the system is actually working correctly at the moment of measurement. You need both: QA ensures the right procedures exist and analysts are competent; QC catches failures in real time when something goes wrong despite the QA framework."
  explanation: "The distinction matters because each addresses a different failure mode. QA prevents failure by building a capable system; QC detects failure when it occurs. A lab with strong QC but no QA might catch errors but will struggle to prevent them systematically. A lab with strong QA but no QC has good policies but no feedback mechanism to know when those policies are failing in practice. ISO/IEC 17025 requires both, and traceability — the ability to follow a reported value back through the entire chain of QC checks and QA documentation — depends on them working together."
```

## Explainer

An analytical result is only useful if the people who rely on it can trust it. **Quality assurance** (QA) is the system of policies, procedures, and documentation that ensures a laboratory consistently produces reliable data, while **quality control** (QC) refers to the specific technical checks performed during and alongside each batch of analyses to verify that the system is working correctly at the time of measurement. From your study of quality assurance principles and statistical methods, you understand that individual measurements contain both random and systematic error. The QA/QC system is how a laboratory detects, quantifies, and controls those errors in routine operation.

The backbone of QC in an analytical laboratory is the **control chart**. In its simplest form (the Levey-Jennings chart), you analyze a control sample — a stable, well-characterized material at a known concentration — alongside every batch of real samples. You plot each control result on a chart with the established mean at center and warning limits at ±2 standard deviations and action limits at ±3 standard deviations. As long as control results fall randomly within the warning limits, the system is in statistical control. Patterns that signal trouble include a single result beyond the action limits, two consecutive results beyond a warning limit on the same side, or a run of seven or more consecutive results on one side of the mean (indicating a systematic drift). The **Westgard rules** formalize these patterns into a decision framework that tells the analyst when to accept the batch, investigate, or reject the results and re-analyze.

Beyond control charts, a complete QC program includes several additional elements. **Method blanks** (processing a sample with no analyte through the entire procedure) verify that the reagents and equipment are not contributing contamination. **Duplicate analyses** assess precision for that specific batch. **Spiked samples** (adding a known amount of analyte to a real sample and measuring recovery) check for matrix effects and systematic bias. **Certified reference materials** (CRMs) provide an independent accuracy check because their composition has been established by authoritative bodies using multiple independent methods. Each of these QC elements targets a different failure mode: blanks catch contamination, duplicates catch precision problems, spikes catch bias, and CRMs catch systematic method errors.

The QA framework wraps around these technical checks with documentation and management practices: **standard operating procedures** (SOPs) that specify exactly how each method is performed, **training records** that verify analyst competency, **instrument maintenance and calibration logs**, **chain-of-custody documentation** for regulated samples, and regular **proficiency testing** where the laboratory analyzes blind samples from an external provider and compares its results to the accepted values. Laboratories operating under accreditation standards (ISO/IEC 17025 is the international standard for testing and calibration laboratories) must demonstrate all of these elements during regular audits. The underlying principle is that every result should be traceable — you should be able to follow the chain from the final reported value back through the instrument calibration, the QC checks, the sample handling, and the method validation to show that the number is defensible.
