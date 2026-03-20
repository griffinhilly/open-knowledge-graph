---
id: substitution-vs-elimination
title: Substitution vs Elimination Competition
domain: chemistry
course: organic-chemistry
prerequisites:
- id: sn2-reaction
  type: hard
- id: sn1-reaction
  type: hard
- id: e2-elimination
  type: hard
- id: e1-elimination
  type: hard
builds-toward:
- retrosynthetic-analysis
tags:
- SN1
- SN2
- E1
- E2
- competition
- substrate
- base strength
- solvent effects
stage: advanced
status: draft
---
# Substitution vs Elimination Competition

## Core Idea
When a substrate bearing a leaving group encounters a nucleophile or base, four pathways compete: SN2, SN1, E2, and E1. The dominant pathway depends on the interplay of substrate class (methyl, primary, secondary, tertiary), nucleophile/base strength and bulk, solvent polarity, and temperature. Strong, unhindered nucleophiles in polar aprotic solvents favor SN2 on primary substrates; strong, bulky bases favor E2; tertiary substrates in polar protic solvents favor SN1 and E1. Predicting the major product requires systematic analysis of all four factors rather than memorizing isolated rules.

## How It's Best Learned
Build a decision flowchart: start with substrate class, then evaluate the nucleophile/base, then solvent, then temperature. Work through a dozen mixed problems where you must predict the dominant pathway and draw the major product. Compare outcomes when a single variable changes (e.g., switching from NaOH to NaOtBu on the same secondary substrate).

## Common Misconceptions
- SN1 and E1 are not independent reactions — they share a common carbocation intermediate and always compete with each other; you cannot get pure SN1 without some E1 byproduct.
- "Strong base = elimination" is an oversimplification; a strong, small base like hydroxide can still do SN2 on a primary substrate faster than E2.
- Temperature affects the SN/E ratio (higher temperature favors elimination) but is rarely the sole deciding factor.

## Explainer

You have studied SN2, SN1, E2, and E1 as separate reactions, each with its own mechanism, stereochemistry, and kinetics. The challenge now is that in real chemistry, these four pathways compete simultaneously whenever a substrate with a leaving group meets a nucleophile or base. Your job is to predict which pathway wins — and that requires a systematic decision framework rather than memorized rules.

Start with the **substrate**. This is the single most powerful predictor. Methyl and primary substrates strongly favor SN2 because the backside of the carbon is accessible. Tertiary substrates cannot do SN2 at all — the three bulky groups block the nucleophile's approach — so they are funneled into SN1, E2, or E1. Secondary substrates are the battleground where all four mechanisms genuinely compete, and the other variables become decisive. Think of substrate class as the first fork in your decision tree: it eliminates certain pathways entirely before you consider anything else.

Next, evaluate the **nucleophile/base**. A strong nucleophile that is also a strong base (like hydroxide, HO⁻) can do either SN2 or E2. A strong, bulky base (like tert-butoxide, (CH₃)₃CO⁻) has difficulty squeezing in for backside attack on carbon but can easily abstract a proton — so it favors E2. A weak nucleophile in a polar protic solvent (like water or an alcohol) favors the unimolecular pathways, SN1 and E1, because it is too weak to drive a bimolecular mechanism. The key distinction is between nucleophilicity (affinity for carbon) and basicity (affinity for a proton): a species can be a good nucleophile but a poor base (like iodide, I⁻) or a good base but a poor nucleophile (like tert-butoxide).

**Solvent** plays a supporting role. Polar aprotic solvents (DMSO, DMF, acetone) enhance nucleophilicity by not solvating the nucleophile, favoring SN2. Polar protic solvents (water, alcohols) stabilize carbocations and solvate nucleophiles, favoring SN1/E1. Temperature provides the final nudge: higher temperatures favor elimination over substitution because elimination produces more product molecules (higher entropy). In practice, here is how these factors combine for the most common scenarios: primary substrate + strong nucleophile + polar aprotic solvent → SN2; tertiary substrate + strong bulky base → E2; tertiary substrate + weak nucleophile + polar protic solvent + heat → E1 with some SN1; secondary substrate requires you to weigh all factors carefully.

The most important insight is that SN1 and E1 always accompany each other because they share the same carbocation intermediate — if conditions favor ionization of the substrate, both products will form as a mixture. Similarly, SN2 and E2 can compete when the nucleophile is also a strong base. Perfect selectivity is rare; the goal is to predict the **major** pathway and understand what minor products to expect as well.
