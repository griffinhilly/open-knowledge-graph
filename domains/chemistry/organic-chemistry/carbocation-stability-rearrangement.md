---
id: carbocation-stability-rearrangement
title: Carbocation Stability and Rearrangements
domain: chemistry
course: organic-chemistry
prerequisites:
- id: sn1-reaction
  type: hard
- id: reaction-mechanisms-overview
  type: soft
builds-toward:
- hyperconjugation
- resonance-in-organic-intermediates
tags:
- carbocation
- stability
- hydride shift
- methyl shift
- ring expansion
- rearrangement
- tertiary
stage: advanced
status: draft
---
# Carbocation Stability and Rearrangements

## Core Idea
Carbocations are stabilized by electron donation from adjacent groups, following the order tertiary > secondary > primary > methyl. When a reaction generates a less stable carbocation, it will spontaneously rearrange to a more stable one through 1,2-hydride shifts (a hydrogen migrates with its bonding electrons) or 1,2-methyl shifts (an alkyl group migrates). Ring expansions — where a four-membered ring opens to a five, or five to six — are driven by the same thermodynamic preference for reduced ring strain and increased carbocation stability. These rearrangements explain why SN1 and E1 products often have different carbon skeletons than the starting material.

## How It's Best Learned
Draw the initial carbocation, identify whether a more stable carbocation is one shift away, then draw the rearranged intermediate and predict the final product. Practice with neopentyl and norbornyl systems where rearrangement is especially prominent. Always ask: "Is there a neighboring H or CH3 whose migration creates a more substituted cation?"

## Common Misconceptions
- Rearrangements do not involve free radicals or full bond-breaking — the migrating group moves with its bonding pair in a concerted 1,2-shift.
- Not every carbocation rearranges; a secondary carbocation adjacent to another secondary position has no driving force to shift.
- Ring expansion is not a separate reaction type — it is the same 1,2-shift mechanism applied to a ring carbon.

## Questions

```yaml
- question: "Which of the following carbocations is most stable?"
  type: multiple-choice
  options:
    - "CH₃⁺ (methyl carbocation)"
    - "CH₃CH₂⁺ (primary, ethyl)"
    - "(CH₃)₂CH⁺ (secondary, isopropyl)"
    - "(CH₃)₃C⁺ (tertiary, tert-butyl)"
  answer: 3
  explanation: "Carbocation stability increases with substitution: tertiary > secondary > primary > methyl. Each additional alkyl group donates electron density toward the electron-deficient carbon through hyperconjugation and inductive effects, spreading and stabilizing the positive charge. The tert-butyl cation has three methyl groups doing this work, making it the most stable of the four."

- question: "In a 1,2-hydride shift, the hydrogen atom first breaks away from the adjacent carbon as a free H⁻ ion, then rebonds to the carbocation."
  type: true-false
  answer: false
  explanation: "A 1,2-hydride shift is a concerted process: the hydrogen migrates with its bonding electron pair in a single step, directly from the adjacent carbon to the carbocation center. There is no free H⁻ intermediate and no bond-breaking before bond-making. This distinguishes rearrangements from radical or ionic chain reactions — the migrating group is always bonded to something throughout the shift."

- question: "Why do SN1 reactions sometimes produce a product with a different carbon skeleton than the starting material?"
  type: short-answer
  answer: "After the leaving group departs and a carbocation forms, a 1,2-hydride or methyl shift can occur if migration produces a more stable (more substituted) carbocation. The rearranged carbocation then captures the nucleophile, giving a product with a different connectivity."
  explanation: "SN1 proceeds through a free carbocation intermediate, and any carbocation that can rearrange to a more stable one will do so before the nucleophile attacks. Because the rearrangement moves a carbon–hydrogen or carbon–carbon bond to a new position, the carbon skeleton itself changes. This is why neopentyl substrates — which would form an unstable primary carbocation — rearrange to give products derived from a tertiary carbocation with a different framework."
```

## Explainer

When you studied SN1 reactions, you learned that the first step — loss of the leaving group — generates a carbocation intermediate. The reaction then completes when a nucleophile attacks that cation. What you may not have fully encountered is what happens *before* the nucleophile arrives if the initial carbocation is unstable: it rearranges.

The stability order of carbocations reflects how well surrounding atoms can donate electron density to the electron-deficient carbon. An alkyl group is slightly electron-donating, so each additional alkyl substituent helps stabilize the positive charge. Tertiary carbocations (3° — three carbon neighbors) are substantially more stable than secondary (2°), which are more stable than primary (1°), which are more stable than methyl. Methyl carbocations are so unstable that reactions that would generate them instead follow a completely different mechanistic pathway. The practical consequence: if a reaction generates a primary carbocation adjacent to a hydrogen-bearing carbon, nature will almost always rearrange.

The **1,2-hydride shift** is the dominant rearrangement mechanism. The hydrogen on the carbon directly adjacent to the cation migrates with both electrons from its C–H bond. In one concerted motion, a C–H bond breaks on the adjacent carbon and forms on the cationic carbon. The result is that the positive charge has moved one carbon over — and if that new location is more substituted, the carbocation is now more stable. A **1,2-methyl shift** works identically but with a methyl (or larger alkyl) group migrating instead of a hydrogen. Both shifts require the migrating group and the vacant orbital to be antiperiplanar (approximately aligned), which means the geometry of the substrate matters.

**Ring expansions** are the same phenomenon in cyclic systems. A cyclobutyl carbocation adjacent to a ring carbon can undergo a 1,2-shift where the C–C bond of the ring migrates, opening the 4-membered ring and generating a cyclopentyl carbocation — a five-membered ring that is both less strained and more substituted. This drives the expansion: ring strain relief plus greater carbocation stability combine to make the rearranged intermediate strongly favored. Five-to-six ring expansions are similarly favorable. This is why norbornane derivatives and cyclobutane-containing substrates show dramatic skeletal rearrangements in solvolysis reactions.

The practical implication is crucial for mechanism-writing: whenever you encounter an SN1 or E1 pathway, ask yourself whether the initially formed carbocation can rearrange. If a neighboring carbon has a hydrogen or alkyl group whose migration would generate a more substituted cation, rearrangement is likely and the major product will reflect the rearranged skeleton, not the original one. Predicting the major product correctly therefore requires following the stability thermodynamics, not just the initial structure of the substrate.
