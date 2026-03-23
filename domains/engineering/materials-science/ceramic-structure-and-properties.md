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

## Questions

```yaml
- question: "A ceramic cutting tool shatters catastrophically when subjected to a tensile load that steel tooling handles without permanent damage. The ceramic's compressive strength exceeds the steel's, yet it fails at much lower tensile stress. What best explains this?"
  type: multiple-choice
  options:
    - "Ceramics have weaker chemical bonds than metals, so they fail at lower stress in all loading modes"
    - "Dislocations in ceramics cannot move under tensile stress because doing so would force like-charged ions adjacent, so cracks propagate without any plastic redistribution of load"
    - "Ceramics are porous materials, and porosity reduces tensile strength more than compressive strength"
    - "Ionic bonds are strong in compression but weak in tension, so ceramics always fail in tension before compression"
  answer: 1
  explanation: "Ceramic brittleness is not about weak bonds — ceramics have very strong ionic and covalent bonds and can exceed steel in compressive strength. The problem is dislocation mobility. In metals, dislocations glide through the crystal under shear stress, redistributing load and absorbing energy (ductility). In ionic ceramics, moving a dislocation would bring like-charged ions into adjacent positions, creating enormous electrostatic repulsion — the energy barrier is prohibitive. So ceramics cannot plastically deform. When tensile stress concentrates at a crack tip, there is no plastic zone to blunt the crack; it propagates catastrophically. This is the bond-level explanation for brittleness."

- question: "An engineer needs to use a ceramic component under heavy mechanical loading. Which loading mode should she design for to best exploit ceramics' mechanical properties?"
  type: multiple-choice
  options:
    - "Tensile loading — ceramics are most reliable under uniform tension because their bonds resist stretching"
    - "Compressive loading — ceramics are much stronger in compression because cracks do not open under compressive stress"
    - "Torsional loading — ceramics are isotropic and handle twisting without preferential crack propagation"
    - "Fatigue loading — ceramics do not fatigue like metals because they have no dislocations to accumulate damage"
  answer: 1
  explanation: "Ceramics are far stronger in compression than in tension — often by a factor of 10 or more. Under compressive stress, crack faces are pressed together rather than pulled apart, so cracks cannot propagate. This is why tempered glass, concrete, and ceramic armor are designed so that expected service loads put the ceramic in compression (or at least counteract tensile stresses with pre-compression). In contrast, any tensile stress, bending, or impact creates tensile regions where brittle fracture can initiate from surface flaws. Engineering with ceramics always involves minimizing tensile stresses."

- question: "Ceramic brittleness is a consequence of material weakness — ceramics fracture at low stress because their bonds are not as strong as metallic bonds."
  type: true-false
  answer: false
  explanation: "This is the key misconception. Ceramics are NOT weak materials — alumina (Al₂O₃) can withstand compressive stresses exceeding 2,000 MPa, surpassing most steels. The brittleness is not about bond strength; it is about the inability to absorb energy through plastic deformation. Metals survive tensile loading partly because dislocations move and distribute stress, blunting crack tips. Ceramics lack this mechanism: cracks grow unchecked because no plastic zone forms at the tip. A ceramic fails not because the bonds are weak, but because all the stress concentrates at crack tips with no mechanism to redistribute it."

- question: "In an ionic ceramic crystal structure, the coordination number of a cation is primarily determined by the ratio of cation radius to anion radius."
  type: true-false
  answer: true
  explanation: "Yes — this is the geometric rule governing ionic crystal structures. For the crystal to be stable, anions must surround each cation and make contact with it (touching constraint), and the overall arrangement must satisfy charge neutrality. As the cation-to-anion radius ratio increases, the cation is large enough to be surrounded by more anions. Ratios below ~0.41 favor tetrahedral coordination (4 anions), ~0.41–0.73 favor octahedral coordination (6 anions), and above ~0.73 favor cubic coordination (8 anions). This is why NaCl (ratio ~0.56) has the rock-salt (octahedral) structure while CsCl (ratio ~0.93) has the cesium-chloride (cubic) structure."

- question: "Why are dislocations effectively immobile in ionic ceramics, and how does this cause brittle fracture rather than ductile deformation?"
  type: short-answer
  answer: "In an ionic crystal, the lattice alternates between positively and negatively charged ions. A dislocation is a line defect representing an extra half-plane of atoms. For a dislocation to move (glide), the ions must slip past one another. In doing so, like-charged ions momentarily end up adjacent — positive next to positive, or negative next to negative. This creates a massive electrostatic repulsion that effectively blocks dislocation motion. Without dislocation motion, there is no plastic deformation. When a crack begins in the material, the stress at its tip is enormous, but no plastic zone forms to redistribute the load or blunt the crack. The crack simply propagates straight through, producing the catastrophic brittle fracture characteristic of ceramics."
  explanation: "This is distinct from covalent ceramics like SiC and Si₃N₄, where immobility comes from the highly directional covalent bonds that resist the changes in bonding geometry required for slip. Either way — ionic electrostatic repulsion or covalent directionality — the result is the same: immobile dislocations, no ductility, brittle fracture."
```

