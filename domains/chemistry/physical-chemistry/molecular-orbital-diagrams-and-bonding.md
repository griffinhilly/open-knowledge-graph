---
id: molecular-orbital-diagrams-and-bonding
title: Molecular Orbital Diagrams and Bond Order
domain: chemistry
course: physical-chemistry
prerequisites:
- id: molecular-orbital-theory-advanced
  type: hard
- id: orbital-theory-and-shapes
  type: hard
- id: quantum-mechanics-postulates-core
  type: soft
- id: molecular-orbital-diagrams-polyatomic
  type: soft
builds-toward:
- perturbation-theory-quantum-chemistry
- selection-rules-electronic-spectroscopy
tags:
- quantum
- bonding
- orbitals
- structure
stage: advanced
status: validated
---
# Molecular Orbital Diagrams and Bond Order

## Core Idea
Molecular orbital diagrams show how atomic orbitals combine to form bonding, antibonding, and nonbonding molecular orbitals in polyatomic molecules. Bond order—calculated as (bonding electrons − antibonding electrons) / 2—quantitatively relates orbital occupancy to bond strength and length. These diagrams provide a visual framework for understanding reactivity and spectroscopic properties.

## How It's Best Learned
Construct MO diagrams for small molecules (O₂, NO, F₂) by starting with atomic orbital energy levels, applying orbital overlap principles, and comparing predictions to experimental bond lengths and magnetic properties (paramagnetism). Verify bond orders using photoelectron spectroscopy data.

## Common Misconceptions
- Assuming higher bond order always means shorter, stronger bonds; actually, nonbonding electrons and occupied antibonding orbitals complicate this relationship. - Treating bonding and antibonding MOs as localized to atom pairs; they are delocalized over the entire molecular framework.

## Questions

```yaml
- question: "O₂ is drawn with a double bond in Lewis notation. What does the MO diagram for O₂ reveal that the Lewis structure cannot predict?"
  type: multiple-choice
  options:
    - "O₂ has a bond order of 3 due to σ-π mixing at this atomic number"
    - "O₂ is paramagnetic because two electrons occupy degenerate π* antibonding orbitals unpaired"
    - "O₂ has no antibonding electrons, which explains its atmospheric stability"
    - "MO theory confirms the Lewis double bond but adds no additional information"
  answer: 1
  explanation: "The π* antibonding orbitals of O₂ are degenerate (equal energy), so by Hund's rule the last two electrons enter them one each — unpaired. Unpaired electrons produce paramagnetism. Lewis structures pair all electrons into bonds and lone pairs and cannot represent this situation; they predict a diamagnetic molecule, which experiment refutes. Liquid O₂ visibly clings between magnet poles. This is one of MO theory's definitive victories over Lewis structures."

- question: "He₂ would place 2 electrons in σ1s (bonding) and 2 electrons in σ*1s (antibonding). What bond order does this give, and what does MO theory predict for He₂?"
  type: multiple-choice
  options:
    - "Bond order = 1; He₂ forms a stable single bond"
    - "Bond order = 2; He₂ is doubly bonded because both bonding and antibonding orbitals are full"
    - "Bond order = 0; He₂ is predicted not to exist as a stable molecule"
    - "Bond order = −1; He₂ is anti-bonded and strongly repulsive"
  answer: 2
  explanation: "Bond order = (bonding electrons − antibonding electrons) / 2 = (2 − 2) / 2 = 0. A bond order of zero means no net bonding: the stabilization from filling σ1s is exactly cancelled by the destabilization from filling σ*1s. He₂ does not exist under normal conditions, consistent with this prediction. This is why noble gases are monatomic — filling both bonding and antibonding MOs gives zero net stabilization regardless of how many electrons are involved."

- question: "Electrons in antibonding molecular orbitals actively destabilize the molecule — they do not merely fail to contribute to bonding."
  type: true-false
  answer: true
  explanation: "This is a critical distinction. A bonding MO lowers the molecular energy relative to separated atoms; an antibonding MO raises it. Each antibonding electron partially cancels the stabilization of a bonding electron — this is why bond order subtracts antibonding occupancy. A molecule like He₂ with equal bonding and antibonding occupancy has zero net bond precisely because the antibonding electrons undo all the stabilization of the bonding ones."

- question: "A molecule with a higher MO bond order will generally have a shorter and stronger bond than a molecule with a lower bond order."
  type: true-false
  answer: false
  explanation: "Bond order correlates with bond strength and length within closely related species (e.g., comparing N₂ bond order 3 with O₂ bond order 2), but is not a universal rule across different molecular frameworks. Atomic size, nonbonding electron repulsion, and the specific orbital types involved all affect bond parameters. The misconception is treating bond order as the sole determinant, when it is a rough guide meaningful primarily within comparable families of molecules."

- question: "Why does MO theory predict O₂ is paramagnetic while a Lewis structure predicts it is diamagnetic, and what does this reveal about Lewis structures?"
  type: short-answer
  answer: "MO theory fills electrons into molecular orbitals by energy, applying Aufbau and Hund's rules. O₂'s last two electrons enter two degenerate π* orbitals one each — unpaired — producing paramagnetism. Lewis structures assign electrons to bonds and lone pairs without access to orbital degeneracy; they cannot represent a state where electrons in equivalent orbitals remain unpaired. This reveals that Lewis structures capture electron counting but miss the quantum mechanical orbital structure governing magnetic and spectroscopic properties."
  explanation: "The experimental paramagnetism of O₂ was known before MO theory provided its explanation. Lewis and valence bond approaches both predicted a paired, diamagnetic structure. MO theory's correct prediction established it as the more complete model of electronic structure, particularly for properties that depend on orbital occupancy and symmetry rather than simple electron-pair counting."
```

