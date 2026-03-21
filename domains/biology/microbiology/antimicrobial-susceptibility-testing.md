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

## Questions

```yaml
- question: "In a Kirby-Bauer disk diffusion assay, antibiotic A produces a zone of inhibition of 28mm and antibiotic B produces a zone of 12mm against the same bacterial isolate. What does the size of these zones indicate about bacterial susceptibility?"
  type: multiple-choice
  options:
    - "The bacterium is more resistant to antibiotic A because it needed a larger zone to be inhibited"
    - "The bacterium is more susceptible to antibiotic A, since a larger zone corresponds to a lower MIC against that drug"
    - "Antibiotic B is more clinically useful because its inhibition was concentrated closer to the disk"
    - "Zone size indicates drug concentration in the disk, not bacterial susceptibility"
  answer: 1
  explanation: "Zone diameter is inversely correlated with MIC. A larger zone means the bacterium was inhibited at a greater distance from the disk, meaning even the low drug concentrations far from the disk exceeded the MIC — indicating susceptibility. A small zone (antibiotic B here) means bacteria grew right up to the disk even at high local concentrations, indicating resistance. Option A is the classic reversal misconception."

- question: "Why is the MIC compared against published breakpoints rather than used as a direct, absolute measure of susceptibility?"
  type: multiple-choice
  options:
    - "Because MIC values drift over time as bacteria adapt to antibiotics during storage in culture"
    - "Because the clinically relevant question is whether the MIC is achievable at the infection site with safe dosing — which breakpoints encode by incorporating pharmacokinetic data"
    - "Because MIC measurement has too much technical variability to be interpreted without a correction factor"
    - "Because breakpoints standardize for differences in bacterial inoculum size across different laboratories"
  answer: 1
  explanation: "An MIC of 0.25 μg/mL means nothing clinically without knowing: can we safely achieve that concentration at a urinary tract infection versus a brain abscess at standard dosing? Breakpoints encode this pharmacokinetic context — they are set based on what drug concentrations are achievable in relevant body compartments at safe doses. A breakpoint defines the threshold above which standard therapy is unlikely to succeed, translating a lab number into a treatment decision."

- question: "A bacterial isolate with a large zone of inhibition on a Kirby-Bauer plate is resistant to that antibiotic."
  type: true-false
  answer: false
  explanation: "The opposite is true. A large zone means the bacterium was inhibited at a great distance from the disk, corresponding to a low MIC — the organism is susceptible. Resistance is indicated by a small or absent zone, meaning bacteria grew right up to the disk even at high local concentrations. This is the single most common Kirby-Bauer interpretation error."

- question: "Broth microdilution is considered the gold standard for MIC determination because it produces a precise numerical concentration value that can be directly compared to breakpoints."
  type: true-false
  answer: true
  explanation: "Broth microdilution uses serial two-fold dilutions of antibiotic in a 96-well plate, each inoculated with standardized bacteria. The first clear well after incubation defines the MIC as a specific value in μg/mL (e.g., 0.25 μg/mL), which can be directly compared to published breakpoints. Kirby-Bauer gives zone diameters that must be converted to S/I/R categories via interpretive charts — an extra translation step with additional imprecision."

- question: "What is a hospital antibiogram, and why is it clinically valuable before an individual patient's susceptibility results are available?"
  type: short-answer
  answer: "An antibiogram is a cumulative resistance profile for common pathogens at a specific institution, compiled from many AST results over time. It reports what percentage of each pathogen species is susceptible to each antibiotic locally. Before a patient's culture results return (typically 16–48 hours), clinicians must choose empiric therapy based on the most likely pathogen and its local resistance patterns. The antibiogram provides this local resistance landscape, enabling evidence-based empiric choices rather than relying on national statistics that may not reflect what is circulating at that hospital."
  explanation: "Local resistance patterns can differ dramatically from regional or national data. A hospital with heavy carbapenem use may have much higher carbapenem resistance rates than the national average. The antibiogram captures this local ecology and makes it actionable for empiric treatment decisions."
```

## Explainer

From your study of antibiotic resistance mechanisms, you know that bacteria can acquire resistance through mutations, plasmid transfer, and mobile genetic elements — and that different resistance genes neutralize antibiotics through different biochemical strategies (efflux pumps, enzymatic degradation, target modification). **Antimicrobial susceptibility testing (AST)** is how clinicians determine which of those resistance mechanisms are actually present in a patient's infection, translating molecular biology into treatment decisions. Without AST, prescribing antibiotics is essentially guesswork, and incorrect guesses both harm the patient and accelerate resistance evolution.

The conceptual foundation of all AST methods is the **minimum inhibitory concentration (MIC)** — the lowest concentration of an antibiotic that prevents visible bacterial growth after overnight incubation. The gold standard for measuring MIC is **broth microdilution**: serial two-fold dilutions of the antibiotic are prepared in a 96-well plate, each well is inoculated with a standardized number of bacteria, and after incubation, the first clear well (no turbidity) indicates the MIC. This gives a precise numerical value — for example, "the MIC of ciprofloxacin against this *E. coli* isolate is 0.25 μg/mL." That number is then compared to established **breakpoints** set by organizations like CLSI or EUCAST, which define concentration thresholds for categorizing the isolate as susceptible, intermediate, or resistant.

The most widely used method in clinical laboratories is the **Kirby-Bauer disk diffusion assay**, which is simpler and cheaper than broth microdilution. A standardized bacterial inoculum is spread across a Mueller-Hinton agar plate, and paper disks impregnated with known concentrations of different antibiotics are placed on the surface. As the antibiotic diffuses outward from each disk, it creates a concentration gradient — high near the disk, decreasing with distance. After incubation, a clear **zone of inhibition** surrounds each disk where the antibiotic concentration exceeded the MIC. The diameter of this zone correlates inversely with the MIC: a large zone means the bacterium is highly susceptible, a small zone or no zone indicates resistance. Published interpretive charts convert zone diameters into the same susceptible/intermediate/resistant categories.

Modern clinical microbiology laboratories increasingly use **automated systems** (VITEK, MicroScan, Phoenix) that combine identification and susceptibility testing in a single instrument. These systems inoculate panels of antibiotics at defined concentrations, monitor growth photometrically or fluorimetrically over hours rather than overnight, and report results with algorithmic interpretation. The speed advantage is significant — results in 6–8 hours versus 16–24 for manual methods — which matters enormously for critically ill patients with bloodstream infections. Regardless of the method used, AST results feed into hospital **antibiograms**: cumulative resistance profiles for common pathogens at a given institution, which guide empiric therapy choices before patient-specific results are available and reveal emerging resistance trends that demand public health intervention.
