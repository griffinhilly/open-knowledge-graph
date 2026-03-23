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
stage: formal-systems
status: draft
---

# Arrhenius Equation and Temperature Dependence

## Core Idea
The Arrhenius equation k = A e^(-E_a/RT) connects rate constant to temperature via activation energy E_a and pre-exponential factor A. The exponential temperature dependence reflects the Boltzmann probability of achieving sufficient energy; small changes in T cause dramatic rate changes. The pre-exponential factor A incorporates entropy of activation and collision orientation effects.

## Questions

```yaml
- question: "Reaction A has Eₐ = 50 kJ/mol and Reaction B has Eₐ = 100 kJ/mol. Both start at 300 K and are heated to 310 K. Which reaction's rate constant increases by a larger factor?"
  type: multiple-choice
  options:
    - "Reaction A, because the lower barrier is easier to overcome with added energy"
    - "Reaction B, because higher activation energy makes the rate more sensitive to temperature"
    - "Both increase by the same factor because the temperature change is identical"
    - "Neither changes significantly because 10 K is too small a change"
  answer: 1
  explanation: "The Arrhenius equation shows that temperature sensitivity scales with Eₐ: in the exponential term −Eₐ/RT, a larger Eₐ means a larger fractional change in the exponent for a given ΔT. Mathematically, d(ln k)/dT = Eₐ/RT², so reactions with higher activation energies have a steeper ln(k) vs T slope. Reaction B will show a greater rate increase per degree. The common misconception (option A) imagines a lower barrier as 'easier to push over' — but it's the opposite: the high-Eₐ reaction is more starved of reactive collisions, so additional thermal energy proportionally helps it more."

- question: "In an Arrhenius plot of ln(k) versus 1/T, what does the slope of the best-fit line equal?"
  type: multiple-choice
  options:
    - "ln(A), the natural log of the pre-exponential factor"
    - "−Eₐ/R, which allows the activation energy to be calculated from the slope"
    - "Eₐ × R, giving the activation energy in units of J²·mol⁻²"
    - "The reaction rate order with respect to temperature"
  answer: 1
  explanation: "Taking the natural log of the Arrhenius equation gives ln(k) = ln(A) − (Eₐ/R)(1/T). Plotting ln(k) on the y-axis versus 1/T on the x-axis gives a line with slope = −Eₐ/R and y-intercept = ln(A). The slope is negative (faster reactions at higher T means higher k at lower 1/T). Multiplying the slope by −R gives Eₐ in J/mol. Option A is the y-intercept, not the slope."

- question: "A reaction with a low activation energy is more sensitive to temperature changes than a reaction with a high activation energy."
  type: true-false
  answer: false
  explanation: "This is a persistent misconception. The Arrhenius equation's exponential form means that high-Eₐ reactions are *more* sensitive to temperature. The derivative d(ln k)/dT = Eₐ/RT² shows sensitivity is proportional to Eₐ. Intuitively, a high-Eₐ reaction has few reactive collisions at low temperatures — a small increase in T shifts many more molecules above the threshold. A low-Eₐ reaction already has many reactive collisions, so adding more energy has a smaller proportional effect."

- question: "The pre-exponential factor A in the Arrhenius equation captures geometric and frequency factors independent of energy, and is approximately constant over moderate temperature ranges."
  type: true-false
  answer: true
  explanation: "A incorporates the collision frequency and the fraction of collisions with correct orientation for reaction — factors that depend weakly on temperature compared to the exponential term. Over a modest temperature range (say, 50–100 K), A is approximately constant, which is why plotting ln(k) vs 1/T gives a straight line. The dramatic temperature dependence of k comes from the e^(−Eₐ/RT) term, not from A."

- question: "Why does a 10°C temperature increase often double or triple a reaction rate, and why does the magnitude of this effect depend on the activation energy?"
  type: short-answer
  answer: "The Arrhenius equation's exponential term e^(−Eₐ/RT) represents the Boltzmann fraction of molecules with enough energy to react. Because the exponent contains temperature in the denominator, even a modest increase in T significantly enlarges this fraction. The effect is larger for high-Eₐ reactions because the exponent −Eₐ/RT changes more when Eₐ is large, meaning the fraction of reactive collisions grows faster per degree of heating."
  explanation: "A 10°C rule of thumb (rate doubling) applies to reactions with Eₐ around 50–60 kJ/mol at room temperature — coincidentally typical of many biochemical reactions. For Eₐ = 100 kJ/mol, the same 10°C increase would roughly quadruple the rate. Understanding this relationship is essential for designing experiments (choosing useful temperature ranges) and interpreting kinetic data (knowing what temperature control precision is needed)."
```

## Explainer

From your study of activation energy and reaction pathways, you know that reactions require molecules to overcome an energy barrier — only collisions with enough energy to reach the transition state lead to products. The **Arrhenius equation** puts this idea into a precise mathematical form: **k = A·e^(−Eₐ/RT)**, where k is the rate constant, A is the **pre-exponential factor**, Eₐ is the **activation energy**, R is the gas constant, and T is the absolute temperature in Kelvin.

The exponential term e^(−Eₐ/RT) is the heart of the equation. It represents the fraction of molecules in a Boltzmann distribution that have enough kinetic energy to surmount the activation barrier. At low temperatures, this fraction is tiny — most molecules lack sufficient energy, and the reaction is slow. As temperature rises, the exponential term grows rapidly because the Boltzmann distribution broadens, placing more molecules above the Eₐ threshold. This is why a modest temperature increase — say, 10°C — can double or triple a reaction rate. The sensitivity depends on Eₐ: reactions with high activation energies are dramatically more temperature-sensitive than those with low barriers, because the exponential amplifies the effect of Eₐ relative to RT.

The **pre-exponential factor A** captures everything that is not about energy: the frequency of collisions and the fraction of those collisions with the correct geometric orientation. A has units matching k (typically s⁻¹ or M⁻¹s⁻¹) and is often on the order of 10⁸–10¹³ s⁻¹ for unimolecular reactions. It is roughly constant over moderate temperature ranges, which is why the temperature dependence is dominated by the exponential term.

The most practical form of the Arrhenius equation comes from taking the natural logarithm: **ln(k) = ln(A) − Eₐ/RT**. This is a linear equation in 1/T — plotting ln(k) versus 1/T yields a straight line with slope −Eₐ/R and intercept ln(A). This **Arrhenius plot** is the standard method for extracting activation energies from experimental kinetic data. You measure the rate constant at several temperatures, plot ln(k) vs. 1/T, and read Eₐ directly from the slope. A two-point version, derived by subtracting the equation at two temperatures, gives ln(k₂/k₁) = (Eₐ/R)(1/T₁ − 1/T₂), which is useful for quick calculations when only two data points are available.
