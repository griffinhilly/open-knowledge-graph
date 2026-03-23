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

## Questions

```yaml
- question: "HCl is added to 3,3-dimethyl-1-butene (CH₂=CH–C(CH₃)₃). Simple Markovnikov addition predicts 2-chloro-3,3-dimethylbutane as the major product. What actually forms and why?"
  type: multiple-choice
  options:
    - "2-chloro-3,3-dimethylbutane, via a stable secondary carbocation at C-2"
    - "2-chloro-2,3-dimethylbutane, because the initially formed secondary carbocation rearranges via a 1,2-methyl shift to a more stable tertiary carbocation"
    - "1-chloro-3,3-dimethylbutane via anti-Markovnikov addition due to steric bulk"
    - "Both products form equally because Markovnikov's rule does not apply to branched alkenes"
  answer: 1
  explanation: "The initial Markovnikov protonation places H at C-1, generating a secondary carbocation at C-2. A 1,2-methyl shift from the adjacent quaternary C-3 converts it to a more stable tertiary carbocation at C-3, which is then captured by Cl⁻. The hydrogen-counting mnemonic correctly predicts the initial protonation site but cannot anticipate rearrangements — only the mechanistic principle (always proceed toward greater carbocation stability) predicts the actual product."

- question: "What is the primary reason Markovnikov's rule correctly predicts the regiochemistry of HX addition to unsymmetrical alkenes?"
  type: multiple-choice
  options:
    - "The carbon with more hydrogens has higher electron density and preferentially attracts the proton"
    - "The rate-determining step generates a more stable carbocation when H adds to the less substituted carbon, leaving X to bond to the more substituted carbon"
    - "Halides preferentially bond to the less sterically hindered (less substituted) carbon"
    - "The thermodynamic product is always the more substituted alkyl halide, driving selectivity"
  answer: 1
  explanation: "The reaction is kinetically controlled: the rate-determining step is carbocation formation. The pathway through the more stable (more substituted) carbocation has lower activation energy and therefore predominates. Option A misidentifies the controlling factor — it is carbocation stability, not electron density. Option C gets the outcome backwards. Option D conflates kinetic and thermodynamic control."

- question: "Markovnikov's rule is fundamentally a statement about carbocation stability; the empirical 'hydrogen-counting' mnemonic works only because the carbon with fewer attached hydrogens is also the more substituted carbon, which better stabilizes a positive charge."
  type: true-false
  answer: true
  explanation: "The modern mechanistic understanding frames Markovnikov's rule entirely in terms of carbocation stability. The 'H goes to the more-H carbon' mnemonic works in simple cases because the more substituted carbon (fewer H's) is better at stabilizing positive charge via hyperconjugation and inductive effects. But the mnemonic fails when rearrangements occur — the mechanistic principle (greatest carbocation stability) always applies."

- question: "In electrophilic addition of HBr to an alkene, Br adds to the less substituted carbon because it is electronegative and is attracted to the electron-rich, less hindered end of the double bond."
  type: true-false
  answer: false
  explanation: "Br⁻ is a nucleophile that attacks the carbocation formed on the MORE substituted carbon. The statement reverses both the logic and the outcome. Regiochemistry is determined by which protonation pathway generates the more stable carbocation — the nucleophile then attacks that cationic site. Electronegativity of bromine and steric preference for the less hindered carbon are not the controlling factors."

- question: "A student claims that Markovnikov's rule is just a memorization trick about counting hydrogens. Using the mechanism of HX addition, explain why this view is incomplete and describe a situation where the mnemonic alone gives an incorrect prediction."
  type: short-answer
  answer: "Markovnikov's rule is grounded in carbocation stability. In the rate-determining step, the proton adds to give the most stable (most substituted) carbocation; the halide then captures it. The mnemonic works only because the more substituted carbon (fewer H's) better stabilizes positive charge. It breaks down when carbocation rearrangements are possible: if the initially formed carbocation can rearrange via a 1,2-hydride or methyl shift to an even more stable carbocation, the product will not match the simple mnemonic prediction. Only the mechanistic principle — follow the path of greatest carbocation stability — correctly handles these cases."
  explanation: "The hydrogen-counting mnemonic is a useful shortcut for simple substrates but provides no mechanistic insight. Students who understand the underlying mechanism can handle rearrangements, ring-expansion products, and unusual substrates; those who only memorized the mnemonic cannot."
```

## Explainer

You know from electrophilic addition that the π bond of an alkene acts as a nucleophile, attacking an electrophile. You also know from carbocation stability that tertiary carbocations are more stable than secondary, which are more stable than primary. **Markovnikov's rule** is the direct consequence of combining these two ideas: when HX adds to an unsymmetrical alkene, the hydrogen goes to the less substituted carbon and the halide goes to the more substituted carbon, because this pathway routes through the more stable carbocation intermediate.

Walk through the mechanism step by step. Consider the addition of HBr to propene (CH₂=CH–CH₃). In the first step, the π electrons of the double bond attack the electrophilic proton of HBr. The proton can bond to either carbon of the double bond, and this is the decision point. If H bonds to C-1 (the –CH₂ end), a secondary carbocation forms on C-2. If H bonds to C-2 (the –CHCH₃ end), a primary carbocation forms on C-1. The secondary carbocation is significantly more stable due to hyperconjugation from the adjacent C–H bonds and the inductive effect of the methyl group. Because this step is **rate-determining**, the reaction preferentially follows the lower-energy pathway — the one that generates the more stable carbocation. In the second step, the bromide ion (released when H⁺ was captured) attacks the carbocation, forming 2-bromopropane as the major product.

The modern understanding reframes Markovnikov's rule as a statement about **carbocation stability**, not about hydrogen counting. The original empirical rule — "hydrogen adds to the carbon with more hydrogens" — is a useful mnemonic, but it works only because the carbon with fewer hydrogens is also the more substituted carbon, and therefore the one that better stabilizes a positive charge. The mechanistic explanation is more powerful because it extends to cases the empirical rule cannot handle. For instance, addition of HCl to methylenecyclohexane places H on the exocyclic =CH₂ (forming a tertiary carbocation on the ring carbon) rather than on the ring carbon (which would give a primary carbocation). The empirical rule about hydrogen counting gives the right answer here, but only the mechanistic reasoning explains *why*.

Markovnikov's rule also explains why **carbocation rearrangements** sometimes produce unexpected products. If the initially formed Markovnikov carbocation is secondary but a 1,2-hydride or methyl shift can generate a more stable tertiary carbocation, the rearrangement will occur before the nucleophile captures the cation. The final product then appears to violate simple Markovnikov addition, but it is fully consistent with the underlying principle: the reaction follows the path of greatest carbocation stability. Recognizing when rearrangement is possible — and when it is not — is the key to applying Markovnikov's rule correctly in complex substrates.
