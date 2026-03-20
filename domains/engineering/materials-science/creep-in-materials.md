---
id: creep-in-materials
title: 'Creep: Time-Dependent Deformation'
domain: engineering
course: materials-science
prerequisites:
- id: stress-strain-behavior
  type: hard
- id: diffusion-in-solids
  type: soft
- id: arrhenius-equation
  type: soft
tags:
- creep
- high-temperature
- tertiary-creep
- steady-state
- dislocation-climb
stage: advanced
status: validated
---

# Creep: Time-Dependent Deformation

## Core Idea
Creep is the slow, time-dependent plastic deformation of a material under constant stress at elevated temperatures (typically above ~0.4 Tm, where Tm is the melting temperature in Kelvin). A creep curve shows three stages: primary (decreasing strain rate as the material strain hardens), secondary/steady-state (constant minimum strain rate governed by balance of hardening and recovery), and tertiary (accelerating strain rate leading to fracture). Mechanisms include dislocation climb (aided by diffusion), grain boundary sliding, and vacancy diffusion. Creep is critical for designing turbine blades, boilers, and other high-temperature structural components.

## How It's Best Learned
Plot creep curves for different stress levels and temperatures, observing how both accelerate creep rate. Apply the Arrhenius relationship to the steady-state creep rate to extract activation energy and compare with diffusion activation energies.

## Common Misconceptions
- Creep occurs in polymers and ceramics at room temperature, not just metals at high temperature — the relevant parameter is the homologous temperature T/Tm, not absolute temperature.
- Increasing grain size reduces creep rate in metals (opposite of the Hall-Petch effect for strength), because grain boundary sliding contributes to creep.

## Explainer

From your study of stress-strain behavior, you know that metals deform elastically (reversibly) below the yield stress and plastically (permanently) above it. Both of these responses happen almost instantaneously when the load is applied. Creep reveals a third type of deformation that your basic stress-strain curve ignores: **time-dependent plastic flow** that occurs even at stresses well below the yield stress, but only when the temperature is high enough. Apply a constant load to a turbine blade at 800°C, come back a week later, and it will be permanently longer — even though the stress never exceeded the yield point you measured at room temperature.

The temperature threshold for creep is not absolute but relative. The relevant parameter is the **homologous temperature** T/Tm (temperature as a fraction of the melting point in Kelvin). Creep becomes significant above roughly 0.4 Tm for metals. This explains why lead creeps at room temperature (Tm ≈ 600K, so 0.4Tm ≈ 240K, below room temperature) while steel requires several hundred degrees Celsius. Your prerequisite on the Arrhenius equation explains why: the mechanisms that drive creep — primarily **dislocation climb** and **grain boundary sliding** — require thermal activation. Dislocation climb involves dislocations absorbing or emitting vacancies to bypass obstacles, and vacancy diffusion has an activation energy that makes the process exponentially more active at higher temperatures.

A **creep curve** plots strain versus time under constant stress and temperature, and it shows three characteristic stages. In **primary creep**, strain rate decreases over time as the material work-hardens: dislocations accumulate and interfere with each other's motion, making further deformation increasingly difficult. In **secondary (steady-state) creep**, hardening and thermally-assisted recovery (annihilation of dislocations by climb) reach a dynamic equilibrium, producing a roughly constant minimum strain rate — this is the stage engineers care most about for life prediction. In **tertiary creep**, internal damage accumulates (grain boundary cavities, necking), hardening can no longer keep pace with damage, and the strain rate accelerates until fracture. The **steady-state creep rate** follows an Arrhenius form: ε̇ = A·σⁿ·exp(−Q/RT), where Q is the activation energy (often close to the activation energy for self-diffusion you learned in diffusion in solids, confirming that diffusion controls the mechanism).

For design, creep limits manifest as two failure modes: **creep rupture** (the component eventually fractures) and **creep deformation** (blade tip clearances close, seals leak, structures sag). Engineers combat creep through microstructural strategies — fine coherent precipitates pin dislocations (as in nickel superalloys used in jet engine turbines), large grain size or single-crystal structures eliminate grain boundaries, and refractory alloying elements raise the effective Tm. Understanding that larger grain size *helps* against creep (by eliminating grain boundary sliding sites) while it *hurts* against fatigue and fracture is one of the fundamental tradeoffs in high-temperature materials design.
