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

## Questions

```yaml
- question: "A molecule contains a quaternary carbon (no directly attached protons) that connects two proton-containing fragments. Which 2D NMR experiment is essential for detecting this carbon and establishing its connectivity?"
  type: multiple-choice
  options:
    - "COSY — it reveals all proton-proton coupling pathways including those bridged by quaternary carbons"
    - "HSQC — it maps every carbon to its directly bonded protons, including quaternary carbons"
    - "HMBC — it shows 2–3 bond C-H correlations, bridging across carbons with no attached protons"
    - "Neither — quaternary carbons are undetectable in any routine 2D NMR experiment"
  answer: 2
  explanation: "Quaternary carbons are silent in HSQC because HSQC requires a directly bonded H (¹J coupling). They also break the COSY proton chain because COSY only shows H-H coupling, and the chain is interrupted at a carbon with no protons. HMBC is specifically designed for long-range C-H correlations (2–3 bonds), so nearby protons show cross-peaks to the quaternary carbon even though they are not directly attached. This is why HMBC is indispensable for connecting spin systems in complex molecules."

- question: "In a COSY spectrum, you observe cross-peaks between proton A (δ 3.5 ppm) and proton B (δ 1.2 ppm), and between proton B and proton C (δ 0.9 ppm), but no cross-peak between A and C. What is the most reasonable structural interpretation?"
  type: multiple-choice
  options:
    - "A, B, and C are all on the same carbon, producing equivalent-proton couplings"
    - "A–B and B–C are on adjacent carbons respectively; A and C are likely separated by more than 3 bonds"
    - "The absence of an A–C cross-peak means they are on opposite ends of a large ring"
    - "B is a heteroatom bridging the A and C fragments"
  answer: 1
  explanation: "COSY cross-peaks typically arise from 3-bond (vicinal) H-H coupling. A cross-peak between A and B means they are on adjacent carbons. A cross-peak between B and C means B and C are on adjacent carbons. The absence of an A-C cross-peak is consistent with them being four or more bonds apart (e.g., A–CH–CH–C where B is in the middle). This is the logic of 'walking the chain' in COSY: each cross-peak traces one step along the carbon backbone."

- question: "HMBC cross-peaks between a proton and a carbon separated by two or three bonds are essential for connecting proton spin systems across quaternary carbons and heteroatoms."
  type: true-false
  answer: true
  explanation: "When the proton connectivity chain is interrupted — by a carbonyl carbon, a quaternary carbon, nitrogen, or oxygen — COSY cannot trace across the gap because there are no protons to couple through. HMBC fills this gap by detecting longer-range C-H correlations. A proton two or three bonds from an 'invisible' quaternary carbon shows up as a cross-peak to that carbon in HMBC, revealing the connection. Without HMBC, the carbon skeleton of complex natural products and pharmaceuticals would be impossible to assemble from NMR data alone."

- question: "Because HSQC and HMBC both display correlations between ¹H and ¹³C chemical shifts, they are interchangeable for assigning which proton is attached to which carbon."
  type: true-false
  answer: false
  explanation: "HSQC and HMBC are complementary, not interchangeable. HSQC shows only one-bond (¹J) C-H correlations — each cross-peak identifies a directly attached H-C pair. HMBC shows two- and three-bond correlations — each cross-peak identifies a proton near (but not directly attached to) a carbon. Using HMBC to assign direct attachments would give completely wrong answers because long-range correlations reach multiple carbons. The two experiments answer different questions: HSQC tells you 'which carbon does this proton sit on?' and HMBC tells you 'which carbons is this proton close to in the bonding network?'"

- question: "Describe the systematic workflow for using COSY, HSQC, and HMBC together for structure determination. What structural question does each experiment answer, and what gap would be left if one were missing?"
  type: short-answer
  answer: "HSQC assigns each proton to its directly bonded carbon, creating a proton-carbon inventory. COSY then traces connected proton spin systems (contiguous chains of coupled protons), mapping the carbon backbone wherever protons are present. HMBC bridges the gaps where the chain is interrupted by quaternary carbons, carbonyls, or heteroatoms, by showing 2-3 bond C-H correlations. Without HSQC, proton shifts cannot be tied to specific carbons. Without COSY, you cannot trace the proton chain. Without HMBC, spin systems remain unconnected across quaternary centers, making the full skeleton impossible to assemble."
  explanation: "The power is in the combination: each experiment compensates for the blind spots of the others. HSQC cannot reveal connectivity; COSY cannot see across gaps in the proton network; HMBC has ambiguity (2-bond vs. 3-bond) that COSY and HSQC help resolve. Together they enable systematic, unambiguous structure elucidation of molecules too complex for 1D methods."
```

## Explainer

From your study of one-dimensional NMR, you know that each nucleus in a molecule resonates at a characteristic chemical shift, and that scalar (J) coupling splits peaks into multiplets that reveal connectivity. But in a complex molecule with dozens of protons, 1D spectra become hopelessly crowded — overlapping multiplets make it impossible to determine which proton is coupled to which. **Two-dimensional NMR** solves this by spreading the information across two frequency axes, creating a correlation map where off-diagonal peaks (cross-peaks) directly reveal relationships between nuclei.

The simplest 2D experiment is **COSY** (Correlation Spectroscopy). Both axes represent proton chemical shifts, and the diagonal contains the same peaks as a 1D spectrum. The key information lives in the **cross-peaks**: a cross-peak at coordinates (δA, δB) means proton A and proton B are connected through scalar coupling, typically across two or three bonds. Walking along COSY cross-peaks, you can trace the connectivity of a spin system — for instance, following an alkyl chain from CH₃ to CH₂ to CH. This is far more powerful than trying to match coupling constants in a 1D spectrum, because you see the connectivity directly as a pattern rather than inferring it from numerical coincidences.

**HSQC** (Heteronuclear Single Quantum Coherence) and **HMBC** (Heteronuclear Multiple Bond Correlation) extend this logic to carbon-proton relationships. In HSQC, one axis is ¹H chemical shift and the other is ¹³C chemical shift, and each cross-peak identifies a directly bonded C-H pair (one-bond ¹J coupling). This immediately tells you which carbon each proton is attached to. HMBC shows longer-range correlations — two-bond and three-bond C-H connections — which are essential for piecing together the carbon skeleton, especially across quaternary carbons (which have no directly attached proton and are invisible in HSQC). Together, COSY traces proton spin systems, HSQC maps each proton to its carbon, and HMBC bridges across gaps in the proton network to connect spin systems through the carbon framework.

The practical workflow for structure determination using 2D NMR follows a systematic logic. First, use HSQC to assign each proton to its directly bonded carbon. Then use COSY to map out connected proton spin systems — contiguous chains of coupled protons. Finally, use HMBC to connect those spin systems across quaternary carbons, heteroatoms, or carbonyl groups where the proton chain is interrupted. For a natural product like strychnine or a pharmaceutical compound, this combination of three experiments can fully determine a structure that would be impossibly ambiguous from 1D data alone. The power of 2D NMR lies in converting structure elucidation from a puzzle of overlapping peaks into a systematic reading of correlation maps.
