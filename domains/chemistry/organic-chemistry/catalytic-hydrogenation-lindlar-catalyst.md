---
id: catalytic-hydrogenation-lindlar-catalyst
title: Catalytic Hydrogenation and Lindlar Catalyst
domain: chemistry
course: organic-chemistry
prerequisites:
- id: alkene-structure-and-nomenclature
  type: hard
- id: alkyne-structure-and-nomenclature
  type: hard
- id: electrophilic-addition-to-alkenes
  type: soft
builds-toward:
- structure-elucidation-using-ir-nmr-and-ms
tags:
- hydrogenation
- lindlar-catalyst
- reduction
- syn-addition
- stereoselectivity
stage: advanced
status: draft
---

# Catalytic Hydrogenation and Lindlar Catalyst

## Core Idea
Catalytic hydrogenation adds H₂ across C=C and C≡C bonds via heterogeneous catalysts (Pt, Pd, Ni). Standard catalysts reduce alkynes to alkanes; the Lindlar catalyst (Pd/CaCO₃ with Pb and quinoline) is deactivated to give syn addition to alkynes, yielding cis-alkenes. Stereoselectivity and regioselectivity depend on the catalyst and substrate geometry.

## Questions

```yaml
- question: "A chemist treats hex-3-yne (CH₃CH₂C≡CCH₂CH₃) with Lindlar catalyst and H₂. What is the major product?"
  type: multiple-choice
  options:
    - "Hexane (fully saturated), because H₂ reduces all pi bonds"
    - "cis-hex-3-ene, because Lindlar catalyst is poisoned to stop at the alkene stage and delivers H₂ from one face"
    - "trans-hex-3-ene, because the bulky catalyst surface forces anti addition"
    - "A mixture of cis- and trans-hex-3-ene in roughly equal amounts"
  answer: 1
  explanation: "Lindlar catalyst (Pd/CaCO₃ poisoned with lead acetate and quinoline) is selectively deactivated so it can reduce a triple bond to a double bond but cannot reduce the resulting alkene further. Because H₂ is delivered from the catalyst surface via syn addition — both hydrogen atoms arrive from the same face — an internal alkyne gives the cis-alkene. Options A and C are wrong for different reasons: A misses the Lindlar selectivity; C confuses syn addition (cis product) with the anti addition mechanism of dissolving-metal reduction, which gives the trans-alkene."

- question: "Why does the Lindlar catalyst stop reduction at the alkene stage rather than reducing the alkene to an alkane?"
  type: multiple-choice
  options:
    - "Alkenes are thermodynamically more stable than alkynes, so the reaction stops at the energy minimum"
    - "The catalyst surface is deliberately poisoned to reduce its activity so that it can reduce a triple bond but not a double bond"
    - "Alkynes adsorb more strongly to the metal surface, blocking alkene adsorption until all alkyne is consumed"
    - "The reaction runs out of H₂ before the alkene can be reduced"
  answer: 1
  explanation: "The Lindlar catalyst is partially deactivated ('poisoned') by lead acetate and quinoline, which adsorb on the palladium surface and reduce its hydrogenation activity. With a standard Pd or Pt catalyst, the intermediate alkene is actually more reactive than the starting alkyne and gets reduced as fast as it forms — giving the alkane. The poisoned Lindlar surface has just enough activity to overcome the alkyne's higher activation barrier but not enough to proceed through the alkene stage. This chemoselectivity is intentional and tunable, not a consequence of thermodynamics."

- question: "Catalytic hydrogenation is a syn addition: both hydrogen atoms are delivered to the same face of the double or triple bond."
  type: true-false
  answer: true
  explanation: "The mechanism requires both the substrate and H₂ to adsorb onto the metal catalyst surface. H₂ dissociates into individual H atoms bound to the metal, and the alkene or alkyne also binds through its pi system. The two hydrogen atoms then transfer from the catalyst surface to the same face of the pi bond — neither H atom diffuses around to the opposite face before bonding. This syn delivery is why internal alkynes give cis-alkenes with Lindlar catalyst: both new C–H bonds form on the same side, preserving the geometrical relationship."

- question: "The Lindlar catalyst produces trans-alkenes from internal alkynes because the bulky lead and quinoline groups sterically force the two hydrogen atoms to add to opposite faces of the triple bond."
  type: true-false
  answer: false
  explanation: "The Lindlar catalyst gives cis-alkenes (syn addition), not trans-alkenes. The lead and quinoline are not bulky directing groups — they are catalyst poisons that reduce overall hydrogenation activity. The syn addition mechanism (both H atoms from the catalyst surface to the same face) is an inherent feature of all heterogeneous catalytic hydrogenation, Lindlar or otherwise. To obtain a trans-alkene from an alkyne, you need a fundamentally different mechanism: dissolving-metal reduction (Na in liquid NH₃), which proceeds through radical anion intermediates with anti addition."

- question: "Why must a synthetic chemist choose between Lindlar catalyst and dissolving-metal reduction (Na/NH₃) when converting an internal alkyne to a specific alkene isomer?"
  type: short-answer
  answer: "Lindlar catalyst and dissolving-metal reduction give opposite geometric isomers from the same alkyne starting material. Lindlar gives the cis-alkene via syn addition (both H atoms delivered from the catalyst surface to the same face). Dissolving-metal reduction (Na/NH₃) gives the trans-alkene via an anti-addition mechanism involving vinyl radical and carbanion intermediates that preferentially adopt a trans geometry before the second protonation. Since these two products are non-interconvertible without breaking C–C bonds, choosing the wrong reagent gives an isomer that cannot easily be corrected."
  explanation: "This choice illustrates a broader principle in synthesis: the same functional group (a triple bond) can be transformed into different products by selecting reagents with different mechanisms. Because geometric isomers have distinct physical, chemical, and biological properties, producing the correct isomer can be the difference between a useful molecule and a useless one. The alkyne is thus a versatile synthetic hub: reduce with Lindlar for cis, reduce with Na/NH₃ for trans, or use a standard catalyst with excess H₂ for the fully saturated alkane."
```

