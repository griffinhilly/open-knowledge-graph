---
id: real-gas-deviations
title: Deviations of Real Gases from Ideal Behavior
domain: physics
course: thermodynamics
prerequisites:
- id: ideal-gas-law
  type: hard
builds-toward:
- van-der-waals-equation-of-state
- compressibility-factor-z
- joule-thomson-expansion-effect
tags:
- equations-of-state
- intermolecular-forces
- high-pressure
stage: formal-systems
status: draft
---

# Deviations of Real Gases from Ideal Behavior

## Core Idea
Real gases deviate from ideal behavior because molecules have finite size (excluded volume) and experience intermolecular attractive forces, particularly at high pressures and low temperatures. The compressibility factor Z = PV/nRT quantifies deviations from ideality (Z = 1 for ideal gas, Z < 1 for attractive forces, Z > 1 for repulsive forces). Understanding real gas deviations is essential for accurate calculations in refrigeration, liquefaction, and high-pressure applications.

## How It's Best Learned
Plot Z versus pressure or reduced pressure for various gases. Identify regions where attractive forces (Z < 1) and repulsive forces (Z > 1) dominate.

## Common Misconceptions
- Thinking the ideal gas law works everywhere (it fails at high P and low T).
- Confusing molecular size effects (repulsive, Z > 1) with attractive forces (Z < 1).
- Assuming deviations are always small (they can be huge near the critical point).

## Questions

```yaml
- question: "At moderate pressures, the compressibility factor Z for CO₂ is measured to be 0.88. This means:"
  type: multiple-choice
  options:
    - "CO₂ occupies more volume than an ideal gas would at the same temperature and pressure"
    - "CO₂ molecules repel each other strongly, making the gas harder to compress"
    - "CO₂ exerts less pressure than the ideal gas law predicts, because intermolecular attractive forces reduce the molecules' momentum at the walls"
    - "CO₂ has a higher molar mass than predicted by its formula weight"
  answer: 2
  explanation: "Z = PV/nRT < 1 means the gas behaves as if it exerts less pressure than the ideal model predicts (at fixed T and V). The physical reason is intermolecular attractive forces: as a molecule approaches the container wall, nearby molecules pull it back, so it arrives with slightly less momentum. The result is lower wall-collision force — lower pressure — than a gas of non-interacting particles would show. Option A is incorrect: Z < 1 at fixed T and P means V < nRT/P (less volume), not more."

- question: "Helium at room temperature shows Z > 1 even at moderate pressures. Carbon dioxide at room temperature shows Z < 1 at moderate pressures before rising above 1 at very high pressures. Why the difference?"
  type: multiple-choice
  options:
    - "Helium has a higher boiling point, making its molecules harder to compress"
    - "Helium atoms are much larger than CO₂ molecules, so excluded volume effects dominate immediately"
    - "CO₂ has stronger intermolecular attractive forces relative to its kinetic energy at room temperature, so attraction (Z < 1) dominates at moderate pressures; helium's weak attractions mean repulsive excluded-volume effects (Z > 1) dominate first"
    - "CO₂ is a linear molecule and behaves differently from monatomic helium because of rotational degrees of freedom"
  answer: 2
  explanation: "The two effects competing are: (1) intermolecular attraction → Z < 1, and (2) excluded volume (finite molecular size) → Z > 1. CO₂ has significant van der Waals attraction, so at moderate pressures when molecules are moderately close, attraction dominates and Z dips below 1. Helium has extremely weak attractive forces (it barely liquefies at all), so excluded-volume repulsion dominates from the start and Z > 1. Room temperature is 'high' for helium relative to its critical temperature (5.2 K) but 'low' for CO₂ relative to its critical temperature (304 K), explaining why CO₂ still shows significant attractive effects at room temperature."

- question: "A gas in a regime where intermolecular attractive forces dominate will exert lower pressure on its container walls than an ideal gas at the same temperature and volume."
  type: true-false
  answer: true
  explanation: "True. Attractive forces create a net inward pull on molecules approaching the wall — they are slowed slightly before impact and thus transfer less momentum to the wall. Pressure is force per unit area, arising from molecular collisions, so reduced collision momentum means reduced pressure. This effect is captured by Z < 1: the actual PV product is less than nRT, indicating the gas is 'underperforming' relative to ideal predictions."

- question: "When the compressibility factor Z < 1, the real gas occupies a larger volume than an ideal gas would at the same temperature and pressure."
  type: true-false
  answer: false
  explanation: "False. Z = PV/nRT < 1 means PV < nRT. At fixed temperature T and pressure P, this rearranges to V < nRT/P — the real gas occupies a smaller volume than an ideal gas. The attractive forces pulling molecules together cause the gas to be more compact. (At fixed T and V, Z < 1 instead means P < nRT/V — lower pressure.) Either way, Z < 1 corresponds to the gas being 'pulled together' by attraction, not expanded."

- question: "Explain the two physical mechanisms that cause real gases to deviate from ideal behavior, and describe the conditions under which each mechanism dominates."
  type: short-answer
  answer: "Two mechanisms cause deviations: (1) Intermolecular attractive forces — at moderate pressures and low temperatures, molecules are close enough to attract each other. A molecule approaching the wall is pulled inward, reducing its impact momentum and lowering pressure below ideal predictions, so Z < 1. (2) Finite molecular volume (excluded volume) — at high pressures, molecules cannot overlap. The volume available to any molecule is less than the total container volume, making the gas harder to compress than ideal, so Z > 1. Attractive effects dominate when molecules are moderately close (moderate P, low T); repulsive/volume effects dominate when molecules are very close (high P). The Boyle temperature is where the two effects cancel and Z ≈ 1."
  explanation: "Both effects appear in the van der Waals equation: the a/V² term corrects for attraction (reduces effective pressure), and the b term corrects for excluded volume (reduces effective volume available). These corrections predict the characteristic dip-then-rise shape of Z vs. P curves observed experimentally for most gases."
```

