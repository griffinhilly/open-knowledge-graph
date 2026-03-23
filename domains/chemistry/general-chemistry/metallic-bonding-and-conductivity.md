---
id: metallic-bonding-and-conductivity
title: Metallic Bonding and Properties of Metals
domain: chemistry
course: general-chemistry
prerequisites:
- id: bond-classification
  type: hard
builds-toward:
- crystal-structures-and-properties
tags:
- metallic bonding
- delocalized electrons
- conductivity
- metals
stage: formal-systems
status: draft
---

# Metallic Bonding and Properties of Metals

## Core Idea
Metallic bonding involves delocalized electrons moving freely throughout a lattice of metal cations. This electron sea model explains metallic properties: conductivity (mobile electrons), malleability (atoms can shift without breaking bonds), ductility, and luster. Metallic bonding strength varies with nuclear charge and electron count.

## Questions

```yaml
- question: "A metal wire conducts electricity without any chemical bonds breaking. Why is this possible when, for example, a covalent solid like diamond cannot conduct electricity under normal conditions?"
  type: multiple-choice
  options:
    - "Metal atoms are larger and therefore have more electrons available to carry charge"
    - "The delocalized electrons in a metal are already free to move through the lattice in response to an applied voltage, requiring no bond breaking"
    - "Metal atoms form temporary bonds that break and reform rapidly when a voltage is applied"
    - "The metallic lattice vibrates when a voltage is applied, pushing electrons forward"
  answer: 1
  explanation: "In metallic bonding, the valence electrons are already delocalized — they do not belong to individual atoms or specific bonds, but to the lattice as a whole. Applying a voltage simply gives these pre-existing free electrons a preferred direction of drift. No bonds need to break because no localized bonds exist to break. Diamond, by contrast, has all valence electrons tied up in directed covalent bonds; to conduct, those bonds would have to be broken, which requires a large energy input. This is why conductivity is an inherent property of metallic bonding, not a special feature of any particular metal."

- question: "Why can metals be hammered into thin sheets (malleability) without shattering, while ionic crystals like NaCl fracture under the same mechanical stress?"
  type: multiple-choice
  options:
    - "Metal atoms are ductile by nature, whereas ions are brittle — this is a property of the atoms themselves"
    - "In metals, shifting the cation lattice simply moves it through the electron sea, preserving bonding; in ionic crystals, shifting brings like charges into contact, creating repulsion that shatters the crystal"
    - "Metallic bonds are weaker than ionic bonds, so metals deform more easily under force"
    - "The electron sea absorbs the mechanical energy of hammering, converting it to heat rather than fracture"
  answer: 1
  explanation: "The key is the non-directional, non-specific nature of metallic bonding. The electron sea fills all space around the cations, so when one layer of cations slides relative to another, the delocalized electrons instantaneously rearrange to maintain the bonding environment. There is no 'correct' arrangement that must be preserved. In an ionic crystal, displacing one layer brings Na⁺ adjacent to Na⁺ and Cl⁻ adjacent to Cl⁻ — like charges repel violently and the crystal cleaves. The difference is not bond strength but bond geometry: metallic bonds are omnidirectional, ionic bonds are position-dependent."

- question: "Solid sodium chloride cannot conduct electricity because it lacks mobile charge carriers, even though it is made entirely of charged ions."
  type: true-false
  answer: true
  explanation: "In the solid state, Na⁺ and Cl⁻ ions are fixed in a rigid crystal lattice — they are charged, but they cannot move. Electrical conduction requires mobile charge carriers. Solid NaCl has none: the ions are locked in place by the crystal structure, and there are no delocalized electrons. When NaCl is dissolved in water or melted, the ions become mobile and the substance conducts. This contrasts with metals, where mobile electrons are present even in the solid state — hence metals conduct as solids while ionic solids do not."

- question: "Metals with more valence electrons and higher nuclear charge tend to have lower melting points because the larger electron sea creates more repulsion between cations, weakening the lattice."
  type: true-false
  answer: false
  explanation: "This reverses the actual trend. More valence electrons contribute more 'glue' to the electron sea, strengthening the metallic bond. Higher nuclear charge holds each cation more tightly within the lattice. Together, these factors raise melting points. Sodium (1 valence electron, low charge, large radius) melts at 98°C and can be cut with a knife. Tungsten (multiple valence electrons, high nuclear charge, small radius) has the highest melting point of any metal at 3,422°C. The electron sea creates attraction — cations are held by it — not repulsion."

- question: "Explain how the electron sea model of metallic bonding accounts for both electrical conductivity and malleability in a single unified picture."
  type: short-answer
  answer: "In the electron sea model, metal atoms release their valence electrons into a collective 'sea' that permeates the lattice of metal cations. Electrical conductivity follows directly: the electrons are already delocalized and mobile, so applying a voltage simply gives them a directed drift — no bonds need to break. Malleability follows from a different consequence of the same structure: because the electrons are not localized between specific pairs of atoms, the bonding has no preferred geometry. When mechanical stress shifts one layer of cations relative to another, the electron sea instantly rearranges to maintain the same non-specific bonding throughout the new configuration. There are no directional bonds to rupture, so the metal deforms rather than fractures."
  explanation: "Both properties arise from the same root cause — delocalization. Conductivity exploits the temporal mobility of electrons (they can flow in response to a field). Malleability exploits the spatial non-specificity of the bond (it survives geometric rearrangement). This is why the electron sea model, despite being a simplified picture, correctly predicts not just conductivity and malleability but also thermal conductivity (mobile electrons transfer kinetic energy) and luster (free electrons absorb and re-emit photons across a wide frequency range)."
```

