---
id: walden-inversion-stereochemistry
title: Walden Inversion and SN2 Stereochemistry
domain: chemistry
course: organic-chemistry
prerequisites:
- id: walden-inversion-sn2
  type: soft
- id: sn2-reaction
  type: hard
- id: enantiomers-and-chirality
  type: hard
builds-toward:
- substitution-vs-elimination
tags:
- stereochemistry
- inversion
- sn2
- mechanism
stage: advanced
status: draft
---

# Walden Inversion and SN2 Stereochemistry

## Core Idea
Walden inversion is the complete reversal of stereochemical configuration (R to S, or vice versa) that occurs during an SN2 reaction. The backside attack by the nucleophile displaces the leaving group through an in-line mechanism, inverting the stereochemistry at the stereocenter like an umbrella turning inside out.

## How It's Best Learned
Draw 3D structures showing backside attack, the transition state, and the inverted stereochemical product. Use molecular models to visualize the inversion geometry.

## Common Misconceptions
- Confusing inversion with racemization; SN2 produces a single inverted stereoisomer, not a 1:1 mixture.
- Forgetting that the entire stereochemical outcome depends on strict backside attack in the SN2 mechanism.

## Explainer

From your study of chirality, you know that a carbon bonded to four different groups exists as two non-superimposable mirror images — enantiomers labeled R or S. From your study of the SN2 mechanism, you know that the nucleophile attacks from the back side of the carbon bearing the leaving group in a single concerted step. **Walden inversion** is the stereochemical consequence that connects these two ideas: every SN2 reaction at a stereocenter inverts the configuration, converting R to S or S to R with complete stereochemical fidelity.

The classic analogy is an **umbrella flipping inside out** in a strong wind. Picture the three non-leaving substituents as the umbrella's canopy pointing toward you, with the leaving group as the handle pointing away. The nucleophile (the wind) strikes the handle side, pushing through and flipping the canopy to the other side. In the transition state, the carbon is momentarily **sp² hybridized** — the three remaining groups are coplanar with the carbon, and the nucleophile and leaving group sit on opposite sides in a linear arrangement. As the leaving group departs, the three groups relax away from the incoming nucleophile, completing the inversion. The geometry of this transition state makes inversion inevitable: there is no pathway for the nucleophile to attack from the front without colliding with the leaving group's electron cloud.

This stereochemical outcome is what distinguishes SN2 from SN1. In an SN1 reaction, the leaving group departs first to form a planar carbocation, and the nucleophile can then attack from either face — producing a roughly equal mixture of R and S products (**racemization**). In SN2, there is no carbocation intermediate; bond formation and bond breaking happen simultaneously through backside attack, guaranteeing **100% inversion**. If you start with a pure R substrate, you get a pure S product — not a mixture. This clean stereochemical outcome is one of the most reliable predictions in organic chemistry and a powerful tool for synthesis: if you need a specific stereochemistry at a carbon center, you can plan an SN2 reaction knowing exactly which configuration you will get.

The historical significance is worth noting. Paul Walden observed in 1896 that certain chemical transformations could convert one enantiomer into the other, but the mechanistic explanation came decades later when Hughes and Ingold established the SN2 mechanism. The Walden inversion became one of the key pieces of evidence for backside attack — if the mechanism allowed frontside attack, you would see retention of configuration instead. Whenever you assign the stereochemistry of an SN2 product, the rule is absolute: find the stereocenter, determine its current configuration, and flip it.
