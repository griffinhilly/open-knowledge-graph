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
status: validated
---

# Bimolecular Reaction Dynamics: Collisions, Cross Sections, and Scattering

## Core Idea
Bimolecular reaction dynamics examines the detailed molecular-level events during a reactive collision. The reactive cross section sigma_r quantifies the effective target area for reaction as a function of collision energy and is related to the rate constant by k = <v_rel * sigma_r>, averaged over the relative velocity distribution. The steric factor p in simple collision theory (k = p * Z * exp(-Ea/kBT)) accounts for the fraction of collisions with the correct mutual orientation, but molecular beam experiments reveal far richer detail: differential cross sections show the angular distribution of products, revealing whether the reaction proceeds through a long-lived complex (forward-backward symmetric scattering) or a direct rebound mechanism (backward scattering). Crossed molecular beam experiments, pioneered by Lee and Herschbach, provide state-resolved information about product vibrational, rotational, and translational energy distributions, connecting directly to the topology of the potential energy surface.

## How It's Best Learned
Analyze molecular beam scattering data for a classic reaction like F + D2 -> DF + D. Examine the velocity-angle contour map (Newton diagram), identify whether the mechanism is direct or complex-mediated, and correlate the product energy disposal with features of the potential energy surface.

## Common Misconceptions
- Treating the steric factor as a simple geometric fraction; it encodes not just orientation but also quantum mechanical effects like tunneling and orbital symmetry constraints.
- Assuming all reactive collisions look alike; the dynamics range from direct rebound (hard repulsive wall) to stripping (long-range attraction) to complex formation (deep well), each with distinct angular and energy distributions.

## Questions

```yaml
- question: "In a crossed molecular beam experiment, products from a bimolecular reaction are detected predominantly scattering backward — toward the direction of the incoming reactant beam. What does this angular distribution indicate about the reaction mechanism?"
  type: multiple-choice
  options:
    - "The reaction is endothermic, so products have less kinetic energy and scatter backward"
    - "The reaction proceeds by a direct rebound mechanism: a brief, hard collision where the new bond forms and old bond breaks in one concerted step"
    - "A long-lived collision complex formed and decayed, distributing products symmetrically in forward and backward directions"
    - "The mass asymmetry between reactants forces products to scatter backward regardless of mechanism"
  answer: 1
  explanation: "Backward scattering is the signature of a direct rebound mechanism — analogous to two billiard balls bouncing head-on. The collision is brief, dominated by short-range repulsion, and the product flies off in the backward hemisphere. Option C (long-lived complex) would produce forward-backward symmetric scattering: the complex survives long enough to rotate and lose memory of the initial collision geometry, making all scattering directions equally likely. Option A confuses energetics with dynamics — reaction enthalpy does not determine scattering angle. Option D is incorrect; mass asymmetry affects velocity magnitudes, not the mechanistic signature."

- question: "For F + D₂ → DF + D, experiments show that the DF product is born predominantly in highly excited vibrational states, with relatively little energy in translation. According to Polanyi's rules, this indicates what feature of the potential energy surface?"
  type: multiple-choice
  options:
    - "A late barrier in the exit channel: the transition state occurs after significant D-D bond extension, channeling energy into product translation"
    - "An early barrier in the entrance channel: the transition state occurs before significant D-D bond extension, and the energy released as the new F-D bond forms is channeled into product vibration"
    - "An early barrier that channels energy into product translation rather than vibration"
    - "A deep potential well (stable complex) that distributes energy equally among all product modes"
  answer: 1
  explanation: "Polanyi's rules connect energy disposal to PES topology. An 'early' barrier means the transition state is in the entrance channel — the D-D bond has barely stretched when the barrier is reached. Most energy is released as the new F-D bond forms along the exit channel, and this late energy release is channeled preferentially into vibration of the new DF bond. A 'late' barrier (exit channel transition state) would instead channel energy into product translation. F + D₂ → DF + D is the textbook case of highly vibrationally excited products arising from an early barrier."

- question: "The steric factor p in simple collision theory fully accounts for most of the reasons why the observed rate constant falls below the hard-sphere collision rate, including quantum tunneling and orbital symmetry constraints."
  type: true-false
  answer: false
  explanation: "The steric factor p is explicitly a fudge factor — a single number between 0 and 1 inserted to make the equation match experiment. It cannot disentangle geometric orientation requirements from quantum mechanical effects like tunneling (which can increase rates beyond classical predictions), orbital symmetry rules (Woodward-Hoffmann), or electronic factors. Molecular beam experiments reveal these contributions separately and show that p can sometimes exceed 1 when tunneling is important. Simple collision theory uses p precisely because it lacks a molecular-level description of what happens during the collision."

- question: "A reaction that produces products with forward-backward symmetric angular scattering in a molecular beam experiment most likely proceeded through a long-lived collision complex."
  type: true-false
  answer: true
  explanation: "When a collision complex forms and survives for many rotational periods, it loses all memory of the initial collision direction. When the complex eventually breaks apart, it ejects products with equal probability in the forward and backward directions, producing a symmetric angular distribution. A direct mechanism (rebound or stripping) is far too brief for significant rotation, so it produces an asymmetric distribution peaked either in the backward hemisphere (rebound) or forward hemisphere (stripping). Forward-backward symmetry is therefore the diagnostic signature of complex formation."

- question: "What is the difference between a 'direct rebound' and a 'complex-mediated' bimolecular reaction mechanism, and what experimental observable most clearly distinguishes them?"
  type: short-answer
  answer: "In direct rebound, the reaction occurs in a single brief collision dominated by short-range repulsion; the product flies off backward. In a complex-mediated mechanism, the collision forms a long-lived intermediate that survives many rotational periods before decomposing, losing directional memory and scattering products with forward-backward symmetry. The differential cross section — the angular distribution of products measured in a crossed molecular beam experiment — is the observable that most directly distinguishes them."
  explanation: "The Newton diagram from a crossed molecular beam experiment maps product scattering in velocity-angle space. Backward-peaked distributions fingerprint direct rebound; forward-backward symmetric distributions indicate complex formation. This experimental signature connects directly to the potential energy surface: reactions with deep wells (stable intermediates) favor complex formation, while reactions with high early barriers and no well favor direct rebound. The shape of the distribution also correlates with product energy disposal, linking angular dynamics to Polanyi's rules."
```