## Explainer

Ceramics are built from ionic and covalent bonds — both of which you have studied as prerequisites. Recall that ionic bonding involves electrostatic attraction between oppositely charged ions, and covalent bonding involves shared electron pairs with directional character. In ceramics, these bond types are often mixed: alumina (Al₂O₃) is largely ionic, silicon carbide (SiC) is largely covalent, and silica (SiO₂) combines both. What both bond types share is that they are strong, stiff, and — critically — non-directional slip is impossible. This last point explains nearly every distinctive property of ceramics.

The crystal structure of a ceramic is governed by one geometric rule: each cation must be surrounded by enough anions to satisfy charge neutrality, and the ions must pack without interpenetrating. The **radius ratio** r_cation/r_anion predicts the **coordination number** — how many anions surround each cation. A small cation (radius ratio < 0.41) fits into tetrahedral holes (coordination 4); a larger one fits into octahedral holes (coordination 6); a very large one fits into cubic holes (coordination 8). NaCl has octahedral coordination (ratio ~0.56), ZnS has tetrahedral coordination (~0.40), and CsCl has cubic coordination (~0.93). From your crystal structure prerequisite, you know these packing arrangements — ceramics simply add the electrostatic constraint that opposite charges must neighbor each other.

The practical consequences of strong, directional bonds fall into two categories: desirable and dangerous. Desirable: ceramics have very high melting points (Al₂O₃ melts at 2072°C), high hardness (diamond hardness is a ceramic extreme), low electrical conductivity (no free electrons), chemical inertness, and excellent strength in compression. Dangerous: ceramics cannot undergo **plastic deformation**. In metals, dislocations — line defects — move easily through the crystal under stress, redistributing load and allowing the metal to absorb energy before fracture (ductility). In ceramics, moving a dislocation would force like-charged ions next to each other, requiring enormous energy. So dislocations are effectively immobile, and under tensile stress, cracks simply propagate without any plastic redistribution. The result is catastrophic brittle fracture at stresses that a metal would survive easily.

Engineering around ceramic brittleness takes several forms. **Transformation toughening** (as in zirconia-toughened alumina) exploits a stress-induced phase transformation that absorbs energy at crack tips. **Fiber reinforcement** (as in ceramic matrix composites) provides crack-bridging and pull-out mechanisms. **Compression loading** exploits the fact that ceramics are strong in compression — pre-stressing ceramic components like tempered glass puts the surface in compression so that service tensile loads must first overcome the compressive pre-stress before opening a crack. Understanding both the bond-level reason for brittleness and these engineering workarounds is essential for selecting ceramics in thermal, structural, and biomedical applications.
