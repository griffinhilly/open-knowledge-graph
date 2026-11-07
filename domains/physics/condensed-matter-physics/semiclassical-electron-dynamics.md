---
id: semiclassical-electron-dynamics
title: 'Semiclassical Electron Dynamics: Effective Mass and Holes'
domain: physics
course: condensed-matter-physics
prerequisites:
- id: bloch-theorem
  type: hard
- id: band-structure-density-of-states
  type: hard
- id: tight-binding-model
  type: soft
- id: group-velocity-and-dispersion
  type: soft
- id: lorentz-force-on-moving-charge
  type: soft
builds-toward:
- semiconductor-physics-doping
- boltzmann-transport-equation-cm
- integer-quantum-hall-effect
tags:
- band-theory
- effective-mass
- holes
- transport
- bloch-oscillations
stage: expert
status: validated
---

# Semiclassical Electron Dynamics: Effective Mass and Holes

## Core Idea
In the semiclassical model, an electron in band n with crystal momentum ħk moves with the group velocity v = (1/ħ)∇ₖε(k), and external forces change its crystal momentum according to ħ dk/dt = −e(E + v × B). The lattice's effect is contained entirely in the band energy ε(k). Near a band minimum or maximum the electron responds as if it had an effective mass m*, set by the curvature of the band, which is negative near the top of a band. A nearly full band is best described by holes, which behave as particles with positive charge and positive mass.

## How It's Best Learned
Work with the one-dimensional tight-binding band ε(k) = −2t cos(ka). Plot ε, the velocity v(k), and the effective mass along the Brillouin zone, and trace an electron's motion in a constant electric field. Show that a completely filled band carries no current, then remove one electron and identify the hole. Compare with measured effective masses and the sign of the Hall coefficient in real materials.

## Common Misconceptions
- An effective mass means the electron's actual mass has changed. (The electron's mass is unchanged; m* summarizes how the periodic lattice potential alters its response to external forces.)
- Holes are positrons or some other real particle. (A hole is the collective behaviour of a nearly full band, described as the absence of one electron; it is a quasiparticle, not an antiparticle.)
- An electron's velocity in a crystal is ħk/m, as for a free particle. (Its velocity is the slope of the band, which falls to zero at the zone boundary even though k is large there.)

## Questions

```yaml
- question: "For the band ε(k) = −2t cos(ka), what is the electron's velocity at the zone boundary k = π/a?"
  type: multiple-choice
  options: ["2ta/ħ", "Zero", "ħπ/(ma)", "Infinite"]
  answer: 1
  explanation: "v = (1/ħ)dε/dk = (2ta/ħ) sin(ka). At k = π/a, sin π = 0, so v = 0. The band is flat at the zone boundary."
- question: "A completely filled energy band carries no net electric current, even when an electric field is applied."
  type: true-false
  answer: true
  explanation: "In a filled band, for every state k there is a state −k with opposite velocity, and the field only relabels states within the band. The velocities sum to zero, so there is no current."
- question: "What is the effective mass at the bottom of the band ε(k) = −2t cos(ka), at k = 0?"
  type: multiple-choice
  options: ["ħ²/(2ta²)", "2ta²/ħ²", "−ħ²/(2ta²)", "The free-electron mass"]
  answer: 0
  explanation: "1/m* = (1/ħ²)d²ε/dk² = 2ta² cos(ka)/ħ². At k = 0 this gives m* = ħ²/(2ta²). At the band top, k = π/a, m* has the same size but negative sign."
- question: "In a perfect crystal under a constant electric field, the semiclassical model predicts that an electron oscillates in position rather than accelerating forever. Name the effect and explain why it is not seen in ordinary metals."
  type: short-answer
  answer: "Bloch oscillations. In ordinary metals, electrons scatter off impurities and phonons long before completing one oscillation period, h/(eEa), which is very long for typical fields and lattice constants."
  explanation: "Bloch oscillations were observed in semiconductor superlattices, whose large period a shortens the oscillation period, and in ultracold atoms in optical lattices."
```

## Explainer
A free electron obeys F = dp/dt and v = p/m. In a crystal the periodic potential changes both relations, but Bloch's theorem keeps a useful structure. Each electron state is labelled by a band index n and a wavevector k, with energy εₙ(k). The semiclassical model treats a wave packet built from states near one k as a particle and gives two rules.

First, the velocity is the group velocity of the band: v = (1/ħ)∇ₖε(k). Second, an external force changes the wavevector: ħ dk/dt = F, where for an electron F = −e(E + v × B). The force acts on ħk, called the crystal momentum. The force from the lattice itself never appears; it is already built into ε(k). The model assumes that fields vary slowly on the scale of the lattice and are too weak to push electrons into other bands.

Combining the rules gives the acceleration. Near a band extremum, ε(k) is close to a parabola, and the electron responds as if it had mass m*, where 1/m* = (1/ħ²) d²ε/dk² in one dimension. In three dimensions this becomes an effective mass tensor. Flat bands give heavy electrons and sharply curved bands give light ones. Electrons in the conduction band of gallium arsenide, for example, have m* close to 0.067 times the free-electron mass. Near the top of a band the curvature is negative, so m* is negative: a force pushes the electron the opposite way.

A filled band carries no current, because velocities at k and −k cancel. A band with one electron missing therefore carries the current of that one missing electron, with the sign reversed. It is simpler to describe this as a single hole with charge +e. Holes sit near the top of a band, where the electron effective mass is negative, so the hole's effective mass is positive. Holes explain positive Hall coefficients in some metals and are the main carriers in p-type semiconductors.

The model makes a surprising prediction. In a constant electric field, k increases steadily and crosses the Brillouin zone. When it reaches the zone boundary it reappears at the opposite edge, and the velocity, which follows sin(ka) in a tight-binding band, oscillates. The electron moves back and forth instead of accelerating. These Bloch oscillations have period h/(eEa). In metals, scattering destroys them long before one period passes, but they have been seen in semiconductor superlattices and in cold atoms in optical lattices. Ordinary conduction arises because scattering keeps resetting the electrons, which the Boltzmann transport equation describes.
