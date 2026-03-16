---
id: reduction-reactions-organic
title: Reduction Reactions in Organic Chemistry
domain: chemistry
course: organic-chemistry
prerequisites:
- id: carbonyl-chemistry-intro
  type: hard
builds-toward:
- retrosynthetic-analysis
tags:
- reduction
- NaBH4
- LiAlH4
- catalytic hydrogenation
- selectivity
- hydride
stage: formal-systems
status: draft
---
# Reduction Reactions in Organic Chemistry

## Core Idea
Reduction of organic compounds most commonly means adding hydrogen (H2) or delivering hydride (H-) to a functional group to lower its oxidation state. NaBH4 is a mild reducing agent that selectively reduces aldehydes and ketones to alcohols without attacking esters or carboxylic acids. LiAlH4 is a powerful, non-selective reducing agent that reduces aldehydes, ketones, esters, carboxylic acids, amides, and epoxides. Catalytic hydrogenation (H2 with Pd, Pt, or Ni catalyst) reduces carbon-carbon pi bonds (alkenes, alkynes) and can also reduce carbonyls under forcing conditions. Choosing the right reagent for selective reduction is a cornerstone of multi-step synthesis.

## How It's Best Learned
Build a selectivity table: rows are functional groups (aldehyde, ketone, ester, acid, amide, alkene), columns are reagents (NaBH4, LiAlH4, H2/Pd). Mark which reagent reduces which group. Then work backward from a target molecule: if you need to reduce a ketone in the presence of an ester, which reagent preserves the ester? Practice drawing the hydride delivery mechanism for NaBH4 and LiAlH4 addition to a carbonyl.

## Common Misconceptions
- NaBH4 and LiAlH4 are not interchangeable — using LiAlH4 where NaBH4 is called for will over-reduce other functional groups in the molecule.
- Catalytic hydrogenation is a syn addition (both hydrogens add to the same face of the double bond); this stereospecificity matters in cyclic systems.
- LiAlH4 reacts violently with water and must be used in anhydrous ether; aqueous workup is added only after the reaction is complete.

## Explainer

From your work on carbonyl chemistry, you know that the C=O double bond is polarized — carbon is electrophilic and oxygen is nucleophilic. **Reduction** in organic chemistry exploits this polarity by delivering a hydride ion (H⁻) to the electrophilic carbonyl carbon, breaking the pi bond and forming a new C–H bond. The oxygen picks up a proton during aqueous workup, yielding an alcohol. This is the conceptual reverse of oxidation: you are climbing down the oxidation-state ladder, decreasing the number of bonds between carbon and oxygen.

The two most important hydride reagents form a natural pair organized by selectivity. **NaBH4** (sodium borohydride) is the mild, selective option. It delivers hydride to aldehydes and ketones but leaves esters, carboxylic acids, and amides untouched. Why the selectivity? NaBH4 is a relatively weak nucleophile — it can attack the highly electrophilic carbon of an aldehyde or ketone carbonyl, but esters and acids have resonance stabilization that makes their carbonyl carbon less electrophilic. NaBH4 can even be used in protic solvents like methanol or ethanol, making it experimentally convenient. **LiAlH4** (lithium aluminum hydride) is the brute-force alternative. It is a much stronger nucleophile and reducing agent, capable of reducing virtually every carbonyl-containing functional group: aldehydes, ketones, esters, carboxylic acids, amides, and even epoxides. The tradeoff is that it is non-selective and violently reactive with water, requiring strictly anhydrous conditions (dry ether or THF) and careful quenching.

**Catalytic hydrogenation** offers a fundamentally different mechanism. Instead of delivering hydride from a reagent, H₂ gas adsorbs onto a metal catalyst surface (Pd, Pt, or Ni), and both hydrogen atoms add across a pi bond in a single **syn addition** — both hydrogens land on the same face. This is the go-to method for reducing C=C double bonds (alkenes to alkanes) and C≡C triple bonds (alkynes to alkenes or alkanes, depending on conditions). Catalytic hydrogenation generally does not reduce isolated carbonyls under mild conditions, which gives you orthogonal selectivity: use H₂/Pd to reduce a double bond while leaving a ketone intact, or use NaBH4 to reduce a ketone while leaving a double bond intact.

The practical takeaway is a decision tree for synthesis problems. Ask: what functional group needs to be reduced, and what other functional groups must survive? If you need to reduce only a ketone in a molecule that also contains an ester, NaBH4 is your answer. If you need to reduce an ester all the way to an alcohol, only LiAlH4 will do the job. If you need to saturate a double bond without touching a carbonyl, catalytic hydrogenation is the right tool. This selectivity logic — matching reagent capability to the functional group landscape of your molecule — is exactly the reasoning you will use when planning multi-step syntheses.
