---
id: partial-pressure-and-mole-fraction
title: Dalton's Law of Partial Pressures
domain: chemistry
course: general-chemistry
prerequisites:
- id: gas-pressure-from-kinetic-theory
  type: hard
- id: gas-stoichiometry
  type: soft
builds-toward:
- henrys-law-gas-solubility
tags:
- partial-pressure
- daltons-law
- gas-mixtures
- mole-fraction
stage: formal-systems
status: validated
---

# Dalton's Law of Partial Pressures

## Core Idea
In a gas mixture, each gas exerts its own partial pressure as if it occupied the container alone; total pressure is the sum of all partial pressures. Partial pressure of a gas equals its mole fraction times the total pressure. This principle explains vapor pressure above solutions and gas collection over water.

## Questions

```yaml
- question: "At high altitude where total atmospheric pressure is 0.50 atm, air still contains 21% oxygen by moles. A climber measures the partial pressure of O₂. What is it, and why is this clinically significant?"
  type: multiple-choice
  options:
    - "0.21 atm — the same as at sea level, since the mole fraction is unchanged"
    - "0.42 atm — doubling because less total gas is present"
    - "0.105 atm — half the sea-level value, because partial pressure scales with total pressure"
    - "0.21 atm, but it acts differently at altitude because of lower air density"
  answer: 2
  explanation: "P_O₂ = χ_O₂ × P_total = 0.21 × 0.50 atm = 0.105 atm — exactly half the sea-level value of ~0.21 atm. The mole fraction is unchanged, but oxygen availability to biological systems depends on partial pressure, not mole fraction. At lower partial pressure, less oxygen dissolves in blood plasma and less is available to bind hemoglobin. This is why altitude sickness occurs even though the air is 'still 21% oxygen' — the common misconception that something about the air's composition changes at altitude. The composition is the same; the partial pressure is what drives gas exchange."

- question: "Hydrogen gas is collected by water displacement in an inverted bottle. The total pressure inside equals atmospheric pressure (1.00 atm) and water vapor pressure at the experiment temperature is 0.031 atm. What is the partial pressure of dry hydrogen gas?"
  type: multiple-choice
  options:
    - "1.031 atm — adding the water vapor to atmospheric pressure"
    - "0.969 atm — subtracting the water vapor pressure from total pressure"
    - "1.00 atm — the water vapor is negligible and can be ignored"
    - "0.031 atm — only the water vapor needs to be measured directly"
  answer: 1
  explanation: "By Dalton's law, P_total = P_H₂ + P_H₂O. So P_H₂ = P_total − P_H₂O = 1.00 − 0.031 = 0.969 atm. The collected gas is a mixture: any gas sample collected over water includes water vapor at its equilibrium vapor pressure for that temperature. This water vapor contributes to total pressure, so it must be subtracted to find the pure gas pressure. Failing to account for water vapor pressure is a common source of error in stoichiometry calculations involving gas collection."

- question: "At high altitude, the percentage of oxygen in the atmosphere decreases compared to sea level, which is why climbers experience hypoxia."
  type: true-false
  answer: false
  explanation: "The mole fraction (percentage) of oxygen in dry air is approximately 21% at all altitudes — it does not decrease. What decreases is the total atmospheric pressure (and therefore the partial pressure of oxygen). Since P_O₂ = χ_O₂ × P_total, halving total pressure halves P_O₂ even if χ_O₂ stays constant. Hypoxia at altitude results from reduced partial pressure, not reduced percentage. This distinction matters: supplemental oxygen works by increasing total pressure available to the lungs (in pressure masks) or by increasing χ_O₂ to nearly 1.0 in the supplied gas, both of which restore adequate P_O₂."

- question: "If the mole fraction of nitrogen in a gas mixture is 0.78 and the total pressure is 1.00 atm, then the partial pressure of nitrogen is 0.78 atm."
  type: true-false
  answer: true
  explanation: "Directly from Dalton's law: P_A = χ_A × P_total = 0.78 × 1.00 atm = 0.78 atm. This relationship is the quantitative backbone of the topic. Note that all mole fractions must sum to 1, so the remaining 0.22 atm of pressure is contributed by other gases in the mixture. The relationship P_A = χ_A × P_total follows from the ideal gas law: if n_A/n_total = χ_A, and P ∝ n at constant V and T, then P_A/P_total = χ_A."

- question: "A scuba diver breathing normal air (21% O₂, 78% N₂) at 30 meters depth, where total pressure is approximately 4 atm, experiences increased dissolved nitrogen in the blood. Explain why, even though the composition of the air supply has not changed."
  type: short-answer
  answer: "At 4 atm total pressure, P_N₂ = 0.78 × 4 atm = 3.12 atm — four times the sea-level value of ~0.78 atm. By Henry's law (which you will study next), the amount of a gas that dissolves in a liquid is proportional to its partial pressure. So even though the air is still 78% nitrogen, the much higher partial pressure of nitrogen drives far more nitrogen into dissolution in the diver's blood and tissues. This is why decompression sickness (the bends) occurs: ascending too quickly causes dissolved nitrogen to come out of solution as bubbles."
  explanation: "This problem illustrates the chain from Dalton's law to Henry's law: composition (mole fraction) is fixed, total pressure increases with depth, partial pressure = mole fraction × total pressure increases, and dissolved gas content scales with partial pressure. The diver's air supply remains 21%/78%, but the effective 'dose' of each gas increases with depth because partial pressures increase. This is why gas management at depth is critical in diving medicine."
```

