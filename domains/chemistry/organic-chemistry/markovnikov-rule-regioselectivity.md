---
id: markovnikov-rule-regioselectivity
title: Markovnikov's Rule and Regioselectivity in Addition
domain: chemistry
course: organic-chemistry
prerequisites:
- id: electrophilic-addition-to-alkenes
  type: hard
- id: carbocation-stability-rearrangement
  type: hard
builds-toward:
- hydroboration-oxidation-alkenes
- oxymercuration-mechanism
tags:
- regioselectivity
- addition
- markovnikov
- carbocation
stage: advanced
status: draft
---

# Markovnikov's Rule and Regioselectivity in Addition

## Core Idea
Markovnikov's rule states that in addition of HX or H₂O to unsymmetrical alkenes, hydrogen adds to the carbon with more hydrogens, and X (or OH) adds to the more substituted carbon. This regioselectivity reflects the mechanism: a carbocation forms at the position that generates the more stable (more substituted) carbocation intermediate.

## How It's Best Learned
Predict regioisomers for Markovnikov additions and confirm that the major product arises from the most stable carbocation. Contrast with anti-Markovnikov reactions to reinforce mechanistic understanding.

## Common Misconceptions
- Treating Markovnikov's rule as a memorized rule rather than a consequence of carbocation stability.
- Forgetting that anti-Markovnikov additions occur when alternative mechanisms (hydroboration) avoid forming the less stable carbocation.

## Explainer

You already understand electrophilic addition to alkenes: an electrophile attacks the electron-rich π bond, forming a carbocation intermediate, and a nucleophile then captures that carbocation. You also know from carbocation stability that tertiary carbocations are more stable than secondary, which are more stable than primary. **Markovnikov's rule** connects these two ideas — it tells you *where* on an unsymmetrical alkene each piece of the adding reagent ends up, and it does so by invoking the carbocation you already understand.

Consider adding HBr to propene (CH₃CH=CH₂). The proton (H⁺) can bond to either carbon of the double bond, generating two possible carbocations. If H⁺ adds to C-1 (the terminal CH₂), the positive charge lands on C-2, a **secondary carbocation** stabilized by two alkyl groups donating electron density through hyperconjugation. If H⁺ instead adds to C-2, the charge lands on C-1, a **primary carbocation** with only one stabilizing alkyl group. Since the secondary carbocation is lower in energy, the transition state leading to it is also lower in energy (Hammond's postulate), so that pathway dominates. Bromide then captures the secondary carbocation, placing Br on the more substituted carbon. The result: H ends up on the carbon that already had more hydrogens, and Br ends up on the more substituted carbon.

This is Markovnikov's rule stated mechanistically: **the electrophile (H⁺) adds to the less substituted carbon of the double bond because doing so generates the more stable carbocation intermediate**. The traditional shorthand — "the rich get richer," hydrogen goes to the carbon with more hydrogens — is a useful mnemonic but hides the real explanation. If you understand *why*, you can predict outcomes that the mnemonic alone cannot handle, such as cases where a less substituted carbocation is stabilized by resonance (allylic or benzylic positions) and becomes the preferred intermediate despite having fewer alkyl substituents.

The rule applies broadly to additions of HX (HCl, HBr, HI) and acid-catalyzed hydration (H₂O/H⁺) across unsymmetrical alkenes. It does *not* apply to reactions that proceed through different mechanisms — hydroboration, for example, follows a concerted pathway with no carbocation intermediate and gives anti-Markovnikov products. Recognizing whether a reaction goes through a carbocation or not is the key to knowing when Markovnikov's rule applies and when it does not.
