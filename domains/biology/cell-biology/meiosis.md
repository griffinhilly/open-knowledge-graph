---
id: meiosis
title: Meiosis
domain: biology
course: cell-biology
prerequisites:
- id: mitosis
  type: hard
- id: nucleus-and-genetic-material
  type: hard
- id: cytokinesis
  type: soft
tags:
- meiosis
- sexual-reproduction
- gametes
- crossing-over
- haploid
stage: advanced
status: validated
---
# Meiosis

## Core Idea
Meiosis is a specialized form of cell division that produces four genetically unique haploid cells (gametes) from one diploid precursor. It consists of two rounds of division: meiosis I separates homologous chromosome pairs (reducing chromosome number by half), and meiosis II separates sister chromatids (analogous to mitosis). Genetic diversity is generated through independent assortment of homologous chromosomes and crossing over (recombination) during prophase I, when non-sister chromatids of homologs exchange segments at chiasmata. Errors in meiosis (nondisjunction) cause chromosomal aneuploidies.

## How It's Best Learned
Diagram meiosis I and II for a cell with 2n=4, tracking each chromosome through both divisions. Compare to mitosis at each equivalent stage. Explicitly work through how crossing over and independent assortment generate new allele combinations.

## Common Misconceptions
- Meiosis II is NOT a repeat of meiosis I — meiosis II separates sister chromatids (like mitosis), while meiosis I separates homologs.
- Crossing over happens during prophase I, not prophase II. By prophase II, chromosomes are already haploid.

## Questions

```yaml
- question: "What is the key mechanistic difference between meiosis I and meiosis II?"
  type: multiple-choice
  options: ["Meiosis I replicates DNA; meiosis II separates chromosomes", "Meiosis I separates homologous chromosomes; meiosis II separates sister chromatids", "Meiosis I produces haploid cells; meiosis II produces diploid cells", "Meiosis I occurs in somatic cells; meiosis II occurs in germ cells"]
  answer: 1
  explanation: "Meiosis I is the reductional division: it separates the two members of each homologous pair, cutting the chromosome number in half (diploid → haploid). Meiosis II is the equational division: it separates sister chromatids within each already-haploid cell, analogous to mitosis. DNA replication occurs before meiosis I (in S phase), not during. Both divisions occur in germ cells."

- question: "Crossing over during meiosis occurs in prophase II, after the chromosome number has already been reduced."
  type: true-false
  answer: false
  explanation: "Crossing over (recombination) occurs during prophase I, when homologous chromosomes are paired in a structure called the synaptonemal complex. This is the only time homologs are close enough to exchange segments at chiasmata. By prophase II, the cell is already haploid — homologs have separated — so there are no homolog pairs present for crossing over to occur between."

- question: "Meiosis generates genetic diversity through two distinct mechanisms. Name both mechanisms and explain how each contributes to variation in gametes."
  type: short-answer
  answer: "Independent assortment: during meiosis I, each pair of homologous chromosomes aligns randomly at the metaphase plate, so the maternal or paternal version of each chromosome is independently inherited. Crossing over: during prophase I, non-sister chromatids of homologs exchange segments, creating recombinant chromosomes with new combinations of alleles that didn't exist in either parent."
  explanation: "Independent assortment alone can produce 2^23 (over 8 million) chromosome combinations in human gametes. Crossing over generates additional variation by shuffling alleles along individual chromosomes, so that even two gametes with the same chromosome set can carry different allele combinations. Together, these mechanisms ensure that virtually every gamete is genetically unique."
```

## Explainer

You already know from studying mitosis that cells can divide to produce two identical daughter cells. Meiosis is a fundamentally different process with a fundamentally different purpose: it produces gametes (sperm and eggs) for sexual reproduction. Instead of copying a cell, meiosis reshuffles and halves the genetic information, generating cells with one copy of each chromosome rather than two. Without this halving, fertilization would double the chromosome number with every generation.

Meiosis consists of two sequential divisions, and the key to understanding it is recognizing that they do different things. Meiosis I is the *reductional* division — it separates the two members of each homologous chromosome pair. Recall that diploid organisms carry two copies of each chromosome: one inherited from each parent. These two copies are called homologs. During meiosis I, homologs pair up, and then the paired homologs are pulled to opposite poles. The result is two haploid cells, each with one copy of each chromosome. Meiosis II is the *equational* division — it separates the sister chromatids within each haploid cell, just as mitosis would. By the end of meiosis II, four haploid cells have been produced from the original diploid precursor.

The most critical event in meiosis for generating genetic diversity is crossing over, which occurs during prophase I. When homologs pair up, their chromatids become physically intertwined. At points called chiasmata, non-sister chromatids from the two homologs break and rejoin — exchanging segments of DNA. This creates recombinant chromosomes that carry allele combinations that existed in neither parent. Think of it as shuffling the cards between the two parental decks before dealing. Crossing over is why siblings who inherit the same two parental chromosomes can still carry different allele combinations: the chromosomes themselves were scrambled before being passed on.

A second source of diversity is independent assortment. When homologous pairs line up at the metaphase plate during meiosis I, the orientation of each pair — which homolog goes to which pole — is random and independent of every other pair. With 23 pairs of chromosomes in humans, this alone generates 2²³ (over 8 million) possible combinations. When you combine independent assortment with crossing over, the number of genetically distinct gametes any one person can produce is astronomically large — essentially infinite for practical purposes.

Errors in meiosis have significant consequences. If homologs or sister chromatids fail to separate properly — a process called nondisjunction — the resulting gametes have too many or too few chromosomes. When such a gamete combines with a normal gamete at fertilization, the embryo has an abnormal chromosome number (aneuploidy). Trisomy 21 (Down syndrome) results from nondisjunction of chromosome 21 during meiosis, producing a gamete with two copies of chromosome 21 instead of one. This is one reason why the precision of meiotic chromosome segregation matters enormously for reproductive success.

