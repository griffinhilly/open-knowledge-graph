---
id: relative-reactivity-carboxylic-acid-derivatives
title: Relative Reactivity of Carboxylic Acid Derivatives
domain: chemistry
course: organic-chemistry
prerequisites:
- id: carboxylic-acid-derivatives-esters-amides-acyl-chlorides
  type: hard
- id: nucleophilic-acyl-substitution
  type: hard
builds-toward:
- retrosynthetic-analysis
tags:
- reactivity-trends
- acid-derivatives
- acyl-chloride
- ester
- amide
stage: formal-systems
status: draft
---

# Relative Reactivity of Carboxylic Acid Derivatives

## Core Idea
Carboxylic acid derivatives follow a reactivity hierarchy in nucleophilic acyl substitution: acyl chlorides > anhydrides > esters > amides (in order of decreasing reactivity). This trend reflects the stability of the tetrahedral intermediate and the quality of the leaving group. Amides are the least reactive because nitrogen's strong electron donation stabilizes the intermediate, while chlorine is the best leaving group.

## Explainer

From your study of nucleophilic acyl substitution, you know the general mechanism: a nucleophile attacks the electrophilic carbonyl carbon, forming a tetrahedral intermediate, and then a leaving group departs to regenerate the carbonyl. The question this topic answers is: why do acyl chlorides react explosively with water while amides can sit in aqueous solution for days without hydrolyzing? The answer comes down to two reinforcing factors — leaving group ability and resonance stabilization of the starting material.

Consider the **leaving group trend** first. In acyl chlorides, the leaving group is Cl⁻ — a weak base and excellent leaving group, happy to depart with the bonding electrons. In anhydrides, the leaving group is a carboxylate (RCO₂⁻), still a reasonably stable anion. In esters, it is an alkoxide (RO⁻) — a stronger base and poorer leaving group. In amides, the leaving group would be an amide ion (NH₂⁻ or NR₂⁻) — an extremely strong base that resists departure. The better the leaving group, the faster the tetrahedral intermediate collapses to products.

Now consider **resonance stabilization** of the starting material. Every carboxylic acid derivative has a lone pair on the atom attached to the carbonyl (the heteroatom). This lone pair can donate into the carbonyl's pi system, stabilizing the ground state and reducing the electrophilicity of the carbonyl carbon. Nitrogen is the best electron donor of the group — its lone pair overlaps strongly with the carbonyl pi* orbital, giving amides substantial double-bond character in the C–N bond (roughly 40% pi character). This makes the amide carbonyl much less electrophilic than you might expect. Oxygen in esters donates less effectively, and chlorine in acyl chlorides barely donates at all because its 3p orbital overlaps poorly with carbon's 2p. So acyl chlorides have the most electrophilic carbonyl and the best leaving group — both factors drive high reactivity.

The practical consequence is that you can only convert derivatives **downhill** in the reactivity series without forcing conditions. An acyl chloride can be converted to an anhydride, ester, or amide simply by adding the appropriate nucleophile. But you cannot convert an amide to an ester just by adding an alcohol — the amide is too stable and NH₂⁻ is too poor a leaving group. To go "uphill" in reactivity, you need activating reagents or harsh conditions. This reactivity ladder is central to retrosynthetic planning: when you see an amide target, you know you can build it from an acyl chloride or ester, but not the reverse without special chemistry.
