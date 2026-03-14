---
id: quorum-sensing
title: Quorum Sensing
domain: biology
course: microbiology
prerequisites:
- id: bacterial-cell-structure
  type: hard
- id: cell-signaling-intro
  type: hard
- id: gene-regulation-prokaryotes
  type: soft
builds-toward:
- biofilm-formation
- host-pathogen-interactions
tags:
- quorum sensing
- autoinducer
- AHL
- AI-2
- density-dependent
- bioluminescence
stage: formal-systems
status: validated
---
# Quorum Sensing

## Core Idea
Quorum sensing (QS) is a population density-dependent signaling system in which bacteria produce small chemical signals called autoinducers that accumulate extracellularly. Once autoinducer concentration crosses a threshold, bacteria collectively alter gene expression to coordinate behaviors only effective at high density — biofilm formation, virulence factor production, sporulation, and bioluminescence. Gram-negative bacteria typically use N-acylhomoserine lactones (AHLs); Gram-positive bacteria use modified peptides; AI-2 enables cross-species communication. Quorum quenching — disrupting QS — is a promising anti-virulence strategy that reduces pathogenicity without bactericidal pressure and therefore without driving classical resistance.

## How It's Best Learned
The Vibrio fischeri LuxI/LuxR system is the canonical model — trace how light production is off at low density and on at high density, then generalize to pathogenic QS circuits. Pseudomonas aeruginosa uses multiple overlapping QS systems (las, rhl, pqs) to regulate biofilm and virulence in cystic fibrosis lungs, making it an ideal complex case study.

## Common Misconceptions
- Quorum sensing is not bacterial cognition — it is a chemical threshold-detection mechanism with no decision-making or awareness involved.
- AI-2 is not a single molecule; it is a class of related furanosyl borate diesters.
- Quorum quenching does not kill bacteria, which is both its advantage (less resistance pressure) and a limitation for therapeutic sterilization goals.
