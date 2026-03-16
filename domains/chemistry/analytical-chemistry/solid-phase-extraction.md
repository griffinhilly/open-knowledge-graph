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

## Explainer

From your work with sample preparation, you know that real-world samples — river water, blood plasma, soil extracts — are complex mixtures where the analyte of interest is buried among thousands of interfering compounds. You also know from chromatography fundamentals that different molecules interact differently with stationary phases based on their polarity, charge, or size. **Solid-phase extraction (SPE)** takes that chromatographic principle and applies it in a simplified, batch-mode format: instead of separating everything, you selectively grab your analyte onto a sorbent, wash away the junk, and then release the analyte in a clean, concentrated form.

The procedure follows four steps, and understanding why each one matters is more important than memorizing the sequence. First, you **condition** the sorbent — typically by passing methanol followed by water through a C18 cartridge. This wets the hydrophobic chains so they can interact with analytes; skip this step and the sorbent stays dry, analytes flow straight through, and your recovery drops to near zero. Second, you **load** the sample. As the liquid passes through the bed, analytes with affinity for the sorbent are retained while most of the matrix passes through. Third, you **wash** with a solvent that is strong enough to remove weakly held interferences but too weak to dislodge your analyte. Finally, you **elute** with a strong solvent — often pure methanol or acetonitrile — that breaks the analyte-sorbent interaction and delivers a small, concentrated volume ready for analysis.

The choice of sorbent chemistry follows the same "like dissolves like" logic you learned in chromatography. **Reversed-phase C18** sorbents retain nonpolar analytes from aqueous samples — pesticides from water, drugs from urine. **Ion-exchange** sorbents retain charged analytes — acidic or basic drugs — by electrostatic attraction, and you release them by changing pH or ionic strength. **Mixed-mode** sorbents combine both mechanisms, giving you two orthogonal handles for selectivity. The decision tree is straightforward: identify your analyte's dominant chemical character, then pick the sorbent that grabs it while ignoring the matrix.

What makes SPE so powerful compared to older liquid-liquid extraction is practical: it uses milliliters of solvent instead of hundreds of milliliters, it handles emulsion-prone samples cleanly, and it can be automated on robotic platforms that process 96 samples in parallel. In regulatory environmental and clinical laboratories, SPE is now the default front-end to HPLC and LC-MS analyses. The conceptual takeaway is that SPE is not a black box — it is chromatographic retention applied strategically, where your method development choices (sorbent type, wash strength, elution solvent) all trace back to the same intermolecular interaction principles that govern column chromatography.
