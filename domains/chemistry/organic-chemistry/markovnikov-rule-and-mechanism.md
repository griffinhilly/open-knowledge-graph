---
id: markovnikov-rule-and-mechanism
title: Markovnikov's Rule and Electrophilic Addition Mechanisms
domain: chemistry
course: organic-chemistry
prerequisites:
- id: electrophilic-addition-to-alkenes
  type: hard
- id: carbocation-stability-rearrangement
  type: hard
builds-toward:
- anti-markovnikov-addition-hydroboration
tags:
- regioselectivity
- markovnikov
- carbocation
- mechanistic-selectivity
stage: formal-systems
status: draft
---

# Markovnikov's Rule and Electrophilic Addition Mechanisms

## Core Idea
Markovnikov's rule states that in HX addition to an alkene, H adds to the carbon with more hydrogens (the less substituted carbon), and X adds to form the more substituted carbocation intermediate. This is a mechanistic consequence: the rate-determining step is carbocation formation, and more substituted carbocations are more stable. The rule applies to HX, H₂SO₄, etc., whenever a carbocation intermediate is involved.

## Explainer

You know from electrophilic addition that the π bond of an alkene acts as a nucleophile, attacking an electrophile. You also know from carbocation stability that tertiary carbocations are more stable than secondary, which are more stable than primary. **Markovnikov's rule** is the direct consequence of combining these two ideas: when HX adds to an unsymmetrical alkene, the hydrogen goes to the less substituted carbon and the halide goes to the more substituted carbon, because this pathway routes through the more stable carbocation intermediate.

Walk through the mechanism step by step. Consider the addition of HBr to propene (CH₂=CH–CH₃). In the first step, the π electrons of the double bond attack the electrophilic proton of HBr. The proton can bond to either carbon of the double bond, and this is the decision point. If H bonds to C-1 (the –CH₂ end), a secondary carbocation forms on C-2. If H bonds to C-2 (the –CHCH₃ end), a primary carbocation forms on C-1. The secondary carbocation is significantly more stable due to hyperconjugation from the adjacent C–H bonds and the inductive effect of the methyl group. Because this step is **rate-determining**, the reaction preferentially follows the lower-energy pathway — the one that generates the more stable carbocation. In the second step, the bromide ion (released when H⁺ was captured) attacks the carbocation, forming 2-bromopropane as the major product.

The modern understanding reframes Markovnikov's rule as a statement about **carbocation stability**, not about hydrogen counting. The original empirical rule — "hydrogen adds to the carbon with more hydrogens" — is a useful mnemonic, but it works only because the carbon with fewer hydrogens is also the more substituted carbon, and therefore the one that better stabilizes a positive charge. The mechanistic explanation is more powerful because it extends to cases the empirical rule cannot handle. For instance, addition of HCl to methylenecyclohexane places H on the exocyclic =CH₂ (forming a tertiary carbocation on the ring carbon) rather than on the ring carbon (which would give a primary carbocation). The empirical rule about hydrogen counting gives the right answer here, but only the mechanistic reasoning explains *why*.

Markovnikov's rule also explains why **carbocation rearrangements** sometimes produce unexpected products. If the initially formed Markovnikov carbocation is secondary but a 1,2-hydride or methyl shift can generate a more stable tertiary carbocation, the rearrangement will occur before the nucleophile captures the cation. The final product then appears to violate simple Markovnikov addition, but it is fully consistent with the underlying principle: the reaction follows the path of greatest carbocation stability. Recognizing when rearrangement is possible — and when it is not — is the key to applying Markovnikov's rule correctly in complex substrates.
