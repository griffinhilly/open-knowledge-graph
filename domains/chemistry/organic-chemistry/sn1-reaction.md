---
id: sn1-reaction
title: SN1 Substitution Reactions
domain: chemistry
course: organic-chemistry
prerequisites:
- id: sn2-reaction
  type: hard
- id: resonance-and-formal-charge
  type: soft
- id: diastereomers-and-meso-compounds
  type: soft
builds-toward:
- e1-elimination
- alcohols-and-ethers
tags:
- SN1
- substitution
- carbocation
- unimolecular
- racemization
- rearrangement
stage: formal-systems
status: validated
---
# SN1 Substitution Reactions

## Core Idea
SN1 (substitution nucleophilic unimolecular) reactions proceed through a two-step mechanism: rate-limiting ionization of the substrate to produce a planar carbocation intermediate, followed by rapid nucleophilic attack from either face. Because the carbocation is sp2 hybridized and planar, attack from both faces is equally probable, producing a racemic mixture at the former stereocenter. SN1 favors tertiary > secondary substrates (reflecting carbocation stability), polar protic solvents (which stabilize ions through solvation), and weak nucleophiles. Carbocation rearrangements (hydride and methyl shifts) can complicate product prediction.

## How It's Best Learned
Draw energy-level diagrams for SN1 with two transition states flanking the carbocation intermediate, then compare with the single-transition-state SN2 diagram. Practice the four-factor analysis to choose between SN1 and SN2 under given conditions.

## Common Misconceptions
- Complete racemization is idealized; partial inversion often occurs because the leaving group shields one face briefly before fully departing.
- Polar protic solvents stabilize both the carbocation and the departing anion through solvation — they do not directly react with the substrate.
- SN1 does not always give a single product: carbocation intermediates can rearrange, undergo elimination, or be captured by different nucleophiles.

## Questions

```yaml
- question: "A tertiary alkyl bromide reacts in aqueous ethanol with no added nucleophile. Why does SN1 proceed faster here than an SN2 reaction would?"
  type: multiple-choice
  options:
    - "The tertiary substrate has more surface area for nucleophilic attack"
    - "The tertiary carbocation intermediate is stabilized by hyperconjugation and inductive donation from three alkyl groups"
    - "Aqueous ethanol is a strong nucleophile that accelerates bimolecular attack"
    - "Tertiary substrates have lower activation energy for backside attack"
  answer: 1
  explanation: "SN1 rate depends only on forming the carbocation intermediate (unimolecular, rate-limiting step). Three alkyl groups stabilize the positive charge through hyperconjugation and inductive electron donation, lowering the activation energy for ionization. SN2, by contrast, is sterically blocked at tertiary carbons, so the bulkier the substrate, the slower the SN2 — not faster."

- question: "An SN1 reaction at a pure stereocenter usually produces a perfectly racemic (50/50) mixture of enantiomers."
  type: true-false
  answer: false
  explanation: "Complete racemization is an idealization. In practice, the departing leaving group briefly shields one face of the nascent carbocation before fully dissociating into the solvent shell. During this fleeting ion pair stage, nucleophilic attack from the retention face is slightly blocked, producing a modest excess of the inverted product. The result is partial inversion — mostly racemic but not perfectly 50/50."

- question: "Why do polar protic solvents (e.g., water, ethanol) favor SN1 reactions over polar aprotic solvents (e.g., acetone, DMSO)?"
  type: short-answer
  answer: "Polar protic solvents stabilize both the developing carbocation and the departing anionic leaving group through hydrogen bonding and ion-dipole interactions, lowering the activation energy for the ionization step."
  explanation: "SN1 depends on forming two charged species (a carbocation and a leaving group anion) from a neutral substrate. Polar protic solvents solvate both ions — their OH groups hydrogen-bond to anions and their dipoles stabilize cations — effectively lowering the energy of the transition state and intermediate. Polar aprotic solvents lack the hydrogen-bond donor ability needed to stabilize the anion as well, so they do not assist ionization as effectively."
```

## Explainer

SN1 stands for Substitution Nucleophilic Unimolecular — the "unimolecular" label tells you the most important thing: the rate-limiting step involves only one molecule, the substrate. This contrasts sharply with SN2, where the nucleophile attacks at the same moment the leaving group departs. In SN1, the reaction happens in two separate steps: first the substrate ionizes to form a carbocation intermediate, then the nucleophile attacks. Because the nucleophile is not involved in the slow step, doubling its concentration does not speed up the reaction.

The key to understanding SN1 is carbocation stability. When the leaving group departs, it takes both electrons from the C–LG bond, leaving the carbon with only three bonds and a positive charge. That carbon becomes sp2-hybridized and planar. Alkyl groups stabilize carbocations by donating electron density through hyperconjugation and induction, so tertiary carbocations (three alkyl groups) are far more stable than secondary, which are far more stable than primary. This is why SN1 is practical only for tertiary — and some secondary — substrates: the carbocation intermediate for primary substrates is so unstable it barely forms.

Once the planar carbocation exists, the nucleophile can attack from either face with roughly equal probability — there is no longer a defined "front" or "back" face the way there is in SN2. This is why SN1 reactions at a stereocenter produce a mixture of enantiomers (racemization). In reality, the departing leaving group lingers as a solvent-caged ion pair and briefly blocks one face, so you typically see mostly racemized product with a small excess of the inverted stereoisomer rather than a perfect 50/50 split.

An additional complication is carbocation rearrangement. Once the carbocation forms, it can shift to a more stable structure via a 1,2-hydride shift or 1,2-methyl shift before the nucleophile attacks. This means the nucleophile sometimes bonds to a carbon that was not the original reaction site, yielding rearranged products. Whenever you draw a proposed SN1 mechanism, always check: is the intermediate carbocation adjacent to a hydrogen or methyl group on a carbon that would give a more stable carbocation after the shift? If yes, expect rearrangement.

Polar protic solvents (water, alcohols) are ideal for SN1 because they stabilize the charged species through hydrogen bonding and ion-dipole interactions. Weak nucleophiles are fine — and sometimes preferred — because strong nucleophiles would compete via SN2 or E2. The full decision tree for predicting substitution mechanisms always considers four factors together: substrate structure, nucleophile strength, solvent, and leaving group quality. SN1 wins when the substrate can form a stable carbocation and the conditions do not favor concerted attack.
