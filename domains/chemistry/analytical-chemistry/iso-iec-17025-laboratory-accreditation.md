---
id: iso-iec-17025-laboratory-accreditation
title: ISO/IEC 17025 Laboratory Accreditation
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: quality-control-and-quality-assurance
  type: hard
- id: analytical-method-validation-core-parameters
  type: hard
builds-toward:
- quality-assurance-analytical
tags:
- accreditation
- iso-iec-17025
- quality
stage: advanced
status: draft
---

# ISO/IEC 17025 Laboratory Accreditation

## Core Idea
ISO/IEC 17025 is the international standard specifying requirements for laboratory competence in testing and calibration, covering management systems, technical competence, equipment calibration, personnel training, method validation, quality assurance, and proficiency testing. Accreditation to ISO 17025 by national accrediting bodies provides third-party independent verification that laboratory results are reliable, metrologically traceable to SI units, and suitable for regulatory, contractual, and liability decision-making.

## Questions

```yaml
- question: "A laboratory is ISO/IEC 17025 accredited for measuring lead in drinking water by ICP-MS. A client asks the lab to analyze pesticide residues in food using the same instruments. Which statement best describes the accreditation status of the pesticide analysis?"
  type: multiple-choice
  options:
    - "The analysis is covered because the lab is accredited and the instruments are the same"
    - "The analysis is covered if the lab uses a validated method"
    - "The analysis is not covered because accreditation is granted for a defined scope of specific methods and matrices"
    - "The analysis is covered as long as the client signs a contract with the lab"
  answer: 2
  explanation: "ISO/IEC 17025 accreditation is scope-specific — it covers exactly the methods and matrices listed in the accreditation certificate, not everything the laboratory does. Using the same instruments for a different analyte or matrix falls outside that scope. A common misconception is that accreditation is a blanket endorsement of the laboratory; in reality, it verifies competence for particular, defined activities."

- question: "A laboratory reports that a water sample contains 15.3 μg/L of lead, traceable to NIST SRM 3128. This traceability means:"
  type: multiple-choice
  options:
    - "The result was verified by NIST independently"
    - "The calibration chain links the measurement through documented steps back to an SI-recognized reference standard"
    - "The sample was prepared by NIST and sent to the laboratory for analysis"
    - "The method was approved by NIST for regulatory use"
  answer: 1
  explanation: "Metrological traceability means there is an unbroken chain of calibrations connecting the laboratory's result back to a recognized reference — ultimately to SI units. Using NIST-certified reference materials establishes that link. Traceability does not mean NIST verified the specific result or approved the method; it means the number carries a defined meaning that is reproducible and comparable across laboratories."

- question: "ISO/IEC 17025 accreditation covers all test methods a laboratory performs, not just those listed in the accreditation scope."
  type: true-false
  answer: false
  explanation: "Accreditation is strictly scope-limited. Accrediting bodies grant approval for specific test methods on specific sample matrices, as listed in the laboratory's scope of accreditation. Tests performed outside this scope are not covered by accreditation, even if the laboratory's general quality system is strong."

- question: "ISO/IEC 17025 requires that every measurement result be accompanied by an estimate of measurement uncertainty."
  type: true-false
  answer: true
  explanation: "Measurement uncertainty is a core technical requirement of ISO/IEC 17025. A result without an uncertainty estimate cannot be fully interpreted — it is unclear how confident anyone should be in the number. The standard requires laboratories to have procedures for estimating uncertainty and to report it alongside results, especially for calibration work and testing with regulatory or contractual significance."

- question: "What is metrological traceability, and why is it central to ISO/IEC 17025 accreditation?"
  type: short-answer
  answer: "Metrological traceability is the property of a measurement result that it can be linked through an unbroken chain of calibrations, each with stated uncertainties, to a recognized reference — ultimately to SI units. It matters for accreditation because it ensures that a laboratory's measurements have a defined meaning that is reproducible and comparable across laboratories and over time. Without traceability, a number reported by one laboratory cannot be meaningfully compared to the same measurement made elsewhere."
  explanation: "Traceability is what makes a measurement credible to parties outside the lab — regulators, clients, courts. A laboratory that can document its entire calibration chain demonstrates that its '15.3 μg/L' result means the same thing as another accredited lab's '15.3 μg/L' result. This comparability is why ISO 17025 exists: to provide confidence that different laboratories produce interchangeable, defensible results."
```

## Explainer

From your work with quality control and quality assurance, you understand that analytical laboratories need systematic approaches to ensure their results are reliable — control charts, reference materials, proficiency testing, and documented procedures. From method validation, you know how to demonstrate that a specific analytical method performs within defined specifications. **ISO/IEC 17025** is the international framework that pulls all of these elements together into a single, auditable standard for laboratory competence. When a laboratory achieves accreditation to ISO 17025, it means an independent third party has verified that the laboratory has the technical competence, management systems, and quality infrastructure to produce reliable results.

The standard is organized around two pillars: **management requirements** and **technical requirements**. The management side covers what you might expect from a quality system — document control, corrective and preventive actions, internal audits, management reviews, and complaint handling. But the technical requirements are where ISO 17025 becomes specific to laboratories. These include requirements for personnel competence (analysts must be trained, assessed, and authorized for each method they perform), equipment calibration (every instrument must be calibrated against traceable standards on a defined schedule, with records maintained), method validation (each method must be demonstrated fit for its intended purpose before use on real samples), **measurement uncertainty** estimation (every result must be accompanied by a statement of how confident the laboratory is in that result), and sample handling procedures that maintain sample integrity from receipt through disposal.

A concept central to ISO 17025 is **metrological traceability** — the idea that every measurement result can be linked, through an unbroken chain of calibrations, back to a recognized standard, ultimately to the International System of Units (SI). When a laboratory reports that a water sample contains 15.3 μg/L of lead, traceability means it can show that its calibration standards were prepared from certified reference materials, that those reference materials are traceable to national metrology institutes, and that its instruments were calibrated against those standards on a documented schedule. Without traceability, a measurement is just a number — with it, the number carries a defined meaning that is comparable across laboratories and over time.

The practical process of accreditation involves a thorough assessment by an accreditation body (such as A2LA in the United States, UKAS in the United Kingdom, or DAkkS in Germany). Assessors review documentation, observe analysts performing tests, examine calibration records, and evaluate the laboratory's proficiency testing results. Accreditation is granted for a defined **scope** — specific test methods on specific matrices — not as a blanket endorsement of everything the laboratory does. Maintaining accreditation requires ongoing surveillance assessments, successful participation in proficiency testing programs, and continuous internal monitoring. For the analytical chemist, working within an ISO 17025 system means that every measurement is embedded in a framework of documented competence, traceability, and continuous improvement — the laboratory equivalent of showing your work at every step.
