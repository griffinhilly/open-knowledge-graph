---
id: bimolecular-reaction-dynamics
title: 'Bimolecular Reaction Dynamics: Collisions, Cross Sections, and Scattering'
domain: chemistry
course: physical-chemistry
prerequisites:
- id: molecularity-vs-order
  type: hard
- id: transition-state-theory
  type: hard
builds-toward: []
tags:
- collision-cross-section
- steric-factor
- reactive-scattering
- molecular-beams
- impact-parameter
- differential-cross-section
stage: advanced
status: draft
---

# Bimolecular Reaction Dynamics: Collisions, Cross Sections, and Scattering

## Core Idea
Bimolecular reaction dynamics examines the detailed molecular-level events during a reactive collision. The reactive cross section sigma_r quantifies the effective target area for reaction as a function of collision energy and is related to the rate constant by k = <v_rel * sigma_r>, averaged over the relative velocity distribution. The steric factor p in simple collision theory (k = p * Z * exp(-Ea/kBT)) accounts for the fraction of collisions with the correct mutual orientation, but molecular beam experiments reveal far richer detail: differential cross sections show the angular distribution of products, revealing whether the reaction proceeds through a long-lived complex (forward-backward symmetric scattering) or a direct rebound mechanism (backward scattering). Crossed molecular beam experiments, pioneered by Lee and Herschbach, provide state-resolved information about product vibrational, rotational, and translational energy distributions, connecting directly to the topology of the potential energy surface.

## How It's Best Learned
Analyze molecular beam scattering data for a classic reaction like F + D2 -> DF + D. Examine the velocity-angle contour map (Newton diagram), identify whether the mechanism is direct or complex-mediated, and correlate the product energy disposal with features of the potential energy surface.

## Common Misconceptions
- Treating the steric factor as a simple geometric fraction; it encodes not just orientation but also quantum mechanical effects like tunneling and orbital symmetry constraints.
- Assuming all reactive collisions look alike; the dynamics range from direct rebound (hard repulsive wall) to stripping (long-range attraction) to complex formation (deep well), each with distinct angular and energy distributions.