## Explainer

From your study of bond classification, you know that ionic bonds involve electron transfer between atoms and covalent bonds involve electron sharing between specific pairs of atoms. **Metallic bonding** is the third major category, and it works by a fundamentally different mechanism: rather than electrons being transferred to or shared with one particular neighbor, the valence electrons of metal atoms become **delocalized** — they detach from individual atoms and spread out across the entire solid. The result is a regular lattice of positively charged metal cations immersed in a "sea" of mobile electrons that belongs collectively to the whole structure.

This **electron sea model** elegantly explains why metals behave so differently from ionic or covalent solids. **Electrical conductivity** is the most direct consequence: when you apply a voltage across a metal wire, the delocalized electrons flow through the lattice in response, carrying charge from one end to the other. No bonds need to break for this to happen — the electrons are already free to move. In an ionic solid like NaCl, by contrast, the electrons are locked onto specific ions, so the solid cannot conduct electricity (though the molten form can, once ions are free to move). **Thermal conductivity** works similarly: mobile electrons transfer kinetic energy rapidly through the metal, which is why a metal spoon in hot soup heats up much faster than a wooden one.

**Malleability** (the ability to be hammered into sheets) and **ductility** (the ability to be drawn into wires) follow from the non-directional nature of the metallic bond. In an ionic crystal, shifting one layer of ions relative to another brings like charges into contact, and the crystal shatters. In a metal, shifting the cation lattice simply moves it through the electron sea — the delocalized electrons rearrange instantly to accommodate the new configuration, and the bonding remains intact. This is why metals can be reshaped without breaking, and why they are the materials of choice for structural applications requiring both strength and flexibility. **Luster** — the characteristic shine of metals — occurs because the free electrons absorb and re-emit photons of light across a wide range of wavelengths, giving polished metal surfaces their reflective quality.

The strength of metallic bonding varies across the periodic table and explains trends in melting point, hardness, and other physical properties. Metals with more valence electrons contributing to the sea and higher nuclear charge holding the lattice together tend to form stronger metallic bonds. Sodium, with one valence electron and a large atomic radius, is soft enough to cut with a knife and melts at just 98°C. Tungsten, with multiple valence electrons and a smaller, more tightly held cation core, has the highest melting point of any metal at 3,422°C. These trends follow logically: more electrons in the sea means more "glue" holding the lattice together, and higher effective nuclear charge means each cation grips the electron sea more tightly.
