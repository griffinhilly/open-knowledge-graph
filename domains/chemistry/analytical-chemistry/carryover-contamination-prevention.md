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
status: validated
---

# Carryover and Cross-Contamination Prevention

## Core Idea
Carryover contamination occurs when residual analyte from one sample remains in instrumental pathways and contaminates the subsequent sample, causing false positives and positive bias in results. Prevention requires appropriate instrument flush volumes and solvent strength progression, careful sample-to-sample ratio management, optimized sample introduction system design, and systematic carryover assessment. Carryover is particularly problematic in high-throughput screening and clinical applications where analyte concentrations vary widely.

## Questions

```yaml
- question: "A laboratory runs samples ranging from 1 ng/mL to 10,000 ng/mL in randomized sequence. Low-concentration samples run immediately after high-concentration samples consistently read higher than expected. What is the most likely cause and the most effective sequence-design fix?"
  type: multiple-choice
  options:
    - "Detector saturation from high-concentration samples; fix by diluting all samples uniformly"
    - "Carryover from residual analyte in the sample introduction pathway; fix by running samples in low-to-high concentration order"
    - "Matrix effects from sample-to-sample carry of matrix components; fix by using a different solvent for all samples"
    - "Baseline drift from thermal expansion; fix by allowing longer equilibration time between injections"
  answer: 1
  explanation: "The pattern — low-concentration samples reading high after high-concentration ones — is the diagnostic signature of carryover. Residual analyte from the concentrated sample contaminates the subsequent injection. Running samples in ascending concentration order is the most effective sequence-design fix: it minimizes the concentration drop between consecutive injections, reducing the severity of any carryover that occurs. Running a 10,000 ng/mL sample followed by 1 ng/mL creates a 10,000-fold gradient that any residual analyte can bridge; running 1, 10, 100, 1000 ... dramatically reduces this problem. Option A (detector saturation) would affect only the high-concentration samples themselves, not subsequent ones."

- question: "A scientist designs a wash sequence for an HPLC autosampler after running very hydrophobic analytes. She programs a single wash with aqueous buffer. Why is this wash likely to be insufficient?"
  type: multiple-choice
  options:
    - "Aqueous buffers have too high a viscosity to flush the sample loop effectively at typical flow rates"
    - "Hydrophobic analytes adsorb strongly to metal and polymer surfaces and require an organic solvent wash to be displaced"
    - "A single wash volume is always insufficient regardless of solvent choice — multiple volumes are always required"
    - "The aqueous wash will precipitate the analyte in the transfer line, worsening carryover"
  answer: 1
  explanation: "Designing a wash sequence means thinking about the chemistry of adsorption, not just the plumbing. Hydrophobic analytes adsorb to hydrophobic surfaces through non-polar interactions that aqueous solvents cannot solvate effectively. An organic solvent (methanol, acetonitrile) with high elution strength for hydrophobic compounds is needed to strip residual analyte. Option C is a common misconception — multiple volumes of the wrong solvent may accomplish less than a single wash with the right solvent. Solvent *chemistry* is as important as wash *volume*."

- question: "Carryover is easily identified because it causes abnormal-looking peaks or error flags in chromatograms, alerting analysts to the problem before results are reported."
  type: true-false
  answer: false
  explanation: "The explainer describes carryover as 'insidious' precisely because 'it produces results that look perfectly normal but are systematically wrong.' A contaminated blank or low-concentration sample produces a peak with normal shape, correct retention time, and expected detector response. There are no automated error flags. The only way to detect carryover is systematic assessment: running a blank after the highest-concentration sample and checking whether signal appears above the method detection limit. Carryover is a silent error that requires deliberate testing to uncover."

- question: "Running a blank after every high-concentration sample (bracketing blanks) serves primarily to detect method detection limit errors rather than to assess carryover between samples."
  type: true-false
  answer: false
  explanation: "Bracketing blanks — running a blank after every high-concentration sample — are specifically described as a carryover safety net, particularly in clinical and forensic contexts where a false positive result can have serious consequences. The blank should contain no signal above the MDL; if it does, carryover from the preceding high-concentration sample has occurred. The method detection limit (MDL) is a separate concept relating to the lowest concentration detectable above background noise, not to sample-to-sample contamination between injections."

- question: "Why is thinking about adsorption chemistry more important than simply increasing wash volume when designing a carryover prevention strategy?"
  type: short-answer
  answer: "Because a wash's effectiveness depends on the chemical affinity between the analyte and the solvent, not just the volume pushed through the system. An analyte adsorbing strongly to stainless steel or polymer tubing through hydrophobic or ionic interactions cannot be removed by a solvent that doesn't disrupt those interactions — even with large volumes. The right solvent chemistry (an organic solvent for hydrophobic analytes, an acidic wash for basic analytes stuck to metal surfaces) can remove residual analyte in a small volume, while the wrong solvent may fail even with large volumes."
  explanation: "This is why 'a single wash solvent is rarely sufficient' — different surfaces and analytes have different adsorption chemistries, and a wash sequence that addresses multiple mechanisms (e.g., weak aqueous rinse followed by strong organic wash) is more reliable than a one-size-fits-all approach. Volume is a secondary optimization; chemistry is the primary design constraint. Failing to account for adsorption chemistry is the most common reason carryover persists despite extensive flushing."
```

## Explainer

Imagine running a very concentrated sample through your instrument and then immediately analyzing a blank or a low-concentration sample. If traces of the first sample linger in the injection port, transfer lines, or detector, that residue shows up as a phantom signal in the next measurement. This is **carryover** — and it is one of the most insidious sources of error in analytical chemistry because it produces results that look perfectly normal but are systematically wrong. Your background in sample preparation has shown you how carefully samples must be handled before they reach the instrument; carryover extends that concern into the instrument itself.

The primary strategy for preventing carryover is **systematic flushing** between injections. In liquid chromatography, this means programming wash cycles with solvents of increasing elution strength — a weak solvent rinse followed by a strong solvent rinse — to strip residual analyte from the autosampler needle, sample loop, and injection valve. In gas chromatography, baking the inlet and column at elevated temperatures between runs serves the same purpose. The key insight is that a single wash solvent is rarely sufficient: a molecule that adsorbs strongly to metal surfaces may need an aggressive organic solvent, while a polar contaminant may need an aqueous wash. Designing a wash sequence means thinking about the chemistry of adsorption, not just the plumbing of the instrument.

**Carryover assessment** should be built into every analytical sequence, not treated as a one-time validation exercise. The standard approach is to run a blank immediately after the highest-concentration standard or sample and check whether any signal appears above the method detection limit. A common acceptance criterion is that carryover in the blank must be less than 20% of the lowest calibration level. When carryover exceeds this threshold, you need to increase wash volumes, add wash steps, or reconsider the sample introduction system entirely — for example, switching from a fixed-loop injector to a flow-through needle design that is easier to flush.

Sequence design also plays a critical role. Arranging samples from low to high concentration within a batch minimizes the concentration jumps between consecutive injections, reducing the severity of any carryover that does occur. In clinical and forensic laboratories where a positive result can have serious consequences, **bracketing blanks** — running a blank after every high-concentration sample — provide an additional safety net. The underlying principle is straightforward: every surface the sample touches is a potential reservoir, and your job is to ensure that reservoir is empty before the next sample arrives.
