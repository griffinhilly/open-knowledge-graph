---
id: competing-substitution-and-elimination
title: Competition Between Substitution and Elimination Pathways
domain: chemistry
course: organic-chemistry
prerequisites:
- id: sn1-mechanism-kinetics-and-factors
  type: hard
- id: sn2-mechanism-kinetics-and-factors
  type: hard
- id: e1-mechanism-zaitsev-rule
  type: hard
- id: e2-mechanism-hoffmann-rule
  type: hard
- id: substitution-vs-elimination
  type: hard
builds-toward:
- retrosynthetic-analysis
tags:
- sn-vs-e
- selectivity
- prediction
- reaction-mechanism
stage: advanced
status: draft
---

# Competition Between Substitution and Elimination Pathways

## Core Idea
Substitution and elimination reactions compete under the same conditions, with the dominant pathway determined by substrate structure (primary/secondary/tertiary), nucleophile strength and basicity, solvent polarity, and temperature. Predicting product distributions requires analyzing all four mechanisms (SN1, SN2, E1, E2) simultaneously.

## Explainer

You have now studied all four mechanisms individually — SN1, SN2, E1, and E2 — and understand their kinetics, stereochemistry, and preferred conditions. The challenge in real chemistry is that when you mix a haloalkane with a reagent, all four pathways are potentially available simultaneously. The dominant products depend on how four variables interact: **substrate structure**, **nucleophile/base character**, **solvent**, and **temperature**. Learning to predict which pathway wins is the central skill of this topic.

Start with substrate structure, because it is the strongest filter. **Primary substrates** strongly favor SN2 — the unhindered carbon is accessible to backside attack by a nucleophile. E2 can compete if you use a strong, bulky base (like tert-butoxide), because the base is too sterically hindered to attack carbon but can still abstract a β-hydrogen. SN1 and E1 are essentially impossible for primary substrates because primary carbocations are too unstable to form. **Tertiary substrates** are the opposite: the carbon bearing the leaving group is too crowded for the SN2 backside attack, so SN2 is ruled out. Instead, tertiary substrates follow SN1/E1 (with weak nucleophiles in polar protic solvents) or E2 (with strong bases). **Secondary substrates** are the most ambiguous — all four mechanisms are potentially operative, and the other variables become decisive.

Next, consider the reagent. A **strong nucleophile that is a weak base** (like I⁻, CN⁻, or RS⁻) favors substitution. A **strong base that is a poor nucleophile** (like tert-butoxide or DBU) favors elimination. A reagent that is both a strong nucleophile and a strong base (like hydroxide or ethoxide) can go either way, and you must look at the substrate and conditions to decide. Weak nucleophiles/weak bases (like water or alcohols) point toward SN1/E1 pathways, which do not require a strong nucleophile because the rate-determining step is unimolecular ionization of the substrate.

Solvent and temperature provide the final adjustments. **Polar protic solvents** (water, alcohols) stabilize carbocations and promote ionization, favoring SN1 and E1. **Polar aprotic solvents** (DMSO, DMF, acetone) do not stabilize cations but do enhance nucleophilicity by not solvating the nucleophile, strongly favoring SN2. Higher temperature generally tips the balance toward elimination (E1 or E2) over substitution, because elimination has a larger positive entropy change — two product molecules form from one substrate.

In practice, the decision tree works like this: identify the substrate class first, eliminate impossible mechanisms, then use the nucleophile/base character and solvent to pick the winner among the remaining candidates. For a tertiary substrate with a strong base, it is E2. For a primary substrate with a good nucleophile in a polar aprotic solvent, it is SN2. For a secondary substrate with a weak nucleophile in a polar protic solvent, SN1 and E1 compete, with E1 favored at higher temperatures. Drilling problems across all substrate classes until this logic becomes automatic is the only way to build reliable predictive skill.
