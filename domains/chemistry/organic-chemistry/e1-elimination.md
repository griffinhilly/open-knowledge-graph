---
id: e1-elimination
title: E1 Elimination Reactions
domain: chemistry
course: organic-chemistry
prerequisites:
- id: sn1-reaction
  type: hard
- id: e2-elimination
  type: soft
builds-toward:
- alcohols-and-ethers
tags:
- E1
- elimination
- unimolecular
- carbocation
- Zaitsev
- competing reactions
stage: formal-systems
status: validated
---

# E1 Elimination Reactions

## Core Idea
E1 (elimination unimolecular) shares its rate-limiting step with SN1: ionization to form a carbocation intermediate. In the second step, any available base removes a beta proton from the carbocation, generating the alkene. E1 and SN1 always compete from the same carbocation — the ratio of products depends on nucleophile/base concentration, temperature, and substrate. Like E2, Zaitsev's rule governs regioselectivity. Elevated temperature generally shifts product distribution toward elimination over substitution.

## How It's Best Learned
Draw the two-step E1 mechanism in full and compare the energy diagram directly with the one-step E2 diagram. Then use the four-factor analysis (substrate, nucleophile/base, solvent, leaving group, temperature) to predict the distribution among SN1, SN2, E1, and E2 products.

## Common Misconceptions
- E1 and SN1 always co-occur from the same carbocation intermediate — you cannot get pure SN1 product without any E1, except by controlling conditions.
- Increasing temperature favors elimination (E1 and E2) over substitution (SN1 and SN2) for entropic reasons.
- E1 does not require a strong base — even the solvent can act as the base that removes the beta proton.

## Explainer

If you understand the SN1 mechanism, you already understand the first and rate-determining step of E1: the leaving group departs on its own to form a carbocation intermediate. The rate law is first-order — rate = k[substrate] — because only the substrate is involved in the slow step. What distinguishes E1 from SN1 is what happens next. In SN1, a nucleophile attacks the carbocation carbon. In E1, a base removes a **beta proton** (a hydrogen on a carbon adjacent to the positive carbon), and the electrons from that C–H bond form the new pi bond of an alkene. The carbocation is the common fork in the road: it can either capture a nucleophile (SN1) or lose a proton (E1).

Because E1 and SN1 share the same intermediate, they **always compete** whenever a carbocation forms. You cannot run an SN1 reaction and get zero elimination, or vice versa — you always get a mixture. The practical question is which pathway dominates, and this depends on conditions. Higher temperature favors elimination because forming two product molecules (alkene + HB) from one substrate creates a positive entropy change (ΔS > 0), making elimination more thermodynamically favorable as temperature rises. Weak, bulky bases that are poor nucleophiles also tilt the balance toward E1, since they are better at abstracting an exposed proton than attacking a hindered carbon center.

When multiple beta positions carry hydrogens, E1 follows **Zaitsev's rule**: the more substituted alkene is the major product. The most substituted alkene is typically the most stable because of hyperconjugation — the same effect that stabilizes more substituted carbocations. If a secondary carbocation can lose a proton from either of two different beta carbons, the product with more alkyl groups on the double bond will predominate. This mirrors the regiochemistry of E2, though E1 tends to give slightly more Zaitsev product since the carbocation intermediate allows the thermodynamic product to dominate without the geometric constraints that anti-periplanar requirements impose on E2.

To decide whether a given reaction will proceed through E1 (versus E2, SN1, or SN2), apply the systematic analysis you have been building: E1 is favored by tertiary substrates (which form stable carbocations), polar protic solvents (which stabilize the carbocation and the leaving group), weak bases, and elevated temperature. Primary substrates essentially never undergo E1 because primary carbocations are too unstable to form. Secondary substrates can go E1 in highly ionizing solvents. Recognizing these patterns lets you predict not just whether elimination occurs, but which elimination mechanism — E1 or E2 — controls the product distribution.
