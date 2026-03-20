---
id: claisen-condensation-mechanism
title: Claisen Condensation and Self-Condensation Reactions
domain: chemistry
course: organic-chemistry
prerequisites:
- id: enolate-alkylation-malonic-ester
  type: hard
- id: nucleophilic-acyl-substitution
  type: hard
builds-toward:
- aldol-reaction
tags:
- condensation
- claisen
- ester
- enolate
- synthesis
stage: advanced
status: draft
---

# Claisen Condensation and Self-Condensation Reactions

## Core Idea
The Claisen condensation is a nucleophilic acyl substitution in which an ester enolate attacks the carbonyl carbon of another ester, forming a β-keto ester. Base deprotonates the α-CH of one ester to form the enolate, which attacks the C=O of a second ester, displacing the alkoxide and generating a C-C bond. Excess base deprotonates the product, driving the equilibrium forward.

## How It's Best Learned
Draw the enolate formation and acyl substitution mechanism, showing the tetrahedral intermediate and alkoxide departure. Understand why excess base is essential.

## Common Misconceptions
- Confusing Claisen with aldol; Claisen uses esters while aldol typically uses aldehydes/ketones.
- Forgetting that the product's acidity (from the α-H of the β-keto ester) is essential for its deprotonation by excess base, which drives the reaction.

## Explainer

You have already seen enolates attack electrophilic carbons in alkylation reactions (like the malonic ester synthesis), and you know that esters undergo nucleophilic acyl substitution — a nucleophile attacks the carbonyl carbon, forms a tetrahedral intermediate, and then a leaving group departs. The **Claisen condensation** combines these two ideas: an ester enolate acts as the nucleophile, and another ester molecule acts as the electrophile, forming a new carbon-carbon bond and producing a **β-keto ester**.

Here is the mechanism step by step. A strong base (typically an alkoxide matching the ester's OR group, like sodium ethoxide for ethyl esters) deprotonates the **α-carbon** of one ester molecule. This generates a resonance-stabilized enolate. The enolate carbon then attacks the carbonyl carbon of a second ester molecule, forming a tetrahedral intermediate. The alkoxide leaving group (–OR) is expelled, regenerating the carbonyl and completing the acyl substitution. The product is a β-keto ester — an ester with a ketone carbonyl at the β position. Notice this is fundamentally different from an aldol reaction: in an aldol, the nucleophile attacks an aldehyde or ketone and the leaving group does not depart; in a Claisen, the nucleophile attacks an ester and the alkoxide leaves. The aldol gives a β-hydroxy carbonyl; the Claisen gives a β-keto ester.

The thermodynamic trick that makes the Claisen work is the final deprotonation step. The equilibrium for the acyl substitution alone is not strongly favorable. But the β-keto ester product has an unusually acidic α-hydrogen (pKa ≈ 11) because the resulting anion is stabilized by two flanking carbonyls. Excess base deprotonates this position, pulling the product out of equilibrium and driving the reaction forward according to Le Chatelier's principle. This is why at least one full equivalent of base is required — it is consumed in this deprotonation step. Acidic workup at the end reprotonates the product.

In the **self-condensation** version, two identical ester molecules react with each other. In a **crossed Claisen**, two different esters are used, but this only works cleanly when one ester lacks α-hydrogens (like ethyl benzoate or ethyl formate) so it can only serve as the electrophile. If both esters have α-hydrogens, you get a mixture of four possible products — a synthetically useless outcome. Recognizing which ester can form the enolate and which serves as the electrophile is the key strategic skill for planning Claisen-based syntheses.
