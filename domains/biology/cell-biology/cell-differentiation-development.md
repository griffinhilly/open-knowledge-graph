---
id: cell-differentiation-development
title: 'Cell Differentiation: Specifying Cell Type'
domain: biology
course: cell-biology
prerequisites:
- id: gene-expression-overview
  type: hard
- id: cell-signaling-receptor-pathways
  type: hard
tags:
- differentiation
- development
- specialization
stage: abstract-reasoning
status: draft
---

# Cell Differentiation: Specifying Cell Type

## Core Idea
During development, genetically identical cells differentiate into hundreds of cell types by selectively expressing different genes. Transcription factors (often activated by signaling) bind enhancers activating cell-type-specific programs. Epigenetic marks (histone modifications, DNA methylation) lock in expression patterns heritably. Developmental fields have positional information specifying cell fate.

## How It's Best Learned
Map transcription factor expression during tissue development. Use chromatin immunoprecipitation to identify enhancer binding. Demonstrate reprogramming: how transcription factors convert fibroblasts to pluripotent stem cells.

## Common Misconceptions
Differentiation is permanent—some cells can dedifferentiate. All cells in tissue are identical—tissues contain multiple cell types. Different tissues have different genomes—all cells have the same genome; different genes are expressed.

## Explainer

You already know that gene expression can be regulated — that cells can turn genes on and off in response to signals. Cell differentiation is what happens when this regulatory capacity is deployed systematically during development: a single fertilized egg divides into billions of cells that, despite carrying identical genomes, become muscle cells, neurons, blood cells, and hundreds of other specialized types. The fundamental question is: if every cell has the same DNA, what makes a liver cell different from a skin cell? The answer is that differentiation is a matter of which genes are expressed, not which genes are present.

The process begins with **transcription factors** — proteins that bind specific DNA sequences (enhancers and promoters) to activate or repress target genes. During development, cells receive signals from their neighbors (morphogens, growth factors, direct cell-cell contacts) that activate signaling cascades, ultimately turning on specific transcription factors. These transcription factors then activate cell-type-specific gene programs. For example, the transcription factor **MyoD** is sufficient to initiate the muscle differentiation program: when expressed in fibroblasts (connective tissue cells), it can convert them into muscle cells. This demonstrates that differentiation is driven by **master regulatory transcription factors** that sit atop hierarchical gene networks.

But if transcription factor expression can change, what keeps a liver cell from spontaneously becoming a neuron? The answer lies in **epigenetic mechanisms** — heritable modifications to chromatin that do not alter the DNA sequence itself. **DNA methylation** (adding methyl groups to cytosines in CpG dinucleotides) typically silences genes by preventing transcription factor binding. **Histone modifications** (acetylation, methylation, phosphorylation of histone tails) alter chromatin accessibility — acetylated histones open chromatin for transcription, while certain methylation marks compact it into silent heterochromatin. Once a cell differentiates, these epigenetic marks are copied during cell division, locking in the gene expression pattern. A liver cell's daughter cells remain liver cells because the epigenetic landscape is faithfully propagated, even though the underlying DNA could in principle express any gene.

The fact that differentiation is maintained by epigenetics rather than by irreversible DNA changes means it is, in principle, reversible. This was dramatically demonstrated by Shinya Yamanaka's discovery that introducing just four transcription factors (Oct4, Sox2, Klf4, c-Myc) into differentiated adult cells can reprogram them into **induced pluripotent stem cells (iPSCs)** — cells that behave like embryonic stem cells and can differentiate into any cell type. This reprogramming works by resetting the epigenetic landscape, erasing the marks that maintained the differentiated state. The reversibility of differentiation confirms that it is a regulatory state, not a genetic one, and opens profound possibilities for regenerative medicine — generating patient-specific cells for transplantation from their own skin cells.
