---
id: maxwell-boltzmann-distribution-thermodynamics
title: Maxwell-Boltzmann Speed Distribution
domain: physics
course: thermodynamics
prerequisites:
- id: rms-speed-and-kinetic-energy
  type: hard
- id: normal-distribution-intro
  type: soft
- id: exponential-functions-and-graphs
  type: soft
- id: definite-integral-definition
  type: soft
tags:
- maxwell-boltzmann
- speed-distribution
- molecular-speeds
- probability-distribution
stage: formal-systems
status: validated
---

# Maxwell-Boltzmann Speed Distribution

## Core Idea
The Maxwell-Boltzmann distribution describes the probability distribution of molecular speeds in an ideal gas at thermal equilibrium. It predicts three characteristic speeds: the most probable speed v_p = √(2kT/m), the mean speed v_avg = √(8kT/πm), and the rms speed v_rms = √(3kT/m), with v_p < v_avg < v_rms. As temperature increases, the distribution broadens and shifts to higher speeds while the total area (probability) remains 1. The high-speed tail of the distribution is crucial for chemical reaction rates.

## How It's Best Learned
Sketch the distribution at two temperatures and identify each characteristic speed graphically. The broadening at high T explains why reaction rates are exponentially sensitive to temperature — even a small temperature increase significantly populates the high-energy tail.

## Common Misconceptions
- The Maxwell-Boltzmann distribution is not Gaussian (normal) — it is asymmetric with a longer high-speed tail.
- The most probable speed is not the average speed; these differ by a factor involving π.

## Explainer

From the rms speed formula v_rms = √(3kT/m), you know that the typical molecular speed in a gas depends on temperature and mass. But "typical" conceals a rich story — molecules in a gas do not all move at the same speed. The **Maxwell-Boltzmann distribution** answers the question: what fraction of molecules have speeds between v and v+dv? The answer is a probability distribution f(v) that combines the Boltzmann energy factor with a geometric counting factor, producing one of the most important results in thermodynamics.

The shape comes from two competing effects. The **Boltzmann factor** e^{−mv²/2kT} favors low speeds — molecules with less kinetic energy are exponentially more probable at thermal equilibrium. But **phase space** favors higher speeds — in 3D, the number of velocity vectors with magnitude between v and v+dv grows as the surface area of a sphere of radius v, which is 4πv². Multiplying these gives f(v) ∝ v² e^{−mv²/2kT}, a distribution that starts at zero (no molecules with zero speed), rises to a peak at the **most probable speed** v_p = √(2kT/m), and then falls off exponentially for large v. It is distinctly asymmetric: the high-speed tail is longer than a Gaussian of the same peak position, because the exponential decay doesn't cut off as sharply.

The three characteristic speeds tell slightly different things about the distribution. The **most probable speed** v_p = √(2kT/m) is the peak — the speed most likely for any single randomly chosen molecule. The **mean speed** v̄ = √(8kT/πm) is the arithmetic average — the factor of 8/π ≈ 0.85 versus 2 means v̄/v_p = √(4/π) ≈ 1.13. The **rms speed** v_rms = √(3kT/m), which you already know, is higher still because squaring before averaging gives extra weight to the high-speed tail. All three scale as √(T/m): hotter gases move faster, heavier molecules move slower — by the same square-root law.

The high-speed tail has consequences far out of proportion to the tiny fraction of molecules it represents. Chemical reactions require collisions above an activation energy E_a. The fraction of molecules with kinetic energy above E_a is proportional to e^{−E_a/kT} — the high-energy tail of the Maxwell-Boltzmann distribution. A temperature increase from 300 K to 310 K (only 3.3%) increases this fraction by a factor of e^{E_a·ΔT/kT²}. For a typical activation energy of ~50 kJ/mol, this is roughly a factor of 2 — explaining why reaction rates often double for every 10°C increase. The entire Arrhenius equation and the exponential sensitivity of reaction rates to temperature traces back to the shape of this tail. Similarly, evaporation — the escape of molecules from a liquid surface — depends on the fraction with enough energy to overcome surface tension, making the high-speed tail crucial for understanding phase transitions at the macroscopic level.
