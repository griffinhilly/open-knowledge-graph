---
id: translation-elongation-and-termination
title: 'Translation Elongation and Termination: Peptide Bond Formation'
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: translation-initiation-and-elongation
  type: hard
- id: ribosomal-rna-and-ribosome-assembly
  type: soft
builds-toward:
- post-translational-modifications
tags:
- elongation-factors
- peptidyl-transferase
- translocase
- release-factors
- stop-codons
stage: formal-systems
status: draft
---

# Translation Elongation and Termination: Peptide Bond Formation

## Core Idea
During translation elongation, aminoacyl-tRNAs are delivered to the A (acceptor) site of the ribosome by elongation factors EF-Tu (prokaryotes) or eEF1A (eukaryotes) in a GTP-dependent manner, with proofreading ensuring accuracy. The peptidyl transferase activity of the ribosome (catalyzed by 23S rRNA in prokaryotes, 28S rRNA in eukaryotes) catalyzes peptide bond formation between the carboxyl group of the P-site peptidyl-tRNA and the amino group of the A-site aminoacyl-tRNA. Elongation factors EF-G (prokaryotes) or eEF2 (eukaryotes) promote translocation, moving tRNAs and mRNA by three nucleotides (one codon), using GTP hydrolysis. Termination occurs when a stop codon (UAA, UAG, or UGA) enters the A site, recognized by release factors (RF1/RF2 in prokaryotes, eRF1/eRF3 in eukaryotes), triggering hydrolysis of the ester bond linking the polypeptide to the tRNA and dissociation of the ribosome from mRNA.

## Explainer

From your study of translation initiation, you know that the ribosome assembles on mRNA with the initiator tRNA positioned in the P site, ready to begin reading codons. Elongation is the repetitive cycle that builds the polypeptide chain one amino acid at a time, and it runs with striking speed and precision — roughly 15–20 amino acids per second in bacteria. The cycle has three steps that repeat for every codon: **delivery**, **peptide bond formation**, and **translocation**.

In the **delivery** step, each new aminoacyl-tRNA arrives at the ribosome's A site as a ternary complex with the elongation factor **EF-Tu** (or **eEF1A** in eukaryotes) and GTP. Think of EF-Tu as a quality-control chaperone: it holds the charged tRNA and allows it to sample the codon in the A site. If the anticodon-codon match is correct, complementary base pairing triggers a conformational change in the ribosome that stimulates GTP hydrolysis by EF-Tu. This is the **kinetic proofreading** step — incorrect tRNAs dissociate before GTP hydrolysis occurs, because they lack the geometric fit needed to trigger the conformational change. The result is an error rate of roughly one misincorporation per 10,000 amino acids, far better than codon-anticodon base pairing alone could achieve.

Once the correct aminoacyl-tRNA is locked into the A site, the **peptidyl transferase** reaction forms the peptide bond. This is catalyzed not by a protein enzyme but by the ribosomal RNA itself — specifically the 23S rRNA (28S in eukaryotes) — making the ribosome a **ribozyme**. The reaction transfers the growing polypeptide chain from the P-site tRNA to the amino group of the A-site aminoacyl-tRNA, extending the chain by one residue. After peptide bond formation, the P site holds a now-empty (deacylated) tRNA and the A site holds the peptidyl-tRNA bearing the entire growing chain. The elongation factor **EF-G** (or **eEF2**) then drives **translocation**: using the energy of GTP hydrolysis, it ratchets the ribosome forward by exactly one codon (three nucleotides), shifting the deacylated tRNA to the E (exit) site and the peptidyl-tRNA to the P site, leaving the A site open for the next incoming aminoacyl-tRNA.

**Termination** breaks this cycle. When a stop codon — **UAA**, **UAG**, or **UGA** — enters the A site, no aminoacyl-tRNA recognizes it. Instead, protein **release factors** bind: in prokaryotes, RF1 recognizes UAA and UAG while RF2 recognizes UAA and UGA; in eukaryotes, a single factor **eRF1** recognizes all three stop codons. The release factor mimics the shape of a tRNA, fitting into the A site and positioning a catalytic domain near the peptidyl transferase center. This triggers hydrolysis of the ester bond connecting the completed polypeptide to the final tRNA, freeing the finished protein. The ribosome then disassembles with help from **ribosome recycling factor** and EF-G (prokaryotes) or from eRF3 and ABCE1 (eukaryotes), releasing the mRNA and ribosomal subunits for reuse. The entire process — from initiation through hundreds or thousands of elongation cycles to termination — produces one complete polypeptide, ready for folding and post-translational modification.
