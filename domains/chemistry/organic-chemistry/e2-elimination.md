---
id: e2-elimination
title: E2 Elimination Reactions
domain: chemistry
course: organic-chemistry
prerequisites:
- id: sn2-reaction
  type: hard
- id: alkene-structure-and-nomenclature
  type: hard
builds-toward:
- e1-elimination
tags:
- E2
- elimination
- bimolecular
- Zaitsev
- anti-periplanar
- regioselectivity
stage: formal-systems
status: validated
---

# E2 Elimination Reactions

## Core Idea
E2 (elimination bimolecular) is a concerted single-step reaction: a strong base abstracts a beta proton simultaneously as the leaving group departs, forming a double bond in one step with no intermediate. The geometry requirement is strict — the H being removed and the leaving group must be anti-periplanar (180°). Zaitsev's rule predicts the major product is the more substituted (thermodynamically more stable) alkene. E2 competes with SN2 under similar conditions, and bulky bases strongly favor elimination.

## How It's Best Learned
Use Newman projections to identify the anti-periplanar conformer required for E2. Practice predicting the regiochemistry using Zaitsev's rule and the stereochemistry of the product alkene from each anti-periplanar H. Pay special attention to cyclic substrates requiring diaxial H and leaving group.

## Common Misconceptions
- E2 requires a strong base but not necessarily a good nucleophile — bulky bases like t-BuOK favor elimination over substitution precisely because they are poor nucleophiles.
- Anti-periplanar means exactly 180°, not loosely 'on opposite sides'; violating this geometry prevents the concerted mechanism.
- In cyclohexane systems, the H and leaving group must both be axial (diaxial) for anti-periplanar geometry to be achievable.

## Explainer

You already know the SN2 mechanism: a nucleophile attacks a carbon bearing a leaving group in a single concerted step, inverting stereochemistry. The **E2 reaction** is the elimination counterpart — also concerted and bimolecular, but instead of substitution, it forms a **double bond**. A strong base abstracts a proton from the beta carbon (the carbon adjacent to the one bearing the leaving group) at the same time the leaving group departs. In one simultaneous motion, the C–H bond breaks, the C–X bond breaks, and a new pi bond forms between the alpha and beta carbons. There is no intermediate — this is a single transition state.

The geometry requirement is what makes E2 distinctive and predictable. The hydrogen being removed and the leaving group must be **anti-periplanar** — positioned exactly 180° apart when viewed along the C–C bond axis. This arrangement allows the developing p orbitals (from the breaking C–H and C–X bonds) to overlap smoothly into the new pi bond. Newman projections are the best tool for visualizing this: rotate the molecule until you find the conformer where the H and the leaving group are anti to each other. In acyclic systems, this is usually straightforward because free rotation allows the molecule to adopt the needed geometry. In **cyclohexane rings**, the requirement is stricter: both the H and the leaving group must be axial and on opposite faces of the ring (diaxial and trans to each other). If the leaving group is equatorial, a ring flip must occur before E2 can proceed.

**Zaitsev's rule** predicts which alkene forms as the major product: the more substituted alkene is generally favored because it is more thermodynamically stable. If a substrate has multiple beta hydrogens that could be removed, the base preferentially abstracts the one that leads to the more substituted double bond. However, **bulky bases** like potassium tert-butoxide (t-BuOK) reverse this preference — they cannot easily access the more hindered beta hydrogen and instead remove the less hindered one, giving the less substituted (Hofmann) product. This is a practical tool: by choosing your base, you can steer the reaction toward the product you want.

E2 and SN2 are always in competition when a strong base/nucleophile encounters a substrate with a leaving group. The key factors that tip the balance toward elimination include heat (which favors the more entropically favorable elimination), bulky bases (poor nucleophiles but effective bases), and increased substitution at the alpha carbon (which sterically hinders the backside attack needed for SN2). Understanding this competition is essential for predicting reaction outcomes and designing synthetic routes.
