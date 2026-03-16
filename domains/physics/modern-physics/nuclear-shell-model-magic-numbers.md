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
stage: advanced
status: draft
---

# Nuclear Shell Model and Magic Numbers

## Core Idea
Nucleons fill quantum levels in a potential well (the nucleus). Closed shells (magic numbers: 2, 8, 20, 28, 50, 82, 126) correspond to filled levels and are exceptionally stable, analogous to noble gas electron shells. Nuclei with both Z and N equal to magic numbers (doubly magic nuclei like ⁴He, ¹⁶O, ⁴⁰Ca, ²⁰⁸Pb) are especially stable. The magic numbers explain deviations from simple liquid-drop-model predictions.

## How It's Best Learned
Identify magic and doubly magic nuclei in a table of isotopes. Compare their binding energies and decay modes with nearby nuclei. Relate to shell-filling in atoms and understand that nuclear levels depend on an effective potential, not the Coulomb potential.

## Common Misconceptions
Magic numbers are not the same in nuclei and atoms (nuclear magic numbers are 2, 8, 20, ..., not 2, 10, 18, ... as in atoms). The shell model predicts magic numbers correctly but is not a detailed quantum mechanical solution (it is a mean-field model).

## Explainer

You know from atomic physics that electrons in an atom fill quantum energy levels, and that the Pauli exclusion principle forces each electron into a distinct quantum state. Noble gas elements — helium, neon, argon — have completely filled electron shells, which makes them exceptionally chemically inert and stable. The nuclear shell model asks whether nucleons (protons and neutrons) obey the same logic inside the nucleus. The answer, discovered by Maria Goeppert Mayer in 1948, is yes — but the numbers come out differently.

The starting point is the **mean-field approximation**: instead of tracking the interactions of all A nucleons simultaneously (an intractable many-body problem), treat each nucleon as moving independently in an average potential created by all the others. This **nuclear potential well** is roughly a finite square well or Woods-Saxon potential — deep inside the nucleus and dropping to zero outside. Solving the quantum mechanics of a single nucleon in this well gives discrete energy levels, just as solving the hydrogen atom gives discrete orbital levels. Each level can hold a fixed number of nucleons consistent with the Pauli principle and spin degeneracy.

The key insight that Mayer added was a strong **spin-orbit coupling** term in the nuclear potential: the energy of a nucleon depends significantly on whether its spin angular momentum is aligned or anti-aligned with its orbital angular momentum. This splitting rearranges the energy-level ordering compared to a simple harmonic well, and it creates large energy gaps — **shell closures** — after filling 2, 8, 20, 28, 50, 82, and 126 nucleons. These are the **magic numbers**. A nucleus with a magic number of protons or neutrons has all its nucleons in a complete shell and the next level is far above in energy. This makes the nucleus especially tightly bound and resistant to excitation or decay.

The evidence is compelling. Magic-number nuclei have anomalously high binding energies compared to the liquid-drop model prediction, extra-low neutron-capture cross sections (they don't easily absorb additional neutrons), and unusual prevalence in nature — tin (Z = 50) has ten stable isotopes, far more than its neighbors. **Doubly magic** nuclei like ⁴He (Z=2, N=2), ¹⁶O (Z=8, N=8), ⁴⁰Ca (Z=20, N=20), and ²⁰⁸Pb (Z=82, N=126) are the nuclear equivalents of noble gases: the most stable configurations in their region of the chart of nuclides. The difference from atomic magic numbers (2, 10, 18, 36...) reflects the different shape and nature of the nuclear potential — the strong force, not the Coulomb force, dominates, and the spin-orbit term in nuclei is much larger relative to other energy scales than it is in atoms.
