---
id: surveillance-system-performance-metrics
title: Surveillance System Performance Metrics
domain: health-and-human-development
course: public-health
prerequisites:
- id: disease-surveillance-systems
  type: hard
- id: biostatistics-in-public-health
  type: hard
builds-toward:
- infectious-disease-surveillance
tags:
- surveillance
- sensitivity
- specificity
- ppv
- system-performance
stage: advanced
status: draft
---

# Surveillance System Performance Metrics

## Core Idea
Surveillance system performance is evaluated using sensitivity (ability to detect cases), specificity (avoid false positives), positive predictive value (accuracy of positive tests), and timeliness (lag between event and reporting). These properties determine a system's ability to detect outbreaks early and guide data quality improvements. System improvements require identifying bottleneck components limiting sensitivity or specificity.

## How It's Best Learned
Evaluate a real surveillance system using performance metrics on historical data. Identify components limiting sensitivity or specificity and propose targeted improvements with expected impact.

## Common Misconceptions
Higher sensitivity is always better regardless of specificity trade-offs. Specificity is not important for disease surveillance systems. System performance is static rather than requiring continuous improvement and evaluation.

## Explainer

From your biostatistics background, you already know sensitivity and specificity as properties of diagnostic tests: sensitivity measures how well a test catches true cases (avoiding false negatives), while specificity measures how well it excludes non-cases (avoiding false positives). Applying these concepts to a surveillance system is a conceptual shift—you are no longer evaluating a single laboratory test but an entire sociotechnical pipeline that runs from the moment a sick person enters the healthcare system to the moment a case report lands in a health department database. Every step in that pipeline—clinical recognition, clinical testing, clinician reporting, laboratory reporting, case investigation, data entry—introduces opportunities for cases to fall through the cracks, and each gap reduces system sensitivity.

**Surveillance sensitivity** measures the proportion of true cases in the population that the system actually detects and counts. A system with 40% sensitivity is missing six out of ten cases. This matters enormously for outbreak detection: a foodborne illness cluster that sickens 100 people might generate only 5–10 reported cases if most patients do not seek care, their physicians do not test, or their physicians do not report. Surveillance data then show only the tip of an iceberg, and epidemiologists must apply **multipliers**—estimated ratios of true cases to reported cases—to reconstruct actual burden. For salmonellosis in the US, the CDC estimates roughly 29 cases occur for every 1 reported, implying a sensitivity of about 3.5%. A system this insensitive can still detect an outbreak if the ratio of true cases to expected background cases is large enough, but it will miss small clusters and undercount endemic burden.

**Specificity** becomes critical when the burden of false positives is high. For rare diseases, even a system that correctly flags 99% of non-cases will generate a large number of false-positive case reports if the disease is sufficiently uncommon—this is the same **positive predictive value (PPV)** problem you learned in biostatistics but now operating at the population level. False-positive case reports consume finite public health investigative resources: each one triggers contact tracing, environmental investigation, or patient follow-up that does not yield a true case. Lowering the reporting threshold to capture more cases (increasing sensitivity) will almost always reduce specificity, generating more false positives. The right trade-off depends on disease severity and the cost of missed cases versus spurious investigations—a highly lethal or transmissible pathogen justifies sacrificing specificity for sensitivity; a less urgent condition may warrant the reverse.

**Timeliness** is a performance dimension orthogonal to sensitivity and specificity: a system can be accurate but too slow. For outbreak detection, a surveillance system that detects an influenza wave two weeks after its peak provides information for historical analysis but not for real-time response. The lag between event and report—from onset to care-seeking, care-seeking to testing, testing to laboratory result, result to clinician, clinician to health department—is called the **reporting delay distribution**, and characterizing it is essential for interpreting surveillance data in real time. Systems can be redesigned to reduce lag: electronic laboratory reporting (ELR) that automatically transmits positive lab results to health departments reduces the clinician-reporting bottleneck. Identifying the **bottleneck component**—the step in the pipeline contributing the most to delay or missed cases—is the key to targeted system improvement, rather than intervening broadly at every stage simultaneously.
