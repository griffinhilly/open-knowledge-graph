---
id: qed-vertex-basic-processes
title: QED Vertex and Basic Processes
domain: physics
course: quantum-field-theory
prerequisites:
- id: feynman-diagrams-systematic
  type: hard
- id: dirac-field-quantization
  type: hard
- id: electromagnetic-field-quantization
  type: hard
tags:
- qed
- vertex
- compton-scattering
- pair-annihilation
stage: expert
status: validated
---

# QED Vertex and Basic Processes

## Core Idea
The QED interaction vertex couples an electron, a positron, and a photon with vertex factor -ie gamma^mu. All electromagnetic processes -- Compton scattering, pair annihilation, Bhabha scattering, Moller scattering -- are built from combinations of this single vertex. The coupling strength is alpha = e^2/(4pi) approximately 1/137.

## Questions

```yaml
- question: "All of QED is built from a single vertex: an electron line, a positron line, and a photon line meeting at a point, with factor -ie gamma^mu. Why can't there be a vertex with two photon lines and no fermion lines?"
  type: multiple-choice
  options:
    - "Because photons are electrically neutral and do not couple directly to each other — the photon-photon interaction is absent from the QED Lagrangian because it is not gauge invariant"
    - "Because two photons would violate energy conservation"
    - "Because the Dirac equation does not allow it"
    - "Because photon-photon scattering has never been observed experimentally"
  answer: 0
  explanation: "The QED Lagrangian is L = psi-bar(i gamma^mu D_mu - m)psi - (1/4)F^2, where D_mu = partial_mu + ieA_mu is the covariant derivative. The interaction term is -e psi-bar gamma^mu psi A_mu, which involves exactly one photon field and two fermion fields. There is no A^3 or A^4 term because the electromagnetic field is abelian (U(1) gauge theory). Photon-photon scattering does occur in QED, but only through a fermion loop (a box diagram with four vertices), making it a higher-order process suppressed by alpha^2. Direct photon self-coupling is a feature of non-abelian gauge theories like QCD."

- question: "Compton scattering (photon + electron -> photon + electron) has two tree-level Feynman diagrams. These are the s-channel (electron absorbs the photon, propagates, then emits the final photon) and the u-channel (crossed diagram). Why is there no t-channel diagram?"
  type: multiple-choice
  options:
    - "A t-channel diagram would have a photon exchanged between two electrons, but there is only one electron in Compton scattering"
    - "A t-channel diagram would require a photon-photon-electron vertex, which does not exist in QED — the exchanged particle would need to couple to two photons on one side, but the QED vertex always has exactly one photon"
    - "The t-channel is suppressed by an additional power of alpha"
    - "The t-channel diagram is included in the s-channel after crossing symmetry"
  answer: 1
  explanation: "In the t-channel, the exchanged particle would connect an incoming electron-outgoing electron vertex on one side and an incoming photon-outgoing photon vertex on the other. The first vertex exists (-ie gamma^mu), but the second would require a photon-photon coupling, which is absent from QED at tree level. The only tree-level diagrams for Compton scattering are those where the electron propagates between the two photon-electron vertices: one where absorption precedes emission (s-channel) and one with the opposite order (u-channel). Both diagrams must be included and their amplitudes added before squaring."

- question: "Electron-positron annihilation into two photons (e+e- -> gamma gamma) is closely related to Compton scattering by crossing symmetry."
  type: true-false
  answer: true
  explanation: "Crossing symmetry relates processes obtained by moving particles between the initial and final states (and replacing particles with antiparticles). Compton scattering (e + gamma -> e + gamma) becomes pair annihilation (e + e+ -> gamma + gamma) when you cross the final-state electron into an initial-state positron and the initial-state photon into a final-state photon. The Feynman diagrams have the same topology, and the amplitudes are related by analytic continuation of the Mandelstam variables (s <-> t or s <-> u). This means you can often compute one process and obtain the others by relabeling momenta."

- question: "Calculate the tree-level amplitude for electron-muon scattering (e- mu- -> e- mu-) and explain why this is the simplest non-trivial QED process."
  type: short-answer
  answer: "There is only one tree-level diagram: a single virtual photon exchanged in the t-channel. The amplitude is M = (-ie)^2 [u-bar(p3) gamma^mu u(p1)] (-ig_{mu nu}/q^2) [u-bar(p4) gamma^nu u(p2)] = ie^2 [u-bar(p3) gamma^mu u(p1)] [u-bar(p4) gamma_mu u(p2)] / q^2, where q = p1 - p3 is the momentum transfer. This is the simplest non-trivial QED process because the electron and muon are distinguishable, so there is no exchange (u-channel) diagram and no identical-particle complications. The single diagram has two vertices (factor e^2), one photon propagator (factor 1/q^2), and two fermion currents."
  explanation: "This amplitude is the prototype for all QED calculations. The structure — two fermion currents connected by a photon propagator — appears in every electromagnetic scattering process. More complex processes (Bhabha scattering, Moller scattering) add exchange diagrams or additional channels but are built from the same ingredients."
```

## Explainer

Quantum electrodynamics is built from a single interaction: the coupling of an electron (or any charged fermion) to a photon. In the Lagrangian, this coupling appears as L_int = -e psi-bar gamma^mu psi A_mu, and in Feynman diagrams it is represented by a vertex where an electron line, a positron line (or equivalently, an electron line with reversed arrow), and a photon line meet. The vertex factor is -ie gamma^mu, and the coupling constant is e, related to the fine structure constant by alpha = e^2/(4pi) approximately 1/137.

Every electromagnetic process in nature is built from this one vertex. **Electron-muon scattering** uses two vertices connected by a single photon propagator (t-channel exchange). **Compton scattering** (photon + electron -> photon + electron) has two diagrams at tree level (s-channel and u-channel). **Pair annihilation** (e+e- -> gamma gamma) is related to Compton scattering by crossing symmetry. **Bhabha scattering** (e+e- -> e+e-) has both t-channel (photon exchange) and s-channel (annihilation) diagrams. **Moller scattering** (e-e- -> e-e-) has t-channel and u-channel diagrams with a relative minus sign from Fermi statistics.

The computation of any tree-level QED process follows a mechanical procedure. Write down all topologically distinct Feynman diagrams. For each diagram: assign momenta to all lines (internal and external), write down the spinor/polarization factors for external lines, write the propagators for internal lines, include the vertex factor -ie gamma^mu at each vertex, impose momentum conservation at each vertex, and multiply everything together. For processes with identical external fermions, include a relative minus sign between diagrams related by exchange of two external fermion lines.

The remarkable fact about QED is how much physics follows from this one vertex. The Coulomb force, the Lamb shift, the anomalous magnetic moment of the electron, pair production, Compton scattering, Bremsstrahlung -- all are consequences of a single coupling. The precision of QED predictions (the electron g-2 agrees with experiment to better than one part in 10^12) validates the framework of perturbative quantum field theory to an extraordinary degree. QED serves as the template for all gauge theories, including the weak and strong interactions.