## Explainer

From your study of alkene and alkyne structure, you know that pi bonds represent regions of high electron density above and below the molecular plane. **Catalytic hydrogenation** is the process of breaking these pi bonds by adding hydrogen (H₂) across them, converting unsaturated compounds into more saturated ones. The reaction requires a **heterogeneous catalyst** — a solid metal surface (typically platinum, palladium, or nickel) over which the reaction takes place. Neither the alkene nor H₂ will react on their own at reasonable temperatures; the metal surface is essential because it adsorbs both the hydrogen gas and the substrate, weakening the H–H bond and bringing the reactants into close proximity.

The mechanism works like this: H₂ molecules land on the metal surface and dissociate into individual hydrogen atoms bound to the metal. The alkene or alkyne also adsorbs onto the surface through its pi electrons. The two hydrogen atoms then transfer from the metal to the same face of the double or triple bond — both hydrogens are delivered from the catalyst surface side. This is why catalytic hydrogenation is a **syn addition**: both new C–H bonds form on the same face of the molecule. For a simple alkene, this means the two hydrogens end up cis to each other, which has important stereochemical consequences when the substrate is part of a ring or has substituents that create defined faces.

The **Lindlar catalyst** solves an important problem. With a standard palladium or platinum catalyst, an alkyne is reduced all the way to the alkane — the intermediate alkene is more reactive toward further hydrogenation than the starting alkyne, so it gets reduced as fast as it forms. The Lindlar catalyst consists of palladium deposited on calcium carbonate, then treated with **lead acetate** and **quinoline** to partially deactivate (or "poison") the catalyst surface. This poisoning reduces the catalyst's activity just enough that it can still reduce a triple bond to a double bond but cannot reduce the resulting double bond further. The product is a **cis-alkene** with defined stereochemistry, because the syn addition mechanism delivers both hydrogens to the same face of the former triple bond.

This selectivity is synthetically powerful. If you need a cis-alkene, you start from an alkyne and use Lindlar catalyst. If you need a trans-alkene from the same alkyne, you use dissolving-metal reduction (Na/NH₃) instead, which proceeds by a different mechanism. And if you want the fully saturated alkane, you use a standard Pd or Pt catalyst with excess H₂. Having all three options from a single alkyne starting material illustrates why chemists value alkynes as versatile synthetic intermediates — and why understanding catalyst choice is as important as understanding the reaction itself.
