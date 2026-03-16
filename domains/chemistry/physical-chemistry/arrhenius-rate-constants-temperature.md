---
id: arrhenius-rate-constants-temperature
title: Arrhenius Equation and Temperature Dependence of Rate Constants
domain: chemistry
course: physical-chemistry
prerequisites: []
builds-toward:
- pre-exponential-factor-collision-theory
- transition-state-theory
tags:
- arrhenius
- kinetics
- rate-constant
- temperature
stage: advanced
status: draft
---

# Arrhenius Equation and Temperature Dependence of Rate Constants

## Core Idea
The Arrhenius equation k = A exp(-Eₐ/RT) quantitatively relates rate constants to temperature through activation energy Eₐ. The pre-exponential factor A accounts for proper orientation and collision frequency. Plotting ln(k) vs 1/T gives a straight line, allowing experimental determination of Eₐ and A from kinetic data. Small changes in temperature cause exponential changes in rate constant, explaining how catalysts and temperature control reaction rates.

## Explainer

Every chemical reaction has a speed, and that speed changes dramatically with temperature. The **Arrhenius equation** — k = A exp(−Eₐ/RT) — captures this relationship in a single expression. Here, k is the rate constant, A is the **pre-exponential factor** (related to how often molecules collide with the right orientation), Eₐ is the **activation energy** (the minimum energy barrier reactants must overcome), R is the gas constant, and T is absolute temperature in Kelvin. The equation says that the rate constant grows exponentially as temperature rises or as activation energy falls.

The intuition behind the equation comes from thinking about molecular collisions. Not every collision between reactant molecules leads to a reaction — only those with enough kinetic energy to surmount the activation energy barrier and with the correct geometric orientation. At higher temperatures, molecules move faster, so a larger fraction of collisions carry enough energy to clear the barrier. The exponential term exp(−Eₐ/RT) represents exactly this fraction: it is the probability that a given collision has energy ≥ Eₐ. Because this fraction sits inside an exponential, even a modest temperature increase — say 10°C — can double or triple the rate constant for a reaction with a typical Eₐ of 50–100 kJ/mol.

The most practical tool derived from the Arrhenius equation is the **Arrhenius plot**. Taking the natural logarithm of both sides gives ln(k) = ln(A) − Eₐ/(RT), which has the form y = b + mx with y = ln(k) and x = 1/T. A plot of ln(k) versus 1/T should yield a straight line with slope −Eₐ/R and y-intercept ln(A). This means you can determine activation energy experimentally by measuring rate constants at several temperatures, plotting the data, and reading Eₐ directly from the slope. Steeper slopes mean higher activation energies; shallow slopes mean the reaction is relatively insensitive to temperature.

Understanding the Arrhenius equation also explains how **catalysts** work at a quantitative level. A catalyst provides an alternative reaction pathway with a lower Eₐ. Because Eₐ appears in the exponent, even a small reduction in activation energy produces a large increase in the rate constant. For example, reducing Eₐ by just 10 kJ/mol at 300 K increases the rate constant by roughly a factor of 50. This exponential sensitivity is why enzymes and industrial catalysts are so effective — they do not change the thermodynamics of the reaction (ΔG is unchanged), but by lowering the kinetic barrier, they make the reaction proceed fast enough to be useful.
