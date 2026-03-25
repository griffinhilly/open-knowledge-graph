---
id: reference-materials
title: Reference Materials and Traceability
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: quality-assurance-analytical
  type: hard
- id: reference-material-traceability
  type: soft
tags:
- CRM
- certified reference material
- traceability
- proficiency testing
- matrix matching
- NIST
- metrological traceability
stage: advanced
status: validated
---
# Reference Materials and Traceability

## Core Idea
A certified reference material (CRM) is a substance with one or more property values established by a metrologically valid procedure, accompanied by a certificate providing the certified value, its uncertainty, and a statement of traceability to SI units or an internationally recognized measurement standard. CRMs serve three roles in analytical chemistry: validating that a method produces accurate results (method validation), monitoring ongoing method performance (quality control), and calibrating instruments. Matrix-matched CRMs — whose composition resembles the actual sample — are particularly valuable because they test whether the method handles real-world interferences correctly. Proficiency testing programs extend this concept by distributing identical samples to multiple laboratories and comparing results, revealing systematic biases that internal QC cannot detect.

## How It's Best Learned
Analyze a commercially available CRM (such as NIST SRM 1643 for trace elements in water) alongside routine samples, compare the measured value to the certified value within its stated uncertainty, and document the result in a control chart. This exercise demonstrates both the concept of traceability and the practical discipline of ongoing quality assurance.

## Common Misconceptions
- A reference material and a certified reference material are not the same; a CRM has values established with documented traceability and uncertainty, while a generic reference material may lack this metrological rigor.
- Using a CRM once during method validation is insufficient; it should be analyzed periodically as part of ongoing quality control to detect method drift or instrument degradation over time.

## Questions

```yaml
- question: "A laboratory analyzes a certified reference material during method validation, obtains a result within the certified uncertainty, and considers the method validated. A colleague objects. What is the most important flaw in this approach?"
  type: multiple-choice
  options:
    - "The lab should have used a matrix-matched standard rather than a CRM for validation"
    - "A single CRM analysis cannot detect method drift or degradation over time; periodic ongoing QC is required"
    - "The certified value must match the measured value exactly, not merely within uncertainty"
    - "CRMs are only suitable for instrument calibration, not full method validation"
  answer: 1
  explanation: "One-time CRM analysis during validation proves the method worked on that day, but methods drift — reagents degrade, instruments go out of alignment, techniques change. The CRM must be analyzed periodically in every batch so that results can be tracked on a control chart. When a CRM result eventually falls outside control limits, it is an early warning before sample data is corrupted. The other options misstate the role and requirements of CRMs."

- question: "Which statement best distinguishes a certified reference material (CRM) from a generic reference material?"
  type: multiple-choice
  options:
    - "A CRM has a higher purity grade than a generic reference material"
    - "A CRM has property values established with documented uncertainty and metrological traceability to SI units; a generic reference material may lack this rigor"
    - "Generic reference materials can be used for calibration; CRMs are reserved for proficiency testing"
    - "CRMs are produced exclusively by NIST, while generic reference materials can come from any supplier"
  answer: 1
  explanation: "The defining features of a CRM are its certificate: a certified value, the expanded uncertainty at a stated confidence level, and a statement of traceability to SI units or an international standard. A generic reference material — even one with a known nominal concentration — may not have been characterized by a metrologically valid procedure and therefore cannot provide the same quality assurance guarantees. NIST, BAM, and NRC are major producers, but CRM status is defined by the characterization process, not the producer."

- question: "Analyzing a matrix-matched CRM tests both instrument calibration and the full sample preparation procedure, including any real-world interferences present in the target matrix."
  type: true-false
  answer: true
  explanation: "This is precisely why matrix matching matters. A clean aqueous standard at the correct concentration tells you whether your instrument is calibrated, but it cannot reveal whether your digestion step efficiently extracts the analyte from a real soil or biological matrix, or whether common co-occurring elements suppress or enhance the signal. A matrix-matched CRM — made from actual soil, water, or tissue — travels through the entire method and therefore tests every step. Agreement with the certified value is evidence the whole procedure works, not just the instrument."

- question: "Because proficiency testing uses the same type of samples as in-house quality control, it provides no additional information beyond what a laboratory's own CRM program already reveals."
  type: true-false
  answer: false
  explanation: "In-house QC with a lab's own CRM can detect random error and drift within that lab, but it cannot reveal systematic biases shared by the lab's reagents, instruments, or analytical culture. Proficiency testing distributes identical samples to many independent laboratories and compares all results. A lab that is consistently high or low relative to its peers has a bias that internal QC — which is anchored to that same lab's procedures — would never expose. Proficiency testing is the only mechanism that catches lab-wide systematic error."

- question: "Why must a CRM be matrix-matched to reliably validate an analytical method for real environmental or biological samples?"
  type: short-answer
  answer: "A pure standard only tests whether the instrument responds correctly to the analyte in a clean medium. Real samples contain matrices — soil particles, organic matter, competing ions, proteins — that can suppress or enhance signals, co-elute with analytes, or be lost during sample preparation. A matrix-matched CRM undergoes the full analytical procedure in the same chemical environment as real samples. When the result agrees with the certified value, you have evidence that the method correctly handles real-world interferences, not just a calibration check."
  explanation: "The distinction is between verifying calibration (clean standard) and verifying the complete analytical system (matrix-matched CRM). Validation requires proof that the method produces accurate results on samples resembling those you actually analyze. Without a matching matrix, you cannot rule out systematic errors introduced during digestion, extraction, or signal suppression in complex matrices."
```

