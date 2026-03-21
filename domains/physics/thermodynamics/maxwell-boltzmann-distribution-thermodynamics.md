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

## Questions

```yaml
- question: "A gas sample is heated from 300 K to 1200 K (temperature quadrupled). By what factor does the most probable molecular speed increase?"
  type: multiple-choice
  options:
    - "It doubles, because most probable speed scales as the square root of temperature"
    - "It quadruples, because most probable speed scales linearly with temperature"
    - "It increases by a factor of 16, because kinetic energy scales as temperature squared"
    - "It stays the same — only the distribution broadens, the peak doesn't move"
  answer: 0
  explanation: "The most probable speed v_p = √(2kT/m) scales as √T. Quadrupling T multiplies v_p by √4 = 2. The common mistake (option B) is to confuse the linear T-dependence of average kinetic energy with the speed — since KE ∝ T and KE ∝ v², we get v ∝ √T, not v ∝ T. Option D is wrong because both the peak position and the width shift with temperature."

- question: "Which ordering correctly ranks the three characteristic speeds of the Maxwell-Boltzmann distribution?"
  type: multiple-choice
  options:
    - "v_p < v_avg < v_rms"
    - "v_avg < v_p < v_rms"
    - "v_rms < v_avg < v_p"
    - "All three are equal for an ideal gas at equilibrium"
  answer: 0
  explanation: "v_p (most probable) = √(2kT/m) < v_avg (mean) = √(8kT/πm) < v_rms = √(3kT/m). The rms speed is highest because squaring before averaging gives extra weight to the high-speed tail. The ratios v_p : v_avg : v_rms = 1 : 1.128 : 1.225. They would only be equal for a delta-function distribution, not the asymmetric Maxwell-Boltzmann."

- question: "The Maxwell-Boltzmann speed distribution is symmetric around the most probable speed — equal fractions of molecules have speeds above and below v_p."
  type: true-false
  answer: false
  explanation: "The distribution is distinctly asymmetric. It starts at zero (no molecules at zero speed), rises to a peak at v_p, then falls off with a longer tail at high speeds than at low speeds. This asymmetry arises because the geometric phase-space factor (∝ v²) pulls the distribution above zero at the peak, and the exponential Boltzmann factor decays but doesn't cut off as sharply as the low-speed side. More molecules have speeds above v_p than below it."

- question: "Even a small temperature increase can dramatically accelerate chemical reaction rates because the fraction of molecules above the activation energy threshold grows exponentially with temperature."
  type: true-false
  answer: true
  explanation: "The fraction of molecules with energy above E_a is proportional to e^(−E_a/kT) from the Boltzmann factor in the Maxwell-Boltzmann distribution. Because E_a appears in the exponent, a small ΔT produces a large multiplicative change in this fraction. For a typical activation energy of ~50 kJ/mol, heating from 300 K to 310 K roughly doubles the reactive fraction — explaining why reaction rates approximately double per 10°C. This exponential sensitivity underlies the Arrhenius equation."

- question: "Why is the high-speed tail of the Maxwell-Boltzmann distribution disproportionately important for chemical reaction rates, even though it represents a tiny fraction of all molecules?"
  type: short-answer
  answer: "Chemical reactions require collisions with energy above the activation energy E_a. Only molecules in the high-speed tail have enough kinetic energy to react. Because the fraction of molecules above E_a depends on e^(−E_a/kT), even a small increase in the tail population produces a large increase in reaction rate — the tail fraction changes exponentially with temperature while average speed changes only as √T."
  explanation: "This is the physical basis of the Arrhenius equation: k = A·e^(−E_a/kT). The pre-exponential factor A reflects collision frequency (which scales slowly with √T), but the exponential term reflects how the tail population changes. A reaction rate that doubles for every 10°C isn't about average speed increasing — average speed only increases by ~1.6% per 10°C at 300 K. It's entirely about the exponential sensitivity of the high-energy tail."
```

## Explainer

From the rms speed formula v_rms = √(3kT/m), you know that the typical molecular speed in a gas depends on temperature and mass. But "typical" conceals a rich story — molecules in a gas do not all move at the same speed. The **Maxwell-Boltzmann distribution** answers the question: what fraction of molecules have speeds between v and v+dv? The answer is a probability distribution f(v) that combines the Boltzmann energy factor with a geometric counting factor, producing one of the most important results in thermodynamics.

The shape comes from two competing effects. The **Boltzmann factor** e^{−mv²/2kT} favors low speeds — molecules with less kinetic energy are exponentially more probable at thermal equilibrium. But **phase space** favors higher speeds — in 3D, the number of velocity vectors with magnitude between v and v+dv grows as the surface area of a sphere of radius v, which is 4πv². Multiplying these gives f(v) ∝ v² e^{−mv²/2kT}, a distribution that starts at zero (no molecules with zero speed), rises to a peak at the **most probable speed** v_p = √(2kT/m), and then falls off exponentially for large v. It is distinctly asymmetric: the high-speed tail is longer than a Gaussian of the same peak position, because the exponential decay doesn't cut off as sharply.

The three characteristic speeds tell slightly different things about the distribution. The **most probable speed** v_p = √(2kT/m) is the peak — the speed most likely for any single randomly chosen molecule. The **mean speed** v̄ = √(8kT/πm) is the arithmetic average — the factor of 8/π ≈ 0.85 versus 2 means v̄/v_p = √(4/π) ≈ 1.13. The **rms speed** v_rms = √(3kT/m), which you already know, is higher still because squaring before averaging gives extra weight to the high-speed tail. All three scale as √(T/m): hotter gases move faster, heavier molecules move slower — by the same square-root law.

The high-speed tail has consequences far out of proportion to the tiny fraction of molecules it represents. Chemical reactions require collisions above an activation energy E_a. The fraction of molecules with kinetic energy above E_a is proportional to e^{−E_a/kT} — the high-energy tail of the Maxwell-Boltzmann distribution. A temperature increase from 300 K to 310 K (only 3.3%) increases this fraction by a factor of e^{E_a·ΔT/kT²}. For a typical activation energy of ~50 kJ/mol, this is roughly a factor of 2 — explaining why reaction rates often double for every 10°C increase. The entire Arrhenius equation and the exponential sensitivity of reaction rates to temperature traces back to the shape of this tail. Similarly, evaporation — the escape of molecules from a liquid surface — depends on the fraction with enough energy to overcome surface tension, making the high-speed tail crucial for understanding phase transitions at the macroscopic level.
