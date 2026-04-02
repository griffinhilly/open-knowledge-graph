---
id: transport-phenomena-gases
title: Transport Properties of Gases
domain: chemistry
course: physical-chemistry
prerequisites:
- id: kinetic-theory-of-gases
  type: hard
- id: maxwell-boltzmann-distribution
  type: hard
- id: rms-speed-and-kinetic-energy
  type: soft
- id: intermolecular-potential-models
  type: soft
builds-toward:
- diffusion-and-ficks-laws
tags:
- viscosity
- thermal-conductivity
- diffusion
- mean-free-path
- collision-diameter
stage: expert
status: validated
---
# Transport Properties of Gases

## Core Idea
Transport properties describe how momentum (viscosity), energy (thermal conductivity), and matter (diffusion) move through gases. All three are governed by molecular collisions characterized by the mean free path λ = 1/(√2·π·d²·N/V) and the mean speed c̄ = (8kT/πm)^(1/2). Viscosity η = (1/3)ρc̄λ increases with temperature as √T (unlike liquids), because faster molecules carry momentum more effectively even as the mean free path shortens. Thermal conductivity κ = (1/3)ρc̄λC_V/M is proportional to η. Chapman-Enskog theory provides more accurate expressions using Lennard-Jones collision integrals that account for the real intermolecular potential.

## How It's Best Learned
Verify the √T temperature dependence of gas viscosity from kinetic theory, then compare to experimental data for N₂ and Ar. Observe that the predicted (η₁/η₂) = (m₁/m₂)^(1/2) mass ratio is approximately correct for isomers.

## Common Misconceptions
- Expecting gas viscosity to decrease with temperature (as liquids do); gas viscosity increases with T because momentum transport improves.
- Thinking all transport coefficients are independent; they are all related through the same mean free path and speed.

## Questions

```yaml
- question: "You measure the viscosity of nitrogen gas at 300 K, then again at 1200 K (a factor-of-4 increase in absolute temperature). What do you expect to observe, and why?"
  type: multiple-choice
  options:
    - "Viscosity decreases by roughly half — higher temperature means faster molecules that disrupt ordered flow more chaotically"
    - "Viscosity is unchanged — the mean free path shortens in exactly the proportion the speed increases"
    - "Viscosity roughly doubles (increases by ~√4) — faster molecules transport momentum across velocity gradients more effectively"
    - "Viscosity increases fourfold — viscosity scales directly with absolute temperature in gases"
  answer: 2
  explanation: "Gas viscosity scales as √T from kinetic theory: η ∝ √T. At 4× the temperature, viscosity increases by √4 = 2×. This contradicts liquid behavior, where viscosity decreases with temperature. In gases, there are no intermolecular attractions to weaken — faster molecules simply carry momentum more effectively across a velocity gradient. Option A describes the liquid case; option D overestimates by confusing √T with T."

- question: "Thermal conductivity (κ) of an ideal gas is proportional to its viscosity (η). Which statement best explains why?"
  type: multiple-choice
  options:
    - "Both properties increase with temperature, so they must be proportional to each other"
    - "Both properties arise from the same microscopic mechanism — molecules traveling a mean free path and carrying a quantity (momentum or energy) between collisions — differing only in what is transported"
    - "They are related because denser gases have both higher viscosity and higher thermal conductivity"
    - "The proportionality is empirical and has no theoretical explanation from kinetic theory"
  answer: 1
  explanation: "The formulas make the connection explicit: η = (1/3)ρc̄λ and κ = (1/3)ρc̄λC_V/M. Both contain the same ρ, c̄, and λ; the only difference is that κ includes the heat capacity per unit mass C_V/M because thermal conductivity transports kinetic energy while viscosity transports momentum. This proportionality is a theoretical prediction, not just an empirical coincidence, and it follows directly from the unified mean-free-path picture of gas transport."

- question: "In an ideal gas, viscosity and thermal conductivity both depend on the same mean free path (λ) and mean molecular speed (c̄)."
  type: true-false
  answer: true
  explanation: "True. The kinetic theory expressions η = (1/3)ρc̄λ and κ = (1/3)ρc̄λC_V/M share the same c̄λ product. Both properties arise because molecules travel on average a distance λ before colliding, carrying whatever macroscopic quantity varies spatially (momentum for viscosity, kinetic energy for thermal conductivity). Diffusion also shares this structure: D = (1/3)c̄λ. The unified mean-free-path picture is the central insight of gas transport theory."

- question: "Like liquids, gases become less viscous when heated, because higher kinetic energy disrupts the intermolecular interactions that cause resistance to flow."
  type: true-false
  answer: false
  explanation: "False — this is the most common misconception in gas transport. Gas viscosity INCREASES with temperature. Gases have negligible intermolecular attractions, so there are no cohesive interactions to disrupt. Instead, gas viscosity arises purely from molecular momentum transfer: faster molecules (higher T) traverse the mean free path more quickly and carry more momentum per molecule, making momentum transport across a velocity gradient more efficient. The result is η ∝ √T. The liquid mechanism described in the question simply does not apply to gases."

- question: "Why does gas viscosity increase with temperature while liquid viscosity decreases? Explain the different mechanisms responsible."
  type: short-answer
  answer: "In liquids, viscosity arises from intermolecular cohesion — molecules must overcome attractive forces to flow past neighbors, and thermal energy reduces these effective energy barriers, so viscosity drops as T rises. In gases, intermolecular attractions are negligible; viscosity arises entirely from momentum transfer between layers. Molecules randomly crossing from a fast-moving layer to a slower one carry excess momentum, dragging the layers toward the same speed. Faster molecules (higher T) traverse the mean free path more quickly and carry more momentum, so viscous coupling between layers strengthens with temperature. The net result is η ∝ √T for ideal gases."
  explanation: "The key is recognizing that liquid and gas viscosity have fundamentally different physical origins. Liquid viscosity is about overcoming attraction; gas viscosity is about collisional momentum transfer. This also explains why adding a noble gas to a mixture affects viscosity even though noble gases have essentially no intermolecular attractions — what matters is their mass and speed, not their chemistry."
```

