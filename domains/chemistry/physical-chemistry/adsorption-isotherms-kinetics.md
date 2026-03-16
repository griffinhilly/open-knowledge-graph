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

## Explainer

Building on what you know about adsorption isotherms and surface thermodynamics, we can now connect the equilibrium description of adsorption (how much sticks at a given pressure) to the kinetic description (how fast it sticks and unsticks). This connection is essential because real applications — catalytic converters, gas masks, chromatography columns — operate under dynamic conditions where both the extent and the rate of adsorption matter.

The **Langmuir isotherm** is the simplest physically motivated model. It treats the surface as a collection of identical, independent binding sites. At equilibrium, the fraction of occupied sites θ = KP/(1 + KP), where K is the equilibrium constant for adsorption and P is gas pressure. At low pressure, θ grows linearly with P (every molecule that hits the surface finds an empty site). At high pressure, θ approaches 1 — the surface is full, and additional gas molecules have nowhere to land. The shape is a hyperbola, identical in form to Michaelis-Menten enzyme kinetics, and for the same mathematical reason: a saturable process with first-order uptake competing against a fixed capacity. The key Langmuir assumptions — uniform sites, no lateral interactions, monolayer only — are often violated in practice, but the model remains the essential starting point.

The **Freundlich isotherm** (θ ∝ P^(1/n)) is empirical and handles heterogeneous surfaces where some sites bind strongly and others weakly. It fits many real systems well over intermediate pressure ranges but lacks Langmuir's saturation behavior — it predicts infinite adsorption at infinite pressure, which is unphysical. The **BET isotherm** extends Langmuir to multilayer adsorption: once the first layer forms, additional layers can stack on top. BET is the standard method for measuring surface area of porous materials; the characteristic S-shaped isotherm reflects monolayer formation followed by multilayer condensation.

On the kinetic side, the rate of adsorption depends on collision frequency (from kinetic molecular theory) multiplied by a **sticking probability** — the fraction of collisions that actually lead to binding. This sticking probability may include an activation energy barrier (chemisorption) or be nearly unity (physisorption). Desorption follows Arrhenius kinetics: rate ∝ exp(−E_des/RT), where E_des is the desorption activation energy. At equilibrium, the rates of adsorption and desorption are equal, and you recover the Langmuir isotherm from the kinetic expressions — this is a satisfying consistency check. For catalysis, the kinetic picture is crucial: a catalyst that binds reactants too weakly never accumulates enough surface coverage, while one that binds too strongly cannot release products fast enough. The optimal catalyst sits at the peak of a **volcano plot**, balancing adsorption and desorption rates — a principle known as the Sabatier principle that directly follows from the kinetics of adsorption.
