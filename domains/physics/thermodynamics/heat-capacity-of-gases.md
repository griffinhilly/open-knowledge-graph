---
id: heat-capacity-of-gases
title: Heat Capacities of Gases (Cv and Cp)
domain: physics
course: thermodynamics
prerequisites:
- id: specific-heat-capacity
  type: hard
- id: equipartition-theorem
  type: hard
- id: isobaric-and-isochoric-processes
  type: hard
- id: mayer-relation-cp-cv-difference
  type: soft
builds-toward:
- adiabatic-processes
tags:
- heat-capacity
- Cv
- Cp
- monatomic
- diatomic
- adiabatic-index
stage: formal-systems
status: validated
---
# Heat Capacities of Gases (Cv and Cp)

## Core Idea
Gases have two important molar heat capacities: Cv (at constant volume) and Cp (at constant pressure). Equipartition gives Cv = (f/2)R where f is the number of active degrees of freedom. For monatomic gases f = 3, so Cv = (3/2)R and Cp = (5/2)R. For diatomic gases at room temperature f = 5, giving Cv = (5/2)R and Cp = (7/2)R. The ratio γ = Cp/Cv = (f+2)/f appears in adiabatic relations and determines the speed of sound.

## How It's Best Learned
Tabulate Cv, Cp, and γ for monatomic, diatomic, and triatomic gases and verify against experimental values. Notice that experimental Cv for diatomic gases at very high temperatures exceeds the f = 5 prediction — vibrational modes are activating.

## Common Misconceptions
- Cp and Cv are properties of the gas, not the process — the process determines which one is relevant.
- Classical equipartition predicts heat capacities that fail for gases at low temperature due to quantum effects (freezing of vibrational modes).

## Questions

```yaml
- question: "Why is Cp always greater than Cv for an ideal gas?"
  type: multiple-choice
  options:
    - "At constant pressure, gas molecules move faster, so more energy is needed per degree of temperature rise"
    - "At constant pressure, some of the heat input does work expanding the gas against external pressure rather than raising temperature, requiring extra heat for the same ΔT"
    - "At constant volume, the gas loses energy through the container walls more rapidly than at constant pressure"
    - "At constant pressure, additional molecular degrees of freedom become accessible that are frozen at constant volume"
  answer: 1
  explanation: "At constant volume, all heat input goes directly into raising internal energy (and thus temperature). At constant pressure, the gas expands as it warms — this expansion does work on the surroundings (W = PΔV = nRΔT for an ideal gas), which consumes energy without raising temperature. You must supply that extra energy on top of raising the internal energy, so Cp = Cv + R. The difference is always R per mole, regardless of molecular structure — it comes from the expansion work, not from the gas's internal degrees of freedom."

- question: "Equal moles of helium (monatomic) and nitrogen (diatomic, room temperature) are each heated by 10 K at constant volume. Which gas requires more heat?"
  type: multiple-choice
  options:
    - "Helium, because lighter molecules heat up faster and need less energy, so nitrogen needs more by comparison — wait, no — helium actually needs more because monatomic gases are efficient heat absorbers"
    - "Nitrogen, because it has more active degrees of freedom (f = 5) and a higher Cv = (5/2)R compared to helium's Cv = (3/2)R"
    - "They require the same heat, because all ideal gases behave identically regardless of molecular structure"
    - "Helium, because its lower molecular mass means each molecule absorbs more energy per collision"
  answer: 1
  explanation: "Cv = (f/2)R, where f is the number of active degrees of freedom. For monatomic helium, f = 3 (translation only), giving Cv = (3/2)R ≈ 12.5 J/(mol·K). For diatomic nitrogen at room temperature, f = 5 (3 translation + 2 rotation), giving Cv = (5/2)R ≈ 20.8 J/(mol·K). Nitrogen has more ways to store energy, so it requires more heat per degree of temperature rise. The difference in Cv directly reflects the molecular identity of the gas through the equipartition theorem."

- question: "The heat capacities Cv and Cp of a gas depend on whether the thermodynamic process is reversible or irreversible — a reversible process has different heat capacities than an irreversible one."
  type: true-false
  answer: false
  explanation: "Cv and Cp are state functions — properties of the gas itself, determined by its molecular structure through the equipartition theorem. They do not depend on the process. What the process determines is which heat capacity is relevant: a constant-volume process uses Cv, a constant-pressure process uses Cp. The distinction is between 'property of the gas' (Cv, Cp) and 'property of the path' (reversibility). Conflating these leads to the error of thinking Cv 'applies' only to reversible constant-volume processes."

- question: "At very high temperatures, the molar heat capacity Cv of a diatomic gas exceeds its room-temperature value, because vibrational degrees of freedom become thermally active."
  type: true-false
  answer: true
  explanation: "At room temperature, vibrational modes of diatomic molecules are quantum-mechanically 'frozen out' — the vibrational energy level spacing is large compared to k_BT, so few molecules are thermally excited. This gives f = 5 and Cv = (5/2)R at room temperature. At high temperatures (typically above ~1000 K for diatomic gases), vibrational modes activate, adding 2 more degrees of freedom per vibrational mode (one kinetic, one potential), pushing Cv toward (7/2)R. This temperature dependence of Cv was historically one of the first failures of classical statistical mechanics that pointed toward quantum theory."

- question: "Explain why Cp = Cv + R for any ideal gas, regardless of its molecular structure."
  type: short-answer
  answer: "At constant pressure, heating a gas by dT requires not only raising its internal energy (which costs Cv dT per mole) but also supplying the work done by the expanding gas. By the ideal gas law, PΔV = nRΔT per mole, so the extra energy per mole per kelvin is R. Therefore Cp = Cv + R. This relationship holds for any ideal gas — monatomic, diatomic, or polyatomic — because the expansion work nRΔT depends only on the ideal gas law, not on molecular structure."
  explanation: "The R in Cp − Cv = R is the gas constant, which appears here because the expansion work PΔV = nRΔT is derived directly from the ideal gas law PV = nRT. This is why the difference is universal: every ideal gas expands by the same amount per mole per kelvin at constant pressure, regardless of how many internal degrees of freedom it has. The molecular structure affects Cv (through f); the ideal gas expansion adds exactly R on top of that for Cp."
```

