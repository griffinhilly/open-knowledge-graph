---
id: molecular-spectroscopy-selection-rules
title: Selection Rules in Molecular Spectroscopy
domain: chemistry
course: physical-chemistry
prerequisites:
- id: electronic-spectroscopy-theory
  type: hard
- id: group-theory-molecular-symmetry
  type: hard
- id: selection-rules-spectroscopy
  type: soft
- id: selection-rules-electronic-spectroscopy
  type: soft
builds-toward:
- electronic-transitions-excited-states
- nmr-spectroscopy-spin-coupling
tags:
- spectroscopy
- selection-rules
- transitions
- symmetry
stage: advanced
status: validated
---
# Selection Rules in Molecular Spectroscopy

## Core Idea
Selection rules determine which transitions between energy levels are allowed by quantum mechanics, predicting whether spectral lines will appear or be absent. Spin, orbital angular momentum, and molecular symmetry all impose selection rules. Violating selection rules results in forbidden transitions with very low intensity or complete absence from the spectrum. Selection rules allow spectroscopists to assign observed spectra to specific molecular transitions.

## How It's Best Learned
Combine symmetry arguments with explicit transition dipole moment calculations. Use character tables from group theory to predict allowed transitions. Compare predictions with experimental spectra from databases.

## Common Misconceptions
- Forbidden transitions never occur (they do, but with much lower intensity from higher-order effects).
- Selection rules are the same in all types of spectroscopy (they vary significantly between UV-Vis, IR, Raman, etc.).

## Questions

```yaml
- question: "In a centrosymmetric molecule, a vibrational mode that does not change the molecular dipole moment shows a strong band in the Raman spectrum but no absorption in the IR spectrum. This is best explained by:"
  type: multiple-choice
  options:
    - "A measurement error — if a vibration is IR-forbidden it must also be Raman-forbidden"
    - "The rule of mutual exclusion: for centrosymmetric molecules, no vibrational mode can be simultaneously IR-active and Raman-active"
    - "The Laporte rule: transitions between states of the same parity are forbidden in UV-Vis but not in vibrational spectra"
    - "The Raman selection rule requires a change in dipole moment, so only IR-inactive modes can appear in Raman"
  answer: 1
  explanation: "The rule of mutual exclusion applies to centrosymmetric molecules: IR-active vibrations (those that change the dipole moment) are Raman-inactive, and vice versa. Symmetric stretches do not change the dipole (IR-inactive) but do change the polarizability (Raman-active). This complementarity is a direct consequence of inversion symmetry and is a powerful structural diagnostic — if a molecule shows mutual exclusion, it must have a center of inversion."

- question: "Group theory predicts that a particular electronic transition is symmetry-forbidden. A spectroscopist observes a weak absorption band at exactly that wavelength. What is the most likely explanation?"
  type: multiple-choice
  options:
    - "The group theory analysis must contain an error — truly forbidden transitions never appear in any spectrum"
    - "The band is from a contaminating molecule in the sample"
    - "Vibronic coupling or spin-orbit coupling is relaxing the symmetry selection rule, allowing the forbidden transition with very low intensity"
    - "The transition is allowed; the selection rule must be evaluated using the excited-state symmetry, not the ground state"
  answer: 2
  explanation: "'Forbidden' means zero intensity to first order — not impossible. Vibronic coupling (molecular vibrations temporarily distort the symmetry, mixing states of different parity) and spin-orbit coupling (heavy atoms mix singlet and triplet states, weakening the ΔS = 0 rule) both relax symmetry-based selection rules. Forbidden bands appear with intensities 10² to 10⁶ times weaker than fully allowed transitions — unmistakably real, and diagnostically important."

- question: "A transition between two energy levels is allowed if and only if the direct product of the symmetry representations of the initial state, the dipole operator, and the final state contains the totally symmetric irreducible representation of the molecule's point group."
  type: true-false
  answer: true
  explanation: "This is the group-theoretical selection rule criterion. The transition dipole integral ⟨ψ_f|μ̂|ψ_i⟩ vanishes by symmetry whenever the integrand's overall symmetry does not contain the totally symmetric representation (A₁ or equivalent), because such integrals over all space equal zero. This allows spectroscopists to predict allowed transitions from character tables alone, without evaluating any integrals."

- question: "Selection rules in infrared and Raman spectroscopy are identical because both techniques involve a photon interacting with the molecule."
  type: true-false
  answer: false
  explanation: "IR and Raman spectroscopy have fundamentally different selection rules because they couple to different molecular properties. IR absorption requires a change in the molecular dipole moment; Raman scattering requires a change in molecular polarizability. These are complementary — for centrosymmetric molecules, the rule of mutual exclusion means IR-active modes are Raman-inactive and vice versa. The physical mechanism of the photon interaction determines the selection rule, not merely the fact that a photon is involved."

- question: "Why do 'forbidden' transitions sometimes appear in experimental spectra, and what physical mechanisms allow them to occur?"
  type: short-answer
  answer: "Selection rules are derived under idealized conditions — rigid geometry, pure spin states, and exact molecular symmetry. Real molecules deviate from these idealizations. Vibronic coupling mixes electronic and vibrational states: molecular vibrations temporarily distort the geometry, breaking the symmetry that forbids the transition and giving it a small but nonzero transition dipole. Spin-orbit coupling mixes singlet and triplet spin states in molecules containing heavy atoms, relaxing the ΔS = 0 spin selection rule. Both mechanisms produce weak but real absorption bands at 'forbidden' energies."
  explanation: "Recognizing forbidden bands and understanding why they appear is essential for correct spectral assignment. A band at an unexpected position with anomalously low intensity (compared to allowed transitions in the same spectrum) is often a signature of a symmetry-forbidden transition made weakly allowed by vibronic or spin-orbit coupling. The intensity contrast itself — weak vs. strong — is a diagnostic fingerprint of the selection rule status."
```

