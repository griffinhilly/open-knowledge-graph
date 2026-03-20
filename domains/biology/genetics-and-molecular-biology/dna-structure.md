---
id: dna-structure
title: DNA Structure
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: nucleus-and-genetic-material
  type: hard
- id: covalent-bonding
  type: soft
- id: intermolecular-forces
  type: soft
- id: organic-chemistry-intro
  type: soft
- id: nucleophile-electrophile-definitions
  type: soft
- id: aromatic-compounds-intro
  type: soft
- id: hydrogen-bonding-energetics
  type: soft
builds-toward:
- dna-replication
- transcription
- gene-expression-overview
- restriction-enzymes
tags:
- dna
- double-helix
- nucleotides
- base-pairing
stage: advanced
status: validated
---

# DNA Structure

## Core Idea
DNA is a double-stranded helix composed of nucleotide monomers, each containing a deoxyribose sugar, a phosphate group, and one of four nitrogenous bases (adenine, thymine, guanine, cytosine). The two strands are held together by hydrogen bonds between complementary base pairs: A pairs with T and G pairs with C. The strands run antiparallel, with one strand oriented 5' to 3' and the other 3' to 5'. This structure encodes genetic information in the sequence of bases and enables faithful copying through complementary base pairing.

## How It's Best Learned
Build or examine physical models of the double helix to internalize the antiparallel orientation and base-pairing rules. Practice identifying 5' and 3' ends and writing the complementary strand of a given sequence.

## Common Misconceptions
- Students often think the bases stack on the outside; in fact the sugar-phosphate backbone faces outward and the bases point inward.
- A-T and G-C pairing is specific: A does not pair with G even though both are purines.

## Questions

```yaml
- question: "In the DNA double helix, where are the nitrogenous bases located relative to the sugar-phosphate backbone?"
  type: multiple-choice
  options: ["On the outer surface, facing the solvent", "Pointing inward, facing the bases on the opposite strand", "Alternating between the inside and outside depending on the base type", "Attached to the phosphate group on the exterior"]
  answer: 1
  explanation: "The sugar-phosphate backbone runs along the outside of the helix, while the bases point inward toward the center, where they pair with complementary bases on the opposite strand via hydrogen bonds. This arrangement protects the genetic information while exposing the backbone to the aqueous environment."

- question: "Adenine (A) can form hydrogen bonds with guanine (G) in a normal DNA double helix because both are purines and have compatible shapes."
  type: true-false
  answer: false
  explanation: "Base pairing is determined by complementary hydrogen-bond donor/acceptor geometry, not by purine/pyrimidine classification. A pairs only with T (two hydrogen bonds) and G pairs only with C (three hydrogen bonds). A and G are both purines but cannot pair with each other; a purine must pair with the pyrimidine of the appropriate complementary type."

- question: "Why is the antiparallel orientation of the two DNA strands important for replication?"
  type: short-answer
  answer: "DNA polymerase can only synthesize new DNA in the 5'-to-3' direction. Because the template strands run antiparallel, each strand can serve as a template read 3'-to-5' while new DNA is synthesized 5'-to-3'. This also means the two new strands are made differently: one continuously (leading strand) and one in fragments (lagging strand, Okazaki fragments)."
  explanation: "The antiparallel rule is not just structural — it directly constrains how replication machinery works. Both strands of the double helix carry independent, readable sequence information, and the complementary base-pairing rules ensure each strand can template the faithful synthesis of its partner."
```

## Explainer

DNA's structure is a direct solution to two biological problems: how to store a large amount of information compactly, and how to copy it faithfully. The double helix solves both by encoding information in a linear sequence of bases while simultaneously providing a built-in template for copying.

Each strand of DNA is a polymer of nucleotides. A nucleotide has three parts: a deoxyribose sugar, a phosphate group, and one of four nitrogenous bases — adenine (A), thymine (T), guanine (G), or cytosine (C). The sugars and phosphates link together end-to-end to form the backbone, which runs along the outside of the helix. The bases hang inward from each sugar, pointing toward the center of the molecule. This arrangement — backbone out, bases in — is the opposite of what many students initially imagine.

The two strands are held together by hydrogen bonds between complementary bases. A always pairs with T (two hydrogen bonds), and G always pairs with C (three hydrogen bonds). This specificity is a consequence of the molecular geometry: only A and T have the right shape and hydrogen-bond donor/acceptor positions to fit together across the helix, and likewise for G and C. The G-C pair is slightly stronger because it has three hydrogen bonds instead of two, which is why DNA with higher G-C content is more thermally stable.

The strands run in opposite directions — one 5' to 3' and the other 3' to 5' — which is called antiparallel orientation. The 5' end of a strand is defined by a free phosphate group attached to the 5' carbon of the deoxyribose; the 3' end has a free hydroxyl group on the 3' carbon. You can think of each strand as having a directionality, like a one-way street, and the two strands run in opposite directions along the helix. This matters enormously for DNA replication, because the enzymes that copy DNA can only work in one direction.

The elegance of this structure is that the base-pairing rules mean each strand of the double helix is an exact informational complement of the other. If you know the sequence of one strand (say, 5'-ATGC-3'), you immediately know the other (3'-TACG-5', or equivalently 5'-CGTA-3'). This complementarity is what allows DNA replication to be accurate and what enables transcription — the process by which a strand of DNA is used as a template to produce RNA.
