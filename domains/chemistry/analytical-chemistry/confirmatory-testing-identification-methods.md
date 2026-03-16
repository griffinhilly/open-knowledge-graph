---
id: confirmatory-testing-identification-methods
title: Confirmatory Testing and Identification Methods
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: analytical-chemistry-intro
  type: hard
- id: structure-elucidation-using-ir-nmr-and-ms
  type: hard
builds-toward:
- forensic-evidence-analytical-methods
- pharmaceutical-impurity-related-substances
tags:
- identification
- confirmation
- specificity
stage: advanced
status: draft
---

# Confirmatory Testing and Identification Methods

## Core Idea
Confirmatory testing employs orthogonal, independent analytical techniques to unequivocally verify analyte identity, eliminating false positives from screening methods. Confirmatory approaches apply selective detection (tandem mass spectrometry, high-resolution MS, NMR) combined with chromatographic separation, use multiple retention markers (retention time, mass-to-charge ratios), and enable structural elucidation of unknown components, providing the high confidence required for forensic, clinical, and regulatory compliance decisions.

## Explainer

Screening methods are designed to cast a wide net — they quickly flag samples that might contain a target substance, but they accept some rate of false positives because speed and throughput matter more than certainty at that stage. A workplace drug immunoassay, for example, might cross-react with structurally similar compounds, flagging a sample as positive when the target drug is actually absent. **Confirmatory testing** exists to resolve this uncertainty. It applies one or more independent, highly selective techniques to definitively establish whether the analyte is truly present, using principles that are fundamentally different from those of the screening method.

The key concept is **orthogonality** — the idea that confirmatory techniques should rely on different physical or chemical properties than the screening method. From your work on structure elucidation using IR, NMR, and MS, you already understand that each spectroscopic technique probes different molecular features: IR detects functional group vibrations, NMR reveals the hydrogen and carbon framework, and MS provides molecular mass and fragmentation patterns. If two independent techniques both identify the same compound, the probability that the identification is wrong drops dramatically because a false positive would have to produce matching artifacts in two unrelated measurement systems simultaneously.

In modern practice, **tandem mass spectrometry** (MS/MS) coupled with chromatographic separation is the gold standard for confirmatory analysis. The chromatographic step provides a retention time that the analyte must match, and the MS/MS step fragments the parent ion into characteristic product ions. Confirmation typically requires matching the retention time (within a tight tolerance, often ±2%), the presence of at least two characteristic precursor-to-product ion transitions, and the correct ratio between those transitions (called **ion ratios**, typically within ±20–30% of the reference standard). Meeting all these criteria simultaneously makes false identification extremely unlikely. High-resolution mass spectrometry (HRMS) adds another dimension by measuring exact mass to four decimal places, narrowing the pool of candidate molecular formulas to one or a very few.

The stakes for confirmatory testing are highest in forensic, clinical, and regulatory contexts where analytical results have legal or medical consequences. A positive drug test that leads to job termination, a doping violation in sport, or a food safety recall must rest on analytically defensible evidence. This is why regulatory frameworks — the Substance Abuse and Mental Health Services Administration (SAMHSA) guidelines, World Anti-Doping Agency (WADA) protocols, EU Commission Decision 2002/657/EC — all mandate specific confirmatory criteria including the number of identification points, acceptable ion ratio tolerances, and the requirement for chromatographic separation before detection. The confirmatory result is not just a second measurement; it is a fundamentally different measurement designed so that the only way both tests agree is if the analyte is genuinely there.
