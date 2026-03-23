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
stage: formal-systems
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

## Questions

```yaml
- question: "Adding HCl to 2-methylpropene [(CH₃)₂C=CH₂] gives predominantly one product. What is it, and why?"
  type: multiple-choice
  options:
    - "1-chloro-2-methylpropane, because HCl always adds Cl to the carbon with the most hydrogen substituents"
    - "2-chloro-2-methylpropane, because the proton adds to the terminal CH₂, generating a tertiary carbocation that is more stable than the alternative primary carbocation"
    - "A 50:50 mixture, because both carbons are equally accessible to the electrophile"
    - "1-chloro-2-methylpropane, because primary carbocations are kinetically preferred due to lower steric hindrance"
  answer: 1
  explanation: "When H⁺ adds to the terminal CH₂ of 2-methylpropene, the positive charge lands on the central carbon bearing three methyl groups — a tertiary carbocation. The alternative (H⁺ adding to the internal carbon) gives a primary carbocation. Tertiary carbocations are far more stable due to hyperconjugative electron donation from three alkyl groups. The major product is 2-chloro-2-methylpropane (tert-butyl chloride), with Cl on the more substituted carbon. Option A is the classic mnemonic confusion: the rule is that Cl goes to the MORE substituted carbon, not to the one with more H's."

- question: "Hydroboration-oxidation of propene gives 1-propanol (OH on C-1), while acid-catalyzed hydration gives 2-propanol (OH on C-2). The best explanation for this difference is:"
  type: multiple-choice
  options:
    - "Hydroboration is less regioselective and gives a random mixture that happens to favor C-1 addition"
    - "Water is a stronger nucleophile than borane and therefore prefers the terminal, less hindered carbon"
    - "Hydroboration proceeds through a concerted four-center transition state with no carbocation intermediate, so carbocation stability arguments do not apply and the boron adds to the less substituted carbon"
    - "The solvent in hydroboration reverses Markovnikov selectivity by stabilizing the primary carbocation"
  answer: 2
  explanation: "This contrast is the key test of whether you understand Markovnikov's rule mechanistically. Acid-catalyzed hydration goes through a carbocation: H⁺ adds to C-1 to generate the more stable secondary carbocation at C-2, then water attacks C-2 giving 2-propanol. Hydroboration is concerted — boron and hydrogen add simultaneously across the double bond with no carbocation formed at all. Since there is no intermediate to stabilize, the regioselectivity is governed by steric effects and orbital geometry, placing boron on the less substituted (terminal) carbon. Anti-Markovnikov outcome is the result of a different mechanism, not a reversal of carbocation stability."

- question: "Markovnikov's rule predicts that in the addition of HBr to an unsymmetrical alkene, Br adds to the carbon bearing the most hydrogen substituents."
  type: true-false
  answer: false
  explanation: "This is a common mnemonic error. Markovnikov's rule says H adds to the carbon with more hydrogens — equivalently, Br adds to the MORE substituted carbon (the one with fewer H's). The carbon with more H's is the less substituted one; the H going there generates a carbocation at the more substituted (adjacent) carbon. Confusing which group goes where is one of the most common errors in predicting addition products."

- question: "A resonance-stabilized allylic carbocation can be the preferred intermediate in an electrophilic addition even if it is not the most alkyl-substituted carbocation, and Markovnikov's rule (understood as a carbocation stability argument) correctly predicts this outcome."
  type: true-false
  answer: true
  explanation: "Markovnikov's rule, properly understood, says the electrophile adds to generate the MORE STABLE carbocation — regardless of whether stability comes from alkyl substitution or resonance. An allylic carbocation (stabilized by delocalization over two carbons) or a benzylic carbocation can be lower in energy than a more substituted but non-resonance-stabilized alternative. The carbocation stability framework predicts both situations correctly; the simple mnemonic ('H goes to C with more H's') fails for resonance-stabilized cases."

- question: "Why is it insufficient to memorize 'hydrogen goes to the carbon with more hydrogens' as a rule for predicting regioselectivity in electrophilic addition? Give an example where this shorthand fails but the carbocation stability argument correctly predicts the product."
  type: short-answer
  answer: "The mnemonic fails whenever the most stable carbocation is not the most alkyl-substituted one. For example, consider adding HBr to 1,3-butadiene (CH₂=CH-CH=CH₂). H⁺ can add to C-1 to give an allylic carbocation (charge delocalized over C-2 and C-4) or to C-2 to give a vinyl carbocation. The allylic carbocation at C-2/C-4 is far more stable than a vinyl carbocation, so H adds to C-1 despite C-1 having more H's than C-2. The product distribution (1,2-addition vs. 1,4-addition) follows from allylic stability, which the simple mnemonic cannot capture. Similarly, addition to styrene (PhCH=CH₂) gives the benzylic carbocation at the internal carbon regardless of substitution count, because benzylic stabilization dominates."
  explanation: "Understanding the mechanism rather than the mnemonic is what allows predictions in novel cases. The mnemonic is a heuristic that works for simple alkyl-substituted alkenes — where alkyl substitution and the number of H's are perfectly correlated. Once resonance, conjugation, or unusual substitution patterns enter, only the mechanistic understanding holds up."
```

## Explainer

You already understand electrophilic addition to alkenes: an electrophile attacks the electron-rich π bond, forming a carbocation intermediate, and a nucleophile then captures that carbocation. You also know from carbocation stability that tertiary carbocations are more stable than secondary, which are more stable than primary. **Markovnikov's rule** connects these two ideas — it tells you *where* on an unsymmetrical alkene each piece of the adding reagent ends up, and it does so by invoking the carbocation you already understand.

Consider adding HBr to propene (CH₃CH=CH₂). The proton (H⁺) can bond to either carbon of the double bond, generating two possible carbocations. If H⁺ adds to C-1 (the terminal CH₂), the positive charge lands on C-2, a **secondary carbocation** stabilized by two alkyl groups donating electron density through hyperconjugation. If H⁺ instead adds to C-2, the charge lands on C-1, a **primary carbocation** with only one stabilizing alkyl group. Since the secondary carbocation is lower in energy, the transition state leading to it is also lower in energy (Hammond's postulate), so that pathway dominates. Bromide then captures the secondary carbocation, placing Br on the more substituted carbon. The result: H ends up on the carbon that already had more hydrogens, and Br ends up on the more substituted carbon.

This is Markovnikov's rule stated mechanistically: **the electrophile (H⁺) adds to the less substituted carbon of the double bond because doing so generates the more stable carbocation intermediate**. The traditional shorthand — "the rich get richer," hydrogen goes to the carbon with more hydrogens — is a useful mnemonic but hides the real explanation. If you understand *why*, you can predict outcomes that the mnemonic alone cannot handle, such as cases where a less substituted carbocation is stabilized by resonance (allylic or benzylic positions) and becomes the preferred intermediate despite having fewer alkyl substituents.

The rule applies broadly to additions of HX (HCl, HBr, HI) and acid-catalyzed hydration (H₂O/H⁺) across unsymmetrical alkenes. It does *not* apply to reactions that proceed through different mechanisms — hydroboration, for example, follows a concerted pathway with no carbocation intermediate and gives anti-Markovnikov products. Recognizing whether a reaction goes through a carbocation or not is the key to knowing when Markovnikov's rule applies and when it does not.
