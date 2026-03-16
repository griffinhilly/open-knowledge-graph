---
id: zaitsev-hofmann-elimination-selectivity
title: Zaitsev and Hofmann Selectivity in Elimination Reactions
domain: chemistry
course: organic-chemistry
prerequisites:
- id: e1-elimination
  type: hard
- id: e2-elimination
  type: hard
builds-toward:
- substitution-vs-elimination
tags:
- regioselectivity
- elimination
- zaitsev
- hofmann
- alkene
stage: formal-systems
status: draft
---

# Zaitsev and Hofmann Selectivity in Elimination Reactions

## Core Idea
Zaitsev's rule predicts that elimination yields the more substituted (more stable) alkene as the major product in E1 and E2 reactions. Hofmann elimination (degradation of quaternary ammonium hydroxides) often violates Zaitsev's rule, producing the less substituted alkene due to steric hindrance from the bulky leaving group preventing formation of the more substituted alkene.

## How It's Best Learned
Predict E1 and E2 products using Zaitsev's rule, then identify exceptions (Hofmann) and explain why steric effects override thermodynamic stability.

## Common Misconceptions
- Assuming all eliminations follow Zaitsev's rule; conditions and leaving group size determine the outcome.
- Misunderstanding the mechanism of Hofmann elimination as a distinct elimination type rather than a steric variant of standard E1/E2.

## Explainer

From your study of E1 and E2 elimination, you know that when a leaving group departs along with a proton from a neighboring carbon, an alkene forms. But when the substrate has multiple beta-hydrogens on different carbons, there is a choice: the reaction could form different alkene products depending on which hydrogen is removed. **Regioselectivity** — which positional isomer of the alkene predominates — is governed by a competition between thermodynamic stability and steric accessibility.

**Zaitsev's rule** states that the more substituted alkene is the major product. This holds for most E1 and E2 reactions with typical bases and leaving groups. The reasoning is straightforward: more substituted alkenes are more thermodynamically stable due to hyperconjugation (the same stabilization that makes more substituted carbocations more stable). In E1 reactions, where the carbocation intermediate allows the system to sample multiple transition states, the product distribution closely reflects thermodynamic stability. In E2 reactions with small, strong bases like ethoxide or hydroxide, the transition state resembles the product enough that the more stable alkene is still favored.

**Hofmann elimination** is the classic exception. When the leaving group is bulky — the textbook case is a quaternary ammonium salt, –N(CH₃)₃⁺, but bulky bases like potassium tert-butoxide produce the same effect — the base cannot easily reach the more hindered beta-hydrogen that would produce the Zaitsev product. Instead, it abstracts the more accessible, less hindered hydrogen, yielding the **less substituted alkene** as the major product. The reaction still follows E2 mechanics; the only difference is that steric congestion around the more substituted position raises the activation energy for that pathway enough to redirect the reaction toward the less substituted product.

The practical takeaway is a decision framework: look at the base and the leaving group. Small base and small leaving group? Expect the Zaitsev (more substituted) alkene. Bulky base or bulky leaving group? Expect the Hofmann (less substituted) alkene. This is not an arbitrary rule to memorize — it follows directly from the geometry of the E2 transition state, where the base, the departing hydrogen, and the leaving group must all be arranged in a specific anti-periplanar relationship. Steric bulk disrupts that arrangement for the more substituted pathway, tilting the balance toward the less substituted product.
