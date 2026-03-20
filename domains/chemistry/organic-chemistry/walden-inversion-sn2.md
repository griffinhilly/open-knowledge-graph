---
id: walden-inversion-sn2
title: Walden Inversion in SN2 Reactions
domain: chemistry
course: organic-chemistry
prerequisites:
- id: sn2-reaction
  type: hard
- id: stereochemistry-intro
  type: hard
builds-toward:
- substitution-vs-elimination
tags:
- Walden inversion
- backside attack
- stereochemistry
- SN2
- steric effects
- configuration
stage: advanced
status: draft
---
# Walden Inversion in SN2 Reactions

## Core Idea
In an SN2 reaction the nucleophile attacks from the side opposite the leaving group (backside attack), passing through a trigonal bipyramidal transition state that results in complete inversion of configuration at the carbon center — the Walden inversion. This stereochemical outcome is as reliable as an umbrella flipping inside-out in the wind: every substituent swaps to the opposite face. The requirement for backside attack also explains why SN2 rates drop sharply with increasing steric bulk around the electrophilic carbon, since bulky groups physically block the nucleophile's approach.

## How It's Best Learned
Use three-dimensional models (physical or software) to visualize the approach trajectory and the umbrella-flip transition state. Practice assigning R/S before and after reaction to confirm inversion occurred. Work through examples where inversion does and does not change the R/S label (it depends on CIP priority changes when the incoming group replaces the leaving group).

## Common Misconceptions
- Inversion of spatial arrangement does not automatically mean R switches to S; the CIP priority of the new substituent may reorder rankings, keeping the same label.
- Walden inversion is not partial — it is complete (100%) inversion at the attacked carbon, distinguishing SN2 from SN1 which gives racemization.
- Steric effects on SN2 are about the transition state geometry, not about thermodynamic stability of the product.

## Explainer

From your study of the SN2 mechanism, you know it is a one-step, concerted process: the nucleophile attacks the electrophilic carbon at the same time the leaving group departs. But there is a critical geometric constraint that your stereochemistry background makes clear. The nucleophile does not approach from just any direction — it attacks from the **backside**, the face directly opposite the leaving group. This approach angle is not a preference; it is a requirement dictated by orbital symmetry. The nucleophile's lone pair donates into the σ* antibonding orbital of the C–LG bond, and that orbital has its largest lobe on the backside of the carbon.

As the nucleophile approaches and the leaving group begins to depart, the three remaining substituents on the carbon flatten out into a plane, creating a **trigonal bipyramidal transition state** — the nucleophile on one side, the leaving group on the other, and the three groups arranged in a plane between them. Then, as the leaving group fully departs, those three groups swing through to the opposite side, like an umbrella flipping inside-out in a strong wind. This is the **Walden inversion**: every substituent ends up on the opposite face of the carbon from where it started. The inversion is complete — 100% of product molecules have the inverted configuration.

One subtlety that frequently causes confusion is the relationship between inversion and R/S designation. Inversion of the spatial arrangement always occurs, but whether the R/S label changes depends on the CIP priority rules. If the incoming nucleophile has a different CIP priority than the leaving group, the priority rankings may reshuffle, and the product might carry the same letter designation (R or S) despite having inverted geometry. The safe approach is to draw the three-dimensional arrangement before and after reaction and assign configurations directly, rather than assuming inversion automatically means R→S or S→R.

The backside-attack requirement also explains why **steric bulk** is the primary enemy of SN2 reactions. If the carbon bearing the leaving group is surrounded by large substituents — as in a tertiary carbon with three alkyl groups — those groups physically block the nucleophile's approach to the backside. Methyl and primary substrates react fastest because the backside is relatively open. Secondary substrates are slower, and tertiary substrates essentially do not undergo SN2 at all. This steric argument is purely about the geometry of the transition state; it has nothing to do with the thermodynamic stability of the product. Walden inversion thus connects stereochemical outcome and reaction rate to a single geometric principle: the nucleophile must come in from behind.
