---
id: time-dependent-dft-excited-states
title: Time-Dependent DFT for Excited States
domain: chemistry
course: physical-chemistry
prerequisites:
- id: density-functional-theory-intro
  type: hard
- id: electronic-spectroscopy-theory
  type: soft
builds-toward:
- selection-rules-electronic-spectroscopy
tags:
- spectroscopy
- excited-states
- dft
- computational
stage: advanced
status: draft
---

# Time-Dependent DFT for Excited States

## Core Idea
Time-Dependent DFT (TDDFT) extends density functional theory to time-dependent perturbations and excited states by introducing the time-dependent density and linear response theory. TDDFT efficiently predicts excitation energies and oscillator strengths for electronic transitions without explicitly constructing excited-state wavefunctions. It balances computational cost and accuracy, making it practical for large molecules.

## How It's Best Learned
Calculate UV-Vis absorption spectra using TDDFT for organic dyes and proteins; compare results to experimental λmax and intensity; test different functionals (PBE, CAM-B3LYP, ωB97X) to understand how exchange admixture affects charge-transfer states.

## Common Misconceptions
- Assuming TDDFT is as reliable for charge-transfer states as for local excitations; standard functionals underestimate CT excitation energies due to insufficient long-range exchange. - Treating the TDDFT excitation energy as a true excited-state energy; it is an excitation energy from the ground state, not an absolute energy.

## Questions

```yaml
- question: "You run a TDDFT calculation on a donor-acceptor dye molecule using a GGA functional and find the predicted lowest excitation energy is 1.2 eV below the experimental absorption peak. Which explanation is most likely correct?"
  type: multiple-choice
  options:
    - "The GGA functional overestimates the exchange-correlation energy, artificially stabilizing the excited state"
    - "The calculation is using the wrong basis set, and a larger basis set would correct the error"
    - "The transition is a charge-transfer excitation, and GGA functionals severely underestimate CT excitation energies due to insufficient long-range exchange"
    - "TDDFT is not applicable to dye molecules because they absorb only in the visible range"
  answer: 2
  explanation: "GGA and other semilocal functionals contain a self-interaction error that fails to properly penalize long-range separation of electron density. For charge-transfer excitations — where an electron moves from a donor fragment to an acceptor fragment far away — this error causes dramatic underestimation of excitation energies, often by 1–2 eV. Range-separated hybrid functionals (CAM-B3LYP, ωB97X) correct this by incorporating increasing Hartree-Fock exchange at long range. Basis set size (option B) is a second-order concern compared to functional choice for this class of excitation."

- question: "What does a TDDFT linear response calculation directly compute, and what does it NOT compute?"
  type: multiple-choice
  options:
    - "It computes the absolute total energy of excited states; it does not compute oscillator strengths"
    - "It computes excitation energies (energy differences from the ground state) and oscillator strengths; it does not compute the absolute energy of excited states"
    - "It computes excited-state wavefunctions explicitly; it does not use the ground-state density"
    - "It computes excited-state geometries; it does not predict absorption wavelengths directly"
  answer: 1
  explanation: "TDDFT linear response calculates excitation energies — the energy required to promote the system from the ground state to each excited state — along with oscillator strengths that predict the intensity of each transition. These are the eigenvalues and related quantities from the Casida equations. TDDFT does NOT compute absolute excited-state energies (which would require placing the total energy on an absolute scale). A common misconception is treating the excitation energy as equivalent to an excited-state wavefunction or total energy; it is simply the gap between ground and excited state energetics."

- question: "Standard GGA TDDFT functionals are equally reliable for valence excitations (local transitions) and charge-transfer excitations in large molecules."
  type: true-false
  answer: false
  explanation: "This is the central practical limitation of TDDFT. For valence excitations — where the excited electron stays near its origin — GGA functionals perform reasonably well because the electron density doesn't move far. For charge-transfer excitations — where density shifts across the molecule — GGA functionals dramatically underestimate excitation energies because they lack the long-range exchange needed to correctly penalize charge separation. Range-separated hybrids (CAM-B3LYP, ωB97X) address this by blending in Hartree-Fock exchange at long range, but local functionals cannot be used reliably for CT states."

- question: "TDDFT requires only a completed ground-state Kohn-Sham DFT calculation as input, making it far less computationally expensive than wavefunction-based excited-state methods."
  type: true-false
  answer: true
  explanation: "This is the core practical appeal of TDDFT. The Casida equations — the eigenvalue problem that yields excitation energies — are constructed entirely from ground-state Kohn-Sham orbitals and orbital energies, plus the exchange-correlation kernel. No explicit excited-state wavefunctions are constructed. The main additional cost is one matrix diagonalization. By contrast, methods like EOM-CCSD or CASSCF/CASPT2 require substantially more computation because they explicitly construct multi-electron excited-state representations."

- question: "Why do range-separated hybrid functionals perform significantly better than GGA functionals for charge-transfer excitations in TDDFT, and what physical feature of GGA functionals causes the failure?"
  type: short-answer
  answer: "GGA functionals have a self-interaction error: an electron's Coulomb repulsion is not fully cancelled by the exchange-correlation term for long-range separations, making it artificially cheap to move electron density far across a molecule. For charge-transfer excitations, where an electron moves from donor to acceptor groups separated by distance, this error causes the excitation energy to be dramatically underestimated. Range-separated hybrid functionals correct this by including 100% Hartree-Fock exchange (which is self-interaction-free) at long interelectronic distances while retaining DFT exchange at short range. This asymptotic correction restores the correct long-range behavior of the exchange potential and gives accurate CT excitation energies."
  explanation: "The failure of GGA for CT states is not just numerical imprecision — it reflects a fundamental theoretical deficiency. The exact exchange-correlation potential must decay as -1/r at large distances (the image charge theorem), but approximate functionals violate this. Hartree-Fock exchange has the correct -1/r asymptotics, which is why range-separated hybrids that switch to 100% HF exchange at long range fix the problem."
```

