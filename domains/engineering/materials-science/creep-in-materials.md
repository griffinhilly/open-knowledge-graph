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
stage: formal-systems
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

## Questions

```yaml
- question: "A lead pipe at room temperature (25°C) slowly deforms under its own weight over several years, while a steel pipe under identical stress conditions shows no time-dependent deformation. What is the correct explanation?"
  type: multiple-choice
  options:
    - "Lead has a lower yield strength than steel, so it deforms plastically at lower stresses"
    - "Room temperature is above 0.4 Tm for lead (Tm ≈ 600 K) but well below 0.4 Tm for steel (Tm ≈ 1811 K), placing lead in the creep regime and steel outside it"
    - "Lead undergoes elastic deformation rather than plastic deformation, making it more susceptible to creep"
    - "Steel is alloyed with carbon which blocks diffusion-driven deformation mechanisms"
  answer: 1
  explanation: "The key is homologous temperature T/Tm, not absolute temperature. For lead, Tm ≈ 600 K, so 0.4Tm ≈ 240 K — well below room temperature (298 K). Lead is already deep into its creep regime at room temperature. For steel, Tm ≈ 1811 K, so 0.4Tm ≈ 724 K (≈ 450°C) — far above room temperature. The yield strength argument (option A) is a tempting distraction because lead does have lower yield strength, but that doesn't explain time-dependent flow at stresses below the yield point. Creep is fundamentally a thermal activation phenomenon, not a yield stress phenomenon."

- question: "An engineer designing turbine blades must choose between an alloy with small grains and one with large grains (same composition). Which should she choose to minimize creep deformation, and why?"
  type: multiple-choice
  options:
    - "Small grain size — the Hall-Petch effect strengthens grain boundaries and resists all forms of deformation including creep"
    - "Large grain size — grain boundary sliding is a major creep mechanism, and fewer grain boundaries reduce this contribution"
    - "Small grain size — finer grains reduce the mean free path for dislocation glide, slowing creep"
    - "Grain size is irrelevant to creep; only the alloy composition determines creep resistance"
  answer: 1
  explanation: "This is a counterintuitive reversal of the Hall-Petch effect. For room-temperature strength, finer grains are better (Hall-Petch: strength ∝ grain size^−½). But at high temperatures where creep dominates, grain boundaries are sites of weakness, not strength — grain boundary sliding allows adjacent grains to shift relative to each other under sustained stress. Larger grains mean fewer grain boundaries per unit volume, reducing this mechanism. Turbine blade alloys take this to the extreme: directionally solidified columnar grains (aligned with the stress axis to eliminate transverse boundaries) or even single-crystal blades (no grain boundaries at all) are used in the hottest turbine stages."

- question: "The steady-state creep rate of a material exhibits an Arrhenius dependence on temperature, with an activation energy that is often similar to the activation energy for self-diffusion."
  type: true-false
  answer: true
  explanation: "The steady-state creep rate is described by ε̇ = A·σⁿ·exp(−Q/RT), where Q is the creep activation energy and R is the gas constant. Experimentally, Q for steady-state creep in metals is typically close to the activation energy for self-diffusion in the same material. This is not a coincidence — the rate-controlling mechanism for creep (dislocation climb) requires dislocations to absorb or emit vacancies, a process that depends on the same atomic diffusion that governs self-diffusion. Measuring the creep activation energy is thus a way to identify the dominant creep mechanism."

- question: "Creep only occurs at stresses that exceed the material's conventional yield stress measured at room temperature."
  type: true-false
  answer: false
  explanation: "Creep is time-dependent plastic deformation that occurs at stresses well below the conventional yield stress, provided the temperature is high enough. A conventional stress-strain test measures near-instantaneous response — if the stress doesn't cause immediate plastic flow, the material appears to be elastic. But at elevated temperatures, thermally activated mechanisms (dislocation climb, grain boundary sliding, vacancy diffusion) allow slow, continuous plastic strain to accumulate over time even at stresses far below the yield point. This is precisely why creep must be analyzed separately from conventional plasticity in high-temperature design."

- question: "Why does homologous temperature T/Tm (rather than absolute temperature) determine whether creep is significant, and what does this reveal about the underlying mechanism?"
  type: short-answer
  answer: "Creep is driven by thermally activated atomic mechanisms — primarily dislocation climb (dislocations absorbing or emitting vacancies to bypass obstacles) and grain boundary sliding, both of which require atomic diffusion. The rate of these processes depends not on absolute temperature alone, but on how active thermal fluctuations are relative to the binding energy of atoms in the crystal — which scales with the melting point Tm. At T/Tm ≈ 0.4, atoms have enough thermal energy to diffuse at rates that matter on engineering timescales, regardless of whether that's −33°C for lead or 450°C for steel. The homologous temperature is essentially a normalized measure of 'how liquid-like is this solid' — near Tm, atoms are highly mobile; far below, they are locked in place. Because the mechanism requires diffusion, and diffusion rates scale with T/Tm, so does creep significance."
  explanation: "This also explains why the Arrhenius equation applies: the rate of any thermally activated process with activation energy Q scales as exp(−Q/RT). For creep, Q ≈ Q_diffusion, so the creep rate has the same Arrhenius form as the diffusion coefficient. T/Tm is a convenient normalization because Tm is approximately proportional to the cohesive energy of the material — it captures the material's resistance to atomic rearrangement in a single number."
```

