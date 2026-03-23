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
stage: formal-systems
status: validated
---

# The Claisen Condensation and β-Keto Esters

## Core Idea
The Claisen condensation couples two molecules of an ester by enolate attack and C-C bond formation. Base (e.g., EtO⁻) deprotonates an α-hydrogen on one ester, forming an enolate; this attacks the ester carbonyl of another ester molecule (nucleophilic acyl substitution). The product is a β-keto ester (stabilized by the adjacent carbonyl groups). The reaction is driven by irreversible deprotonation of the final product (which has a very acidic α-hydrogen between two carbonyls).

## Questions

```yaml
- question: "Why does the Claisen condensation require a full equivalent of base rather than a catalytic amount?"
  type: multiple-choice
  options:
    - "The base is consumed forming the initial enolate, so a catalytic amount is quickly depleted"
    - "The base irreversibly deprotonates the β-keto ester product, pulling the equilibrium forward — without this step the condensation is readily reversible"
    - "A catalytic base causes the enolate to react with water rather than the second ester molecule"
    - "Catalytic base cannot generate sufficient enolate concentration to achieve useful yield"
  answer: 1
  explanation: "The condensation step itself is reversible — nucleophilic acyl substitution can go backward. What drives it forward is the irreversible deprotonation of the β-keto ester product: the α-hydrogen flanked by two carbonyls has a pKa ≈ 11, far lower than ethanol (pKa ≈ 16), so ethoxide removes it completely. A catalytic base would be consumed in this step and unavailable to form more enolate, stalling the reaction. A stoichiometric base is required because one equivalent is consumed as the thermodynamic driving force."

- question: "An ester with no α-hydrogens (e.g., ethyl benzoate) is treated with sodium ethoxide. What happens?"
  type: multiple-choice
  options:
    - "Ethoxide deprotonates the arene ring to form an aryl enolate that attacks the carbonyl"
    - "No Claisen self-condensation occurs because no enolate can form, but the ester can serve as the electrophilic (acyl donor) component in a crossed Claisen with a different ester"
    - "The reaction proceeds normally because the ester carbonyl is sufficiently electrophilic without enolate involvement"
    - "The ester undergoes saponification because ethoxide is too strong a base for the Claisen pathway"
  answer: 1
  explanation: "Self-condensation requires an α-hydrogen to form the enolate nucleophile. Without one, ethyl benzoate cannot attack another molecule. However, it can receive attack from a different ester's enolate — acting as the electrophilic acyl acceptor in a crossed Claisen. This is actually useful: because ethyl benzoate cannot form its own enolate, it cannot produce unwanted self-condensation products, giving cleaner crossed-Claisen yields."

- question: "The β-keto ester product of the Claisen condensation is more acidic at its central α-carbon than a simple monoester."
  type: true-false
  answer: true
  explanation: "True. In a β-keto ester, the α-carbon sits between two carbonyl groups. Deprotonation generates an enolate stabilized by resonance delocalization into both carbonyls, distributing the negative charge over two oxygen atoms. This extra stabilization dramatically lowers the pKa to approximately 11, compared to ~25 for a simple ester α-carbon. This extraordinary acidity is precisely what allows ethoxide (conjugate acid pKa ≈ 16) to deprotonate the product irreversibly, providing the thermodynamic driving force for the reaction."

- question: "In the Claisen condensation, the enolate attacks the α-carbon of the second ester molecule to form the new C-C bond."
  type: true-false
  answer: false
  explanation: "False. The enolate attacks the electrophilic carbonyl carbon of the second ester — this is nucleophilic acyl substitution, not α-alkylation. The mechanism proceeds through a tetrahedral intermediate which then collapses by expelling the alkoxide leaving group. If the enolate attacked the α-carbon instead, it would be an SN2 reaction on a primary carbon — possible but not what occurs here, and it would not produce the β-keto ester product."

- question: "Why must the Claisen condensation product be irreversibly deprotonated, and what would happen to the reaction yield if the base were too weak to do so?"
  type: short-answer
  answer: "The β-keto ester product contains an α-hydrogen with pKa ≈ 11 (flanked by two carbonyls). A base strong enough to deprotonate this position converts the product into a stable enolate, removing it from equilibrium and pulling the condensation forward irreversibly. If the base were too weak to deprotonate the product, the nucleophilic acyl substitution step would remain reversible — the condensation equilibrium would heavily favor reactants, and the yield would be very low or negligible."
  explanation: "This is the key to understanding why stoichiometric base is required. The thermodynamic sink is not the condensation itself but the subsequent irreversible deprotonation of the product. The Claisen condensation is essentially 'driven' by the exceptional acidity of the β-keto ester: the reaction sequence is only thermodynamically favorable overall because the final step is so favorable."
```

## Explainer

You already know two key pieces of chemistry that combine in the Claisen condensation: **enolate formation** (base removes an α-hydrogen adjacent to a carbonyl, generating a resonance-stabilized carbanion) and **nucleophilic acyl substitution** (a nucleophile attacks an ester carbonyl, forms a tetrahedral intermediate, and then the leaving group departs). The Claisen condensation simply chains these two reactions together — an enolate from one ester molecule acts as the nucleophile that attacks the carbonyl of a second ester molecule, forming a new carbon-carbon bond.

Here is the step-by-step logic. A strong base like sodium ethoxide (NaOEt) deprotonates the α-carbon of an ester — say, ethyl acetate — to form the ester **enolate**. This enolate, a good nucleophile, attacks the electrophilic carbonyl carbon of a second ethyl acetate molecule. The result is a tetrahedral intermediate that collapses by expelling the ethoxide leaving group (just as in any nucleophilic acyl substitution). What you now have is a **β-keto ester**: a molecule with two carbonyl groups separated by a single carbon. The name "condensation" reflects the loss of a small molecule (ethanol) during the process.

The critical question is: why does this reaction proceed in the forward direction? After all, nucleophilic acyl substitution is often reversible. The answer lies in the product's unique acidity. The α-hydrogen that sits between the two carbonyl groups in the β-keto ester is extraordinarily acidic (pKa ≈ 11) because the resulting anion is stabilized by resonance delocalization into both adjacent carbonyls. The base in solution (ethoxide, pKa of ethanol ≈ 16) irreversibly deprotonates this position, pulling the equilibrium forward. This final deprotonation is the thermodynamic driving force — without it, the condensation would be readily reversible and give poor yields. This is why you need a full equivalent of base, not just a catalytic amount.

One practical requirement follows directly: the ester must have at least two α-hydrogens — one to form the initial enolate, and one on the product to be irreversibly removed as the driving force. Esters with no α-hydrogens (like ethyl benzoate) cannot undergo the Claisen condensation on their own, though they can serve as the electrophilic partner in a **crossed Claisen** variant. The β-keto ester products are themselves versatile synthetic intermediates, serving as starting materials for further decarboxylation, alkylation, and enolate chemistry — making the Claisen condensation a foundational carbon-carbon bond-forming tool in organic synthesis.