## Explainer

Standard density functional theory, which you already know, is fundamentally a ground-state theory — the Hohenberg-Kohn theorems guarantee that the ground-state electron density determines all ground-state properties. But chemistry and spectroscopy constantly demand information about excited states: What wavelength of light does a molecule absorb? What color does a dye appear? How does a photoreceptor protein respond to light? **Time-Dependent DFT (TDDFT)** extends the DFT framework to answer these questions without abandoning the computational efficiency that makes DFT practical for large molecules.

The theoretical foundation is the **Runge-Gross theorem**, the time-dependent analog of the Hohenberg-Kohn theorem. It establishes that the time-dependent external potential is uniquely determined by the time-dependent electron density (up to a trivial additive function of time). This means we can, in principle, track how the electron density evolves under a perturbation — like an oscillating electric field from a light wave — using time-dependent Kohn-Sham equations. In practice, we rarely solve the full time-dependent equations. Instead, **linear response TDDFT** asks a simpler question: if we apply an infinitesimally small perturbation to the ground state, at what frequencies does the density oscillate in response? These resonant frequencies correspond to electronic excitation energies, and their intensities give **oscillator strengths** that predict absorption spectra.

The linear response calculation reduces to solving the **Casida equations**, an eigenvalue problem built from the ground-state Kohn-Sham orbitals and a coupling matrix that depends on the exchange-correlation functional. Each eigenvalue gives an excitation energy, and the eigenvectors describe which orbital transitions contribute to each excited state. The beauty of this approach is that it requires only the ground-state Kohn-Sham calculation as input, plus one matrix diagonalization — far cheaper than wavefunction-based excited-state methods like equation-of-motion coupled cluster or multireference configuration interaction.

The choice of exchange-correlation functional matters more for TDDFT than for ground-state DFT. Local and semilocal functionals (LDA, GGA) work reasonably well for **valence excitations** — transitions where the excited electron stays near its original location. But for **charge-transfer excitations**, where electron density moves a significant distance across the molecule, these functionals dramatically underestimate excitation energies. The problem traces to the self-interaction error in approximate functionals, which fails to penalize long-range charge separation correctly. **Range-separated hybrid functionals** like CAM-B3LYP and ωB97X fix this by including increasing amounts of exact Hartree-Fock exchange at long range. Choosing the right functional for your system is arguably the most important practical decision in TDDFT calculations, and validating against experimental spectra or higher-level theory should always be part of the workflow.
