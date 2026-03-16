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

## Explainer

From your work on acid–base chemistry and pH calculations, you already know that mixing an acid with a base produces a neutralization reaction, and that pH quantifies the hydrogen ion concentration in solution. An acid–base titration puts this knowledge to quantitative use: you add a titrant of known concentration from a buret into an analyte solution of unknown concentration, tracking pH as you go. The volume at which the reaction is exactly complete — the **equivalence point** — lets you back-calculate the analyte's concentration through simple stoichiometry. The key insight is that the titration curve (pH plotted against volume of titrant added) is not a straight line but an S-shaped curve with a dramatic vertical inflection right at the equivalence point.

The shape of that curve depends entirely on the strengths of the acid and base involved. For a strong acid titrated with a strong base, the equivalence point falls at pH 7 and the inflection is steep and symmetric. But when you titrate a weak acid with a strong base, the equivalence point shifts above pH 7 — the conjugate base produced by the neutralization hydrolyzes water, making the solution basic at equivalence. This is a critical point that follows directly from your pH calculation prerequisites: the species present at equivalence determine the pH, not some universal rule that neutralization always yields pH 7.

Halfway to the equivalence point, something elegant happens. At this **half-equivalence point**, exactly half the weak acid has been converted to its conjugate base, so [HA] = [A⁻]. Plugging this into the **Henderson–Hasselbalch equation** — pH = pKa + log([A⁻]/[HA]) — gives pH = pKa, because log(1) = 0. This is the heart of the **buffer region**, where pH changes very slowly with added titrant because the solution contains roughly equal amounts of a weak acid and its conjugate base. Buffers resist pH change by absorbing added H⁺ or OH⁻, and the titration curve is nearly flat through this region.

Detecting the equivalence point in practice requires an **indicator** — a weak acid whose protonated and deprotonated forms have different colors. The indicator must change color within the steep portion of the titration curve, where pH swings by several units with a single drop of titrant. For a strong acid–strong base titration, the steep region spans roughly pH 4–10, so many indicators work. For a weak acid–strong base titration, the steep region is narrower and shifted basic, so you need an indicator like phenolphthalein that transitions around pH 8–10. Choosing the wrong indicator means the color change happens before or after the true equivalence point, introducing systematic error into your result.

Polyprotic acids — like phosphoric acid with three ionizable protons — produce multiple equivalence points, each with its own inflection and buffer region. The titration curve shows a series of S-shaped steps, and you can read off successive pKa values at each half-equivalence point. This makes acid–base titration not just a concentration measurement tool but also a way to characterize the acid–base properties of unknown compounds, connecting the quantitative power of titrimetry to the deeper chemical understanding of proton-transfer equilibria you built in your prerequisite courses.
