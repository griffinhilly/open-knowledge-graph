---
id: carbonyl-reduction-to-alcohols
title: Reduction of Carbonyls to Alcohols
domain: chemistry
course: organic-chemistry
prerequisites:
- id: reduction-reactions-organic
  type: soft
- id: nucleophile-electrophile-definitions
  type: hard
builds-toward:
- selectivity-reduction-techniques
- organometallic-grignard-organolithium
tags:
- reduction
- carbonyl
- alcohol
- hydride
stage: formal-systems
status: validated
---

# Reduction of Carbonyls to Alcohols

## Core Idea
Aldehydes are reduced to primary alcohols; ketones are reduced to secondary alcohols. Common reducing agents include LiAlH₄ (powerful, non-selective), NaBH₄ (milder, selective for carbonyls over esters), and Dibal-H (which can selectively reduce esters/acids at low temperature). The reactivity and functional group tolerance vary significantly among reagents.

## How It's Best Learned
Predict the products of reduction with LiAlH₄, NaBH₄, and Dibal-H on various carbonyl-containing molecules. Understand which functional groups are reduced by each agent and when to use each.

## Common Misconceptions
- Assuming LiAlH₄ and NaBH₄ reduce all carbonyls identically; NaBH₄ does not reduce carboxylic acids or esters under normal conditions.
- Forgetting that Dibal-H is selective for aldehydes/ketones over esters at low temperature and requires careful stoichiometry.

## Questions

```yaml
- question: "A molecule contains both a ketone and an ester group. You want to reduce only the ketone to a secondary alcohol without touching the ester. Which reagent is the correct choice?"
  type: multiple-choice
  options:
    - "LiAlH₄ in THF, then aqueous workup"
    - "NaBH₄ in methanol, then aqueous workup"
    - "DIBAL-H at −78°C in hexane, then aqueous workup"
    - "H₂ over Pd/C catalyst"
  answer: 1
  explanation: "NaBH₄ is the correct choice because it reduces aldehydes and ketones efficiently but does not reduce esters under standard conditions. LiAlH₄ would reduce both the ketone and the ester (it reduces virtually all carbonyl-containing groups). DIBAL-H at −78°C selectively reduces esters — the opposite selectivity from what is needed here. H₂/Pd is used for alkene hydrogenation or debenzylation, not for reducing isolated carbonyls. Matching reagent selectivity to the substrate is the core skill of this topic."

- question: "DIBAL-H is added to an ester at −78°C with exactly one equivalent. What is the expected product after aqueous workup?"
  type: multiple-choice
  options:
    - "A secondary alcohol, because the ester is fully reduced"
    - "A carboxylic acid, because the hydride adds to the carbonyl and water re-oxidizes it"
    - "An aldehyde, because the intermediate aluminum alkoxide is stable at low temperature and collapses to an aldehyde on workup"
    - "No reaction — DIBAL-H does not react with esters"
  answer: 2
  explanation: "DIBAL-H at −78°C with one equivalent reduces an ester to an aldehyde via a key mechanistic feature: the first hydride addition produces a tetrahedral aluminum alkoxide intermediate (an aminol-type complex) that is kinetically stable at low temperature. It does not collapse to the aldehyde until warm aqueous workup, at which point the aldehyde is released. At higher temperatures or with excess DIBAL-H, this intermediate collapses and is reduced further to a primary alcohol. The temperature and stoichiometry control is critical — this is a classic example of kinetic vs. thermodynamic control of a reaction outcome."

- question: "LiAlH₄ and NaBH₄ both deliver hydride (H⁻) to carbonyl carbons, so they reduce the same set of functional groups."
  type: true-false
  answer: false
  explanation: "Although both reagents deliver hydride via the same fundamental mechanism (nucleophilic addition of H⁻ to the electrophilic carbonyl carbon), their reactivity differs dramatically. LiAlH₄ reduces aldehydes, ketones, esters, carboxylic acids, and amides. NaBH₄ selectively reduces aldehydes and ketones but leaves esters and carboxylic acids intact under standard conditions. The difference stems from the metal: aluminum is more electropositive than boron, making the Al–H bond more polarized and the hydride more nucleophilic and reactive. Boron's more covalent character makes NaBH₄ a gentler, more selective reagent."

- question: "The reduction of a ketone by NaBH₄ produces a secondary alcohol because the hydride adds to the less hindered face of the carbonyl."
  type: true-false
  answer: false
  explanation: "The statement correctly identifies the product (secondary alcohol from ketone) but gives the wrong reason for *why* it is secondary. A ketone gives a secondary alcohol because the carbonyl carbon bears two carbon substituents (R groups): after hydride addition and protonation, the carbon has H, OH, and two R groups — the definition of a secondary alcohol. The facial selectivity (which face the hydride attacks) determines *stereochemistry* of the product (R vs. S configuration), not the alcohol class. Facial selectivity is governed by steric bulk and is a separate consideration from the primary/secondary classification."

- question: "Explain why choosing between LiAlH₄ and NaBH₄ matters in synthesis, and how you would decide which to use for a given substrate."
  type: short-answer
  answer: "The choice hinges on selectivity: LiAlH₄ is a powerful, non-selective hydride source that reduces virtually every carbonyl-containing functional group (aldehydes, ketones, esters, acids, amides), while NaBH₄ selectively reduces aldehydes and ketones and leaves esters and carboxylic acids intact. If the target molecule has only an aldehyde or ketone, either reagent works, but NaBH₄ is often preferred for safety and ease of handling. If the molecule contains both a ketone and an ester and only the ketone must be reduced, NaBH₄ is the correct choice because LiAlH₄ would non-selectively reduce both."
  explanation: "This reagent selection logic is an example of chemoselectivity — choosing a reagent that reacts with one functional group in the presence of another. The underlying principle is that reactivity differences stem from the polarization of the M–H bond: the more electropositive the metal (Al vs. B), the more reactive the hydride. Mastering this means understanding *why* selectivity exists, not just memorizing 'NaBH₄ doesn't reduce esters' as an isolated fact."
```

