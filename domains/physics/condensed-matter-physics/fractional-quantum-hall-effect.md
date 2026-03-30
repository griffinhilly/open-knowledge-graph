---
id: fractional-quantum-hall-effect
title: Fractional Quantum Hall Effect
domain: physics
course: condensed-matter-physics
prerequisites:
- id: integer-quantum-hall-effect
  type: hard
tags:
- fractional-quantum-hall
- laughlin-wavefunction
- anyons
- topological-order
stage: expert
status: validated
---

# Fractional Quantum Hall Effect

## Core Idea
The fractional quantum Hall effect (FQHE) occurs at fractional Landau level fillings nu = p/q (most prominently nu = 1/3, 2/5, 3/7, ...) where electron-electron interactions in a partially filled Landau level create incompressible quantum liquid states. The Laughlin wavefunction Psi = product_{i<j} (z_i - z_j)^m exp(-sum|z_k|^2/4l_B^2) for nu = 1/m describes a state with no single-particle analog — it is an intrinsically many-body phenomenon. The quasiparticle excitations carry fractional charge e/m and obey fractional (anyonic) statistics, neither bosonic nor fermionic. The FQHE was the first example of topological order and remains the most dramatic manifestation of strong correlations in condensed matter.

## Questions

```yaml
- question: "The integer quantum Hall effect can be understood in a single-particle picture (filled Landau levels). The fractional quantum Hall effect cannot. Why?"
  type: multiple-choice
  options:
    - "Fractional filling means not enough electrons to fill a Landau level"
    - "At fractional filling, a single Landau level is partially occupied and all electrons have the same kinetic energy (the Landau level is flat/degenerate). With the kinetic energy quenched, electron-electron interactions completely determine the ground state. The resulting correlated many-body state has no single-particle description — it is an emergent collective phenomenon with properties (fractional charge, anyonic statistics) that no individual electron possesses"
    - "The magnetic field is stronger in the fractional case"
    - "Disorder prevents integer quantization at these fillings"
  answer: 1
  explanation: "This is the key conceptual point. In a partially filled, highly degenerate Landau level, the electrons must decide how to arrange themselves within that level. The answer is determined entirely by the Coulomb interaction, which selects an incompressible liquid state at special filling fractions. This state is qualitatively new — not a Slater determinant, not describable by any mean-field or band theory. The Laughlin state at ν = 1/3 was the first example of a state with topological order: its properties (ground state degeneracy on a torus, fractional quasiparticles) have no local order parameter description."

- question: "Quasiparticles in the ν = 1/3 Laughlin state carry charge e/3 and obey anyonic statistics. What does 'anyonic statistics' mean?"
  type: multiple-choice
  options:
    - "The quasiparticles can have any energy"
    - "When two quasiparticles are exchanged, the many-body wavefunction acquires a phase e^{iθ} with θ = π/3, intermediate between bosons (θ = 0) and fermions (θ = π). This is only possible in two dimensions, where the braid group (not the permutation group) governs particle exchanges"
    - "The quasiparticles obey classical statistics"
    - "Anyonic means the quasiparticles are neither particles nor waves"
  answer: 1
  explanation: "In 3D, exchanging two identical particles twice returns to the original configuration, so the phase must satisfy e^{2iθ} = 1, giving θ = 0 (bosons) or θ = π (fermions). In 2D, the double exchange is topologically distinct from no exchange (you cannot continuously deform one into the other), so θ can be any value — hence 'anyons.' For ν = 1/m Laughlin states, the statistics angle is θ = π/m. Anyonic statistics are not just a theoretical curiosity — they are the basis of topological quantum computation proposals, where information is encoded in the braiding of anyons and is inherently protected from local errors."

- question: "The Laughlin wavefunction was proposed as a variational guess, yet it captures the exact ground state physics at ν = 1/3 with remarkable accuracy."
  type: true-false
  answer: true
  explanation: "Laughlin's wavefunction Ψ = Π_{i<j}(z_i - z_j)³ exp(-Σ|z_k|²/4l_B²) was constructed by physical intuition: the (z_i - z_j)³ factor ensures each electron has a third-order zero when another approaches (keeping electrons apart efficiently) while maintaining the lowest Landau level constraint. Numerical exact diagonalization studies on small systems show that the overlap between the Laughlin state and the true Coulomb ground state exceeds 0.99. The wavefunction also gives the correct excitation spectrum, fractional charge, and topological degeneracy. This is one of the most successful variational wavefunctions in physics."

- question: "Explain why the fractional quantum Hall effect is considered a more fundamental phenomenon than the integer quantum Hall effect, from a theoretical perspective."
  type: short-answer
  answer: "The IQHE can be fully explained by single-particle physics (Landau levels + disorder + topology) — interactions are not essential. The FQHE is an intrinsically many-body phenomenon that arises entirely from electron-electron interactions in a degenerate Landau level. It represents a new class of quantum matter — topologically ordered states — that cannot be described by symmetry breaking or band topology alone. The FQHE ground state has properties with no single-particle analog: fractional charge, anyonic statistics, topological ground state degeneracy, and long-range entanglement. These properties define a new organizational principle for quantum matter that goes beyond Landau's symmetry-breaking paradigm."
  explanation: "The FQHE opened the era of topological order in condensed matter physics. Concepts first developed for the FQHE — anyons, topological degeneracy, edge conformal field theories, composite fermions — have become central to our understanding of strongly correlated quantum matter and are the foundation of proposals for topological quantum computation."
```

