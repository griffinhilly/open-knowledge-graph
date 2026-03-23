---
id: zaitsevs-rule-hofmann-elimination
title: Zaitsev's Rule and Hofmann Elimination
domain: chemistry
course: organic-chemistry
prerequisites:
- id: e2-elimination
  type: hard
- id: alkene-structure-and-nomenclature
  type: soft
tags:
- regioselectivity
- elimination
- hofmann
- zaitsev
- alkene-stability
stage: formal-systems
status: validated
---

# Zaitsev's Rule and Hofmann Elimination

## Core Idea
E2 eliminations typically form the most substituted (most stable) alkene product—Zaitsev's rule. This is because substitution stabilizes the C=C double bond. However, bulky bases (like t-BuOK) or quaternary ammonium hydroxides undergoing Hofmann elimination form the less substituted, terminal alkene product instead. This anti-Zaitsev selectivity occurs when steric hindrance dominates thermodynamic stability.

## Questions

```yaml
- question: "A chemist treats 2-bromobutane with potassium tert-butoxide (t-BuOK), a bulky base. Which product predominates and why?"
  type: multiple-choice
  options:
    - "2-butene, because t-BuOK is a strong base that favors the more stable alkene"
    - "1-butene, because the bulky tert-butyl group cannot reach the internal beta-hydrogen and abstracts the terminal one instead"
    - "Butane, because t-BuOK is too hindered to initiate elimination"
    - "A 1:1 mixture of 1-butene and 2-butene, because base size does not affect regioselectivity"
  answer: 1
  explanation: "t-BuOK is a bulky base — the three methyl groups create significant steric bulk. When approaching 2-bromobutane, the bulky base cannot reach the internal beta-hydrogens (adjacent to C2) because the carbon backbone blocks access. It can only abstract the more accessible terminal hydrogens on C1, yielding 1-butene (the less substituted alkene). This is the anti-Zaitsev or Hofmann product. Base size, not base strength, controls regioselectivity — both NaOEt and t-BuOK are strong bases, but only t-BuOK is bulky."

- question: "Which factor is the primary determinant of whether an E2 elimination gives the Zaitsev or anti-Zaitsev product?"
  type: multiple-choice
  options:
    - "The strength of the base — stronger bases give Zaitsev products"
    - "The temperature — higher temperatures favor the anti-Zaitsev product"
    - "The size of the base — bulky bases favor anti-Zaitsev products by directing abstraction to less hindered hydrogens"
    - "The leaving group — better leaving groups give Zaitsev products"
  answer: 2
  explanation: "The key variable is base size. A small, non-bulky base (like NaOEt) can reach both internal and terminal beta-hydrogens and preferentially abstracts the internal one because the transition state leading to the more substituted alkene is lower in energy (Zaitsev product). A bulky base (like t-BuOK) cannot reach the hindered internal hydrogens and is forced to abstract the terminal ones (anti-Zaitsev product). Neither base strength, temperature, nor leaving group identity is the primary determinant of this regioselectivity difference."

- question: "Zaitsev's rule predicts the major E2 product is the more substituted alkene because alkyl substituents destabilize the double bond through steric strain."
  type: true-false
  answer: false
  explanation: "This reverses the logic. Alkyl substituents actually stabilize double bonds through hyperconjugation — the overlap of adjacent C–H sigma bonds with the pi system donates electron density and lowers the energy of the alkene. More substituted alkenes are more stable. Zaitsev's rule predicts the more substituted alkene is the major product precisely because it is more stable (lower energy), and the E2 transition state has partial double-bond character that benefits from this stability."

- question: "Using a bulky base instead of a small base in an E2 elimination changes which beta-hydrogen is abstracted without changing the overall E2 mechanism."
  type: true-false
  answer: true
  explanation: "The mechanism remains E2 in both cases — concerted, anti-periplanar, with a strong base abstracting a beta-hydrogen as the leaving group departs. What changes is only which beta-hydrogen is accessible to the base. A bulky base is sterically prevented from reaching hindered (internal) beta-hydrogens and abstracts the more accessible terminal ones instead. The concertedness, the anti-periplanar requirement, and the role of the leaving group are all unchanged. Hofmann elimination is the same mechanism with a different regioselectivity outcome due to steric effects."

- question: "A synthetic chemist needs to make 1-butene (not 2-butene) from 2-bromobutane via E2 elimination. Describe what base should be used and why the choice achieves the desired regioselectivity."
  type: short-answer
  answer: "The chemist should use a bulky base such as potassium tert-butoxide (t-BuOK). The large tert-butyl group creates steric bulk around the basic oxygen, preventing it from reaching the internal beta-hydrogens adjacent to the bromine. Instead, the base abstracts the terminal beta-hydrogen on C1, forming 1-butene as the major product — the anti-Zaitsev (Hofmann) product. A small base like sodium ethoxide (NaOEt) would give 2-butene as the major product because it can access the internal hydrogens and the more substituted alkene is thermodynamically preferred."
  explanation: "This tests whether the student can apply the principle to a synthetic design problem rather than just recalling which rule gives which product. The key insight is that base SIZE (not strength or type) is the adjustable parameter that controls regioselectivity in E2 eliminations. Both NaOEt and t-BuOK are strong enough bases to drive E2; only their steric bulk differs."
```

## Explainer

From your study of E2 elimination, you know the mechanism: a strong base abstracts a beta-hydrogen while the leaving group departs, forming a new C=C double bond in a single concerted step. But when a substrate has beta-hydrogens on more than one carbon, which hydrogen gets abstracted? This is a question of **regioselectivity** — the elimination can form different constitutional isomers of the alkene depending on which beta-hydrogen is removed.

**Zaitsev's rule** states that the major product is the more substituted alkene — the one with more alkyl groups attached to the double bond carbons. Why? Alkyl groups stabilize double bonds through hyperconjugation (overlap of adjacent C–H sigma bonds with the pi system). A trisubstituted alkene is more stable than a disubstituted one, which is more stable than a monosubstituted one. Since E2 transition states have partial double-bond character, the transition state leading to the more substituted product is lower in energy, making it the kinetically and thermodynamically favored pathway. For example, when 2-bromobutane undergoes E2 elimination with sodium ethoxide, the major product is 2-butene (the more substituted, internal alkene), not 1-butene (the less substituted, terminal alkene).

The exception arises when steric effects override thermodynamic preferences. **Hofmann elimination** produces the less substituted alkene and occurs in two classic situations. First, when you use a bulky base like potassium tert-butoxide (t-BuOK), the large tert-butyl group physically cannot reach the more hindered internal beta-hydrogens. It instead abstracts the more accessible hydrogen on the less substituted carbon, yielding the terminal alkene. Second, the original Hofmann elimination involves heating a quaternary ammonium hydroxide — here the bulky NR₃ leaving group makes the transition state leading to the more substituted alkene sterically crowded, again favoring the less substituted product.

The practical takeaway is a simple decision rule: use a normal-sized base (like NaOEt or NaOH) for Zaitsev products (more substituted alkenes), and switch to a bulky base (t-BuOK) when you want the anti-Zaitsev or Hofmann product (less substituted, terminal alkene). This is one of the clearest examples in organic chemistry of how base choice controls product distribution — the substrate and mechanism are the same, but the size of the base determines which hydrogen is accessible and therefore which alkene forms.
