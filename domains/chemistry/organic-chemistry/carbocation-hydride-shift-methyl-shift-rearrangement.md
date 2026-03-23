---
id: carbocation-hydride-shift-methyl-shift-rearrangement
title: 'Carbocation Rearrangement: Hydride and Alkyl Shifts'
domain: chemistry
course: organic-chemistry
prerequisites:
- id: carbocation-stability-rearrangement
  type: hard
- id: sn1-mechanism-kinetics-and-factors
  type: soft
builds-toward:
- e1-mechanism-zaitsev-rule
tags:
- carbocation-rearrangement
- hydride-shift
- methyl-shift
- 1,2-shift
stage: formal-systems
status: draft
---

# Carbocation Rearrangement: Hydride and Alkyl Shifts

## Core Idea
When a secondary carbocation is adjacent to a quaternary carbon, a hydride or alkyl group (often methyl) shifts from that quaternary carbon to the positive carbon, forming a more stable tertiary carbocation. These 1,2-shifts occur to increase carbocation stability and are a competing process in SN1 and E1 reactions. The driving force is the relief of strain and increased stabilization from additional alkyl substitution.

## Questions

```yaml
- question: "An SN1 reaction begins with 2-bromo-3-methylbutane. The leaving group departs from C2, generating an initial secondary carbocation. What product do you expect?"
  type: multiple-choice
  options:
    - "Substitution at C2 — the nucleophile attacks the initial secondary carbocation directly"
    - "Substitution at C3 — a hydride shift from C3 to C2 produces a tertiary carbocation at C3, and the nucleophile attacks there"
    - "No reaction — secondary carbocations are too unstable to form"
    - "Elimination only — secondary carbocations always eliminate rather than rearrange"
  answer: 1
  explanation: "After the leaving group departs from C2, the adjacent C3 bears a hydrogen and is part of a tertiary arrangement. A 1,2-hydride shift from C3 to C2 converts the secondary carbocation at C2 into a more stable tertiary carbocation at C3. The nucleophile then attacks C3, giving a product that a student predicting from the original leaving group position would get wrong. This is exactly why checking for possible rearrangements is mandatory before predicting SN1 products."

- question: "What is the fundamental driving force behind 1,2-hydride and 1,2-alkyl shifts in carbocation intermediates?"
  type: multiple-choice
  options:
    - "Relief of ring strain in cyclic systems"
    - "Formation of a more stable (more highly substituted) carbocation"
    - "Charge neutralization — the positive carbon becomes neutral after the shift"
    - "Faster reaction kinetics — shifted carbocations react more quickly with nucleophiles"
  answer: 1
  explanation: "Rearrangements are driven by the thermodynamic gain from moving from a less stable to a more stable carbocation. Tertiary carbocations are more stable than secondary due to greater hyperconjugation and inductive stabilization from surrounding alkyl groups. The shift occurs because the transition state leading to the more stable carbocation is lower in energy. Charge is not neutralized — it simply relocates to a position that is better stabilized."

- question: "In a 1,2-hydride shift, the hydrogen migrates from the positively charged carbocation center to an adjacent neutral carbon."
  type: true-false
  answer: false
  explanation: "This reverses the direction. A 1,2-hydride shift moves a hydrogen (with its bonding electrons) FROM a neutral adjacent carbon TO the positively charged carbocation center. The positive charge then moves to the carbon that donated the hydrogen. The migration always flows toward the positive center, because it is the carbocation's empty orbital that accepts the electron pair from the migrating group."

- question: "A 1,2-methyl shift can occur when the carbon adjacent to a secondary carbocation is a quaternary carbon bearing no hydrogens."
  type: true-false
  answer: true
  explanation: "This is precisely the scenario where alkyl shifts occur rather than hydride shifts. If the adjacent carbon has no H atoms available to migrate (as in a quaternary carbon with four C substituents), a methyl or other alkyl group can migrate instead. The driving force is the same: the rearrangement produces a more stable (often tertiary) carbocation. In fact, a 1,2-methyl shift from a quaternary carbon to an adjacent secondary carbocation is one of the clearest examples of carbocation rearrangement."

- question: "Why do carbocation rearrangements cause SN1 reactions to produce unexpected products, and what should you check before predicting any SN1 product?"
  type: short-answer
  answer: "Rearrangements cause unexpected products because the nucleophile attacks the rearranged carbocation, not the one initially formed when the leaving group departs. If the initial carbocation rearranges (via a hydride or alkyl shift) to a more stable carbocation at a different carbon, the product will have the nucleophile attached at that new position — not where the leaving group was. Before predicting any SN1 product, you should examine the carbons adjacent to the initially formed carbocation and check whether a hydride or alkyl shift would produce a more stable (more substituted) carbocation. If it would, assume the rearrangement occurs first."
  explanation: "The key habit is never predicting the SN1 product purely from where the leaving group departs. Rearrangement is a competing process that occurs before the nucleophile arrives, and it is favored whenever it yields a stability gain. The practical consequence is that SN1 reactions adjacent to quaternary or tertiary carbons should always be examined for possible rearrangements."
```

## Explainer

From your study of carbocation stability, you know that tertiary carbocations are more stable than secondary, which are more stable than primary, due to hyperconjugation and inductive effects from surrounding alkyl groups. Carbocation rearrangements are nature's way of exploiting this stability hierarchy: if a reaction generates a less stable carbocation and a more stable one is just one bond shift away, the rearrangement will often occur. The two main types — **hydride shifts** and **methyl (alkyl) shifts** — both follow the same logic but move different groups.

A **1,2-hydride shift** occurs when a hydrogen atom, along with its bonding electrons, migrates from an adjacent carbon to the positively charged carbon. Picture a secondary carbocation where the neighboring carbon bears a hydrogen: that hydrogen slides over, carrying the bonding pair with it. The positive charge moves to the carbon that lost the hydrogen, and if that carbon is now tertiary (surrounded by three alkyl groups), the rearrangement is energetically favorable. The "1,2" designation means the group moves between two adjacent carbons — longer-range shifts are rare because they would require impossible bond geometries.

A **1,2-methyl shift** (or more generally, an alkyl shift) follows identical logic, except an entire methyl group or alkyl group migrates instead of a hydrogen. This happens when no hydrogen is available on the adjacent carbon to shift, but an alkyl group is. For example, if a secondary carbocation sits next to a quaternary carbon (four carbon substituents, no hydrogens to shift), a methyl group can migrate from the quaternary carbon to the cation center. The result is the same: the positive charge relocates to a position with greater alkyl substitution, and stability increases.

These rearrangements matter practically because they produce **unexpected products** in SN1 and E1 reactions. If you predict the product of an SN1 reaction based on where the leaving group departs, you may get the wrong answer whenever the initially formed carbocation can rearrange to a more stable one. The nucleophile (or base, in E1) attacks the rearranged carbocation, not the original one. Whenever you see a carbocation intermediate in a mechanism, you should check the adjacent carbons: if a hydride or alkyl shift would produce a more stable cation, assume the rearrangement happens before the nucleophile arrives. This habit will save you from many incorrect product predictions.
