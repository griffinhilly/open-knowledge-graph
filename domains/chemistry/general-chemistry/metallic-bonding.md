---
id: metallic-bonding
title: Metallic Bonding
domain: chemistry
course: general-chemistry
prerequisites:
- id: periodic-trends
  type: hard
- id: ionic-bonding
  type: soft
builds-toward:
- electrochemistry-basics
tags:
- metals
- electron-sea
- conductivity
- malleability
- ductility
- alloys
stage: advanced
status: validated
---

# Metallic Bonding

## Core Idea
In metallic bonding, metal atoms release their valence electrons into a shared 'sea' of delocalized electrons that flows freely throughout the solid structure. The resulting lattice of positive metal cations is held together by electrostatic attraction to this mobile electron sea. This model explains characteristic metallic properties: electrical and thermal conductivity (mobile electrons carry charge and energy), malleability and ductility (cation layers can slide without breaking the delocalized bonding), and metallic luster (free electrons interact with and reflect visible light).

## How It's Best Learned
Compare metallic bonding to ionic and covalent bonding by contrasting their properties — conductivity, hardness, melting point. Use the trend in metallic properties across the d-block to see how electron count affects bond strength.

## Common Misconceptions
- The electron sea model is a useful simplification; band theory provides a more accurate quantum mechanical description that explains semiconductors and insulators as well.
- Not all shiny solids are metals — some nonmetals like iodine can appear metallic in appearance but lack the delocalized bonding that gives true metals their properties.

## Questions

```yaml
- question: "When you hammer a metal, it flattens into a sheet rather than shattering. When you apply similar force to an ionic crystal like NaCl, it fractures. What explains this difference?"
  type: multiple-choice
  options:
    - "Metals are softer because their bonds are weaker overall"
    - "In ionic crystals, bonds are directional — shifting a layer brings like charges face-to-face, causing repulsion and fracture; in metals, the non-directional electron sea maintains bonding regardless of cation position"
    - "Metal atoms are larger and absorb impact energy better than small ionic lattice atoms"
    - "Metals contain more free space in their lattice, allowing compression without fracture"
  answer: 1
  explanation: "The key is bond directionality. In ionic crystals, each ion is attracted to specific oppositely charged neighbors. Shift a layer and like charges suddenly face each other — electrostatic repulsion shatters the crystal. In metallic bonding, the delocalized electron sea is non-directional: it glues cations together regardless of their positions. When cation layers slide, the electron sea simply redistributes to maintain bonding in the new arrangement. This is why metals are malleable and ductile while ionic solids are brittle."

- question: "Transition metals like tungsten (W) typically have much higher melting points than alkali metals like sodium (Na). Which explanation is most consistent with the electron sea model?"
  type: multiple-choice
  options:
    - "Tungsten has stronger covalent bonds between adjacent metal atoms that must be broken to melt"
    - "Tungsten contributes more valence electrons to a denser electron sea and has smaller, more closely packed cations, creating stronger electrostatic attraction"
    - "Sodium has a lower melting point because it is in a lower period of the periodic table"
    - "Tungsten's larger atomic mass requires more energy to set atoms into random motion"
  answer: 1
  explanation: "Metallic bond strength depends on the electron sea density and cation charge-to-size ratio. Tungsten (a d-block metal) contributes many valence electrons per atom to a dense electron sea, while sodium contributes only one. More electrons per cation and smaller atomic radii mean stronger electrostatic attraction between the cation lattice and the electron sea, requiring more energy to disrupt — hence a much higher melting point. Atomic mass alone doesn't determine melting point; gold is heavy but less refractory than tungsten."

- question: "Electrical conductivity in metals arises from the mobility of delocalized electrons that are not bound to specific atoms and respond freely to an applied electric field."
  type: true-false
  answer: true
  explanation: "This is the central mechanistic explanation. Because electrons in a metal are already delocalized — not associated with any particular atom — they drift toward the positive terminal when a voltage is applied without needing to break or reform bonds. This is fundamentally different from ionic conduction, which requires ions to physically migrate through a solution or molten state. The metallic electron sea is always mobile, which is why metals conduct electricity in the solid state."

- question: "Metallic bonding involves directional bonds between specific pairs of adjacent metal atoms, which is why metals can be reshaped without fracturing — each bond can reattach to a neighboring atom."
  type: true-false
  answer: false
  explanation: "Metallic bonding is explicitly *non-directional* — the electron sea belongs to the entire lattice, not to specific atom-atom pairs. There are no localized bonds to 'break and reform.' When cation layers slide during hammering, the electron sea simply redistributes to maintain cohesion throughout the new configuration without any bond-breaking event. This non-directionality is precisely what makes metals malleable. Directional bonding (as in covalent crystals like diamond) actually causes brittleness, because displacement breaks specific bonds that cannot reform in the new geometry."

- question: "Explain how the electron sea model accounts for both the malleability of metals and their electrical conductivity using the same underlying property."
  type: short-answer
  answer: "Both properties arise from the same feature: valence electrons are delocalized and not bound to specific atoms. For malleability: when cation layers slide under mechanical stress, the electron sea — being non-directional and unlocalized — redistributes to maintain bonding in the new arrangement, so no bonds break and the material deforms rather than fractures. For electrical conductivity: those same delocalized electrons are already free to move throughout the lattice, so applying a voltage simply causes them to drift toward the positive terminal without needing to break any bonds."
  explanation: "The unifying insight is that delocalization = both mobility and non-directionality. Mobility gives conductivity (electrons flow); non-directionality gives malleability (cations can slide without bond rupture). If electrons were localized in specific bonds (as in covalent solids), both properties would be lost: the material would be brittle (bonds break on displacement) and non-conducting (electrons can't flow freely). The electron sea model explains a whole cluster of metallic properties from one structural feature."
```

