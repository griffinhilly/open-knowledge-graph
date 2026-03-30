---
id: nuclear-shell-model-magic-numbers
title: Nuclear Shell Model and Magic Numbers
domain: physics
course: modern-physics
prerequisites:
- id: nuclear-structure
  type: hard
- id: pauli-exclusion-principle
  type: hard
- id: nuclear-stability-binding-curve
  type: soft
tags:
- nuclear-structure
- shell-model
- magic-numbers
stage: expert
status: validated
---

# Nuclear Shell Model and Magic Numbers

## Core Idea
Nucleons fill quantum levels in a potential well (the nucleus). Closed shells (magic numbers: 2, 8, 20, 28, 50, 82, 126) correspond to filled levels and are exceptionally stable, analogous to noble gas electron shells. Nuclei with both Z and N equal to magic numbers (doubly magic nuclei like ⁴He, ¹⁶O, ⁴⁰Ca, ²⁰⁸Pb) are especially stable. The magic numbers explain deviations from simple liquid-drop-model predictions.

## How It's Best Learned
Identify magic and doubly magic nuclei in a table of isotopes. Compare their binding energies and decay modes with nearby nuclei. Relate to shell-filling in atoms and understand that nuclear levels depend on an effective potential, not the Coulomb potential.

## Common Misconceptions
Magic numbers are not the same in nuclei and atoms (nuclear magic numbers are 2, 8, 20, ..., not 2, 10, 18, ... as in atoms). The shell model predicts magic numbers correctly but is not a detailed quantum mechanical solution (it is a mean-field model).

## Questions

```yaml
- question: "The nuclear magic numbers (2, 8, 20, 28, 50, 82, 126) differ from the atomic magic numbers (2, 10, 18, 36, 54, 86). What is the primary reason for this difference?"
  type: multiple-choice
  options:
    - "Nucleons obey Fermi-Dirac statistics differently than electrons, so their energy levels are populated in a different order"
    - "The nuclear potential is governed by the strong force (not the Coulomb force) and has much stronger spin-orbit coupling, which rearranges the energy level ordering and creates different shell gaps"
    - "Nucleons have higher mass than electrons, which shifts the zero-point energy and changes the level ordering"
    - "The nuclear shell model uses a harmonic oscillator potential instead of a Coulomb potential, which happens to produce the magic numbers by coincidence"
  answer: 1
  explanation: "The key difference is the nature of the potential and the strength of spin-orbit coupling. Atomic magic numbers come from filling shells in a Coulomb (electrostatic) potential with weak spin-orbit coupling. Nuclear magic numbers require the spin-orbit term to be large — comparable to the spacing between major shells. This strong spin-orbit splitting reorganizes the level ordering, breaking the harmonic oscillator magic numbers (2, 8, 20, 40, 70...) and shifting them to (2, 8, 20, 28, 50, 82, 126). Maria Goeppert Mayer's key insight was that only a large spin-orbit term could reproduce the observed nuclear magic numbers."

- question: "A nucleus has Z = 50 protons and N = 82 neutrons. How would you expect its binding energy to compare to neighboring nuclei?"
  type: multiple-choice
  options:
    - "Lower binding energy than neighbors, because having 50 protons means high Coulomb repulsion, which destabilizes the nucleus"
    - "About average for nuclei in that mass range, since binding energy mainly depends on A = Z + N"
    - "Higher binding energy than neighbors, because both Z = 50 and N = 82 are magic numbers — this is a doubly magic nucleus with both proton and neutron shells closed"
    - "Higher binding energy only if N is also magic; Z = 50 alone provides no stability advantage"
  answer: 2
  explanation: "This is a doubly magic nucleus: Z = 50 (tin) is a proton magic number and N = 82 is a neutron magic number. Both the proton shell and the neutron shell are closed, meaning the next nucleon of either type would have to occupy a much higher energy level. This makes the nucleus exceptionally tightly bound. Doubly magic nuclei show anomalously high binding energies compared to liquid-drop model predictions, extra-low neutron-capture cross sections, and unusual abundance. Tin (Z = 50) has 10 stable isotopes — far more than its neighbors — partly because the magic proton number makes many neutron-number configurations stable."

- question: "In the nuclear shell model, the magic number 28 arises from the same energy-level filling pattern that gives the atomic magic number 18 (argon)."
  type: true-false
  answer: false
  explanation: "The nuclear and atomic magic numbers are fundamentally different because the underlying potentials are different. Atomic magic number 18 (argon) corresponds to filling the 3p subshell in a Coulomb potential with weak spin-orbit coupling. Nuclear magic number 28 arises from a shell gap created by strong spin-orbit splitting in the nuclear (Woods-Saxon) potential — the 1f_{7/2} subshell fills and the next level is far above. The level-filling sequences are entirely different. Without the large nuclear spin-orbit term, the nuclear magic numbers would be the harmonic oscillator magic numbers (2, 8, 20, 40, 70...), not the observed ones."

- question: "A nucleus at or near a magic number has lower neutron-capture cross sections than its neighbors, meaning it is less likely to absorb an additional neutron."
  type: true-false
  answer: true
  explanation: "This is correct and is one of the key experimental signatures of nuclear shell closures. When a magic nucleus absorbs a neutron, that neutron would have to occupy the next shell — which is much higher in energy than the closed shell. The transition matrix element for this process is small, giving a low cross section. This was one of the empirical facts that motivated the development of the nuclear shell model: magic-number nuclei are systematically less reactive to neutron capture than their neighbors, a pattern that cannot be explained by the liquid-drop model but follows naturally from shell structure."

- question: "What role did spin-orbit coupling play in the development of the nuclear shell model, and why was its inclusion necessary to reproduce the observed magic numbers?"
  type: short-answer
  answer: "Without spin-orbit coupling, nuclear energy levels follow a pattern similar to a harmonic oscillator or square well, producing shell gaps after 2, 8, 20, 40, 70 nucleons — not the observed magic numbers. Maria Goeppert Mayer realized that including a strong spin-orbit term — which shifts levels by an amount proportional to the dot product of orbital and spin angular momenta — rearranges the level ordering. Specifically, it lowers the energy of states with spin aligned with orbital angular momentum (j = l + 1/2) relative to anti-aligned states (j = l - 1/2). This splitting is large enough in nuclei to move high-j states from one major shell into the one below, creating the large gaps after 28, 50, 82, and 126 that define the magic numbers."
  explanation: "The spin-orbit term in nuclei is much larger relative to other energy scales than in atoms — this is why the atomic and nuclear shell models, while analogous in structure, produce different magic numbers. In atoms, spin-orbit coupling is a small relativistic correction. In nuclei, it is comparable in size to the spacing between major shells, which is why it can dramatically rearrange the level ordering. Mayer's insight was recognized with the Nobel Prize in Physics (1963), shared with J.H.D. Jensen who independently reached the same conclusion."
```

