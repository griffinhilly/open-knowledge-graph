---
id: oxymercuration-mechanism
title: 'Oxymercuration: Hg(OAc)₂-Mediated Hydration'
domain: chemistry
course: organic-chemistry
prerequisites:
- id: electrophilic-addition-to-alkenes
  type: hard
- id: markovnikov-rule-regioselectivity
  type: hard
builds-toward:
- alcohol-oxidation-to-carbonyls
tags:
- addition
- hydration
- mercury
- mechanism
- alcohol-synthesis
stage: advanced
status: draft
---

# Oxymercuration: Hg(OAc)₂-Mediated Hydration

## Core Idea
Oxymercuration provides Markovnikov hydration of alkenes via a mercurinium ion intermediate that is opened by nucleophilic attack from the alcohol solvent. Hg(OAc)₂ generates a three-membered mercurinium ion (bridged intermediate), which is more resistant to carbocation rearrangement than a carbocation. Reduction with NaBH₄ replaces mercury with hydrogen.

## How It's Best Learned
Draw the mercurinium ion formation, nucleophilic opening, and NaBH₄ reduction, showing the anti addition geometry and Markovnikov regioselectivity. Compare carbocation stability to mercurinium ion stability.

## Common Misconceptions
- Assuming the mercurinium ion completely prevents rearrangement; some rearrangement is still possible if a more stable carbocation forms transiently.
- Forgetting the final NaBH₄ step or misunderstanding its role in replacing Hg with H.

## Explainer

You already know that electrophilic addition to alkenes follows Markovnikov's rule — the electrophile adds to the less substituted carbon, placing the positive charge (or partial positive character) on the more substituted carbon where it is more stable. Acid-catalyzed hydration accomplishes this, but it has a serious drawback: the free carbocation intermediate can rearrange via hydride or methyl shifts, giving you unexpected products. Oxymercuration solves this problem by never forming a free carbocation in the first place.

The reaction begins when mercury(II) acetate, Hg(OAc)₂, acts as the electrophile. The mercury ion attacks the alkene's pi bond, but instead of landing on one carbon and leaving the other as a naked carbocation, it bridges across both carbons to form a **mercurinium ion** — a three-membered ring with mercury bonded to both carbons simultaneously. Think of it as mercury putting a "cap" over the double bond. This bridged structure distributes the positive charge and prevents the skeletal rearrangements that plague simple carbocation intermediates. The more substituted carbon still bears more of the positive character (Markovnikov selectivity is preserved), but the bridging keeps everything locked in place.

Water (or the alcohol solvent) then attacks this mercurinium ion as a nucleophile. Because the mercury bridge sits on one face of the ring, the nucleophile must attack from the opposite face — this gives you **anti addition** geometry, meaning the mercury and the incoming oxygen end up on opposite sides of what was the double bond. The nucleophile preferentially attacks the more substituted carbon because that carbon bears more positive character, delivering the Markovnikov product. After deprotonation, you have an organomercury alcohol intermediate.

The final step is **demercuration**: sodium borohydride (NaBH₄) replaces the mercury with hydrogen. This reductive step is not stereospecific — the C–Hg bond is replaced by C–H without strict retention or inversion — so the overall stereochemistry of the product reflects the anti addition of the first two steps but loses some stereocontrol at the mercury-bearing carbon. The net result of the full sequence is Markovnikov hydration of an alkene to an alcohol, with no rearrangement. Whenever you need a Markovnikov alcohol from an alkene and the substrate is prone to rearrangement, oxymercuration-demercuration is the method of choice.
