---
id: vapor-pressure-raoults-law
title: Vapor Pressure and Raoult's Law
domain: chemistry
course: general-chemistry
prerequisites:
- id: intermolecular-forces
  type: hard
- id: colligative-properties
  type: soft
builds-toward: []
tags:
- vapor-pressure
- Raoults-law
- ideal-solution
- positive-deviation
- negative-deviation
- volatile-solute
stage: advanced
status: draft
---
# Vapor Pressure and Raoult's Law

## Core Idea
Every liquid exerts a vapor pressure — the pressure of gas-phase molecules in equilibrium with the liquid surface — that increases with temperature and decreases with stronger intermolecular forces. Raoult's law states that the partial vapor pressure of each component in an ideal solution equals the product of its mole fraction and its pure-component vapor pressure: Pᵢ = χᵢPᵢ°. For non-volatile solutes, the total vapor pressure is simply lowered (vapor-pressure lowering is a colligative property). Real solutions show positive deviations (weaker solute-solvent interactions than pure components, higher vapor pressure) or negative deviations (stronger interactions, lower vapor pressure).

## How It's Best Learned
Calculate total vapor pressure over two-component solutions by summing partial pressures from Raoult's law. Compare ideal vs actual vapor pressure diagrams to identify positive and negative deviations and connect them to the relative strength of intermolecular forces between components.

## Common Misconceptions
- Raoult's law applies strictly to ideal solutions. Most real solutions deviate; Raoult's law is accurate mainly when the components are chemically similar (e.g., benzene and toluene).
- Vapor pressure lowering by a non-volatile solute depends on the number of solute particles, not their identity — an ionic solute that dissociates into two ions has roughly twice the effect of a molecular solute at the same molality.

## Questions

```yaml
- question: "Ethanol and hexane are mixed in equal mole fractions. Compared to what Raoult's law predicts, the observed total vapor pressure is higher. What best explains this positive deviation?"
  type: multiple-choice
  options:
    - "Mixing generates heat, which raises the temperature and therefore the vapor pressure above the predicted value"
    - "The ethanol-hexane interactions are weaker than the ethanol-ethanol and hexane-hexane self-interactions, so molecules escape the liquid more easily"
    - "Ethanol has a higher pure vapor pressure than hexane, pulling the mixture above Raoult's prediction"
    - "Positive deviations occur whenever both components are polar, because polarity increases volatility"
  answer: 1
  explanation: "Positive deviations arise when cross-interactions (solute-solvent) are WEAKER than self-interactions (solute-solute and solvent-solvent). Pure ethanol is held by hydrogen bonds; in hexane, ethanol loses those partners and the weaker London-dispersion interactions with hexane don't compensate — molecules escape more readily than predicted. Option A (heat of mixing) is related but doesn't directly explain the direction of the vapor pressure deviation. Option C misunderstands the law — Raoult's law already accounts for pure vapor pressures via mole fraction weighting. Option D is wrong; positive deviation is about weakened interactions, not polarity per se."

- question: "A solution contains benzene (mole fraction 0.4, P° = 75 mmHg) and toluene (mole fraction 0.6, P° = 25 mmHg). Assuming ideal behavior, what is the total vapor pressure above this solution?"
  type: multiple-choice
  options:
    - "50 mmHg — the simple average of the two pure vapor pressures"
    - "45 mmHg — calculated as (0.4 × 75) + (0.6 × 25)"
    - "75 mmHg — dominated by the more volatile component"
    - "100 mmHg — the sum of the two pure vapor pressures"
  answer: 1
  explanation: "Raoult's law: P_total = χ_A × P°_A + χ_B × P°_B = (0.4)(75) + (0.6)(25) = 30 + 15 = 45 mmHg. Each component contributes its partial pressure proportional to its mole fraction in the liquid. Option A (simple average) ignores the mole fraction weighting. Option C confuses the total pressure with the pure vapor pressure of the more volatile component. Option D would require the two pure vapor pressures to simply add, which would only be true if both components had mole fraction 1 simultaneously — impossible."

- question: "A non-volatile solute that dissociates into two ions will lower the vapor pressure of a solvent approximately twice as much as a non-dissociating solute at the same molality."
  type: true-false
  answer: true
  explanation: "Vapor pressure lowering is a colligative property — it depends on the number of solute particles, not their chemical identity. An ionic solute like NaCl dissociates into Na⁺ and Cl⁻, doubling the number of particles compared to a molecular solute at the same molality. Since more particles occupy surface sites and reduce the solvent's mole fraction, twice as many particles produce roughly twice the vapor pressure lowering. This same principle gives ionic solutes larger boiling point elevation and freezing point depression effects than molecular solutes at equal molality."

- question: "Raoult's law is accurate for any mixture of two liquids, as long as the mole fractions are correctly calculated."
  type: true-false
  answer: false
  explanation: "Raoult's law applies strictly to ideal solutions, where solute-solvent interactions are essentially identical to the self-interactions of each pure component. In practice, this requires chemically similar components (e.g., benzene and toluene, or hexane and heptane). Most real solutions deviate — positively when cross-interactions are weaker, negatively when they are stronger. The law is an approximation, not a universal rule; whether a mixture is 'ideal' always depends on the similarity of intermolecular forces between the components."

- question: "Acetone and chloroform form a solution with lower-than-expected vapor pressure (negative deviation from Raoult's law). Using intermolecular force reasoning, explain why."
  type: short-answer
  answer: "Acetone's carbonyl oxygen (C=O) accepts a hydrogen bond from chloroform's acidic C-H (made acidic by the three adjacent electronegative Cl atoms). This C-H···O=C cross-interaction is stronger than either pure component's self-interactions (acetone has only dipole-dipole; chloroform has only weak C-H interactions with itself). Stronger cross-interactions hold molecules in solution more tightly, reducing their tendency to escape into the vapor phase — lowering vapor pressure below Raoult's prediction."
  explanation: "The sign of the deviation is a direct readout of relative interaction strengths: stronger cross-interactions → negative deviation (lower vapor pressure than ideal); weaker cross-interactions → positive deviation (higher vapor pressure than ideal). Acetone-chloroform is the textbook example of a hydrogen-bond-driven negative deviation. This reasoning — compare cross-interactions to self-interactions — is the general rule for predicting deviation direction from intermolecular forces."
```

