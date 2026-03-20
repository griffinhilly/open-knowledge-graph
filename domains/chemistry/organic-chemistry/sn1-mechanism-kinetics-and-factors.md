---
id: sn1-mechanism-kinetics-and-factors
title: SN1 Mechanism, Kinetics, and Factors Affecting Reactivity
domain: chemistry
course: organic-chemistry
prerequisites:
- id: sn1-reaction
  type: hard
- id: carbocation-stability-rearrangement
  type: hard
- id: haloalkane-structure-nomenclature
  type: hard
builds-toward:
- competing-substitution-and-elimination
- carbocation-hydride-shift-methyl-shift-rearrangement
tags:
- sn1
- unimolecular
- mechanism
- kinetics
- tertiary
stage: advanced
status: draft
---

# SN1 Mechanism, Kinetics, and Factors Affecting Reactivity

## Core Idea
The SN1 reaction is a two-step unimolecular nucleophilic substitution where the rate-determining step is carbocation formation. First-order kinetics depend only on the substrate concentration. Factors favoring SN1 include tertiary carbon centers, polar protic solvents, stable carbocations, and weak or neutral nucleophiles.

## Explainer

You already know from studying the SN1 reaction that it proceeds in two discrete steps, and from carbocation stability that tertiary and resonance-stabilized carbocations are strongly favored over primary ones. This topic pulls those ideas together into a predictive framework: given a substrate, solvent, and nucleophile, can you predict whether SN1 will dominate?

The defining feature of the SN1 mechanism is that the **rate-determining step** is the spontaneous departure of the leaving group to form a carbocation — the nucleophile is not involved in this slow step. This is why the kinetics are **first-order**: rate = k[substrate]. Doubling the nucleophile concentration has no effect on how fast the reaction proceeds because the nucleophile only enters in the fast second step, attacking the already-formed carbocation. This is the sharpest experimental distinction between SN1 and SN2 — if you double the nucleophile and the rate does not change, you are observing first-order, unimolecular kinetics.

Because the rate depends entirely on how easily the carbocation forms, **substrate structure** is the single most important factor. Tertiary substrates react fastest by SN1 because three alkyl groups stabilize the positive charge through hyperconjugation and inductive donation. Secondary substrates are borderline. Primary substrates almost never react by SN1 because a primary carbocation is too unstable to form under normal conditions — the energy cost is prohibitive. Allylic and benzylic substrates are exceptions: even primary allylic or benzylic halides can undergo SN1 because the resulting carbocation is stabilized by resonance delocalization into the adjacent π system.

**Solvent** plays a critical supporting role. **Polar protic solvents** — water, methanol, acetic acid — stabilize both the departing anion (through hydrogen bonding) and the developing carbocation (through solvation of the positive charge). This lowers the energy of the transition state for ionization, dramatically accelerating SN1. A polar aprotic solvent, by contrast, does not stabilize the leaving group as effectively and tends to favor SN2 instead. The nucleophile matters too, but in the opposite way from what you might expect: weak or neutral nucleophiles (water, alcohols) favor SN1 because strong nucleophiles would attack before the carbocation forms, pushing the mechanism toward SN2.

One important consequence of the carbocation intermediate is **stereochemical outcome**. Because the carbocation is planar and sp²-hybridized, the nucleophile can attack from either face. This leads to **racemization** — a roughly equal mixture of R and S products when the electrophilic carbon was a stereocenter. In practice, the ratio is often not perfectly 50:50 because the departing leaving group can partially block one face (ion-pair effects), but the loss of stereochemical purity is a hallmark of SN1 and a useful diagnostic tool.
