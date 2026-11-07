---
id: carbon-allotropes-nanocarbons
title: "Carbon Allotropes: Diamond, Graphite, Fullerenes, Nanotubes, and Graphene"
domain: chemistry
course: materials-chemistry
prerequisites:
- id: hybridization-sp-orbitals
  type: hard
- id: electronic-band-theory-of-solids
  type: soft
- id: aromatic-compounds-intro
  type: soft
- id: crystal-structures-and-unit-cells
  type: soft
builds-toward: []
tags:
- allotropes
- diamond
- graphite
- fullerenes
- carbon nanotubes
- graphene
stage: advanced
status: validated
---

# Carbon Allotropes: Diamond, Graphite, Fullerenes, Nanotubes, and Graphene

## Core Idea
Carbon forms several allotropes whose very different properties come from how the atoms are bonded. In diamond, every carbon is sp³ and bonded to four neighbors in a rigid 3D network, giving an extremely hard electrical insulator. In graphite, sp² carbons form flat hexagonal sheets with delocalized π electrons, so it conducts along the sheets and the weakly bound layers slide. Curling or isolating sp² sheets gives the nanocarbons: fullerenes such as C₆₀, carbon nanotubes, and single-layer graphene.

## How It's Best Learned
Start from hybridization: build a diamond model and a graphite layer model and relate each property (hardness, conductivity, lubrication) to the bonding. Then show how graphene is one graphite layer, how rolling it gives a nanotube, and how adding twelve pentagons closes it into a fullerene. Finish with the nanotube (n,m) rule to see how geometry controls electronic behavior.

## Common Misconceptions
- Diamond and graphite are different elements or compounds. (Both are pure carbon; they differ only in bonding and structure.)
- Graphite is soft because its C–C bonds are weak. (The in-plane C–C bonds are very strong; graphite is soft because the layers are held together only by weak van der Waals forces.)
- All carbon nanotubes are metallic conductors. (Whether a single-walled nanotube is metallic or semiconducting depends on how the graphene sheet is rolled, described by the chiral indices (n,m).)

## Questions

```yaml
- question: "Why does graphite conduct electricity while diamond does not?"
  type: multiple-choice
  options: ["Graphite contains metal impurities", "Graphite's sp² carbons have delocalized π electrons that move within each layer, while diamond's sp³ carbons have all electrons in localized σ bonds", "Diamond has weaker C–C bonds", "Graphite is an ionic solid"]
  answer: 1
  explanation: "Each graphite carbon uses three electrons in σ bonds and contributes one to a π system spread over the whole sheet. In diamond all four electrons are in localized σ bonds, and a large band gap leaves no mobile carriers."
- question: "Buckminsterfullerene, C₆₀, is built from how many pentagons and hexagons?"
  type: multiple-choice
  options: ["6 pentagons and 20 hexagons", "12 pentagons and 20 hexagons", "12 pentagons and 30 hexagons", "20 pentagons and 12 hexagons"]
  answer: 1
  explanation: "C₆₀ has the shape of a truncated icosahedron, like a soccer ball, with 12 pentagonal and 20 hexagonal faces. Twelve pentagons are exactly what is needed to close a sheet of hexagons into a cage."
- question: "Every single-walled carbon nanotube is a metallic conductor."
  type: true-false
  answer: false
  explanation: "For a tube with chiral indices (n,m), it is metallic or nearly so when n − m is a multiple of 3, and semiconducting otherwise. Armchair tubes (n = m) are metallic."
- question: "How was graphene first isolated as a single layer, and why was this significant?"
  type: short-answer
  answer: "In 2004, Andre Geim and Konstantin Novoselov peeled graphite repeatedly with adhesive tape (mechanical exfoliation) until single atomic layers remained. It showed that a stable two-dimensional crystal could exist and opened the study of its unusual electronic properties, recognized by the 2010 Nobel Prize in Physics."
  explanation: "The simplicity of the method made graphene widely available for experiments. Its electrons behave as if massless near the Fermi level, giving very high carrier mobility."
```

## Explainer

Carbon can bond in several ways, and each way builds a different solid. These solid forms of one element are called allotropes.

In diamond, each carbon atom is sp³ hybridized and bonded to four others at the corners of a tetrahedron. The bonds extend in three dimensions into one giant covalent network. Breaking the crystal means breaking many strong C–C bonds, so diamond is the hardest natural material. All valence electrons sit in localized σ bonds, and the large band gap makes diamond an electrical insulator. It is, however, an excellent conductor of heat, because the stiff lattice carries vibrations efficiently.

In graphite, each carbon is sp² hybridized and bonded to three neighbors in a flat sheet of hexagons. The fourth electron of each atom sits in a p orbital perpendicular to the sheet, and these orbitals form a delocalized π system across the layer. Electrons can move freely within the sheet, so graphite conducts electricity along its layers. Between the layers, about 0.335 nm apart, only weak van der Waals forces act, so layers slide over one another. That is why graphite works as a lubricant and leaves marks as pencil "lead."

A single layer of graphite is graphene. Andre Geim and Konstantin Novoselov isolated it in 2004 by peeling graphite with adhesive tape. They shared the 2010 Nobel Prize in Physics. Graphene has no band gap and very high electron mobility, and it is extremely strong for its thickness.

Curved sp² carbon gives two more families. A sheet of hexagons cannot close on itself, but adding exactly twelve pentagons lets it form a cage. The best known cage is C₆₀, buckminsterfullerene, with 12 pentagons and 20 hexagons in the pattern of a soccer ball. Harold Kroto, Robert Curl and Richard Smalley discovered it in 1985 and received the 1996 Nobel Prize in Chemistry.

Rolling a graphene sheet into a seamless cylinder gives a carbon nanotube. Sumio Iijima's 1991 report of multiwalled tubes started intense research. The way the sheet is rolled, labeled by two integers (n,m), controls the electronic behavior. Some tubes are metallic and others are semiconductors, even though both are pure carbon.

Across all five forms, the composition is the same. Hybridization sets the geometry, and geometry sets hardness, conductivity and band structure.
