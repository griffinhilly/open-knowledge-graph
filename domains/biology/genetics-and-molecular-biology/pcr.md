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
status: validated
---

# Polymerase Chain Reaction (PCR)

## Core Idea
The polymerase chain reaction (PCR) amplifies a specific DNA sequence exponentially using repeated cycles of denaturation, primer annealing, and extension. Short synthetic oligonucleotide primers flanking the target region define what is amplified; thermostable Taq polymerase (from Thermus aquaticus) extends primers at 72°C. After n cycles, the target sequence is amplified approximately 2ⁿ fold, enabling detection of minute quantities of DNA. PCR is foundational in molecular diagnostics, forensics, sequencing, and cloning, and variants such as quantitative PCR (qPCR) and RT-PCR (using reverse-transcribed cDNA) extend its applications.

## How It's Best Learned
Walk through a three-cycle PCR diagram showing how the discrete target-length product accumulates. Design primers for a hypothetical gene (selecting appropriate Tm, avoiding secondary structures) and describe the expected thermocycle.

## Common Misconceptions
- PCR does not require the full genome as template; even a single DNA molecule can be sufficient with enough cycles.
- Taq polymerase lacks 3' proofreading exonuclease activity, so PCR introduces errors; higher-fidelity polymerases are used when accuracy is critical.

## Explainer

From your study of DNA replication, you know the essential ingredients: a template strand, a primer with a free 3'-OH, nucleotide triphosphates, and a DNA polymerase. **PCR** takes these same ingredients and runs replication in a test tube — but with a clever twist that turns a single copy of a DNA sequence into billions of copies in just a few hours.

The trick is **thermal cycling**. A PCR reaction alternates between three temperatures. First, **denaturation** at ~95°C melts the double-stranded DNA into single strands by breaking hydrogen bonds. Second, **annealing** at ~55-65°C allows short synthetic DNA primers (typically 18-25 nucleotides) to bind to complementary sequences flanking your target region. You add two primers — one for each strand — pointing inward toward each other. Third, **extension** at 72°C lets DNA polymerase synthesize new strands starting from each primer. The key innovation that made PCR practical was using **Taq polymerase**, isolated from the thermophilic bacterium *Thermus aquaticus*, which survives the 95°C denaturation step that would destroy ordinary polymerases. Before Taq, researchers had to add fresh enzyme after every cycle.

Each cycle doubles the target sequence, so amplification is exponential: after *n* cycles, you have approximately **2ⁿ copies**. Thirty cycles produce roughly a billion-fold amplification (2³⁰ ≈ 10⁹). But there is a subtlety worth understanding. In the first few cycles, the polymerase extends past the target region because there's no defined endpoint — the products are variable-length strands. Starting at cycle 3, however, products bounded by both primers begin to appear, and these defined-length fragments accumulate exponentially while the longer products only increase linearly. By cycle 5-6, the short target-length products vastly outnumber everything else.

PCR's power lies in its specificity and sensitivity — the primers determine exactly which sequence gets amplified, and the exponential amplification means you can start from vanishingly small amounts of DNA. A single molecule of template is theoretically sufficient. This is why PCR revolutionized forensics (amplifying DNA from a hair follicle or blood drop), medical diagnostics (detecting viral DNA in patient samples), ancient DNA research (recovering sequences from fossils), and molecular cloning (generating defined DNA fragments for insertion into vectors). Variants like **RT-PCR** (which first reverse-transcribes RNA into cDNA) let you measure gene expression, while **quantitative PCR (qPCR)** uses fluorescent reporters to measure amplification in real time, converting PCR from a qualitative yes/no tool into a precise quantitative assay.
