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
status: validated
---

# Liquid-Liquid Extraction

## Core Idea
Liquid-liquid extraction (LLE) separates an analyte from matrix components by partitioning it between two immiscible solvents, typically an aqueous phase and an organic phase. The distribution ratio (D) describes the total concentration of all forms of the analyte in the organic phase divided by that in the aqueous phase, and it can be manipulated by adjusting pH, adding complexing agents, or choosing different solvents. Multiple sequential extractions are more efficient than a single extraction of the same total volume, a relationship quantified by the Craig equation. LLE remains widely used for sample cleanup before chromatographic analysis, for preconcentrating trace analytes, and for isolating analytes from complex biological or environmental matrices.

## How It's Best Learned
Extract a colored analyte (such as iodine or a metal-dithizone complex) from water into an organic solvent using a separatory funnel, measure the fraction extracted spectrophotometrically, then perform two extractions with half-volumes and compare total recovery. Seeing the Craig equation prediction confirmed experimentally makes the advantage of multiple extractions concrete.

## Common Misconceptions
- The partition coefficient (K) and distribution ratio (D) are not the same: K refers to a single chemical species, while D accounts for all forms of the analyte (protonated, complexed, etc.) in each phase, making D the practically useful quantity.
- Increasing the volume of extracting solvent has diminishing returns; it is almost always more efficient to perform multiple small extractions than one large one.

## Questions

```yaml
- question: "An analyst needs to extract 90% of an analyte from 100 mL of aqueous solution. The distribution ratio D = 5. Which extraction scheme achieves better recovery?"
  type: multiple-choice
  options:
    - "One extraction with 100 mL organic solvent — using the maximum total volume maximizes contact"
    - "Two extractions with 50 mL organic solvent each — multiple smaller extractions recover more analyte than one large extraction of the same total volume"
    - "Both schemes give identical recovery because the total volume of organic solvent is the same"
    - "One extraction with 100 mL is better because each contact with fresh solvent is less efficient than a large single contact"
  answer: 1
  explanation: "The Craig equation shows that multiple extractions with smaller volumes always outperform one extraction with the same total volume, given D > 0. After the first extraction, the analyte concentration in the aqueous phase is reduced — a fresh portion of organic solvent contacts a depleted aqueous phase and extracts a fixed fraction of what remains. With D = 5 and 100 mL aqueous vs. 100 mL organic in one extraction: fraction remaining = 100/(100 + 5×100) = 100/600 = 1/6, so 83% extracted. With two extractions of 50 mL each: fraction remaining = [100/(100 + 5×50)]² = [100/350]² = 0.286² ≈ 8%, so 92% extracted. Multiple extractions win."

- question: "A weak acid drug (pKa = 5) is being extracted from a biological sample into an organic solvent. The neutral form of the drug has a partition coefficient K = 100, but at pH 7.4 (blood pH), D = 0.03. Why is D so much lower than K?"
  type: multiple-choice
  options:
    - "At pH 7.4, the drug binds to plasma proteins, reducing free drug concentration in the aqueous phase"
    - "K and D are unrelated quantities — D at physiological pH reflects a different chemical equilibrium than K"
    - "At pH 7.4, which is well above the pKa, the drug is predominantly ionized; the ionized form does not extract into organic solvent, greatly reducing D below K"
    - "K is measured in different units than D, so direct comparison is not meaningful"
  answer: 2
  explanation: "The distribution ratio D accounts for all chemical forms of the analyte in each phase. At pH 7.4 (two units above pKa = 5), the Henderson-Hasselbalch equation predicts roughly 99.6% of the drug is in the ionized (conjugate base) form. The ionized form is polar and essentially insoluble in organic solvents, while only the tiny fraction of neutral form extracts. D therefore reflects the weighted average across all forms: mostly ionized drug that won't transfer, giving D ≪ K. This is why pH adjustment is the primary tool for LLE — lowering the pH toward or below pKa converts most of the drug to the neutral form, dramatically increasing D."

- question: "The distribution ratio D is always equal to or greater than the partition coefficient K for a given analyte and solvent pair, because D accounts for more chemical species."
  type: true-false
  answer: false
  explanation: "D can be less than K, greater than K, or equal to K depending on the chemical conditions. D = K only when the analyte exists entirely in a single chemical form in both phases. If the analyte is partially ionized in the aqueous phase (as for a weak acid at high pH), D < K because the ionized form does not extract into the organic phase, reducing the effective concentration ratio. If conditions promote the formation of extractable complexes in the organic phase (e.g., metal-chelate complexes), D could exceed K. The relationship between D and K is not fixed — it depends on pH, complexing agents, and other equilibrium conditions."

- question: "Performing three extractions with 10 mL of organic solvent each will recover more analyte than one extraction with 30 mL of the same solvent, assuming D > 0."
  type: true-false
  answer: true
  explanation: "This follows directly from the Craig equation. Each fresh portion of organic solvent extracts a fixed fraction of the analyte remaining in the aqueous phase. After one extraction, the second portion contacts a depleted aqueous phase and still extracts that same fraction of the remainder. The cumulative effect is always greater recovery with multiple smaller extractions than with one large extraction of the same total volume, as long as D > 0. In practice, three to four extractions are sufficient to achieve >95% recovery for analytes with moderate D values, and adding more extractions beyond that yields diminishing returns."

- question: "Why is the distribution ratio D a more useful quantity than the partition coefficient K for predicting and optimizing liquid-liquid extraction of real analytical samples?"
  type: short-answer
  answer: "K describes the partitioning of a single, specific chemical species between two phases — it is a thermodynamic constant that applies only to one form of the analyte (e.g., the neutral molecule). In real samples, analytes often exist as multiple chemical species simultaneously: a weak acid can be neutral or ionized, a metal can be free or complexed, a drug can be protein-bound or free. D accounts for all of these forms: it is the ratio of total analytical concentration in the organic phase to total analytical concentration in the aqueous phase. Because extraction efficiency in practice depends on how much of the analyte actually transfers (in all its forms), D directly predicts extraction yield, whereas K alone would overestimate extraction if most of the analyte is in a form that cannot transfer."
  explanation: "The practical consequence is that D, not K, is what the analyst controls and optimizes. By adjusting pH to change the ionization state, or adding complexing agents to convert a poorly extractable form into an extractable complex, the analyst changes D without changing K. This is why pH is the most powerful LLE parameter: it shifts the equilibrium between forms with very different K values, dramatically changing the overall extraction efficiency. The key insight is that K is a property of a specific molecule under specific conditions, while D is a measurable property of the full chemical system that directly predicts experimental outcome."
```

