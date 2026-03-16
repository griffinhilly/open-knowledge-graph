---
id: transamination-reactions
title: Transamination and Aminotransferases
domain: biology
course: biochemistry
prerequisites:
- id: amino-acid-structure-and-properties
  type: hard
- id: enzyme-kinetics
  type: hard
- id: enzyme-cofactors-and-coenzymes
  type: soft
- id: nucleophile-electrophile-definitions
  type: soft
builds-toward:
- amino-acid-degradation-overview
- oxidative-deamination
- urea-cycle
tags:
- amino-acids
- enzymes
- nitrogen-transfer
stage: advanced
status: draft
---

# Transamination and Aminotransferases

## Core Idea
Transamination is the reversible transfer of an amino group from an amino acid to a keto acid, catalyzed by aminotransferases. The reaction requires pyridoxal phosphate (PLP) as a cofactor and is the primary mechanism for both amino acid synthesis and degradation. The amino group typically transfers to α-ketoglutarate, forming glutamate.

## How It's Best Learned
Draw the PLP-mediated mechanism showing Schiff base formation. Compare ALT and AST in serum—when and why they are elevated in disease. Calculate amino acid pools using transamination.

## Common Misconceptions
Transamination removes ammonia directly; it transfers the amino group to another keto acid. The reaction is freely reversible, not unidirectional.

## Explainer

Amino acids are unique among biomolecules because they carry nitrogen — and managing that nitrogen is one of metabolism's central challenges. **Transamination** is the reaction that shuttles amino groups between molecules, and it is the entry point for both amino acid synthesis and degradation. If you understand amino acid structure (an amino group, a carboxyl group, and a variable R group on a central carbon) and the basics of enzyme kinetics, transamination is where those concepts converge in a single, elegant reaction.

The reaction itself is conceptually simple: an **amino acid** donates its amino group to a **keto acid** (an α-keto acid, which has a carbonyl where the amino group would be). The amino acid becomes a keto acid, and the keto acid becomes an amino acid. It is a molecular swap — nitrogen moves from one carbon skeleton to another, and neither molecule is destroyed. For example, alanine (amino acid) + α-ketoglutarate (keto acid) → pyruvate (keto acid) + glutamate (amino acid). The enzyme catalyzing this particular reaction is **alanine aminotransferase (ALT)**, and its counterpart **aspartate aminotransferase (AST)** transfers the amino group from aspartate to α-ketoglutarate. Both are clinically measured in blood tests — elevated ALT and AST indicate liver damage because these enzymes leak from injured hepatocytes.

What makes transamination mechanistically fascinating is its absolute dependence on the cofactor **pyridoxal phosphate (PLP)**, the active form of vitamin B₆. PLP acts as a molecular intermediary: first, it forms a **Schiff base** (a covalent bond between its aldehyde group and the amino acid's amino group), then facilitates the transfer of the amino group through a series of electron rearrangements. Midway through the reaction, PLP temporarily carries the amino group as pyridoxamine phosphate (PMP), then donates it to the incoming keto acid. This ping-pong mechanism means the enzyme cycles between two forms — PLP-bound and PMP-bound — with each half-reaction handling one substrate.

The metabolic significance of transamination lies in its role as a **nitrogen funnel**. Most amino acids cannot be directly deaminated (have their nitrogen removed as free ammonia). Instead, their amino groups are first transaminated onto α-ketoglutarate, producing **glutamate** — the universal nitrogen collector. Glutamate can then be oxidatively deaminated by glutamate dehydrogenase to release free NH₄⁺, which enters the urea cycle for excretion. This two-step process (transamination → oxidative deamination) is how the body safely handles the nitrogen from protein breakdown. Because the reaction is freely reversible, transamination also works in the biosynthetic direction — cells can synthesize nonessential amino acids by transferring amino groups onto available carbon skeletons.
