---
id: allylic-oxidation-selectivity
title: Allylic Oxidation and Selectivity
domain: chemistry
course: organic-chemistry
prerequisites:
- id: oxidation-reactions-organic
  type: soft
- id: free-radical-chain-halogenation
  type: soft
builds-toward:
- alcohol-oxidation-to-carbonyls
tags:
- oxidation
- allylic
- selectivity
- free-radical
stage: formal-systems
status: validated
---

# Allylic Oxidation and Selectivity

## Core Idea
Allylic oxidation selectively oxidizes C-H bonds at the position adjacent to a double bond (the allylic position) to alcohols or ketones. The allylic C-H is activated by the adjacent π-bond (resonance stabilization of the resulting radical or carbocation), making it more susceptible to oxidative attack than saturated alkyl C-H bonds.

## How It's Best Learned
Identify allylic positions in structures and predict oxidation products with various reagents (KMnO₄, Cr(VI), SeO₂, or bromine/light). Compare allylic oxidation selectivity to direct hydroxylation of the double bond.

## Common Misconceptions
- Confusing allylic oxidation with epoxidation or direct alkene hydroxylation; these are distinct reactions at different positions.
- Failing to recognize that the allylic C-H is activated relative to typical alkyl C-H due to resonance stabilization of intermediates.

## Questions

```yaml
- question: "Cyclohexene is treated with SeO₂ under mild conditions. Which product is primarily formed?"
  type: multiple-choice
  options:
    - "Cyclohexene oxide (an epoxide bridging across the double bond)"
    - "Cyclohexane-1,2-diol (a cis-diol from direct double-bond hydroxylation)"
    - "Cyclohex-2-en-1-ol (an allylic alcohol with the double bond intact)"
    - "Cyclohexanone (a saturated ketone with no double bond)"
  answer: 2
  explanation: "SeO₂ performs allylic oxidation — it targets the C–H bond adjacent to the double bond, not the π bond itself. The product is cyclohex-2-en-1-ol, an allylic alcohol with the original double bond preserved. Options A and B describe reactions of the double bond (epoxidation with mCPBA, dihydroxylation with OsO₄ or KMnO₄), which are entirely different reactions at a different site. Option D would require the double bond to be lost, which does not happen under these conditions."

- question: "Why are allylic C–H bonds more reactive toward oxidizing agents than typical secondary alkyl C–H bonds?"
  type: multiple-choice
  options:
    - "Allylic carbons are more electronegative due to adjacent π electrons, making them better hydrogen-bond donors"
    - "The oxidant first attacks the C=C double bond, then migrates to the adjacent carbon in a two-step process"
    - "The transition state for allylic C–H abstraction is stabilized by resonance delocalization of the resulting radical across two carbons"
    - "Allylic C–H bonds are stronger than typical secondary C–H bonds and therefore require more forcing oxidative conditions"
  answer: 2
  explanation: "The key is the stability of the allylic radical intermediate. When the allylic C–H is abstracted, the resulting radical is stabilized by resonance with the adjacent π system — the unpaired electron delocalizes over two carbons, lowering the energy of both the intermediate and the transition state leading to it. This makes allylic C–H bonds significantly weaker (~88 kcal/mol) than typical secondary C–H bonds (~99 kcal/mol). The oxidant does not attack the double bond first — that would be an electrophilic addition, a different reaction entirely."

- question: "Allylic oxidation with SeO₂ attacks the C=C double bond directly, converting it to a carbonyl group."
  type: true-false
  answer: false
  explanation: "SeO₂ performs allylic oxidation by reacting at the C–H bond adjacent to the double bond, leaving the π bond intact and producing an allylic alcohol. Reactions that directly attack the C=C bond are a different class: epoxidation (mCPBA), dihydroxylation (OsO₄), ozonolysis (O₃), and others. Confusing these reaction sites — the double bond versus the adjacent allylic C–H — is the most common misconception in this topic."

- question: "Resonance stabilization of the allylic radical lowers the activation energy for allylic C–H abstraction relative to abstraction of an ordinary secondary C–H bond."
  type: true-false
  answer: true
  explanation: "By Hammond's postulate, for an endothermic step (hydrogen abstraction), the transition state resembles the product — in this case, the carbon radical. A more stable radical (lower energy) means a lower-energy transition state, which means a lower activation barrier. The allylic radical is stabilized by resonance delocalization across the adjacent π system, making it more stable than a localized secondary alkyl radical. This stability advantage is reflected directly in the selectivity: allylic positions react preferentially under oxidative conditions."

- question: "Explain why an oxidizing reagent selectively reacts at the allylic position rather than at other C–H bonds in the same molecule."
  type: short-answer
  answer: "The allylic C–H is selectively broken because abstraction of that hydrogen produces a resonance-stabilized radical (or ionic intermediate): the unpaired electron delocalizes over the adjacent π system, spreading across two carbons. This delocalization makes allylic C–H bonds significantly weaker (~88 kcal/mol) than typical secondary C–H bonds (~99 kcal/mol). By Hammond's postulate, the more stable radical intermediate corresponds to a lower-energy transition state, so the activation barrier for allylic C–H abstraction is lower than for abstraction at other positions. The oxidant simply follows the path of least resistance."
  explanation: "The selectivity is thermodynamically and kinetically favorable for the same reason: resonance stabilization lowers both the intermediate energy and the transition-state energy. This is directly analogous to why allylic halogenation (NBS/light) is selective for the same position — the allylic radical is the most stable radical available in the molecule, so the chain-carrying radical abstracts from that position first."
```

