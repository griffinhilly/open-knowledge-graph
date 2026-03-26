---
id: pharmaceutical-quality-analysis
title: Pharmaceutical Quality and Purity Analysis
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: hplc
  type: hard
- id: method-validation
  type: hard
tags:
- pharmaceutical
- drug analysis
- quality control
stage: advanced
status: validated
---

# Pharmaceutical Quality and Purity Analysis

## Core Idea
Pharmaceutical analysis determines active pharmaceutical ingredient content, impurity profiles, and degradation products in drug substances and finished products. Methods must comply with pharmacopeial standards and regulatory requirements for stability and quality assurance.

## Questions

```yaml
- question: "An analyst detects a synthetic intermediate at 0.12% in a drug product taken at a daily dose of 1 g. According to ICH Q3A thresholds, what action is required?"
  type: multiple-choice
  options:
    - "No action is needed — 0.12% is below all reporting thresholds"
    - "The impurity must be reported and structurally identified"
    - "The impurity must only be reported, not identified"
    - "The impurity must be reported, identified, and qualified for safety"
  answer: 1
  explanation: "For a 1 g/day drug, the ICH Q3A identification threshold is 0.10% — any impurity above this level must be structurally characterized. At 0.12%, the impurity exceeds the identification threshold but not the qualification threshold (0.15% for a 2 g/day drug; similar thresholds apply here), so structural identification is required but a full safety qualification study is not yet triggered. Option D would apply if the level were above the qualification threshold."

- question: "A USP monograph specifies a particular C18 column, mobile phase, and detection wavelength for a drug assay. A laboratory wants to use a slightly different column from a different manufacturer. What must they do?"
  type: multiple-choice
  options:
    - "Nothing — column brand does not affect the validity of a USP method"
    - "Document the change in a lab notebook and proceed"
    - "Formally demonstrate method equivalence through validation before using the alternative column"
    - "Obtain permission from the drug manufacturer before any changes"
  answer: 2
  explanation: "USP monographs are legally enforceable standards, not guidelines. A laboratory may use an alternative system only if they can formally demonstrate equivalence — meaning the alternative column produces results within the same acceptance criteria as the specified method. This requires validation data showing equivalent selectivity, accuracy, and precision. Simply assuming a column of the same type from a different vendor will perform identically is not acceptable in a regulated pharmaceutical quality control laboratory."

- question: "Accelerated stability testing at 40°C/75% relative humidity is used to predict long-term shelf life more quickly than waiting for real-time data."
  type: true-false
  answer: true
  explanation: "Accelerated stability conditions (40°C/75% RH) stress the drug product to speed up degradation kinetics, allowing prediction of long-term behavior in months rather than years. These results are used to support early approval timelines and set preliminary shelf-life estimates while real-time data at 25°C/60% RH accumulates. The two datasets together establish the approved shelf life and storage conditions."

- question: "The 95–105% of label claim acceptance criterion for API content applies universally to most pharmaceutical dosage forms."
  type: true-false
  answer: false
  explanation: "While 95–105% is a common range for solid oral dosage forms, acceptance criteria are set individually in each pharmacopeial monograph and regulatory submission. Narrow therapeutic index drugs (e.g., anticoagulants, thyroid hormones) may have tighter specifications (e.g., 90–110% or even narrower), while some biologics or modified-release products have different acceptance windows. The criterion is product-specific, not universal."

- question: "Why are ICH impurity reporting, identification, and qualification thresholds expressed relative to daily dose rather than simply as a fixed percentage of the drug product?"
  type: short-answer
  answer: "Because the actual amount of impurity a patient is exposed to depends on how much drug they take. A 0.1% impurity in a 10 mg/day drug delivers 0.01 mg/day, while the same 0.1% in a 2 g/day drug delivers 2 mg/day — a 200-fold difference in exposure. Dose-based thresholds ensure that the safety evaluation is proportional to actual human exposure rather than to an arbitrary percentage that would be permissive for high-dose drugs and overly strict for low-dose drugs."
  explanation: "This dose-normalization principle underlies the entire ICH Q3A/Q3B framework. It reflects the toxicological reality that risk is driven by exposure (amount × duration), not by relative concentration alone. A substance that is safe at microgram per day exposures may be hazardous at milligram levels, so the threshold for requiring safety qualification must scale with the total amount reaching the patient."
```

## Explainer

From your study of HPLC, you know how to separate and quantify components in a mixture using liquid chromatography. From method validation, you understand how to prove that an analytical method performs reliably within defined specifications. **Pharmaceutical quality analysis** is where these skills converge on one of the highest-stakes applications in analytical chemistry: ensuring that every dose of medication a patient takes contains the right amount of the right compound, with impurities controlled to levels that are safe for human consumption.

The central analytical task is **assay** — determining the content of the **active pharmaceutical ingredient (API)** in a drug product. A tablet labeled as containing 500 mg of acetaminophen must actually contain between 475 and 525 mg (typically 95–105% of label claim) when tested by the official pharmacopeial method. HPLC with UV detection is the workhorse technique, and the methods are defined in extraordinary detail by pharmacopeias such as the **United States Pharmacopeia (USP)**, **European Pharmacopoeia (Ph. Eur.)**, and **Japanese Pharmacopoeia (JP)**. These are not guidelines — they are legally enforceable standards. When a USP monograph specifies a C18 column, a particular mobile phase composition, and a detection wavelength, a quality control laboratory must either use that method exactly or demonstrate equivalence through formal validation.

Equally important is **impurity profiling** — identifying and quantifying all substances in a drug product that are not the intended API. Impurities fall into several categories: **process-related impurities** (unreacted starting materials, synthetic intermediates, catalysts, and residual solvents from manufacturing), **degradation products** (compounds formed by chemical breakdown of the API during storage due to heat, light, moisture, or oxidation), and **elemental impurities** (heavy metals from equipment or raw materials). Regulatory guidelines, particularly **ICH Q3A/Q3B**, set reporting, identification, and qualification thresholds based on the daily dose of the drug. For a drug taken at 2 g/day, any impurity above 0.05% must be reported, above 0.1% must be structurally identified, and above 0.15% must be qualified for safety. These are remarkably low levels, and achieving the chromatographic resolution and detection sensitivity to meet them is a significant analytical challenge.

**Stability testing** ties assay and impurity analysis together over time. Regulatory authorities require that drug products be tested under defined storage conditions — 25°C/60% relative humidity for long-term studies, 40°C/75% RH for accelerated studies — at specified time points throughout the product's shelf life. The goal is to demonstrate that the API content remains within specification and that impurity levels do not exceed qualified limits over the labeled storage period. A failing stability result does not just affect a single batch — it can trigger product recalls, shorten approved shelf lives, and require reformulation. For the analytical chemist in a pharmaceutical quality control laboratory, every chromatographic run carries this weight: the results determine whether medicine reaches patients or gets destroyed.
