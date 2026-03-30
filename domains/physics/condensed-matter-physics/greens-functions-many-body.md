---
id: greens-functions-many-body
title: Green's Functions in Many-Body Physics
domain: physics
course: condensed-matter-physics
prerequisites:
- id: fermi-liquid-theory
  type: hard
- id: creation-annihilation-operators
  type: hard
tags:
- greens-function
- self-energy
- spectral-function
- feynman-diagrams
stage: expert
status: validated
---

# Green's Functions in Many-Body Physics

## Core Idea
The single-particle Green's function G(k, omega) = 1/(omega - epsilon_k - Sigma(k, omega)) encodes the propagation of a single electron (or hole) through an interacting many-body system. The self-energy Sigma(k, omega) captures all interaction effects: its real part shifts the quasiparticle energy, and its imaginary part gives the quasiparticle lifetime. The spectral function A(k, omega) = -Im G(k, omega)/pi, which is directly measured by ARPES (angle-resolved photoemission spectroscopy), shows a sharp quasiparticle peak in a Fermi liquid and broad, incoherent features in strongly correlated systems. Feynman diagram techniques provide systematic perturbative approximations for Sigma.

## Questions

```yaml
- question: "The retarded Green's function G^R(k, t) = -iθ(t)<{c_k(t), c†_k(0)}>  describes the propagation of an added electron. What physical question does it answer?"
  type: multiple-choice
  options:
    - "It tells you the energy of the electron in the crystal"
    - "If you add an electron with momentum k at time 0 to the interacting ground state, G^R(k, t) gives the amplitude that the system still has that electron with momentum k at time t. In frequency space, the poles of G(k, ω) give the quasiparticle energies and lifetimes — the complete excitation spectrum of the interacting system as seen by adding or removing one electron"
    - "It describes the scattering of two electrons"
    - "It gives the pair correlation function between electrons"
  answer: 1
  explanation: "The Green's function is the fundamental propagator of the many-body system. It tells you everything about single-particle-like excitations: their energies (pole positions), lifetimes (pole widths), and spectral weight (residues). For a non-interacting system, G₀(k,ω) = 1/(ω - ε_k + iδ) has poles at the bare band energies with infinite lifetime. Interactions move the poles (renormalize energies), broaden them (finite lifetime), and redistribute spectral weight from the quasiparticle peak to an incoherent background."

- question: "The self-energy Σ(k, ω) is the central object in many-body perturbation theory. If you know Σ exactly, what do you know?"
  type: multiple-choice
  options:
    - "Only the electron-phonon coupling strength"
    - "Everything about single-particle excitations: the full Green's function G = 1/(ω - ε_k - Σ), from which you extract the quasiparticle dispersion E*(k) = ε_k + Re Σ(k, E*), the quasiparticle lifetime τ = ħ/|2 Im Σ|, the quasiparticle residue Z = (1 - ∂Re Σ/∂ω)^{-1}, and the spectral function A(k,ω). The self-energy is the complete encoding of all many-body effects on single-particle propagation"
    - "The total energy of the system"
    - "The self-energy only gives the effective mass"
  answer: 1
  explanation: "The Dyson equation G = G₀ + G₀ΣG means that Σ is the 'correction' to free propagation caused by interactions. Knowing Σ exactly gives the exact single-particle Green's function and thus the exact spectral function, quasiparticle properties, and single-particle density of states. In a Fermi liquid, Im Σ ~ (ω - E_F)² near E_F (giving long-lived quasiparticles), and the quasiparticle residue Z < 1 measures the fraction of spectral weight in the coherent peak versus the incoherent background."

- question: "ARPES (angle-resolved photoemission spectroscopy) measures the spectral function A(k, ω) = -(1/π)Im G(k, ω). In a Fermi liquid, A(k, ω) shows a sharp peak (quasiparticle) on a broad background (incoherent spectral weight)."
  type: true-false
  answer: true
  explanation: "This is the direct experimental test of many-body theory. In a non-interacting system, A(k,ω) is a delta function at ω = ε_k. In a Fermi liquid, interactions broaden the delta function into a Lorentzian of width Γ = |Im Σ| and shift it by Re Σ, while transferring some spectral weight (1-Z) to a broad incoherent continuum. ARPES on simple metals shows sharp quasiparticle peaks (Z ~ 0.7-0.9). On strongly correlated materials like cuprate superconductors, the peaks can be broad and Z small, indicating strong deviation from Fermi liquid behavior. ARPES on topological insulators reveals the surface Dirac cone directly."

- question: "Explain why Feynman diagrams are useful for computing the self-energy, and what the GW approximation captures physically."
  type: short-answer
  answer: "Feynman diagrams provide a systematic graphical expansion of the self-energy in powers of the interaction. Each diagram represents a specific physical process: electron-electron scattering, phonon emission/absorption, repeated scattering events. The diagrammatic approach allows selective summation of important classes of diagrams (e.g., all ring diagrams for screening) rather than computing all diagrams order by order. The GW approximation keeps only the simplest diagram: Σ = iGW, where G is the Green's function and W is the dynamically screened Coulomb interaction. Physically, GW describes an electron propagating through a medium that dynamically screens its Coulomb interaction with other electrons. It captures quasiparticle energy shifts and lifetimes and gives much more accurate band gaps than DFT (typically within 10% of experiment for semiconductors)."
  explanation: "The GW approximation is the standard 'beyond-DFT' method for computing quasiparticle band structures. It is the lowest-order diagram in the screened interaction W, which already includes the dominant correlation effect (screening). Higher-order diagrams (vertex corrections) are needed for strongly correlated systems."
```

