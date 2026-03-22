---
id: hydroboration-oxidation-anti-markovnikov
title: 'Hydroboration-Oxidation: Anti-Markovnikov Addition'
domain: chemistry
course: organic-chemistry
prerequisites:
- id: electrophilic-addition-to-alkenes
  type: hard
- id: alkene-structure-and-nomenclature
  type: hard
builds-toward:
- catalytic-hydrogenation-lindlar-catalyst
tags:
- hydroboration
- oxidation
- anti-markovnikov
- syn-addition
- alcohols
stage: advanced
status: draft
---

# Hydroboration-Oxidation: Anti-Markovnikov Addition

## Core Idea
Hydroboration-oxidation is a two-step sequence: first, borane (BH₃) adds to the alkene in a syn manner (both atoms add from the same face) and anti-Markovnikov manner (B adds to the less substituted carbon); then, hydrogen peroxide oxidizes the C-B bond to C-OH, inverting stereochemistry at that center. This sequence provides primary alcohols from terminal alkenes and secondary alcohols from internal alkenes with predictable regioselectivity and stereochemistry.

## Questions

```yaml
- question: "A student argues that hydroboration-oxidation places the hydroxyl group on the less substituted carbon because a primary carbocation is more stable than a tertiary one. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Primary carbocations are actually less stable than tertiary, so the argument is backwards"
    - "No carbocation intermediate forms — addition is concerted, and regiochemistry reflects steric preference of boron, not carbocation stability"
    - "The hydroxyl group actually ends up on the more substituted carbon in hydroboration-oxidation"
    - "The student is correct — carbocation stability does determine regiochemistry"
  answer: 1
  explanation: "The critical mechanistic distinction is that hydroboration proceeds through a concerted four-membered transition state — no carbocation ever forms. Boron, as the larger electrophilic atom, bonds to the less sterically hindered (less substituted) carbon to minimize steric strain. The regiochemistry is entirely steric in origin, which is why it is anti-Markovnikov rather than some modified carbocation argument."

- question: "What is the stereochemical consequence of performing hydroboration-oxidation on (Z)-2-butene compared to (E)-2-butene?"
  type: multiple-choice
  options:
    - "Both give the same racemic product because the intermediate is planar"
    - "Both give the same product because stereochemistry is lost during the oxidation step"
    - "They give different stereoisomeric products because syn addition preserves the relative face of addition from the starting alkene geometry"
    - "They give enantiomers of each other because the reaction proceeds through a carbocation that can be attacked from either face"
  answer: 2
  explanation: "Syn addition — both B and H add from the same face — combined with the fixed geometry of (Z) vs (E) alkenes produces different diastereomers. The concerted mechanism locks in the facial selectivity from the starting material, so geometry matters. This contrasts with reactions through carbocation intermediates, where rotation allows nucleophilic attack from either face and stereochemical information is often lost."

- question: "Hydroboration-oxidation places the hydroxyl group on the less substituted carbon because boron forms a more stable primary carbocation at that position."
  type: true-false
  answer: false
  explanation: "No carbocation forms in hydroboration-oxidation. The addition is concerted — boron and hydrogen add simultaneously through a four-membered transition state. The anti-Markovnikov outcome results from steric preference: boron, as the bulkier group, bonds to the less hindered carbon. Carbocation stability is irrelevant here, which is precisely why the reaction gives the opposite regiochemistry to acid-catalyzed hydration."

- question: "The syn addition observed in hydroboration-oxidation means that boron and hydrogen add to the same face of the alkene double bond."
  type: true-false
  answer: true
  explanation: "The concerted four-membered transition state forces boron and hydrogen to approach the alkene from the same face simultaneously. This syn selectivity is preserved through the oxidation step (which proceeds with retention of configuration at carbon), so the final alcohol retains the stereochemical information about which face of the double bond was attacked."

- question: "Why does hydroboration-oxidation give anti-Markovnikov regiochemistry, and how does this differ mechanistically from reactions that follow Markovnikov's rule?"
  type: short-answer
  answer: "Hydroboration-oxidation is concerted — no carbocation intermediate forms. Boron bonds to the less substituted carbon due to steric preference in the four-membered transition state. Markovnikov reactions (acid-catalyzed hydration, HX addition) proceed through a discrete carbocation intermediate that forms at the more substituted (more stable) carbon, directing the nucleophile there."
  explanation: "The mechanistic distinction is fundamental: carbocation stability controls Markovnikov regiochemistry, while steric effects in a concerted mechanism control anti-Markovnikov regiochemistry. Understanding this lets you predict regiochemistry from mechanism rather than memorizing outcomes — and explains why both reactions can serve as complementary tools to place OH on either carbon of a double bond."
```

## Explainer

From electrophilic addition to alkenes, you know that adding HBr or H₂O across a double bond typically follows Markovnikov's rule — the electrophile (H⁺) adds to the less substituted carbon, forming the more stable carbocation at the more substituted position, and the nucleophile (Br⁻ or OH⁻) ends up there. **Hydroboration-oxidation** achieves the opposite regiochemistry: the hydroxyl group ends up on the *less* substituted carbon, giving **anti-Markovnikov** addition. This complementary selectivity makes it one of the most important reactions in your synthetic toolkit.

The first step is **hydroboration**: borane (BH₃, often used as the THF complex BH₃·THF) adds across the double bond in a single concerted step — no carbocation intermediate forms. Boron is electron-deficient (it has an empty p orbital), so it acts as the electrophile, but because the addition is concerted rather than stepwise, both the B–H bond and the new C–B and C–H bonds form simultaneously through a four-membered transition state. Boron, being the larger atom, preferentially bonds to the **less sterically hindered** (less substituted) carbon. This steric preference is what produces anti-Markovnikov regiochemistry — it has nothing to do with carbocation stability because no carbocation ever forms. The concerted mechanism also ensures **syn addition**: boron and hydrogen both add from the same face of the double bond.

The second step is **oxidation**: treating the organoborane intermediate with hydrogen peroxide (H₂O₂) in aqueous NaOH replaces the C–B bond with a C–OH bond. The oxygen inserts between carbon and boron through a 1,2-migration with **retention of configuration** at the carbon that was bonded to boron. The net result is that the OH ends up exactly where the boron was — on the less substituted carbon, on the same face where addition occurred.

Consider 1-methylcyclohexene as a concrete example. Acid-catalyzed hydration (Markovnikov) would give 1-methylcyclohexanol — OH on the more substituted carbon. Hydroboration-oxidation gives *trans*-2-methylcyclohexanol — OH on the less substituted carbon, with syn stereochemistry. Having both reactions available means you can place the hydroxyl group on either carbon of an unsymmetrical alkene, choosing Markovnikov or anti-Markovnikov addition by choosing the appropriate reagent. This is the power of understanding mechanism over memorizing outcomes: the concerted, non-carbocation pathway of hydroboration is *why* it gives the "opposite" regiochemistry.
