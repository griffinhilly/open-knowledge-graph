---
id: quality-assurance-analytical
title: Quality Assurance and Laboratory Quality Control
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: method-validation
  type: hard
- id: statistical-methods-analytical
  type: hard
tags:
- QA
- QC
- control charts
- SOP
- accreditation
- traceability
- certified reference material
stage: advanced
status: validated
---

# Quality Assurance and Laboratory Quality Control

## Core Idea
Quality assurance (QA) encompasses all planned and systematic activities that ensure an analytical laboratory produces reliable data; quality control (QC) is the operational subset — the measurements taken to verify that a method is performing as validated. Control charts (Shewhart charts) plot successive QC sample results and apply statistical rules (e.g., Western Electric rules) to detect bias and drift before they affect reported results. Measurement traceability — an unbroken chain of comparisons to national or international standards — underpins the metrological validity of results. Accreditation bodies (ISO/IEC 17025) formalize these requirements for laboratories providing data to external parties.

## How It's Best Learned
Maintain a control chart for a monthly QC sample over a semester-long laboratory course, applying rules to detect out-of-control events and diagnosing causes. Experiencing how a gradual reagent degradation or calibration drift manifests in control chart patterns is the most effective preparation for real laboratory work.

## Common Misconceptions
- QC checks on a single sample type do not validate performance across all sample types; a CRM matched to the matrix of interest is needed.
- Passing a control chart rule does not prove the result is correct — it proves the method is in statistical control relative to its historical performance.

## Questions

```yaml
- question: "A laboratory's Shewhart control chart shows all QC sample results within ±2s for the past month with no rule violations. An independent audit then reveals that a systematic calibration error has been biasing all results by +15% for three months. How is this possible?"
  type: multiple-choice
  options:
    - "It is not possible — a ±2s control chart would have detected a 15% bias as an out-of-control event"
    - "The control chart only detects variation relative to the laboratory's own historical performance; if the bias was consistent, the chart would show in-control results even while all values were wrong"
    - "Control charts track individual sample results, so a systematic calibration error would appear as random scatter"
    - "The ±2s control limits should have been set at ±1s to detect a 15% bias; this is a chart design error"
  answer: 1
  explanation: "This is the critical distinction between statistical control and accuracy. Control charts track whether the method is behaving consistently relative to its own historical performance (the established mean and standard deviation). If a calibration error was introduced during the establishment period, that error becomes baked into the center line. The chart then tracks consistency around that biased mean — and everything looks fine. Control charts detect *drift and instability*, not absolute accuracy. Only traceability to external reference materials reveals whether the established mean itself is correct."

- question: "A laboratory validates a method for measuring lead in drinking water using a certified reference material (CRM) in a clean water matrix. They then apply this validated method to measure lead in blood samples from occupationally exposed workers. What is the primary quality concern?"
  type: multiple-choice
  options:
    - "The method needs to be re-validated using a CRM matched to the blood matrix, since a clean-water CRM does not establish performance in blood"
    - "No concern — method validation transfers between matrices once the analytical procedure is confirmed accurate in any matrix"
    - "The laboratory needs only to recalibrate the instrument with blood-matrix standards before running the samples"
    - "The concern is only about detection limits, which may differ in blood versus clean water"
  answer: 0
  explanation: "Matrix effects — the influence of sample composition on the analytical signal — are a fundamental challenge in analytical chemistry. Blood contains proteins, lipids, cells, and endogenous metals that can suppress or enhance the lead signal, cause co-elution with interferences, or degrade instrument components. A CRM in clean water demonstrates that the method works in clean water. It says nothing about whether the method is free from matrix effects in blood. A matched CRM (e.g., certified bovine blood with a known lead concentration) is required to establish accuracy in the actual sample matrix."

- question: "A passing result on a control chart — most QC samples within ±2s with no rule violations — proves that the analytical results reported in that batch are accurate (close to the true values of the samples)."
  type: true-false
  answer: false
  explanation: "Passing a control chart proves statistical control — that the method is behaving consistently relative to its own historical baseline. It does not prove accuracy. The entire historical baseline could be biased (wrong calibration, matrix effects, incorrect reference values). A method can be perfectly in statistical control while producing results that are systematically 15% too high or too low. Accuracy requires external validation — traceability to national or international measurement standards through certified reference materials."

- question: "Measurement traceability means that a laboratory's reported results can be connected, through an unbroken chain of comparisons, to recognized national or international measurement standards."
  type: true-false
  answer: true
  explanation: "Traceability is the metrological foundation of analytical chemistry. The chain typically runs: analyst's working standard → laboratory reference standard → certified reference material from an accredited supplier (e.g., NIST, LGC) → SI units via the national metrology institute. Each link involves a documented comparison with stated uncertainty. If any link is broken — uncertified reagent, uncalibrated balance, uncharacterized CRM — the result cannot be shown to mean the same thing as a result from another laboratory. Traceability is what allows regulatory agencies to accept results from multiple laboratories as comparable."

- question: "What is the difference between a laboratory's results being 'in statistical control' and being 'accurate,' and why does this distinction matter for laboratories whose data supports regulatory or clinical decisions?"
  type: short-answer
  answer: "Statistical control means the method is producing consistent, reproducible results relative to its own historical performance — results cluster around a stable mean with predictable variability. Accuracy means the results are close to the true values of the quantities being measured. A method can be in perfect statistical control while being consistently wrong if the historical mean itself is biased. The distinction matters for regulatory and clinical decisions because consistency without accuracy produces repeatable but incorrect conclusions. A laboratory certifying that a drinking water source contains 3 μg/L lead (consistently, month after month) when it actually contains 45 μg/L would never trigger a rule violation — yet its data would fail to protect public health. Traceability to external standards is what bridges the gap between 'consistent with ourselves' and 'correct relative to the real world.'"
  explanation: "This is why both internal QC (control charts) and external QC (CRMs, proficiency testing, accreditation) are necessary. Internal QC catches instability and drift; external QC catches systematic bias. Neither alone is sufficient for high-stakes analytical work."
```

