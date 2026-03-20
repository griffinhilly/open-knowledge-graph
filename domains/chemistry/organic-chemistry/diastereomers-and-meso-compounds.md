---
id: diastereomers-and-meso-compounds
title: Diastereomers and Meso Compounds
domain: chemistry
course: organic-chemistry
prerequisites:
- id: enantiomers-and-chirality
  type: hard
- id: cycloalkanes
  type: soft
builds-toward:
- sn1-reaction
- sn2-reaction
tags:
- diastereomers
- meso
- stereoisomers
- cis-trans
- internal symmetry
stage: advanced
status: validated
---

# Diastereomers and Meso Compounds

## Core Idea
Diastereomers are stereoisomers that are not mirror images of each other; they differ in configuration at one or more (but not all) stereocenters. Unlike enantiomers, diastereomers have different physical and chemical properties and can be separated by conventional techniques. A meso compound contains stereocenters but possesses an internal plane of symmetry that renders the molecule achiral overall. For n stereocenters the maximum number of stereoisomers is 2ⁿ, reduced when meso forms are possible.

## How It's Best Learned
Draw all stereoisomers of 2,3-dibromobutane systematically in wedge-dash notation. Identify all enantiomeric and diastereomeric relationships and locate the internal symmetry plane in the meso isomer. Extend the exercise to cis/trans-1,2-dimethylcyclohexane.

## Common Misconceptions
- Meso compounds are NOT chiral despite containing stereocenters — the internal symmetry plane makes the molecule superimposable on its mirror image.
- Cis and trans isomers of cycloalkanes are diastereomers, not enantiomers.
- Diastereomers can have dramatically different physical constants, making them separable by chromatography or crystallization.

## Explainer

You already know from studying enantiomers and chirality that molecules with stereocenters can exist as non-superimposable mirror images. **Diastereomers** extend this concept: they are stereoisomers that are *not* mirror images of each other. The simplest way to see this is with a molecule that has two stereocenters, like 2,3-dibromobutane. Each stereocenter can be R or S, giving four possible configurations: (R,R), (S,S), (R,S), and (S,R). The (R,R) and (S,S) forms are mirror images of each other — they are enantiomers. But (R,R) and (R,S) differ at only one stereocenter — they are diastereomers. The critical practical difference is that enantiomers have identical physical properties (same melting point, same solubility, same boiling point), while diastereomers have *different* physical properties and can therefore be separated by ordinary techniques like column chromatography or recrystallization.

Now consider what happens with the (R,S) and (S,R) configurations of 2,3-dibromobutane. You might expect them to be enantiomers — after all, they are mirror images. But if you build a model of the (R,S) isomer and look carefully, you will find an **internal plane of symmetry** that cuts the molecule in half, making the top half a mirror image of the bottom half. This symmetry means the molecule is superimposable on its mirror image: it is achiral despite having two stereocenters. This is a **meso compound**. The optical rotation contributed by one stereocenter is exactly canceled by the opposite rotation from the other, resulting in zero net rotation of plane-polarized light.

Recognizing meso compounds matters for counting stereoisomers correctly. The formula 2ⁿ gives the maximum number of stereoisomers for n stereocenters, but meso compounds reduce this count. For 2,3-dibromobutane, 2² = 4 predicts four stereoisomers, but because the (R,S) and (S,R) forms are the same meso compound, there are only three distinct stereoisomers: the (R,R)/(S,S) enantiomeric pair and the single meso form. The key diagnostic for a meso compound is an internal mirror plane — look for it whenever a molecule has two or more stereocenters with identical substituents.

Cis-trans isomers of substituted cycloalkanes provide another common example of diastereomers. In cis-1,2-dimethylcyclohexane, both methyl groups are on the same face of the ring; in the trans isomer, they are on opposite faces. These are diastereomers — not mirror images, and with different physical properties. The cis isomer of 1,2-dimethylcyclohexane is also a meso compound when both carbons bearing methyl groups are stereocenters, because the plane of the ring serves as the internal mirror plane. Developing the habit of drawing all possible stereoisomers, checking for internal symmetry, and then classifying every pair as either enantiomers or diastereomers is the core skill this topic demands.
