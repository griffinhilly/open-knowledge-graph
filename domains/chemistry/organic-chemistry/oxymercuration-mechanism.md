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
- id: oxymercuration-markovnikov-hydration
  type: soft
builds-toward:
- alcohol-oxidation-to-carbonyls
tags:
- addition
- hydration
- mercury
- mechanism
- alcohol-synthesis
stage: formal-systems
status: validated
---
# Oxymercuration: Hg(OAc)₂-Mediated Hydration

## Core Idea
Oxymercuration provides Markovnikov hydration of alkenes via a mercurinium ion intermediate that is opened by nucleophilic attack from the alcohol solvent. Hg(OAc)₂ generates a three-membered mercurinium ion (bridged intermediate), which is more resistant to carbocation rearrangement than a carbocation. Reduction with NaBH₄ replaces mercury with hydrogen.

## How It's Best Learned
Draw the mercurinium ion formation, nucleophilic opening, and NaBH₄ reduction, showing the anti addition geometry and Markovnikov regioselectivity. Compare carbocation stability to mercurinium ion stability.

## Common Misconceptions
- Assuming the mercurinium ion completely prevents rearrangement; some rearrangement is still possible if a more stable carbocation forms transiently.
- Forgetting the final NaBH₄ step or misunderstanding its role in replacing Hg with H.

## Questions

```yaml
- question: "A chemist needs to add water across an alkene that has a tertiary carbon adjacent to the double bond — a substrate prone to carbocation rearrangement. Which method should they choose, and why?"
  type: multiple-choice
  options:
    - "Acid-catalyzed hydration, because it forms the most stable carbocation intermediate"
    - "Oxymercuration-demercuration, because the mercurinium ion intermediate prevents skeletal rearrangements"
    - "Oxymercuration-demercuration, because it produces anti-Markovnikov products that avoid the rearrangement site"
    - "Acid-catalyzed hydration, because strong acid suppresses rearrangement pathways"
  answer: 1
  explanation: "Oxymercuration is preferred precisely because it avoids a free carbocation. The mercury bridges both carbons of the double bond as a mercurinium ion, preventing the hydride and methyl shifts that plagued the acid-catalyzed route. It still delivers Markovnikov selectivity — not anti-Markovnikov — because the more substituted carbon bears more positive character within the bridged ring."

- question: "In oxymercuration, the nucleophilic attack of water on the mercurinium ion gives anti addition geometry. What structural feature of the mercurinium ion causes this?"
  type: multiple-choice
  options:
    - "The positive charge on mercury repels incoming nucleophiles to the opposite face"
    - "Mercury sits on one face of the ring, so the nucleophile must attack the opposite face"
    - "The carbonyl character of mercury blocks syn attack by steric bulk"
    - "Anti addition is enforced by the NaBH₄ reduction step, not the mercurinium ring opening"
  answer: 1
  explanation: "The mercurinium ion is a three-membered ring with mercury bonded to both carbons on one face of what was the double bond. This bridge physically blocks approach from that face, so the nucleophile (water or alcohol) must attack from the opposite face — yielding anti addition. The NaBH₄ step that follows is not stereospecific and does not enforce the anti geometry."

- question: "Oxymercuration produces Markovnikov products because a free carbocation forms on the more substituted carbon, just as in acid-catalyzed hydration."
  type: true-false
  answer: false
  explanation: "This is the central misconception to avoid. Oxymercuration does NOT form a free carbocation — that is the whole point of the reaction. Instead, mercury bridges both carbons as a mercurinium ion. Markovnikov selectivity is preserved because the more substituted carbon bears more partial positive character within the bridged ring, directing nucleophilic attack there. The advantage over acid-catalyzed hydration is precisely that the skeleton stays intact."

- question: "The NaBH₄ demercuration step in oxymercuration-demercuration is stereospecific, proceeding with inversion of configuration at the carbon that bore the mercury."
  type: true-false
  answer: false
  explanation: "The demercuration step with NaBH₄ is NOT stereospecific. The C–Hg bond is replaced by C–H via a radical-like mechanism that proceeds without strict retention or inversion. The overall stereochemical outcome of the sequence is governed by the anti addition geometry established in the mercurinium ring-opening step, not by the demercuration."

- question: "Why does oxymercuration-demercuration reduce the likelihood of carbocation rearrangements compared to acid-catalyzed hydration, and what intermediate is responsible for this advantage?"
  type: short-answer
  answer: "Acid-catalyzed hydration generates a free carbocation, which can undergo hydride or methyl shifts to produce rearranged products. Oxymercuration avoids this by forming a mercurinium ion — a three-membered ring in which mercury bridges across both carbons of the former double bond. Because the carbon skeleton is held rigidly in the bridged ring, the skeletal rearrangements that require a fully open carbocation are largely prevented."
  explanation: "The key insight is that the mercurinium ion distributes the positive charge without fully exposing either carbon as a naked carbenium. Some rearrangement is still theoretically possible if a highly stabilized carbocation can form transiently, but the bridged structure substantially suppresses this pathway. Whenever a substrate's structure would lead to rearrangement under acidic conditions, oxymercuration is the standard synthetic solution."
```

## Explainer

You already know that electrophilic addition to alkenes follows Markovnikov's rule — the electrophile adds to the less substituted carbon, placing the positive charge (or partial positive character) on the more substituted carbon where it is more stable. Acid-catalyzed hydration accomplishes this, but it has a serious drawback: the free carbocation intermediate can rearrange via hydride or methyl shifts, giving you unexpected products. Oxymercuration solves this problem by never forming a free carbocation in the first place.

The reaction begins when mercury(II) acetate, Hg(OAc)₂, acts as the electrophile. The mercury ion attacks the alkene's pi bond, but instead of landing on one carbon and leaving the other as a naked carbocation, it bridges across both carbons to form a **mercurinium ion** — a three-membered ring with mercury bonded to both carbons simultaneously. Think of it as mercury putting a "cap" over the double bond. This bridged structure distributes the positive charge and prevents the skeletal rearrangements that plague simple carbocation intermediates. The more substituted carbon still bears more of the positive character (Markovnikov selectivity is preserved), but the bridging keeps everything locked in place.

Water (or the alcohol solvent) then attacks this mercurinium ion as a nucleophile. Because the mercury bridge sits on one face of the ring, the nucleophile must attack from the opposite face — this gives you **anti addition** geometry, meaning the mercury and the incoming oxygen end up on opposite sides of what was the double bond. The nucleophile preferentially attacks the more substituted carbon because that carbon bears more positive character, delivering the Markovnikov product. After deprotonation, you have an organomercury alcohol intermediate.

The final step is **demercuration**: sodium borohydride (NaBH₄) replaces the mercury with hydrogen. This reductive step is not stereospecific — the C–Hg bond is replaced by C–H without strict retention or inversion — so the overall stereochemistry of the product reflects the anti addition of the first two steps but loses some stereocontrol at the mercury-bearing carbon. The net result of the full sequence is Markovnikov hydration of an alkene to an alcohol, with no rearrangement. Whenever you need a Markovnikov alcohol from an alkene and the substrate is prone to rearrangement, oxymercuration-demercuration is the method of choice.
