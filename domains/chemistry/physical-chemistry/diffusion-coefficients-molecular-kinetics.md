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
stage: advanced
status: draft
---

# Diffusion Coefficients and Kinetic Molecular Theory

## Core Idea
Diffusion is molecular transport driven by concentration gradients, obeying Fick's law: J = -D(∂c/∂x). The diffusion coefficient D reflects molecular size, mass, temperature, and intermolecular interactions. Kinetic molecular theory predicts D from collision frequency and mean free path; for gases, D ∝ T^(3/2)/σ. Experimental measurements of D reveal molecular dimensions and intermolecular force models.

## Explainer

From kinetic molecular theory, you know that gas molecules are in constant, random thermal motion — colliding with each other and with container walls billions of times per second. When a concentration gradient exists — say, a drop of perfume released in one corner of a room — this random motion gradually carries molecules from regions of high concentration to low concentration. This net transport is **diffusion**, and it occurs not because molecules "know" where to go, but because random walks statistically favor spreading out. **Fick's first law**, J = −D(∂c/∂x), formalizes this: the flux J (amount of substance crossing a unit area per unit time) is proportional to the concentration gradient, with the **diffusion coefficient** D as the proportionality constant.

The diffusion coefficient D has units of m²/s and encodes everything about how fast a particular species spreads through a given medium. Kinetic molecular theory lets you predict D from first principles for gases. A molecule that travels a long distance between collisions (large **mean free path** λ) and moves fast (high average speed ū) will diffuse quickly: D ≈ ⅓λū. Since the mean free path depends on molecular size (collision cross-section σ) and gas density, while the average speed depends on temperature and molecular mass, you can derive that D ∝ T^(3/2)/(Pσ²√m), where P is pressure and m is molecular mass. Heavier molecules diffuse more slowly; higher temperatures increase diffusion; higher pressures decrease it by shortening the mean free path.

These predictions connect beautifully to experimental observations. Graham's law of effusion — that lighter gases escape through small holes faster than heavier ones — is a direct consequence of the mass dependence of molecular speeds. Measuring D experimentally (for example, using a diffusion tube where two gases mix across a boundary) provides a way to extract effective molecular diameters and test intermolecular force models. If your measured D deviates from the hard-sphere prediction, the deviation reveals the softness of the repulsive potential or the strength of attractive interactions between molecules.

In liquids, diffusion is orders of magnitude slower because molecules are packed closely and must push past neighbors rather than flying freely between collisions. The **Stokes-Einstein equation**, D = k_BT/(6πηr), relates the diffusion coefficient in a liquid to the solvent viscosity η and the solute's hydrodynamic radius r. Despite the very different physical picture, the same conceptual framework applies: D measures how effectively random thermal energy translates into net molecular transport down a concentration gradient. Whether in gases, liquids, or across membranes, the diffusion coefficient remains the central quantitative handle on molecular mobility.
