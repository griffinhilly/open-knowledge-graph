---
id: van-der-waals-equation-of-state-advanced
title: 'Van der Waals Equation: Real Gas Behavior'
domain: chemistry
course: physical-chemistry
prerequisites:
- id: real-gases-van-der-waals
  type: hard
- id: intermolecular-potential-energy-functions
  type: soft
builds-toward:
- hydrogen-bonding-energetics
tags:
- thermodynamics
- equation-of-state
- real-gases
- virial
stage: formal-systems
status: validated
---

# Van der Waals Equation: Real Gas Behavior

## Core Idea
(P + a/V²)(V − b) = RT introduces molecular size (excluded volume b) and attractive forces (a parameter) to ideal gas law, predicting real gas behavior near condensation. Higher virial coefficients and compressibility factors Z extend this to even better accuracy. These corrections explain why gases liquefy and why critical phenomena (critical point, law of rectilinear diameters) occur.

## How It's Best Learned
Calculate compressibility factors for CO₂ near critical point using van der Waals vs. ideal gas law; measure or look up a and b parameters from literature; plot isotherms and identify critical behavior; relate a to intermolecular attractions and b to molecular size.

## Common Misconceptions
- Assuming the van der Waals equation is quantitatively accurate across all conditions; it fails near the critical point and for hydrogen-bonded fluids. - Treating a and b as truly universal constants; they depend on the model and are temperature-dependent for accurate predictions.

## Questions

```yaml
- question: "A real gas at moderate pressure shows a compressibility factor Z = 0.87. What does this tell you about which intermolecular effect dominates at these conditions?"
  type: multiple-choice
  options:
    - "Excluded volume dominates — gas molecules are crowding each other, increasing pressure beyond ideal"
    - "Attractive forces between molecules dominate — they pull molecules together, reducing pressure below ideal, so PV < nRT"
    - "The gas behaves ideally; Z values near 1 indicate ideal behavior"
    - "The temperature is above the critical temperature, so neither correction applies"
  answer: 1
  explanation: "Z = PV/nRT. When Z < 1, the actual PV product is smaller than nRT predicts, meaning the gas exerts less pressure than an ideal gas would. This happens because attractive intermolecular forces pull molecules toward each other, reducing the frequency and force of wall collisions. The van der Waals correction term a/V² captures this: it reduces the measured pressure (P_measured = P_ideal − a/V²). At very high pressures, excluded volume dominates and Z > 1. The crossover behavior is a diagnostic of which physical effect wins in each regime."

- question: "The van der Waals equation predicts a universal critical compressibility Z_c = 3/8 = 0.375 for all gases. Measured values range from 0.23 to 0.29. What is the correct interpretation?"
  type: multiple-choice
  options:
    - "The van der Waals equation is fundamentally incorrect about the existence of critical points"
    - "The law of corresponding states is qualitatively correct — all gases behave similarly at reduced conditions — but the van der Waals equation overestimates Z_c because it treats molecular interactions too simply"
    - "Only the a parameter needs to be adjusted; the b parameter is universal"
    - "Real gases cannot be described by any two-parameter equation of state"
  answer: 1
  explanation: "The van der Waals equation captures the essential physics of the critical point and correctly predicts that all gases share a universal behavior when expressed in reduced variables (the law of corresponding states). However, it overestimates Z_c by about 30–60% because its pairwise, spherically symmetric treatment of molecular interactions misses the complexity of real molecules (non-spherical shapes, hydrogen bonding, three-body interactions). The qualitative insight — universal critical behavior — survives into more sophisticated equations of state; the quantitative prediction does not."

- question: "At very high pressures, the compressibility factor Z of a real gas always exceeds 1.0."
  type: true-false
  answer: true
  explanation: "At very high pressures, molecules are forced close together and the excluded volume correction (the b term) dominates. Because molecules physically occupy space, the effective volume available for molecular motion (V − b) is smaller than the container volume V. This means the gas resists compression more than an ideal gas would, pushing Z above 1. The attractive-force correction (a/V²) is significant only at moderate pressures; at high enough pressures, excluded volume always wins."

- question: "The van der Waals parameters a and b are universal constants that apply equally well to all gas molecules, analogous to how universal gas constant R applies universally."
  type: true-false
  answer: false
  explanation: "R is truly universal — it appears in all ideal gas behavior by definition. The van der Waals a and b parameters are substance-specific: a reflects the strength of intermolecular attractions (large for polar or easily polarizable molecules, small for noble gases) and b reflects molecular size. They must be experimentally determined for each gas. Moreover, they are not strictly constant — b is essentially a molecular-volume parameter that is approximately constant, but a is somewhat temperature-dependent for quantitative accuracy. Different equations of state (Redlich-Kwong, Peng-Robinson) use different functional forms to capture this temperature dependence."

- question: "Explain why the compressibility factor Z of a real gas can be both less than 1 at moderate pressures and greater than 1 at very high pressures. What physical effect governs each regime?"
  type: short-answer
  answer: "At moderate pressures, molecules are far enough apart that attractive forces between them are significant. These attractions pull molecules toward each other, reducing the force of wall collisions and making the pressure lower than ideal-gas predictions — so PV < nRT and Z < 1. At very high pressures, molecules are forced so close together that their finite volumes become important: the space available for molecular motion is V − b (the excluded volume), not V. Molecules collide with walls more forcefully than in an ideal gas because they have less room to move, so PV > nRT and Z > 1. The crossover point where Z = 1 despite non-ideal behavior is called the Boyle temperature."
  explanation: "The van der Waals equation builds in both corrections: the a/V² term reduces pressure (attractive forces) and the 1/(V−b) term increases it (excluded volume). Plotting Z vs. pressure for a real gas shows it dipping below 1 at intermediate pressures before rising above 1 at high pressures. The temperature determines which effect dominates: near the boiling point, attractions dominate; well above the critical temperature, excluded volume tends to dominate even at moderate pressures."
```