## Explainer

From transition state theory, you know that a bimolecular reaction proceeds through an activated complex sitting at a saddle point on the potential energy surface. That framework gives you the rate constant — the macroscopic "how fast" — but it treats the molecular collision as a black box. Bimolecular reaction dynamics opens that box and asks: what actually happens during the collision? How do the molecules approach each other, how does energy redistribute, and where do the products fly off to?

The starting concept is the **reactive cross section**, σᵣ, which you can think of as the effective target area a molecule presents for a reactive collision. It depends on the collision energy, the relative orientation of the reactants, and quantum mechanical factors. Simple collision theory approximates the rate constant as k = p · Z · exp(−Eₐ/k_BT), where Z is the collision frequency and p is the **steric factor** — a fudge factor between 0 and 1 that accounts for the fact that most collisions have the wrong orientation for reaction. While p gives you a single number, the reality is far richer: the probability of reaction varies continuously with the **impact parameter** b (how far off-center the collision is) and the mutual orientation of the molecules.

**Crossed molecular beam experiments** are the experimental tool that reveals this richness. Two beams of reactant molecules, each with well-defined velocity and direction, intersect in a vacuum chamber. By detecting the scattered products as a function of angle and velocity, experimentalists construct a **Newton diagram** — a velocity-space map showing where products end up. The angular distribution of products is the **differential cross section**, and its shape is a direct fingerprint of the reaction mechanism. If products scatter predominantly backward (back toward the incoming reactant), the reaction proceeded by a **direct rebound mechanism** — a hard, head-on collision where the old bond breaks and the new bond forms in a single concerted motion, like two billiard balls bouncing off each other. If products scatter with forward-backward symmetry, the collision formed a **long-lived complex** that survived several rotational periods before breaking apart, losing memory of the initial collision geometry.

The most revealing aspect of molecular beam experiments is **product state analysis** — measuring how much energy goes into translation, vibration, and rotation of the products. For the classic reaction F + D₂ → DF + D, experiments show that most of the energy is channeled into vibration of the DF product, with the DF molecule born in highly excited vibrational states. This maps directly onto the topology of the potential energy surface: an "early barrier" (transition state located in the entrance channel, before significant bond extension) funnels the energy released by the new bond into product vibration. A "late barrier" (transition state in the exit channel) would instead channel energy into translation. This connection between surface topology and energy disposal, first articulated through Polanyi's rules, shows how the shape of the potential energy surface governs not just whether a reaction occurs, but exactly how the products emerge.
