---
id: antimicrobial-susceptibility-testing
title: Antimicrobial Susceptibility Testing and Resistance Profiling
domain: biology
course: microbiology
prerequisites:
- id: antibiotic-resistance-genetic-mechanisms
  type: hard
- id: sterilization-and-disinfection
  type: soft
builds-toward:
- emerging-infectious-diseases
tags:
- susceptibility
- testing
- resistance
stage: advanced
status: draft
---

# Antimicrobial Susceptibility Testing and Resistance Profiling

## Core Idea
Antimicrobial susceptibility testing (AST) determines the minimum inhibitory concentration (MIC) of drugs against bacterial isolates using agar diffusion (Kirby-Bauer), broth microdilution, or automated systems. Results guide clinical treatment and surveillance. Resistance patterns inform epidemiology and public health responses.

## Explainer

From your study of antibiotic resistance mechanisms, you know that bacteria can acquire resistance through mutations, plasmid transfer, and mobile genetic elements — and that different resistance genes neutralize antibiotics through different biochemical strategies (efflux pumps, enzymatic degradation, target modification). **Antimicrobial susceptibility testing (AST)** is how clinicians determine which of those resistance mechanisms are actually present in a patient's infection, translating molecular biology into treatment decisions. Without AST, prescribing antibiotics is essentially guesswork, and incorrect guesses both harm the patient and accelerate resistance evolution.

The conceptual foundation of all AST methods is the **minimum inhibitory concentration (MIC)** — the lowest concentration of an antibiotic that prevents visible bacterial growth after overnight incubation. The gold standard for measuring MIC is **broth microdilution**: serial two-fold dilutions of the antibiotic are prepared in a 96-well plate, each well is inoculated with a standardized number of bacteria, and after incubation, the first clear well (no turbidity) indicates the MIC. This gives a precise numerical value — for example, "the MIC of ciprofloxacin against this *E. coli* isolate is 0.25 μg/mL." That number is then compared to established **breakpoints** set by organizations like CLSI or EUCAST, which define concentration thresholds for categorizing the isolate as susceptible, intermediate, or resistant.

The most widely used method in clinical laboratories is the **Kirby-Bauer disk diffusion assay**, which is simpler and cheaper than broth microdilution. A standardized bacterial inoculum is spread across a Mueller-Hinton agar plate, and paper disks impregnated with known concentrations of different antibiotics are placed on the surface. As the antibiotic diffuses outward from each disk, it creates a concentration gradient — high near the disk, decreasing with distance. After incubation, a clear **zone of inhibition** surrounds each disk where the antibiotic concentration exceeded the MIC. The diameter of this zone correlates inversely with the MIC: a large zone means the bacterium is highly susceptible, a small zone or no zone indicates resistance. Published interpretive charts convert zone diameters into the same susceptible/intermediate/resistant categories.

Modern clinical microbiology laboratories increasingly use **automated systems** (VITEK, MicroScan, Phoenix) that combine identification and susceptibility testing in a single instrument. These systems inoculate panels of antibiotics at defined concentrations, monitor growth photometrically or fluorimetrically over hours rather than overnight, and report results with algorithmic interpretation. The speed advantage is significant — results in 6–8 hours versus 16–24 for manual methods — which matters enormously for critically ill patients with bloodstream infections. Regardless of the method used, AST results feed into hospital **antibiograms**: cumulative resistance profiles for common pathogens at a given institution, which guide empiric therapy choices before patient-specific results are available and reveal emerging resistance trends that demand public health intervention.
