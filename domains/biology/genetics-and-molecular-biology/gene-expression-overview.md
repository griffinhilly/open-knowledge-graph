---
id: gene-expression-overview
title: Central Dogma of Molecular Biology
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: dna-structure
  type: hard
- id: ribosomes-and-protein-synthesis-intro
  type: soft
builds-toward:
- transcription
- translation
- gene-regulation-prokaryotes
tags:
- central-dogma
- gene-expression
- DNA
- RNA
- protein
stage: advanced
status: validated
---

# Central Dogma of Molecular Biology

## Core Idea
The central dogma of molecular biology describes the directional flow of genetic information: DNA is transcribed into RNA, which is then translated into protein. DNA also replicates to pass information to daughter cells. This framework, articulated by Francis Crick in 1958, defines the canonical path by which stored genetic sequence becomes functional molecules. Exceptions such as reverse transcription (RNA to DNA) in retroviruses exist but do not contradict the general principle that protein sequence cannot be reverse-translated back into nucleic acid.

## How It's Best Learned
Diagram the three processes — replication, transcription, translation — with arrows indicating direction of information flow. Connect each step to a specific cellular location (nucleus vs. cytoplasm in eukaryotes).

## Common Misconceptions
- The dogma is sometimes misstated as 'DNA makes RNA makes protein' with no other possibilities; reverse transcription is a real exception.
- Information flows from sequence to sequence, not from chemistry to sequence — environmental conditions do not rewrite DNA in Lamarckian fashion.

## Questions

```yaml
- question: "Which of the following correctly describes what the central dogma rules out as impossible?"
  type: multiple-choice
  options: ["RNA being copied into DNA", "DNA being replicated before cell division", "Protein sequence being used to write a new DNA or RNA sequence", "A single gene producing multiple protein variants"]
  answer: 2
  explanation: "The central dogma's core claim is that information cannot flow from protein back into nucleic acid. RNA-to-DNA (reverse transcription) does occur in retroviruses and was anticipated as an exception. DNA replication and alternative splicing are normal biological processes. What is forbidden is translating an amino acid sequence back into a nucleotide sequence."

- question: "The discovery of reverse transcriptase in retroviruses disproves the central dogma of molecular biology."
  type: true-false
  answer: false
  explanation: "Crick explicitly noted that RNA-to-DNA information flow was a theoretical possibility he called a 'special transfer.' Retroviruses confirmed this exception. What the central dogma absolutely prohibits — and what has never been observed — is protein-to-nucleic-acid information flow. The discovery of reverse transcription extended the dogma, it did not invalidate it."

- question: "Why can't a cell use a protein's amino acid sequence to reconstruct the exact DNA sequence that encoded it?"
  type: short-answer
  answer: "The genetic code is degenerate — multiple codons encode the same amino acid — so the protein sequence does not preserve which specific codon was used, making exact back-translation impossible."
  explanation: "For example, leucine is encoded by six different codons (UUA, UUG, CUU, CUC, CUA, CUG). Given a leucine in a protein, you cannot tell which codon was originally used. This degeneracy is one-directional: DNA → protein loses information, so the reverse is not recoverable from sequence alone."
```

## Explainer

From your study of DNA structure, you know that DNA is a double-stranded polymer encoding information in the sequence of its bases. But DNA itself does nothing — it is an inert archive. The central dogma describes how that stored information gets converted into molecules that actually *do* things: proteins. Francis Crick's 1958 formulation identified three processes: DNA replicates to copy itself, DNA is transcribed into RNA, and RNA is translated into protein. The arrow of information always points away from DNA and toward protein, never in reverse.

Think of DNA as a master blueprint locked in the nucleus (in eukaryotes). You would never let workers handle the original, so instead you make a working copy — messenger RNA — and send that to the construction site. The ribosome, guided by the mRNA sequence, assembles the protein by reading each three-nucleotide codon and adding the corresponding amino acid. The sequence of the mRNA dictates the sequence of the protein, which in turn determines the protein's shape and function. Information flows from one type of molecule to another, but the information content — the sequence — is what is preserved.

The most important conceptual boundary the central dogma draws is at protein. Once information has been translated into an amino acid sequence, it cannot flow back into nucleic acid. This rules out Lamarckian inheritance: a muscle you develop through exercise does not write that information back into your DNA to pass on to children. It also explains why acquired characteristics — scars, skills, environmental adaptations in the body — are not heritable at the genetic level. The body changes, but the genome's sequence does not (barring mutations).

Retroviruses like HIV complicate the simple "DNA → RNA → protein" summary: their genome is RNA, and they carry reverse transcriptase, an enzyme that writes RNA information back into DNA. This DNA then integrates into the host chromosome as a provirus. This is a genuine exception to the transcription arrow, but it does not violate the core constraint — reverse transcriptase makes DNA from RNA, but no enzyme writes DNA from protein. Knowing this exception matters because reverse transcriptase is also a drug target: HIV antiretrovirals inhibit this enzyme precisely because it is absent in human cells.
