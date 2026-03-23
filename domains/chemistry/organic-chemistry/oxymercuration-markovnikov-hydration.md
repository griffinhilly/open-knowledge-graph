---
id: oxymercuration-markovnikov-hydration
title: 'Oxymercuration: Markovnikov Hydration of Alkenes'
domain: chemistry
course: organic-chemistry
prerequisites:
- id: electrophilic-addition-to-alkenes
  type: hard
- id: markovnikov-rule-in-addition-reactions
  type: soft
builds-toward:
- catalytic-hydrogenation-lindlar-catalyst
tags:
- oxymercuration
- hydration
- markovnikov
- mercurinium-ion
stage: formal-systems
status: draft
---

# Oxymercuration: Markovnikov Hydration of Alkenes

## Core Idea
Oxymercuration uses Hg(OAc)₂ to add water to alkenes in a Markovnikov fashion, with subsequent NaBH₄ reduction converting the C-HgOAc intermediate to C-H. The reaction proceeds via a mercurinium ion intermediate that is attacked by water, followed by carbocation rearrangement if needed. This method avoids carbocation rearrangement better than simple acid-catalyzed hydration.

## Questions

```yaml
- question: "You need to add water across a double bond in a substrate where a secondary carbocation intermediate would rearrange to a tertiary one, giving an unwanted product. Which method best solves this problem while still delivering Markovnikov regioselectivity?"
  type: multiple-choice
  options:
    - "Acid-catalyzed hydration (H₂SO₄/H₂O), because the carbocation forms too quickly to rearrange"
    - "Oxymercuration-demercuration, because the mercurinium ion prevents rearrangement by avoiding a true carbocation"
    - "Oxymercuration-demercuration, but only if the substrate has no substituents near the double bond"
    - "Hydroboration-oxidation, because it also gives Markovnikov products and avoids rearrangement"
  answer: 1
  explanation: "Oxymercuration proceeds through a mercurinium ion — a three-membered ring where mercury bridges both carbons and distributes the positive charge, so no discrete carbocation ever forms. Because there is no carbenyl center to migrate to, rearrangements cannot occur. Acid-catalyzed hydration (option A) forms a true carbocation that rearranges readily. Hydroboration-oxidation (option D) avoids rearrangement but gives anti-Markovnikov regiochemistry, placing OH on the less substituted carbon."

- question: "In the oxymercuration step, water attacks the more substituted carbon of the mercurinium ion. What is the best explanation for this regioselectivity?"
  type: multiple-choice
  options:
    - "The more substituted carbon is less sterically hindered, making it easier for water to approach"
    - "The more substituted carbon carries more of the partial positive charge in the mercurinium ion, making it more electrophilic"
    - "Mercury migrates to the less substituted carbon first, leaving the more substituted carbon open for attack"
    - "Water is a hard nucleophile and always attacks the carbon with the lowest electron density regardless of substitution"
  answer: 1
  explanation: "The mercurinium ion is not a symmetric intermediate. The more substituted carbon can better stabilize partial positive charge (via hyperconjugation and inductive donation from alkyl groups), so it bears more of the electrophilic character of the bridged ring. Water as a nucleophile preferentially attacks the most electrophilic carbon — the more substituted one — giving the Markovnikov alcohol. Option A is wrong: more substituted carbons are typically *more* hindered, yet water still attacks there because electronic factors dominate."

- question: "Oxymercuration-demercuration gives the same Markovnikov regiochemical outcome as acid-catalyzed hydration but proceeds through a fundamentally different intermediate."
  type: true-false
  answer: true
  explanation: "Both reactions deliver the OH group to the more substituted carbon (Markovnikov selectivity), so the regiochemical outcome is the same. However, acid-catalyzed hydration forms a discrete, planar carbocation that can rearrange, whereas oxymercuration forms a cyclic mercurinium ion bridged by mercury that distributes charge and prevents rearrangement. The product connectivity matches, but the mechanism is distinct — and for substrates prone to rearrangement, only oxymercuration gives the desired product cleanly."

- question: "The mercurinium ion intermediate in oxymercuration is equivalent to a classical carbocation because both carry a formal positive charge on carbon."
  type: true-false
  answer: false
  explanation: "This is a critical distinction. In a classical carbocation, a single sp²-hybridized carbon bears the full positive charge and is highly susceptible to rearrangement (1,2-hydride or alkyl shifts). In the mercurinium ion, the positive charge is delocalized across a three-membered ring involving mercury — neither carbon carries a full positive charge. Because there is no carbenyl center, the driving force for rearrangement is absent. The bridging by mercury is precisely what makes oxymercuration synthetically useful for substrates that would rearrange under carbocation conditions."

- question: "Explain why the mercurinium ion intermediate prevents carbocation rearrangement, and identify the step in the overall oxymercuration-demercuration sequence where regioselectivity is established."
  type: short-answer
  answer: "Carbocation rearrangements occur because a 1,2-hydride or alkyl shift can convert a less stable carbocation into a more stable one — the driving force is stabilization of the cationic center. In a mercurinium ion, the positive charge is spread across the bridged three-membered ring (C–Hg–C) rather than concentrated on a single carbon, so there is no empty p-orbital to receive a migrating group. Without a true carbenyl center, the electronic driving force for rearrangement is absent. Regioselectivity is established in the second step when water (the nucleophile) attacks the mercurinium ion: it preferentially attacks the more substituted carbon because that carbon bears more of the partial positive character."
  explanation: "The demercuration step (NaBH₄ reduction of C–HgOAc to C–H) occurs after regioselectivity is already set. It replaces the mercury group with hydrogen but does not change which carbon bears the oxygen. Understanding that selectivity is established at the nucleophilic attack step — not during the demercuration — is key to predicting products."
```

