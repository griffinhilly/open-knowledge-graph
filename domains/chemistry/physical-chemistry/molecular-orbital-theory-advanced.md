---
id: molecular-orbital-theory-advanced
title: 'Molecular Orbital Theory: LCAO-MO'
domain: chemistry
course: physical-chemistry
prerequisites:
- id: born-oppenheimer-approximation
  type: hard
- id: hydrogen-atom-wavefunctions
  type: hard
- id: variational-principle-chemistry
  type: hard
- id: quantum-mechanics-postulates-core
  type: hard
- id: eigenvalues-and-eigenvectors
  type: soft
- id: schrodinger-equation-molecular-systems
  type: soft
builds-toward:
- huckel-molecular-orbital-theory
- electronic-spectroscopy-theory
tags:
- LCAO
- bonding-antibonding
- MO-theory
- sigma
- pi-orbitals
- overlap-integral
stage: advanced
status: validated
---

# Molecular Orbital Theory: LCAO-MO

## Core Idea
Molecular orbital theory constructs MOs as linear combinations of atomic orbitals (LCAO): φ = c_A χ_A + c_B χ_B. Applying the variational principle leads to the secular determinant, whose solutions give bonding and antibonding orbital energies and coefficients. The key integrals are the overlap integral S, Coulomb integral α, and resonance integral β; their relative magnitudes determine the energy stabilization of bonding MOs and the destabilization of antibonding ones. Bond order is (bonding electrons − antibonding electrons)/2. MO theory correctly predicts O₂ paramagnetism and the non-existence of He₂, where valence bond theory struggles.

## How It's Best Learned
Work through H₂⁺ in detail before tackling H₂ and second-row homonuclear diatomics. Draw the MO energy-level diagrams, fill in electrons using the Aufbau principle, and compute bond orders.

## Common Misconceptions
- Confusing the LCAO coefficients c with probabilities; the coefficients can be negative, while |c|² gives orbital contribution.
- Thinking bonding MOs are always lower in energy than the constituent AOs — they are only if S is positive and β < 0.

## Questions

```yaml
- question: "MO theory correctly predicts that O₂ is paramagnetic, while valence bond theory (Lewis structures) predicts it is diamagnetic. Which feature of the MO energy-level diagram explains paramagnetism?"
  type: multiple-choice
  options:
    - "O₂ has a triple bond, giving it more electrons than expected."
    - "Two electrons occupy degenerate π* antibonding orbitals singly, with parallel spins, following Hund's rule."
    - "The σ bonding MO is completely filled before any electrons enter antibonding orbitals."
    - "The overlap integral S for the 2p orbitals is negative, destabilizing the bonding MO."
  answer: 1
  explanation: "After filling σ and π bonding MOs, O₂ has two electrons remaining to place in two degenerate π* orbitals. By Hund's rule, one electron goes into each π* orbital with parallel spins rather than pairing in one. Parallel (unpaired) electrons create a net magnetic moment, making O₂ paramagnetic. A Lewis structure cannot represent degenerate orbitals or Hund's rule, so it draws a double bond with all electrons paired and incorrectly predicts diamagnetism."

- question: "In LCAO-MO theory, the coefficients c_A and c_B in the expansion φ = c_A χ_A + c_B χ_B represent the probability of finding an electron on atom A or B, respectively."
  type: true-false
  answer: false
  explanation: "The coefficients c_A and c_B are amplitude coefficients, not probabilities, and can be negative (as in antibonding MOs where the combination is φ* = c_A χ_A − c_B χ_B). The probability density contribution of atom A is related to c_A² (and a cross term involving the overlap S), not c_A itself. This distinction matters: a negative coefficient means the wavefunction has a node between the atoms — the defining feature of an antibonding orbital."

- question: "Using MO theory, calculate the bond order of He₂ and state what this predicts about the molecule's stability. Identify which electrons are responsible for this result."
  type: short-answer
  answer: "Bond order = (bonding electrons − antibonding electrons) / 2 = (2 − 2) / 2 = 0. A bond order of zero predicts He₂ does not form a stable bond and should not exist as a molecule. The two electrons in the σ(1s) bonding MO provide stabilization, but this is exactly canceled by the two electrons in the σ*(1s) antibonding MO, which destabilize the molecule by roughly the same amount. He₂ is indeed not observed under normal conditions."
  explanation: "This is one of MO theory's most elegant predictions. Both bonding and antibonding MOs form from the 1s atomic orbitals of the two helium atoms. The bonding energy gained from filling σ is nearly perfectly canceled by the antibonding energy cost of filling σ*. The net stabilization is essentially zero, and the molecule does not form. The analogous argument explains why He₂⁺ (bond order = 1/2) is weakly stable — removing one electron from σ* tips the balance toward bonding."
```

## Explainer

Valence bond theory describes bonding in terms of electron pairs localized between specific atoms — a useful picture, but one that struggles with delocalized electrons, unpredicted magnetic properties, and fractional bond orders. Molecular orbital theory takes a fundamentally different starting point: rather than thinking of electrons as belonging to individual atoms that then share a pair, MO theory asks what orbitals emerge when atoms come together to form a molecule.

The LCAO (linear combination of atomic orbitals) approximation constructs these molecular orbitals by adding and subtracting atomic wavefunctions. For a diatomic A–B, we form φ_bond = c_A χ_A + c_B χ_B and φ_anti = c_A χ_A − c_B χ_B. The bonding combination has constructive interference between the atoms: electron density builds up in the internuclear region, stabilizing both nuclei simultaneously and lowering the energy below the atomic orbitals. The antibonding combination has a nodal plane between the nuclei: destructive interference removes electron density from the internuclear region, raising the energy above the atomic orbitals. This is where the "bonding stabilizes, antibonding destabilizes" rule comes from — it's a direct consequence of constructive versus destructive wavefunction interference.

To find the actual coefficients and energies, you apply the variational principle: the best approximate MOs are those that minimize the energy. This leads to the secular determinant, a 2×2 equation involving three key integrals. The Coulomb integrals α_A and α_B are the energies of electrons in the original atomic orbitals — essentially the ionization energies. The resonance integral β is the key interaction term: it is negative (stabilizing) and its magnitude measures how much the two orbitals overlap and interact. The overlap integral S quantifies the spatial overlap of χ_A and χ_B; for identical atoms S > 0 for orbitals pointing toward each other. Solving the secular determinant gives two eigenvalues (the MO energies) and two sets of coefficients describing how each atom contributes to each MO.

With the MO energy levels in hand, electrons are filled in using the Aufbau principle and Hund's rule, just as for atomic orbitals. Bond order = (bonding electrons − antibonding electrons)/2 gives a quantitative measure of bond strength. For H₂: (2−0)/2 = 1 (single bond). For N₂: (8−2)/2 = 3 (triple bond, consistent with N₂'s extraordinary stability). For O₂: filling the degenerate π* orbitals places one electron in each with parallel spins — Hund's rule in action — giving bond order 2 and predicting paramagnetism. The Lewis structure misses this because it has no mechanism for representing degenerate orbitals.

MO theory's success with O₂ is not just a coincidence; it reflects a deeper truth. When electrons are delocalized over a molecule, localized pair models break down. MO theory handles this naturally because its wavefunctions are inherently molecule-wide. As you extend LCAO to larger molecules — benzene, conjugated polyenes, transition metal complexes — the same framework generalizes, and Hückel MO theory makes it computationally tractable. The key habit to build now is reading MO energy diagrams: identify the symmetry labels (σ, π, *, g, u), count electrons, apply Aufbau and Hund's rule, and read off bond order and magnetic properties directly.
