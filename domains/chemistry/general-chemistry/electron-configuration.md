---
id: electron-configuration
title: Electron Configuration
domain: chemistry
course: general-chemistry
prerequisites:
- id: atomic-structure-basics
  type: hard
- id: atomic-orbitals
  type: soft
- id: periodic-table-overview
  type: soft
- id: quantum-numbers
  type: soft
- id: pauli-exclusion-principle
  type: soft
builds-toward:
- periodic-trends
- ionic-bonding
- covalent-bonding
tags:
- orbitals
- aufbau
- Pauli-exclusion
- Hunds-rule
- valence-electrons
- subshells
stage: advanced
status: validated
---

# Electron Configuration

## Core Idea
Electrons fill atomic orbitals in order of increasing energy following the Aufbau principle, with at most two electrons per orbital (Pauli exclusion principle) and one electron in each degenerate orbital before pairing begins (Hund's rule). The resulting electron configuration — for example, 1s²2s²2p⁶ — specifies how electrons are distributed across subshells. The outermost electrons (valence electrons) govern chemical bonding and reactivity, while the periodic table's block structure directly reflects orbital filling order.

## How It's Best Learned
Practice writing full and noble-gas shorthand configurations for elements across the periodic table, using the periodic table's block layout as a guide. Pay special attention to exceptions like Cr ([Ar]3d⁵4s¹) and Cu ([Ar]3d¹⁰4s¹), where half-filled or fully filled d subshells provide extra stability.

## Common Misconceptions
- When ions form, electrons are removed from the highest principal quantum number shell first (not the last orbital filled in the Aufbau sequence) — so Fe²⁺ loses 4s electrons before 3d.
- Noble-gas shorthand is convenient, but the noble gas symbol replaces all inner electrons, not just those in the previous row.

## Questions

```yaml
- question: "What is the electron configuration of Fe²⁺? (Iron's neutral configuration is [Ar]3d⁶4s².)"
  type: multiple-choice
  options: ["[Ar]3d⁴4s²", "[Ar]3d⁶", "[Ar]3d⁵4s¹", "[Ar]3d⁴4s²"]
  answer: 1
  explanation: "When transition metals form ions, electrons are removed from the highest principal quantum number first — the 4s electrons are lost before the 3d. So Fe²⁺ = [Ar]3d⁶, not [Ar]3d⁴4s². This is counterintuitive because 4s fills before 3d in neutral atoms (Aufbau), but energetics shift upon ionization so 4s becomes higher in energy than 3d."

- question: "According to Hund's rule, two electrons in the same subshell always pair up in the same orbital before occupying empty orbitals."
  type: true-false
  answer: false
  explanation: "Hund's rule states the opposite: electrons fill empty degenerate orbitals one at a time with parallel spins before any pairing occurs. Pairing is energetically costly due to electron-electron repulsion. Carbon (1s²2s²2p²), for example, has its two 2p electrons in separate p orbitals, not the same one."

- question: "Why does chromium have the electron configuration [Ar]3d⁵4s¹ rather than the expected [Ar]3d⁴4s²?"
  type: short-answer
  answer: "A half-filled d subshell (3d⁵) has extra stability due to exchange energy — electrons with the same spin in different orbitals lower the total energy through favorable exchange interactions. This stabilization is large enough that one electron migrates from 4s to 3d, giving a half-filled d subshell at the cost of a singly occupied 4s."
  explanation: "This is one of several Aufbau exceptions where the stability of a half-filled or fully filled d subshell (e.g., Cu = [Ar]3d¹⁰4s¹) outweighs the expected energy ordering. These exceptions matter for predicting the reactivity and magnetic properties of transition metals."
```

## Explainer

Your knowledge of atomic structure tells you that electrons occupy energy levels around the nucleus. Electron configuration systematizes exactly where those electrons go — which subshells, how many in each, and in what arrangement. Three rules govern the filling.

The **Aufbau principle** says electrons fill orbitals in order of increasing energy. The periodic table's block structure gives you the sequence: 1s, 2s, 2p, 3s, 3p, 4s, 3d, 4p, 5s, 4d, 5p... The fact that 4s fills before 3d reflects a quantum mechanical result — when the 3d subshell is empty, 4s sits at slightly lower energy. The **Pauli exclusion principle** caps each orbital at two electrons with opposite spins. An orbital is a quantum state defined by four quantum numbers; no two electrons can share all four, so the maximum occupancy per orbital is two. **Hund's rule** resolves what happens when multiple orbitals of equal energy (degenerate orbitals) are available: electrons spread out with parallel spins first, pairing only when no empty orbitals remain. Pairing costs energy because two electrons in the same orbital repel each other more strongly than two in separate orbitals.

The practical skill is writing configurations quickly. Using noble-gas shorthand, you replace all filled inner shells with the symbol of the preceding noble gas in brackets: iron is [Ar]3d⁶4s² rather than the full 26-electron string. The periodic table makes this mechanical — count along the s-block (left), p-block (right), d-block (middle transition metals), or f-block (lanthanides and actinides) to track which subshell you are filling.

A critical exception catches many students: when a transition metal loses electrons to form a cation, the Aufbau sequence reverses. Electrons are removed from the highest principal quantum number first. For iron (Fe: [Ar]3d⁶4s²), losing two electrons gives Fe²⁺: [Ar]3d⁶ — not [Ar]3d⁴4s², as you might guess by undoing the filling order. The 4s electrons leave first because ionization shifts the relative energies of 4s and 3d, making 4s higher in energy in the cation. This has real consequences: transition metal ions like Fe²⁺ and Fe³⁺ differ by one 3d electron, affecting their color, magnetism, and reactivity.

Finally, the periodic table's block structure is a physical map of orbital filling. Elements in the same group share the same valence electron count and therefore similar chemistry. The valence electrons — those in the outermost shell — are what bond with other atoms. Understanding electron configuration is not just bookkeeping; it is the structural foundation for all of chemical bonding, periodic trends, and spectroscopic properties.
