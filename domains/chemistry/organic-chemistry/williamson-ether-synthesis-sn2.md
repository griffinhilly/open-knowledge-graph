---
id: williamson-ether-synthesis-sn2
title: Williamson Ether Synthesis via SN2
domain: chemistry
course: organic-chemistry
prerequisites:
- id: sn2-reaction
  type: hard
- id: alcohols-and-ethers
  type: hard
- id: sn2-mechanism-kinetics-and-factors
  type: hard
builds-toward:
- ether-cleavage-and-fragmentation
tags:
- williamson-ether-synthesis
- sn2
- alkoxide
- ether-formation
stage: advanced
status: draft
---

# Williamson Ether Synthesis via SN2

## Core Idea
Williamson ether synthesis couples an alkoxide nucleophile (RO⁻) with a primary alkyl halide or tosylate in an SN2 reaction to form an ether. The reaction works best with primary substrates to avoid elimination. This is the most general method for ether synthesis and is widely used because the regiochemistry is predictable: the alkoxide attacks the alkyl halide at the carbon bearing the leaving group.

## Explainer

You already understand that SN2 reactions involve backside attack of a nucleophile on an electrophilic carbon, displacing a leaving group in a single concerted step. The **Williamson ether synthesis** is one of the most important applications of this mechanism: an **alkoxide ion** (RO⁻), formed by deprotonating an alcohol with a strong base like NaH, attacks a **primary alkyl halide** (or tosylate) to form a new C–O bond. The product is an ether, R–O–R'.

The power of this reaction lies in its predictability. Because it proceeds through SN2, the outcome follows all the rules you learned for that mechanism. **Primary substrates** work best because the transition state is unhindered — the nucleophile can access the electrophilic carbon easily. **Secondary substrates** are borderline: the bulky alkoxide is a strong base as well as a nucleophile, so E2 elimination competes heavily. **Tertiary substrates** are effectively useless — elimination dominates completely, and you get alkene instead of ether. This means that when planning a Williamson synthesis for an unsymmetrical ether like methyl tert-butyl ether, you must choose the correct disconnection: the tert-butyl group must come from the alkoxide (since tert-butoxide is easily formed and acts as the nucleophile), while the methyl group comes from a methyl halide (an excellent SN2 substrate). Reversing this assignment — trying to use a tert-butyl halide as the electrophile — would give elimination.

The practical setup is straightforward. First, deprotonate the alcohol with a strong base (NaH is standard because it produces H₂ gas as the only byproduct and drives the reaction forward). The resulting alkoxide then attacks the alkyl halide in a polar aprotic or mildly protic solvent. Tosylates (OTs) work just as well as halides and are sometimes preferred because they are easily prepared from the corresponding alcohol and toluenesulfonyl chloride. The key synthetic planning skill is the **disconnection analysis**: for any target ether R–O–R', break the C–O bond on the less hindered side to identify which fragment becomes the alkoxide and which becomes the electrophile. Choose the combination that puts the SN2 reaction on the least substituted carbon, and the synthesis will work cleanly.
