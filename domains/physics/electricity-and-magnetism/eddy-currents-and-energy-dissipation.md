---
id: eddy-currents-and-energy-dissipation
title: Eddy Currents and Energy Dissipation
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: faraday-law-of-induction
  type: hard
- id: joule-heating-resistive-power
  type: hard
builds-toward:
- transformer-efficiency
tags:
- induction
- energy dissipation
- losses
stage: formal-systems
status: draft
---

# Eddy Currents and Energy Dissipation

## Core Idea
Changing magnetic fields induce circular currents (eddy currents) in conductors that produce fields opposing the change (Lenz's law). These eddy currents dissipate energy as Joule heat. Eddy current losses increase with the square of frequency and conductivity. Laminating conductors reduces eddy current losses by confining them to smaller loops.

## How It's Best Learned
Observe eddy current effects using a magnet and conducting plate. Calculate power dissipation from eddy currents in a plate in an AC magnetic field.

## Common Misconceptions
- Eddy currents are desirable (they dissipate energy and reduce efficiency).
- Lamination eliminates eddy currents (it reduces them by confining to smaller loops).
- Eddy currents are the same as primary circuit currents (they are separate, induced effects).

## Explainer

Faraday's law says that any changing magnetic flux through a conducting loop induces an EMF. In a wire coil, we channel this EMF to drive current through a defined circuit. But conductors don't come in neat loops — a solid block of aluminum or steel is just a sea of free charges embedded in a conductor with no preferred path. When a changing magnetic field threads through such a bulk conductor, EMF is induced everywhere, and current flows in whatever closed loops it can find within the material. These are **eddy currents**: closed swirls of current circling inside a conductor, named by analogy to the eddies that form when water flows around an obstacle.

Lenz's law, which you know from Faraday's law, governs eddy currents just as it governs coil currents: the induced current always flows in the direction that opposes the change causing it. If a magnet falls toward a conducting plate, the eddy currents in the plate create a magnetic field that pushes back against the falling magnet — producing a braking force. This is the principle behind magnetic brakes in trains and roller coasters. Unlike friction brakes, magnetic braking produces no wear and adjusts automatically: the faster the motion, the greater the flux change, the stronger the induced currents, and the stronger the braking force.

The energy side connects directly to your prerequisite on Joule heating. Eddy currents are real currents flowing through material with finite resistance. By P = I²R (or equivalently P = V²/R in the per-loop picture), they dissipate energy as heat. The loss scales with the square of frequency: at twice the frequency, the flux changes twice as fast, doubling the induced EMF, quadrupling the current and therefore quadrupling the power dissipated. This is why **lamination** is the key engineering solution. If you slice a transformer core into thin sheets separated by thin insulating layers, you prevent eddy currents from looping across the full cross-section. Each lamination can still carry eddy currents, but they are confined to a much smaller area, with much smaller loops — and since EMF scales with the loop area while resistance increases (thinner path), the eddy current and its associated loss drop dramatically. The power lost per unit volume scales as the square of the lamination thickness, so thinner laminations are strongly favored.

This trade-off is central to power engineering: a solid iron transformer core would be far too lossy for the AC frequencies used in power grids. High-frequency devices like switching power supplies require even thinner laminations, or better yet, ferrite cores (ceramic magnetic materials with very high resistivity) that nearly eliminate eddy current paths altogether. The principle generalizes: wherever you want to carry magnetic flux efficiently without turning the material into a resistive heater, you must either restrict current paths or use materials that resist current flow.