## Explainer

You already know that electrophilic addition to alkenes follows a general pattern: an electrophile attacks the electron-rich pi bond, forming a cationic intermediate, and then a nucleophile completes the addition. You also know from Markovnikov's rule that in unsymmetrical alkenes, the nucleophile ends up on the more substituted carbon. The challenge with simple acid-catalyzed hydration (adding H₃O⁺ to an alkene) is that it forms a true carbocation intermediate — and carbocations rearrange. If you have a substrate where the carbon skeleton could shift to form a more stable cation, you may get a product with a completely different connectivity than you intended. Oxymercuration solves this problem elegantly.

In the first step, **mercury(II) acetate** — Hg(OAc)₂ — acts as the electrophile. The mercury ion attacks the alkene's pi bond, but instead of forming an open carbocation, it forms a **mercurinium ion**: a three-membered ring where mercury bridges both carbons. This bridged intermediate is the key to the entire reaction's usefulness. Because the positive charge is delocalized across the mercury bridge rather than sitting on a single carbon, the intermediate never becomes a true carbocation. No rearrangement occurs, even on substrates that would rearrange instantly under acid-catalyzed conditions.

Water then attacks the mercurinium ion as a nucleophile. It preferentially attacks the **more substituted carbon** of the three-membered ring — this is the Markovnikov selectivity you expect. The more substituted carbon bears more of the positive character because it can better stabilize partial positive charge, making it the preferred site for nucleophilic attack. After deprotonation, you have an alcohol on the more substituted carbon and a mercury-containing group on the less substituted carbon.

The second step is **demercuration**: sodium borohydride (NaBH₄) replaces the C–HgOAc bond with a C–H bond. The mechanism of this reduction is complex (and likely involves radicals), but the practical result is clean: you get the Markovnikov alcohol product without rearrangement, without harsh acid conditions, and with excellent regioselectivity. This makes oxymercuration-demercuration the go-to method when you need Markovnikov hydration of an alkene and cannot tolerate the rearrangements that plague acid-catalyzed routes.
