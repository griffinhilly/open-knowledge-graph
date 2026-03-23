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
status: validated
---

# Zaitsev and Hofmann Selectivity in Elimination Reactions

## Core Idea
Zaitsev's rule predicts that elimination yields the more substituted (more stable) alkene as the major product in E1 and E2 reactions. Hofmann elimination (degradation of quaternary ammonium hydroxides) often violates Zaitsev's rule, producing the less substituted alkene due to steric hindrance from the bulky leaving group preventing formation of the more substituted alkene.

## How It's Best Learned
Predict E1 and E2 products using Zaitsev's rule, then identify exceptions (Hofmann) and explain why steric effects override thermodynamic stability.

## Common Misconceptions
- Assuming all eliminations follow Zaitsev's rule; conditions and leaving group size determine the outcome.
- Misunderstanding the mechanism of Hofmann elimination as a distinct elimination type rather than a steric variant of standard E1/E2.

## Questions

```yaml
- question: "A student predicts that treating 2-methylbutyltrimethylammonium hydroxide with base will produce 2-methylbut-2-ene (the more substituted alkene) as the major product, reasoning that it is thermodynamically more stable. What is the flaw in this prediction?"
  type: multiple-choice
  options:
    - "The substrate cannot undergo elimination because quaternary ammonium ions are too stable to react"
    - "The reaction will proceed via E1, not E2, so Zaitsev's rule does not apply here"
    - "The trimethylammonium leaving group is bulky, which prevents the base from accessing the more hindered beta-hydrogen; the Hofmann product (less substituted alkene) is the major product"
    - "The more substituted alkene is actually less stable in this case, so Zaitsev's rule predicts the less substituted product anyway"
  answer: 2
  explanation: "Quaternary ammonium leaving groups are large and bulky. In the E2 transition state, the base, the departing hydrogen, and the leaving group must be arranged anti-periplanar. The steric bulk of the –N(CH₃)₃⁺ group raises the activation energy for removing the more hindered beta-hydrogen (which would give the Zaitsev product), redirecting the reaction toward the less hindered hydrogen and the Hofmann (less substituted) alkene. The student correctly applies Zaitsev's rule but ignores the steric override."

- question: "Potassium tert-butoxide reacts with 2-bromobutane under E2 conditions. Which outcome is expected?"
  type: multiple-choice
  options:
    - "But-2-ene (Zaitsev product) forms predominantly because tert-butoxide is a strong, hindered base that favors E2 over SN2"
    - "But-1-ene (Hofmann product) forms predominantly because tert-butoxide is bulky and preferentially abstracts the less hindered terminal hydrogen"
    - "SN2 substitution predominates because tert-butoxide is an excellent nucleophile"
    - "Both but-1-ene and but-2-ene form in equal amounts because tert-butoxide has no preference"
  answer: 1
  explanation: "Tert-butoxide is bulky due to its three methyl groups. It has difficulty reaching the more hindered internal beta-hydrogen (C-3) that would produce but-2-ene, but can easily access the less hindered terminal hydrogen (C-1). This steric preference overrides the thermodynamic bias toward the more substituted alkene, giving the Hofmann product. Bulky bases consistently direct E2 reactions toward less substituted alkenes."

- question: "Hofmann elimination is a mechanistically distinct reaction type from E2 — it involves a different transition state geometry than standard E2 elimination."
  type: true-false
  answer: false
  explanation: "Hofmann elimination is not a separate mechanism — it follows standard E2 mechanics with the same anti-periplanar transition state requirement. The only difference is that steric bulk (from a bulky base or bulky leaving group) raises the activation energy for the pathway leading to the more substituted (Zaitsev) alkene, redirecting the reaction toward the less substituted product. The mechanism itself is identical to any E2 reaction."

- question: "A bulky leaving group alone — not just a bulky base — can direct an elimination reaction toward the Hofmann (less substituted) product."
  type: true-false
  answer: true
  explanation: "Steric bulk near the reacting carbon can originate from either the leaving group or the base. Quaternary ammonium salts (–N(CH₃)₃⁺) are the classic example: the bulky leaving group creates steric congestion around the more substituted beta-carbon, making it harder for the base to achieve the required anti-periplanar geometry there. The result is identical to using a bulky base — the less hindered hydrogen is abstracted and the less substituted alkene predominates."

- question: "Explain why Hofmann elimination produces the less substituted alkene, in terms of the E2 transition state geometry rather than just 'steric hindrance blocks access.'"
  type: short-answer
  answer: "E2 elimination requires a specific anti-periplanar arrangement: the base, the beta-hydrogen being abstracted, the alpha-carbon, and the leaving group must all lie in the same plane with a 180° dihedral angle. When the leaving group or base is bulky, achieving this geometry at the more substituted beta-carbon is sterically demanding — multiple groups crowd the transition state. The activation energy for that pathway rises, making it slower than the less substituted pathway where the transition state is less congested. The reaction favors whichever anti-periplanar arrangement has lower steric strain in the transition state."
  explanation: "The key is that it is not simply about 'the base can't get close' — it is about the geometry of the entire transition state, which requires five atoms in near-coplanar alignment. Steric bulk disrupts this specific geometry at the more substituted carbon without necessarily blocking access to the alpha-carbon. Understanding the anti-periplanar requirement explains why Hofmann products result even when the base is not especially bulky, as long as the leaving group creates enough congestion at the more substituted position."
```

## Explainer

From your study of E1 and E2 elimination, you know that when a leaving group departs along with a proton from a neighboring carbon, an alkene forms. But when the substrate has multiple beta-hydrogens on different carbons, there is a choice: the reaction could form different alkene products depending on which hydrogen is removed. **Regioselectivity** — which positional isomer of the alkene predominates — is governed by a competition between thermodynamic stability and steric accessibility.

**Zaitsev's rule** states that the more substituted alkene is the major product. This holds for most E1 and E2 reactions with typical bases and leaving groups. The reasoning is straightforward: more substituted alkenes are more thermodynamically stable due to hyperconjugation (the same stabilization that makes more substituted carbocations more stable). In E1 reactions, where the carbocation intermediate allows the system to sample multiple transition states, the product distribution closely reflects thermodynamic stability. In E2 reactions with small, strong bases like ethoxide or hydroxide, the transition state resembles the product enough that the more stable alkene is still favored.

**Hofmann elimination** is the classic exception. When the leaving group is bulky — the textbook case is a quaternary ammonium salt, –N(CH₃)₃⁺, but bulky bases like potassium tert-butoxide produce the same effect — the base cannot easily reach the more hindered beta-hydrogen that would produce the Zaitsev product. Instead, it abstracts the more accessible, less hindered hydrogen, yielding the **less substituted alkene** as the major product. The reaction still follows E2 mechanics; the only difference is that steric congestion around the more substituted position raises the activation energy for that pathway enough to redirect the reaction toward the less substituted product.

The practical takeaway is a decision framework: look at the base and the leaving group. Small base and small leaving group? Expect the Zaitsev (more substituted) alkene. Bulky base or bulky leaving group? Expect the Hofmann (less substituted) alkene. This is not an arbitrary rule to memorize — it follows directly from the geometry of the E2 transition state, where the base, the departing hydrogen, and the leaving group must all be arranged in a specific anti-periplanar relationship. Steric bulk disrupts that arrangement for the more substituted pathway, tilting the balance toward the less substituted product.
