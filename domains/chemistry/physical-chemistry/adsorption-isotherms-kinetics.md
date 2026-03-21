---
id: adsorption-isotherms-kinetics
title: Adsorption Isotherms and Kinetics
domain: chemistry
course: physical-chemistry
prerequisites:
- id: adsorption-isotherms-advanced
  type: hard
- id: surface-thermodynamics-adsorption
  type: soft
tags:
- adsorption
- isotherms
- kinetics
- catalysis
stage: advanced
status: draft
---

# Adsorption Isotherms and Kinetics

## Core Idea
Langmuir, Freundlich, and BET isotherms model how adsorbate coverage changes with pressure or concentration at constant T. Langmuir assumes monolayer adsorption with a single binding site type; BET extends to multilayers. Kinetics involve forward adsorption (collision/activation limited) and reverse desorption (Arrhenius-like). Together, isotherms and kinetics characterize adsorbent capacity, selectivity, and rates for separations and catalysis.

## Questions

```yaml
- question: "A Langmuir adsorption isotherm shows that surface coverage θ approaches 1.0 asymptotically at high pressure. What physical assumption produces this saturation behavior?"
  type: multiple-choice
  options:
    - "Adsorption sites become more energetically favorable as pressure increases"
    - "The surface has a finite number of equivalent, independent sites that each accommodate only one adsorbate molecule"
    - "At high pressure, adsorbate molecules stack into multiple layers above the first"
    - "Surface area decreases as coverage increases, limiting further adsorption"
  answer: 1
  explanation: "The Langmuir saturation ceiling arises directly from the monolayer assumption: there are only so many binding sites, each can be occupied once, and all sites are equivalent. As pressure rises, more sites fill, but θ can never exceed 1 (100% coverage). This is mathematically analogous to enzyme kinetics (Michaelis-Menten) for the same reason — both describe a saturable process. Option C describes what the BET isotherm models, not Langmuir."

- question: "Catalyst A binds oxygen with very high adsorption energy; Catalyst B binds oxygen very weakly. In an oxidation reaction that requires surface oxygen, which catalyst shows higher activity?"
  type: multiple-choice
  options:
    - "Catalyst A, because strong binding ensures maximum surface coverage at all times"
    - "Catalyst B, because weak binding lets the reaction proceed faster"
    - "Neither extreme; a catalyst with intermediate binding energy sits at the volcano plot peak, balancing coverage against desorption rate"
    - "Catalyst A, because higher surface coverage always means more product"
  answer: 2
  explanation: "This is the Sabatier principle. Catalyst A binds so strongly that products cannot desorb — the surface stays covered but the active sites are blocked. Catalyst B binds so weakly that reactants never accumulate to meaningful coverage. The optimal catalyst sits at the peak of the volcano plot: strong enough binding to achieve useful coverage, weak enough to release products promptly. Options A and D ignore the desorption half of the kinetic cycle."

- question: "The Freundlich isotherm predicts a maximum surface coverage (saturation), just like the Langmuir isotherm — it simply reaches that maximum more gradually."
  type: true-false
  answer: false
  explanation: "The Freundlich isotherm (θ ∝ P^(1/n)) is empirical and has no saturation limit — it predicts continuously increasing coverage with increasing pressure, which is physically unrealistic at high pressures. This is a known limitation. Langmuir achieves saturation via its explicit monolayer assumption and finite site count; Freundlich lacks this and fits heterogeneous surfaces well only over intermediate pressure ranges."

- question: "At adsorption equilibrium, the rate of adsorption equals the rate of desorption, and this kinetic balance mathematically recovers the Langmuir isotherm."
  type: true-false
  answer: true
  explanation: "Setting the adsorption rate (proportional to P × (1 − θ)) equal to the desorption rate (proportional to θ) and solving for θ yields θ = KP/(1 + KP) — exactly the Langmuir isotherm, where K = k_ads/k_des. This is a satisfying self-consistency check: the equilibrium isotherm and the kinetic rate equations are two faces of the same physical model."

- question: "Explain why a catalyst that binds its reactants too strongly is ineffective, using the kinetics of adsorption and desorption."
  type: short-answer
  answer: "If adsorption energy is very high, the desorption activation energy E_des is also very high (Arrhenius: rate ∝ exp(−E_des/RT)). The desorption rate becomes vanishingly slow — products and reaction intermediates remain stuck on the surface, blocking active sites from accepting new reactants. Even though surface coverage is high, turnover is negligible because the surface never frees up. Catalysis requires a cycle: bind, react, release. A catalyst that binds too strongly gets stuck at the 'release' step."
  explanation: "This is the mechanistic basis of the Sabatier principle and the volcano plot. The optimal binding energy maximizes the product of coverage (favors strong binding) and turnover (favors weak binding). Too strong: surface poisoning by products or intermediates. Too weak: insufficient coverage to drive the reaction. The volcano plot visualizes this tradeoff across real catalysts."
```

## Explainer

Building on what you know about adsorption isotherms and surface thermodynamics, we can now connect the equilibrium description of adsorption (how much sticks at a given pressure) to the kinetic description (how fast it sticks and unsticks). This connection is essential because real applications — catalytic converters, gas masks, chromatography columns — operate under dynamic conditions where both the extent and the rate of adsorption matter.

The **Langmuir isotherm** is the simplest physically motivated model. It treats the surface as a collection of identical, independent binding sites. At equilibrium, the fraction of occupied sites θ = KP/(1 + KP), where K is the equilibrium constant for adsorption and P is gas pressure. At low pressure, θ grows linearly with P (every molecule that hits the surface finds an empty site). At high pressure, θ approaches 1 — the surface is full, and additional gas molecules have nowhere to land. The shape is a hyperbola, identical in form to Michaelis-Menten enzyme kinetics, and for the same mathematical reason: a saturable process with first-order uptake competing against a fixed capacity. The key Langmuir assumptions — uniform sites, no lateral interactions, monolayer only — are often violated in practice, but the model remains the essential starting point.

The **Freundlich isotherm** (θ ∝ P^(1/n)) is empirical and handles heterogeneous surfaces where some sites bind strongly and others weakly. It fits many real systems well over intermediate pressure ranges but lacks Langmuir's saturation behavior — it predicts infinite adsorption at infinite pressure, which is unphysical. The **BET isotherm** extends Langmuir to multilayer adsorption: once the first layer forms, additional layers can stack on top. BET is the standard method for measuring surface area of porous materials; the characteristic S-shaped isotherm reflects monolayer formation followed by multilayer condensation.

On the kinetic side, the rate of adsorption depends on collision frequency (from kinetic molecular theory) multiplied by a **sticking probability** — the fraction of collisions that actually lead to binding. This sticking probability may include an activation energy barrier (chemisorption) or be nearly unity (physisorption). Desorption follows Arrhenius kinetics: rate ∝ exp(−E_des/RT), where E_des is the desorption activation energy. At equilibrium, the rates of adsorption and desorption are equal, and you recover the Langmuir isotherm from the kinetic expressions — this is a satisfying consistency check. For catalysis, the kinetic picture is crucial: a catalyst that binds reactants too weakly never accumulates enough surface coverage, while one that binds too strongly cannot release products fast enough. The optimal catalyst sits at the peak of a **volcano plot**, balancing adsorption and desorption rates — a principle known as the Sabatier principle that directly follows from the kinetics of adsorption.
