---
id: ceramic-structure-and-properties
title: Ceramic Structure and Properties
domain: engineering
course: materials-science
prerequisites:
- id: crystal-structure-basics
  type: hard
- id: ionic-bonding
  type: hard
- id: covalent-bonding
  type: soft
builds-toward:
- composite-materials
tags:
- ceramic
- brittleness
- oxides
- silicates
- thermal-stability
stage: formal-systems
status: validated
---

# Ceramic Structure and Properties

## Core Idea
Ceramics are inorganic, non-metallic solids held together primarily by ionic and/or covalent bonds. Their crystal structures are governed by the ratio of cation to anion radii, which determines coordination number and packing geometry (e.g., NaCl, ZnS, CsCl structures). Strong, directional bonds give ceramics high hardness, high melting points, chemical inertness, and electrical insulativity — but also extreme brittleness due to immobile dislocations and no ductile energy absorption before fracture. Glasses are amorphous ceramics with a continuous network structure. Engineering ceramics (Al₂O₃, SiC, Si₃N₄) exploit these properties in cutting tools, armor, thermal barrier coatings, and biomedical implants.

## How It's Best Learned
Compare dislocation mobility in NaCl (limited) vs. a metal (easy) and explain why this leads to brittleness. Calculate coordination numbers from ionic radii ratios and match to known crystal structures.

## Common Misconceptions
- Ceramic brittleness is not because ceramics are weak — alumina is stronger in compression than most steels. It fails because it cannot redistribute stress plastically.
- Glasses are not crystalline; they are supercooled liquids with no long-range order, which is why they are isotropic and have no defined melting point.

## Explainer

Ceramics are built from ionic and covalent bonds — both of which you have studied as prerequisites. Recall that ionic bonding involves electrostatic attraction between oppositely charged ions, and covalent bonding involves shared electron pairs with directional character. In ceramics, these bond types are often mixed: alumina (Al₂O₃) is largely ionic, silicon carbide (SiC) is largely covalent, and silica (SiO₂) combines both. What both bond types share is that they are strong, stiff, and — critically — non-directional slip is impossible. This last point explains nearly every distinctive property of ceramics.

The crystal structure of a ceramic is governed by one geometric rule: each cation must be surrounded by enough anions to satisfy charge neutrality, and the ions must pack without interpenetrating. The **radius ratio** r_cation/r_anion predicts the **coordination number** — how many anions surround each cation. A small cation (radius ratio < 0.41) fits into tetrahedral holes (coordination 4); a larger one fits into octahedral holes (coordination 6); a very large one fits into cubic holes (coordination 8). NaCl has octahedral coordination (ratio ~0.56), ZnS has tetrahedral coordination (~0.40), and CsCl has cubic coordination (~0.93). From your crystal structure prerequisite, you know these packing arrangements — ceramics simply add the electrostatic constraint that opposite charges must neighbor each other.

The practical consequences of strong, directional bonds fall into two categories: desirable and dangerous. Desirable: ceramics have very high melting points (Al₂O₃ melts at 2072°C), high hardness (diamond hardness is a ceramic extreme), low electrical conductivity (no free electrons), chemical inertness, and excellent strength in compression. Dangerous: ceramics cannot undergo **plastic deformation**. In metals, dislocations — line defects — move easily through the crystal under stress, redistributing load and allowing the metal to absorb energy before fracture (ductility). In ceramics, moving a dislocation would force like-charged ions next to each other, requiring enormous energy. So dislocations are effectively immobile, and under tensile stress, cracks simply propagate without any plastic redistribution. The result is catastrophic brittle fracture at stresses that a metal would survive easily.

Engineering around ceramic brittleness takes several forms. **Transformation toughening** (as in zirconia-toughened alumina) exploits a stress-induced phase transformation that absorbs energy at crack tips. **Fiber reinforcement** (as in ceramic matrix composites) provides crack-bridging and pull-out mechanisms. **Compression loading** exploits the fact that ceramics are strong in compression — pre-stressing ceramic components like tempered glass puts the surface in compression so that service tensile loads must first overcome the compressive pre-stress before opening a crack. Understanding both the bond-level reason for brittleness and these engineering workarounds is essential for selecting ceramics in thermal, structural, and biomedical applications.
