---
id: environmental-exposure-assessment
title: Environmental Exposure Assessment
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: environmental-epidemiology-assessment
  type: hard
- id: measurement-error-epidemiology
  type: hard
- id: information-bias-epidemiology
  type: soft
tags:
- exposure-measurement
- biomarkers
- environmental-health
stage: advanced
status: draft
---

# Environmental Exposure Assessment

## Core Idea
Environmental epidemiology requires accurate characterization of exposure to chemicals, air pollutants, radiation, and other hazards—a major challenge given limited measurement resources. Approaches include biomarkers reflecting internal dose (urine, blood, tissues), environmental monitoring for external exposure, and occupational/residential history as proxy measures. Exposure error is typically non-differential and biases risk estimates toward null; systematic exposure misclassification causes directional bias. Exposure validation substudies quantify misclassification, and exposure reconstruction estimates past exposure when baseline measures unavailable.

## Explainer

In environmental epidemiology, the exposure is often invisible — a chemical in drinking water, a mixture of air pollutants, ionizing radiation, or a pesticide applied decades ago. Unlike a drug trial where exposure is assigned and recorded precisely, environmental studies must reconstruct or estimate what people actually experienced. Your prerequisite work on measurement error and information bias frames the core challenge: any gap between the true exposure and the measured surrogate introduces error that distorts risk estimates. Understanding exposure assessment is really about understanding where that error comes from and what it does to your results.

The three main approaches operate at different distances from the biological target. **Biomarkers** measure the internal dose — the amount of a substance (or its metabolite) that actually reached the body's tissues, detectable in blood, urine, hair, or biopsy specimens. Urinary cotinine reflects tobacco smoke exposure; blood lead captures absorbed lead regardless of route; urinary arsenic metabolites reflect recent seafood and drinking-water arsenic together. Biomarkers are appealing because they integrate all exposure routes and reflect what actually entered the body. Their weaknesses are practical: they require biological specimens, they often reflect only recent exposure (half-lives vary enormously), and they can be confounded by metabolic differences between individuals. **Environmental monitoring** — air samplers, water testing, soil measurements — estimates external exposure in the subject's environment. It can cover longer time windows and multiple people but must assume individuals actually encountered the measured levels. **Proxy measures** — occupation, residence, questionnaire responses about product use — are the lowest-fidelity approach but often the only one feasible for historical exposures.

The consequences of measurement error depend critically on whether it is **differential** or **non-differential**. Non-differential misclassification means the exposure measurement error is unrelated to disease status — equally bad in cases and controls, or equally bad in the diseased and healthy. When this happens in a dichotomous exposure, the observed risk estimate is systematically biased toward the null (relative risk toward 1.0), making true associations appear smaller than they are. This has a disturbing implication: a study using crude proxy exposure measures that finds no association cannot distinguish "there is no effect" from "there is an effect that our exposure measurement was too crude to detect." Differential misclassification — where error differs by disease status, as when ill people recall their exposures differently than healthy controls (recall bias) — can bias in either direction, inflating or deflating associations unpredictably.

**Exposure validation substudies** are the remedy: a subsample of study participants receive gold-standard exposure assessment (e.g., biomarkers or intensive monitoring) alongside the main proxy measure. Comparing the two allows researchers to estimate the degree of misclassification and apply correction factors to the main analysis. **Exposure reconstruction** uses historical records, environmental fate models, or job-exposure matrices to estimate what past exposures were likely to have been — critical for diseases with long latency periods like cancer, where the relevant exposure may have occurred 20–30 years before diagnosis. Together, these methods transform the exposure axis from a crude "exposed / unexposed" dichotomy into a more refined estimate of dose, enabling stronger causal inference.
