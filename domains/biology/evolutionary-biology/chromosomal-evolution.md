---
id: chromosomal-evolution
title: Chromosomal Rearrangements and Karyotype Evolution
domain: biology
course: evolutionary-biology
prerequisites:
- id: genome-duplications
  type: hard
- id: reproductive-isolation
  type: hard
- id: chromosomal-theory-of-inheritance
  type: soft
builds-toward:
- speciation
- major-evolutionary-innovations
tags:
- chromosomes
- rearrangement
- karyotype
- evolution
stage: advanced
status: draft
---

# Chromosomal Rearrangements and Karyotype Evolution

## Core Idea
Large-scale chromosomal changes—duplications, deletions, inversions, translocations—reshape genomes. Can create reproductive isolation, suppress recombination near breakpoints, and enable acquisition of novel functions through retained duplicates.

## Questions

```yaml
- question: "A population of birds adapts to two different habitats. An inversion polymorphism is found at high frequency in the coastal population but rarely in the inland population. Genome sequencing reveals that the inversion region contains multiple alleles favoring coastal conditions. Why is the inversion maintained at high frequency in the coastal population?"
  type: multiple-choice
  options:
    - "The inversion spread by genetic drift because the coastal population is small and isolated"
    - "The inversion doubled the dosage of coastal-adaptation genes within the inverted segment"
    - "By suppressing recombination in heterozygotes, the inversion keeps a set of co-adapted coastal alleles together, preventing gene flow from breaking them apart"
    - "The inversion caused chromosomal incompatibility with inland birds, blocking hybridization entirely"
  answer: 2
  explanation: "When individuals heterozygous for an inversion attempt to recombine within the inverted region during meiosis, the resulting crossover products are chromosomally unbalanced (duplications and deletions) and form inviable offspring. This means the entire inverted segment is effectively inherited as a unit — the alleles within it cannot be reshuffled by recombination. If that segment happens to contain multiple alleles that work well together in the coastal environment, the inversion locks them together and allows them to spread as a unit without being disrupted by recombination with inland-adapted chromosomes. This is the 'supergene' principle. Options A and B are not the correct mechanism here; option D describes a real consequence of extensive rearrangement but not the primary adaptive mechanism of a single inversion."

- question: "An inversion heterozygote (carrying one normal and one inverted chromosome) typically shows reduced fertility compared to inversion homozygotes. What is the mechanistic reason?"
  type: multiple-choice
  options:
    - "The inverted chromosome cannot be read by the transcriptional machinery because the gene order is reversed"
    - "The two chromosomes fail to pair during meiosis I because they cannot find complementary sequences"
    - "Crossovers within the inverted region produce chromosomes with duplications and deletions, generating inviable gametes"
    - "The inversion prevents proper kinetochore attachment, causing nondisjunction at the first meiotic division"
  answer: 2
  explanation: "In a heterozygote with one normal and one inverted chromosome, synapsis during meiosis requires the inverted chromosome to loop back on itself to allow pairing. If a crossover occurs within the looped region, the recombinant chromatids will have duplications of sequences on one side of the inversion and deletions on the other — they carry unbalanced chromosomal content. Zygotes receiving these gametes typically abort early. The effect is a strong selection against recombination within the inverted region in heterozygotes, which is exactly what creates the supergene effect. The transcription machinery (option A) reads genes by sequence, not position, so gene order reversal is typically tolerated; what matters is whether the regulatory sequences are disrupted."

- question: "Chromosomal fusions (two chromosomes merging into one) and fissions (one chromosome splitting into two) change the chromosome number but do not add or remove genetic material from the genome."
  type: true-false
  answer: true
  explanation: "Fusions and fissions are rearrangements of existing genetic material, not duplications or deletions. A fusion reduces the chromosome number by one (as in the human chromosome 2 fusion that distinguishes our karyotype from chimpanzees') but all the genes from both ancestral chromosomes are present in the resulting single chromosome. A fission increases the chromosome number by one but no material is lost. What does change is the mechanics of meiosis (now one fewer or one more pairing event is required) and potentially effective recombination rates genome-wide — consequences that can have significant evolutionary effects without any change in total gene content."

- question: "Because inversions suppress recombination in heterozygotes, they are evolutionarily disadvantageous and spread only by neutral genetic drift, never by positive selection."
  type: true-false
  answer: false
  explanation: "Inversions can be strongly positively selected precisely *because* they suppress recombination. When a chromosomal region contains multiple alleles that function well together in a particular environment, natural selection favors mechanisms that keep those combinations intact. An inversion that captures co-adapted alleles spreads because the inversion-bearing chromosomes produce better-adapted offspring than chromosomes that allow recombination to break up the favorable combinations. The 'supergene' inversions found in migratory birds, social insects, and coastal adaptation in fish are maintained at high frequencies by selection — the suppression of recombination is the adaptive mechanism, not an unfortunate side effect."

- question: "Why are chromosomal inversions described as 'supergenes,' and what advantage does this property provide to locally adapted populations experiencing gene flow from other populations?"
  type: short-answer
  answer: "An inversion acts as a supergene because it locks together all the alleles within the inverted region into a single non-recombining unit. In heterozygotes, crossovers within the inversion produce unbalanced, inviable chromosomes — so recombination within the region is effectively eliminated. The entire inverted segment is inherited intact, as if it were a single gene. For a population locally adapted to a specific environment, this is valuable when gene flow from a population with different adaptations would otherwise break up co-adapted allele combinations. The inversion preserves the set of locally adapted alleles as a package that spreads together or not at all, maintaining local adaptation despite ongoing hybridization with genetically different populations."
  explanation: "The classic examples are inversions in the ruff (a shorebird with alternative male strategies encoded in a supergene), the *Heliconius* butterfly wing pattern loci, and adaptation to salinity, altitude, and temperature across multiple species. In each case, multiple alleles that collectively confer advantage in a specific context are held together by an inversion that resists the homogenizing effect of recombination."
```

