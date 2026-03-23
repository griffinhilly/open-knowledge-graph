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

## Questions

```yaml
- question: "A molecule contains both a ketone and an ester. You want to reduce only the ketone to an alcohol while leaving the ester intact. Which reagent should you use?"
  type: multiple-choice
  options:
    - "LiAlH4 — it is the most powerful reducing agent and will cleanly reduce the ketone"
    - "NaBH4 — it reduces aldehydes and ketones but is too weak to reduce esters"
    - "H2/Pd — catalytic hydrogenation selectively reduces ketones over esters"
    - "Either LiAlH4 or NaBH4 will work, since both reduce ketones"
  answer: 1
  explanation: "NaBH4 is selective — it reduces aldehydes and ketones but leaves esters untouched because the ester carbonyl carbon is less electrophilic due to resonance stabilization from the alkoxy oxygen. LiAlH4 would reduce both the ketone AND the ester, destroying selectivity. H2/Pd reduces C=C double bonds, not isolated carbonyls under mild conditions. The key skill in synthesis is matching reagent capability to what must survive, not just what must react."

- question: "Catalytic hydrogenation (H2/Pd) adds two hydrogens across an alkene in a cyclic system. What does 'syn addition' mean for the stereochemical outcome?"
  type: multiple-choice
  options:
    - "Both hydrogens add to opposite faces of the double bond, giving a trans product"
    - "Both hydrogens add to the same face of the double bond simultaneously"
    - "Only one hydrogen adds at a time, proceeding through a radical intermediate"
    - "Syn addition means the reaction is reversible — hydrogens can be removed under the same conditions"
  answer: 1
  explanation: "Syn addition means both hydrogens are delivered to the same face (same side) of the pi bond simultaneously, as they adsorb together onto the metal catalyst surface. In cyclic systems this produces cis-substituted products from cis-accessible substrates. Anti addition (opposite faces) is a different mechanism seen in reactions like bromine addition to alkenes. The stereochemical outcome of catalytic hydrogenation is not random — syn delivery is a mechanistic consequence of the surface adsorption process."

- question: "NaBH4 can be used in methanol or ethanol as the reaction solvent."
  type: true-false
  answer: true
  explanation: "Unlike LiAlH4, NaBH4 is mild enough to tolerate protic solvents like methanol and ethanol. It reacts slowly with water/alcohols compared to its rate of ketone/aldehyde reduction, making aqueous or alcoholic conditions practical. LiAlH4 reacts violently with protic solvents and requires strictly anhydrous ether (THF, Et2O). This difference in experimental handling is a practical consequence of the difference in hydride-donating strength."

- question: "LiAlH4 is impractical for reducing esters because the reaction is too slow — that is why NaBH4 is preferred when possible."
  type: true-false
  answer: false
  explanation: "LiAlH4 does reduce esters (to primary alcohols) and does so vigorously, not slowly. The reason to prefer NaBH4 when it suffices is not speed — it is selectivity. If a molecule contains both an ester and a ketone, LiAlH4 attacks both, destroying the functional group you wanted to preserve. NaBH4 is preferred for its chemoselectivity. LiAlH4's limitation is over-reduction and incompatibility with protic solvents, not insufficient reactivity with esters."

- question: "A target molecule contains an alkene and a ketone. You need to saturate the alkene without touching the ketone. Identify the correct reagent and explain the selectivity principle."
  type: short-answer
  answer: "H2/Pd (catalytic hydrogenation) selectively reduces the alkene to an alkane while leaving the ketone intact under mild conditions."
  explanation: "H2/Pd operates through surface adsorption at C=C pi bonds and does not reduce isolated ketone carbonyls under mild conditions. NaBH4 would do the opposite: reduce the ketone and leave the alkene untouched. This is orthogonal selectivity — H2/Pd and NaBH4 target different functional group classes, allowing a chemist to choose which group to reduce. Synthesis planning depends on this 'selectivity table' logic: identify every functional group present, decide which must react and which must survive, then choose the reagent whose selectivity profile matches."
```

## Explainer

From your work on carbonyl chemistry, you know that the C=O double bond is polarized — carbon is electrophilic and oxygen is nucleophilic. **Reduction** in organic chemistry exploits this polarity by delivering a hydride ion (H⁻) to the electrophilic carbonyl carbon, breaking the pi bond and forming a new C–H bond. The oxygen picks up a proton during aqueous workup, yielding an alcohol. This is the conceptual reverse of oxidation: you are climbing down the oxidation-state ladder, decreasing the number of bonds between carbon and oxygen.

The two most important hydride reagents form a natural pair organized by selectivity. **NaBH4** (sodium borohydride) is the mild, selective option. It delivers hydride to aldehydes and ketones but leaves esters, carboxylic acids, and amides untouched. Why the selectivity? NaBH4 is a relatively weak nucleophile — it can attack the highly electrophilic carbon of an aldehyde or ketone carbonyl, but esters and acids have resonance stabilization that makes their carbonyl carbon less electrophilic. NaBH4 can even be used in protic solvents like methanol or ethanol, making it experimentally convenient. **LiAlH4** (lithium aluminum hydride) is the brute-force alternative. It is a much stronger nucleophile and reducing agent, capable of reducing virtually every carbonyl-containing functional group: aldehydes, ketones, esters, carboxylic acids, amides, and even epoxides. The tradeoff is that it is non-selective and violently reactive with water, requiring strictly anhydrous conditions (dry ether or THF) and careful quenching.

**Catalytic hydrogenation** offers a fundamentally different mechanism. Instead of delivering hydride from a reagent, H₂ gas adsorbs onto a metal catalyst surface (Pd, Pt, or Ni), and both hydrogen atoms add across a pi bond in a single **syn addition** — both hydrogens land on the same face. This is the go-to method for reducing C=C double bonds (alkenes to alkanes) and C≡C triple bonds (alkynes to alkenes or alkanes, depending on conditions). Catalytic hydrogenation generally does not reduce isolated carbonyls under mild conditions, which gives you orthogonal selectivity: use H₂/Pd to reduce a double bond while leaving a ketone intact, or use NaBH4 to reduce a ketone while leaving a double bond intact.

The practical takeaway is a decision tree for synthesis problems. Ask: what functional group needs to be reduced, and what other functional groups must survive? If you need to reduce only a ketone in a molecule that also contains an ester, NaBH4 is your answer. If you need to reduce an ester all the way to an alcohol, only LiAlH4 will do the job. If you need to saturate a double bond without touching a carbonyl, catalytic hydrogenation is the right tool. This selectivity logic — matching reagent capability to the functional group landscape of your molecule — is exactly the reasoning you will use when planning multi-step syntheses.
