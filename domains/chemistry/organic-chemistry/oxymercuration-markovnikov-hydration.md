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
stage: advanced
status: draft
---

# Oxymercuration: Markovnikov Hydration of Alkenes

## Core Idea
Oxymercuration uses Hg(OAc)₂ to add water to alkenes in a Markovnikov fashion, with subsequent NaBH₄ reduction converting the C-HgOAc intermediate to C-H. The reaction proceeds via a mercurinium ion intermediate that is attacked by water, followed by carbocation rearrangement if needed. This method avoids carbocation rearrangement better than simple acid-catalyzed hydration.

## Explainer

You already know that electrophilic addition to alkenes follows a general pattern: an electrophile attacks the electron-rich pi bond, forming a cationic intermediate, and then a nucleophile completes the addition. You also know from Markovnikov's rule that in unsymmetrical alkenes, the nucleophile ends up on the more substituted carbon. The challenge with simple acid-catalyzed hydration (adding H₃O⁺ to an alkene) is that it forms a true carbocation intermediate — and carbocations rearrange. If you have a substrate where the carbon skeleton could shift to form a more stable cation, you may get a product with a completely different connectivity than you intended. Oxymercuration solves this problem elegantly.

In the first step, **mercury(II) acetate** — Hg(OAc)₂ — acts as the electrophile. The mercury ion attacks the alkene's pi bond, but instead of forming an open carbocation, it forms a **mercurinium ion**: a three-membered ring where mercury bridges both carbons. This bridged intermediate is the key to the entire reaction's usefulness. Because the positive charge is delocalized across the mercury bridge rather than sitting on a single carbon, the intermediate never becomes a true carbocation. No rearrangement occurs, even on substrates that would rearrange instantly under acid-catalyzed conditions.

Water then attacks the mercurinium ion as a nucleophile. It preferentially attacks the **more substituted carbon** of the three-membered ring — this is the Markovnikov selectivity you expect. The more substituted carbon bears more of the positive character because it can better stabilize partial positive charge, making it the preferred site for nucleophilic attack. After deprotonation, you have an alcohol on the more substituted carbon and a mercury-containing group on the less substituted carbon.

The second step is **demercuration**: sodium borohydride (NaBH₄) replaces the C–HgOAc bond with a C–H bond. The mechanism of this reduction is complex (and likely involves radicals), but the practical result is clean: you get the Markovnikov alcohol product without rearrangement, without harsh acid conditions, and with excellent regioselectivity. This makes oxymercuration-demercuration the go-to method when you need Markovnikov hydration of an alkene and cannot tolerate the rearrangements that plague acid-catalyzed routes.