## Explainer

The ideal gas law PV = nRT rests on two simplifying assumptions: molecules have negligible volume, and they exert no forces on each other between collisions. From your study of the ideal gas law, you know it works well for dilute gases at high temperatures — conditions where molecules are far apart and moving fast. Real gases deviate because both assumptions fail as pressure rises or temperature falls, and the **compressibility factor** Z = PV/nRT provides a single dimensionless measure of the deviation (Z = 1 for ideal, Z ≠ 1 for real).

Consider **attractive intermolecular forces** first. At moderate pressures, molecules are close enough to exert van der Waals attraction on each other. A molecule approaching the container wall feels a net inward pull from its neighbors — it arrives at the wall with slightly less momentum than it would in isolation. The result is that the gas exerts *less* pressure than the ideal model predicts: Z < 1. This is why gases can condense into liquids at all — attractive forces can overwhelm thermal kinetic energy, causing molecules to cluster and reducing the pressure. Carbon dioxide near its critical point (31°C, 73 atm) shows Z dramatically less than 1 because intermolecular attractions are near their strongest relative to the particles' kinetic energy.

At **high pressures**, the finite physical size of molecules becomes dominant. Molecules cannot occupy the same space — they have a hard repulsive core — so the volume actually available to any one molecule is less than the total container volume. The gas is harder to compress than the ideal model assumes: Z > 1. Think of compressing a jar of marbles: below some minimum volume they simply cannot pack any tighter, regardless of applied pressure. For gases like helium and hydrogen at room temperature, which have very weak attractive forces, this repulsive-core effect dominates even at moderate pressures and Z > 1 throughout.

The competition between these two effects produces the characteristic Z-vs-P curve: at low pressure, Z dips below 1 (attraction dominates), reaches a minimum, then rises above 1 at high pressure (repulsion dominates). The **Boyle temperature** — where B₂(T) = 0 in the virial expansion — is the temperature at which Z ≈ 1 across a range of pressures because attractive and repulsive effects cancel. Different gases cross the Boyle temperature at different values because their intermolecular potentials differ in depth and range. All of this behavior is captured quantitatively by the van der Waals equation (P + an²/V²)(V − nb) = nRT, where the constant a measures the strength of attractions and b measures the excluded volume — translating molecular-scale physics directly into macroscopic equations of state.
