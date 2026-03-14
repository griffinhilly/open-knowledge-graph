---
id: diagnostic-microbiology
title: Diagnostic Microbiology
domain: biology
course: microbiology
prerequisites:
- id: bacterial-growth-and-reproduction
  type: hard
- id: pcr
  type: hard
- id: gel-electrophoresis
  type: soft
- id: adaptive-immune-response
  type: soft
- id: biofilm-formation
  type: soft
- id: sterilization-and-disinfection
  type: soft
tags:
- culture
- serology
- PCR diagnostics
- sensitivity
- specificity
- MALDI-TOF
- clinical microbiology
- rapid antigen test
stage: formal-systems
status: validated
---
# Diagnostic Microbiology

## Core Idea
Diagnostic microbiology identifies infectious agents through culture-based, molecular, and immunological methods. Bacterial culture on selective and differential media remains the gold standard for many infections; colonies are identified by morphology, biochemical tests, and increasingly by MALDI-TOF mass spectrometry, which provides species identification in minutes from a single colony. Molecular methods including PCR and next-generation sequencing provide rapid, sensitive detection of slow-growing or unculturable organisms, with multiplex panels simultaneously screening for dozens of pathogens. Serological methods detect patient antibodies (IgM indicates recent infection; IgG indicates past infection or vaccination) or microbial antigens directly. Sensitivity (true positive rate) and specificity (true negative rate) are the key performance metrics, with positive and negative predictive values varying with disease prevalence.

## How It's Best Learned
Work through the diagnostic algorithm for pneumonia: specimen collection (sputum, BAL) → Gram stain for preliminary identification → culture on blood and chocolate agar → susceptibility testing. Then calculate positive and negative predictive values for a rapid antigen test at 1% vs. 20% disease prevalence to make the Bayesian logic of diagnostic interpretation concrete.

## Common Misconceptions
- A negative culture does not rule out infection — some pathogens require special media, extended incubation, or molecular methods for detection.
- Antibody-based tests cannot detect active infections during the serological window (first 1–2 weeks post-infection before seroconversion).
- Sensitivity and specificity are fixed properties of a test; positive and negative predictive values are not — they change with population prevalence and must be recalculated for each clinical context.
