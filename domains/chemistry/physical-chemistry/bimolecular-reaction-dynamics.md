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

## Explainer

From transition state theory, you know that a bimolecular reaction proceeds through an activated complex sitting at a saddle point on the potential energy surface. That framework gives you the rate constant — the macroscopic "how fast" — but it treats the molecular collision as a black box. Bimolecular reaction dynamics opens that box and asks: what actually happens during the collision? How do the molecules approach each other, how does energy redistribute, and where do the products fly off to?

The starting concept is the **reactive cross section**, σᵣ, which you can think of as the effective target area a molecule presents for a reactive collision. It depends on the collision energy, the relative orientation of the reactants, and quantum mechanical factors. Simple collision theory approximates the rate constant as k = p · Z · exp(−Eₐ/k_BT), where Z is the collision frequency and p is the **steric factor** — a fudge factor between 0 and 1 that accounts for the fact that most collisions have the wrong orientation for reaction. While p gives you a single number, the reality is far richer: the probability of reaction varies continuously with the **impact parameter** b (how far off-center the collision is) and the mutual orientation of the molecules.

**Crossed molecular beam experiments** are the experimental tool that reveals this richness. Two beams of reactant molecules, each with well-defined velocity and direction, intersect in a vacuum chamber. By detecting the scattered products as a function of angle and velocity, experimentalists construct a **Newton diagram** — a velocity-space map showing where products end up. The angular distribution of products is the **differential cross section**, and its shape is a direct fingerprint of the reaction mechanism. If products scatter predominantly backward (back toward the incoming reactant), the reaction proceeded by a **direct rebound mechanism** — a hard, head-on collision where the old bond breaks and the new bond forms in a single concerted motion, like two billiard balls bouncing off each other. If products scatter with forward-backward symmetry, the collision formed a **long-lived complex** that survived several rotational periods before breaking apart, losing memory of the initial collision geometry.

The most revealing aspect of molecular beam experiments is **product state analysis** — measuring how much energy goes into translation, vibration, and rotation of the products. For the classic reaction F + D₂ → DF + D, experiments show that most of the energy is channeled into vibration of the DF product, with the DF molecule born in highly excited vibrational states. This maps directly onto the topology of the potential energy surface: an "early barrier" (transition state located in the entrance channel, before significant bond extension) funnels the energy released by the new bond into product vibration. A "late barrier" (transition state in the exit channel) would instead channel energy into translation. This connection between surface topology and energy disposal, first articulated through Polanyi's rules, shows how the shape of the potential energy surface governs not just whether a reaction occurs, but exactly how the products emerge.
