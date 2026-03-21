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

## Questions

```yaml
- question: "A student attempts a permanganometry titration in near-neutral solution instead of strongly acidic solution. What goes wrong?"
  type: multiple-choice
  options:
    - "The permanganate oxidizes the solvent instead of the analyte, consuming extra titrant"
    - "MnO₄⁻ is reduced to MnO₂ (a brown precipitate) rather than Mn²⁺, so the endpoint color change is obscured and the stoichiometry changes"
    - "The reaction proceeds too quickly in neutral solution, making it impossible to detect the endpoint"
    - "Nothing changes — the endpoint is equally well-defined in neutral and acidic solution"
  answer: 1
  explanation: "Permanganometry is self-indicating only in strongly acidic solution because only there is the MnO₄⁻ → Mn²⁺ reduction (5 electrons per Mn) thermodynamically favored and fast. In neutral or basic solution, MnO₄⁻ is reduced to MnO₂ (brown precipitate, 3 electrons per Mn), which clouds the solution and makes the persistent-pink endpoint undetectable. The different stoichiometry also invalidates any calculation based on the acidic-solution reaction. Acid concentration is not a minor procedural detail — it determines which reduction product forms and therefore whether the titration is valid."

- question: "In an indirect iodometric titration, the analyte oxidizes iodide (I⁻) to iodine (I₂), which is then back-titrated with sodium thiosulfate. Why is starch indicator added near the endpoint rather than at the beginning?"
  type: multiple-choice
  options:
    - "Starch destroys thiosulfate if present from the start, preventing accurate measurement"
    - "Starch forms an intensely blue complex with I₂; added at the start when I₂ concentration is high, the blue color is so dark it masks the gradual color change, making the endpoint hard to detect"
    - "The starch–I₂ complex is irreversible, so if added early it permanently sequesters iodine from the titration"
    - "Starch reacts with the analyte rather than with iodine if it is present before the back-titration begins"
  answer: 1
  explanation: "Starch binds I₂ (as I₃⁻) to form a deep blue complex — this is the detection chemistry. But at high I₂ concentrations (early in the titration), the intense blue color is so dark that tracking the gradual lightening is difficult, and the bound complex is slow to release I₂ to react with thiosulfate, which can cause a premature apparent endpoint. Near the endpoint when I₂ concentration is already low (the solution is pale yellow-straw), adding starch gives a clean blue → colorless transition that is easy to detect precisely. Timing of starch addition is a practical precision issue."

- question: "Before the equivalence point in a redox titration, the solution potential is governed by the redox couple of the analyte rather than the titrant."
  type: true-false
  answer: true
  explanation: "The Nernst equation governs potential through the ratio of oxidized to reduced species. Before the equivalence point, excess analyte remains — for example, a mixture of Fe²⁺ and Fe³⁺ if iron is being titrated. The potential is determined by the Fe³⁺/Fe²⁺ ratio as titrant converts Fe²⁺ to Fe³⁺. Only after the equivalence point, when excess titrant (e.g., MnO₄⁻/Mn²⁺) dominates, does the titrant's redox couple govern the potential. At the equivalence point itself, the potential is intermediate and both couples contribute — and it jumps sharply, defining the endpoint."

- question: "In iodometric titrations, the pH of the solution has little effect on the accuracy of the result."
  type: true-false
  answer: false
  explanation: "pH is critical in iodometric methods. In alkaline conditions, iodine disproportionates: I₂ + 2OH⁻ → I⁻ + IO⁻ + H₂O. This converts I₂ to iodate (IO₃⁻) and iodide, meaning the I₂ that was supposed to be the measured species is consumed by a side reaction, causing low results. Acidic pH is required to suppress this disproportionation. Additionally, some analytes (like dichromate) generate different products at different pH values. pH control is as important in redox titrations as in acid–base work."

- question: "Why is it often necessary to pre-treat an analyte sample before performing a redox titration, and what would go wrong if this step were skipped?"
  type: short-answer
  answer: "Many real samples contain the analyte in mixed oxidation states — for example, an iron ore sample may contain both Fe²⁺ and Fe³⁺. A redox titrant reacts with only one oxidation state (e.g., KMnO₄ oxidizes Fe²⁺ but not Fe³⁺). If pre-reduction is skipped, the titration only consumes the portion of iron already in the lower state, giving a result that is systematically low and irreproducible depending on sample preparation. Pre-treatment (e.g., reducing all iron to Fe²⁺ with SnCl₂) ensures every mole of the analyte element reacts with the titrant, making the stoichiometric calculation valid."
  explanation: "The excess reductant from pre-treatment must also be destroyed before titration begins — otherwise it reacts with the titrant and consumes extra equivalents, giving a high result. This step (adding HgCl₂ to oxidize excess Sn²⁺, for example) is easy to overlook but essential. The concept generalizes: pre-oxidation may be needed instead if the analyte must be brought to a higher state before titration with a reducing titrant."
```

## Explainer

You already understand titrimetric analysis — adding a titrant of known concentration until the reaction is complete — and you know from electrochemistry that oxidation-reduction reactions involve electron transfer between species. A **redox titration** combines these two ideas: the titrant is an oxidizing or reducing agent, the analyte is its redox partner, and the equivalence point occurs when exactly the stoichiometric number of electrons has been transferred. Instead of tracking pH as in acid–base titrations, you track the electrochemical potential of the solution, which changes as the ratio of oxidized to reduced species shifts during the titration.

The **Nernst equation** governs the shape of the titration curve, just as the Henderson–Hasselbalch equation governs acid–base curves. Before the equivalence point, excess analyte remains unreacted, and the potential is determined by the analyte's redox couple (e.g., Fe³⁺/Fe²⁺). After the equivalence point, excess titrant dominates, and the potential reflects the titrant's redox couple (e.g., MnO₄⁻/Mn²⁺). At the equivalence point itself, the potential jumps sharply — this inflection is steeper when the difference in standard reduction potentials between the two couples is larger. A difference of at least 0.2 V typically produces a sharp enough break for accurate endpoint detection.

**Permanganometry** is the most elegant redox titration because KMnO₄ is its own indicator. In strongly acidic solution, MnO₄⁻ (deep purple) is reduced to Mn²⁺ (nearly colorless). As you add permanganate to the analyte, each drop is instantly decolorized as it reacts. The **endpoint** is the first drop that produces a persistent pink color — meaning all the analyte has been consumed and excess MnO₄⁻ remains. No separate indicator is needed. **Iodometric methods** work differently: iodine (I₂) or the triiodide complex (I₃⁻) serves as either a direct titrant or an intermediate. In indirect iodometry, the analyte oxidizes excess I⁻ to I₂, and the liberated iodine is then back-titrated with standardized sodium thiosulfate (Na₂S₂O₃). The starch indicator — which forms a deep blue complex with I₂ — signals the endpoint when the blue color disappears.

A practical consideration that distinguishes redox titrations from acid–base work is the frequent need for **pre-treatment** of the analyte. Many analytes exist in mixed oxidation states in real samples. To titrate iron in an ore, for example, you must first dissolve the sample and reduce all iron to Fe²⁺ using a reducing agent like SnCl₂ or a Jones reductor column. Any excess reducing agent must then be destroyed (by adding HgCl₂ or by air oxidation) before beginning the titration. This pre-reduction step ensures that every mole of titrant consumed corresponds to a mole of analyte, making the stoichiometric calculation valid. The combination of selective redox chemistry, Nernst-governed titration curves, and visual or potentiometric endpoint detection makes redox titrations a versatile and precise tool for determining metals, dissolved oxygen, and many other analytically important species.
