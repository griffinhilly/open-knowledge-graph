---
id: henrys-law-gas-solubility
title: Henry's Law and Gas Solubility
domain: chemistry
course: general-chemistry
prerequisites:
- id: partial-pressure-and-mole-fraction
  type: hard
- id: solution-concentration
  type: hard
builds-toward:
- solute-solvent-interactions-solvation
tags:
- henrys-law
- solubility
- gas
- pressure
stage: formal-systems
status: validated
---

# Henry's Law and Gas Solubility

## Core Idea
Henry's law states that the solubility of a gas is directly proportional to the partial pressure of that gas above the solution (at constant temperature). Increased pressure forces more gas molecules into solution; increased temperature decreases gas solubility by increasing molecular motion. This law applies to ideal solutions of gases.

## Questions

```yaml
- question: "A scuba diver breathes compressed air at depth where nitrogen has a partial pressure of 4 atm. At the surface, atmospheric nitrogen partial pressure is approximately 0.8 atm. According to Henry's law, what happens to the nitrogen dissolved in the diver's blood when they ascend?"
  type: multiple-choice
  options:
    - "It remains dissolved — nitrogen is permanently trapped in the bloodstream once absorbed"
    - "It is rapidly exhaled as the lungs exchange nitrogen gas with the atmosphere"
    - "Its equilibrium solubility drops to about 20% of the depth value, so excess dissolved nitrogen tends to come out of solution"
    - "Nothing changes — blood plasma is not an ideal solution, so Henry's law does not apply to biological fluids"
  answer: 2
  explanation: "Henry's law (C = kH × P) tells us the equilibrium dissolved concentration is proportional to partial pressure. At 4 atm, the equilibrium concentration is 5× higher than at 0.8 atm. When the diver surfaces, the equilibrium concentration drops to 20% of its at-depth value, so the blood is supersaturated — it holds far more dissolved nitrogen than the new pressure can sustain. If ascent is too fast, nitrogen comes out of solution as bubbles in tissues and blood, causing decompression sickness (the bends)."

- question: "A factory dissolves CO₂ into water at 5°C under elevated pressure. An engineer proposes switching to 50°C water to dissolve more CO₂ per unit time. What is the fundamental error in this reasoning?"
  type: multiple-choice
  options:
    - "CO₂ reacts with warm water to form carbonic acid, which corrodes the equipment"
    - "Higher pressure would be required at 50°C to achieve the same flow rate, increasing energy costs"
    - "Gas solubility decreases with increasing temperature, so warm water would dissolve less CO₂ than cold water at the same pressure"
    - "At 50°C, CO₂ transitions to a supercritical state and Henry's law no longer applies"
  answer: 2
  explanation: "Unlike most solids, gases become less soluble as temperature rises. Higher temperature gives dissolved gas molecules more kinetic energy, making them more likely to escape the liquid back into the gas phase. The equilibrium shifts toward less dissolved gas. This is the opposite of what the engineer assumed. Cold water is deliberately used in carbonation precisely because it holds more CO₂ at a given pressure — and why warm soda goes flat faster than cold soda."

- question: "A gas that reacts chemically with water (such as HCl or NH₃) will dissolve in greater quantities than Henry's law alone predicts."
  type: true-false
  answer: true
  explanation: "Henry's law predicts dissolved concentration based on equilibrium between gas-phase and dissolved-phase molecules. When a gas reacts with water (e.g., HCl → H⁺ + Cl⁻; NH₃ + H₂O → NH₄⁺ + OH⁻), the dissolved molecules are consumed by the chemical reaction and converted to ions, removing them from the dissolved equilibrium. This continuously pulls more gas into solution beyond what the pressure-based equilibrium would predict. The total amount dissolved (as ions plus molecules) greatly exceeds Henry's law predictions, which is why HCl is described as deviating from ideal Henry's law behavior."

- question: "Henry's law states that gas solubility is proportional to total atmospheric pressure, so at high altitude (where total pressure is lower), most dissolved gases in water should be equally reduced."
  type: true-false
  answer: false
  explanation: "Henry's law concerns the partial pressure of the specific gas in question, not total atmospheric pressure. At high altitude, total pressure is lower, but the key quantity for each gas is its own partial pressure (determined by its mole fraction times total pressure). The partial pressure of O₂ at altitude is lower, reducing dissolved oxygen in water — but this is because O₂'s partial pressure dropped, not because total pressure dropped uniformly. Gases whose partial pressures are maintained (e.g., by a pressurized system) are unaffected regardless of ambient atmospheric pressure."

- question: "Explain using Henry's law why a sealed soda bottle stays carbonated at room temperature but goes flat within hours of being opened."
  type: short-answer
  answer: "In a sealed bottle, the CO₂ above the liquid is at high pressure (2–4 atm), and Henry's law predicts a correspondingly high equilibrium dissolved CO₂ concentration. The system is at equilibrium: the rate of CO₂ escaping the liquid equals the rate of CO₂ dissolving back in. When the bottle is opened, the partial pressure of CO₂ above the liquid plummets to atmospheric CO₂ partial pressure (~0.0004 atm). Henry's law now predicts a much lower equilibrium dissolved concentration — the liquid is supersaturated. CO₂ escapes as bubbles until the dissolved concentration reaches the new, much lower equilibrium value, at which point the soda is flat."
  explanation: "The key insight is that Henry's law governs equilibrium: the dissolved concentration adjusts to match whatever partial pressure exists above the solution. Changing the headspace pressure (by opening the bottle) immediately changes what the equilibrium concentration should be, and the system then relaxes toward that new equilibrium by releasing dissolved gas."
```

