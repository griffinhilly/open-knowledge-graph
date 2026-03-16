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

## Explainer

You already understand how bacteria grow and reproduce in culture, how PCR amplifies specific DNA sequences, and the basics of the adaptive immune response (including antibody production). Diagnostic microbiology is where all of these concepts converge into a practical question: a patient is sick — what is causing the infection, and how do we find out?

The oldest and still most informative method is **culture**. A clinical specimen (blood, urine, sputum, wound swab) is inoculated onto agar plates and incubated, typically at 35–37°C for 18–24 hours. Different media serve different purposes. **Blood agar** is a general-purpose medium that supports most bacteria and reveals hemolysis patterns (alpha, beta, gamma) that help narrow identification. **MacConkey agar** is both selective (bile salts and crystal violet inhibit Gram-positive organisms) and differential (lactose fermenters produce pink colonies; non-fermenters stay colorless). A Gram stain of the original specimen provides the first rapid clue — within minutes you know the morphology (cocci vs. rods) and Gram reaction, which immediately narrows the differential diagnosis from hundreds of organisms to a manageable few. Once colonies grow, **MALDI-TOF mass spectrometry** can identify the species in minutes by generating a protein "fingerprint" from a single colony — a technology that has revolutionized clinical microbiology by replacing hours of biochemical testing with a single automated measurement.

**Molecular methods** fill the gaps where culture fails. Some organisms grow too slowly (*Mycobacterium tuberculosis* takes weeks), some cannot be cultured at all (*Treponema pallidum*), and some require rapid identification to guide emergency treatment. **PCR** detects pathogen DNA or RNA with high sensitivity, often from specimens that would yield negative cultures. Multiplex PCR panels can simultaneously test for 20+ respiratory or gastrointestinal pathogens from a single swab, returning results in one to two hours. The tradeoff is that PCR detects nucleic acid regardless of viability — a positive result may reflect dead organisms from a resolved infection rather than active disease, and molecular tests typically do not provide antimicrobial susceptibility data.

**Serological methods** detect the host's immune response to infection rather than the pathogen itself. Measuring antibody levels can confirm diagnosis when direct detection is difficult — for example, detecting IgM against hepatitis A virus confirms acute infection. The critical limitation is the **serological window**: after initial infection, it takes one to two weeks for the adaptive immune response to generate detectable antibodies, during which time serological tests will be falsely negative. Rapid **antigen tests** (like the lateral flow assays used for strep throat or COVID-19) detect microbial antigens directly in specimens and provide results in minutes, but they sacrifice sensitivity for speed. A negative rapid antigen test in a clinically suspicious case should be followed up with culture or PCR. Understanding the performance metrics — **sensitivity** (proportion of true positives correctly identified) and **specificity** (proportion of true negatives correctly identified) — is essential, but the clinically actionable numbers are the **predictive values**, which depend on disease prevalence. A test with 95% sensitivity and 95% specificity has a positive predictive value of only 16% when prevalence is 1%, but 86% when prevalence is 25%. This Bayesian reasoning is what separates effective diagnostic interpretation from naive test ordering.
