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

## Questions

```yaml
- question: "A restriction enzyme recognizes GAATTC. Person X is heterozygous: one chromosome has this site intact between two flanking cuts (producing a 4 kb fragment), while the other chromosome has a mutation that destroys this internal site. What banding pattern appears when Person X's DNA is run on a gel?"
  type: multiple-choice
  options:
    - "Two bands: 4 kb and 7 kb"
    - "One band: 7 kb (the mutation always dominates on a gel)"
    - "Three bands: one at 4 kb, one at 3 kb, and one at 7 kb"
    - "No bands — heterozygosity prevents clear fragment separation"
  answer: 2
  explanation: "A heterozygote has two alleles: the intact chromosome produces the 4 kb fragment (the enzyme cuts at both flanking sites and the internal site); the mutant chromosome lacks the internal site, so the enzyme produces only one larger fragment spanning the distance covered by the 4 kb + 3 kb segments — typically 7 kb. Both alleles' DNA is present in the sample, so the gel shows all products: the 4 kb and 3 kb bands from the intact chromosome AND the 7 kb band from the mutant chromosome — three bands total. Option A (just two bands) would describe a homozygous normal individual; only heterozygotes show three."

- question: "Why do VNTR (minisatellite) loci produce individually unique banding patterns suitable for forensic identification, while a typical restriction site polymorphism at a single locus usually has only two alleles?"
  type: multiple-choice
  options:
    - "VNTR loci are located in coding regions where mutations accumulate faster than at non-coding restriction sites"
    - "VNTRs have a short tandem repeat motif that varies in copy number between individuals due to unequal crossing over and replication slippage, creating dozens to hundreds of distinct alleles rather than just two"
    - "VNTR loci are near centromeres and therefore experience more mutation per generation"
    - "Restriction site polymorphisms occur only once per genome, but VNTRs occur in multiple locations simultaneously"
  answer: 1
  explanation: "The power of VNTR-based fingerprinting comes from the mechanism of variation. Minisatellites consist of a short repeat unit (e.g., a 16 bp motif) that can occur in tandem 10, 20, 50, or 200+ times — and unequal crossing over or polymerase slippage during replication can increase or decrease this count. The result is dozens to hundreds of distinct alleles per locus. At multiple independent VNTR loci, the probability of two unrelated individuals sharing the same multi-locus pattern becomes astronomically small. A single-nucleotide restriction site polymorphism, by contrast, is biallelic — the site either exists or it doesn't — providing much less discriminatory power."

- question: "RFLP analysis requires sequencing the individual's DNA to identify genetic differences, since the underlying single nucleotide changes are too small to detect by gel electrophoresis alone."
  type: true-false
  answer: false
  explanation: "This is precisely what makes RFLP analysis powerful — it reveals genetic differences without sequencing. A single nucleotide change that creates or destroys a restriction site changes the size of the resulting fragment, and fragment size differences of even a few hundred base pairs are readily resolved by gel electrophoresis. The gel image translates molecular genetic variation directly into visible banding patterns. RFLP was developed specifically to detect polymorphisms efficiently before sequencing was fast or cheap, and the underlying principle remains: you're measuring the consequence of the mutation (fragment size) rather than reading the mutation itself."

- question: "A single nucleotide change in a DNA sequence can produce a detectably different banding pattern on an agarose gel following restriction enzyme digestion."
  type: true-false
  answer: true
  explanation: "If the single nucleotide change occurs within a restriction enzyme's recognition sequence, it eliminates (or creates) a cut site. This converts two smaller fragments into one larger fragment (or vice versa) — a size difference easily detected by gel electrophoresis. For example, changing GAATTC (EcoRI site) to GAACTC by a single transversion eliminates the cut site entirely, merging two bands into one larger band. This is the molecular basis of RFLP analysis: restriction fragment length polymorphisms exist because individuals differ in which restriction sites they carry, and those differences in restriction sites are often caused by single nucleotide changes."

- question: "Explain how RFLP analysis could be used to identify the biological parents of an individual, even without sequencing their DNA."
  type: short-answer
  answer: "RFLP-based parentage testing works because restriction fragment patterns are heritable — a child must receive one allele at each locus from each parent. If you digest the child's DNA and both parents' DNA with the same restriction enzyme panel and run the fragments on a gel, each child's band must be present in at least one parent at every polymorphic locus. A 7 kb band in the child that appears in the mother's profile but not the father's confirms maternal inheritance; a 4 kb band in the child that matches the alleged father but no other candidate provides paternity evidence. The more polymorphic loci analyzed, the lower the probability that a non-parent could match by chance. For minisatellite VNTR-based fingerprinting, multi-locus profiles can establish parentage with virtual certainty."
  explanation: "Parentage testing illustrates Mendelian logic applied at the molecular level. Each RFLP band corresponds to an allele inherited from one parent or the other. Exclusion (a band in the child that cannot be in either parent) rules out parentage; inclusion across many loci establishes it statistically. Modern STR-based testing uses the same logic but with PCR-amplified microsatellites, giving greater sensitivity and the ability to work with degraded or tiny samples — but the conceptual foundation is identical to Jeffreys' original RFLP approach."
```

## Explainer

You already know that **restriction enzymes** cut DNA at specific recognition sequences and that **gel electrophoresis** separates the resulting fragments by size. RFLP analysis combines these two techniques into a powerful method for detecting genetic variation between individuals — without needing to sequence a single base.

The logic is straightforward. Imagine a restriction enzyme that cuts the sequence GAATTC. If person A has this sequence at two nearby positions on a chromosome, the enzyme produces a fragment of, say, 4,000 base pairs between those cuts. But if person B has a single nucleotide polymorphism that changes one GAATTC to GAACTC, the enzyme no longer recognizes that site. The two adjacent fragments in person A now run as one larger fragment in person B — perhaps 7,000 bp. When you run both samples on a gel, person A shows a 4 kb band and person B shows a 7 kb band. This difference — a **restriction fragment length polymorphism** — is a heritable genetic marker that follows Mendelian inheritance, with heterozygotes showing both bands.

**DNA fingerprinting** takes RFLP analysis further by targeting **minisatellites** (also called VNTRs — variable number tandem repeats). These are genomic regions where a short sequence motif is repeated in tandem, and the number of repeats varies enormously between individuals due to unequal crossing over and replication slippage. When you digest genomic DNA and probe for minisatellite regions, each person produces a unique constellation of bands — a molecular fingerprint. Because these loci are so polymorphic, the probability that two unrelated individuals share the same pattern across multiple probes is astronomically small (often less than one in a billion), which is why courts accept DNA fingerprinting as definitive evidence.

In practice, the original RFLP-based fingerprinting developed by Alec Jeffreys in 1984 required substantial amounts of high-quality DNA and took days of Southern blotting. This is why it has been largely replaced by PCR-based microsatellite (STR) analysis for forensic work. But the underlying principle remains the same: natural variation in DNA sequence creates detectable size differences when you have the right molecular tools to reveal them. RFLP analysis also remains important in genetic mapping, where polymorphic restriction sites serve as landmarks for locating genes associated with diseases or traits along chromosomes.
