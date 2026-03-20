---
id: liquid-liquid-extraction
title: Liquid-Liquid Extraction
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: sample-preparation
  type: hard
tags:
- extraction
- partition coefficient
- distribution ratio
- Craig equation
- separatory funnel
- solvent extraction
- back extraction
stage: advanced
status: draft
---

# Liquid-Liquid Extraction

## Core Idea
Liquid-liquid extraction (LLE) separates an analyte from matrix components by partitioning it between two immiscible solvents, typically an aqueous phase and an organic phase. The distribution ratio (D) describes the total concentration of all forms of the analyte in the organic phase divided by that in the aqueous phase, and it can be manipulated by adjusting pH, adding complexing agents, or choosing different solvents. Multiple sequential extractions are more efficient than a single extraction of the same total volume, a relationship quantified by the Craig equation. LLE remains widely used for sample cleanup before chromatographic analysis, for preconcentrating trace analytes, and for isolating analytes from complex biological or environmental matrices.

## How It's Best Learned
Extract a colored analyte (such as iodine or a metal-dithizone complex) from water into an organic solvent using a separatory funnel, measure the fraction extracted spectrophotometrically, then perform two extractions with half-volumes and compare total recovery. Seeing the Craig equation prediction confirmed experimentally makes the advantage of multiple extractions concrete.

## Common Misconceptions
- The partition coefficient (K) and distribution ratio (D) are not the same: K refers to a single chemical species, while D accounts for all forms of the analyte (protonated, complexed, etc.) in each phase, making D the practically useful quantity.
- Increasing the volume of extracting solvent has diminishing returns; it is almost always more efficient to perform multiple small extractions than one large one.

## Explainer

From your study of sample preparation, you know that real analytical samples — blood, soil, wastewater, food — contain far more than just the analyte. Before an instrument can measure what you care about, you need to isolate it from the matrix. **Liquid-liquid extraction** (LLE) does this by exploiting a fundamental physical chemistry principle: when two immiscible solvents are shaken together, each dissolved substance distributes between the two phases according to its relative solubility in each. A nonpolar analyte will preferentially dissolve in an organic solvent like dichloromethane or ethyl acetate, leaving polar matrix components behind in the aqueous phase.

The quantitative measure of this partitioning is the **distribution ratio** (D), defined as the total analytical concentration of the analyte in the organic phase divided by that in the aqueous phase. D differs from the thermodynamic **partition coefficient** (K) because D accounts for all chemical forms of the analyte — if an acidic drug exists partly as the neutral molecule and partly as its conjugate base, only the neutral form extracts well into organic solvent, so D depends on pH even though K for the neutral species is constant. This is why pH adjustment is the most powerful tool for controlling LLE: by shifting the equilibrium between ionized and un-ionized forms, you can make D very large (for extraction) or very small (for back-extraction into a fresh aqueous phase at a different pH).

The most important quantitative insight in LLE is captured by the **Craig equation**: the fraction extracted in n extractions with volume V of organic solvent from volume Vaq of aqueous phase is 1 − [Vaq/(Vaq + D·V)]ⁿ. This reveals that two extractions with 25 mL each always recover more analyte than one extraction with 50 mL, given the same D. The mathematical reason is that each fresh portion of solvent contacts a solution that has already been partially depleted, so it extracts a fixed fraction of what remains. Three extractions of 15 mL will recover even more. In practice, three to four extractions capture >95% of analytes with moderate D values, and the equation lets you calculate exactly how many extractions you need for a target recovery.

Beyond simple partitioning, LLE can be made more selective through **chemical manipulation**. Adding a chelating agent (like dithizone for heavy metals) converts metal ions into neutral complexes that partition strongly into organic solvents, achieving both extraction and selectivity simultaneously. **Ion-pair extraction** adds a large hydrophobic counterion that pairs with a charged analyte, creating a neutral ion pair that transfers to the organic phase. **Back-extraction** — shaking the organic extract with a fresh aqueous phase under conditions that favor the analyte returning to water — provides a second dimension of cleanup and can preconcentrate the analyte if the back-extraction volume is small. These techniques, combined with pH control, make LLE a versatile and powerful sample preparation method that remains in wide use despite the growth of solid-phase extraction alternatives.
