---
id: rutherford-scattering
title: Rutherford Scattering and the Nuclear Atom
domain: physics
course: modern-physics
prerequisites:
- id: electric-charge-and-coulombs-law
  type: hard
- id: conservation-of-angular-momentum
  type: hard
- id: central-force-motion-analysis
  type: soft
- id: electric-potential-energy
  type: soft
builds-toward:
- cross-sections-scattering
- born-approximation
- nuclear-structure
tags:
- scattering
- nucleus
- cross-section
- atomic-models
stage: advanced
status: validated
---

# Rutherford Scattering and the Nuclear Atom

## Core Idea
In experiments reported in 1909, Hans Geiger and Ernest Marsden, working in Ernest Rutherford's laboratory, fired alpha particles at thin metal foils and found that a small fraction bounced back through large angles. In 1911 Rutherford explained this with a nuclear atom: nearly all the mass and all the positive charge sit in a tiny central nucleus. Treating each alpha particle as a charge moving on a hyperbolic path in the nucleus's Coulomb field gives the Rutherford formula, dσ/dΩ = (zZe²/(16πε₀K))² / sin⁴(θ/2). Its 1/sin⁴(θ/2) angular dependence matched the data and fixed the nuclear model of the atom.

## How It's Best Learned
Start with the plum-pudding model and estimate why it allows only tiny deflections. Then work the head-on collision with energy conservation to find the distance of closest approach. Next relate impact parameter to scattering angle and show how a beam spread over area turns into a differential cross-section. Compare the predicted counts at several angles with a table of data.

## Common Misconceptions
- The deflected alpha particles collide with the nucleus. (At the energies Geiger and Marsden used, the alpha particles never come close enough to touch the gold nucleus; the Coulomb repulsion turns them around tens of femtometres away.)
- Most alpha particles bounced back. (Most passed through with small deflections; only about one in several thousand was scattered through more than 90°.)
- The Rutherford formula needs quantum mechanics. (It follows from classical mechanics; the quantum calculation for a pure Coulomb potential happens to give the same result.)

## Questions

```yaml
- question: "According to the Rutherford formula, how does the scattering rate per unit solid angle at θ = 60° compare with the rate at θ = 180°?"
  type: multiple-choice
  options: ["The same", "4 times larger at 60°", "16 times larger at 60°", "16 times smaller at 60°"]
  answer: 2
  explanation: "dσ/dΩ ∝ 1/sin⁴(θ/2). At 60°, sin 30° = 0.5 and sin⁴ = 1/16. At 180°, sin 90° = 1. So the 60° rate is 16 times larger."
- question: "What feature of the Geiger-Marsden results ruled out Thomson's plum-pudding model?"
  type: multiple-choice
  options: ["Most alpha particles passed straight through", "Some alpha particles were deflected through very large angles", "The foil became positively charged", "The alpha particles lost all their energy in the foil"]
  answer: 1
  explanation: "Charge spread through a whole atom cannot produce a field strong enough to reverse a fast alpha particle. Large-angle scattering requires the positive charge to be concentrated in a very small region."
- question: "If the alpha particles' kinetic energy is doubled, the Rutherford cross-section at a fixed angle falls to one quarter of its original value."
  type: true-false
  answer: true
  explanation: "dσ/dΩ ∝ 1/K². Doubling K divides the cross-section by 4. Faster particles are deflected less at a given impact parameter."
- question: "Using e²/(4πε₀) = 1.44 MeV·fm, find the distance of closest approach for a 5.0 MeV alpha particle (z = 2) aimed head-on at a gold nucleus (Z = 79). How does it compare with the gold nuclear radius of about 7 fm?"
  type: short-answer
  answer: "About 45 fm, roughly six times the nuclear radius."
  explanation: "At closest approach all kinetic energy becomes potential energy: K = zZe²/(4πε₀d). So d = 2 × 79 × 1.44 MeV·fm / 5.0 MeV ≈ 45 fm. The alpha particle turns around well outside the nucleus."
```

## Explainer
Around 1904, J. J. Thomson's model pictured the atom as a sphere of spread-out positive charge with electrons embedded in it. In such an atom, an alpha particle passing through would feel only weak electric forces, because the positive charge is spread over the whole atom. Each atom could deflect it by a tiny fraction of a degree. Large deflections should essentially never happen.

Geiger and Marsden found otherwise. About one alpha particle in eight thousand striking a thin metal foil came back toward the source. Rutherford later said it was as if a shell fired at tissue paper had bounced back. He concluded that the positive charge and nearly all the mass of the atom must sit in a nucleus far smaller than the atom itself.

To test the idea, Rutherford treated an alpha particle of charge ze and kinetic energy K moving past a fixed nucleus of charge Ze. The repulsive inverse-square force gives a hyperbolic orbit. Angular momentum and energy conservation link the impact parameter b, the sideways offset of the incoming path, to the scattering angle θ:

b = (d/2) cot(θ/2), with d = zZe²/(4πε₀K).

Here d is the distance of closest approach in a head-on collision. A smaller impact parameter means a larger deflection.

A beam contains particles at every impact parameter. Those passing through a ring of radius b and width db are scattered into a cone between θ and θ + dθ. Dividing the ring's area by the solid angle of the cone gives the differential cross-section:

dσ/dΩ = (zZe²/(16πε₀K))² / sin⁴(θ/2).

In 1913 Geiger and Marsden checked the predictions over a wide range of angles. The counts followed the 1/sin⁴(θ/2) law, rose roughly with the square of the nuclear charge, and fell as 1/K², as the formula requires.

For 5 MeV alpha particles on gold, d is about 45 fm, while the gold nucleus has a radius near 7 fm. The particles never reach the nucleus, so the pure Coulomb formula works. At much higher energies the formula fails at large angles, because the particles come close enough to feel the strong nuclear force. The angle at which the failure begins gave early estimates of nuclear size. The same reasoning, comparing measured scattering with a point-charge prediction, is still used today to probe the structure of protons and nuclei.
