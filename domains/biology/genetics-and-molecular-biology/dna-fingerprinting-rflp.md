---
id: dna-fingerprinting-rflp
title: DNA Fingerprinting and RFLP Analysis
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: restriction-enzymes
  type: hard
- id: gel-electrophoresis
  type: hard
builds-toward:
- dna-barcoding-markers
tags:
- dna-fingerprinting
- rflp
- restriction-fragment-length-polymorphism
- molecular-markers
- forensics
stage: advanced
status: draft
---

# DNA Fingerprinting and RFLP Analysis

## Core Idea
RFLP (Restriction Fragment Length Polymorphism) analysis detects DNA polymorphisms by cutting genomic DNA with restriction enzymes and visualizing different fragment sizes on gels. A single base change can create or eliminate a restriction site, changing fragment patterns and producing distinct banding patterns that identify individuals. DNA fingerprinting exploits minisatellites (hypervariable tandem repeats) to create individually unique banding patterns, standard in forensics and paternity testing.

## Explainer

You already know that **restriction enzymes** cut DNA at specific recognition sequences and that **gel electrophoresis** separates the resulting fragments by size. RFLP analysis combines these two techniques into a powerful method for detecting genetic variation between individuals — without needing to sequence a single base.

The logic is straightforward. Imagine a restriction enzyme that cuts the sequence GAATTC. If person A has this sequence at two nearby positions on a chromosome, the enzyme produces a fragment of, say, 4,000 base pairs between those cuts. But if person B has a single nucleotide polymorphism that changes one GAATTC to GAACTC, the enzyme no longer recognizes that site. The two adjacent fragments in person A now run as one larger fragment in person B — perhaps 7,000 bp. When you run both samples on a gel, person A shows a 4 kb band and person B shows a 7 kb band. This difference — a **restriction fragment length polymorphism** — is a heritable genetic marker that follows Mendelian inheritance, with heterozygotes showing both bands.

**DNA fingerprinting** takes RFLP analysis further by targeting **minisatellites** (also called VNTRs — variable number tandem repeats). These are genomic regions where a short sequence motif is repeated in tandem, and the number of repeats varies enormously between individuals due to unequal crossing over and replication slippage. When you digest genomic DNA and probe for minisatellite regions, each person produces a unique constellation of bands — a molecular fingerprint. Because these loci are so polymorphic, the probability that two unrelated individuals share the same pattern across multiple probes is astronomically small (often less than one in a billion), which is why courts accept DNA fingerprinting as definitive evidence.

In practice, the original RFLP-based fingerprinting developed by Alec Jeffreys in 1984 required substantial amounts of high-quality DNA and took days of Southern blotting. This is why it has been largely replaced by PCR-based microsatellite (STR) analysis for forensic work. But the underlying principle remains the same: natural variation in DNA sequence creates detectable size differences when you have the right molecular tools to reveal them. RFLP analysis also remains important in genetic mapping, where polymorphic restriction sites serve as landmarks for locating genes associated with diseases or traits along chromosomes.
