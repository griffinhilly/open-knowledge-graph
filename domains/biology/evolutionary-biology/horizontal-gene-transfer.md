---
id: horizontal-gene-transfer
title: Horizontal Gene Transfer
domain: biology
course: evolutionary-biology
prerequisites:
- id: molecular-evolution
  type: hard
builds-toward:
- tree-of-life-reticulation
tags:
- molecular-evolution
- microbial-evolution
- genomics
stage: advanced
status: validated
---

# Horizontal Gene Transfer

## Core Idea
Horizontal gene transfer (HGT) moves genes between distantly related organisms without vertical inheritance, especially common in prokaryotes. HGT can rapidly introduce metabolic innovations and pathogenicity factors, causing sudden phenotypic shifts. Evidence of HGT complicates phylogenetic reconstruction and challenges tree-of-life assumptions.

## Questions

```yaml
- question: "A researcher builds phylogenetic trees from three different genes in Bacterium X. The tree based on Gene A places it near Cyanobacteria; trees based on Genes B and C place it near Proteobacteria. What is the most likely explanation?"
  type: multiple-choice
  options:
    - "Bacterium X is a hybrid organism with two separate cellular lineages merged into one"
    - "Gene A was horizontally transferred from a cyanobacterial donor and carries the donor's evolutionary history, not the organism's"
    - "The phylogenetic analysis of Gene A was performed incorrectly and should be redone"
    - "Cyanobacteria and Proteobacteria are more closely related to each other than currently recognized"
  answer: 1
  explanation: "When a gene's phylogenetic history conflicts with the species tree, HGT is the primary explanation. Gene A appears to have been acquired from a cyanobacterial donor — its sequence reflects cyanobacterial ancestry rather than the organism's own lineage. Genes B and C, which agree with each other, likely reflect the actual species history. Conflicting gene trees are one of the primary methods for detecting HGT events, and this scenario is precisely why biologists must use multiple genes — especially vertically inherited core genes — to reconstruct reliable species phylogenies."

- question: "A harmless soil bacterium and a pathogenic Staphylococcus share an identical beta-lactamase gene that destroys penicillin, despite being otherwise very distantly related. What is the most parsimonious explanation?"
  type: multiple-choice
  options:
    - "Beta-lactamase evolved independently in both species by convergent evolution at the molecular sequence level"
    - "The gene was horizontally transferred between the species or from a shared recent donor, rather than inherited from a distant common ancestor"
    - "Both species share a recent common ancestor that has since gone extinct and left no other trace"
    - "The gene is ancient enough to have been present in the common ancestor of all bacteria and retained unchanged in both lineages"
  answer: 1
  explanation: "Sequence identity between distantly related organisms is the hallmark of recent horizontal transfer. If the gene were vertically inherited from a common ancestor, the sequences would have diverged in proportion to the evolutionary distance between the species — distantly related organisms should have very different sequences. Near-identical sequences across a large evolutionary gap signal recent HGT. Convergent evolution at the sequence level (Option A) is astronomically unlikely for a complex protein. Option D would not explain sequence identity because billions of years of independent evolution would diversify the sequences even if both retained the gene."

- question: "Horizontal gene transfer means that a single prokaryotic cell can contain genes with completely different evolutionary histories — some inherited vertically from its ancestors, others acquired laterally from unrelated donors."
  type: true-false
  answer: true
  explanation: "This mosaic genome structure is a fundamental feature of prokaryotic evolution. Through transformation, transduction, or conjugation, individual genes can be acquired from entirely unrelated donors throughout an organism's existence. The recipient's lineage is determined by vertical inheritance of its core genome, but acquired genes carry the evolutionary history of their donors. A single bacterium can therefore contain ancient core genes tracing back to its lineage alongside recently acquired genes from cyanobacteria, archaea, or other donors — all within the same cell."

- question: "Because bacteria reproduce asexually (without meiosis or gamete fusion), they can seldom transfer genetic material to other bacteria during their lifetimes."
  type: true-false
  answer: false
  explanation: "Bacteria transfer genetic material extensively through HGT mechanisms that are entirely independent of sexual reproduction: transformation (uptake of free environmental DNA), transduction (phage-mediated gene delivery), and conjugation (direct cell-to-cell plasmid transfer through a pilus). These operate during the organisms' lifetimes, between distantly related species, and even across domain boundaries. Asexual reproduction means genes flow vertically without recombination, but HGT provides an alternative route for acquiring new genetic information that is, if anything, more promiscuous than sexual reproduction."

- question: "Why does horizontal gene transfer mean that a single gene's phylogenetic tree may not accurately represent the evolutionary history of the organism that carries it?"
  type: short-answer
  answer: "Each gene has its own evolutionary history determined by where it came from. A vertically inherited gene traces the organism's lineage back through its direct ancestors. A horizontally transferred gene traces back to its donor species, not the recipient's lineage. Building a phylogeny from a transferred gene reconstructs the donor's history, not the organism's — the gene tree and the species tree conflict."
  explanation: "This is why microbiologists must use multiple genes — and ideally genes known to be vertically inherited — to reconstruct reliable species phylogenies. Core housekeeping genes (ribosomal proteins, RNA polymerase subunits) are rarely transferred and are preferred for species trees. Genes on plasmids, pathogenicity islands, or associated with specialized metabolism are more likely to have HGT histories. The recognition that prokaryotic evolution involves extensive gene sharing has shifted the conceptual model from a 'tree of life' to a 'web of life' — reticulate rather than purely branching — and is why horizontal transfer must be screened for before any genomic phylogenetic inference."
```

## Explainer

From your study of molecular evolution, you know that DNA sequences change over time through mutation, drift, and selection, and that comparing sequences reveals evolutionary relationships. Vertical inheritance — parent to offspring — is the default assumption: genes flow down the tree of life. **Horizontal gene transfer** (HGT) breaks this assumption entirely. In HGT, an organism acquires genes not from its parent but from a completely unrelated organism, sometimes one that diverged billions of years ago.

Three main mechanisms drive HGT in prokaryotes. **Transformation** occurs when a bacterium takes up free DNA from its environment — for instance, DNA released by a dead neighboring cell. **Transduction** happens when a bacteriophage (a virus that infects bacteria) accidentally packages host DNA and delivers it to a new bacterial cell. **Conjugation** involves direct cell-to-cell contact through a pilus, transferring a plasmid or even chromosomal DNA from donor to recipient. Each mechanism moves genetic material sideways across lineages rather than vertically through reproduction.

The consequences of HGT are enormous. Consider antibiotic resistance: a gene encoding a beta-lactamase enzyme that destroys penicillin can jump from a harmless soil bacterium into a pathogenic Staphylococcus in a single transfer event, instantly conferring resistance. This is far faster than waiting for the pathogen to evolve resistance through point mutations. HGT can also introduce entirely new metabolic capabilities — some bacteria have acquired photosynthesis genes, nitrogen fixation genes, or toxin-production genes from distantly related donors, fundamentally reshaping their ecological roles.

For phylogenetics, HGT creates a serious problem. If you build a tree from a gene that was horizontally transferred, that gene's tree will not match the species tree. One gene might place a bacterium near cyanobacteria while another places it near proteobacteria, not because the species has two ancestors but because different genes have different histories. This is why molecular evolution in prokaryotes is often better described as a **web of life** or a network rather than a strictly branching tree. Recognizing when a gene's phylogeny conflicts with the species tree is one of the primary methods for detecting HGT events, and it forces biologists to think carefully about which genes are reliable markers of organismal relationships and which have been "borrowed" from elsewhere.