## Explainer

From your study of intermolecular forces, you know that molecules in a liquid are held together by attractive interactions — hydrogen bonds, dipole-dipole forces, or London dispersion forces. **Vapor pressure** is the pressure exerted by the gas-phase molecules that have escaped from a liquid surface into the space above it. At any temperature, some molecules at the surface have enough kinetic energy to overcome these attractions and enter the gas phase. When the rate of escape equals the rate of return, the system reaches a dynamic equilibrium, and the pressure of the vapor at that point is the liquid's vapor pressure. Liquids with weak intermolecular forces (like diethyl ether) have high vapor pressures because molecules escape easily; liquids with strong forces (like water) have lower vapor pressures.

**Raoult's law** describes what happens to vapor pressure when you mix two liquids (or dissolve a solute in a solvent). For an ideal solution, the partial vapor pressure of each component equals its mole fraction in the liquid multiplied by its pure-component vapor pressure: Pᵢ = χᵢPᵢ°. The intuition is simple — if only 70% of the surface molecules are solvent A, then A contributes only 70% of the vapor pressure it would have on its own. The total vapor pressure above the solution is the sum of the partial pressures of all volatile components. When you dissolve a non-volatile solute like sugar in water, the solute contributes zero vapor pressure, so the total vapor pressure drops. This **vapor-pressure lowering** depends only on how many solute particles are present (it is a colligative property), not on what the solute is.

Real solutions rarely obey Raoult's law perfectly, and the deviations reveal important chemistry. **Positive deviations** occur when solute-solvent interactions are weaker than the pure-component interactions — the molecules "want to escape" more readily than Raoult's law predicts, so the observed vapor pressure is higher than ideal. An example is ethanol mixed with hexane: ethanol loses its hydrogen-bonding partners, and the weaker ethanol-hexane interactions make both components more volatile. **Negative deviations** occur when solute-solvent interactions are unusually strong — the molecules are held more tightly in solution, and the observed vapor pressure is lower than predicted. Acetone mixed with chloroform is a classic case: a hydrogen bond forms between chloroform's C-H and acetone's C=O that neither pure liquid can form on its own.

Raoult's law is most accurate when the solution components are chemically similar — benzene and toluene, for instance, interact with each other almost identically to how they interact with themselves. As the components become more dissimilar, deviations grow larger. Recognizing whether a given mixture should show positive or negative deviation is a direct application of your intermolecular forces knowledge: compare the strength of the cross-interactions (solute-solvent) to the self-interactions (solute-solute and solvent-solvent). Stronger cross-interactions mean negative deviation; weaker cross-interactions mean positive deviation.
