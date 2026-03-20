---
id: reference-materials
title: Reference Materials and Traceability
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: quality-assurance-analytical
  type: hard
tags:
- CRM
- certified reference material
- traceability
- proficiency testing
- matrix matching
- NIST
- metrological traceability
stage: advanced
status: draft
---

# Reference Materials and Traceability

## Core Idea
A certified reference material (CRM) is a substance with one or more property values established by a metrologically valid procedure, accompanied by a certificate providing the certified value, its uncertainty, and a statement of traceability to SI units or an internationally recognized measurement standard. CRMs serve three roles in analytical chemistry: validating that a method produces accurate results (method validation), monitoring ongoing method performance (quality control), and calibrating instruments. Matrix-matched CRMs — whose composition resembles the actual sample — are particularly valuable because they test whether the method handles real-world interferences correctly. Proficiency testing programs extend this concept by distributing identical samples to multiple laboratories and comparing results, revealing systematic biases that internal QC cannot detect.

## How It's Best Learned
Analyze a commercially available CRM (such as NIST SRM 1643 for trace elements in water) alongside routine samples, compare the measured value to the certified value within its stated uncertainty, and document the result in a control chart. This exercise demonstrates both the concept of traceability and the practical discipline of ongoing quality assurance.

## Common Misconceptions
- A reference material and a certified reference material are not the same; a CRM has values established with documented traceability and uncertainty, while a generic reference material may lack this metrological rigor.
- Using a CRM once during method validation is insufficient; it should be analyzed periodically as part of ongoing quality control to detect method drift or instrument degradation over time.

## Explainer

From your study of quality assurance in analytical chemistry, you know that producing a number is not the same as producing a *trustworthy* number. Reference materials are the mechanism by which the analytical community anchors measurements to a common standard of truth. Without them, two laboratories analyzing the same sample could report different results with no way to determine which — if either — is correct. **Metrological traceability** is the principle that every measurement should be connected, through an unbroken chain of comparisons, to a recognized standard, ultimately to SI units. Reference materials are the physical embodiments of links in that chain.

A **certified reference material (CRM)** is not simply a "known sample." It is a material whose property values have been determined by a procedure that meets strict metrological criteria, and it comes with a certificate stating the certified value, its expanded uncertainty (typically at 95% confidence), and a statement of how the value is traceable to SI or international standards. Organizations like NIST (United States), BAM (Germany), and NRC (Canada) produce CRMs following ISO Guide 34 and ISO 17034 standards. The uncertainty on the certificate is not a formality — it defines the range within which the true value lies, and your measured result must fall within your method's uncertainty combined with the CRM's uncertainty to be considered acceptable.

**Matrix matching** is a concept that separates useful CRMs from misleading ones. A pure aqueous standard of lead at 10 µg/L tells you whether your instrument is calibrated, but it does not test whether your method can extract lead from soil, survive the digestion step, or tolerate the iron and calcium present in a real soil matrix. A matrix-matched CRM — say, NIST SRM 2710a (Montana Soil) — contains certified lead values in an actual soil matrix, testing the entire analytical procedure from sample preparation through measurement. When your result on the CRM agrees with the certified value, you have evidence that your method works for real samples, not just clean standards.

CRMs serve three distinct roles in laboratory practice. During **method validation**, analyzing a CRM demonstrates that the method produces accurate results — this is the initial proof that the method works. During **routine quality control**, a CRM is analyzed alongside every batch of samples and the result is plotted on a control chart. As long as CRM results cluster around the certified value within expected limits, you have ongoing evidence that the method remains in control. When a CRM result falls outside control limits, it is an early warning that something has changed — reagent degradation, instrument drift, a new analyst's technique — before the problem corrupts sample results. Finally, **proficiency testing** extends the concept beyond a single laboratory: an external organization sends identical samples to many labs and compares their results, revealing systematic biases that internal QC with a lab's own CRM cannot detect. Together, these three uses create a layered system of accountability that gives analytical results their credibility.