## Explainer

From method validation, you know how to demonstrate that an analytical method works correctly at the time of validation. Quality assurance asks the next question: how do you know it is still working correctly on Tuesday of week 37, after three different analysts have used it, the column has been replaced twice, and a new lot of reagent has arrived? **Quality assurance (QA)** is the systematic framework that ensures data quality over time; **quality control (QC)** is the operational component — the specific measurements and checks performed during routine analysis to detect problems before they corrupt reported results.

The workhorse of laboratory QC is the **control chart**, most commonly a Shewhart chart. You analyze a QC sample (a stable material with a known or established value) alongside every batch of unknown samples, and plot the QC result on a chart with a center line (the established mean) and control limits set at ±2s and ±3s (where s is the standard deviation from the validation or initial characterization period). A result within ±2s is normal. A result between 2s and 3s is a warning. A result beyond ±3s — which should occur less than 0.3% of the time by chance — triggers an **out-of-control** investigation. Beyond single-point rules, the **Western Electric rules** detect subtler problems: six consecutive points trending in one direction indicate drift, two out of three points beyond ±2s suggest increased bias, and other patterns reveal specific failure modes like reagent degradation or calibration shift.

**Measurement traceability** is the concept that every reported result can be connected, through an unbroken chain of comparisons, to a recognized standard — ultimately to SI units. In practice, this chain runs from your working standard to your laboratory's reference standard, to a **certified reference material (CRM)** from an accredited supplier (NIST, LGC, etc.), and from there to the SI through the metrology institute's primary measurement. If any link in this chain is broken — if your working standard was prepared from an uncertified reagent, or if your balance was not calibrated against traceable weights — the results lack metrological validity. This is not merely bureaucratic: traceability ensures that your result of "4.2 mg/L lead" means the same thing as the result from a laboratory in another country.

Formal **accreditation** under ISO/IEC 17025 ties these elements together into a management system. An accredited laboratory must document its methods in **standard operating procedures (SOPs)**, maintain competency records for all analysts, participate in proficiency testing (inter-laboratory comparisons), conduct internal audits, and demonstrate traceability for all measurements. Accreditation does not guarantee that every result is correct — no system can do that — but it provides structured evidence that the laboratory has the processes in place to detect and correct problems. For laboratories whose data supports regulatory decisions, legal proceedings, or public health actions, accreditation is the threshold requirement for results to be accepted by external parties.
