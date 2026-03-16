---
id: meso-compounds-prochirality
title: Meso Compounds and Prochiral Centers
domain: chemistry
course: organic-chemistry
prerequisites:
- id: diastereomers-and-meso-compounds
  type: hard
- id: r-s-stereochemical-designation
  type: hard
tags:
- stereochemistry
- meso
- achiral
- plane-of-symmetry
- prochirality
stage: formal-systems
status: draft
---

# Meso Compounds and Prochiral Centers

## Core Idea
A meso compound has multiple stereocenters but is achiral due to an internal plane of symmetry; its R and S stereocenters cancel in terms of optical rotation. Prochiral compounds lack stereogenicity overall but contain groups that would become stereocenters if modified. Enzymatic reactions often distinguish prochiral groups, assigning pro-R/pro-S labels based on priority rules.

## Explainer

From your study of diastereomers and meso compounds, you know that a meso compound contains stereocenters yet is achiral because an internal mirror plane makes the molecule superimposable on its mirror image. You also know how to assign R and S configurations using Cahn-Ingold-Prelog priority rules. This topic deepens both concepts and introduces **prochirality** — a subtle but powerful idea that connects stereochemistry to enzyme selectivity.

Consider **meso-tartaric acid**, one of the classic examples. It has two stereocenters, one with R configuration and the other with S. If you draw the molecule in its eclipsed conformation and look for a mirror plane perpendicular to the C2–C3 bond, you will find it: the top half of the molecule is a mirror image of the bottom half. Because of this symmetry, the optical rotation from the R center is exactly canceled by the opposite rotation from the S center, and the compound shows **zero net optical rotation**. It is not a racemic mixture (which is a 50:50 mixture of two enantiomers) — it is a single, pure compound that happens to be achiral. This distinction matters: a racemic mixture can be resolved into its component enantiomers; a meso compound cannot, because there are no enantiomers to separate.

**Prochirality** describes molecules or groups that are not chiral themselves but are one step away from becoming chiral. A **prochiral center** is a tetrahedral carbon bearing two identical substituents. If you mentally replace one of those identical groups with something different, the carbon becomes a stereocenter. The two identical groups are called **enantiotopic** — they are related by a mirror plane in the molecule. To label them, you use the pro-R/pro-S system: mentally replace each group in turn with a higher-priority group, determine whether the resulting stereocenter would be R or S, and assign that label to the original group. For example, in ethanol (CH₃CH₂OH), the two hydrogens on C-1 are enantiotopic. Replacing one gives R at that center, so it is the **pro-R hydrogen**; replacing the other gives S, making it the **pro-S hydrogen**.

Why does this matter? Because **enzymes are chiral catalysts** that can distinguish between enantiotopic groups. When alcohol dehydrogenase removes a hydrogen from ethanol to make acetaldehyde, it selectively removes the pro-R hydrogen and ignores the pro-S hydrogen. Similarly, when a reductase adds hydrogen to a prochiral ketone, it delivers it to one specific face, producing one enantiomer preferentially. This enantiotopic selectivity is a direct consequence of the enzyme's chiral active site interacting differently with groups that, to a small-molecule achiral reagent, would look identical. Understanding prochirality lets you predict which stereochemical outcome an enzymatic reaction will produce and explains why biological systems achieve stereoselectivity that synthetic chemists often struggle to replicate.
