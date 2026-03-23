---
id: diffusion-coefficients-molecular-kinetics
title: Diffusion Coefficients and Kinetic Molecular Theory
domain: chemistry
course: physical-chemistry
prerequisites:
- id: transport-phenomena-gases
  type: hard
- id: kinetic-molecular-theory
  type: hard
builds-toward:
- viscosity-gas-liquid-transport
tags:
- diffusion
- transport
- kinetic-molecular
- coefficients
stage: formal-systems
status: draft
---

# Diffusion Coefficients and Kinetic Molecular Theory

## Core Idea
Diffusion is molecular transport driven by concentration gradients, obeying Fick's law: J = -D(∂c/∂x). The diffusion coefficient D reflects molecular size, mass, temperature, and intermolecular interactions. Kinetic molecular theory predicts D from collision frequency and mean free path; for gases, D ∝ T^(3/2)/σ. Experimental measurements of D reveal molecular dimensions and intermolecular force models.

## Questions

```yaml
- question: "A gas has a diffusion coefficient D at pressure P and temperature T. If the pressure is doubled while temperature is held constant, what happens to D?"
  type: multiple-choice
  options:
    - "D doubles, because more collisions carry molecules farther"
    - "D is halved, because the mean free path is halved by higher pressure"
    - "D is unchanged, because pressure doesn't affect molecular speed"
    - "D increases by T^(3/2), because temperature still dominates"
  answer: 1
  explanation: "From kinetic theory, D ≈ ⅓λū, where λ is the mean free path. Doubling pressure doubles the number density of molecules, which cuts the mean free path in half (molecules collide more frequently before traveling far). Average molecular speed ū is set by temperature and doesn't change. So D is halved. The common misconception is that more pressure means more 'push,' but diffusion is driven by concentration gradients and random walks, not bulk pressure."

- question: "Which gas would you expect to diffuse most rapidly through air at the same temperature and pressure?"
  type: multiple-choice
  options:
    - "Sulfur hexafluoride (SF₆, M = 146 g/mol), because it is a large molecule that sweeps more volume"
    - "Carbon dioxide (CO₂, M = 44 g/mol), because it is a common atmospheric gas"
    - "Hydrogen (H₂, M = 2 g/mol), because its high average speed and small cross-section give it the longest mean free path"
    - "Nitrogen (N₂, M = 28 g/mol), because it dominates air and equilibrates quickly"
  answer: 2
  explanation: "D ∝ T^(3/2)/(Pσ²√m): lighter molecules move faster and, if small, also have smaller collision cross-sections σ². H₂ is both the lightest molecule and physically tiny, giving it the highest average speed and longest mean free path. SF₆ is both heavy and geometrically large — a disastrous combination for diffusion. This is the physical basis of Graham's law of effusion."

- question: "In a liquid, the Stokes-Einstein equation D = k_BT/(6πηr) implies that a smaller solute molecule diffuses faster than a larger one, all else equal."
  type: true-false
  answer: true
  explanation: "The Stokes-Einstein equation shows D is inversely proportional to the hydrodynamic radius r: smaller r means larger D. This makes physical sense — a smaller molecule needs to push less solvent out of the way as it moves. The same logic applies to viscosity η: more viscous solvents slow diffusion. Both r and η appear in the denominator, so decreasing either increases D."

- question: "Diffusion is driven by molecules actively moving from high to low concentration in response to a chemical potential gradient, analogous to how a ball rolls downhill."
  type: true-false
  answer: false
  explanation: "Diffusion is driven by random thermal motion, not directed movement toward low concentration. Individual molecules have no 'awareness' of concentration gradients. The net flux toward lower concentration emerges statistically: in a region with many more molecules on one side than the other, random walks produce more crossings from the dense side to the sparse side simply because there are more molecules to cross. Fick's law J = −D(∂c/∂x) describes the macroscopic result of this statistical asymmetry, not a molecular driving force."

- question: "Why does increasing temperature increase the diffusion coefficient of a gas, while increasing pressure decreases it? What molecular-level mechanisms explain each effect?"
  type: short-answer
  answer: "Higher temperature increases the average molecular speed (ū ∝ √T) and also increases the mean free path slightly through reduced density at fixed volume, resulting in D ∝ T^(3/2). Higher pressure, at fixed temperature, increases the number density of molecules without changing their speed — this shortens the mean free path because molecules collide more frequently, reducing D ∝ 1/P. In short: temperature controls how fast molecules move between collisions; pressure controls how far they travel before the next collision."
  explanation: "The key is that D depends on both molecular speed (set by temperature) and mean free path (set by collision frequency, which depends on density/pressure). These two factors are controlled by different variables. Understanding this distinction — temperature affects kinetic energy, pressure affects collision frequency — is essential for predicting how D changes under different conditions."
```

## Explainer

From kinetic molecular theory, you know that gas molecules are in constant, random thermal motion — colliding with each other and with container walls billions of times per second. When a concentration gradient exists — say, a drop of perfume released in one corner of a room — this random motion gradually carries molecules from regions of high concentration to low concentration. This net transport is **diffusion**, and it occurs not because molecules "know" where to go, but because random walks statistically favor spreading out. **Fick's first law**, J = −D(∂c/∂x), formalizes this: the flux J (amount of substance crossing a unit area per unit time) is proportional to the concentration gradient, with the **diffusion coefficient** D as the proportionality constant.

The diffusion coefficient D has units of m²/s and encodes everything about how fast a particular species spreads through a given medium. Kinetic molecular theory lets you predict D from first principles for gases. A molecule that travels a long distance between collisions (large **mean free path** λ) and moves fast (high average speed ū) will diffuse quickly: D ≈ ⅓λū. Since the mean free path depends on molecular size (collision cross-section σ) and gas density, while the average speed depends on temperature and molecular mass, you can derive that D ∝ T^(3/2)/(Pσ²√m), where P is pressure and m is molecular mass. Heavier molecules diffuse more slowly; higher temperatures increase diffusion; higher pressures decrease it by shortening the mean free path.

These predictions connect beautifully to experimental observations. Graham's law of effusion — that lighter gases escape through small holes faster than heavier ones — is a direct consequence of the mass dependence of molecular speeds. Measuring D experimentally (for example, using a diffusion tube where two gases mix across a boundary) provides a way to extract effective molecular diameters and test intermolecular force models. If your measured D deviates from the hard-sphere prediction, the deviation reveals the softness of the repulsive potential or the strength of attractive interactions between molecules.

In liquids, diffusion is orders of magnitude slower because molecules are packed closely and must push past neighbors rather than flying freely between collisions. The **Stokes-Einstein equation**, D = k_BT/(6πηr), relates the diffusion coefficient in a liquid to the solvent viscosity η and the solute's hydrodynamic radius r. Despite the very different physical picture, the same conceptual framework applies: D measures how effectively random thermal energy translates into net molecular transport down a concentration gradient. Whether in gases, liquids, or across membranes, the diffusion coefficient remains the central quantitative handle on molecular mobility.