## Explainer

From your study of genome duplications, you know that entire genomes or large segments can be copied, providing raw material for evolutionary innovation. **Chromosomal evolution** extends this perspective to the full range of large-scale structural changes that reshape genomes over time: not just duplications, but also **inversions** (a segment flips orientation), **translocations** (a segment moves to a different chromosome), **fusions** (two chromosomes merge into one), and **fissions** (one chromosome splits into two). These rearrangements alter the karyotype — the number, size, and shape of chromosomes — and comparing karyotypes across species reveals the history of genomic restructuring that accompanied their divergence.

The most immediate evolutionary consequence of chromosomal rearrangements is their effect on **recombination**. Consider an inversion: when a segment of chromosome is flipped relative to the ancestral arrangement, individuals heterozygous for the inversion (carrying one normal and one inverted chromosome) cannot recombine normally within the inverted region. During meiosis, crossovers within the inversion produce unbalanced gametes — with duplications and deletions — that are inviable. The result is that inversions effectively lock together all the genes within the inverted segment, preventing recombination from breaking up co-adapted gene combinations. This is why inversions are often found harboring clusters of locally adapted alleles: the inversion acts as a "supergene" that keeps beneficial allele combinations together despite gene flow from populations with different adaptations.

Chromosomal rearrangements also play a direct role in **reproductive isolation**, a concept you studied as a prerequisite. When two populations accumulate different chromosomal rearrangements, hybrids between them may be partially or fully sterile. A translocation heterozygote, for instance, can produce unbalanced gametes during meiosis because the rearranged and normal chromosomes segregate improperly. If enough rearrangements accumulate, the fitness of hybrids drops substantially, reinforcing the genetic separation between the two populations. This is thought to be one mechanism by which speciation proceeds — not through any single dramatic mutation, but through the gradual accumulation of rearrangements that collectively make hybridization costly. The comparison between human and chimpanzee karyotypes illustrates this beautifully: humans have 23 chromosome pairs while chimps have 24, because two ancestral chromosomes fused into human chromosome 2. This fusion, along with at least nine major inversions, occurred in the roughly six million years since our lineages diverged.

On longer evolutionary timescales, chromosomal rearrangements contribute to genome architecture in ways that extend beyond individual genes. Translocations can move genes into new regulatory neighborhoods, placing them under the control of different enhancers and potentially changing their expression patterns — a mechanism for evolutionary novelty that operates without any change to the gene's coding sequence. Fusions and fissions change the total chromosome number, which affects the mechanics of meiosis and can influence effective recombination rates genome-wide. The extraordinary variation in chromosome number across life — from a single chromosome pair in the jack jumper ant to over 600 pairs in some ferns — testifies to the dynamic nature of karyotype evolution and its capacity to reshape the genetic landscape within which natural selection operates.
