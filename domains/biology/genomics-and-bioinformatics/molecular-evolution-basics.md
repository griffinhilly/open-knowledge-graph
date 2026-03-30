---
id: molecular-evolution-basics
title: Molecular Evolution Basics for Bioinformatics
domain: biology
course: genomics-and-bioinformatics
prerequisites:
- id: dna-mutations
  type: hard
- id: dna-structure
  type: hard
- id: pairwise-sequence-alignment
  type: soft
- id: molecular-evolution
  type: soft
builds-toward:
- phylogenetic-tree-construction
- population-genomics
- comparative-genomics
tags:
- substitution-models
- dN-dS
- neutral-theory
- sequence-divergence
- homology
stage: advanced
status: validated
---
# Molecular Evolution Basics for Bioinformatics

## Core Idea
Molecular evolution provides the theoretical foundation for interpreting sequence comparisons. Substitution models (JC69, K2P, GTR) formalize how DNA sequences change over time, accounting for multiple hits at the same site. The distinction between orthology (divergence by speciation) and paralogy (divergence by gene duplication) determines whether sequence similarity reflects shared species history or gene family expansion. The dN/dS ratio (nonsynonymous to synonymous substitution rate) identifies genes under purifying selection, neutral drift, or positive selection. These concepts underpin every comparative and phylogenetic analysis in genomics.

## How It's Best Learned
Calculate raw percent identity between two homologous sequences, then apply a Jukes-Cantor correction and compare the two distance estimates. The difference — which grows dramatically for divergent sequences — demonstrates why substitution models matter. Then compute dN/dS for a pair of orthologous coding sequences using an online tool.

## Common Misconceptions
- Percent identity underestimates true evolutionary distance because it does not account for multiple substitutions at the same site (back-mutations, convergent changes).
- Two sequences can be homologous (share common ancestry) even at 25% identity for proteins — the "twilight zone" where statistical significance becomes uncertain.

## Questions

```yaml
- question: "Why does raw percent identity between two sequences underestimate the true evolutionary distance?"
  type: multiple-choice
  options: ["Because alignment algorithms introduce errors", "Because some mutations are silent and not counted", "Because multiple substitutions can occur at the same site, and only the most recent change is visible", "Because gaps are not counted as differences"]
  answer: 2
  explanation: "Over evolutionary time, the same nucleotide position can mutate multiple times. A site that changed from A to G and then from G to C appears as an A-to-C change — two events counted as one difference. A site that changed from A to G and back to A appears unchanged — two events counted as zero differences. These multiple hits cause percent identity to plateau around 25% for DNA (random expectation for 4 bases), even as true divergence continues to increase. Substitution models like Jukes-Cantor correct for this by estimating the actual number of substitutions per site."

- question: "Orthologs always have the same function in different species."
  type: true-false
  answer: false
  explanation: "Orthologs (genes that diverged by speciation) tend to retain similar functions, and this is often a useful working assumption. But function can diverge after speciation due to changes in regulatory context, protein-protein interactions, or adaptive evolution in one lineage. Furthermore, paralogs (genes that diverged by duplication) can also retain similar function, or one copy may neofunctionalize or subfunctionalize. The ortholog conjecture — that orthologs are more functionally similar than paralogs — is a useful heuristic, not an absolute rule."

- question: "Explain the biological significance of finding a dN/dS ratio significantly greater than 1 for a gene."
  type: short-answer
  answer: "A dN/dS ratio greater than 1 means nonsynonymous (amino acid-changing) substitutions are being fixed at a higher rate than synonymous (silent) substitutions. Since synonymous substitutions approximate the neutral mutation rate, a ratio above 1 indicates that natural selection is actively favoring amino acid changes — positive (diversifying) selection. This signature often occurs in genes involved in immune defense, reproduction, or host-pathogen interactions, where there is an evolutionary advantage to rapid protein sequence change."
  explanation: "Most genes have dN/dS well below 1, indicating purifying selection removes most amino acid changes. A ratio near 1 suggests neutral evolution (relaxed constraint). Values significantly above 1 are relatively rare genome-wide but point to genes of particular evolutionary interest. Branch-specific and site-specific models can localize positive selection to particular lineages or amino acid positions."
```

## Explainer

Every time you compare two sequences and ask "are these related?" or "how has this gene changed?", you are implicitly relying on molecular evolution theory. This topic covers the core concepts that make sequence comparison biologically meaningful rather than purely computational.

**Substitution models** are mathematical descriptions of how DNA sequences change over time. The simplest, Jukes-Cantor (JC69), assumes all four nucleotides are equally frequent and all substitutions are equally likely. This gives a clean formula for converting observed percent differences into estimated evolutionary distance, correcting for the multiple-hit problem. More realistic models add complexity: Kimura's two-parameter model (K2P) distinguishes transitions from transversions (transitions are more common); the General Time-Reversible model (GTR) allows each of the six substitution types to have its own rate and accommodates unequal base frequencies. Choosing the right model matters because underparameterized models underestimate distances between divergent sequences, distorting phylogenetic trees and divergence time estimates.

The concepts of **homology, orthology, and paralogy** are central to comparative genomics. Two sequences are homologous if they share a common ancestor. Orthologs diverged by speciation — they are the "same" gene in different species. Paralogs diverged by gene duplication — they are "sibling" genes within a genome (or across genomes if the duplication preceded speciation). This distinction matters because orthologs tend to preserve function (the gene does the same job in mouse and human), while paralogs are more likely to have diverged in function (one copy may take on a new role). Incorrectly treating paralogs as orthologs leads to wrong functional predictions, which is why reciprocal best BLAST hits and more sophisticated orthology assignment tools (OrthoFinder, OMA) are critical in comparative studies.

The **dN/dS ratio** connects molecular evolution to natural selection in a quantifiable way. By comparing the rate of amino acid-changing substitutions (dN) to the rate of silent substitutions (dS) in protein-coding genes, you can infer the selective pressure acting on the protein. Most genes show dN/dS well below 1 because most amino acid changes are deleterious and removed by purifying selection. A ratio near 1 suggests the protein is evolving without constraint — perhaps a pseudogene or a gene that has become dispensable. A ratio above 1 is the signature of positive selection, meaning amino acid changes are being actively favored. Genome-wide dN/dS scans have identified genes under positive selection across many lineages, including genes involved in immunity, reproduction, and sensory perception.
