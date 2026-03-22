---
id: fine-structure-hydrogen
title: Fine Structure and Relativistic Corrections
domain: physics
course: quantum-mechanics
prerequisites:
- id: hydrogen-atom-solution
  type: hard
- id: spin-angular-momentum
  type: hard
tags:
- fine-structure
- relativistic
stage: advanced
status: draft
---

# Fine Structure and Relativistic Corrections

## Core Idea
Fine structure arises from relativistic corrections and spin-orbit coupling. Total J⃗ = L⃗ + S⃗ becomes the good quantum number, splitting levels with same n, l but different j.

## Questions

```yaml
- question: "Which two physical effects contribute comparably to the fine structure of hydrogen, lifting the degeneracy between states with the same n but different l?"
  type: multiple-choice
  options:
    - "Zeeman effect and Lamb shift"
    - "Relativistic kinetic energy correction and spin-orbit coupling"
    - "Nuclear spin coupling and vacuum polarization"
    - "Diamagnetic correction and hyperfine interaction"
  answer: 1
  explanation: "Fine structure has two comparably-sized contributions. First, the relativistic kinetic energy correction: expanding the full relativistic kinetic energy to order (v/c)² yields a p⁴ term that depends on both n and l, breaking l-degeneracy. Second, spin-orbit coupling: the electron's magnetic moment interacts with the magnetic field it 'sees' as the proton orbits it in the electron's rest frame; this adds an L⃗·S⃗ term that also depends on l. The Zeeman effect requires an external field; the Lamb shift is a QED correction beyond fine structure; hyperfine structure comes from nuclear spin and is ~1000× smaller still."

- question: "A student says the fine structure states of hydrogen are labeled by quantum numbers n, l, m_l, and m_s. What is wrong with this description?"
  type: multiple-choice
  options:
    - "Nothing — those are exactly the right quantum numbers for fine structure states"
    - "Fine structure only requires n and l; spin plays no role"
    - "The correct quantum numbers are n, l, j, and m_j — because spin-orbit coupling makes m_l and m_s individually non-conserved"
    - "The correct quantum numbers are n and j only; l is no longer defined once spin-orbit coupling is included"
  answer: 2
  explanation: "Once spin-orbit coupling (L⃗·S⃗) is added to the Hamiltonian, L⃗ and S⃗ precess around their sum J⃗ = L⃗ + S⃗. The operators L_z and S_z no longer commute with the full Hamiltonian, so m_l and m_s are not individually conserved. The good quantum numbers become n (principal), l (orbital magnitude, still conserved), j = l ± ½ (total angular momentum magnitude), and m_j (total z-projection). Spectroscopic notation reflects this: the 2p levels become 2P₃/₂ and 2P₁/₂, labeled by j not by m_l and m_s."

- question: "Fine structure alone predicts that the 2S₁/₂ and 2P₁/₂ states of hydrogen are degenerate — they have the same energy within the fine structure approximation."
  type: true-false
  answer: true
  explanation: "Fine structure energy corrections depend on n and j (total angular momentum). Both 2S₁/₂ (n=2, l=0, j=½) and 2P₁/₂ (n=2, l=1, j=½) have the same n=2 and j=½, so within Dirac theory (which accounts for relativistic corrections and spin-orbit coupling), they are degenerate. Their actual separation — the Lamb shift of ~1058 MHz — is a quantum electrodynamic effect from vacuum fluctuations and electron self-energy, which lies beyond fine structure. The Lamb shift was a key experimental triumph for QED."

- question: "Fine structure energy corrections are comparable in magnitude to the gross structure (Bohr) energy level spacings, which is why they are visible in ordinary spectroscopy."
  type: true-false
  answer: false
  explanation: "Fine structure corrections scale as α² × Eₙ, where α ≈ 1/137 is the fine structure constant. Since α² ≈ 5×10⁻⁵, fine structure corrections (~10⁻³ eV) are roughly 10,000 times smaller than the gross structure spacings (~1–10 eV). This is why fine structure is 'fine' — it requires high-resolution spectroscopy to resolve. The sodium D-line doublet, one of the most famous examples, consists of two lines only 0.6 nm apart (589.0 and 589.6 nm); at low resolution they appear as a single yellow line."

- question: "Why do m_l and m_s cease to be good quantum numbers when spin-orbit coupling is added to the hydrogen Hamiltonian, and what replaces them?"
  type: short-answer
  answer: "Spin-orbit coupling adds a term proportional to L⃗·S⃗ to the Hamiltonian. This operator does not commute with L_z or S_z individually, so those quantities are no longer conserved. Instead, L⃗ and S⃗ precess around the total J⃗ = L⃗ + S⃗, and the conserved quantities become the magnitudes of L⃗, S⃗, and J⃗ (quantum numbers l, s, j) and the z-projection of the total angular momentum m_j."
  explanation: "A quantum number is 'good' — a constant of the motion — if and only if its operator commutes with the Hamiltonian. Writing L⃗·S⃗ = ½(J² − L² − S²) shows it commutes with J², L², and S² but not with L_z or S_z. So after including spin-orbit coupling, the set of commuting observables that diagonalizes the Hamiltonian is {H, L², S², J², J_z}, corresponding to quantum numbers {n, l, s=½, j, m_j}. The individual z-projections m_l and m_s fluctuate because L⃗ and S⃗ are coupled and precess."
```

## Explainer

From your solution of the hydrogen atom, you know that energy levels depend only on the principal quantum number n: Eₙ = −13.6 eV / n². States with the same n but different orbital quantum number l are degenerate — they sit at exactly the same energy. This degeneracy is an artifact of the ideal Bohr model. Fine structure is what happens when you treat the electron more carefully, including corrections that the basic Schrödinger equation ignores.

Two physical effects contribute comparably to **fine structure**. First, the relativistic kinetic energy correction: the electron is moving fast enough (especially in inner orbits) that the classical p²/2m underestimates its kinetic energy. Using the full relativistic expression K = (γ − 1)mc² and expanding to order (v/c)², you get a correction term proportional to p⁴. This lowers the energy and depends on both n and l. Second, **spin-orbit coupling**: in the electron's rest frame, the proton appears to orbit it, creating a magnetic field. The electron's magnetic moment (arising from its spin s = ½) interacts with this field. The coupling energy is proportional to L⃗ · S⃗, and its size depends on n, l, and the relative orientation of L⃗ and S⃗.

Because the Hamiltonian now contains L⃗ · S⃗, the individual L_z and S_z quantum numbers m_l and m_s are no longer conserved — L⃗ and S⃗ precess around the total **J⃗ = L⃗ + S⃗**. The good quantum numbers become n, l, j, and m_j, where j = l ± ½ for an electron (since s = ½). For example, the 2p level (n = 2, l = 1) splits into two sublevels: j = 3/2 (four states) and j = 1/2 (two states). In spectroscopic notation these are written 2P₃/₂ and 2P₁/₂. The 2S₁/₂ level (l = 0, j = ½) remains close to 2P₁/₂ but is separated by the Lamb shift (a quantum electrodynamics correction, not fine structure).

The magnitude of fine structure is set by the **fine structure constant** α ≈ 1/137. The fine structure energy corrections are of order α² × 13.6 eV ≈ 10⁻³ eV — about 10,000 times smaller than the gross structure spacing. This is why spectral lines that appear single at low resolution reveal doublets and multiplets at higher resolution. The famous sodium D-line doublet (the two yellow lines at 589.0 and 589.6 nm) is a direct experimental signature of the 3P₃/₂ − 3P₁/₂ fine structure splitting.
