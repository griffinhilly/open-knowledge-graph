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

## Explainer

An analytical result is only useful if the people who rely on it can trust it. **Quality assurance** (QA) is the system of policies, procedures, and documentation that ensures a laboratory consistently produces reliable data, while **quality control** (QC) refers to the specific technical checks performed during and alongside each batch of analyses to verify that the system is working correctly at the time of measurement. From your study of quality assurance principles and statistical methods, you understand that individual measurements contain both random and systematic error. The QA/QC system is how a laboratory detects, quantifies, and controls those errors in routine operation.

The backbone of QC in an analytical laboratory is the **control chart**. In its simplest form (the Levey-Jennings chart), you analyze a control sample — a stable, well-characterized material at a known concentration — alongside every batch of real samples. You plot each control result on a chart with the established mean at center and warning limits at ±2 standard deviations and action limits at ±3 standard deviations. As long as control results fall randomly within the warning limits, the system is in statistical control. Patterns that signal trouble include a single result beyond the action limits, two consecutive results beyond a warning limit on the same side, or a run of seven or more consecutive results on one side of the mean (indicating a systematic drift). The **Westgard rules** formalize these patterns into a decision framework that tells the analyst when to accept the batch, investigate, or reject the results and re-analyze.

Beyond control charts, a complete QC program includes several additional elements. **Method blanks** (processing a sample with no analyte through the entire procedure) verify that the reagents and equipment are not contributing contamination. **Duplicate analyses** assess precision for that specific batch. **Spiked samples** (adding a known amount of analyte to a real sample and measuring recovery) check for matrix effects and systematic bias. **Certified reference materials** (CRMs) provide an independent accuracy check because their composition has been established by authoritative bodies using multiple independent methods. Each of these QC elements targets a different failure mode: blanks catch contamination, duplicates catch precision problems, spikes catch bias, and CRMs catch systematic method errors.

The QA framework wraps around these technical checks with documentation and management practices: **standard operating procedures** (SOPs) that specify exactly how each method is performed, **training records** that verify analyst competency, **instrument maintenance and calibration logs**, **chain-of-custody documentation** for regulated samples, and regular **proficiency testing** where the laboratory analyzes blind samples from an external provider and compares its results to the accepted values. Laboratories operating under accreditation standards (ISO/IEC 17025 is the international standard for testing and calibration laboratories) must demonstrate all of these elements during regular audits. The underlying principle is that every result should be traceable — you should be able to follow the chain from the final reported value back through the instrument calibration, the QC checks, the sample handling, and the method validation to show that the number is defensible.
