---
id: claisen-condensation
title: The Claisen Condensation and β-Keto Esters
domain: chemistry
course: organic-chemistry
prerequisites:
- id: enols-and-enolate-chemistry
  type: hard
- id: nucleophilic-acyl-substitution
  type: hard
builds-toward:
- crossed-aldol-selective-condensation
tags:
- claisen
- enolate
- condensation
- beta-keto-ester
- c-c-coupling
stage: advanced
status: draft
---

# The Claisen Condensation and β-Keto Esters

## Core Idea
The Claisen condensation couples two molecules of an ester by enolate attack and C-C bond formation. Base (e.g., EtO⁻) deprotonates an α-hydrogen on one ester, forming an enolate; this attacks the ester carbonyl of another ester molecule (nucleophilic acyl substitution). The product is a β-keto ester (stabilized by the adjacent carbonyl groups). The reaction is driven by irreversible deprotonation of the final product (which has a very acidic α-hydrogen between two carbonyls).

## Explainer

You already know two key pieces of chemistry that combine in the Claisen condensation: **enolate formation** (base removes an α-hydrogen adjacent to a carbonyl, generating a resonance-stabilized carbanion) and **nucleophilic acyl substitution** (a nucleophile attacks an ester carbonyl, forms a tetrahedral intermediate, and then the leaving group departs). The Claisen condensation simply chains these two reactions together — an enolate from one ester molecule acts as the nucleophile that attacks the carbonyl of a second ester molecule, forming a new carbon-carbon bond.

Here is the step-by-step logic. A strong base like sodium ethoxide (NaOEt) deprotonates the α-carbon of an ester — say, ethyl acetate — to form the ester **enolate**. This enolate, a good nucleophile, attacks the electrophilic carbonyl carbon of a second ethyl acetate molecule. The result is a tetrahedral intermediate that collapses by expelling the ethoxide leaving group (just as in any nucleophilic acyl substitution). What you now have is a **β-keto ester**: a molecule with two carbonyl groups separated by a single carbon. The name "condensation" reflects the loss of a small molecule (ethanol) during the process.

The critical question is: why does this reaction proceed in the forward direction? After all, nucleophilic acyl substitution is often reversible. The answer lies in the product's unique acidity. The α-hydrogen that sits between the two carbonyl groups in the β-keto ester is extraordinarily acidic (pKa ≈ 11) because the resulting anion is stabilized by resonance delocalization into both adjacent carbonyls. The base in solution (ethoxide, pKa of ethanol ≈ 16) irreversibly deprotonates this position, pulling the equilibrium forward. This final deprotonation is the thermodynamic driving force — without it, the condensation would be readily reversible and give poor yields. This is why you need a full equivalent of base, not just a catalytic amount.

One practical requirement follows directly: the ester must have at least two α-hydrogens — one to form the initial enolate, and one on the product to be irreversibly removed as the driving force. Esters with no α-hydrogens (like ethyl benzoate) cannot undergo the Claisen condensation on their own, though they can serve as the electrophilic partner in a **crossed Claisen** variant. The β-keto ester products are themselves versatile synthetic intermediates, serving as starting materials for further decarboxylation, alkylation, and enolate chemistry — making the Claisen condensation a foundational carbon-carbon bond-forming tool in organic synthesis.
