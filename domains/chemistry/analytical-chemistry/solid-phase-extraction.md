---
id: solid-phase-extraction
title: Solid-Phase Extraction
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: sample-preparation
  type: hard
- id: chromatography-fundamentals
  type: soft
tags:
- SPE
- sorbent
- C18
- cleanup
- preconcentration
- cartridge
- conditioning
- elution
stage: formal-systems
status: draft
---

# Solid-Phase Extraction

## Core Idea
Solid-phase extraction (SPE) uses a sorbent-packed cartridge or disk to selectively retain the analyte (or the interferences) from a liquid sample, enabling cleanup and preconcentration in a single step. The procedure follows four stages: conditioning the sorbent to activate it, loading the sample so analytes adsorb, washing to remove interferences, and eluting the analyte with a strong solvent for analysis. Sorbent chemistry (reversed-phase C18, ion-exchange, mixed-mode, immunoaffinity) is chosen to match the analyte's properties, and the method essentially applies chromatographic retention principles in a batch format. SPE largely replaced liquid-liquid extraction in modern environmental and pharmaceutical laboratories because it uses less solvent, is more easily automated, and handles emulsion-prone samples without difficulty.

## How It's Best Learned
Process a spiked water sample through a C18 SPE cartridge to isolate a pesticide or pharmaceutical, then elute and analyze by HPLC. Run a parallel extraction skipping the conditioning step to observe failed retention, which demonstrates why proper sorbent activation is not optional.

## Common Misconceptions
- SPE is not simply 'small-scale chromatography'; the goal is quantitative retention and recovery of the analyte, not separation of multiple species, so the method development logic differs from chromatographic method development.
- Skipping or rushing the conditioning step is the most common cause of poor SPE recovery — the sorbent must be fully wetted and activated before the sample is loaded.
