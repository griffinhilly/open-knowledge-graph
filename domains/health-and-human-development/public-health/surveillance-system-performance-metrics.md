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
stage: expert
status: validated
---

# Surveillance System Performance Metrics

## Core Idea
Surveillance system performance is evaluated using sensitivity (ability to detect cases), specificity (avoid false positives), positive predictive value (accuracy of positive tests), and timeliness (lag between event and reporting). These properties determine a system's ability to detect outbreaks early and guide data quality improvements. System improvements require identifying bottleneck components limiting sensitivity or specificity.

## How It's Best Learned
Evaluate a real surveillance system using performance metrics on historical data. Identify components limiting sensitivity or specificity and propose targeted improvements with expected impact.

## Common Misconceptions
Higher sensitivity is always better regardless of specificity trade-offs. Specificity is not important for disease surveillance systems. System performance is static rather than requiring continuous improvement and evaluation.

## Questions

```yaml
- question: "A state health department lowers its reporting threshold for a rare infectious disease, capturing 30% more true cases. An epidemiologist warns this change will create resource problems. What is her most likely concern?"
  type: multiple-choice
  options:
    - "Lower thresholds slow processing speed because more paperwork must be filed for each case"
    - "Increased sensitivity at very low disease prevalence reduces positive predictive value, generating more false-positive reports that must be investigated and that consume finite public health resources"
    - "Sensitivity and specificity are independent of the reporting threshold, so changing the threshold cannot affect the false-positive rate"
    - "Lower thresholds improve sensitivity and specificity simultaneously, so there is no trade-off to worry about"
  answer: 1
  explanation: "This is the PPV problem applied to surveillance. When a disease is rare, even a modestly imperfect system generates many false positives relative to true positives. Lowering the reporting threshold captures more true cases (sensitivity rises) but also accepts more false-positive reports. Each false-positive triggers contact tracing, environmental investigation, or patient follow-up — real costs that grow as the false-positive rate increases. The right threshold depends on disease severity: a highly transmissible pathogen justifies the resource cost; a less urgent condition may not."

- question: "A public health team wants to improve a salmonellosis surveillance system that detects only 1 in 29 actual cases. Which intervention strategy is most directly targeted at finding the true bottleneck?"
  type: multiple-choice
  options:
    - "Hire additional staff at the health department to process case reports more quickly"
    - "Lower the case definition threshold to include milder presentations"
    - "Systematically audit each stage of the reporting pipeline — from care-seeking to testing to reporting — to identify which step loses the most cases, then intervene there"
    - "Increase laboratory capacity to run more diagnostic tests per day"
  answer: 2
  explanation: "Bottleneck analysis is the key concept here. A surveillance pipeline with 3.5% sensitivity is losing cases at many points: some sick people never seek care, some who seek care are never tested, some who test positive are never reported. Intervening at the wrong stage (e.g., improving laboratory capacity when most cases are lost before patients see a doctor) wastes resources with minimal gain. Mapping the pipeline stage-by-stage and quantifying loss at each step is the only way to identify the correct intervention point."

- question: "A surveillance system can achieve high sensitivity for detecting true cases yet still have low positive predictive value (PPV) when the disease being surveilled is very rare in the population."
  type: true-false
  answer: true
  explanation: "This is the same PPV paradox you learned in biostatistics, operating at the population level. PPV depends on three things: sensitivity, specificity, and prevalence. When prevalence is very low, even a system with 99% specificity will generate many false positives for every true positive, because there are so many more non-cases in the population. A surveillance system detecting a disease affecting 1 in 100,000 people will be overwhelmed with false alarms even if its specificity is high. This is why PPV — not just sensitivity and specificity — must be considered when evaluating surveillance system performance."

- question: "Timeliness and sensitivity measure the same underlying property of a surveillance system — a system with higher sensitivity will automatically detect cases more quickly."
  type: true-false
  answer: false
  explanation: "Timeliness and sensitivity are orthogonal dimensions. Sensitivity measures the proportion of true cases that are ever detected; timeliness measures the lag between when an event occurs and when the system reports it. A system could detect 80% of cases but take 3 weeks to report each one (high sensitivity, poor timeliness) — useless for real-time outbreak control. Conversely, a system might report immediately but only capture 20% of cases. Improving timeliness requires reducing delays in the reporting pipeline; improving sensitivity requires capturing more cases at each stage."

- question: "Why does the appropriate trade-off between sensitivity and specificity in a surveillance system depend on the severity and transmissibility of the disease being surveilled?"
  type: short-answer
  answer: "For a highly lethal or rapidly transmissible disease, missing a true case carries extreme consequences — an undetected smallpox case or early cluster could be catastrophic. The cost of a missed case vastly exceeds the cost of investigating a false positive, so it makes sense to sacrifice specificity for sensitivity. For a less severe or less transmissible condition, the calculus reverses: false-positive reports consume investigative resources and may harm individuals (stigma, unnecessary treatment), while missed cases carry lower population-level consequences. The correct balance is a policy judgment that requires knowing the stakes on both sides."
  explanation: "This is analogous to medical testing: for diseases where missing a diagnosis is lethal (e.g., certain cancers), clinicians use highly sensitive screening tests and accept more false positives that trigger confirmatory workup. For conditions where overdiagnosis causes substantial harm, more specific tests are preferred. Surveillance faces the same trade-off at population scale — the 'cost' of a false positive is investigative resources and potential stigma; the 'cost' of a false negative is undetected disease spread or burden."
```

