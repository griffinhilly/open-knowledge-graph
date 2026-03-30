---
id: confinement-and-hadrons
title: Confinement and Hadrons
domain: physics
course: quantum-field-theory
prerequisites:
- id: asymptotic-freedom
  type: hard
- id: qcd-basics
  type: hard
tags:
- confinement
- hadrons
- mesons
- baryons
stage: expert
status: validated
---

# Confinement and Hadrons

## Core Idea
Color confinement is the phenomenon that quarks and gluons cannot exist as free particles -- they are always bound into color-neutral hadrons (mesons, baryons). The quark-antiquark potential grows linearly at large distances, making separation impossible. Confinement is a non-perturbative effect that has been confirmed numerically by lattice QCD but lacks a rigorous analytical proof.

## Questions

```yaml
- question: "The potential between a quark and an antiquark at large separation r goes as V(r) ~ sigma r, where sigma (the string tension) is approximately 1 GeV/fm. What happens physically when you try to pull a quark-antiquark pair apart?"
  type: multiple-choice
  options:
    - "The quarks accelerate away from each other until they escape"
    - "The energy stored in the color flux tube grows until it exceeds 2 m_q, at which point a new quark-antiquark pair is created from the vacuum — you end up with two mesons instead of two free quarks"
    - "The potential eventually flattens to a constant, allowing separation at sufficient energy"
    - "The quarks radiate gluons that carry away the excess energy"
  answer: 1
  explanation: "This is string breaking. The color flux tube between the quark and antiquark stores energy proportional to its length. When the energy exceeds the rest mass of a quark-antiquark pair (about 300 MeV for light quarks), it is energetically favorable to create a new pair from the vacuum. The newly created quark binds with the original antiquark, and the newly created antiquark binds with the original quark, producing two separate mesons. You can never isolate a single quark — adding energy simply creates more hadrons. This is why high-energy collisions produce jets of hadrons rather than free quarks."

- question: "Lattice QCD is a method for computing QCD predictions non-perturbatively by discretizing spacetime on a grid and evaluating the path integral numerically. It has successfully computed the proton mass to within a few percent of the experimental value."
  type: true-false
  answer: true
  explanation: "Lattice QCD replaces continuous spacetime with a discrete lattice (typically with spacing a ~ 0.1 fm), which provides a natural ultraviolet cutoff. The path integral becomes a finite-dimensional integral that can be evaluated by Monte Carlo methods. The proton mass (938 MeV), computed from first principles with no free parameters except the quark masses and the QCD coupling, agrees with experiment to within about 2%. Lattice QCD has also successfully computed meson masses, the pion decay constant, and other non-perturbative quantities. It is currently the only systematic method for first-principles calculations in the confining regime of QCD."

- question: "All observed hadrons are either mesons (quark-antiquark) or baryons (three quarks). Exotic hadrons like tetraquarks (two quarks + two antiquarks) or pentaquarks are forbidden by QCD."
  type: true-false
  answer: false
  explanation: "QCD requires hadrons to be color-neutral, but this does not restrict them to only mesons (q q-bar) and baryons (qqq). Any color-singlet combination is allowed. Tetraquarks (qq q-bar q-bar), pentaquarks (qqqq q-bar), and glueballs (bound states of gluons with no quarks) are all consistent with QCD. Several tetraquark and pentaquark candidates have been observed at the LHC and other experiments (e.g., the X(3872), Z_c(3900), and the P_c pentaquark states discovered by LHCb in 2015 and 2019). These exotic hadrons are more difficult to produce and identify than conventional mesons and baryons, but they are real predictions of QCD."

- question: "Explain why approximately 99% of the proton's mass comes from the energy of the gluon field and quark kinetic energy, rather than from the intrinsic masses of the quarks."
  type: short-answer
  answer: "The proton mass is approximately 938 MeV. The up and down quark masses are approximately 2-5 MeV each, totaling about 10 MeV for the three valence quarks — roughly 1% of the proton mass. The remaining 99% comes from two sources: the kinetic energy of the confined quarks (the uncertainty principle requires large momenta when quarks are confined to a region of size ~1 fm) and the energy stored in the gluon field that binds them. This is a purely relativistic and quantum effect: E = mc^2 applied to the field energy gives the proton its mass. In this sense, most of the mass of ordinary matter is 'made of' the energy of the strong force rather than the intrinsic masses of quarks."
  explanation: "This is confirmed by lattice QCD, which computes the proton mass from the QCD Lagrangian with light quark masses as inputs. If you set the quark masses to zero (the chiral limit), the proton mass decreases by only about 5-10%, not to zero. The strong interaction generates mass from pure energy — a dramatic manifestation of E = mc^2."
```

## Explainer

**Confinement** is the most distinctive property of QCD and has no analog in electromagnetism. While the electromagnetic potential between two charges falls off as 1/r (allowing charges to be separated to arbitrary distances), the QCD potential between a quark and an antiquark grows linearly at large distances: V(r) approximately -4 alpha_s/(3r) + sigma r. The first term is the perturbative Coulomb-like potential (dominant at short distances); the second is the confining term (dominant at large distances), where sigma approximately 1 GeV/fm is the **string tension**. The linear potential means that infinite energy would be required to separate a quark from an antiquark -- but before this happens, the flux tube breaks by creating a new quark-antiquark pair from the vacuum.

The physical picture is that the color electric field between a quark-antiquark pair does not spread out as it does in QED. Instead, gluon self-interactions squeeze the field into a narrow **flux tube** (or string) of roughly constant cross-section, approximately 1 fm^2. The energy stored in this tube is proportional to its length, giving the linear potential. When the tube's energy exceeds the pair-creation threshold, it snaps, producing new hadrons. This is why high-energy collisions produce **jets**: a knocked-out quark drags a flux tube behind it, which fragments into a shower of mesons and baryons moving roughly in the same direction.

The observable particles -- **hadrons** -- are color-neutral combinations of quarks and gluons. Mesons consist of a quark and an antiquark (whose color and anti-color combine to a singlet). Baryons consist of three quarks (one of each color, combining to a singlet via the antisymmetric epsilon tensor). More exotic combinations (tetraquarks, pentaquarks, glueballs) are allowed by color neutrality and have been observed experimentally in recent years.

A remarkable consequence of confinement is that nearly all the mass of ordinary matter comes from the energy of the strong force, not from the intrinsic masses of quarks. The up and down quark masses total about 10 MeV, but the proton mass is 938 MeV. The remaining 99% is gluon field energy and quark kinetic energy, computed from first principles by **lattice QCD**. This numerical approach discretizes spacetime and evaluates the QCD path integral on a computer, providing non-perturbative predictions that agree with experiment. A rigorous analytical proof of confinement from the QCD Lagrangian remains one of the unsolved Millennium Prize Problems.
