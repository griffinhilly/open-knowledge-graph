---
id: translation
title: 'Translation: RNA to Protein'
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: rna-types-and-structure
  type: hard
- id: genetic-code
  type: hard
- id: ribosomes-and-protein-synthesis-intro
  type: hard
- id: rna-processing
  type: soft
builds-toward:
- gene-regulation-prokaryotes
- gene-regulation-eukaryotes
tags:
- translation
- ribosome
- tRNA
- codon
- anticodon
- peptide bond
stage: advanced
status: validated
---

# Translation: RNA to Protein

## Core Idea
Translation is the synthesis of a polypeptide from the information encoded in mRNA, carried out by ribosomes with the help of tRNAs. The ribosome has three tRNA-binding sites — A (aminoacyl), P (peptidyl), and E (exit) — and moves along the mRNA in the 5'-to-3' direction. Each elongation cycle involves: codon recognition by a charged tRNA in the A site, peptide bond formation by peptidyl transferase (a ribozyme), and translocation shifting the ribosome one codon. Translation begins at AUG and terminates when a stop codon enters the A site, releasing the finished protein.

## How It's Best Learned
Use a codon table and manually translate a short mRNA sequence step by step, tracking tRNA movements through A, P, and E sites. Compare prokaryotic (70S, Shine-Dalgarno) and eukaryotic (80S, Kozak sequence) initiation.

## Common Misconceptions
- Peptide bond formation is catalyzed by the rRNA component of the ribosome (a ribozyme), not by a protein enzyme.
- The reading frame is set by the AUG start codon; a frameshift mutation shifts every codon downstream.

## Questions

```yaml
- question: "During translation elongation, what catalyzes the formation of the peptide bond between the growing polypeptide and the incoming amino acid?"
  type: multiple-choice
  options: ["A protein enzyme called peptidyl transferase", "The rRNA component of the large ribosomal subunit", "A charged tRNA in the A site", "Translation elongation factor EF-Tu / EF-1α"]
  answer: 1
  explanation: "Peptide bond formation is catalyzed by the 23S rRNA (in prokaryotes) or 28S rRNA (in eukaryotes) of the large ribosomal subunit — making the ribosome a ribozyme. This was a landmark discovery because it showed that RNA, not protein, performs this central catalytic function. The protein components of the ribosome play structural and regulatory roles."

- question: "The peptide bond in a growing polypeptide is formed by a protein enzyme called peptidyl transferase."
  type: true-false
  answer: false
  explanation: "Peptidyl transferase activity resides in the rRNA of the large ribosomal subunit, not a protein enzyme — the ribosome is a ribozyme. This fact also supports the RNA World hypothesis, since it implies that protein synthesis could have originated in an RNA-based system before protein enzymes evolved."

- question: "What sets the reading frame during translation, and why does a single-nucleotide insertion in the middle of a coding sequence typically destroy protein function?"
  type: short-answer
  answer: "The reading frame is established by the AUG start codon. A single nucleotide insertion shifts the triplet grouping of every codon downstream, producing a completely different amino acid sequence from that point forward — almost always including a premature stop codon."
  explanation: "The ribosome reads mRNA in non-overlapping three-nucleotide codons starting from the AUG. Insert one nucleotide and all downstream codons are misread: the mutation is not a single amino acid change but a garbled sequence for the entire remainder of the protein, almost always rendering it nonfunctional."
```

## Explainer

You know the genetic code: each three-nucleotide codon specifies an amino acid. Translation is the molecular machinery that reads codons in sequence and assembles the corresponding amino acids into a polypeptide. The central player is the ribosome, which is far more than a passive scaffold — it is a molecular machine with moving parts and, crucially, catalytic activity residing in its RNA.

The ribosome has three named sites that track the state of the tRNAs involved in each round of elongation. The A (aminoacyl) site receives an incoming charged tRNA — a tRNA carrying its specific amino acid — whose anticodon must complement the mRNA codon currently positioned there. The P (peptidyl) site holds the tRNA attached to the growing polypeptide chain. The E (exit) site holds the now-uncharged tRNA just before it leaves the ribosome. Each elongation cycle proceeds in three coordinated steps: a charged tRNA enters the A site and base-pairs with the codon; peptidyl transferase catalyzes the transfer of the polypeptide from the P-site tRNA to the A-site amino acid, forming a new peptide bond; and the ribosome translocates one codon in the 5'-to-3' direction, shifting the tRNAs from A to P, P to E, and ejecting the E-site tRNA. The surprising fact revealed by structural and biochemical studies is that peptidyl transferase is not a protein enzyme — it is the rRNA of the large ribosomal subunit. The ribosome is a ribozyme, and this discovery supports the idea that protein synthesis evolved in an RNA-based world.

Translation does not begin at just any AUG in the mRNA. Initiation requires signals that position the ribosome at the correct start codon. In prokaryotes, a Shine-Dalgarno sequence a few nucleotides upstream of the AUG base-pairs with the 16S rRNA of the small ribosomal subunit, delivering the ribosome directly to the right position. In eukaryotes, the 40S subunit loads at the 5' cap and scans in the 3' direction until it encounters an AUG in a favorable Kozak context. This difference has profound implications: prokaryotic mRNAs are often polycistronic (multiple genes on one mRNA, each with its own Shine-Dalgarno) while eukaryotic mRNAs are usually monocistronic, translated from a single start site.

The reading frame set at AUG is non-negotiable. Once the ribosome commits to an AUG, it reads every subsequent codon as exactly three nucleotides, without gaps or shifts. This is why a frameshift mutation — a single nucleotide insertion or deletion in the coding sequence — is typically catastrophic: it changes the triplet grouping of every codon downstream, producing a completely garbled amino acid sequence that almost always includes a premature stop codon. A single nucleotide change therefore does not just alter one amino acid; it destroys the entire C-terminal portion of the protein.

Termination is triggered by stop codons (UAA, UAG, UGA), which have no corresponding tRNAs. Instead, protein release factors bind the A site when a stop codon arrives, hydrolyze the bond between the polypeptide and the final tRNA, and release the finished protein. The ribosomal subunits then dissociate and are recycled. In active cells, many ribosomes can translate the same mRNA simultaneously, forming polysomes — a strategy that greatly amplifies protein output from a single mRNA molecule.

