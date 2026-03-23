---
id: crystal-structures-and-properties
title: Crystal Structures and Solid Properties
domain: chemistry
course: general-chemistry
prerequisites:
- id: ionic-bonding-formation
  type: soft
- id: metallic-bonding-and-conductivity
  type: soft
builds-toward:
- states-of-matter-phase-changes
tags:
- crystal structure
- solid state
- unit cell
- ionic crystals
stage: formal-systems
status: validated
---

# Crystal Structures and Solid Properties

## Core Idea
Solids form repeating 3D patterns of atoms or ions. Ionic solids have alternating cations and anions in fixed arrangements. Metallic solids have atoms in close-packed arrays. Covalent network solids have all atoms bonded throughout. Molecular solids have discrete molecules held by intermolecular forces. Crystal type determines physical properties like hardness and melting point.

## Questions

```yaml
- question: "A newly synthesized material forms a solid with an extremely high melting point, exceptional hardness, and no electrical conductivity in any state — solid, liquid, or dissolved. What crystal structure does it most likely have?"
  type: multiple-choice
  options:
    - "Ionic crystal (like NaCl)"
    - "Metallic crystal (like copper)"
    - "Covalent network solid (like diamond)"
    - "Molecular solid (like ice)"
  answer: 2
  explanation: "Covalent network solids consist of atoms connected by continuous covalent bonds throughout the entire crystal — there are no discrete molecules and no free electrons or ions. This produces exceptional hardness (breaking the solid requires breaking strong covalent bonds), very high melting points (same reason), and no electrical conductivity in any state (no mobile charge carriers). Ionic solids also have high melting points but conduct when molten or dissolved. Metallic solids conduct readily. Molecular solids have low melting points and are soft."

- question: "Why are ionic crystals brittle rather than malleable, while metals can be bent and shaped without fracturing?"
  type: multiple-choice
  options:
    - "Ionic bonds are weaker than metallic bonds, so ionic crystals break more easily under stress"
    - "When layers of an ionic crystal shift under stress, like charges come face to face, producing strong repulsive forces that fracture the crystal"
    - "The electron sea in metallic bonding lubricates layer sliding, while ionic crystals lack any lubrication"
    - "Ionic crystals have lower melting points, making them more susceptible to mechanical failure"
  answer: 1
  explanation: "Brittleness in ionic crystals is structural. In the undisturbed lattice, each positive ion is surrounded by negative ions, maximizing attraction. When a force shifts one layer relative to another, previously alternating charges suddenly align — positive faces positive, negative faces negative. The resulting electrostatic repulsion is enormous and the crystal snaps along the slip plane. In metals, when layers slide, the delocalized electron sea simply redistributes around the new arrangement, maintaining cohesion rather than shattering."

- question: "A molecular solid like sugar has a lower melting point than an ionic solid like table salt because melting molecular solids requires overcoming only weak intermolecular forces, not the strong ionic bonds of the crystal lattice."
  type: true-false
  answer: true
  explanation: "In molecular solids, discrete molecules are held together by relatively weak forces — hydrogen bonds, dipole-dipole interactions, or London dispersion forces. Melting only requires overcoming these intermolecular forces, not breaking any covalent bonds within the molecules. In ionic solids, melting requires separating ions held together by strong electrostatic attractions throughout the lattice. This is why NaCl melts at 801°C while sugar melts around 160°C."

- question: "Metals conduct electricity well because each metal atom forms strong directional covalent bonds with its neighbors, which frees electrons to move through the lattice."
  type: true-false
  answer: false
  explanation: "This confuses the mechanism entirely. Metal atoms do NOT form directional covalent bonds — they release their valence electrons into a delocalized 'electron sea' shared collectively by all atoms in the lattice. It is precisely the absence of directional bonds that explains both metallic conductivity (free electrons carry charge) and metallic malleability (layers can slide without breaking specific bonds). Covalent bonds are directional and localized; metallic bonding is non-directional and delocalized. Materials with strong directional covalent bonds (like diamond) are electrical insulators and brittle, not conductors and malleable."

- question: "Why do metals conduct electricity while ionic solids in the solid state do not, even though both types of materials contain charged particles?"
  type: short-answer
  answer: "Conductivity requires mobile charge carriers. In metals, valence electrons are delocalized into an electron sea — they are not bound to individual atoms and can move freely through the lattice under an applied electric field. In ionic solids, the charged particles (cations and anions) are locked into fixed positions in the crystal lattice by strong electrostatic forces. The ions cannot move in response to an electric field. When an ionic solid is melted or dissolved in water, however, the lattice is disrupted and the ions become free to move — so ionic compounds conduct electricity in liquid or dissolved form, just not as solids."
  explanation: "This comparison highlights why the type of bonding — not just the presence of charge — determines conductivity. The key variable is mobility: conduction requires charges that can move in response to a field. Metallic bonding inherently produces mobile electrons; ionic bonding inherently immobilizes charges in a lattice. Electrical conductivity is therefore a diagnostic property for identifying crystal type, alongside melting point, hardness, and brittleness."
```

## Explainer

When a liquid cools into a solid, the particles arrange themselves into a repeating three-dimensional pattern called a **crystal lattice**. The smallest repeating unit of this pattern is the **unit cell** — think of it as the tile that, when copied in all directions, builds the entire crystal. From your work with ionic and metallic bonding, you already know the forces holding these particles together. Crystal structure is where those forces become visible as architecture.

**Ionic solids** like sodium chloride arrange alternating cations and anions so that every positive ion is surrounded by negative ions and vice versa, maximizing electrostatic attraction while minimizing repulsion. The result is a rigid, brittle lattice with high melting points — it takes enormous energy to pull all those opposite charges apart. When you strike an ionic crystal, layers shift so that like charges suddenly face each other, and the crystal shatters along clean planes. Ionic solids do not conduct electricity as solids because ions are locked in place, but they conduct when melted or dissolved because the ions become free to move.

**Metallic solids** take a different approach. Metal atoms pack together as tightly as possible — often in face-centered cubic or hexagonal close-packed arrangements — with their valence electrons delocalized into a shared "electron sea." This delocalization, which you studied in metallic bonding, explains why metals conduct electricity and heat so well: electrons flow freely through the lattice. It also explains malleability — when layers of metal atoms slide past each other, the electron sea simply redistributes around the new arrangement, maintaining cohesion rather than shattering.

**Covalent network solids** like diamond and quartz are built from atoms connected by continuous covalent bonds extending throughout the entire crystal. There are no discrete molecules — the whole crystal is essentially one giant molecule. This makes them extraordinarily hard and gives them very high melting points, because breaking the solid means breaking strong covalent bonds. **Molecular solids** like ice or sugar, by contrast, consist of individual molecules held together only by weak intermolecular forces (hydrogen bonds, dipole-dipole, or London dispersion). The covalent bonds within each molecule are strong, but the forces between molecules are weak, so molecular solids have low melting points and are soft. The key insight is that a solid's physical properties — melting point, hardness, electrical conductivity, brittleness — are direct consequences of which type of bonding holds the crystal together.
