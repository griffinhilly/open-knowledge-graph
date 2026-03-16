---
id: energy-density-electric-field
title: Energy Density in Electric Fields
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: potential-energy-systems
  type: hard
- id: dielectric-susceptibility-constant
  type: soft
builds-toward:
- electric-current-definition
tags:
- energy
- density
- field
stage: formal-systems
status: draft
---

# Energy Density in Electric Fields

## Core Idea
Energy density in an electric field is u = ½ε₀εᵣE². Total energy stored in a capacitor is U = ½CV² = ½QV = Q²/(2C), which can be recovered as field energy integrated over volume.

## Explainer

When you push charges onto a capacitor against the repulsion of charges already there, you do work. Where does that energy go? Not into heat — there is no dissipation. It goes into the electric field itself. This is a conceptual leap worth dwelling on: **energy can be stored in a field**, not just in the configuration of particles. The field between the capacitor plates is a real physical entity that carries energy.

The energy density u = ½ε₀E² (in vacuum) tells you how much energy is packed into each cubic meter of space where the field has strength E. The factor of ½ appears for the same reason it does in spring potential energy ½kx² — both represent a linear restoring force integrated over displacement. For a parallel-plate capacitor with plate area A, separation d, and uniform field E = V/d, integrating the energy density over the volume between the plates gives U = ½ε₀E² · Ad = ½(ε₀A/d)V² = ½CV². You have rederived the capacitor energy formula from field energy — these are equivalent descriptions of the same stored energy.

The three equivalent forms U = ½CV² = ½QV = Q²/(2C) are useful in different situations. Use ½CV² when voltage is the given quantity (charging from a battery at fixed V). Use Q²/(2C) when charge is held fixed — for instance, calculating how the energy changes when you pull the plates apart while disconnected from any source. Use ½QV as a bridge when relating both. For dielectrics, the energy density becomes u = ½ε₀εᵣE², where εᵣ is the relative permittivity. A dielectric material amplifies how much energy is stored at a given field strength, which is why inserting a dielectric increases a capacitor's capacitance and stored energy at fixed voltage.

The field-energy perspective is more powerful than the circuit perspective because it generalizes. Magnetic fields carry energy density ½μ₀⁻¹B². Electromagnetic waves carry energy through empty space, described by the Poynting vector E⃗ × H⃗. The recognition that fields themselves carry energy — not merely the charges that create them — is foundational to all of classical electromagnetism and, eventually, to quantum field theory, where particle interactions are mediated by field quanta.
