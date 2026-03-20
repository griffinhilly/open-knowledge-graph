---
id: carbonyl-chemistry-intro
title: 'Aldehydes and Ketones: Structure and Reactivity'
domain: chemistry
course: organic-chemistry
prerequisites:
- id: functional-groups-overview
  type: hard
- id: resonance-and-formal-charge
  type: soft
- id: molecular-polarity
  type: soft
- id: alcohol-reactions
  type: soft
- id: alcohols-and-ethers
  type: soft
builds-toward:
- nucleophilic-addition-to-carbonyls
- enols-and-enolate-chemistry
- carboxylic-acids-and-derivatives
tags:
- aldehydes
- ketones
- carbonyl
- electrophilicity
- alpha carbon
- polarity
stage: advanced
status: validated
---
# Aldehydes and Ketones: Structure and Reactivity

## Core Idea
The carbonyl group (C=O) is the most important functional group in organic chemistry, present in aldehydes, ketones, carboxylic acids, esters, and amides. The C=O bond is highly polarized because oxygen is electronegative, making the carbonyl carbon a potent electrophile susceptible to nucleophilic attack. Aldehydes (RCHO) are more reactive than ketones (RCOR') toward nucleophilic addition because they are less sterically shielded and less stabilized by electron-donating alkyl groups. The alpha carbon adjacent to the carbonyl is acidic (pKa ≈ 20 for ketones) because the resulting carbanion is resonance-stabilized as the enolate.

## How It's Best Learned
Draw resonance structures of the carbonyl group to show partial positive charge on carbon and partial negative on oxygen. Rank the reactivities of formaldehyde, acetaldehyde, acetone, and benzaldehyde toward a nucleophile, justifying each ranking with steric and electronic arguments.

## Common Misconceptions
- Nucleophilic attack occurs at the carbonyl carbon, not at oxygen, even though oxygen bears the partial negative charge in the ground state.
- Aldehydes and ketones are often confused in structures: an aldehyde must have at least one H on the carbonyl carbon; a ketone has two carbon substituents.
- Carboxylic acid derivatives also contain a carbonyl but behave very differently from aldehydes and ketones because of the attached leaving group.

## Questions

```yaml
- question: "Why does a nucleophile attack the carbonyl carbon rather than the carbonyl oxygen, even though the oxygen bears the partial negative charge (δ−) in the ground state?"
  type: multiple-choice
  options: ["The oxygen lone pairs are too tightly held to react", "The carbonyl carbon carries the partial positive charge (δ+) and is the electrophilic site that attracts nucleophiles", "The C=O pi bond blocks access to the oxygen", "Nucleophiles attack both carbon and oxygen with equal probability"]
  answer: 1
  explanation: "The C=O bond is polarized so that carbon is δ+ and oxygen is δ−. Nucleophiles are electron-rich species attracted to electron-poor sites — so they attack the δ+ carbon. The δ− oxygen actually repels nucleophiles. Attack at carbon leads to a productive tetrahedral intermediate; attack at oxygen would require breaking a much stronger bond and leads nowhere useful. The misconception that negative charge marks the site of nucleophilic attack is one of the most common errors in carbonyl chemistry."

- question: "Aldehydes are generally more reactive than ketones toward nucleophilic addition."
  type: true-false
  answer: true
  explanation: "Both steric and electronic factors favor aldehydes. Electronically, ketones have two alkyl groups flanking the carbonyl; these groups donate electron density through hyperconjugation and induction, reducing the partial positive charge on carbon and making it less electrophilic. Sterically, two alkyl groups block nucleophile approach more than the one alkyl group (plus H) in an aldehyde. Formaldehyde (two H atoms, no alkyl groups) is the most reactive common carbonyl compound."

- question: "What makes the alpha C–H bond of a ketone (pKa ≈ 20) far more acidic than a typical alkane C–H bond (pKa ≈ 50)?"
  type: short-answer
  answer: "When the alpha proton is removed, the resulting carbanion is stabilized by resonance with the adjacent carbonyl group — the negative charge delocalizes from the alpha carbon onto the electronegative oxygen, forming the enolate ion. Resonance stabilization of the conjugate base always increases acidity (lowers pKa). A typical alkane C–H loses a proton to form an unstabilized carbanion with no resonance, which is why those bonds are far less acidic."
  explanation: "Enolate formation underlies much of synthetic organic chemistry — aldol condensation, Claisen condensation, and alkylation reactions all depend on generating the alpha carbanion. The roughly 30-unit pKa difference between an alpha C–H and a typical C–H is entirely due to resonance stabilization of the enolate. Whenever you see a C–H bond adjacent to an electron-withdrawing group, expect enhanced acidity."
```

## Explainer

The carbonyl group (C=O) is the most important functional group in organic chemistry, appearing in aldehydes, ketones, esters, amides, carboxylic acids, and many other compound classes. Its reactivity stems from one source: the electronegativity of oxygen. The shared electrons in the C=O double bond are pulled strongly toward oxygen, leaving the carbon electron-poor. This partial positive charge (δ+) on carbon makes the carbonyl carbon an electrophile — a target for electron-rich species called nucleophiles. Understanding this polarity is the key to predicting carbonyl reactivity.

A point that confuses nearly every student initially: nucleophilic attack occurs at the carbonyl carbon, not the oxygen, even though oxygen bears the δ− charge in the ground state. The δ− oxygen actually repels nucleophiles, which carry their own electron pairs. The δ+ carbon attracts them. When a nucleophile donates electrons to the carbon, the π electrons of the C=O bond shift entirely onto oxygen, generating an alkoxide (or similar) intermediate. This is the general mechanism for nucleophilic addition to carbonyls: nucleophile attacks C, π bond breaks toward O, tetrahedral intermediate forms.

Comparing aldehydes and ketones reveals how both steric bulk and electron density shape reactivity. In a ketone, two alkyl groups flank the carbonyl carbon — they donate electron density through induction and hyperconjugation, reducing the δ+ charge, and they physically block the approach of a nucleophile. In an aldehyde, only one alkyl group and one hydrogen occupy those positions. The result: aldehydes are more electrophilic and less sterically hindered, so they react faster with nucleophiles. Formaldehyde (H₂C=O), with two hydrogens and no alkyl groups, is the most reactive simple carbonyl compound.

The alpha carbon — the sp3 carbon directly adjacent to C=O — has a surprisingly acidic C–H bond, with pKa around 20 for ketones compared to roughly 50 for a typical alkane C–H. This enormous difference in acidity is due entirely to resonance stabilization of the conjugate base. When the alpha proton is removed by a base, the resulting carbanion delocalizes its negative charge through the carbonyl system onto oxygen, forming the enolate ion. Because the conjugate base (enolate) is far more stable than an unresolved carbanion, the equilibrium for proton removal lies much further toward the deprotonated side — the acid is stronger. Enolate chemistry is what makes carbonyls so versatile in synthesis.

The aldehyde/ketone reactivity you learn here is the foundation for the rest of carbonyl chemistry. Carboxylic acid derivatives (esters, amides, acid chlorides) also contain C=O, but the heteroatom attached directly to the carbonyl changes the mechanism: instead of simple addition, these compounds undergo acyl substitution, where the nucleophile adds and then a leaving group departs. The carbonyl carbon's electrophilicity, nucleophilic attack at C rather than O, and resonance-driven enolate acidity are threads that run through all of it.
