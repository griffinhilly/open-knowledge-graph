---
id: carryover-contamination-prevention
title: Carryover and Cross-Contamination Prevention
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: analytical-chemistry-intro
  type: hard
- id: sample-preparation
  type: soft
builds-toward:
- quality-control-and-quality-assurance
- batch-and-sequence-optimization
tags:
- contamination
- carryover
- quality-control
stage: advanced
status: draft
---

# Carryover and Cross-Contamination Prevention

## Core Idea
Carryover contamination occurs when residual analyte from one sample remains in instrumental pathways and contaminates the subsequent sample, causing false positives and positive bias in results. Prevention requires appropriate instrument flush volumes and solvent strength progression, careful sample-to-sample ratio management, optimized sample introduction system design, and systematic carryover assessment. Carryover is particularly problematic in high-throughput screening and clinical applications where analyte concentrations vary widely.

## Explainer

Imagine running a very concentrated sample through your instrument and then immediately analyzing a blank or a low-concentration sample. If traces of the first sample linger in the injection port, transfer lines, or detector, that residue shows up as a phantom signal in the next measurement. This is **carryover** — and it is one of the most insidious sources of error in analytical chemistry because it produces results that look perfectly normal but are systematically wrong. Your background in sample preparation has shown you how carefully samples must be handled before they reach the instrument; carryover extends that concern into the instrument itself.

The primary strategy for preventing carryover is **systematic flushing** between injections. In liquid chromatography, this means programming wash cycles with solvents of increasing elution strength — a weak solvent rinse followed by a strong solvent rinse — to strip residual analyte from the autosampler needle, sample loop, and injection valve. In gas chromatography, baking the inlet and column at elevated temperatures between runs serves the same purpose. The key insight is that a single wash solvent is rarely sufficient: a molecule that adsorbs strongly to metal surfaces may need an aggressive organic solvent, while a polar contaminant may need an aqueous wash. Designing a wash sequence means thinking about the chemistry of adsorption, not just the plumbing of the instrument.

**Carryover assessment** should be built into every analytical sequence, not treated as a one-time validation exercise. The standard approach is to run a blank immediately after the highest-concentration standard or sample and check whether any signal appears above the method detection limit. A common acceptance criterion is that carryover in the blank must be less than 20% of the lowest calibration level. When carryover exceeds this threshold, you need to increase wash volumes, add wash steps, or reconsider the sample introduction system entirely — for example, switching from a fixed-loop injector to a flow-through needle design that is easier to flush.

Sequence design also plays a critical role. Arranging samples from low to high concentration within a batch minimizes the concentration jumps between consecutive injections, reducing the severity of any carryover that does occur. In clinical and forensic laboratories where a positive result can have serious consequences, **bracketing blanks** — running a blank after every high-concentration sample — provide an additional safety net. The underlying principle is straightforward: every surface the sample touches is a potential reservoir, and your job is to ensure that reservoir is empty before the next sample arrives.
