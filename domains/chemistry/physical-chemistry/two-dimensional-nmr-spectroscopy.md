---
id: two-dimensional-nmr-spectroscopy
title: Two-Dimensional NMR Techniques
domain: chemistry
course: physical-chemistry
prerequisites:
- id: nmr-spectroscopy-basics
  type: hard
- id: nmr-quantum-theory
  type: hard
builds-toward:
- chemical-exchange-kinetics-nmr
tags:
- nmr
- spectroscopy
- structure
- correlation
stage: advanced
status: draft
---

# Two-Dimensional NMR Techniques

## Core Idea
2D NMR experiments (COSY, HSQC, HMBC) correlate nuclear spins via scalar coupling or dipolar interactions, mapping which protons and carbons are connected by chemical bonds or spatial proximity. These correlation maps accelerate structural assignment, especially for complex organic molecules, by replacing one-dimensional guess-and-check with systematic 2D patterns.

## How It's Best Learned
Record COSY, HSQC, and HMBC spectra of a natural product or pharmaceutical compound; interpret cross-peak patterns to identify J-coupling pathways and long-range C-H correlations; compare 2D spectra to predicted connectivities from proposed structure.

## Common Misconceptions
- Assuming all COSY cross-peaks arise from ³J (three-bond) coupling; ⁴J and even ⁵J couplings appear, and long-range coupling is especially strong through unsaturation. - Treating HSQC and HMBC as simply proton-carbon maps; HSQC shows direct ¹J(C-H) only, while HMBC shows ²J and ³J(C-H).

## Explainer

From your study of one-dimensional NMR, you know that each nucleus in a molecule resonates at a characteristic chemical shift, and that scalar (J) coupling splits peaks into multiplets that reveal connectivity. But in a complex molecule with dozens of protons, 1D spectra become hopelessly crowded — overlapping multiplets make it impossible to determine which proton is coupled to which. **Two-dimensional NMR** solves this by spreading the information across two frequency axes, creating a correlation map where off-diagonal peaks (cross-peaks) directly reveal relationships between nuclei.

The simplest 2D experiment is **COSY** (Correlation Spectroscopy). Both axes represent proton chemical shifts, and the diagonal contains the same peaks as a 1D spectrum. The key information lives in the **cross-peaks**: a cross-peak at coordinates (δA, δB) means proton A and proton B are connected through scalar coupling, typically across two or three bonds. Walking along COSY cross-peaks, you can trace the connectivity of a spin system — for instance, following an alkyl chain from CH₃ to CH₂ to CH. This is far more powerful than trying to match coupling constants in a 1D spectrum, because you see the connectivity directly as a pattern rather than inferring it from numerical coincidences.

**HSQC** (Heteronuclear Single Quantum Coherence) and **HMBC** (Heteronuclear Multiple Bond Correlation) extend this logic to carbon-proton relationships. In HSQC, one axis is ¹H chemical shift and the other is ¹³C chemical shift, and each cross-peak identifies a directly bonded C-H pair (one-bond ¹J coupling). This immediately tells you which carbon each proton is attached to. HMBC shows longer-range correlations — two-bond and three-bond C-H connections — which are essential for piecing together the carbon skeleton, especially across quaternary carbons (which have no directly attached proton and are invisible in HSQC). Together, COSY traces proton spin systems, HSQC maps each proton to its carbon, and HMBC bridges across gaps in the proton network to connect spin systems through the carbon framework.

The practical workflow for structure determination using 2D NMR follows a systematic logic. First, use HSQC to assign each proton to its directly bonded carbon. Then use COSY to map out connected proton spin systems — contiguous chains of coupled protons. Finally, use HMBC to connect those spin systems across quaternary carbons, heteroatoms, or carbonyl groups where the proton chain is interrupted. For a natural product like strychnine or a pharmaceutical compound, this combination of three experiments can fully determine a structure that would be impossibly ambiguous from 1D data alone. The power of 2D NMR lies in converting structure elucidation from a puzzle of overlapping peaks into a systematic reading of correlation maps.
