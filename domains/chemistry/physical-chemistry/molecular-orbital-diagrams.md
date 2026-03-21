---
id: molecular-orbital-diagrams
title: Constructing Molecular Orbital Diagrams for Diatomics
domain: chemistry
course: physical-chemistry
prerequisites:
- id: quantum-chemistry-foundations
  type: hard
- id: molecular-orbital-theory-advanced
  type: soft
builds-toward:
- bonding-antibonding-orbitals
tags:
- MO-diagrams
- diatomics
- bond-order
- paramagnetism
- energy-levels
stage: advanced
status: draft
---

# Constructing Molecular Orbital Diagrams for Diatomics

## Core Idea
Molecular orbital (MO) diagrams are energy-level diagrams that show how atomic orbitals on separate atoms combine to form molecular orbitals shared across the molecule. For homonuclear diatomics, atomic orbitals of the same symmetry mix to produce bonding (lower energy) and antibonding (higher energy) MOs, and the filling order follows Aufbau, Pauli, and Hund principles. Bond order = (bonding electrons - antibonding electrons)/2 predicts bond strength and existence; the diagram also reveals magnetic properties directly, since unpaired electrons in degenerate MOs produce paramagnetism. A key subtlety is the s-p mixing (orbital ordering switch) that occurs for diatomics lighter than O2, where the sigma-2p orbital rises above the two pi-2p orbitals.

## How It's Best Learned
Construct MO diagrams for the full series Li2 through Ne2, filling electrons and computing bond orders at each step. Compare predicted magnetic behavior (paramagnetic vs diamagnetic) to experimental data -- the O2 case is the classic validation.

## Common Misconceptions
- Assuming the MO energy ordering is the same for all second-row diatomics; the s-p mixing reversal for B2, C2, and N2 changes the sigma/pi ordering below O2.
- Equating bond order with bond strength across different elements; bond order comparisons are most meaningful within the same pair of atoms or isoelectronic series.

## Questions

```yaml
- question: "MO theory predicts that O₂ is paramagnetic. Which feature of the MO diagram explains this, and why can't the Lewis structure for O₂ predict it?"
  type: multiple-choice
  options:
    - "O₂ has an odd total number of electrons, and odd-electron molecules are always paramagnetic"
    - "The two degenerate π*₂p antibonding orbitals each hold one unpaired electron by Hund's rule, giving two unpaired electrons total — a feature Lewis structures have no mechanism to represent"
    - "All of O₂'s electrons occupy bonding orbitals, releasing enough energy to produce a magnetic moment"
    - "The σ₂p orbital in O₂ is singly occupied, providing one unpaired electron"
  answer: 1
  explanation: "O₂ has 12 electrons. After filling σ₂s (2), σ*₂s (2), σ₂p (2), and π₂p (4), the last 2 electrons enter the two degenerate π*₂p orbitals. By Hund's rule, they occupy these orbitals singly with parallel spins — giving two unpaired electrons and paramagnetism. The Lewis structure draws O₂ as O=O with all electrons paired, completely failing to predict this. This is the classic case where MO theory succeeds where Lewis structures fail, and it validates MO theory as the correct framework for understanding molecular electronic structure."

- question: "N₂ has 14 electrons and a bond order of 3. If two electrons are added (forming N₂²⁻), what are the new bond order and magnetic properties?"
  type: multiple-choice
  options:
    - "Bond order increases to 4 and N₂²⁻ is diamagnetic"
    - "Bond order decreases to 2 and N₂²⁻ becomes paramagnetic"
    - "Bond order stays at 3 but N₂²⁻ becomes paramagnetic due to electron repulsion"
    - "Bond order decreases to 2.5 and N₂²⁻ remains diamagnetic"
  answer: 1
  explanation: "N₂'s 14 electrons (using s-p mixing ordering) fill: σ₂s(2), σ*₂s(2), π₂p(4), σ₂p(2) — 8 bonding, 2 antibonding, bond order = 3, diamagnetic. Adding 2 electrons fills both degenerate π*₂p orbitals: bonding = 8, antibonding = 4, bond order = (8−4)/2 = 2. By Hund's rule, the two new electrons each occupy one π*₂p orbital singly — two unpaired electrons, so N₂²⁻ is paramagnetic. Both the weakened bond and the paramagnetism follow directly from reading the MO diagram."

- question: "For second-row diatomics lighter than O₂ (such as N₂ and C₂), the σ₂p molecular orbital lies at lower energy than the degenerate π₂p orbitals."
  type: true-false
  answer: false
  explanation: "For Li₂ through N₂, s-p mixing (interaction between the σ₂s/σ*₂s orbitals and the σ₂p/σ*₂p orbitals) pushes σ₂p upward in energy above the π₂p orbitals. The correct ordering is: σ₂s < σ*₂s < π₂p < σ₂p < π*₂p < σ*₂p. For O₂ and F₂, the larger energy gap between 2s and 2p orbitals reduces this mixing, and σ₂p drops back below π₂p. Getting this switch wrong leads to incorrect electron filling and wrong predictions — for example, incorrectly predicting B₂ is diamagnetic when it is actually paramagnetic."

- question: "A homonuclear diatomic molecule with bond order 0 predicted by its MO diagram is an unstable species that does not exist as an isolated molecule under ordinary conditions."
  type: true-false
  answer: true
  explanation: "Bond order = (bonding electrons − antibonding electrons)/2. A bond order of 0 means equal numbers of bonding and antibonding electrons, so all bonding stabilization is cancelled out. There is no net attraction between the two atoms — no bond. Ne₂ is the canonical example: filling all MOs from σ₂s through σ*₂p with 18 total electrons gives 8 bonding and 8 antibonding electrons (ignoring core), bond order 0. Noble gas diatomics do not form stable molecules, exactly as MO theory predicts. Bond order is thus a direct existence criterion for molecules."

- question: "Why can MO theory correctly predict that O₂ is paramagnetic while Lewis structures cannot, even though both are attempting to describe the same molecule's electrons?"
  type: short-answer
  answer: "Lewis structures distribute electrons as localized pairs in bonds and lone pairs, with no concept of orbital degeneracy or Hund's rule. They inherently assume all electrons are paired. MO theory instead places electrons into molecular orbitals that are energy-ordered and may be degenerate. When electrons partially fill degenerate orbitals (like the two π*₂p in O₂), Hund's rule demands one electron per orbital before pairing — leaving unpaired electrons that cause paramagnetism. Lewis structures have no framework for representing degenerate antibonding orbitals, so they miss this entirely."
  explanation: "The Lewis structure of O₂ (O=O) correctly counts 12 electrons and shows a double bond, but forces all electrons into paired bonds and lone pairs. MO theory reveals that 2 of those 12 electrons must occupy two separate π* antibonding orbitals — a fact that emerges naturally from the energy level diagram and Hund's rule. The experimental paramagnetism of liquid oxygen (it sticks to a magnet) is a direct confirmation of MO theory over Lewis structures."
```

