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
stage: advanced
status: validated
---

# Solid-Phase Extraction

## Core Idea
Solid-phase extraction (SPE) uses a sorbent-packed cartridge or disk to selectively retain the analyte (or the interferences) from a liquid sample, enabling cleanup and preconcentration in a single step. The procedure follows four stages: conditioning the sorbent to activate it, loading the sample so analytes adsorb, washing to remove interferences, and eluting the analyte with a strong solvent for analysis. Sorbent chemistry (reversed-phase C18, ion-exchange, mixed-mode, immunoaffinity) is chosen to match the analyte's properties, and the method essentially applies chromatographic retention principles in a batch format. SPE largely replaced liquid-liquid extraction in modern environmental and pharmaceutical laboratories because it uses less solvent, is more easily automated, and handles emulsion-prone samples without difficulty.

## How It's Best Learned
Process a spiked water sample through a C18 SPE cartridge to isolate a pesticide or pharmaceutical, then elute and analyze by HPLC. Run a parallel extraction skipping the conditioning step to observe failed retention, which demonstrates why proper sorbent activation is not optional.

## Common Misconceptions
- SPE is not simply 'small-scale chromatography'; the goal is quantitative retention and recovery of the analyte, not separation of multiple species, so the method development logic differs from chromatographic method development.
- Skipping or rushing the conditioning step is the most common cause of poor SPE recovery — the sorbent must be fully wetted and activated before the sample is loaded.

## Questions

```yaml
- question: "A technician loads a water sample onto a C18 SPE cartridge without first conditioning it. What most likely happens to the target pesticide?"
  type: multiple-choice
  options:
    - "The pesticide is retained but co-elutes with interferences during the wash step"
    - "The pesticide passes through the cartridge without being retained"
    - "The pesticide is permanently bound to the dry sorbent and cannot be eluted"
    - "The conditioning step only matters for ion-exchange sorbents, so recovery is unaffected"
  answer: 1
  explanation: "The conditioning step wets the C18 hydrophobic chains with methanol then equilibrates them with water. Without this activation, the dry sorbent cannot establish the hydrophobic interactions needed to retain nonpolar analytes — the sample flows straight through as if the sorbent bed weren't there, and recovery drops to near zero. This is the single most common cause of failed SPE in practice. The chains must be in their extended, solvated configuration to interact with the analyte."

- question: "How does the fundamental goal of solid-phase extraction differ from the goal of column chromatography, even though both use a sorbent and a liquid phase?"
  type: multiple-choice
  options:
    - "SPE uses synthetic sorbents while chromatography uses naturally occurring mineral phases"
    - "SPE aims for quantitative retention and recovery of one analyte; chromatography aims to separate multiple analytes from each other"
    - "Chromatography can preconcentrate analytes while SPE only removes interferences"
    - "SPE requires a gradient elution while chromatography uses an isocratic mobile phase"
  answer: 1
  explanation: "This distinction changes the entire method development logic. In chromatography, you want analytes to move at different rates so they separate from each other. In SPE, you want one analyte (or class) to be completely retained while everything else passes through, then released cleanly with a strong solvent. You are not trying to resolve peaks — you are trying to maximize retention and recovery. The wash step exploits this difference: you need a wash that removes interferences without displacing your analyte, a judgment that has no direct analogue in chromatographic method development."

- question: "In reversed-phase SPE, the analyte is retained on the sorbent while most of the aqueous sample matrix passes through during the loading step."
  type: true-false
  answer: true
  explanation: "This is the core mechanism of reversed-phase SPE. C18 sorbents are hydrophobic; when an aqueous sample is loaded, nonpolar analytes preferentially interact with the hydrophobic chains and are retained, while polar and ionic matrix components (salts, proteins, sugars) have little affinity for the sorbent and wash through. The elution step later uses an organic solvent (methanol, acetonitrile) to break the hydrophobic interaction and release the analyte in a small, concentrated volume."

- question: "Because SPE applies the same intermolecular interaction principles as chromatography, the method development approach for SPE is essentially the same as for developing an HPLC separation."
  type: true-false
  answer: false
  explanation: "The intermolecular principles are shared, but the development goals diverge. HPLC method development focuses on resolving multiple analytes from each other by tuning their relative retention. SPE development focuses on maximizing the retention of one target analyte while finding wash conditions that selectively strip interferences. You are optimizing for *quantitative capture and release*, not *relative migration rates*. The practical consequence is that SPE method development starts from 'will this sorbent grab my analyte at all?' rather than 'will these two analytes separate?'"

- question: "Why is the conditioning step in solid-phase extraction not optional, and what specifically fails when it is skipped?"
  type: short-answer
  answer: "Conditioning wets and activates the sorbent so it can interact with analytes. For a C18 sorbent, methanol solvates the hydrophobic chains and extends them, then water equilibrates the bed to match the aqueous sample. Without this, the dry chains cannot establish hydrophobic interactions, and the analyte passes through unretained. Recovery drops to near zero not because the sorbent is 'deactivated' but because the physical and chemical environment needed for retention simply hasn't been established."
  explanation: "A useful analogy: conditioning is like warming up a glue surface. A dry, unconditioned C18 bed is like glue that hasn't been prepared — the analyte can't adhere. The step is easy to skip under time pressure, and the failure mode looks deceptively like a method problem (poor recovery) rather than a procedural one. Running a parallel extraction without conditioning, as described in the learning suggestion, immediately demonstrates this — the sample eluate contains the analyte that should have been retained."
```

