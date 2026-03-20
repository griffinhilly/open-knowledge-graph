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
stage: advanced
status: draft
---

# Reduction of Carbonyls to Alcohols

## Core Idea
Aldehydes are reduced to primary alcohols; ketones are reduced to secondary alcohols. Common reducing agents include LiAlH₄ (powerful, non-selective), NaBH₄ (milder, selective for carbonyls over esters), and Dibal-H (which can selectively reduce esters/acids at low temperature). The reactivity and functional group tolerance vary significantly among reagents.

## How It's Best Learned
Predict the products of reduction with LiAlH₄, NaBH₄, and Dibal-H on various carbonyl-containing molecules. Understand which functional groups are reduced by each agent and when to use each.

## Common Misconceptions
- Assuming LiAlH₄ and NaBH₄ reduce all carbonyls identically; NaBH₄ does not reduce carboxylic acids or esters under normal conditions.
- Forgetting that Dibal-H is selective for aldehydes/ketones over esters at low temperature and requires careful stoichiometry.

## Explainer

You know that a carbonyl group (C=O) is polarized: oxygen is more electronegative, making the carbon electrophilic and the oxygen nucleophilic. **Reduction of a carbonyl to an alcohol** is fundamentally a nucleophilic addition — a hydride ion (H⁻) attacks the electrophilic carbon, breaking the π bond of C=O and forming a new C–H bond. After aqueous workup, the oxygen picks up a proton, and the result is an alcohol. An aldehyde (one R group, one H) gives a **primary alcohol**; a ketone (two R groups) gives a **secondary alcohol**.

The three workhorse reducing agents differ in how aggressively they deliver hydride. **Lithium aluminum hydride** (LiAlH₄) is the most powerful — it reduces virtually every carbonyl-containing functional group: aldehydes, ketones, esters, carboxylic acids, and even amides. Think of it as a sledgehammer. **Sodium borohydride** (NaBH₄) is gentler — it reduces aldehydes and ketones efficiently but leaves esters and carboxylic acids untouched under standard conditions. This selectivity makes NaBH₄ invaluable when a molecule contains both a ketone and an ester and you want to reduce only the ketone. The difference comes down to the metal: aluminum is more electropositive than boron, making its hydrides more reactive and less discriminating.

**Diisobutylaluminum hydride** (DIBAL-H) occupies a unique niche. At low temperatures (−78°C) and with exactly one equivalent, DIBAL-H can reduce an ester to an aldehyde — stopping at the halfway point rather than going all the way to an alcohol. This is possible because the first addition creates a stable tetrahedral aluminum alkoxide intermediate that does not collapse further at low temperature. At higher temperatures or with excess reagent, DIBAL-H reduces esters all the way to primary alcohols, behaving more like LiAlH₄.

Choosing the right reagent is a matter of matching selectivity to the substrate. If you need to reduce everything, use LiAlH₄. If you need to reduce an aldehyde or ketone in the presence of an ester, use NaBH₄. If you need to convert an ester to an aldehyde without over-reducing, use DIBAL-H at −78°C. Memorizing reagent names without understanding their selectivity is a trap — what matters is knowing *why* each reagent stops where it does, which comes back to the reactivity of the hydride source and the stability of the intermediate.
