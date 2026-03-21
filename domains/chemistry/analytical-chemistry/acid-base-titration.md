---
id: acid-base-titration
title: Acid–Base Titrations and Buffer Systems
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: titrimetric-analysis-intro
  type: hard
- id: acid-base-chemistry
  type: hard
- id: ph-and-acid-base-calculations
  type: hard
tags:
- acid-base titration
- titration curve
- buffer
- equivalence point
- Henderson-Hasselbalch
stage: advanced
status: validated
---

# Acid–Base Titrations and Buffer Systems

## Core Idea
Acid–base titrations exploit neutralization reactions to determine the concentration of an acid or base. The titration curve (pH vs volume of titrant) shows an inflection at the equivalence point; its sharpness depends on the strength of the acid and base and their concentrations. Buffer regions — where pH changes slowly — occur when roughly half the titrant has been added. The Henderson–Hasselbalch equation describes buffer pH as pKa + log([A⁻]/[HA]). Indicators are weak acids whose conjugated forms have different colors; they must change color within the steep portion of the titration curve for accurate endpoint detection.

## How It's Best Learned
Calculate and then experimentally measure titration curves for strong acid–strong base, weak acid–strong base, and diprotic acid systems. Overlaying calculated and measured curves pinpoints where assumptions (activity vs concentration) break down.

## Common Misconceptions
- For a weak acid titrated with strong base, the equivalence point pH is NOT 7 — it is basic due to hydrolysis of the conjugate base.
- Phenolphthalein (changes at pH 8–10) is appropriate for weak acid–strong base titrations but may give large errors in weak base–strong acid titrations.

## Questions

```yaml
- question: "Acetic acid (a weak acid) is titrated with sodium hydroxide (a strong base). What is the expected pH at the equivalence point?"
  type: multiple-choice
  options:
    - "Exactly 7.00, because equal molar amounts of acid and base have been combined"
    - "Below 7, because excess acetic acid remains at the equivalence point"
    - "Above 7, because the sodium acetate produced hydrolyzes water to generate hydroxide ions"
    - "Exactly 7 for all monoprotic acids regardless of their strength"
  answer: 2
  explanation: "At the equivalence point of a weak acid–strong base titration, all the weak acid has been converted to its conjugate base (sodium acetate). Acetate ion is itself a weak base that hydrolyzes water: CH₃COO⁻ + H₂O ⇌ CH₃COOH + OH⁻. This produces hydroxide, making the solution basic — pH > 7. Only for strong acid–strong base titrations does the equivalence point fall at pH 7, because neither product (Na⁺ nor Cl⁻) affects water equilibrium. The common mistake is assuming neutralization always yields pH 7."

- question: "During a weak acid–strong base titration, the pH equals 4.75 at the half-equivalence point. What does this tell you about the acid?"
  type: multiple-choice
  options:
    - "The molar mass of the acid is 4.75 g/mol"
    - "The concentration of the acid solution is 4.75 M"
    - "The pKa of the acid is 4.75, because at half-equivalence [HA] = [A⁻] and the Henderson–Hasselbalch equation reduces to pH = pKa"
    - "The titration is 47.5% complete at this measurement"
  answer: 2
  explanation: "At the half-equivalence point, exactly half the weak acid has been converted to its conjugate base, so [HA] = [A⁻]. Substituting into Henderson–Hasselbalch: pH = pKa + log([A⁻]/[HA]) = pKa + log(1) = pKa + 0 = pKa. This makes acid–base titration a practical tool for determining pKa values experimentally — simply read the pH at the half-equivalence point from the titration curve. The buffer region near this point is flat precisely because pH ≈ pKa throughout."

- question: "For a strong acid–strong base titration, the equivalence point occurs at pH 7."
  type: true-false
  answer: true
  explanation: "When a strong acid (e.g., HCl) is fully neutralized by a strong base (e.g., NaOH), the products are a neutral salt (NaCl) and water. NaCl dissociates completely into Na⁺ and Cl⁻, neither of which undergoes hydrolysis or perturbs water's autoionization equilibrium. Therefore, the solution at the equivalence point is effectively pure salt water at pH 7. This is true specifically for strong acid–strong base pairs; weak acid or weak base systems produce non-neutral equivalence points."

- question: "Any indicator that changes color in the basic pH range can be used for any acid–base titration."
  type: true-false
  answer: false
  explanation: "An indicator must change color within the steep portion of the titration curve — the narrow range where a tiny volume of titrant causes a large pH swing. That steep region differs by titration type: for strong acid–strong base it spans roughly pH 4–10; for weak acid–strong base it is narrower and shifted basic (approximately pH 7–11). Using an indicator that transitions outside the steep region — even if it is technically 'in the basic range' — means the color change occurs before or after the true equivalence point, introducing systematic error."

- question: "Why does the pH at the equivalence point of a weak acid–strong base titration exceed 7, even though equal moles of acid and base were combined?"
  type: short-answer
  answer: "At the equivalence point, all the weak acid has been converted to its conjugate base. Unlike the neutral products of a strong acid–strong base reaction, a weak acid's conjugate base is itself a weak base that reacts with water: A⁻ + H₂O ⇌ HA + OH⁻. This hydrolysis generates hydroxide ions, making the solution basic. The pH above 7 is not a failure of the stoichiometry — it reflects the incomplete ionization character of the original weak acid: its conjugate base retains enough basicity to raise the solution's pH."
  explanation: "This follows directly from the definition of a weak acid: a weak acid does not fully donate its proton to water, so its conjugate base retains the capacity to accept protons from water. The stronger the original acid (higher Ka), the weaker its conjugate base, and the closer the equivalence point pH approaches 7. For a truly strong acid, the conjugate base has negligible basicity — hence pH 7 at equivalence. Every equivalence point pH is determined by the species present in solution at that point, not by a universal neutralization rule."
```