## Explainer

You know that a carbonyl group (C=O) is polarized: oxygen is more electronegative, making the carbon electrophilic and the oxygen nucleophilic. **Reduction of a carbonyl to an alcohol** is fundamentally a nucleophilic addition — a hydride ion (H⁻) attacks the electrophilic carbon, breaking the π bond of C=O and forming a new C–H bond. After aqueous workup, the oxygen picks up a proton, and the result is an alcohol. An aldehyde (one R group, one H) gives a **primary alcohol**; a ketone (two R groups) gives a **secondary alcohol**.

The three workhorse reducing agents differ in how aggressively they deliver hydride. **Lithium aluminum hydride** (LiAlH₄) is the most powerful — it reduces virtually every carbonyl-containing functional group: aldehydes, ketones, esters, carboxylic acids, and even amides. Think of it as a sledgehammer. **Sodium borohydride** (NaBH₄) is gentler — it reduces aldehydes and ketones efficiently but leaves esters and carboxylic acids untouched under standard conditions. This selectivity makes NaBH₄ invaluable when a molecule contains both a ketone and an ester and you want to reduce only the ketone. The difference comes down to the metal: aluminum is more electropositive than boron, making its hydrides more reactive and less discriminating.

**Diisobutylaluminum hydride** (DIBAL-H) occupies a unique niche. At low temperatures (−78°C) and with exactly one equivalent, DIBAL-H can reduce an ester to an aldehyde — stopping at the halfway point rather than going all the way to an alcohol. This is possible because the first addition creates a stable tetrahedral aluminum alkoxide intermediate that does not collapse further at low temperature. At higher temperatures or with excess reagent, DIBAL-H reduces esters all the way to primary alcohols, behaving more like LiAlH₄.

Choosing the right reagent is a matter of matching selectivity to the substrate. If you need to reduce everything, use LiAlH₄. If you need to reduce an aldehyde or ketone in the presence of an ester, use NaBH₄. If you need to convert an ester to an aldehyde without over-reducing, use DIBAL-H at −78°C. Memorizing reagent names without understanding their selectivity is a trap — what matters is knowing *why* each reagent stops where it does, which comes back to the reactivity of the hydride source and the stability of the intermediate.
