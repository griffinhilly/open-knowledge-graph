---
id: hydrogen-quantum-energy-levels
title: 'Hydrogen Atom: Quantum Energy Levels and Orbitals'
domain: physics
course: modern-physics
prerequisites:
- id: hydrogen-atom-quantum
  type: hard
- id: schrodinger-equation-intro
  type: soft
- id: eigenvalues-and-eigenvectors
  type: hard
- id: spherical-harmonics-electrostatics
  type: soft
- id: stark-effect-electric-field-splitting
  type: soft
- id: bohr-model-to-quantum
  type: soft
builds-toward:
- atomic-orbitals-shapes-nodes
tags:
- atomic-physics
- hydrogen
stage: advanced
status: validated
---
# Hydrogen Atom: Quantum Energy Levels and Orbitals

## Core Idea
Solutions to the Schrödinger equation for hydrogen give energy levels E_n = −13.6 eV/n², matching Bohr's prediction and explaining spectral lines. Each level is labeled by principal quantum number n. Unlike Bohr's orbits, quantum mechanics gives probability densities (orbitals) for finding the electron at various distances from the nucleus, with characteristic spatial shapes determined by angular momentum quantum numbers.

## Questions

```yaml
- question: "Two hydrogen orbitals have quantum numbers (n=2, l=0, m=0) and (n=2, l=1, m=0) respectively. What can you say about their energies?"
  type: multiple-choice
  options:
    - "The 2p orbital (l=1) has lower energy because angular momentum stabilizes the electron"
    - "The 2s orbital (l=0) has lower energy because s electrons penetrate closer to the nucleus"
    - "Both orbitals have the same energy — in hydrogen, energy depends only on the principal quantum number n"
    - "Their energies cannot be compared without knowing the electron's spin quantum number"
  answer: 2
  explanation: "In hydrogen, the energy eigenvalues E_n = −13.6 eV/n² depend only on n, not on l or m_l. Both the 2s and 2p orbitals have n=2, so both have energy E₂ = −3.4 eV. Options A and B describe real effects — in multi-electron atoms, l does affect energy through shielding and penetration — but these effects arise from electron-electron repulsion, which doesn't exist in hydrogen. This confusion between hydrogen and many-electron atoms is one of the most common errors in atomic physics."

- question: "The 1s orbital of hydrogen has its highest probability density at the nucleus (r=0). What does this mean about where the electron is most likely to be found?"
  type: multiple-choice
  options:
    - "The electron is most likely found at r=0, inside the nucleus itself"
    - "The electron follows a circular orbit closest to the nucleus, as Bohr predicted"
    - "The most probable radius to find the electron is the Bohr radius a₀, because the radial probability distribution 4πr²|ψ|² peaks there despite |ψ|² being highest at r=0"
    - "The electron is uniformly distributed throughout a sphere of radius a₀"
  answer: 2
  explanation: "This question targets the distinction between probability density |ψ(r)|² and the radial probability distribution P(r) = 4πr²|ψ|². The probability density |ψ|² is indeed highest at r=0 for the 1s orbital. But the probability of finding the electron in a thin shell at radius r involves both |ψ|² and the volume of that shell (4πr²dr). Near r=0, the shell volume goes to zero, so even though |ψ|² is large there, the electron is rarely found at the nucleus. The radial probability distribution P(r) = 4πr²|ψ|² peaks at exactly r = a₀, the Bohr radius — which is why Bohr got the right scale but for the wrong reason (he had definite orbits; QM has probability distributions)."

- question: "According to quantum mechanics, the electron in a hydrogen atom follows a definite circular orbit at a distance determined by the quantum number n, just as Bohr described."
  type: true-false
  answer: false
  explanation: "This is the central conceptual error the topic addresses. Quantum mechanics replaces Bohr's definite orbits with probability densities: |ψ(r)|² gives the probability per unit volume of finding the electron near position r. There is no trajectory; between measurements the electron doesn't 'travel' anywhere in a classically meaningful sense. The Bohr model predicts correct energy levels by lucky cancellation of errors, but its physical picture — electrons in circular orbits at fixed radii — is wrong. Nodes in the wavefunction, where |ψ|² = 0, have no classical analogue (an orbiting particle can't simply skip a region), and confirm that the orbital picture is fundamentally different from Bohr's."

- question: "In a hydrogen atom, the 2s and 2p orbitals have the same energy because the energy formula E_n = −13.6 eV/n² depends only on the principal quantum number n."
  type: true-false
  answer: true
  explanation: "This is correct for hydrogen specifically. Both 2s (n=2, l=0) and 2p (n=2, l=1) have E₂ = −13.6/4 = −3.4 eV. This degeneracy is a special feature of the Coulomb potential — it breaks down in multi-electron atoms where electron repulsion makes energy depend on both n and l. For hydrogen, the three quantum numbers (n, l, m_l) describe the shape and orientation of the orbital but only n determines the energy."

- question: "What is the fundamental conceptual difference between a Bohr orbit and a quantum mechanical orbital, and why does this difference matter physically?"
  type: short-answer
  answer: "A Bohr orbit is a definite circular path: the electron travels around the nucleus at a fixed radius with a specific speed, like a planet orbiting a star. A quantum mechanical orbital is a probability density distribution |ψ(r)|² — it describes the probability per unit volume of finding the electron near each point in space if you make a measurement, not a trajectory the electron follows. Physically this matters because orbitals can have nodes (surfaces where |ψ|² = 0) that a trajectory could never pass through, because orbitals have complex spatial shapes (p, d, f) with lobes and angular nodes that have no classical counterpart, and because the electron's position is genuinely indeterminate between measurements — not merely unknown but undefined."
  explanation: "The key phrase is 'probability density, not path.' The Bohr model is conceptually wrong even when numerically correct: the electron doesn't 'travel' in a circle, its position has no determinate value between observations, and the orbital shapes (including nodes) are intrinsically quantum phenomena with no classical analogue. Understanding this shift is essential for everything from chemical bonding to spectroscopy to quantum computing."
```