## Explainer

From kinetic theory, you know that gas molecules are in constant random motion, colliding with each other billions of times per second. Transport properties describe what happens when this random motion carries something — momentum, energy, or molecules themselves — from one region of the gas to another. The unifying idea is that each transport property arises from the same microscopic mechanism: molecules traveling an average distance λ (the **mean free path**) between collisions, carrying with them whatever macroscopic quantity varies across space.

Consider **viscosity** first. Imagine two parallel layers of gas moving at different speeds, like cards sliding over each other. Molecules randomly crossing between layers carry momentum from the faster layer to the slower one, effectively dragging the slow layer forward and the fast layer back. This molecular momentum transfer is viscosity. The kinetic theory result η = (1/3)ρc̄λ makes physical sense: viscosity increases with density ρ (more carriers), mean speed c̄ (faster delivery), and mean free path λ (each molecule carries momentum further before surrendering it in a collision). The counterintuitive prediction is the temperature dependence. In liquids, viscosity drops with temperature because thermal energy helps molecules overcome intermolecular attractions. In gases, there are no such attractions to overcome — instead, higher temperature means faster molecules that transport momentum more effectively. Since c̄ ∝ √T and λ also changes with T, the net result is that gas viscosity increases as √T.

**Thermal conductivity** κ follows the same logic, but now molecules carry kinetic energy rather than momentum across a temperature gradient. The formula κ = (1/3)ρc̄λC_V/M shows that thermal conductivity is essentially viscosity multiplied by the specific heat capacity per unit mass. This proportionality between η and κ is not a coincidence — both properties originate from the same collision dynamics, differing only in what quantity is being transported. **Diffusion** completes the triad: when a concentration gradient exists, random molecular motion produces a net flux of molecules from high to low concentration. The self-diffusion coefficient D = (1/3)c̄λ depends on the same mean speed and mean free path but not on density, because diffusion measures how fast individual molecules spread rather than how much momentum or energy the bulk gas transfers.

The simple kinetic theory expressions are approximate because they treat molecules as hard spheres with a fixed collision diameter. Real molecules interact through softer potentials — they attract at long range and repel sharply at short range, as described by the Lennard-Jones potential you encountered in intermolecular force models. **Chapman-Enskog theory** incorporates these realistic potentials through temperature-dependent collision integrals Ω, which account for the fact that glancing collisions at high relative velocity are less deflected than slow head-on ones. The resulting expressions predict transport properties to within a few percent of experimental values and correctly capture features that hard-sphere theory misses, such as the stronger-than-√T temperature dependence observed in real gases.