## Explainer

The **fractional quantum Hall effect**, discovered by Tsui, Stormer, and Gossard in 1982 (Nobel Prize 1998 with Laughlin), is one of the most remarkable phenomena in all of physics. At certain fractional Landau level fillings — most notably nu = 1/3, 2/5, 3/7, and their particle-hole conjugates — the Hall conductance is quantized at sigma_{xy} = (p/q)(e^2/h) with the same extraordinary precision as the integer effect. But unlike the IQHE, no single-particle picture can explain it: the FQHE is a purely interaction-driven phenomenon.

The physical setup is the same as the IQHE — a 2DEG in a strong magnetic field — but at fractional filling, a Landau level is partially occupied. Since all electrons in a Landau level have the same kinetic energy (the level is massively degenerate), the kinetic energy is "quenched" and the Coulomb interaction alone determines the ground state. **Laughlin** (1983) proposed a variational wavefunction for nu = 1/m: Psi = product_{i<j} (z_i - z_j)^m exp(-sum|z_k|^2/4l_B^2), where z_i = x_i + iy_i are complex coordinates. The (z_i - z_j)^m factor ensures that electrons avoid each other (each electron has an m-th order zero when another approaches), while the exponential confines them to the lowest Landau level. For m = 3 (nu = 1/3), this wavefunction has overlap >0.99 with the exact ground state.

The excitations of the Laughlin state are extraordinary. Creating a quasihole (by inserting a flux quantum) produces an excitation with **fractional charge** e/m = e/3 at nu = 1/3. This fractional charge has been directly measured through shot noise experiments. Even more remarkably, these quasiparticles obey **anyonic statistics**: exchanging two quasiholes multiplies the wavefunction by a phase e^{i pi/m}, intermediate between bosons (phase 1) and fermions (phase -1). Anyonic statistics are possible only in two spatial dimensions, where the topology of particle exchanges is richer than in 3D.

The broader significance of the FQHE is that it introduced the concept of **topological order** — a kind of quantum order that is not described by any local order parameter or symmetry breaking. The Laughlin state has a topological ground state degeneracy (m-fold on a torus), long-range quantum entanglement, and edge excitations described by a chiral Luttinger liquid. Composite fermion theory (Jain, 1989) extended the Laughlin picture to explain the full hierarchy of observed fractions: at nu = p/(2sp+1), electrons bind with 2s flux quanta to form composite fermions that then fill p integer Landau levels. The FQHE remains the most compelling example of emergent phenomena in condensed matter — properties of the collective state (fractional charge, anyonic statistics) that no individual electron possesses.
