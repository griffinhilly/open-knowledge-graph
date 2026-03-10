---
id: pcr
title: Polymerase Chain Reaction (PCR)
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: dna-replication
  type: hard
- id: restriction-enzymes
  type: soft
- id: gel-electrophoresis
  type: soft
- id: chemical-kinetics
  type: soft
builds-toward:
- recombinant-dna-technology
- genomics-overview
tags:
- PCR
- Taq polymerase
- primers
- thermocycler
- DNA amplification
stage: formal-systems
status: draft
---

# Polymerase Chain Reaction (PCR)

## Core Idea
The polymerase chain reaction (PCR) amplifies a specific DNA sequence exponentially using repeated cycles of denaturation, primer annealing, and extension. Short synthetic oligonucleotide primers flanking the target region define what is amplified; thermostable Taq polymerase (from Thermus aquaticus) extends primers at 72°C. After n cycles, the target sequence is amplified approximately 2ⁿ fold, enabling detection of minute quantities of DNA. PCR is foundational in molecular diagnostics, forensics, sequencing, and cloning, and variants such as quantitative PCR (qPCR) and RT-PCR (using reverse-transcribed cDNA) extend its applications.

## How It's Best Learned
Walk through a three-cycle PCR diagram showing how the discrete target-length product accumulates. Design primers for a hypothetical gene (selecting appropriate Tm, avoiding secondary structures) and describe the expected thermocycle.

## Common Misconceptions
- PCR does not require the full genome as template; even a single DNA molecule can be sufficient with enough cycles.
- Taq polymerase lacks 3' proofreading exonuclease activity, so PCR introduces errors; higher-fidelity polymerases are used when accuracy is critical.