## Explainer

From electronic spectroscopy and group theory, you know that molecules absorb light to transition between energy levels and that molecular symmetry governs many physical properties. **Selection rules** connect these ideas by answering a precise question: for a given pair of energy levels, will the molecule actually absorb (or emit) a photon to make the transition? The answer comes from evaluating the **transition dipole moment integral** ⟨ψ_final|μ̂|ψ_initial⟩, where μ̂ is the dipole moment operator. If this integral is zero by symmetry, the transition is "forbidden" and will not appear in the spectrum (or will appear only very weakly). If it is nonzero, the transition is "allowed."

This is where group theory earns its keep. Rather than computing the integral explicitly, you can determine whether it is zero by inspecting **symmetry representations**. The rule is: the direct product of the representations of ψ_initial, the dipole operator μ̂, and ψ_final must contain the totally symmetric representation of the molecule's point group. If it does not, the integral vanishes by symmetry and the transition is forbidden. In practice, you look up the irreducible representations in the character table, take their direct product, and check whether A₁ (or whatever the totally symmetric species is called in that point group) appears. This symmetry-based approach lets you predict the entire absorption spectrum's structure without solving any integrals.

Different types of spectroscopy interact with molecules through different mechanisms, producing different selection rules. In **infrared (IR) spectroscopy**, the photon couples to changes in dipole moment, so a vibration is IR-active only if it changes the molecular dipole moment — symmetric stretches of homonuclear diatomics (like N₂ or O₂) are IR-inactive. In **Raman spectroscopy**, the photon couples to changes in polarizability, so the complementary rule applies: symmetric stretches that do not change the dipole are often Raman-active. For centrosymmetric molecules, the **rule of mutual exclusion** states that no vibration can be both IR- and Raman-active. In **electronic (UV-Vis) spectroscopy**, the key selection rules involve spin (ΔS = 0, transitions must conserve spin multiplicity) and orbital symmetry (Laporte rule: in centrosymmetric molecules, transitions between states of the same parity, g→g or u→u, are forbidden).

A crucial nuance is that "forbidden" does not mean "impossible." Forbidden transitions still occur, just with much lower intensity — sometimes 100 to 1,000,000 times weaker than allowed transitions. Mechanisms that relax selection rules include **vibronic coupling** (molecular vibrations temporarily break the symmetry that makes a transition forbidden), **spin-orbit coupling** (heavy atoms mix spin states, weakening the ΔS = 0 rule), and **magnetic dipole or electric quadrupole transitions** (higher-order interaction mechanisms with weaker but nonzero transition moments). Recognizing these weak, "forbidden" bands in experimental spectra — and understanding why they appear at all — is essential for correctly assigning molecular electronic structure.