## Explainer

Solving the Schrödinger equation for hydrogen is the quantum mechanical analogue of solving Newton's equations for a planet orbiting the sun — both are two-body inverse-square-law problems. From your prerequisite on the hydrogen atom and Schrödinger equation, you know that the wavefunction ψ(r, θ, φ) must satisfy −(ℏ²/2m)∇²ψ + V(r)ψ = Eψ with V(r) = −e²/(4πε₀r). Separation of variables in spherical coordinates breaks this into a radial equation and an angular equation. The angular equation produces **spherical harmonics** Y_l^m(θ, φ), which your spherical harmonics prerequisite introduced. The radial equation produces quantized energy eigenvalues and associated Laguerre polynomials for the radial part.

The energy eigenvalues E_n = −13.6 eV/n² depend only on the **principal quantum number** n = 1, 2, 3, .... The negative sign reflects that the electron is bound (lower energy than a free electron at infinity). The spacing between levels decreases rapidly: the n=1 to n=2 gap is 10.2 eV, while n=10 to n=11 is only about 0.03 eV. This is why the Lyman series (transitions to n=1) produces ultraviolet photons while the Balmer series (transitions to n=2) produces visible light — those famous red, blue-green, and violet lines in hydrogen's spectrum. Each spectral line corresponds to a photon with energy exactly equal to the difference between two energy levels, E_photon = E_n2 − E_n1 = 13.6 eV × (1/n₁² − 1/n₂²).

The full description of each quantum state requires three quantum numbers. The **principal quantum number** n sets the energy and the overall scale of the orbital. The **angular momentum quantum number** l (ranging from 0 to n−1) sets the total orbital angular momentum: L = √(l(l+1))ℏ. States with l=0 are called s orbitals, l=1 are p, l=2 are d. The **magnetic quantum number** m_l (ranging from −l to +l) sets the z-component of angular momentum. Each (n, l, m_l) triple specifies a distinct orbital with a distinct probability density shape. The 1s orbital (n=1, l=0) is spherically symmetric with maximum electron density at the nucleus. The 2p orbitals (n=2, l=1) have dumbbell shapes with a nodal plane through the nucleus.

The critical conceptual shift from Bohr to quantum mechanics is replacing definite orbits with **probability densities**. There is no trajectory for the electron — only |ψ(r)|² giving the probability per unit volume of finding the electron near point r. The average radius ⟨r⟩ for the 1s orbital is 1.5 times the Bohr radius a₀, and the most probable radius is exactly a₀ ≈ 0.053 nm — so Bohr's model gets the right scale but for the wrong reason. Nodes in the wavefunction (surfaces where |ψ|² = 0) have no classical analogue. The number of radial nodes is n − l − 1 and the number of angular nodes is l, giving a total of n−1 nodes — which is why higher-n states have more oscillatory wavefunctions and more complex spatial structure.
