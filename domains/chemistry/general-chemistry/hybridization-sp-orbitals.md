---
id: hybridization-sp-orbitals
title: 'Orbital Hybridization: sp, sp², and sp³'
domain: chemistry
course: general-chemistry
prerequisites:
- id: covalent-bonding
  type: hard
- id: vsepr-theory
  type: hard
builds-toward:
- molecular-geometry
- bonding-antibonding-orbitals
tags:
- hybridization
- sp orbitals
- molecular geometry
stage: advanced
status: draft
---

# Orbital Hybridization: sp, sp², and sp³

## Core Idea
Hybridization describes the mixing of atomic orbitals to form new orbitals for bonding. The type of hybridization (sp, sp², sp³) directly correlates with molecular geometry and bond angles.

## How It's Best Learned
Start with Lewis structures and VSEPR predictions, then determine hybridization type from geometry.

## Common Misconceptions
Thinking hybridization happens before bonding; confusing the number of hybrid orbitals with bond count.

## Questions

```yaml
- question: "Nitrogen in ammonia (NH₃) forms three bonds to hydrogen atoms. What is nitrogen's hybridization in ammonia?"
  type: multiple-choice
  options:
    - "sp — nitrogen uses one s and one p orbital for its three bonds"
    - "sp² — three bonds require three hybrid orbitals"
    - "sp³ — three bonds plus one lone pair give four electron groups requiring four hybrid orbitals"
    - "sp³d — nitrogen requires an expanded octet to form three bonds"
  answer: 2
  explanation: "Hybridization is determined by the total number of electron groups around the central atom — including lone pairs, not just bonds. Nitrogen in NH₃ has three N-H bonds and one lone pair, giving four electron groups. Four electron groups require four hybrid orbitals, so nitrogen is sp³ hybridized. The common mistake is counting only bonds (three) and concluding sp² — but lone pairs occupy hybrid orbitals just as bonding pairs do."

- question: "Which statement correctly distinguishes sp² from sp³ hybridization in carbon?"
  type: multiple-choice
  options:
    - "sp² carbon has one unhybridized p orbital available for π bonding; sp³ carbon does not"
    - "sp² carbon forms more total bonds than sp³ carbon"
    - "sp³ hybridization requires more energy to form than sp² hybridization"
    - "sp² hybridization occurs as a prior step before carbon bonds to three atoms"
  answer: 0
  explanation: "sp² carbon mixes one s + two p orbitals, leaving one p orbital unhybridized and perpendicular to the plane of the three hybrid orbitals. This leftover p orbital is what forms π bonds in double bonds. sp³ carbon mixes all three p orbitals, leaving none for π bonding. Option B is wrong — sp² carbon in ethylene forms the same number of total bonds as sp³ carbon in methane (four). Option D reverses causation: hybridization describes the result of bonding, not a preparatory process."

- question: "An atom's hybridization can be determined by counting the number of atoms bonded to it, since each bond requires one hybrid orbital."
  type: true-false
  answer: false
  explanation: "This is a critical misconception. Hybridization is determined by the total number of electron groups — both bonds AND lone pairs. Water (H₂O) has two O-H bonds but also two lone pairs on oxygen, giving four electron groups and sp³ hybridization, not sp. Counting only bonded atoms would incorrectly predict sp hybridization for water and give the wrong geometry. Always count lone pairs when determining hybridization."

- question: "A carbon atom in a C=C double bond is sp² hybridized, with the π bond formed by lateral overlap of two unhybridized p orbitals that are not part of the hybrid orbital set."
  type: true-false
  answer: true
  explanation: "sp² hybridization mixes one s + two p orbitals to produce three sp² hybrid orbitals arranged at 120° in a plane, which form the three σ bonds. The remaining unhybridized p orbital on each carbon sticks out perpendicular to this plane and overlaps sideways with its counterpart on the adjacent carbon to form the π bond. This division — sp² hybrids for σ bonds, unhybridized p for π — correctly explains both the 120° bond angles and the nature of double bonds."

- question: "Why does the number of hybrid orbitals equal the number of atomic orbitals mixed, and what does this imply about where lone pairs are located?"
  type: short-answer
  answer: "Orbital hybridization conserves the number of orbitals: mixing N atomic orbitals always produces exactly N hybrid orbitals. This means lone pairs must occupy hybrid orbitals — there are no separate 'unhybridized' slots for them. In ammonia, four orbitals mix (one s + three p) to give four sp³ hybrid orbitals; three hold bonding pairs and one holds the lone pair. Lone pairs count toward hybridization just as bonds do."
  explanation: "Orbital arithmetic is the key: start with N atomic orbitals, end with N hybrid orbitals, each holding either a bonding pair or a lone pair. The energy cost of mixing is paid by forming stronger, more directional bonds. Placing lone pairs in hybrid orbitals minimizes electron-electron repulsion by pointing them toward the corners of a tetrahedron (in sp³) rather than leaving them in compact spherical s orbitals. This is why water's bond angle is 104.5° rather than 90° — the lone pairs in sp³-like orbitals push the bonding pairs closer together than unhybridized p orbitals would."
```

## Explainer

You already know from VSEPR theory that electron groups around a central atom arrange themselves to minimize repulsion, producing geometries like linear, trigonal planar, and tetrahedral. Hybridization explains *why* bonds point in those directions by describing how atomic orbitals mix to create new orbitals oriented toward bonding partners.

Consider carbon in methane (CH₄). A ground-state carbon atom has the configuration 1s² 2s² 2p², with two unpaired electrons in separate 2p orbitals. This suggests carbon should form only two bonds — but it forms four. The resolution is that one 2s and three 2p orbitals **hybridize** (mathematically mix) to produce four equivalent **sp³ hybrid orbitals**, each containing one electron and pointing toward the corner of a tetrahedron. The energy cost of mixing is more than repaid by forming four strong bonds instead of two. The resulting bond angle is 109.5°, exactly matching VSEPR's prediction for four electron groups.

The pattern extends to other hybridization types. When carbon forms a double bond (as in ethylene, C₂H₄), it needs only three σ-bonding directions in a plane. One 2s and two 2p orbitals mix to form three **sp² hybrid orbitals** arranged in a trigonal planar geometry (120° apart), while the remaining unhybridized p orbital sticks out perpendicular to the plane and forms the π bond of the double bond. In a triple bond (as in acetylene, C₂H₂), one 2s and one 2p orbital mix to give two **sp hybrid orbitals** pointing in opposite directions (180°, linear), while two unhybridized p orbitals form two π bonds. The rule is simple: count the number of electron groups (σ bonds + lone pairs) around an atom — 4 groups means sp³, 3 means sp², 2 means sp.

A critical point: hybridization is a model that describes the *result* of bonding, not a process that happens before bonds form. Atoms do not first hybridize and then look for partners — the mixing of orbitals occurs because it produces a lower-energy bonded state. Also, the number of hybrid orbitals equals the number of atomic orbitals that mixed, and each hybrid orbital holds either a bonding pair or a lone pair. Lone pairs occupy hybrid orbitals just like bonding pairs do: ammonia (NH₃) is sp³ with three bonding pairs and one lone pair, giving a tetrahedral electron geometry but a pyramidal molecular shape — consistent with what VSEPR already told you.
