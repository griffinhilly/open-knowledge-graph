---
id: systems-biology-data-integration
title: Systems Biology and Data Integration
domain: biology
course: genomics-and-bioinformatics
prerequisites:
- id: rna-seq-analysis-pipeline
  type: hard
- id: differential-gene-expression
  type: hard
- id: proteomics-data-analysis
  type: soft
- id: metabolomics
  type: soft
builds-toward:
- multi-omics-integration
tags:
- systems-biology
- network-analysis
- pathway-enrichment
- gene-ontology
- data-integration
- biological-networks
stage: expert
status: validated
---
# Systems Biology and Data Integration

## Core Idea
Systems biology studies biological processes as integrated systems rather than isolated components, using computational models to understand how genes, proteins, metabolites, and their interactions give rise to cellular behavior. Data integration combines multiple omics datasets (transcriptomics, proteomics, metabolomics, epigenomics) with pathway databases and interaction networks to build holistic models. Key analytical approaches include pathway enrichment analysis (Gene Ontology, KEGG), network-based analysis (protein-protein interaction networks, gene co-expression networks), and constraint-based metabolic modeling (flux balance analysis). The goal is to move from lists of differentially expressed genes to mechanistic understanding of biological processes.

## How It's Best Learned
Take a list of differentially expressed genes from an RNA-seq experiment and perform Gene Ontology enrichment analysis (using clusterProfiler or DAVID). Then map the same genes onto KEGG pathways and a protein-protein interaction network (STRING). Compare what each approach reveals and note how they complement each other.

## Common Misconceptions
- Pathway enrichment p-values do not mean the pathway is "activated" — they mean more genes in the pathway changed than expected by chance, which could reflect activation, repression, or dysregulation.
- Biological networks are not static wiring diagrams; interactions are context-dependent (tissue-specific, condition-specific) and the same network topology can produce different behaviors depending on activity states.

## Questions

```yaml
- question: "What is the purpose of Gene Ontology (GO) enrichment analysis in the context of a differential expression experiment?"
  type: multiple-choice
  options: ["To identify which genes are most highly expressed", "To determine the chromosomal location of differentially expressed genes", "To identify biological processes, molecular functions, or cellular components that are over-represented among differentially expressed genes", "To predict the three-dimensional structure of the proteins encoded by differentially expressed genes"]
  answer: 2
  explanation: "GO enrichment tests whether genes associated with a particular biological function appear more often in your differentially expressed gene list than expected by chance. If 30 out of 500 DE genes are involved in 'inflammatory response' but only 5 would be expected by chance from a genome of that size, the enrichment is statistically significant. This transforms an uninterpretable list of hundreds of gene names into a concise summary of which biological processes are affected, providing biological meaning to the statistical results."

- question: "Combining transcriptomics and proteomics data always shows the same biological signal because proteins are translated from mRNA."
  type: true-false
  answer: false
  explanation: "Transcript and protein levels correlate only moderately (r ~ 0.4-0.6) because post-transcriptional regulation, translation efficiency, and protein stability create divergence. A gene may be transcriptionally upregulated but its protein rapidly degraded, or an mRNA may be translationally repressed. Integrating both layers reveals biology that neither alone captures: transcriptomics shows regulatory intent, proteomics shows functional outcome, and the discrepancies between them reveal post-transcriptional regulatory mechanisms."

- question: "Explain why network-based analysis can identify important biology that single-gene analysis misses."
  type: short-answer
  answer: "Many biological processes involve coordinated changes across multiple interacting genes, each with individually modest effects that may not reach statistical significance in a single-gene test. Network analysis aggregates these small effects across connected genes: if many members of a protein complex or pathway show modest changes in the same direction, the pathway-level signal can be strong even when no individual gene is significant. This 'guilt by association' approach also helps interpret genes of unknown function — if an uncharacterized gene is co-expressed with known immune genes, it likely has an immune-related function."
  explanation: "The classic example is GSEA (Gene Set Enrichment Analysis), which detects coordinated shifts in gene sets without requiring individual genes to pass a significance threshold. Network propagation methods extend this further by spreading signal through interaction networks, identifying modules of functionally related genes that are collectively perturbed."
```

## Explainer

Individual omics experiments produce lists: differentially expressed genes, altered metabolites, modified proteins. But biology operates as interconnected systems, not lists. Systems biology aims to understand how the interactions between molecular components produce the behaviors of cells, tissues, and organisms. Data integration — combining multiple types of molecular measurements with prior knowledge about pathways and interactions — is the central computational challenge.

**Pathway enrichment analysis** is usually the first integration step. Given a list of differentially expressed genes, enrichment analysis asks: are any known biological pathways or functional categories disproportionately represented? Gene Ontology (GO) provides a hierarchical vocabulary of biological processes, molecular functions, and cellular components. KEGG provides curated metabolic and signaling pathway maps. Reactome provides detailed reaction-level pathway models. Over-representation analysis (ORA) tests each pathway using a hypergeometric test; Gene Set Enrichment Analysis (GSEA) ranks all genes by their expression change and tests whether pathway members cluster at the top or bottom of the ranking. These approaches convert gene lists into biological narratives.

**Network analysis** adds another dimension. Protein-protein interaction (PPI) networks from databases like STRING and BioGRID map the physical and functional connections between proteins. Gene co-expression networks (built from RNA-seq data using WGCNA) identify modules of genes that vary together across conditions. Overlaying differential expression data onto these networks reveals which modules are perturbed and identifies hub genes — highly connected nodes whose disruption affects many downstream partners. Network propagation algorithms spread experimental signal through the network, identifying genes that are not themselves differentially expressed but are strongly connected to genes that are, potentially revealing upstream regulators or downstream effectors.

**Multi-omics integration** is the frontier. Combining transcriptomics, proteomics, metabolomics, and epigenomics from the same samples provides complementary views of the same biological system. Transcripts show regulatory changes, proteins show functional capacity, metabolites show biochemical output, and epigenomic marks show regulatory state. Statistical methods for integration range from simple (overlapping significant results from each layer) to sophisticated (multivariate methods like MOFA, network-based integration like iNetModules, and causal inference frameworks). The emerging paradigm is that no single omics layer tells the full story — diseases, drug responses, and developmental processes are best understood by examining how perturbations propagate across molecular layers, from genome to phenome.