## Explainer

Heat capacity measures how much energy a substance needs per degree of temperature rise. For gases, the answer depends critically on what you hold constant: at constant volume, all energy input goes into molecular motion; at constant pressure, the gas expands as it heats, doing work on its surroundings. This is why gases have two distinct heat capacities — and understanding their relationship unlocks much of thermodynamics.

From the **equipartition theorem**, each quadratic degree of freedom contributes ½k_B per molecule (or ½R per mole) to the internal energy. A **monatomic** ideal gas (helium, argon) has only three translational degrees of freedom — motion in x, y, and z — giving U = (3/2)nRT. At constant volume, all heat input raises internal energy: C_V = (∂U/∂T)_V = (3/2)R ≈ 12.5 J/(mol·K). At constant pressure, the gas also expands against external pressure as it warms. That expansion work equals PΔV = nRΔT per mole (from the ideal gas law), so C_P = C_V + R = (5/2)R. The ratio **γ = C_P/C_V** = 5/3 ≈ 1.67 for monatomic gases, in excellent agreement with experiment for noble gases.

A **diatomic** gas (N₂, O₂ at room temperature) adds two rotational degrees of freedom — tumbling about the two axes perpendicular to the bond — raising f from 3 to 5, C_V to (5/2)R, and γ to 7/5 = 1.40. The bond axis itself carries negligible rotational energy because the moment of inertia about that axis is nearly zero. At high temperatures, **vibrational modes** also activate: the bond can stretch and compress, adding 2 more degrees of freedom (one kinetic, one potential) and pushing C_V toward (7/2)R. The fact that vibrational modes are "frozen out" at room temperature is a purely quantum effect — the vibrational energy level spacing is large compared to k_BT, so few molecules are thermally excited into the first vibrational state. This temperature dependence of f was one of the earliest clues that classical statistical mechanics was incomplete and quantum mechanics was needed.

The ratio γ = C_P/C_V appears throughout the rest of thermodynamics. In **adiabatic processes** — your next topic — the relations TV^{γ−1} = const and PV^γ = const both depend on γ. The speed of sound in a gas is v = √(γRT/M): acoustic compression and rarefaction happen adiabatically (too fast for heat exchange), so γ rather than 1 appears. Every time you track how a gas changes temperature during rapid, insulated, or isentropic processes, γ is the key parameter — and it encodes the molecular identity of the gas through the number of active degrees of freedom f = 2C_V/R.