## Explainer

You already know from periodic trends that metals sit on the left and center of the periodic table and tend to have low ionization energies — they give up valence electrons readily. From ionic bonding, you learned how electrons can transfer entirely from one atom to another. **Metallic bonding** represents a third possibility: instead of transferring electrons to a specific partner, metal atoms collectively release their valence electrons into a shared pool that belongs to no individual atom. The result is a lattice of positively charged metal cations immersed in a "sea" of delocalized electrons that flows freely throughout the entire solid.

This **electron sea model** explains why metals behave so differently from ionic or covalent solids. In an ionic crystal like NaCl, each ion is locked in place by directional electrostatic attraction to its specific neighbors — if you try to shift one layer, like charges suddenly face each other and the crystal shatters. In a metal, the bonding is non-directional: the electron sea glues the cations together regardless of their exact positions. When you hammer a metal, the cation layers slide past one another, but the delocalized electrons simply redistribute to maintain bonding in the new configuration. This is why metals are **malleable** (can be hammered into sheets) and **ductile** (can be drawn into wires), while ionic solids are brittle.

**Electrical conductivity** follows directly from electron delocalization. When a voltage is applied across a metal wire, the free electrons drift toward the positive terminal — they are already mobile and require no energy to break free from individual bonds. This is fundamentally different from ionic conduction, which requires ions to physically migrate through a liquid or molten salt. **Thermal conductivity** works similarly: the mobile electrons efficiently transfer kinetic energy from hotter regions to cooler ones, supplementing the slower vibration-based heat transfer through the cation lattice. **Metallic luster** arises because free electrons can absorb and re-emit photons across a broad range of visible wavelengths, giving metals their characteristic reflective appearance.

The strength of metallic bonding varies systematically across the periodic table. Metals with more valence electrons and smaller atomic radii form stronger metallic bonds — the electron sea is denser and the cations are closer together. This is why transition metals in the middle of the d-block (like tungsten and chromium) generally have higher melting points and greater hardness than alkali metals like sodium, which contribute only one electron each to a sea spread across large, widely spaced cations. Alloying — mixing two or more metals — works because the electron sea accommodates different-sized cations, and the size mismatch can actually strengthen the material by disrupting the regular sliding of cation layers.
