---
id: loop-diagrams-divergences
title: Loop Diagrams and Divergences
domain: physics
course: quantum-field-theory
prerequisites:
- id: feynman-diagrams-systematic
  type: hard
- id: qed-vertex-basic-processes
  type: hard
tags:
- loop-diagrams
- divergences
- ultraviolet
- infrared
stage: expert
status: validated
---

# Loop Diagrams and Divergences

## Core Idea
Loop diagrams arise at higher orders in perturbation theory and involve integrals over undetermined internal momenta. These integrals often diverge: ultraviolet (UV) divergences come from high momenta (short distances) and infrared (IR) divergences from low momenta (long distances). Understanding and controlling these divergences is essential for extracting finite, physical predictions.

## Questions

```yaml
- question: "A one-loop Feynman diagram has one undetermined internal momentum that must be integrated over all values. The electron self-energy diagram in QED integrates over a loop momentum k from 0 to infinity. Why does this integral diverge?"
  type: multiple-choice
  options:
    - "Because the integrand oscillates without damping"
    - "At large k, the integrand falls off as 1/k^2 while the four-dimensional integration measure grows as k^3 dk — the integral diverges logarithmically because 1/k^2 times k^3 = k grows without bound"
    - "Because the electron propagator in the loop has a pole on the real axis"
    - "Because the photon is massless, creating an infrared divergence"
  answer: 1
  explanation: "In four spacetime dimensions, the loop integration measure is d^4k ~ k^3 dk (in spherical coordinates). The electron self-energy has a fermion propagator (~1/k) and a photon propagator (~1/k^2) in the loop, giving an integrand that falls as 1/k^3 at large k. Combined with the measure k^3 dk, the integral goes as dk/k ~ ln(k), which diverges logarithmically as k -> infinity. This is an ultraviolet divergence — it comes from arbitrarily high momenta (equivalently, arbitrarily short distances). Different diagrams have different power-counting behavior; some diverge quadratically, some logarithmically, and some are finite."

- question: "Ultraviolet divergences indicate that QFT is mathematically inconsistent and must be replaced by a fundamentally different theory at high energies."
  type: true-false
  answer: false
  explanation: "UV divergences do not mean the theory is inconsistent. They mean that the bare parameters in the Lagrangian (bare mass, bare charge) are not the physical parameters. Renormalization absorbs the divergences into redefinitions of these parameters, yielding finite predictions for all physical observables. The renormalized theory is perfectly well-defined and makes extraordinarily precise predictions (QED's electron g-2 agrees with experiment to 12 digits). What UV divergences may indicate is that the theory is an effective field theory — valid up to some energy scale but potentially replaced by a more complete theory at higher energies. But as a computational framework, renormalizable QFT is entirely self-consistent."

- question: "The vacuum polarization diagram (a fermion loop inserted into a photon propagator) modifies the photon propagator. What is the physical effect of this modification?"
  type: multiple-choice
  options:
    - "It gives the photon a mass"
    - "It screens the bare electric charge at long distances — the effective charge is smaller at low energies and increases at higher energies (shorter distances), because virtual electron-positron pairs polarize the vacuum like a dielectric"
    - "It causes the photon to decay into electron-positron pairs"
    - "It violates gauge invariance"
  answer: 1
  explanation: "Virtual electron-positron pairs in the vacuum act as electric dipoles that partially screen the bare charge. At large distances (low energies), the screening is maximal and the measured charge is the familiar alpha ~ 1/137. At shorter distances (higher energies), you probe inside the screening cloud and see a larger effective charge. This is the running of the QED coupling constant. The photon does not acquire a mass — gauge invariance (enforced by the Ward identity) guarantees that the vacuum polarization tensor is transverse, which protects the photon's masslessness."

- question: "Explain the difference between ultraviolet and infrared divergences, and give a physical example of each in QED."
  type: short-answer
  answer: "Ultraviolet divergences arise from loop momenta going to infinity (equivalently, distances going to zero) and indicate sensitivity to short-distance physics. Example: the electron self-energy, where a virtual photon is emitted and reabsorbed — the integral over the photon's momentum diverges logarithmically at high momentum. Infrared divergences arise from loop momenta going to zero (long distances) and are related to the emission of very soft (low-energy) photons. Example: the vertex correction in QED diverges logarithmically as the photon momentum goes to zero. IR divergences cancel when you include the corresponding real emission process (Bremsstrahlung) — the Bloch-Nordsieck theorem guarantees this cancellation for any process where you sum over all possible soft photon emissions."
  explanation: "UV and IR divergences have completely different origins and resolutions. UV divergences are handled by renormalization (redefining bare parameters). IR divergences cancel between virtual corrections and real emission when you compute physically measurable (inclusive) cross sections. The KLN (Kinoshita-Lee-Nauenberg) theorem generalizes this: all IR divergences cancel in sufficiently inclusive observables."
```

## Explainer

Tree-level Feynman diagrams give the leading-order predictions of quantum field theory. The next level of precision requires **loop diagrams**, in which one or more internal propagators form closed loops. Each loop introduces an integral over an undetermined four-momentum, and these integrals frequently diverge. Understanding the nature and origin of these divergences is the gateway to renormalization.

**Ultraviolet (UV) divergences** arise from the high-momentum (short-distance) behavior of loop integrals. In four dimensions, the integration measure d^4k grows as k^3 dk, while propagators fall off as powers of 1/k. If the measure grows faster than the propagators fall, the integral diverges. Simple power counting determines the degree of divergence: for a diagram with L loops, I internal lines, and V vertices, the superficial degree of divergence is D = 4L - 2I_B - I_F (where I_B and I_F count boson and fermion propagators). If D >= 0, the diagram diverges (quadratically for D = 2, logarithmically for D = 0). Only a finite number of diagram types are divergent in renormalizable theories — this is what makes renormalization possible.

**Infrared (IR) divergences** arise from the low-momentum (long-distance) behavior and are associated with massless particles. In QED, virtual photons with very low momentum give logarithmic divergences in loop integrals. These are not handled by renormalization but instead cancel when you ask the right physical question. No detector can distinguish between an electron and an electron accompanied by a very soft photon, so the physically measurable quantity includes both virtual and real soft photon contributions. The **Bloch-Nordsieck theorem** guarantees that IR divergences from virtual loops cancel against those from real soft photon emission in any inclusive cross section.

The three UV-divergent diagrams in QED are the electron self-energy (fermion loop correction to the electron propagator), the vacuum polarization (fermion loop correction to the photon propagator), and the vertex correction (photon-electron vertex with a loop). These three diagrams generate all the divergences of QED at every order in perturbation theory. The self-energy renormalizes the electron mass and wave function, the vacuum polarization renormalizes the electric charge, and the vertex correction renormalizes the coupling. All other diagrams either are finite or contain these three as subdiagrams. This finiteness of the set of divergent structures is the hallmark of a renormalizable theory.
