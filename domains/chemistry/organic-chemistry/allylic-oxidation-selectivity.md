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
status: draft
---

# Allylic Oxidation and Selectivity

## Core Idea
Allylic oxidation selectively oxidizes C-H bonds at the position adjacent to a double bond (the allylic position) to alcohols or ketones. The allylic C-H is activated by the adjacent π-bond (resonance stabilization of the resulting radical or carbocation), making it more susceptible to oxidative attack than saturated alkyl C-H bonds.

## How It's Best Learned
Identify allylic positions in structures and predict oxidation products with various reagents (KMnO₄, Cr(VI), SeO₂, or bromine/light). Compare allylic oxidation selectivity to direct hydroxylation of the double bond.

## Common Misconceptions
- Confusing allylic oxidation with epoxidation or direct alkene hydroxylation; these are distinct reactions at different positions.
- Failing to recognize that the allylic C-H is activated relative to typical alkyl C-H due to resonance stabilization of intermediates.

## Explainer

From your work on free-radical halogenation, you know that hydrogen abstraction creates a carbon radical, and that the stability of that radical determines which C–H bond breaks preferentially. The **allylic position** — the carbon directly adjacent to a C=C double bond — takes this selectivity to a new level. When a hydrogen is abstracted from an allylic carbon, the resulting radical is stabilized by **resonance**: the unpaired electron delocalizes across the adjacent π system, spreading over two carbons rather than sitting on one. This resonance stabilization makes allylic C–H bonds significantly weaker (~88 kcal/mol) compared to typical secondary C–H bonds (~99 kcal/mol), meaning they break more easily under oxidative conditions.

This thermodynamic advantage translates directly into selectivity. When an oxidizing agent encounters a molecule with both allylic and ordinary alkyl C–H bonds, it preferentially attacks the allylic position because the transition state leading to the resonance-stabilized intermediate is lower in energy. Consider cyclohexene treated with selenium dioxide (SeO₂): oxidation occurs at the allylic carbon to give cyclohex-2-en-1-ol, not at the saturated carbons elsewhere in the ring. The double bond itself is untouched — the reagent targets the adjacent C–H, not the π bond.

Different reagents exploit this selectivity through different mechanisms. **SeO₂** performs an ene reaction followed by a [2,3]-sigmatropic rearrangement, delivering allylic alcohols with transposition of the double bond. **Chromium(VI) reagents** (like PCC or Jones reagent) can oxidize allylic alcohols further to enones. **Radical initiators** (such as NBS with peroxides or light) abstract the allylic hydrogen via a radical chain mechanism, replacing it with bromine — this is allylic bromination, the radical counterpart of allylic oxidation. In every case, the underlying principle is the same: the allylic position is the most reactive C–H site because resonance stabilizes whatever intermediate forms there.

The critical distinction to keep clear is between allylic oxidation and reactions of the double bond itself. Epoxidation (with mCPBA) and dihydroxylation (with OsO₄) attack the π bond directly. Allylic oxidation leaves the double bond intact and modifies the carbon next door. Recognizing which type of reaction a reagent performs — attack at the alkene or at the allylic position — is essential for predicting products in multifunctional molecules.