## Explainer

Green's functions are the language of many-body quantum physics in condensed matter. While the wavefunction of N interacting electrons is hopelessly complex, the **single-particle Green's function** G(k, omega) extracts precisely the information relevant to experiments that add or remove one electron: photoemission, tunneling, transport, and optical absorption. It is defined as the Fourier transform of the time-ordered expectation value G(k, t-t') = -i<T c_k(t) c^dagger_k(t')>, where T denotes time ordering and the expectation value is taken in the interacting ground state.

For non-interacting electrons, G_0(k, omega) = 1/(omega - epsilon_k + i delta sgn(epsilon_k - E_F)) has simple poles at the bare band energies. Interactions modify G through the **self-energy** Sigma(k, omega), via the Dyson equation: G(k, omega) = 1/(omega - epsilon_k - Sigma(k, omega)). The self-energy is the sum of all "proper" (one-particle irreducible) interaction diagrams. Its real part shifts the quasiparticle energy: E*(k) = epsilon_k + Re Sigma(k, E*). Its imaginary part gives the quasiparticle decay rate: Gamma = |Im Sigma(k, E*)|, which translates to a lifetime tau = hbar/(2 Gamma).

The **spectral function** A(k, omega) = -(1/pi) Im G(k, omega) is the observable quantity — it is directly measured by ARPES. In a Fermi liquid, A(k, omega) near the Fermi surface consists of a sharp Lorentzian peak (the quasiparticle, with weight Z < 1 and width proportional to (omega - E_F)^2) sitting on top of a broad incoherent background (weight 1-Z). The quasiparticle residue Z = 1/(1 - partial Re Sigma/partial omega) measures how much of the single-particle character survives the dressing by interactions. In copper, Z ~ 0.8; in heavy fermion compounds, Z ~ 0.001; in a Mott insulator, Z = 0 (no quasiparticle).

Computing Sigma is the central technical challenge. **Feynman diagrams** provide a systematic perturbative expansion: each diagram represents a specific process (electron-hole pair creation, phonon exchange, repeated scattering) and contributes a specific integral to Sigma. The art is in selecting which diagrams to sum. The **GW approximation** (Sigma = i G W, where W is the screened Coulomb interaction) captures dynamic screening and gives accurate quasiparticle band structures for semiconductors and simple metals. **Dynamical mean-field theory** (DMFT) maps the lattice problem onto a self-consistent impurity problem, capturing local correlations and the Mott transition. The Green's function framework thus provides a unified language connecting microscopic many-body theory to experimentally measurable quantities.