## Explainer

From molecular orbital theory, you know that when atoms combine to form molecules, their atomic orbitals mix to produce new orbitals that belong to the molecule as a whole. A **molecular orbital diagram** is the visual tool that organizes this information: atomic orbital energy levels are drawn on the left and right sides, and the molecular orbitals that form from their combination are drawn in the center, with lines connecting each MO to its parent atomic orbitals. The vertical axis represents energy, and electrons are filled into the molecular orbitals from lowest to highest energy, following the Aufbau principle and Hund's rule — exactly as you do for atomic electron configurations.

When two atomic orbitals of similar energy and compatible symmetry overlap, they produce two molecular orbitals: one lower in energy than either parent (**bonding**) and one higher (**antibonding**). The bonding MO has constructive interference of the wavefunctions — electron density builds up between the nuclei, pulling them together. The antibonding MO has destructive interference — a node between the nuclei depletes electron density there, and electrons in this orbital actively weaken the bond. Some atomic orbitals may lack a symmetry-compatible partner and pass through unchanged as **nonbonding** orbitals, contributing neither to bond strength nor weakness.

The **bond order** — calculated as (number of bonding electrons − number of antibonding electrons) / 2 — quantifies the net bonding effect. For O₂, the diagram predicts a bond order of 2 (a double bond), consistent with its bond length and strength. But the diagram reveals something Lewis structures cannot: O₂ has two unpaired electrons in its degenerate π* antibonding orbitals, making it paramagnetic. This is one of the great triumphs of MO theory — it explains O₂'s magnetism, which Lewis dot structures incorrectly predict as a non-issue. Similarly, the MO diagram for NO shows an odd electron in a π* orbital, giving a bond order of 2.5 and explaining its radical character.

Building diagrams for second-row diatomics requires knowing one important detail: for Li₂ through N₂, the σ₂p orbital lies above the π₂p orbitals (due to s-p mixing), while for O₂ and F₂, the σ₂p drops below the π₂p. Getting this ordering right is essential for correct electron configurations and magnetic predictions. Beyond diatomics, MO diagrams extend to polyatomic molecules through group theory and symmetry-adapted linear combinations of atomic orbitals, but the core logic remains the same: identify the symmetry-compatible orbital interactions, rank the resulting MOs by energy, fill electrons, and read off bond orders and electronic properties. The diagram is not just a bookkeeping device — it is a map of molecular electronic structure that predicts stability, reactivity, and spectroscopic behavior.
