---
id: arrhenius-equation-temperature-dependence
title: Arrhenius Equation and Temperature Dependence
domain: chemistry
course: physical-chemistry
prerequisites:
- id: activation-energy-catalysis-reaction-pathways
  type: hard
- id: integrated-rate-laws
  type: hard
builds-toward:
- diffusion-controlled-reaction-kinetics
tags:
- kinetics
- temperature-dependence
- activation-energy
stage: advanced
status: draft
---

# Arrhenius Equation and Temperature Dependence

## Core Idea
The Arrhenius equation k = A e^(-E_a/RT) connects rate constant to temperature via activation energy E_a and pre-exponential factor A. The exponential temperature dependence reflects the Boltzmann probability of achieving sufficient energy; small changes in T cause dramatic rate changes. The pre-exponential factor A incorporates entropy of activation and collision orientation effects.

## Explainer

From your study of activation energy and reaction pathways, you know that reactions require molecules to overcome an energy barrier — only collisions with enough energy to reach the transition state lead to products. The **Arrhenius equation** puts this idea into a precise mathematical form: **k = A·e^(−Eₐ/RT)**, where k is the rate constant, A is the **pre-exponential factor**, Eₐ is the **activation energy**, R is the gas constant, and T is the absolute temperature in Kelvin.

The exponential term e^(−Eₐ/RT) is the heart of the equation. It represents the fraction of molecules in a Boltzmann distribution that have enough kinetic energy to surmount the activation barrier. At low temperatures, this fraction is tiny — most molecules lack sufficient energy, and the reaction is slow. As temperature rises, the exponential term grows rapidly because the Boltzmann distribution broadens, placing more molecules above the Eₐ threshold. This is why a modest temperature increase — say, 10°C — can double or triple a reaction rate. The sensitivity depends on Eₐ: reactions with high activation energies are dramatically more temperature-sensitive than those with low barriers, because the exponential amplifies the effect of Eₐ relative to RT.

The **pre-exponential factor A** captures everything that is not about energy: the frequency of collisions and the fraction of those collisions with the correct geometric orientation. A has units matching k (typically s⁻¹ or M⁻¹s⁻¹) and is often on the order of 10⁸–10¹³ s⁻¹ for unimolecular reactions. It is roughly constant over moderate temperature ranges, which is why the temperature dependence is dominated by the exponential term.

The most practical form of the Arrhenius equation comes from taking the natural logarithm: **ln(k) = ln(A) − Eₐ/RT**. This is a linear equation in 1/T — plotting ln(k) versus 1/T yields a straight line with slope −Eₐ/R and intercept ln(A). This **Arrhenius plot** is the standard method for extracting activation energies from experimental kinetic data. You measure the rate constant at several temperatures, plot ln(k) vs. 1/T, and read Eₐ directly from the slope. A two-point version, derived by subtracting the equation at two temperatures, gives ln(k₂/k₁) = (Eₐ/R)(1/T₁ − 1/T₂), which is useful for quick calculations when only two data points are available.
