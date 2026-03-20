---
id: gene-conversion-meiotic
title: Gene Conversion and Nonreciprocal Recombination
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: meiosis
  type: hard
- id: meiotic-recombination-crossing-over
  type: hard
builds-toward:
- unequal-crossing-over-duplication
tags:
- gene-conversion
- recombination
- biased-inheritance
- meiotic-drive
stage: advanced
status: draft
---

# Gene Conversion and Nonreciprocal Recombination

## Core Idea
Gene conversion is a nonreciprocal recombination event where one DNA sequence is replaced by a copy of a homologous sequence, creating asymmetric inheritance (one parent's allele appears in both products of meiosis). Gene conversion occurs during meiotic recombination through mismatch repair of heteroduplex DNA formed during strand invasion. Biased gene conversion, where certain alleles preferentially copy from heterozygotes, can spread alleles through populations independent of natural selection.

## Explainer

From your study of meiosis and meiotic recombination, you know that homologous chromosomes pair up and undergo crossing over, exchanging segments of DNA. In a standard crossover, the exchange is **reciprocal** — each chromosome gives and receives equally, so a heterozygote (Aa) produces two A gametes and two a gametes from one meiosis, exactly as Mendel predicted. **Gene conversion** violates this expectation. Instead of a 2:2 ratio, you observe a 3:1 ratio — one allele has been "converted" to the other, as if one chromosome copied its sequence onto the homolog.

To understand how this happens, recall the molecular mechanism of crossing over. Recombination begins when an enzyme called Spo11 creates a double-strand break in one chromosome. The broken ends are processed to expose single-stranded tails, and one of these tails invades the homologous chromosome, base-pairing with the complementary strand and displacing the other strand. This creates a region of **heteroduplex DNA** — a stretch where one strand comes from one homolog and the other strand comes from the other. If the two homologs differ at a nucleotide within this heteroduplex region, the result is a mismatch (for example, A paired with C instead of the expected A-T or G-C).

The cell's **mismatch repair** machinery detects this heteroduplex mismatch and "fixes" it — but it can only correct one strand to match the other. If it repairs the invading strand to match the template, the original allele is restored. But if it repairs the template strand to match the invader, the recipient chromosome now carries the donor's allele. Either way, one allele has been copied over the other, producing the 3:1 segregation pattern. The conversion is nonreciprocal because information flows in one direction — one allele overwrites the other rather than both being exchanged.

Gene conversion has surprisingly important evolutionary consequences. If the repair machinery has even a slight preference for certain nucleotides — and evidence shows it favors G/C over A/T at mismatches — then **biased gene conversion** acts like a weak selective force, driving GC-rich alleles to higher frequency in the population regardless of their fitness effects. This GC-biased gene conversion helps explain why recombination hotspots in genomes tend to have elevated GC content. Gene conversion also homogenizes multigene families: ribosomal RNA genes exist in hundreds of tandem copies, and frequent gene conversion among copies keeps them nearly identical, a phenomenon called **concerted evolution**. Without gene conversion, these copies would gradually diverge through independent mutations.
