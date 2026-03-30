---
id: antiferromagnetism-spin-waves
title: Antiferromagnetism and Spin Waves (Magnons)
domain: physics
course: condensed-matter-physics
prerequisites:
- id: ferromagnetism-heisenberg-model
  type: hard
- id: creation-annihilation-operators
  type: soft
tags:
- antiferromagnetism
- magnon
- spin-wave
- neel-temperature
stage: expert
status: validated
---

# Antiferromagnetism and Spin Waves (Magnons)

## Core Idea
In antiferromagnets, the exchange coupling J < 0 favors antiparallel alignment of neighboring spins, producing a state with zero net magnetization but long-range alternating order below the Neel temperature T_N. The order parameter is the staggered magnetization (sublattice difference). Spin waves in both ferromagnets and antiferromagnets are quantized collective excitations called magnons. Ferromagnetic magnons have a quadratic dispersion omega proportional to k^2, while antiferromagnetic magnons have a linear dispersion omega proportional to k (like phonons). Magnons are bosons and their thermal population determines the temperature dependence of the magnetization.

## Questions

```yaml
- question: "Ferromagnetic magnons have dispersion ω ∝ k² while antiferromagnetic magnons have ω ∝ |k|. What determines this fundamental difference?"
  type: multiple-choice
  options:
    - "Antiferromagnets have stronger exchange coupling"
    - "In a ferromagnet, the ground state has all spins aligned and a single magnon is a long-wavelength precession — the restoring force comes from the exchange stiffness and is proportional to k². In an antiferromagnet, the two sublattices precess against each other and the dynamics resemble two coupled oscillators, producing a linear (acoustic-like) dispersion that reflects the staggered nature of the order"
    - "The crystal structure determines the dispersion shape"
    - "Antiferromagnetic magnons are fermions, not bosons"
  answer: 1
  explanation: "The magnon dispersion reflects the symmetry of the ordered state. In a ferromagnet, the uniform state is the ground state and small deviations cost exchange energy proportional to (∇M)² ~ k², giving ω ~ k². In an antiferromagnet, the order parameter (staggered magnetization) breaks a continuous symmetry, and the Goldstone theorem guarantees gapless excitations with linear dispersion — analogous to acoustic phonons from broken translational symmetry. The linear dispersion is a direct consequence of the antiferromagnetic order being a broken-symmetry state with a 'stiffness' for long-wavelength distortions."

- question: "Neutron scattering is the primary experimental probe of magnon dispersions. Why are neutrons uniquely suited for this measurement?"
  type: multiple-choice
  options:
    - "Neutrons are the only particles that can penetrate solids"
    - "Neutrons carry a magnetic moment (spin-1/2) that interacts with the local magnetic field of ordered spins, allowing them to create or annihilate magnons; additionally, thermal neutrons have wavelengths ~Å and energies ~meV, matching the length and energy scales of magnon dispersions in solids"
    - "X-rays are absorbed too strongly by magnetic materials"
    - "Neutrons are lighter than electrons and scatter less"
  answer: 1
  explanation: "Neutrons interact with atomic magnetic moments through their own magnetic dipole moment, giving them direct sensitivity to spin ordering and spin excitations. Thermal neutrons (from reactor sources) have de Broglie wavelengths of ~1-2 Å and energies of ~10-100 meV, perfectly matched to interatomic spacings and typical magnon energies. By measuring the energy and momentum transferred to the neutron (inelastic neutron scattering), one maps out the magnon dispersion ω(q) directly. X-rays can now probe magnons via resonant techniques, but neutron scattering remains the gold standard."

- question: "Below the Neel temperature, an antiferromagnet has zero net magnetization but can still be detected as magnetically ordered by neutron diffraction. Explain why."
  type: short-answer
  answer: "Neutron diffraction detects magnetic order through the coherent scattering of neutron magnetic moments from the ordered spin arrangement. In an antiferromagnet, the magnetic unit cell is larger than the chemical unit cell (it includes both sublattices), so magnetic Bragg peaks appear at reciprocal lattice vectors of the magnetic superlattice — these are at positions between the chemical Bragg peaks. These extra diffraction peaks are the unambiguous signature of antiferromagnetic order. They vanish above T_N. X-ray diffraction misses these peaks because X-rays scatter from electron density, not magnetic moments, and the chemical unit cell shows no evidence of the spin order."
  explanation: "The classic experiment is on MnO: neutron diffraction below T_N = 118 K shows extra peaks at half-integer positions corresponding to the doubled magnetic unit cell. Above T_N, these peaks disappear. This was the definitive proof of antiferromagnetic order."

- question: "In the Heisenberg antiferromagnet, the classical Neel state (perfectly alternating up-down spins) is NOT the exact quantum ground state. Why not?"
  type: short-answer
  answer: "The Neel state has each spin pointing exactly up or down along a chosen axis. But the Heisenberg Hamiltonian H = -J Σ S_i · S_j contains transverse terms (S_i^x S_j^x + S_i^y S_j^y) that flip pairs of neighboring spins. The Neel state is not an eigenstate of these operators — applying them generates configurations with spin deviations. The true quantum ground state includes quantum fluctuations (virtual magnon pairs) that reduce the sublattice magnetization below its classical value. For S = 1/2 on a square lattice, quantum fluctuations reduce the ordered moment by about 40% from its classical value. In one dimension, fluctuations are so strong that the S = 1/2 Heisenberg antiferromagnet has no long-range order at any temperature."
  explanation: "This 'quantum reduction' of the order parameter is a hallmark of quantum antiferromagnets. It is largest for small S and low dimension, and is responsible for the rich physics of quantum spin liquids in frustrated magnets."
```

