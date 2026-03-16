---
id: redox-titration
title: Oxidation–Reduction Titrations
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: titrimetric-analysis-intro
  type: hard
- id: electrochemistry-basics
  type: hard
- id: electrochemical-cells
  type: soft
tags:
- redox titration
- permanganometry
- iodometry
- dichromate
- oxidation state
stage: advanced
status: validated
---

# Oxidation–Reduction Titrations

## Core Idea
Redox titrations use oxidizing or reducing titrants to determine analytes through electron-transfer reactions. Common systems include permanganometry (KMnO₄ as self-indicating oxidant), dichromate titrations (K₂Cr₂O₇ with diphenylamine indicator), and iodometric methods (I₂/I₃⁻ or back-titration with thiosulfate). The Nernst equation governs how cell potential changes with analyte concentration; the titration curve plots potential vs volume. Pre-oxidation or pre-reduction steps convert analytes to a single oxidation state before titration.

## How It's Best Learned
Determine iron content in an ore sample by dissolving, reducing all iron to Fe²⁺ with SnCl₂, and titrating with standardized KMnO₄. Comparing to a dichromate method with a potentiometric endpoint illustrates how detection strategy affects precision.

## Common Misconceptions
- KMnO₄ is self-indicating only in strongly acidic solution; in neutral or basic conditions, MnO₂ precipitates and the endpoint is poorly defined.
- Iodometric methods require careful pH control because iodine disproportionates in base, and starch indicator must be added near the endpoint to avoid premature decolorization.

## Explainer

You already understand titrimetric analysis — adding a titrant of known concentration until the reaction is complete — and you know from electrochemistry that oxidation-reduction reactions involve electron transfer between species. A **redox titration** combines these two ideas: the titrant is an oxidizing or reducing agent, the analyte is its redox partner, and the equivalence point occurs when exactly the stoichiometric number of electrons has been transferred. Instead of tracking pH as in acid–base titrations, you track the electrochemical potential of the solution, which changes as the ratio of oxidized to reduced species shifts during the titration.

The **Nernst equation** governs the shape of the titration curve, just as the Henderson–Hasselbalch equation governs acid–base curves. Before the equivalence point, excess analyte remains unreacted, and the potential is determined by the analyte's redox couple (e.g., Fe³⁺/Fe²⁺). After the equivalence point, excess titrant dominates, and the potential reflects the titrant's redox couple (e.g., MnO₄⁻/Mn²⁺). At the equivalence point itself, the potential jumps sharply — this inflection is steeper when the difference in standard reduction potentials between the two couples is larger. A difference of at least 0.2 V typically produces a sharp enough break for accurate endpoint detection.

**Permanganometry** is the most elegant redox titration because KMnO₄ is its own indicator. In strongly acidic solution, MnO₄⁻ (deep purple) is reduced to Mn²⁺ (nearly colorless). As you add permanganate to the analyte, each drop is instantly decolorized as it reacts. The **endpoint** is the first drop that produces a persistent pink color — meaning all the analyte has been consumed and excess MnO₄⁻ remains. No separate indicator is needed. **Iodometric methods** work differently: iodine (I₂) or the triiodide complex (I₃⁻) serves as either a direct titrant or an intermediate. In indirect iodometry, the analyte oxidizes excess I⁻ to I₂, and the liberated iodine is then back-titrated with standardized sodium thiosulfate (Na₂S₂O₃). The starch indicator — which forms a deep blue complex with I₂ — signals the endpoint when the blue color disappears.

A practical consideration that distinguishes redox titrations from acid–base work is the frequent need for **pre-treatment** of the analyte. Many analytes exist in mixed oxidation states in real samples. To titrate iron in an ore, for example, you must first dissolve the sample and reduce all iron to Fe²⁺ using a reducing agent like SnCl₂ or a Jones reductor column. Any excess reducing agent must then be destroyed (by adding HgCl₂ or by air oxidation) before beginning the titration. This pre-reduction step ensures that every mole of titrant consumed corresponds to a mole of analyte, making the stoichiometric calculation valid. The combination of selective redox chemistry, Nernst-governed titration curves, and visual or potentiometric endpoint detection makes redox titrations a versatile and precise tool for determining metals, dissolved oxygen, and many other analytically important species.
