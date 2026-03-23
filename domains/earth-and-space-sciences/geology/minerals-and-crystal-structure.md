---
id: minerals-and-crystal-structure
title: Minerals and Crystal Structure
domain: earth-and-space-sciences
course: geology
prerequisites:
- id: atomic-structure-basics
  type: soft
- id: ionic-bonding
  type: soft
- id: covalent-bonding
  type: soft
- id: crystal-structures-and-properties
  type: soft
builds-toward:
- rock-forming-minerals
- weathering-and-erosion
tags:
- minerals
- crystallography
- bonding
- structure
stage: formal-systems
status: validated
---

# Minerals and Crystal Structure

## Core Idea
A mineral is a naturally occurring, inorganic solid with a definite chemical composition and an ordered internal crystal structure. Atoms bond in repeating three-dimensional lattice patterns that determine a mineral's hardness, cleavage, luster, and other physical properties. The dominant bonding types—ionic, covalent, and metallic—explain why quartz is hard and brittle while mica cleaves into thin sheets. Seven crystal systems (cubic, tetragonal, orthorhombic, hexagonal, trigonal, monoclinic, triclinic) classify the symmetry of all mineral lattices.

## How It's Best Learned
Hands-on work with mineral hand samples and a hardness kit grounds abstract lattice theory in observable properties. Comparing the cleavage of halite (perfect cubic) with the conchoidal fracture of quartz makes the link between structure and physical behavior concrete. Connecting what you know about ionic vs. covalent bonds to mineral hardness and melting point reinforces the chemistry prerequisite.

## Common Misconceptions
- 'Rock' and 'mineral' are often used interchangeably, but rocks are aggregates of one or more minerals.
- Hardness (resistance to scratching) is not the same as brittleness; diamond is the hardest mineral but can be cleaved along crystal planes.
- Not all shiny or metallic-looking materials are metals; luster is an optical property, not a compositional one.

## Questions

```yaml
- question: "Mica cleaves into thin, flexible sheets, while quartz fractures conchoidally (in smooth, curved surfaces) and cannot be split into sheets. What accounts for this difference in physical behavior?"
  type: multiple-choice
  options:
    - "Mica is softer than quartz, so it breaks more easily along any surface"
    - "Mica has weak ionic bonds between its silicate sheet layers but strong covalent bonds within each layer; quartz has uniformly strong covalent Si-O bonds throughout its framework"
    - "Mica is an amorphous solid while quartz has a crystal structure, giving quartz no preferred cleavage planes"
    - "Mica cleaves because it contains metalite elements, while quartz is a pure silicate"
  answer: 1
  explanation: "The physical behavior of a mineral is a direct expression of its crystal structure and bonding. Mica's sheet silicate structure has strong covalent bonds within each silicate layer but only weak van der Waals or ionic bonds between layers — so the crystal naturally separates along those weak interlayer planes. Quartz has a three-dimensional framework of Si-O covalent bonds with similar strength in all directions, so there is no preferred weak plane; instead, it fractures in smooth curves (conchoidal fracture) wherever stress is applied. Option A confuses hardness with cleavage — mica is indeed softer (Mohs ~2–3 vs. quartz at 7), but hardness measures scratch resistance, not cleavage tendency."

- question: "Diamond is the hardest known mineral (Mohs hardness 10). What does this tell us about whether diamond can be cleaved?"
  type: multiple-choice
  options:
    - "Diamond cannot be cleaved — its extreme hardness means no force can separate its atoms along any plane"
    - "Diamond can be cleaved along its octahedral crystal planes, despite its hardness, because hardness and cleavage measure different properties"
    - "Diamond's hardness implies it would fracture conchoidally rather than cleave, since all bonds are equally strong"
    - "Diamond can only be cleaved by other diamonds, since only a harder material can break its bonds"
  answer: 1
  explanation: "Hardness (resistance to scratching) and cleavage (tendency to split along crystallographic planes) are distinct properties that measure different aspects of a crystal's bonding. Diamond is the hardest mineral because every carbon atom is covalently bonded to four neighbors with strong, uniform bonds — a scratch requires breaking many bonds simultaneously. But diamond also has perfect octahedral cleavage: the (111) planes are less densely bonded per unit area than other orientations, so a sharp impact along the correct angle causes the crystal to split cleanly. Gem cutters exploit this exact property to shape diamonds. A common misconception conflates 'hard = unbreakable' with 'hard = no preferred fracture plane.'"

- question: "Hardness and resistance to cleavage measure the same underlying property of a mineral's crystal structure."
  type: true-false
  answer: false
  explanation: "False — this is a persistent misconception. Hardness (as defined by the Mohs scale) measures resistance to being scratched, which depends on the overall bond strength and density throughout the crystal. Cleavage measures the tendency to split along specific crystallographic planes where bonding is relatively weaker. Diamond is the hardest mineral (Mohs 10) but has perfect octahedral cleavage. Conversely, a mineral can be relatively soft but have no well-defined cleavage planes (like quartz at Mohs 7, which fractures conchoidally rather than cleaving). The two properties often correlate loosely but are conceptually and physically distinct."

- question: "Rocks are aggregates of one or more minerals, while a single mineral has a definite chemical composition and an ordered internal crystal structure."
  type: true-false
  answer: true
  explanation: "True. The rock/mineral distinction is fundamental in geology. Granite is a rock composed of multiple minerals — quartz, feldspar, and mica — interlocked in irregular patches. Quartz alone is a mineral: it has a fixed composition (SiO₂) and a specific crystalline lattice structure regardless of where it forms. A rock has neither a fixed composition nor a single crystal structure. Glass and obsidian fail the mineral test not on composition but on structure — they lack the ordered internal lattice required for a material to be classified as a mineral."

- question: "How does the type of chemical bonding in a mineral's crystal lattice determine its physical properties, specifically hardness and cleavage? Use at least one specific mineral example."
  type: short-answer
  answer: "The bonds within a crystal lattice control both how hard the mineral is and whether it preferentially breaks along specific planes. Strong, directional covalent bonds resist scratching (high hardness) but may be anisotropic — if bond density varies by direction, the mineral cleaves along weaker planes. Diamond is the hardest mineral because every carbon atom is bonded to four neighbors with strong, uniform covalent bonds, making scratching in any direction difficult; yet it cleaves along octahedral planes where fewer bonds cross the fracture surface. Halite (NaCl) has ionic bonds that are moderately strong but break cleanly along cubic lattice planes where the repulsive like-charge ions align, producing perfect cubic cleavage at moderate hardness (Mohs 2.5). Mica has mixed bonding: strong Si-O covalent bonds within each tetrahedral sheet but weak forces between sheets, producing perfect basal cleavage into thin sheets despite moderate hardness."
  explanation: "The key insight is that physical properties are not arbitrary — they are the macroscopic expression of atomic-scale bonding geometry. Reading a mineral's behavior (hardness, cleavage, fracture) gives direct information about its internal structure."
```

