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

## Questions

```yaml
- question: "In tetrad analysis of a heterozygous yeast strain (Aa), a researcher observes 3 A spores and 1 a spore from a single meiosis rather than the expected 2:2 ratio. This 3:1 ratio is most directly explained by:"
  type: multiple-choice
  options:
    - "Nondisjunction during meiosis II, causing one A chromosome to be mis-segregated"
    - "A crossover occurring between the A and a loci that swapped the entire chromosomal arm"
    - "Gene conversion: mismatch repair of heteroduplex DNA replaced the a allele sequence with a copy of the A allele sequence on one chromatid"
    - "The a allele having a growth disadvantage that caused the a spore to divide fewer times"
  answer: 2
  explanation: "A 3:1 spore ratio (instead of the Mendelian 2:2) is the hallmark of gene conversion. During recombination, strand invasion creates heteroduplex DNA where one strand comes from each homolog. If the two alleles differ at a nucleotide in this heteroduplex region, a mismatch forms. Mismatch repair can resolve this by overwriting the a sequence with the A sequence (or vice versa), converting one chromatid's allele. Nondisjunction would produce aneuploid spores, not a 3:1 ratio. A simple crossover would still give 2:2 ratios at the point of exchange."

- question: "Biased gene conversion at a locus in a large population favors GC alleles over AT alleles during mismatch repair. What population-level consequence would you expect over many generations?"
  type: multiple-choice
  options:
    - "GC alleles would decrease in frequency because they are more likely to be repaired away"
    - "No change in allele frequencies, because gene conversion is random by definition"
    - "GC alleles would increase in frequency regardless of their fitness effects, because the repair bias acts as a weak directional force independent of natural selection"
    - "GC alleles would increase only if they also confer a selective advantage"
  answer: 2
  explanation: "Biased gene conversion acts like directional selection: in every heterozygote, mismatch repair slightly favors copying the GC allele onto the AT chromosome rather than the reverse. This directional repair bias systematically shifts allele frequencies toward GC at recombination hotspots over generations, independently of whether GC alleles are beneficial, neutral, or even slightly deleterious. This is why recombination hotspots tend to be GC-rich in the genome — not because GC content has a functional advantage there, but because of the physical chemistry of mismatch repair."

- question: "In standard reciprocal crossing over between homologs, a heterozygote (Aa) produces gametes in a 2:2 ratio (2 A and 2 a), while gene conversion at the same locus can produce a 3:1 or even 4:0 ratio."
  type: true-false
  answer: true
  explanation: "Reciprocal crossing over physically exchanges chromosomal segments between homologs symmetrically — what one chromosome gives, the other receives. A heterozygote therefore still has one A chromatid and one a chromatid after crossing over, giving 2A:2a in the final products. Gene conversion is nonreciprocal: one allele overwrites the other without an equal exchange in the opposite direction. Mismatch repair converts one copy of (say) the a allele to A, yielding 3A:1a. In principle, if both heteroduplex mismatches are repaired the same way, a 4:0 ratio is possible, though rare."

- question: "Gene conversion involves an unequal physical exchange of chromosomal segments, where one chromosome receives more sequence than it gives to its homolog."
  type: true-false
  answer: false
  explanation: "Gene conversion does not involve a physical exchange of chromosomal material at all. It is a nonreciprocal information transfer: during mismatch repair of heteroduplex DNA, one strand is rewritten to match the other, but no chromosomal segment physically moves from one chromosome to the other. Both chromosomes remain intact in terms of segment composition — what changes is the sequence of one allele, overwritten to match the donor sequence. Unequal crossing over (a different event) does involve asymmetric physical exchange, but that is distinct from gene conversion."

- question: "Explain how heteroduplex DNA and mismatch repair together produce gene conversion, and why the information transfer is nonreciprocal."
  type: short-answer
  answer: "During meiotic recombination, Spo11 creates a double-strand break and the ends are resected to expose single-stranded tails. One tail invades the homologous chromosome and base-pairs with the complementary strand, displacing the other strand. The region where one strand comes from one chromosome and the other strand from the homolog is called heteroduplex DNA. If the two chromosomes differ at a nucleotide within this region, the result is a mismatched base pair. Mismatch repair enzymes detect and correct this mismatch, but they can only rewrite one strand to match the other — not exchange information symmetrically. If the invading strand is rewritten, the original allele is restored; if the resident strand is rewritten, it now carries the invader's sequence. Either way, one allele has been overwritten by the other — gene conversion — and information flowed in one direction only."
  explanation: "The nonreciprocity follows directly from the repair mechanism: repair converts the mismatch to a Watson-Crick base pair by editing one strand, not by swapping segments. The chromosome that 'donated' the sequence is unchanged; only the 'recipient' chromosome is altered. This contrasts with reciprocal crossing over, where both chromosomes exchange physically equivalent segments and both are modified symmetrically."
```

## Explainer

From your study of meiosis and meiotic recombination, you know that homologous chromosomes pair up and undergo crossing over, exchanging segments of DNA. In a standard crossover, the exchange is **reciprocal** — each chromosome gives and receives equally, so a heterozygote (Aa) produces two A gametes and two a gametes from one meiosis, exactly as Mendel predicted. **Gene conversion** violates this expectation. Instead of a 2:2 ratio, you observe a 3:1 ratio — one allele has been "converted" to the other, as if one chromosome copied its sequence onto the homolog.

To understand how this happens, recall the molecular mechanism of crossing over. Recombination begins when an enzyme called Spo11 creates a double-strand break in one chromosome. The broken ends are processed to expose single-stranded tails, and one of these tails invades the homologous chromosome, base-pairing with the complementary strand and displacing the other strand. This creates a region of **heteroduplex DNA** — a stretch where one strand comes from one homolog and the other strand comes from the other. If the two homologs differ at a nucleotide within this heteroduplex region, the result is a mismatch (for example, A paired with C instead of the expected A-T or G-C).

The cell's **mismatch repair** machinery detects this heteroduplex mismatch and "fixes" it — but it can only correct one strand to match the other. If it repairs the invading strand to match the template, the original allele is restored. But if it repairs the template strand to match the invader, the recipient chromosome now carries the donor's allele. Either way, one allele has been copied over the other, producing the 3:1 segregation pattern. The conversion is nonreciprocal because information flows in one direction — one allele overwrites the other rather than both being exchanged.

Gene conversion has surprisingly important evolutionary consequences. If the repair machinery has even a slight preference for certain nucleotides — and evidence shows it favors G/C over A/T at mismatches — then **biased gene conversion** acts like a weak selective force, driving GC-rich alleles to higher frequency in the population regardless of their fitness effects. This GC-biased gene conversion helps explain why recombination hotspots in genomes tend to have elevated GC content. Gene conversion also homogenizes multigene families: ribosomal RNA genes exist in hundreds of tandem copies, and frequent gene conversion among copies keeps them nearly identical, a phenomenon called **concerted evolution**. Without gene conversion, these copies would gradually diverge through independent mutations.