## Explainer

From your work on acid–base chemistry and pH calculations, you already know that mixing an acid with a base produces a neutralization reaction, and that pH quantifies the hydrogen ion concentration in solution. An acid–base titration puts this knowledge to quantitative use: you add a titrant of known concentration from a buret into an analyte solution of unknown concentration, tracking pH as you go. The volume at which the reaction is exactly complete — the **equivalence point** — lets you back-calculate the analyte's concentration through simple stoichiometry. The key insight is that the titration curve (pH plotted against volume of titrant added) is not a straight line but an S-shaped curve with a dramatic vertical inflection right at the equivalence point.

The shape of that curve depends entirely on the strengths of the acid and base involved. For a strong acid titrated with a strong base, the equivalence point falls at pH 7 and the inflection is steep and symmetric. But when you titrate a weak acid with a strong base, the equivalence point shifts above pH 7 — the conjugate base produced by the neutralization hydrolyzes water, making the solution basic at equivalence. This is a critical point that follows directly from your pH calculation prerequisites: the species present at equivalence determine the pH, not some universal rule that neutralization always yields pH 7.

Halfway to the equivalence point, something elegant happens. At this **half-equivalence point**, exactly half the weak acid has been converted to its conjugate base, so [HA] = [A⁻]. Plugging this into the **Henderson–Hasselbalch equation** — pH = pKa + log([A⁻]/[HA]) — gives pH = pKa, because log(1) = 0. This is the heart of the **buffer region**, where pH changes very slowly with added titrant because the solution contains roughly equal amounts of a weak acid and its conjugate base. Buffers resist pH change by absorbing added H⁺ or OH⁻, and the titration curve is nearly flat through this region.

Detecting the equivalence point in practice requires an **indicator** — a weak acid whose protonated and deprotonated forms have different colors. The indicator must change color within the steep portion of the titration curve, where pH swings by several units with a single drop of titrant. For a strong acid–strong base titration, the steep region spans roughly pH 4–10, so many indicators work. For a weak acid–strong base titration, the steep region is narrower and shifted basic, so you need an indicator like phenolphthalein that transitions around pH 8–10. Choosing the wrong indicator means the color change happens before or after the true equivalence point, introducing systematic error into your result.

Polyprotic acids — like phosphoric acid with three ionizable protons — produce multiple equivalence points, each with its own inflection and buffer region. The titration curve shows a series of S-shaped steps, and you can read off successive pKa values at each half-equivalence point. This makes acid–base titration not just a concentration measurement tool but also a way to characterize the acid–base properties of unknown compounds, connecting the quantitative power of titrimetry to the deeper chemical understanding of proton-transfer equilibria you built in your prerequisite courses.