## Explainer

From your study of quantum chemistry foundations and molecular orbital theory, you know that electrons in molecules occupy orbitals that extend over the entire molecule, not just individual atoms. A **molecular orbital (MO) diagram** is the visual tool for organizing these orbitals by energy and seeing how they arise from atomic orbital combinations. Building one for a homonuclear diatomic like O₂ or N₂ follows a systematic procedure that, once mastered, provides immediate predictions about bond strength, bond order, and magnetic behavior.

Start by placing the atomic orbital energy levels for each atom on the left and right sides of the diagram. For second-row diatomics, you use the 2s and 2p orbitals. Orbitals combine according to symmetry: the two 2s orbitals form a **σ₂s** (bonding) and **σ*₂s** (antibonding) pair. The 2p orbitals split by their orientation relative to the internuclear axis. The two p orbitals pointing along the axis (pz) combine to form **σ₂p** and **σ*₂p**, while the perpendicular pairs (px, py) form two degenerate **π₂p** (bonding) and **π*₂p** (antibonding) pairs. Every atomic orbital that goes in produces one bonding and one antibonding MO — orbital count is conserved.

The critical subtlety is the **s-p mixing** (also called s-p hybridization in the MO context). For lighter diatomics — Li₂ through N₂ — the 2s and 2p energy levels on the atoms are close enough that the σ₂s and σ₂p orbitals interact, pushing σ₂p up in energy above the π₂p orbitals. This gives the ordering: σ₂s < σ*₂s < π₂p < σ₂p < π*₂p < σ*₂p. For O₂ and F₂, the larger 2s-2p energy gap reduces this mixing, and the "normal" ordering holds: σ₂p drops below π₂p. Getting this switch right is essential — it determines whether B₂ and C₂ are paramagnetic or diamagnetic.

Once the energy levels are set, fill electrons from the bottom up following the **Aufbau principle**, **Pauli exclusion** (two electrons per orbital, opposite spins), and **Hund's rule** (fill degenerate orbitals singly before pairing). Then calculate **bond order = (bonding electrons − antibonding electrons)/2**. For O₂, you fill 12 electrons and get bond order 2 (a double bond), but the diagram also reveals two unpaired electrons in the degenerate π*₂p orbitals — correctly predicting that O₂ is **paramagnetic**, a fact that Lewis structures cannot explain. For N₂, bond order is 3 (a triple bond) with no unpaired electrons (diamagnetic). Ne₂ gives bond order 0 — confirming that neon does not form a stable diatomic. The MO diagram thus unifies bond strength, bond existence, and magnetic properties in a single framework.