## Explainer

From your biostatistics background, you already know sensitivity and specificity as properties of diagnostic tests: sensitivity measures how well a test catches true cases (avoiding false negatives), while specificity measures how well it excludes non-cases (avoiding false positives). Applying these concepts to a surveillance system is a conceptual shift—you are no longer evaluating a single laboratory test but an entire sociotechnical pipeline that runs from the moment a sick person enters the healthcare system to the moment a case report lands in a health department database. Every step in that pipeline—clinical recognition, clinical testing, clinician reporting, laboratory reporting, case investigation, data entry—introduces opportunities for cases to fall through the cracks, and each gap reduces system sensitivity.

**Surveillance sensitivity** measures the proportion of true cases in the population that the system actually detects and counts. A system with 40% sensitivity is missing six out of ten cases. This matters enormously for outbreak detection: a foodborne illness cluster that sickens 100 people might generate only 5–10 reported cases if most patients do not seek care, their physicians do not test, or their physicians do not report. Surveillance data then show only the tip of an iceberg, and epidemiologists must apply **multipliers**—estimated ratios of true cases to reported cases—to reconstruct actual burden. For salmonellosis in the US, the CDC estimates roughly 29 cases occur for every 1 reported, implying a sensitivity of about 3.5%. A system this insensitive can still detect an outbreak if the ratio of true cases to expected background cases is large enough, but it will miss small clusters and undercount endemic burden.

**Specificity** becomes critical when the burden of false positives is high. For rare diseases, even a system that correctly flags 99% of non-cases will generate a large number of false-positive case reports if the disease is sufficiently uncommon—this is the same **positive predictive value (PPV)** problem you learned in biostatistics but now operating at the population level. False-positive case reports consume finite public health investigative resources: each one triggers contact tracing, environmental investigation, or patient follow-up that does not yield a true case. Lowering the reporting threshold to capture more cases (increasing sensitivity) will almost always reduce specificity, generating more false positives. The right trade-off depends on disease severity and the cost of missed cases versus spurious investigations—a highly lethal or transmissible pathogen justifies sacrificing specificity for sensitivity; a less urgent condition may warrant the reverse.

**Timeliness** is a performance dimension orthogonal to sensitivity and specificity: a system can be accurate but too slow. For outbreak detection, a surveillance system that detects an influenza wave two weeks after its peak provides information for historical analysis but not for real-time response. The lag between event and report—from onset to care-seeking, care-seeking to testing, testing to laboratory result, result to clinician, clinician to health department—is called the **reporting delay distribution**, and characterizing it is essential for interpreting surveillance data in real time. Systems can be redesigned to reduce lag: electronic laboratory reporting (ELR) that automatically transmits positive lab results to health departments reduces the clinician-reporting bottleneck. Identifying the **bottleneck component**—the step in the pipeline contributing the most to delay or missed cases—is the key to targeted system improvement, rather than intervening broadly at every stage simultaneously.