## Explainer

You know from atomic physics that electrons in an atom fill quantum energy levels, and that the Pauli exclusion principle forces each electron into a distinct quantum state. Noble gas elements — helium, neon, argon — have completely filled electron shells, which makes them exceptionally chemically inert and stable. The nuclear shell model asks whether nucleons (protons and neutrons) obey the same logic inside the nucleus. The answer, discovered by Maria Goeppert Mayer in 1948, is yes — but the numbers come out differently.

The starting point is the **mean-field approximation**: instead of tracking the interactions of all A nucleons simultaneously (an intractable many-body problem), treat each nucleon as moving independently in an average potential created by all the others. This **nuclear potential well** is roughly a finite square well or Woods-Saxon potential — deep inside the nucleus and dropping to zero outside. Solving the quantum mechanics of a single nucleon in this well gives discrete energy levels, just as solving the hydrogen atom gives discrete orbital levels. Each level can hold a fixed number of nucleons consistent with the Pauli principle and spin degeneracy.

The key insight that Mayer added was a strong **spin-orbit coupling** term in the nuclear potential: the energy of a nucleon depends significantly on whether its spin angular momentum is aligned or anti-aligned with its orbital angular momentum. This splitting rearranges the energy-level ordering compared to a simple harmonic well, and it creates large energy gaps — **shell closures** — after filling 2, 8, 20, 28, 50, 82, and 126 nucleons. These are the **magic numbers**. A nucleus with a magic number of protons or neutrons has all its nucleons in a complete shell and the next level is far above in energy. This makes the nucleus especially tightly bound and resistant to excitation or decay.

The evidence is compelling. Magic-number nuclei have anomalously high binding energies compared to the liquid-drop model prediction, extra-low neutron-capture cross sections (they don't easily absorb additional neutrons), and unusual prevalence in nature — tin (Z = 50) has ten stable isotopes, far more than its neighbors. **Doubly magic** nuclei like ⁴He (Z=2, N=2), ¹⁶O (Z=8, N=8), ⁴⁰Ca (Z=20, N=20), and ²⁰⁸Pb (Z=82, N=126) are the nuclear equivalents of noble gases: the most stable configurations in their region of the chart of nuclides. The difference from atomic magic numbers (2, 10, 18, 36...) reflects the different shape and nature of the nuclear potential — the strong force, not the Coulomb force, dominates, and the spin-orbit term in nuclei is much larger relative to other energy scales than it is in atoms.