## Explainer

From kinetic molecular theory, you know that gas pressure results from molecules colliding with container walls. In a mixture of gases — say, nitrogen and oxygen in a flask — each type of molecule bounces off the walls independently of the others. Nitrogen molecules do not "know" oxygen is present, and vice versa. **Dalton's law of partial pressures** formalizes this insight: the total pressure of a gas mixture equals the sum of the individual **partial pressures**, where each gas's partial pressure is the pressure it would exert if it alone occupied the entire container. Mathematically: P_total = P₁ + P₂ + P₃ + ...

The bridge between partial pressure and composition is the **mole fraction** (χ). The mole fraction of gas A in a mixture is simply the moles of A divided by the total moles of all gases: χ_A = n_A / n_total. Because pressure is proportional to the number of moles (from the ideal gas law, PV = nRT), the partial pressure of gas A is its mole fraction times the total pressure: P_A = χ_A × P_total. If air is 78% nitrogen by moles and atmospheric pressure is 1.00 atm, then the partial pressure of nitrogen is 0.78 × 1.00 = 0.78 atm. Note that all mole fractions in a mixture must sum to 1, and all partial pressures must sum to the total pressure — these are useful checks on your arithmetic.

A classic application is **collecting a gas over water**. When you produce hydrogen gas in a reaction and collect it by displacing water in an inverted bottle, the gas in the bottle is not pure hydrogen — it is a mixture of hydrogen and water vapor. The total pressure inside the bottle (equal to atmospheric pressure) is the sum of the partial pressure of hydrogen and the **vapor pressure of water** at the experimental temperature. To find the partial pressure of the dry hydrogen, you subtract the water's vapor pressure (looked up in a table) from the total: P_H₂ = P_total − P_H₂O. From there, you can use the ideal gas law with the partial pressure of hydrogen alone to calculate the moles of H₂ collected.

Dalton's law appears throughout chemistry and beyond. In respiratory physiology, the partial pressure of oxygen decreases at high altitude because total atmospheric pressure drops — even though the mole fraction of O₂ remains 21%. This is why climbers need supplemental oxygen. In scuba diving, increased total pressure at depth raises the partial pressure of nitrogen, increasing the amount that dissolves in blood — a direct setup for Henry's law, which you will study next. Mastering the relationship between mole fraction, partial pressure, and total pressure gives you a versatile tool for any situation involving gas mixtures.
