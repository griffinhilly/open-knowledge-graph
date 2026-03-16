---
id: larmor-formula
title: Larmor Formula for Radiated Power
domain: physics
course: electrodynamics
prerequisites:
- id: radiation-from-accelerated-charges
  type: hard
- id: poynting-vector-and-energy-flux
  type: soft
builds-toward:
- electric-dipole-radiation
- synchrotron-radiation
tags:
- power
- larmor
- acceleration
stage: abstract-reasoning
status: draft
---

# Larmor Formula for Radiated Power

## Core Idea
The Larmor formula P = (q²a²)/(6πε₀c³) gives power radiated by a non-relativistic accelerated point charge. Maximum power radiates perpendicular to acceleration; no power along the acceleration direction. This fundamental result connects acceleration to energy loss by radiation.

## Explainer

From your study of radiation from accelerated charges, you know that the radiation field falls off as 1/r — unlike the near (velocity) field which falls off as 1/r². This 1/r behavior means the energy flux (Poynting vector) falls off as 1/r², and when integrated over a sphere of radius r, the total power flowing outward is constant — the same at every r, meaning energy genuinely escapes to infinity. The **Larmor formula** puts a number on exactly how much power escapes: P = q²a²/(6πε₀c³). It depends on the charge squared, the acceleration squared, and three fundamental constants.

To see why acceleration squared appears, recall that the radiation field is proportional to acceleration (E_rad ∝ a/r), so the Poynting vector goes as a²/r², and integrating over the sphere gives a² with no r-dependence — consistent with power flowing away. The three constants encode the electromagnetic structure of space: ε₀ tells you how "difficult" it is for fields to exist in vacuum, while c³ reflects the fact that radiation involves the field restructuring itself at the speed of light. Larger charge radiates more (it couples more strongly to the EM field); higher acceleration radiates more (it disturbs the field more violently); weaker constants mean easier propagation.

The **radiation pattern** — which direction the power flows — is not uniform. No power is radiated along the direction of acceleration; maximum power is radiated perpendicular to it. The angular distribution goes as sin²θ, where θ is measured from the acceleration axis, giving a donut-shaped pattern with the acceleration axis as the hole. This is the characteristic signature of electric dipole radiation: you can think of the accelerated charge as an oscillating electric dipole, and dipoles don't radiate along their axis.

The practical consequences of the Larmor formula are everywhere. In classical atomic physics, an electron orbiting a nucleus is centripetally accelerated and should therefore radiate, losing energy and spiraling inward — the "classical collapse" that demanded quantum mechanics. In particle accelerators, electrons radiated via this mechanism (called **synchrotron radiation**) lose significant energy per revolution, limiting the energy achievable in circular machines. In radio antennas, it's the acceleration of electrons back and forth in the antenna wire that produces the outgoing EM wave. The Larmor formula gives the engineering relationship between antenna current (and hence charge acceleration) and radiated power. The formula's simplicity — two fundamental constants, charge, and acceleration — belies its reach across atomic, accelerator, and antenna physics.
