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
- id: electroanalytical-overview
  type: soft
tags:
- conductometry
- conductance
- molar conductivity
- Kohlrausch
- conductometric titration
stage: formal-systems
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

## Questions

```yaml
- question: "A student performs a conductometric titration of HCl with NaOH. A classmate says: 'The endpoint is where conductance reaches its maximum — that's when the most ions are present.' Who is correct?"
  type: multiple-choice
  options:
    - "The classmate is correct — maximum conductance indicates maximum ion concentration at the equivalence point"
    - "The student is correct — the endpoint appears as a minimum in conductance, because fast H⁺ ions are progressively replaced by slower Na⁺ ions before the equivalence point, and excess OH⁻ accumulates after it"
    - "Neither — the endpoint appears as a plateau where conductance stops changing"
    - "The classmate is correct — the high reactivity at the equivalence point creates a conductance spike"
  answer: 1
  explanation: "The V-shaped minimum, not a maximum, marks the endpoint. Before the equivalence point, highly mobile H⁺ ions (molar conductivity ~350 S·cm²/mol) are replaced by much slower Na⁺ ions (~50 S·cm²/mol), so conductance drops steadily. At the equivalence point, all H⁺ has been consumed and no excess OH⁻ has yet accumulated — conductance is at its minimum. Past the endpoint, each addition of NaOH adds highly mobile OH⁻ (~198 S·cm²/mol) to the solution, so conductance rises. The endpoint is the geometric intersection of these two linear segments."

- question: "Why do H⁺ and OH⁻ ions have exceptionally high molar conductivities compared to other ions like Na⁺ or Cl⁻?"
  type: multiple-choice
  options:
    - "H⁺ and OH⁻ are lighter than most ions, so they diffuse through water faster"
    - "H⁺ and OH⁻ carry more charge per ion than other common electrolytes"
    - "H⁺ and OH⁻ use the Grotthuss mechanism — proton hopping between water molecules — rather than physical migration through solution"
    - "H⁺ and OH⁻ are always present at higher concentrations, so their total conductance contribution is larger"
  answer: 2
  explanation: "The Grotthuss mechanism (proton hopping) allows charge to be transported without a proton physically moving across the solution. Instead, a proton transfers to an adjacent water molecule, which then transfers to the next, creating a 'relay' that propagates charge much faster than ionic migration. This is why H⁺ molar conductivity (~350 S·cm²/mol) is roughly 5-7× higher than typical ions like Na⁺ (~50) or K⁺ (~74). OH⁻ similarly benefits from this mechanism in reverse."

- question: "In a conductometric titration of HCl with NaOH, conductance reaches a maximum at the equivalence point because most H⁺ has been consumed and the solution now contains primarily Na⁺ and Cl⁻ at their highest combined concentration."
  type: true-false
  answer: false
  explanation: "Conductance reaches a MINIMUM at the equivalence point, not a maximum. Before the endpoint, fast H⁺ is replaced by slow Na⁺ — conductance falls. At the endpoint, H⁺ is fully consumed and no excess OH⁻ has accumulated, so only Na⁺ and Cl⁻ are present, giving the lowest conductance of the titration. After the endpoint, each volume of NaOH added introduces both Na⁺ and OH⁻ (and OH⁻ is very mobile), causing conductance to rise steeply. The common misconception confuses 'endpoint = special event' with 'endpoint = conductance maximum.'"

- question: "Conductometry measures the total ionic content of a solution without distinguishing which specific ions are present, making it unsuitable for identifying individual ionic species in complex mixtures."
  type: true-false
  answer: true
  explanation: "Conductivity cells respond to all ions in solution — there is no mechanism for ion-specific detection. Na⁺, K⁺, Mg²⁺, and Ca²⁺ all contribute to measured conductance, weighted by their concentrations and molar conductivities. This is both conductometry's strength (fast, non-destructive measurement of total dissolved ions) and its key limitation. For specific ion determination, techniques like ion-selective electrodes, ion chromatography, or ICP-MS are needed."

- question: "Explain why the endpoint of a conductometric acid-base titration is identified as a minimum in conductance, and how this geometric determination differs from finding the endpoint in a standard pH titration."
  type: short-answer
  answer: "The minimum occurs because fast H⁺ ions are replaced by slower Na⁺ before the equivalence point (conductance falls), and then excess OH⁻ accumulates after it (conductance rises). The endpoint is the intersection of two linear regression lines — a geometric V-shape. In a pH titration, the endpoint is the maximum slope point (inflection) of a sigmoid pH curve, identified by finding the largest ΔpH/ΔV step."
  explanation: "The two methods detect the same chemical equivalence point by completely different physical signals. Conductometric determination is often more precise for dilute solutions or weak acid-weak base titrations, where the pH change at equivalence is gradual and hard to locate accurately. The straight-line segments of a conductometric titration allow robust geometric fitting even with noisy data, and the V-shape minimum is unambiguous. The two techniques are complementary — pH detects hydrogen ion activity; conductance detects total ionic current."
```

## Explainer

From your study of electrochemistry, you know that ions in solution carry electric current. Conductometry turns this into an analytical technique by measuring how well a solution conducts — its **conductance** (G), the reciprocal of resistance. A conductivity cell with two electrodes of known area and separation applies an alternating current (AC is used to prevent electrolysis) and measures the resulting current. The **conductivity** (κ) is conductance corrected for cell geometry, and **molar conductivity** (Λm) normalizes this to concentration, giving a property that reflects how effectively a given electrolyte carries current per mole of dissolved substance.

For strong electrolytes that dissociate completely, molar conductivity decreases slightly as concentration increases — not because fewer ions exist, but because electrostatic interactions between ions (the ionic atmosphere) slow their migration. **Kohlrausch's law** captures this empirically: Λm = Λm° − K√c, where Λm° is the molar conductivity at infinite dilution (where ions are independent) and K is a constant for a given electrolyte. This relationship, rooted in the Debye-Hückel theory you may have encountered in electrochemistry, means each ion contributes independently to conductivity at infinite dilution — the **law of independent migration of ions**. This allows you to calculate Λm° for weak electrolytes (like acetic acid) from the tabulated values of their constituent ions, even though Kohlrausch's law itself only applies to strong electrolytes.

**Conductometric titrations** exploit the fact that different ions have very different molar conductivities. The hydrogen ion (H⁺) has an exceptionally high molar conductivity (~350 S·cm²/mol) due to the Grotthuss proton-hopping mechanism, and the hydroxide ion (OH⁻) is similarly fast (~198 S·cm²/mol). In a titration of HCl with NaOH, adding base replaces fast H⁺ ions with slower Na⁺ ions, so conductance drops steadily. Past the equivalence point, excess OH⁻ is added with no H⁺ left to consume, so conductance rises sharply. The endpoint appears as the intersection of two straight lines on a conductance-versus-volume plot — a V-shaped minimum. This geometric determination is often more precise than a color-change indicator, especially for dilute solutions or weak acid-weak base titrations where pH changes near the endpoint are gradual.

Direct conductometry — simply measuring the conductivity of a solution without titration — is the basis for monitoring water purity (ultrapure water has conductivity below 0.055 μS/cm), measuring total dissolved solids in environmental samples, and checking electrolyte concentrations in clinical and industrial settings. Its main limitation is that it responds to all ions indiscriminately, so it cannot tell you which ions are present or distinguish between different sources of conductivity. For that, you need ion-selective techniques. But for total ionic content — fast, inexpensive, and non-destructive — conductometry is hard to beat.