## Explainer

From your work with sample preparation, you know that real-world samples — river water, blood plasma, soil extracts — are complex mixtures where the analyte of interest is buried among thousands of interfering compounds. You also know from chromatography fundamentals that different molecules interact differently with stationary phases based on their polarity, charge, or size. **Solid-phase extraction (SPE)** takes that chromatographic principle and applies it in a simplified, batch-mode format: instead of separating everything, you selectively grab your analyte onto a sorbent, wash away the junk, and then release the analyte in a clean, concentrated form.

The procedure follows four steps, and understanding why each one matters is more important than memorizing the sequence. First, you **condition** the sorbent — typically by passing methanol followed by water through a C18 cartridge. This wets the hydrophobic chains so they can interact with analytes; skip this step and the sorbent stays dry, analytes flow straight through, and your recovery drops to near zero. Second, you **load** the sample. As the liquid passes through the bed, analytes with affinity for the sorbent are retained while most of the matrix passes through. Third, you **wash** with a solvent that is strong enough to remove weakly held interferences but too weak to dislodge your analyte. Finally, you **elute** with a strong solvent — often pure methanol or acetonitrile — that breaks the analyte-sorbent interaction and delivers a small, concentrated volume ready for analysis.

The choice of sorbent chemistry follows the same "like dissolves like" logic you learned in chromatography. **Reversed-phase C18** sorbents retain nonpolar analytes from aqueous samples — pesticides from water, drugs from urine. **Ion-exchange** sorbents retain charged analytes — acidic or basic drugs — by electrostatic attraction, and you release them by changing pH or ionic strength. **Mixed-mode** sorbents combine both mechanisms, giving you two orthogonal handles for selectivity. The decision tree is straightforward: identify your analyte's dominant chemical character, then pick the sorbent that grabs it while ignoring the matrix.

What makes SPE so powerful compared to older liquid-liquid extraction is practical: it uses milliliters of solvent instead of hundreds of milliliters, it handles emulsion-prone samples cleanly, and it can be automated on robotic platforms that process 96 samples in parallel. In regulatory environmental and clinical laboratories, SPE is now the default front-end to HPLC and LC-MS analyses. The conceptual takeaway is that SPE is not a black box — it is chromatographic retention applied strategically, where your method development choices (sorbent type, wash strength, elution solvent) all trace back to the same intermolecular interaction principles that govern column chromatography.
