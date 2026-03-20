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
stage: advanced
status: draft
---

# Carbocation Rearrangement: Hydride and Alkyl Shifts

## Core Idea
When a secondary carbocation is adjacent to a quaternary carbon, a hydride or alkyl group (often methyl) shifts from that quaternary carbon to the positive carbon, forming a more stable tertiary carbocation. These 1,2-shifts occur to increase carbocation stability and are a competing process in SN1 and E1 reactions. The driving force is the relief of strain and increased stabilization from additional alkyl substitution.

## Explainer

From your study of carbocation stability, you know that tertiary carbocations are more stable than secondary, which are more stable than primary, due to hyperconjugation and inductive effects from surrounding alkyl groups. Carbocation rearrangements are nature's way of exploiting this stability hierarchy: if a reaction generates a less stable carbocation and a more stable one is just one bond shift away, the rearrangement will often occur. The two main types — **hydride shifts** and **methyl (alkyl) shifts** — both follow the same logic but move different groups.

A **1,2-hydride shift** occurs when a hydrogen atom, along with its bonding electrons, migrates from an adjacent carbon to the positively charged carbon. Picture a secondary carbocation where the neighboring carbon bears a hydrogen: that hydrogen slides over, carrying the bonding pair with it. The positive charge moves to the carbon that lost the hydrogen, and if that carbon is now tertiary (surrounded by three alkyl groups), the rearrangement is energetically favorable. The "1,2" designation means the group moves between two adjacent carbons — longer-range shifts are rare because they would require impossible bond geometries.

A **1,2-methyl shift** (or more generally, an alkyl shift) follows identical logic, except an entire methyl group or alkyl group migrates instead of a hydrogen. This happens when no hydrogen is available on the adjacent carbon to shift, but an alkyl group is. For example, if a secondary carbocation sits next to a quaternary carbon (four carbon substituents, no hydrogens to shift), a methyl group can migrate from the quaternary carbon to the cation center. The result is the same: the positive charge relocates to a position with greater alkyl substitution, and stability increases.

These rearrangements matter practically because they produce **unexpected products** in SN1 and E1 reactions. If you predict the product of an SN1 reaction based on where the leaving group departs, you may get the wrong answer whenever the initially formed carbocation can rearrange to a more stable one. The nucleophile (or base, in E1) attacks the rearranged carbocation, not the original one. Whenever you see a carbocation intermediate in a mechanism, you should check the adjacent carbons: if a hydride or alkyl shift would produce a more stable cation, assume the rearrangement happens before the nucleophile arrives. This habit will save you from many incorrect product predictions.