## Explainer

From your work on free-radical halogenation, you know that hydrogen abstraction creates a carbon radical, and that the stability of that radical determines which C–H bond breaks preferentially. The **allylic position** — the carbon directly adjacent to a C=C double bond — takes this selectivity to a new level. When a hydrogen is abstracted from an allylic carbon, the resulting radical is stabilized by **resonance**: the unpaired electron delocalizes across the adjacent π system, spreading over two carbons rather than sitting on one. This resonance stabilization makes allylic C–H bonds significantly weaker (~88 kcal/mol) compared to typical secondary C–H bonds (~99 kcal/mol), meaning they break more easily under oxidative conditions.

This thermodynamic advantage translates directly into selectivity. When an oxidizing agent encounters a molecule with both allylic and ordinary alkyl C–H bonds, it preferentially attacks the allylic position because the transition state leading to the resonance-stabilized intermediate is lower in energy. Consider cyclohexene treated with selenium dioxide (SeO₂): oxidation occurs at the allylic carbon to give cyclohex-2-en-1-ol, not at the saturated carbons elsewhere in the ring. The double bond itself is untouched — the reagent targets the adjacent C–H, not the π bond.

Different reagents exploit this selectivity through different mechanisms. **SeO₂** performs an ene reaction followed by a [2,3]-sigmatropic rearrangement, delivering allylic alcohols with transposition of the double bond. **Chromium(VI) reagents** (like PCC or Jones reagent) can oxidize allylic alcohols further to enones. **Radical initiators** (such as NBS with peroxides or light) abstract the allylic hydrogen via a radical chain mechanism, replacing it with bromine — this is allylic bromination, the radical counterpart of allylic oxidation. In every case, the underlying principle is the same: the allylic position is the most reactive C–H site because resonance stabilizes whatever intermediate forms there.

The critical distinction to keep clear is between allylic oxidation and reactions of the double bond itself. Epoxidation (with mCPBA) and dihydroxylation (with OsO₄) attack the π bond directly. Allylic oxidation leaves the double bond intact and modifies the carbon next door. Recognizing which type of reaction a reagent performs — attack at the alkene or at the allylic position — is essential for predicting products in multifunctional molecules.
