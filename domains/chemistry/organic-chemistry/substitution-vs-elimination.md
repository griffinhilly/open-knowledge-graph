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
stage: formal-systems
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

## Questions

```yaml
- question: "2-Bromopropane (a secondary substrate) is treated with sodium tert-butoxide (NaOtBu) in DMSO. What is the major product?"
  type: multiple-choice
  options:
    - "2-propanol via SN2 — polar aprotic solvent strongly favors substitution"
    - "Propene via E2 — the bulky base cannot access the carbon backside but can abstract a proton"
    - "2-propanol via SN1 — tertiary carbocation forms readily from secondary substrates"
    - "Equal SN2 and E1 products, because secondary substrates always split between pathways"
  answer: 1
  explanation: "Even though DMSO (polar aprotic) normally favors SN2, NaOtBu is an exceptionally bulky base — its three methyl groups physically block backside attack on the carbon. Proton abstraction is far less sterically demanding, so E2 wins. The misconception is treating 'polar aprotic = SN2' as absolute; steric bulk of the base can override the solvent effect, especially on secondary substrates."

- question: "A tertiary alkyl bromide is placed in a water/ethanol mixture at 50°C. What outcome is most likely?"
  type: multiple-choice
  options:
    - "E2 elimination exclusively, because tertiary substrates always eliminate"
    - "SN2 substitution, because the polar protic solvent activates the nucleophile"
    - "A mixture of SN1 and E1 products, because both pathways share a common carbocation intermediate"
    - "No reaction, because tertiary substrates are too hindered for any mechanism"
  answer: 2
  explanation: "Tertiary substrates cannot do SN2 — the three alkyl groups completely block backside attack. Water/ethanol is a polar protic solvent that stabilizes the carbocation and contains only a weak nucleophile, strongly favoring the unimolecular pathways. SN1 and E1 always accompany each other because they arise from the same carbocation intermediate — ionization produces a carbocation that can be captured by the nucleophile (SN1) or lose a proton (E1). You never get pure SN1 without some E1 byproduct."

- question: "SN1 and E1 reactions always produce product mixtures because they share a common carbocation intermediate."
  type: true-false
  answer: true
  explanation: "Correct. Both SN1 and E1 begin with ionization of the substrate to form a carbocation. That intermediate can then be captured by a nucleophile (giving the substitution product) or lose an adjacent proton (giving the elimination product). Because both pathways originate from the same intermediate, they compete simultaneously whenever conditions favor ionization. A reaction described as 'SN1' is more precisely described as 'predominantly SN1, with SN1/E1 competition.'"

- question: "A strong, small base like hydroxide (HO⁻) always gives elimination as the major product on primary substrates, because base strength is the key factor in E2 selectivity."
  type: true-false
  answer: false
  explanation: "Base strength is necessary but not sufficient for E2 selectivity. On a primary substrate, the carbon backside is unhindered, so even hydroxide — which is both a strong base and a good nucleophile — performs SN2 faster than E2. Elimination becomes dominant over substitution when the base is both strong AND sterically bulky (like tert-butoxide), making proton abstraction preferred over backside attack. On tertiary substrates SN2 is blocked regardless, but on primary substrates the substrate accessibility matters more than base strength alone."

- question: "Why is substrate class the first factor to assess when predicting which of SN1, SN2, E1, or E2 will dominate?"
  type: short-answer
  answer: "Substrate class can completely eliminate certain mechanisms before other variables are considered. Tertiary substrates cannot undergo SN2 — the three alkyl groups block backside attack regardless of nucleophile, solvent, or temperature. Methyl and primary substrates cannot form stable carbocations, so SN1 and E1 are negligible. These structural constraints prune the decision tree immediately, so the remaining factors (base/nucleophile identity, solvent, temperature) only need to adjudicate among the pathways that remain possible for that substrate class."
  explanation: "The decision framework is hierarchical: substrate class eliminates mechanisms structurally, then reagent character (nucleophilicity vs. basicity, steric bulk) selects among the surviving options, then solvent and temperature fine-tune the outcome. Starting with substrate class prevents applying irrelevant rules — asking whether hydroxide does SN2 or E2 on a tertiary substrate is a moot question, because neither SN2 nor E2 is efficient there."
```

## Explainer

You have studied SN2, SN1, E2, and E1 as separate reactions, each with its own mechanism, stereochemistry, and kinetics. The challenge now is that in real chemistry, these four pathways compete simultaneously whenever a substrate with a leaving group meets a nucleophile or base. Your job is to predict which pathway wins — and that requires a systematic decision framework rather than memorized rules.

Start with the **substrate**. This is the single most powerful predictor. Methyl and primary substrates strongly favor SN2 because the backside of the carbon is accessible. Tertiary substrates cannot do SN2 at all — the three bulky groups block the nucleophile's approach — so they are funneled into SN1, E2, or E1. Secondary substrates are the battleground where all four mechanisms genuinely compete, and the other variables become decisive. Think of substrate class as the first fork in your decision tree: it eliminates certain pathways entirely before you consider anything else.

Next, evaluate the **nucleophile/base**. A strong nucleophile that is also a strong base (like hydroxide, HO⁻) can do either SN2 or E2. A strong, bulky base (like tert-butoxide, (CH₃)₃CO⁻) has difficulty squeezing in for backside attack on carbon but can easily abstract a proton — so it favors E2. A weak nucleophile in a polar protic solvent (like water or an alcohol) favors the unimolecular pathways, SN1 and E1, because it is too weak to drive a bimolecular mechanism. The key distinction is between nucleophilicity (affinity for carbon) and basicity (affinity for a proton): a species can be a good nucleophile but a poor base (like iodide, I⁻) or a good base but a poor nucleophile (like tert-butoxide).

**Solvent** plays a supporting role. Polar aprotic solvents (DMSO, DMF, acetone) enhance nucleophilicity by not solvating the nucleophile, favoring SN2. Polar protic solvents (water, alcohols) stabilize carbocations and solvate nucleophiles, favoring SN1/E1. Temperature provides the final nudge: higher temperatures favor elimination over substitution because elimination produces more product molecules (higher entropy). In practice, here is how these factors combine for the most common scenarios: primary substrate + strong nucleophile + polar aprotic solvent → SN2; tertiary substrate + strong bulky base → E2; tertiary substrate + weak nucleophile + polar protic solvent + heat → E1 with some SN1; secondary substrate requires you to weigh all factors carefully.

The most important insight is that SN1 and E1 always accompany each other because they share the same carbocation intermediate — if conditions favor ionization of the substrate, both products will form as a mixture. Similarly, SN2 and E2 can compete when the nucleophile is also a strong base. Perfect selectivity is rare; the goal is to predict the **major** pathway and understand what minor products to expect as well.