## Explainer

From your study of sample preparation, you know that real analytical samples — blood, soil, wastewater, food — contain far more than just the analyte. Before an instrument can measure what you care about, you need to isolate it from the matrix. **Liquid-liquid extraction** (LLE) does this by exploiting a fundamental physical chemistry principle: when two immiscible solvents are shaken together, each dissolved substance distributes between the two phases according to its relative solubility in each. A nonpolar analyte will preferentially dissolve in an organic solvent like dichloromethane or ethyl acetate, leaving polar matrix components behind in the aqueous phase.

The quantitative measure of this partitioning is the **distribution ratio** (D), defined as the total analytical concentration of the analyte in the organic phase divided by that in the aqueous phase. D differs from the thermodynamic **partition coefficient** (K) because D accounts for all chemical forms of the analyte — if an acidic drug exists partly as the neutral molecule and partly as its conjugate base, only the neutral form extracts well into organic solvent, so D depends on pH even though K for the neutral species is constant. This is why pH adjustment is the most powerful tool for controlling LLE: by shifting the equilibrium between ionized and un-ionized forms, you can make D very large (for extraction) or very small (for back-extraction into a fresh aqueous phase at a different pH).

The most important quantitative insight in LLE is captured by the **Craig equation**: the fraction extracted in n extractions with volume V of organic solvent from volume Vaq of aqueous phase is 1 − [Vaq/(Vaq + D·V)]ⁿ. This reveals that two extractions with 25 mL each always recover more analyte than one extraction with 50 mL, given the same D. The mathematical reason is that each fresh portion of solvent contacts a solution that has already been partially depleted, so it extracts a fixed fraction of what remains. Three extractions of 15 mL will recover even more. In practice, three to four extractions capture >95% of analytes with moderate D values, and the equation lets you calculate exactly how many extractions you need for a target recovery.

Beyond simple partitioning, LLE can be made more selective through **chemical manipulation**. Adding a chelating agent (like dithizone for heavy metals) converts metal ions into neutral complexes that partition strongly into organic solvents, achieving both extraction and selectivity simultaneously. **Ion-pair extraction** adds a large hydrophobic counterion that pairs with a charged analyte, creating a neutral ion pair that transfers to the organic phase. **Back-extraction** — shaking the organic extract with a fresh aqueous phase under conditions that favor the analyte returning to water — provides a second dimension of cleanup and can preconcentrate the analyte if the back-extraction volume is small. These techniques, combined with pH control, make LLE a versatile and powerful sample preparation method that remains in wide use despite the growth of solid-phase extraction alternatives.
