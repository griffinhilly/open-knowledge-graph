---
id: toroid-magnetic-field-calculation
title: Toroid Magnetic Field and Calculation
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: amperes-law
  type: hard
- id: solenoid-magnetic-field-properties
  type: hard
builds-toward:
- inductance-and-inductors
tags:
- magnetism
- toroids
- Ampere's law
stage: formal-systems
status: draft
---

# Toroid Magnetic Field and Calculation

## Core Idea
A toroid is a solenoid bent into a ring with current through a wrapped coil. The magnetic field is contained inside: B(r) = μ₀NI/(2πr), varying with radius. The field outside is zero. A toroid confines the magnetic field completely, useful for inductors and transformers where containment is desired. The field magnitude decreases as 1/r with radius.

## Explainer

You already know that a solenoid — a helical coil of wire — produces a nearly uniform magnetic field along its axis when current flows through it. The field lines run straight through the interior and loop back outside. But those external field lines mean a solenoid "leaks" magnetic flux into surrounding space. A **toroid** solves this by bending the solenoid into a closed ring so that the field lines have nowhere to go but around the inside of the ring. Every field line that would have been external in a straight solenoid is now forced to stay inside the donut-shaped core.

Ampere's law is the key tool for calculating the field. Drawing a circular Amperian loop of radius r centered at the toroid's axis of symmetry: if the loop is inside the toroid (between the inner and outer radii), every one of the N turns threads through the loop, contributing NI to the enclosed current. By the same azimuthal symmetry argument you used for a solenoid, B must be tangent to the loop and constant in magnitude, so B(2πr) = μ₀NI, giving **B(r) = μ₀NI/(2πr)**. The 1/r dependence distinguishes the toroid from a solenoid: a solenoid has uniform field inside, while a toroid's field is strongest near the inner radius and weakest at the outer radius.

For a loop drawn entirely outside the toroid — any circle with radius greater than the outer radius — the current-in minus current-out through the Amperian surface is zero. Every wire that carries current in one direction through the loop is paired with a return wire in the other direction (because the coil wraps around the full 360° of the ring). The enclosed current is exactly zero, and therefore B = 0 outside. This perfect containment is what makes toroids so valuable in circuit design: an inductor or transformer wound as a toroid does not radiate magnetic flux into neighboring components, eliminating crosstalk and electromagnetic interference.

This leads naturally to inductance. Because the flux is confined and calculable, the inductance L = NΦ/I can be computed analytically, using the field expression and integrating over the cross-sectional area of the core. For a rectangular cross-section toroid with inner radius a, outer radius b, and height h, this integral gives L = (μ₀N²h/2π) ln(b/a). The practical upshot is that toroids allow compact, efficient, interference-free inductors — which is why they appear everywhere from audio amplifiers to power supply filters to the magnetic cores of transformers in laptops and phone chargers.
