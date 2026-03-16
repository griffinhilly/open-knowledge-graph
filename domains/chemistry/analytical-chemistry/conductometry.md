---
id: conductometry
title: Conductometry and Conductometric Titrations
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: electrochemistry-basics
  type: hard
- id: titrimetric-analysis-intro
  type: soft
- id: electric-current-and-resistance
  type: soft
- id: ohms-law
  type: soft
- id: electric-current-definition
  type: soft
tags:
- conductometry
- conductance
- molar conductivity
- Kohlrausch
- conductometric titration
stage: advanced
status: validated
---

# Conductometry and Conductometric Titrations

## Core Idea
Conductometry measures the ability of a solution to conduct electric current, which depends on ion concentration, charge, and mobility. Molar conductivity Λm decreases with concentration for strong electrolytes (Kohlrausch's law: Λm = Λm° − K√c) due to ion–ion interactions. Conductometric titrations track solution conductance during a reaction; the endpoint appears as a change in slope because different ions have different molar conductivities. The high mobility of H⁺ and OH⁻ makes conductometry especially sensitive for acid–base reactions. Direct conductometry is used for total dissolved solids (TDS) and purity of deionized water.

## How It's Best Learned
Conduct a conductometric titration of HCl with NaOH, measuring conductance after each addition and plotting to locate the endpoint geometrically from the two linear segments. Compare the endpoint to that from a pH titration run simultaneously to understand the complementary nature of the methods.

## Common Misconceptions
- Conductance increases on both sides of the acid–base equivalence point — the minimum is the endpoint, not a maximum.
- Conductometry is not selective for specific ions; it measures all ionic species, making it unsuitable for complex matrices with many ionic components.

## Explainer

From your study of electrochemistry, you know that ions in solution carry electric current. Conductometry turns this into an analytical technique by measuring how well a solution conducts — its **conductance** (G), the reciprocal of resistance. A conductivity cell with two electrodes of known area and separation applies an alternating current (AC is used to prevent electrolysis) and measures the resulting current. The **conductivity** (κ) is conductance corrected for cell geometry, and **molar conductivity** (Λm) normalizes this to concentration, giving a property that reflects how effectively a given electrolyte carries current per mole of dissolved substance.

For strong electrolytes that dissociate completely, molar conductivity decreases slightly as concentration increases — not because fewer ions exist, but because electrostatic interactions between ions (the ionic atmosphere) slow their migration. **Kohlrausch's law** captures this empirically: Λm = Λm° − K√c, where Λm° is the molar conductivity at infinite dilution (where ions are independent) and K is a constant for a given electrolyte. This relationship, rooted in the Debye-Hückel theory you may have encountered in electrochemistry, means each ion contributes independently to conductivity at infinite dilution — the **law of independent migration of ions**. This allows you to calculate Λm° for weak electrolytes (like acetic acid) from the tabulated values of their constituent ions, even though Kohlrausch's law itself only applies to strong electrolytes.

**Conductometric titrations** exploit the fact that different ions have very different molar conductivities. The hydrogen ion (H⁺) has an exceptionally high molar conductivity (~350 S·cm²/mol) due to the Grotthuss proton-hopping mechanism, and the hydroxide ion (OH⁻) is similarly fast (~198 S·cm²/mol). In a titration of HCl with NaOH, adding base replaces fast H⁺ ions with slower Na⁺ ions, so conductance drops steadily. Past the equivalence point, excess OH⁻ is added with no H⁺ left to consume, so conductance rises sharply. The endpoint appears as the intersection of two straight lines on a conductance-versus-volume plot — a V-shaped minimum. This geometric determination is often more precise than a color-change indicator, especially for dilute solutions or weak acid-weak base titrations where pH changes near the endpoint are gradual.

Direct conductometry — simply measuring the conductivity of a solution without titration — is the basis for monitoring water purity (ultrapure water has conductivity below 0.055 μS/cm), measuring total dissolved solids in environmental samples, and checking electrolyte concentrations in clinical and industrial settings. Its main limitation is that it responds to all ions indiscriminately, so it cannot tell you which ions are present or distinguish between different sources of conductivity. For that, you need ion-selective techniques. But for total ionic content — fast, inexpensive, and non-destructive — conductometry is hard to beat.