## Explainer

From Dalton's law and the concept of partial pressure, you know that each gas in a mixture exerts its own pressure independently, proportional to its mole fraction. **Henry's law** extends this idea to the liquid phase: the amount of gas that dissolves in a liquid is directly proportional to the partial pressure of that gas above the liquid. The mathematical expression is simple: C = kH × P, where C is the concentration of dissolved gas, P is the partial pressure of the gas above the solution, and kH is the **Henry's law constant** — a value specific to each gas-solvent pair at a given temperature.

The physical picture is straightforward. Gas molecules are constantly striking the liquid surface. Some bounce off; some penetrate and dissolve. At the same time, dissolved gas molecules near the surface escape back into the gas phase. At equilibrium, the rate of dissolution equals the rate of escape. If you increase the partial pressure of the gas — by pumping more gas into the space above the liquid — more molecules strike the surface per second, and more dissolve until a new, higher equilibrium concentration is reached. Double the pressure, double the dissolved concentration. This linear relationship is Henry's law.

The most familiar example is carbonated beverages. Carbon dioxide is dissolved in soda under high pressure (typically 2–4 atmospheres of CO₂). When you open the bottle, the partial pressure of CO₂ above the liquid drops to atmospheric levels (about 0.0004 atm), and Henry's law predicts a dramatic decrease in solubility. The excess dissolved CO₂ comes out of solution as bubbles — that is the fizz. If you leave the bottle open, it eventually goes flat as dissolved CO₂ equilibrates with the tiny partial pressure of CO₂ in the atmosphere. Divers encounter the same principle: at depth, the elevated pressure causes more nitrogen to dissolve in blood. Rising too quickly drops the pressure faster than nitrogen can leave the blood gradually, forming bubbles that cause decompression sickness (the bends).

Temperature works against gas solubility — unlike most solids, gases become *less* soluble as temperature rises. Higher temperature gives dissolved gas molecules more kinetic energy, making them more likely to escape the liquid. This is why a warm soda goes flat faster than a cold one, and why aquatic organisms can be stressed by warm water that holds less dissolved oxygen. Henry's law applies best to dilute solutions of gases that do not react chemically with the solvent. Gases like HCl or NH₃ that react extensively with water deviate from Henry's law because the chemical reaction removes dissolved gas, pulling more into solution than pressure alone would predict.
