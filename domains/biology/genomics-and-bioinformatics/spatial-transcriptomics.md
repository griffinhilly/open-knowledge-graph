---
id: spatial-transcriptomics
title: Spatial Transcriptomics
domain: biology
course: genomics-and-bioinformatics
prerequisites:
- id: single-cell-rna-sequencing
  type: hard
- id: rna-seq-analysis-pipeline
  type: hard
builds-toward:
- multi-omics-integration
tags:
- spatial-transcriptomics
- Visium
- MERFISH
- tissue-architecture
- cell-cell-communication
- spatial-gene-expression
stage: expert
status: validated
---
# Spatial Transcriptomics

## Core Idea
Spatial transcriptomics measures gene expression while preserving the spatial location of each measurement within a tissue section. Sequencing-based methods (10x Visium, Slide-seq) capture mRNA on spatially barcoded arrays, providing transcriptome-wide coverage at defined locations. Imaging-based methods (MERFISH, seqFISH) use multiplexed fluorescence in situ hybridization to detect hundreds to thousands of genes at single-molecule resolution within intact tissue. By retaining spatial context that scRNA-seq loses during dissociation, spatial transcriptomics reveals how gene expression varies across tissue architecture, identifies spatial domains and niches, and maps cell-cell communication patterns.

## How It's Best Learned
Analyze a 10x Visium dataset from a mouse brain section using Squidpy or Scanpy: visualize gene expression overlaid on the tissue image, identify spatially variable genes, and map clusters to anatomical regions. Compare to a dissociated scRNA-seq dataset from the same tissue and note what spatial information was lost in the scRNA-seq.

## Common Misconceptions
- 10x Visium spots are not single cells — each 55-micrometer spot captures RNA from approximately 1-10 cells, requiring computational deconvolution to estimate cell type composition per spot.
- Spatial transcriptomics does not yet provide the same transcriptome-wide coverage at single-cell resolution in a single technology — there is a tradeoff between the number of genes measured and spatial resolution.

## Questions

```yaml
- question: "What is the fundamental advantage of spatial transcriptomics over standard single-cell RNA sequencing?"
  type: multiple-choice
  options: ["Spatial transcriptomics detects more genes per cell", "Spatial transcriptomics retains the physical location of each measurement within the tissue", "Spatial transcriptomics is cheaper per sample", "Spatial transcriptomics requires fewer cells"]
  answer: 1
  explanation: "scRNA-seq dissociates tissue into single cells before sequencing, destroying all spatial information — which cells were neighbors, which resided in specific tissue regions, and how gene expression varied across anatomical structures. Spatial transcriptomics preserves this information, enabling analysis of tissue architecture, spatial gene expression gradients, cell-cell communication, and spatial organization of cell types. This spatial context is critical for understanding tissue function, disease pathology, and developmental patterning."

- question: "Imaging-based spatial transcriptomics methods like MERFISH can currently measure the full transcriptome (all ~20,000 genes) at single-cell resolution in a tissue section."
  type: true-false
  answer: false
  explanation: "Current imaging-based methods typically measure hundreds to a few thousand genes per experiment (MERFISH routinely detects ~500-1,000 genes, with newer versions reaching several thousand). While this is far more than traditional FISH, it falls short of the full transcriptome. Sequencing-based methods like Visium capture transcriptome-wide data but at lower spatial resolution (multi-cell spots). Ongoing technology development is narrowing this gap, with methods like MERFISH+ and Slide-seq V2 pushing toward both higher gene counts and finer resolution."

- question: "Explain why cell-cell communication analysis is more reliable with spatial transcriptomics data than with dissociated scRNA-seq data."
  type: short-answer
  answer: "Cell-cell communication analysis infers signaling interactions by identifying ligand-receptor pairs where the ligand is expressed in one cell type and the receptor in another. With dissociated scRNA-seq, any two cell types in the dataset could theoretically interact, but in reality only cells that are physically proximal can communicate through short-range signals (paracrine, juxtacrine). Spatial transcriptomics reveals which cell types are actually neighbors in the tissue, restricting the analysis to biologically plausible interactions. This eliminates false-positive ligand-receptor predictions between cell types that are expressed in the same tissue but located in distant compartments."
  explanation: "Tools like CellChat and NicheNet have been adapted for spatial data, using the spatial coordinates to constrain interaction analysis to cells within a defined radius. This spatial constraint dramatically reduces the number of predicted interactions and increases the proportion that are biologically meaningful."
```

## Explainer

Single-cell RNA sequencing revealed that tissues are composed of diverse cell types with distinct transcriptional programs. But by dissociating tissue into single cells, scRNA-seq destroys the very thing that makes a tissue a tissue: the spatial organization of cells. Which cells are next to which? How does gene expression change from the center to the edge of a tumor? Where exactly in the brain is a particular gene expressed? Spatial transcriptomics answers these questions by measuring gene expression in situ — within intact tissue sections.

**Sequencing-based methods** work by placing a tissue section onto a surface printed with spatially barcoded oligonucleotides. When RNA is released from the tissue (by permeabilization), it hybridizes to the barcoded probes, which capture it at known locations. After reverse transcription and sequencing, each read carries both the gene identity and the spatial barcode, enabling reconstruction of a spatial gene expression map. 10x Genomics Visium, the most widely used platform, prints ~5,000 spots (each 55 micrometers in diameter, spaced 100 micrometers apart) on a capture area. This provides transcriptome-wide coverage but at multi-cell resolution — each spot captures RNA from several cells. Newer methods like Slide-seq (10-micrometer beads) and Stereo-seq (sub-cellular resolution) are pushing spatial resolution finer.

**Imaging-based methods** take the opposite approach: they visualize individual RNA molecules in situ using multiplexed FISH. MERFISH (Multiplexed Error-Robust Fluorescence In Situ Hybridization) encodes each RNA species with a unique combination of fluorescent probes across multiple rounds of imaging. A gene detected in rounds 1, 3, and 5 (but not 2, 4, and 6) has a unique binary barcode that identifies it. Error-robust encoding schemes tolerate missed or false hybridizations. seqFISH uses a sequential barcoding strategy for similar results. These methods achieve single-molecule, subcellular resolution but are limited in gene number (hundreds to low thousands) and require specialized microscopy.

The analytical challenge is integrating spatial and molecular information. **Spatially variable gene detection** identifies genes whose expression shows significant spatial patterns (gradients, hot spots, domain boundaries). **Spatial domain identification** segments the tissue into regions with coherent expression programs, often corresponding to anatomical structures. **Deconvolution** (for multi-cell-resolution data like Visium) estimates the cell type composition of each spot by combining the spatial data with a scRNA-seq reference. **Cell-cell communication analysis** maps ligand-receptor interactions between spatially adjacent cells. These analyses are producing spatial cell atlases of organs in health and disease, revealing how tissue microenvironments shape cell behavior in ways that dissociated studies could never capture.
