---
id: imine-enamine-formation
title: Imine and Enamine Formation
domain: chemistry
course: organic-chemistry
prerequisites:
- id: nucleophilic-addition-to-carbonyls
  type: hard
- id: amines-structure-and-properties
  type: soft
builds-toward: []
tags:
- imine
- Schiff base
- enamine
- primary amine
- secondary amine
- condensation
- pH dependence
stage: formal-systems
status: draft
---
# Imine and Enamine Formation

## Core Idea
Primary amines react with aldehydes and ketones to form imines (C=N, also called Schiff bases) through nucleophilic addition followed by loss of water. Secondary amines undergo the same initial addition, but because they lack a second N-H for the elimination step, they lose water from the alpha carbon instead, producing enamines (amino-substituted alkenes). Both reactions are acid-catalyzed and pH-dependent: mildly acidic conditions (pH 4-5) are optimal because the acid catalyzes water loss without fully protonating the amine nucleophile. Imines and enamines are key intermediates in biological transamination and in synthetic strategies like the Stork enamine synthesis.

## How It's Best Learned
Draw the full mechanism for imine formation: nucleophilic attack of the amine on the carbonyl, proton transfer to give a carbinolamine (tetrahedral intermediate), then acid-catalyzed dehydration to the C=N bond. Then repeat for a secondary amine and show how the absence of N-H forces elimination from the alpha carbon to give the enamine. Experiment with pH: too acidic (amine protonated, no nucleophile), too basic (no acid catalyst for dehydration), just right (pH 4-5).

## Common Misconceptions
- The carbinolamine intermediate is analogous to a hemiacetal — both are tetrahedral addition products — but carbinolamines from primary amines lose water to form C=N, not C=O.
- Enamines are not simply "nitrogen enols"; the nitrogen is part of the pi system, and the reactivity pattern (nucleophilic alpha carbon) differs from enolate chemistry.
- Imine formation is reversible under aqueous conditions; hydrolysis regenerates the carbonyl and free amine, which is why imines are often reduced (NaBH3CN) to stable amines.

## Explainer

You know from nucleophilic addition to carbonyls that the carbonyl carbon is electrophilic and can be attacked by nucleophiles. When the nucleophile is an amine — a nitrogen with a lone pair — the initial addition step is familiar: the amine attacks the carbonyl carbon, the pi bond breaks, and the oxygen picks up a proton to form a **carbinolamine** (also called a hemiaminal). This tetrahedral intermediate is analogous to the hemiacetal you saw when alcohols add to carbonyls. What happens next, however, depends on whether the amine is primary or secondary, and this fork in the road is the heart of this topic.

With a **primary amine** (RNH₂), the carbinolamine has an N–H bond available. Under mildly acidic conditions, the hydroxyl group is protonated and lost as water, while the nitrogen simultaneously loses a proton, forming a **C=N double bond**. The product is an **imine** (also called a Schiff base). The overall transformation is a condensation: one molecule of water is lost as the C=O double bond is replaced by a C=N double bond. The mechanism requires acid catalysis for the dehydration step but not so much acid that the amine nucleophile gets fully protonated (which would kill its nucleophilicity). This is why the reaction has an optimal **pH window around 4–5** — acidic enough to catalyze water loss, basic enough to leave some free amine available for the initial attack.

With a **secondary amine** (R₂NH), the nitrogen has no second hydrogen to lose after forming the carbinolamine. The C=N bond cannot form because nitrogen is already fully substituted. Instead, the dehydration takes a different path: a proton is removed from the **alpha carbon** (the carbon adjacent to what was the carbonyl), and water departs. The result is a C=C double bond with the nitrogen still attached — an **enamine** (an amine-substituted alkene). The name literally comes from combining "ene" (double bond) with "amine." The nitrogen's lone pair is conjugated with the new C=C double bond, making the beta carbon nucleophilic — a property that becomes enormously useful in enamine alkylation chemistry.

Both reactions are **reversible** under aqueous conditions. Adding water shifts the equilibrium back toward the carbonyl and free amine, which is why imine and enamine formations are typically driven forward by removing water (using a Dean-Stark trap or molecular sieves). This reversibility also means imines and enamines serve as temporary functional group modifications — you can form them, perform chemistry on them, and then hydrolyze them back to carbonyls. In biological chemistry, imine formation (as a Schiff base) is central to the mechanism of pyridoxal phosphate-dependent enzymes that catalyze amino acid transformations, making this reaction one of the most important in both synthetic and biological contexts.
