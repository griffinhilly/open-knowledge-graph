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
