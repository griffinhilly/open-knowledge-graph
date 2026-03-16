---
id: conservation-of-electric-charge
title: Conservation of Electric Charge
domain: physics
course: electricity-and-magnetism
prerequisites: []
builds-toward:
- coulomb-force-superposition
tags:
- charge
- conservation
- continuity
stage: formal-systems
status: draft
---

# Conservation of Electric Charge

## Core Idea
Electric charge is conserved in all interactions within an isolated system. Charge cannot be created or destroyed, only transferred between objects or separated. This fundamental conservation principle is encoded in the continuity equation ∂ρ/∂t + ∇·J⃗ = 0, which relates charge density to current density.

## Explainer

**Electric charge** is one of the most fundamental properties of matter, and its conservation is one of the most thoroughly tested laws in physics. When you rub a glass rod with silk, the rod becomes positively charged — but not because charge was created. Instead, electrons (negative charge carriers) moved from the glass onto the silk, leaving the glass with a net positive charge and the silk with an equal net negative charge. The total charge of the glass-plus-silk system is exactly what it was before: zero. Charge is always transferred, never manufactured.

This seemingly simple observation has deep consequences. No known physical process — chemical reactions, nuclear decays, particle–antiparticle creation — has ever been observed to change the net electric charge of an isolated system. When a neutron decays into a proton, an electron, and an antineutrino, the total charge before (zero) equals the total charge after (+1 − 1 + 0 = 0). When a gamma ray creates an electron–positron pair, a negative and positive charge appear simultaneously and in equal magnitude, keeping the total at zero. Conservation of charge is exact and universal.

The mathematical backbone of this principle is the **continuity equation**: ∂ρ/∂t + ∇·J⃗ = 0. Here ρ is the charge density (charge per unit volume) at a point in space, and J⃗ is the current density (charge flowing per unit area per unit time). The divergence ∇·J⃗ measures how much charge is flowing *out* of a small volume per unit time. If charge is flowing out of a region (∇·J⃗ > 0), then the charge density inside must be decreasing (∂ρ/∂t < 0) at exactly the same rate. This is the local statement of conservation: charge doesn't teleport. If charge leaves a region, it flows out continuously through the boundary.

Think of it as a bookkeeping identity for charge, identical in structure to mass conservation in fluid mechanics — which you may already know as the continuity equation for fluids. If water flows out of a volume faster than it flows in, the volume must be draining. Charge obeys the same logic. This conservation law underpins Kirchhoff's current law in circuits (the sum of currents entering a node equals the sum leaving), the behavior of capacitors, and the derivation of Gauss's law from Maxwell's equations. Every electromagnetic calculation you will do rests on this foundation.

Conservation of charge is also connected to a deep principle in theoretical physics: **Noether's theorem** tells us that every continuous symmetry of the laws of physics corresponds to a conserved quantity. Conservation of charge corresponds to a symmetry of the electromagnetic field equations under a certain class of transformations of the potentials (gauge invariance). In this sense, conservation of charge is not an empirical accident but a structural necessity of the theory. As you advance into electrodynamics and quantum field theory, this connection will become progressively more concrete and powerful.