## Explainer

You already know from your introduction to real gases that the ideal gas law, PV = nRT, breaks down when molecules are close together — at high pressures and low temperatures. The **van der Waals equation** was your first correction: (P + a/V²)(V − b) = RT (per mole). Now we dig deeper into what these corrections actually mean physically and where the equation succeeds and fails. The parameter **b** represents the **excluded volume** — the space physically occupied by the molecules themselves. Think of it this way: if you have a box of tennis balls, the gas molecules can only move in the space between the balls, not through them. This makes the effective volume smaller than the container volume, so V becomes V − b. The parameter **a** captures the average attractive force between molecules: in a real gas, molecules pulling on each other slightly reduce the pressure compared to what you'd expect from ideal behavior, so the measured pressure is P_ideal − a/V².

The most revealing way to see where the van der Waals equation works and fails is through the **compressibility factor** Z = PV/(nRT). For an ideal gas, Z = 1 everywhere. For a real gas, Z deviates: at moderate pressures, attractive forces dominate and Z < 1 (the gas is more compressible than ideal), while at very high pressures, excluded volume dominates and Z > 1 (the gas resists compression more than ideal). If you plot van der Waals isotherms (P vs. V at constant T), something dramatic happens below the **critical temperature**: the isotherms develop an S-shaped wiggle, predicting that pressure would decrease as volume decreases — a physically impossible region. This unphysical loop (called the **van der Waals loop**) is replaced in reality by a horizontal tie line representing the liquid-gas phase transition, determined by the **Maxwell equal-area construction**.

The **critical point** is where the van der Waals equation makes its most elegant prediction. At the critical temperature and pressure, the distinction between liquid and gas vanishes. The van der Waals equation predicts critical constants in terms of a and b: T_c = 8a/(27Rb), P_c = a/(27b²), V_c = 3b. This gives a universal critical compressibility factor Z_c = P_cV_c/(RT_c) = 3/8 = 0.375 for all gases — a prediction of the **law of corresponding states**, which says that all gases behave similarly when expressed in reduced variables (P/P_c, V/V_c, T/T_c). Real gases have Z_c values ranging from about 0.23 to 0.29, so the van der Waals prediction is qualitatively right but quantitatively off.

For higher accuracy, you need more sophisticated equations of state. The **virial expansion** Z = 1 + B'/V + C'/V² + … systematically adds correction terms, where each virial coefficient captures interactions between pairs, triples, and higher-order clusters of molecules. The second virial coefficient B' is directly related to the intermolecular potential energy function — connecting macroscopic gas behavior to the microscopic forces you studied in your prerequisite on intermolecular potentials. The van der Waals equation can be recast as a truncated virial expansion, revealing that it captures pairwise interactions but neglects higher-order terms. For engineering applications, more flexible equations like the Redlich-Kwong, Peng-Robinson, or multi-parameter correlations provide the quantitative accuracy that van der Waals sacrifices for conceptual clarity.
