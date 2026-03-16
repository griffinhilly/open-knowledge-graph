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

## Explainer

From method validation, you know how to demonstrate that an analytical method works correctly at the time of validation. Quality assurance asks the next question: how do you know it is still working correctly on Tuesday of week 37, after three different analysts have used it, the column has been replaced twice, and a new lot of reagent has arrived? **Quality assurance (QA)** is the systematic framework that ensures data quality over time; **quality control (QC)** is the operational component — the specific measurements and checks performed during routine analysis to detect problems before they corrupt reported results.

The workhorse of laboratory QC is the **control chart**, most commonly a Shewhart chart. You analyze a QC sample (a stable material with a known or established value) alongside every batch of unknown samples, and plot the QC result on a chart with a center line (the established mean) and control limits set at ±2s and ±3s (where s is the standard deviation from the validation or initial characterization period). A result within ±2s is normal. A result between 2s and 3s is a warning. A result beyond ±3s — which should occur less than 0.3% of the time by chance — triggers an **out-of-control** investigation. Beyond single-point rules, the **Western Electric rules** detect subtler problems: six consecutive points trending in one direction indicate drift, two out of three points beyond ±2s suggest increased bias, and other patterns reveal specific failure modes like reagent degradation or calibration shift.

**Measurement traceability** is the concept that every reported result can be connected, through an unbroken chain of comparisons, to a recognized standard — ultimately to SI units. In practice, this chain runs from your working standard to your laboratory's reference standard, to a **certified reference material (CRM)** from an accredited supplier (NIST, LGC, etc.), and from there to the SI through the metrology institute's primary measurement. If any link in this chain is broken — if your working standard was prepared from an uncertified reagent, or if your balance was not calibrated against traceable weights — the results lack metrological validity. This is not merely bureaucratic: traceability ensures that your result of "4.2 mg/L lead" means the same thing as the result from a laboratory in another country.

Formal **accreditation** under ISO/IEC 17025 ties these elements together into a management system. An accredited laboratory must document its methods in **standard operating procedures (SOPs)**, maintain competency records for all analysts, participate in proficiency testing (inter-laboratory comparisons), conduct internal audits, and demonstrate traceability for all measurements. Accreditation does not guarantee that every result is correct — no system can do that — but it provides structured evidence that the laboratory has the processes in place to detect and correct problems. For laboratories whose data supports regulatory decisions, legal proceedings, or public health actions, accreditation is the threshold requirement for results to be accepted by external parties.
