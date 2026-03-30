---
id: long-read-sequencing
title: Long-Read Sequencing Technologies
domain: biology
course: genomics-and-bioinformatics
prerequisites:
- id: dna-sequencing-technologies
  type: hard
- id: genome-assembly
  type: hard
builds-toward:
- spatial-transcriptomics
- multi-omics-integration
tags:
- PacBio
- Oxford-Nanopore
- long-reads
- HiFi
- structural-variants
- direct-RNA-sequencing
stage: expert
status: validated
---
# Long-Read Sequencing Technologies

## Core Idea
Long-read sequencing platforms (PacBio and Oxford Nanopore) produce reads of 10,000 to over 100,000 base pairs, overcoming the fundamental limitation of short-read technologies in resolving repetitive regions, structural variants, and complex genomic rearrangements. PacBio's HiFi mode generates highly accurate long reads (~99.9% at 15-20 kb) through circular consensus sequencing. Oxford Nanopore sequences single DNA or RNA molecules in real time by measuring current changes as they pass through a protein nanopore, enabling ultra-long reads (>1 Mb) and direct detection of base modifications without bisulfite conversion. These technologies have enabled telomere-to-telomere genome assemblies, comprehensive structural variant detection, and full-length transcript sequencing.

## How It's Best Learned
Compare assemblies of the same genome using short reads alone versus long reads alone versus a hybrid approach. Examine how repeat-rich regions (centromeres, segmental duplications) that were gaps in the short-read assembly become resolved with long reads. Then visualize structural variant calls from long reads and see how many were invisible to short-read analysis.

## Common Misconceptions
- Long-read sequencing is not universally better than short-read sequencing — short reads remain more cost-effective for applications like RNA-seq quantification and variant calling in non-repetitive regions where read length does not matter.
- Oxford Nanopore's raw error rate (~5-10%) does not mean the final results are inaccurate — consensus from multiple reads or correction with short reads brings accuracy to 99.99%+.

## Questions

```yaml
- question: "What is the key advantage of PacBio HiFi reads over traditional PacBio CLR (continuous long reads)?"
  type: multiple-choice
  options: ["HiFi reads are longer", "HiFi reads achieve high accuracy (~99.9%) by circularizing the DNA molecule and sequencing it multiple times", "HiFi reads do not require library preparation", "HiFi reads can sequence RNA directly"]
  answer: 1
  explanation: "PacBio HiFi uses circular consensus sequencing (CCS): a DNA molecule is circularized with adapters, and the polymerase reads around the circle multiple times. Each pass has ~10-15% error, but errors are random, so consensus across 10-20 passes yields a single read with ~99.9% accuracy at 15-20 kb length. This combines long-read advantages (spanning repeats, resolving structural variants) with short-read-level accuracy, making HiFi the current gold standard for de novo genome assembly."

- question: "Oxford Nanopore sequencing requires PCR amplification of the DNA before sequencing."
  type: true-false
  answer: false
  explanation: "Oxford Nanopore can sequence native DNA directly without amplification, which is one of its key advantages. The DNA molecule (or RNA, for direct RNA sequencing) is driven through a protein nanopore embedded in a membrane, and changes in ionic current as each base passes through the pore are measured in real time. This preserves base modifications (methylation, hydroxymethylation) that would be erased by PCR amplification. Amplification-free protocols also eliminate PCR bias. However, amplified libraries can be used when input DNA is limited."

- question: "Explain why long reads are essential for resolving structural variants that short-read sequencing misses."
  type: short-answer
  answer: "Structural variants (SVs) — insertions, deletions, inversions, duplications, and translocations >50 bp — often involve or are flanked by repetitive sequences. Short reads (150-300 bp) cannot span these events: a 5-kb deletion flanked by homologous repeats produces ambiguous short-read alignments because the reads from flanking repeats map to multiple locations. Long reads spanning the entire SV, including both breakpoints and flanking unique sequences, resolve the variant unambiguously. Studies comparing short-read and long-read SV calling on the same genomes find that long reads detect 2-3 times more SVs, revealing a previously hidden layer of genetic variation."
  explanation: "The T2T (Telomere-to-Telomere) Consortium used ultra-long Oxford Nanopore reads and PacBio HiFi to complete the first gapless human genome assembly in 2022, filling in centromeres, segmental duplications, and telomeres that had been missing from the human reference for 20 years. This required reads long enough to span the megabase-scale tandem repeats in centromeric regions."
```

## Explainer

The Illumina sequencing revolution made genomics affordable, but it introduced a fundamental limitation: read lengths of 150-300 bp cannot resolve genomic features longer than themselves. Repetitive elements (which comprise half the human genome), structural variants, full-length transcript isoforms, and base modifications all require longer reads to study comprehensively. Third-generation long-read sequencing, pioneered by Pacific Biosciences and Oxford Nanopore Technologies, addresses these limitations with fundamentally different approaches to reading DNA.

**PacBio** sequencing uses single-molecule real-time (SMRT) sequencing: a DNA polymerase is fixed at the bottom of a tiny well (zero-mode waveguide), and fluorescently labeled nucleotides are incorporated in real time, with each incorporation producing a light pulse that identifies the base. The original continuous long-read (CLR) mode produced reads averaging 10-20 kb but with 10-15% error rate. The breakthrough came with **HiFi** (high-fidelity) reads: the template DNA is circularized, and the polymerase reads around the circle multiple times. Consensus across multiple passes of the same molecule reduces the error rate to ~0.1% (Q30), while maintaining read lengths of 15-20 kb. HiFi reads combine the two properties that were previously mutually exclusive: long length and high accuracy.

**Oxford Nanopore** takes a radically different approach. A single-stranded DNA (or RNA) molecule is ratcheted through a protein nanopore embedded in a synthetic membrane. As each base passes through the pore, it modulates the ionic current flowing through the pore. A neural network base-caller translates the raw current signal into a nucleotide sequence. Read length is limited only by the input DNA fragment length — reads of 1 Mb+ have been demonstrated, and typical reads are 10-100 kb. The raw error rate is higher (~5-10%) than HiFi, but newer base-callers and consensus approaches are rapidly improving accuracy. A unique advantage is **direct modification detection**: because the current signal is affected by base modifications (5-methylcytosine, 6-methyladenine), Nanopore can detect epigenetic marks on native DNA without bisulfite treatment or antibody enrichment.

These technologies have transformed several areas of genomics. **De novo assembly** benefits most dramatically: HiFi reads produce assemblies with N50s of tens of megabases, compared to tens of kilobases for short-read assemblies of the same genome. The T2T Consortium used long reads to complete the first gapless human genome, adding 200 Mb of sequence (including centromeres and short arms of acrocentric chromosomes) that were missing from GRCh38. **Structural variant calling** reveals the full spectrum of genomic variation, with long reads detecting thousands of SVs invisible to short-read methods. **Full-length transcript sequencing** (PacBio Iso-Seq, Nanopore direct RNA) captures complete isoforms without assembly, resolving alternative splicing and gene fusion events at single-molecule resolution. The tradeoff remains cost: per-base, long-read sequencing is more expensive than Illumina, though the gap narrows continuously.
