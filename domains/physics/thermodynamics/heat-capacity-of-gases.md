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

## Explainer

Heat capacity measures how much energy a substance needs per degree of temperature rise. For gases, the answer depends critically on what you hold constant: at constant volume, all energy input goes into molecular motion; at constant pressure, the gas expands as it heats, doing work on its surroundings. This is why gases have two distinct heat capacities — and understanding their relationship unlocks much of thermodynamics.

From the **equipartition theorem**, each quadratic degree of freedom contributes ½k_B per molecule (or ½R per mole) to the internal energy. A **monatomic** ideal gas (helium, argon) has only three translational degrees of freedom — motion in x, y, and z — giving U = (3/2)nRT. At constant volume, all heat input raises internal energy: C_V = (∂U/∂T)_V = (3/2)R ≈ 12.5 J/(mol·K). At constant pressure, the gas also expands against external pressure as it warms. That expansion work equals PΔV = nRΔT per mole (from the ideal gas law), so C_P = C_V + R = (5/2)R. The ratio **γ = C_P/C_V** = 5/3 ≈ 1.67 for monatomic gases, in excellent agreement with experiment for noble gases.

A **diatomic** gas (N₂, O₂ at room temperature) adds two rotational degrees of freedom — tumbling about the two axes perpendicular to the bond — raising f from 3 to 5, C_V to (5/2)R, and γ to 7/5 = 1.40. The bond axis itself carries negligible rotational energy because the moment of inertia about that axis is nearly zero. At high temperatures, **vibrational modes** also activate: the bond can stretch and compress, adding 2 more degrees of freedom (one kinetic, one potential) and pushing C_V toward (7/2)R. The fact that vibrational modes are "frozen out" at room temperature is a purely quantum effect — the vibrational energy level spacing is large compared to k_BT, so few molecules are thermally excited into the first vibrational state. This temperature dependence of f was one of the earliest clues that classical statistical mechanics was incomplete and quantum mechanics was needed.

The ratio γ = C_P/C_V appears throughout the rest of thermodynamics. In **adiabatic processes** — your next topic — the relations TV^{γ−1} = const and PV^γ = const both depend on γ. The speed of sound in a gas is v = √(γRT/M): acoustic compression and rarefaction happen adiabatically (too fast for heat exchange), so γ rather than 1 appears. Every time you track how a gas changes temperature during rapid, insulated, or isentropic processes, γ is the key parameter — and it encodes the molecular identity of the gas through the number of active degrees of freedom f = 2C_V/R.