## Explainer

From your study of quality assurance in analytical chemistry, you know that producing a number is not the same as producing a *trustworthy* number. Reference materials are the mechanism by which the analytical community anchors measurements to a common standard of truth. Without them, two laboratories analyzing the same sample could report different results with no way to determine which — if either — is correct. **Metrological traceability** is the principle that every measurement should be connected, through an unbroken chain of comparisons, to a recognized standard, ultimately to SI units. Reference materials are the physical embodiments of links in that chain.

A **certified reference material (CRM)** is not simply a "known sample." It is a material whose property values have been determined by a procedure that meets strict metrological criteria, and it comes with a certificate stating the certified value, its expanded uncertainty (typically at 95% confidence), and a statement of how the value is traceable to SI or international standards. Organizations like NIST (United States), BAM (Germany), and NRC (Canada) produce CRMs following ISO Guide 34 and ISO 17034 standards. The uncertainty on the certificate is not a formality — it defines the range within which the true value lies, and your measured result must fall within your method's uncertainty combined with the CRM's uncertainty to be considered acceptable.

**Matrix matching** is a concept that separates useful CRMs from misleading ones. A pure aqueous standard of lead at 10 µg/L tells you whether your instrument is calibrated, but it does not test whether your method can extract lead from soil, survive the digestion step, or tolerate the iron and calcium present in a real soil matrix. A matrix-matched CRM — say, NIST SRM 2710a (Montana Soil) — contains certified lead values in an actual soil matrix, testing the entire analytical procedure from sample preparation through measurement. When your result on the CRM agrees with the certified value, you have evidence that your method works for real samples, not just clean standards.

CRMs serve three distinct roles in laboratory practice. During **method validation**, analyzing a CRM demonstrates that the method produces accurate results — this is the initial proof that the method works. During **routine quality control**, a CRM is analyzed alongside every batch of samples and the result is plotted on a control chart. As long as CRM results cluster around the certified value within expected limits, you have ongoing evidence that the method remains in control. When a CRM result falls outside control limits, it is an early warning that something has changed — reagent degradation, instrument drift, a new analyst's technique — before the problem corrupts sample results. Finally, **proficiency testing** extends the concept beyond a single laboratory: an external organization sends identical samples to many labs and compares their results, revealing systematic biases that internal QC with a lab's own CRM cannot detect. Together, these three uses create a layered system of accountability that gives analytical results their credibility.