## Explainer

From your study of stress-strain behavior, you know that metals deform elastically (reversibly) below the yield stress and plastically (permanently) above it. Both of these responses happen almost instantaneously when the load is applied. Creep reveals a third type of deformation that your basic stress-strain curve ignores: **time-dependent plastic flow** that occurs even at stresses well below the yield stress, but only when the temperature is high enough. Apply a constant load to a turbine blade at 800°C, come back a week later, and it will be permanently longer — even though the stress never exceeded the yield point you measured at room temperature.

The temperature threshold for creep is not absolute but relative. The relevant parameter is the **homologous temperature** T/Tm (temperature as a fraction of the melting point in Kelvin). Creep becomes significant above roughly 0.4 Tm for metals. This explains why lead creeps at room temperature (Tm ≈ 600K, so 0.4Tm ≈ 240K, below room temperature) while steel requires several hundred degrees Celsius. Your prerequisite on the Arrhenius equation explains why: the mechanisms that drive creep — primarily **dislocation climb** and **grain boundary sliding** — require thermal activation. Dislocation climb involves dislocations absorbing or emitting vacancies to bypass obstacles, and vacancy diffusion has an activation energy that makes the process exponentially more active at higher temperatures.

A **creep curve** plots strain versus time under constant stress and temperature, and it shows three characteristic stages. In **primary creep**, strain rate decreases over time as the material work-hardens: dislocations accumulate and interfere with each other's motion, making further deformation increasingly difficult. In **secondary (steady-state) creep**, hardening and thermally-assisted recovery (annihilation of dislocations by climb) reach a dynamic equilibrium, producing a roughly constant minimum strain rate — this is the stage engineers care most about for life prediction. In **tertiary creep**, internal damage accumulates (grain boundary cavities, necking), hardening can no longer keep pace with damage, and the strain rate accelerates until fracture. The **steady-state creep rate** follows an Arrhenius form: ε̇ = A·σⁿ·exp(−Q/RT), where Q is the activation energy (often close to the activation energy for self-diffusion you learned in diffusion in solids, confirming that diffusion controls the mechanism).

For design, creep limits manifest as two failure modes: **creep rupture** (the component eventually fractures) and **creep deformation** (blade tip clearances close, seals leak, structures sag). Engineers combat creep through microstructural strategies — fine coherent precipitates pin dislocations (as in nickel superalloys used in jet engine turbines), large grain size or single-crystal structures eliminate grain boundaries, and refractory alloying elements raise the effective Tm. Understanding that larger grain size *helps* against creep (by eliminating grain boundary sliding sites) while it *hurts* against fatigue and fracture is one of the fundamental tradeoffs in high-temperature materials design.