## Explainer

While ferromagnetism produces dramatic macroscopic effects (permanent magnets, compass needles), **antiferromagnetism** is far more common but invisible to simple measurements because the net magnetization is zero. In an antiferromagnet with exchange coupling J < 0, neighboring spins prefer to be antiparallel. Below the **Neel temperature** T_N, the spins order into two interpenetrating sublattices with opposite magnetization, producing a staggered pattern. The order parameter is the **staggered magnetization** L = M_A - M_B, where A and B are the two sublattices. Above T_N, the susceptibility follows a modified Curie-Weiss law chi = C/(T + Theta), where the positive Weiss constant Theta reflects the antiferromagnetic coupling.

The elementary excitations of magnetically ordered states are **spin waves** — collective, wave-like disturbances in which the spin direction varies smoothly across the lattice. Quantizing spin waves gives **magnons**, which are bosons (the spin change per magnon is Delta S_z = 1). In a ferromagnet, the long-wavelength dispersion is omega = Dk^2, where D is the spin-wave stiffness — a quadratic dispersion resembling that of a free particle. This arises because the ferromagnetic ground state is an eigenstate of S_total, and single-magnon states involve a gentle precession that costs exchange energy proportional to k^2.

In an antiferromagnet, the magnon dispersion is qualitatively different: omega = c|k| (linear), resembling an acoustic phonon. This linear dispersion is guaranteed by the **Goldstone theorem**: the antiferromagnetic ground state spontaneously breaks the continuous spin-rotation symmetry, and the magnon is the corresponding massless Goldstone boson. There are actually two magnon branches (one per sublattice), both with linear dispersion at long wavelengths. The magnon velocity c plays the same role as the speed of sound for phonons.

Magnon populations govern the temperature dependence of the magnetization. In ferromagnets, the Bloch T^{3/2} law — M(T) = M(0)[1 - (T/T_C)^{3/2}] — follows from the k^2 dispersion and 3D Bose statistics. In antiferromagnets, the linear dispersion changes the magnon density of states and the thermal reduction of the sublattice magnetization goes as T^2 in 3D. Beyond the ordered phases, spin waves and their interactions contain rich physics: magnon-magnon scattering, magnon-phonon coupling, and the breakdown of spin-wave theory near quantum critical points. In frustrated magnets (where geometry prevents all interactions from being satisfied simultaneously), quantum fluctuations can be so strong that long-range order is destroyed entirely, producing exotic **quantum spin liquid** states with no classical analog.
