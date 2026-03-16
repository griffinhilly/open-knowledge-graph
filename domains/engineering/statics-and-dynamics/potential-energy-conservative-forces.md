---
id: potential-energy-conservative-forces
title: Potential Energy and Conservative Forces
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: work-power-energy-fundamentals
  type: hard
- id: rigid-body-work-energy
  type: soft
builds-toward:
- energy-conservation-methods
- vibrations-simple-harmonic
tags:
- potential-energy
- conservative
- gravity
- springs
stage: formal-systems
status: draft
---

# Potential Energy and Conservative Forces

## Core Idea
A conservative force is one where work done is independent of the path; it can be represented by a potential energy function: F = -∇U. Gravitational potential energy is mgh and elastic potential energy is ½kx². For conservative forces, mechanical energy E = KE + PE is conserved: E = constant along the motion.

## Explainer

From the work-energy theorem you already know, the net work done on a body equals its change in kinetic energy: W_net = ΔKE. This is always true. But for certain forces — gravity, spring forces — something special holds: the work they do depends only on the starting and ending position, not on the path traveled between them. A ball dropped straight down and a ball rolled down a curved ramp gain the same kinetic energy from gravity if they fall the same height. These are **conservative forces**, and recognizing them unlocks a far more powerful method of analysis.

The key is the **potential energy function** U, defined so that F = -dU/dx in one dimension (or F = -∇U in three). The negative sign encodes the physical intuition: force points toward decreasing potential energy, just as a ball rolls downhill. For gravity near Earth's surface, U = mgh, and F = -d(mgh)/dh = -mg, consistent with gravity pulling downward. For a spring, U = ½kx², and F = -kx, consistent with the restoring force toward equilibrium. These potential energy expressions are not definitions to memorize independently — they follow from integrating the forces you already know.

The payoff is **conservation of mechanical energy**: when only conservative forces do work on a system, the total mechanical energy E = KE + PE is constant throughout the motion. Writing E_initial = E_final lets you solve for any unknown state without tracing the path. A roller coaster descending from rest at height h reaches speed v = √(2gh) at the bottom, regardless of the track's shape — you don't integrate work along the curve, you simply equate energy. A mass on a spring oscillates indefinitely, converting kinetic energy to elastic potential and back, with the total unchanged.

The contrast with non-conservative forces defines the method's scope. Friction, drag, and externally applied forces that lack a potential energy function do work that depends on path length — they convert mechanical energy to heat or inject energy from external sources. When these are present, use the general form: ΔE_mechanical = W_non-conservative. Conservative forces still contribute through ΔPE, but non-conservative work appears explicitly on the right. Identifying which forces are conservative is always the first step: segregate the forces, handle conservative ones through potential energy, and account for the rest through path-dependent work.