## Explainer

From your study of atomic structure and chemical bonding, you know that atoms bond together in predictable ways depending on their electron configurations. Minerals are what happens when those bonding principles operate under geological conditions — high temperatures, high pressures, and abundant silicon, oxygen, aluminum, and iron. The result is a vast family of naturally occurring crystalline solids, each with a unique combination of composition and structure that determines its physical properties.

The defining feature of a mineral is its **crystal structure**: atoms arranged in a repeating three-dimensional pattern called a **lattice**. This internal order is not optional — it is what distinguishes a mineral from an amorphous solid like volcanic glass. Consider quartz and window glass: both are made of silicon and oxygen, but quartz has a perfectly ordered tetrahedral lattice (each silicon bonded to four oxygens in a repeating framework) while glass has the same atoms frozen in a disordered arrangement. The ordered lattice gives quartz its characteristic hexagonal crystal shape, its hardness of 7 on the Mohs scale, and its conchoidal fracture pattern. Glass, lacking that order, has none of these consistent properties.

The type of bonding within the lattice controls a mineral's physical behavior. **Ionic bonds** — like those in halite (NaCl), where sodium donates an electron to chlorine — produce minerals with moderate hardness and perfect **cleavage** along planes where the ionic bonds are weakest. Break a piece of halite and it shatters into little cubes because the crystal structure is cubic and bonds break most easily along the lattice planes. **Covalent bonds** — where atoms share electrons — are much stronger and more directional. Diamond is pure carbon with every atom covalently bonded to four neighbors in a tetrahedral arrangement, making it the hardest known mineral. But minerals rarely have purely one bond type; most silicate minerals (the largest mineral group, making up over 90% of Earth's crust) have a mix of strong covalent Si-O bonds within silicate tetrahedra and weaker ionic bonds linking those tetrahedra together. This mixed bonding explains why mica cleaves into thin flexible sheets: strong bonds hold atoms together within each sheet, but weak bonds between sheets let them peel apart easily.

All mineral lattices belong to one of **seven crystal systems** — cubic, tetragonal, orthorhombic, hexagonal, trigonal, monoclinic, and triclinic — classified by the symmetry of their unit cell (the smallest repeating box that tiles to build the full lattice). Cubic minerals like halite and garnet have three equal axes at right angles; hexagonal minerals like quartz and beryl have a distinctive six-fold symmetry. Learning to recognize these systems connects the microscopic world of atomic arrangement to the macroscopic shapes you can see and measure in a hand sample. When you pick up a garnet crystal and see its twelve-faced dodecahedral shape, you are looking directly at the expression of its cubic lattice symmetry — the internal atomic order made visible at the scale of your hand.
