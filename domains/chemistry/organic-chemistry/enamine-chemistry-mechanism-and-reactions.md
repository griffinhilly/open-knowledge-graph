---
id: enamine-chemistry-mechanism-and-reactions
title: 'Enamine Chemistry: Formation, Mechanism, and Reactions'
domain: chemistry
course: organic-chemistry
prerequisites:
- id: imine-enamine-formation
  type: hard
- id: amine-reactivity-nucleophile-base
  type: hard
- id: keto-enol-tautomerism-mechanism
  type: soft
builds-toward:
- retrosynthetic-analysis
tags:
- enamine
- secondary-amine
- nucleophile
- activated-alkene
stage: formal-systems
status: draft
---

# Enamine Chemistry: Formation, Mechanism, and Reactions

## Core Idea
Enamines form from the condensation of secondary amines with aldehydes or ketones, yielding activated C=C double bonds with increased nucleophilicity at the β-carbon. Enamines act as nucleophiles in conjugate additions and alkylations, serving as masked enolates that avoid over-alkylation. The mechanism mirrors imine formation but with dehydration producing the C=C rather than C=N.

## Explainer

You have already seen how secondary amines react with aldehydes and ketones to form enamines through the imine-enamine formation pathway. Now the question becomes: why are enamines useful, and what can you do with them? The answer lies in understanding enamines as **masked enolates** — nucleophilic species that react at the alpha carbon of the original carbonyl, but with better selectivity than enolates themselves.

Recall from keto-enol tautomerism that enolates are powerful nucleophiles at the alpha carbon, but they suffer from a practical problem: they can be alkylated more than once, because the product of monoalkylation is still acidic at the alpha position and can form another enolate. Enamines solve this problem elegantly. In an enamine, the nitrogen lone pair donates electron density into the C=C double bond through **resonance**, making the **beta carbon** (the carbon alpha to the original carbonyl) strongly nucleophilic. When this carbon attacks an electrophile — an alkyl halide in an SN2 reaction or a Michael acceptor in a conjugate addition — the nitrogen becomes positively charged (an iminium ion). This iminium ion cannot form another enamine without being hydrolyzed first, which means the reaction stops cleanly at monoalkylation. This self-limiting behavior is the key advantage over direct enolate chemistry.

The **Stork enamine synthesis** is the classic application of this reactivity. The procedure has three steps: (1) form the enamine by condensing a secondary amine (typically pyrrolidine, morpholine, or piperidine) with a ketone under acid catalysis with removal of water; (2) react the enamine with an electrophile (alkyl halide or α,β-unsaturated carbonyl compound), which produces an iminium salt; (3) hydrolyze the iminium salt under mildly acidic aqueous conditions to regenerate the carbonyl group and release the amine. The net result is alkylation at the alpha position of the original ketone, achieved with monoalkylation selectivity that would be difficult or impossible using enolate chemistry directly.

Enamines also participate in **conjugate (Michael) additions** with particular efficiency. The soft nucleophilic character of the enamine beta carbon pairs well with the soft electrophilic character of a Michael acceptor's beta carbon. After conjugate addition and hydrolysis, you have achieved a 1,5-dicarbonyl product — the same type of product that a Michael reaction between an enolate and an enone would give, but again with cleaner selectivity. Understanding enamine chemistry gives you a versatile alternative to enolate-based strategies, and recognizing when to use enamines versus enolates is a key judgment call in retrosynthetic planning.
