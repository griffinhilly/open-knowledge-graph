---
id: organometallic-grignard-organolithium
title: Grignard and Organolithium Reagents in Synthesis
domain: chemistry
course: organic-chemistry
prerequisites:
- id: grignard-reagent
  type: soft
- id: nucleophile-electrophile-definitions
  type: hard
- id: carbonyl-reduction-to-alcohols
  type: soft
builds-toward:
- wittig-reaction-mechanism
tags:
- organometallic
- grignard
- organolithium
- nucleophile
- synthesis
stage: formal-systems
status: draft
---

# Grignard and Organolithium Reagents in Synthesis

## Core Idea
Grignard (RMgX) and organolithium (RLi) reagents are strong carbon nucleophiles and bases formed from alkyl halides. They react with carbonyl electrophiles (aldehydes, ketones, esters) and CO₂ to form C-C bonds. RLi is more reactive and less selective than RMgX. Both require anhydrous, aprotic conditions and are incompatible with protic functional groups.

## How It's Best Learned
Draw mechanisms for Grignard additions to various carbonyls. Compare the reactivity of RMgX and RLi. Identify functional groups that will interfere with organometallic reagents.

## Common Misconceptions
- Assuming Grignards and RLi can be used in protic solvents; they react with water and require aprotic conditions.
- Forgetting that organometallic reagents are strong bases and nucleophiles, reacting with multiple functional group types beyond carbonyls.

## Explainer

You already know that nucleophiles attack electrophiles — that electron-rich species seek out electron-poor centers. Grignard and organolithium reagents take this idea to its most powerful extreme by turning carbon itself into the nucleophile. When an alkyl halide like CH₃Br reacts with magnesium metal in dry ether, the result is CH₃MgBr — a **Grignard reagent** where the carbon-magnesium bond is so polarized that the carbon carries a strong partial negative charge. It behaves, for all practical purposes, as a carbanion: a carbon nucleophile ready to attack electrophilic carbon centers. **Organolithium reagents** (like CH₃Li, formed from alkyl halides and lithium metal) are even more reactive because the C–Li bond is more ionic, making the carbon an even stronger nucleophile and base.

The signature reaction of these reagents is **nucleophilic addition to carbonyls**. When a Grignard reagent attacks formaldehyde (HCHO), you get a primary alcohol after acidic workup. Attack on any other aldehyde yields a secondary alcohol. Attack on a ketone yields a tertiary alcohol. Attack on an ester proceeds through two additions (since the first addition produces a ketone intermediate) to give a tertiary alcohol where two of the substituents come from the Grignard. These transformations are among the most important C–C bond-forming reactions in organic synthesis, because they let you build up a carbon skeleton one piece at a time from simpler starting materials.

The critical constraint is **functional group compatibility**. Both Grignard and organolithium reagents are destroyed by any protic source — water, alcohols, amines, carboxylic acids, even terminal alkynes. They are also strong enough bases to deprotonate many weakly acidic functional groups. This means you cannot prepare or use these reagents in the presence of –OH, –NH, or –COOH groups unless those groups are protected first. Solvents must be rigorously dried and aprotic; diethyl ether and THF are standard choices. Forgetting this incompatibility is the single most common source of failed Grignard reactions.

The difference between RMgX and RLi matters in practice. Organolithium reagents are more reactive and less selective — they react faster but are harder to control, and they can add to functional groups that Grignard reagents leave alone (such as certain amides). When you need a powerful, indiscriminate carbon nucleophile, RLi is the tool. When you need more selectivity or milder conditions, RMgX is preferred. Choosing between them is a judgment call that depends on the substrate's other functional groups and the desired product, and it is a recurring decision in synthetic planning.
