---
id: sn2-reaction
title: SN2 Substitution Reactions
domain: chemistry
course: organic-chemistry
prerequisites:
- id: reaction-mechanisms-overview
  type: hard
- id: enantiomers-and-chirality
  type: hard
- id: diastereomers-and-meso-compounds
  type: soft
builds-toward:
- sn1-reaction
- e2-elimination
- alcohols-and-ethers
tags:
- SN2
- substitution
- nucleophilic
- bimolecular
- backside attack
- inversion
- Walden inversion
stage: advanced
status: validated
---
# SN2 Substitution Reactions

## Core Idea
SN2 (substitution nucleophilic bimolecular) reactions proceed by a concerted one-step mechanism in which a nucleophile attacks the backside of the carbon bearing the leaving group, simultaneously displacing it through a trigonal bipyramidal transition state. This backside attack causes Walden inversion of configuration at the stereocenter. SN2 reactivity decreases with increasing steric hindrance: methyl > primary > secondary >> tertiary. Rate depends on the concentrations of both the substrate and the nucleophile, reflecting the bimolecular transition state.

## How It's Best Learned
Draw the transition state explicitly (trigonal bipyramidal, partial bonds to both nucleophile and leaving group) for each example. Practice the four-factor analysis — substrate class, nucleophile strength, solvent, leaving group — and predict whether SN2 will occur. Confirm stereoochemical outcomes.

## Common Misconceptions
- Good leaving groups and good nucleophiles are independent properties; iodide is both a good nucleophile and a good leaving group, but these roles are context-dependent.
- Inversion of spatial arrangement does not always change the R/S label — it depends on how the priorities of the incoming group shift the CIP ranking.
- SN2 has no carbocation intermediate; the concerted mechanism bypasses any ionic species.

## Questions

```yaml
- question: "Which substrate would you expect to undergo SN2 substitution most readily with a strong nucleophile?"
  type: multiple-choice
  options:
    - "(CH₃)₃CBr — tert-butyl bromide"
    - "CH₃CH₂CH₂Br — n-propyl bromide (primary)"
    - "(CH₃)₂CHBr — isopropyl bromide (secondary)"
    - "CH₃Br — methyl bromide"
  answer: 3
  explanation: "SN2 reactivity is methyl > primary > secondary >> tertiary, because the nucleophile must approach the backside of the electrophilic carbon through a trigonal bipyramidal transition state. Methyl bromide (CH₃Br) has no alkyl substituents blocking the backside, making it the most accessible. Tert-butyl bromide has three methyl groups flanking the reactive carbon, creating severe steric crowding that essentially prevents backside attack — SN2 at tertiary centers is so slow as to be negligible."

- question: "In an SN2 reaction at a stereocenter, inversion of the spatial arrangement of substituents always results in a change from R to S configuration (or vice versa)."
  type: true-false
  answer: false
  explanation: "Backside attack always causes Walden inversion — the spatial arrangement of the three non-leaving substituents is flipped like an umbrella turning inside out. However, whether the R/S label changes depends on the CIP priority ranking of the incoming nucleophile relative to the other substituents. If the nucleophile has lower priority than the leaving group, the inversion of geometry coincides with an R→S or S→R change. But if the new substituent has higher priority than what it replaced, the spatial inversion can appear to leave the R/S designation unchanged, because the priority ranking that determines the label has also changed."

- question: "Why does SN2 rate depend on the concentration of both the nucleophile and the substrate, while SN1 rate depends only on the substrate concentration?"
  type: short-answer
  answer: "SN2 is a concerted, one-step mechanism: the nucleophile attacks and the leaving group departs simultaneously in a single transition state. Both the nucleophile and the substrate must collide to form this transition state, so the rate depends on both concentrations (rate = k[substrate][nucleophile]). SN1 involves a two-step mechanism where the rate-determining step is unimolecular ionization of the substrate to form a carbocation intermediate — the nucleophile is not involved in this slow step, so its concentration does not affect the rate."
  explanation: "The 'bimolecular' in SN2 refers to the kinetics: two species appear in the rate law because both must be present at the transition state. In SN1, the slow step is the spontaneous ionization of the C–LG bond; the nucleophile only participates in the fast second step after the carbocation has already formed. This mechanistic difference has practical consequences: increasing nucleophile concentration accelerates SN2 but has no effect on SN1."
```

## Explainer

SN2 reactions are the cleanest, most predictable substitution reactions in organic chemistry. The mechanism is a single concerted step: a nucleophile approaches the carbon bearing the leaving group from the backside — directly opposite the leaving group — and attacks at the same moment the leaving group departs. There is no intermediate; the entire process occurs through a single transition state where the carbon is transiently pentacoordinated (five bonds) in a trigonal bipyramidal geometry with partial bonds to both the nucleophile and the leaving group. Because the two reactants must collide in this precise geometry, the rate depends on both concentrations: rate = k[substrate][nucleophile]. That is the "bimolecular" in SN2.

The stereochemical consequence of backside attack is Walden inversion, sometimes described as an umbrella flipping inside out. Imagine the carbon at the center of the umbrella, with three substituents as the ribs. When the nucleophile attacks from one face and the leaving group departs from the other, the three remaining substituents invert through the trigonal bipyramidal transition state and end up on the opposite side from where they started. This is always 100% stereospecific in SN2 — every molecule reacts with complete inversion. Whether this changes the R or S label depends on how the CIP priorities of the substituents compare before and after, which is a labeling consequence, not a mechanistic one.

Steric hindrance is the dominant factor controlling SN2 reactivity. The nucleophile must attack the backside of the electrophilic carbon, which requires an unobstructed approach. Methyl substrates have no alkyl groups at all, so backside access is wide open. Primary substrates have one alkyl group — some steric hindrance but still fast. Secondary substrates have two alkyl groups flanking the reaction center — notably slower. Tertiary substrates have three alkyl groups fully crowding the backside — SN2 is essentially impossible. This is not a matter of thermodynamics but of transition-state accessibility: the incoming nucleophile and the three substituents must all fit in the transition state simultaneously.

The stereochemistry you studied in enantiomers and chirality is essential here. SN2 is a powerful stereochemical tool: if you start with an enantiopure substrate, you get an enantiopure product with inverted configuration. Synthetic chemists use this predictability to construct molecules with defined stereocenters. The reaction is also sensitive to solvent: polar aprotic solvents (DMSO, acetone, DMF) are ideal because they dissolve ionic nucleophiles without surrounding and deactivating them with solvent hydrogen-bonding. Polar protic solvents (water, methanol) solvate nucleophiles and reduce their reactivity, slowing SN2.

Finally, keep in mind that the SN2 mechanism is one tool among several for substitution reactions. Its competitor, SN1, operates through a two-step mechanism involving a carbocation intermediate and is favored by tertiary substrates, stable carbocations, and polar protic solvents. The contrast between them — concerted vs. stepwise, inversion vs. racemization, steric sensitivity vs. carbocation stability — will become a recurring theme as you move through organic mechanisms. Recognizing which pathway dominates under a given set of conditions (substrate class, nucleophile, solvent) is a core skill in predicting reaction outcomes.
