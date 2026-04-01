---
id: single-cell-trajectory-analysis
title: Single-Cell Trajectory Analysis
domain: biology
course: systems-biology
prerequisites:
- id: single-cell-rna-sequencing
  type: hard
- id: stochastic-gene-expression
  type: hard
- id: multi-omics-integration-systems
  type: soft
builds-toward: []
tags:
- pseudotime
- RNA-velocity
- trajectory-inference
- Monocle
- cell-fate
- lineage-tracing
stage: expert
status: validated
---
# Single-Cell Trajectory Analysis

## Core Idea
Single-cell trajectory analysis reconstructs the continuous progression of cells through biological processes — differentiation, activation, disease progression — from snapshot scRNA-seq data where each cell is measured only once. Since single-cell RNA sequencing destroys the cell, temporal ordering must be inferred computationally: cells at different stages of a process coexist in the sample, and trajectory inference algorithms arrange them along a pseudotime axis that recapitulates the biological progression. Pseudotime methods (Monocle, Slingshot, PAGA) construct low-dimensional manifolds from gene expression space and order cells along paths through these manifolds. RNA velocity (La Manno et al., 2018) adds directionality by exploiting the ratio of unspliced to spliced mRNA within each cell as a proxy for transcriptional rate of change, predicting each cell's future state without requiring external time labels. Together, these methods transform static snapshots into dynamic narratives of cell-state change, making trajectory analysis central to modern developmental and stem cell biology.

## Questions

```yaml
- question: "Pseudotime analysis of a scRNA-seq dataset places cells along a trajectory from stem cells to differentiated cells. What does the pseudotime value represent?"
  type: multiple-choice
  options:
    - "The actual chronological time since the cell was born"
    - "An inferred ordering that reflects the relative progress of each cell through the biological process, based on gene expression similarity — cells with similar pseudotime values have similar transcriptional states, but the mapping to real time is generally nonlinear and unknown"
    - "The number of cell divisions the cell has undergone"
    - "The distance of the cell from the centroid of the dataset in PCA space"
  answer: 1
  explanation: "Pseudotime is an abstract coordinate that orders cells by transcriptional similarity along a trajectory, not a measurement of real time. Two cells with pseudotime values of 0.3 and 0.6 are inferred to be at different stages of the process, with 0.6 being further along, but this does not mean 0.6 has been differentiating for twice as long. The relationship between pseudotime and real time depends on the rate of transcriptional change, which may vary across the trajectory — rapid transitions compress pseudotime, slow transitions stretch it. Calibrating pseudotime to real time requires additional information (time-stamped samples, pulse-chase experiments, or live imaging)."

- question: "RNA velocity determines the direction of cell-state transitions by comparing future and past gene expression measurements from the same cell."
  type: true-false
  answer: false
  explanation: "RNA velocity does not require measuring the same cell at two time points — that would be impossible since scRNA-seq is destructive. Instead, it exploits a snapshot measurement: within each cell, the ratio of unspliced pre-mRNA to spliced mature mRNA reflects whether a gene is being upregulated (unspliced > expected at steady state, meaning transcription recently increased) or downregulated (unspliced < expected, meaning transcription has decreased but mature mRNA persists). By computing this ratio across all genes, RNA velocity infers a vector in gene expression space that points toward the cell's predicted future state. The key biological insight is that unspliced and spliced mRNA act as a natural 'time derivative' built into every cell — the unspliced fraction is a leading indicator of where expression is heading."

- question: "What is the fundamental assumption that allows trajectory inference from a single-time-point scRNA-seq experiment, and when does this assumption fail?"
  type: short-answer
  answer: "The fundamental assumption is ergodicity (or quasi-ergodicity): that the population of cells captured at a single time point contains cells at all stages of the biological process, so the distribution of cell states in the sample recapitulates the temporal progression. This assumes the process is asynchronous — not all cells started at the same time — so that cells spanning the full trajectory are present simultaneously. This assumption fails when the process is highly synchronized (all cells transition together, as in stimulus-response experiments where the entire population is perturbed simultaneously), when rare intermediate states are undersampled, or when the process has not yet begun or has fully completed at the time of capture. In synchronized processes, all cells are at approximately the same stage, providing no information about the trajectory."
  explanation: "The ergodic assumption is borrowed from statistical mechanics: measuring many particles at one time point is equivalent to measuring one particle at many time points, if the system is in a steady state of flow. In biology, this works well for continuous developmental processes (hematopoiesis, spermatogenesis) where cells constantly enter and progress through the trajectory, but fails for acute responses (all cells responding to a drug simultaneously)."

- question: "How does Slingshot differ from Monocle 3 in its approach to trajectory inference?"
  type: short-answer
  answer: "Slingshot and Monocle 3 differ primarily in their dimensionality reduction and curve-fitting strategies. Slingshot operates in a reduced-dimension space (typically from PCA), constructs a minimum spanning tree (MST) on cluster centroids to identify the global trajectory topology (linear, branching), then fits simultaneous principal curves through the data along each lineage path, producing smooth pseudotime orderings. Monocle 3 uses UMAP for dimensionality reduction, learns a principal graph (not just an MST on clusters but a graph learned directly from the data points) in the UMAP space, and assigns pseudotime by geodesic distance along this graph from a user-specified root. Monocle 3 handles more complex topologies (loops, convergences) through its graph-learning approach, while Slingshot's principal curve fitting tends to produce smoother trajectories for simpler branching structures."
  explanation: "Both methods require the user to specify a root cell or starting point, which introduces subjectivity. In practice, the choice of method matters less than the biological validation of the resulting trajectory — do known marker genes change monotonically along pseudotime? Do branch points correspond to known fate decisions? Computational trajectory inference generates hypotheses that must be validated by independent experimental methods (lineage tracing, time-course experiments)."
```

## Explainer

Single-cell RNA sequencing captures the transcriptomes of thousands to millions of individual cells, revealing the full heterogeneity of cell states within a tissue. But scRNA-seq provides only a **snapshot** — each cell is measured once and destroyed. If you want to understand a dynamic process like differentiation (how a stem cell becomes a neuron or a blood cell), you face a fundamental problem: you cannot follow individual cells through time. **Trajectory inference** solves this by exploiting the fact that in most biological processes, cells are asynchronous — at any given moment, cells at different stages of the process coexist in the tissue. By computationally ordering these cells by their transcriptional similarity, you can reconstruct the trajectory that any individual cell would follow over time.

**Pseudotime methods** — including Monocle (Trapnell et al., 2014), Slingshot (Street et al., 2018), and PAGA (Wolf et al., 2019) — construct this ordering algorithmically. The general approach is: (1) reduce the high-dimensional gene expression matrix to a lower-dimensional representation (PCA, diffusion maps, UMAP), (2) identify the topology of the trajectory (linear, branching, cyclical) using graph-based methods, and (3) assign each cell a pseudotime value reflecting its position along the trajectory. The result is a continuous ordering from progenitor states to differentiated states, along which you can identify genes that are dynamically regulated, branch points where fate decisions occur, and transcription factors that drive transitions. The critical assumption is **ergodicity** — that the snapshot population samples all stages of the process — which holds well for ongoing processes like hematopoiesis but fails for synchronized acute responses.

**RNA velocity** (La Manno et al., 2018) added a transformative dimension to trajectory analysis: **directionality**. Standard pseudotime methods infer an ordering but cannot intrinsically determine which end is the beginning and which is the end without prior biological knowledge (the user must specify a root). RNA velocity solves this by exploiting a signal internal to each cell: the ratio of unspliced pre-mRNA to spliced mature mRNA. Under a simple kinetic model, a gene being actively upregulated has an excess of unspliced mRNA relative to the steady-state expectation (transcription has increased, but the new transcripts have not yet been spliced). A gene being downregulated has a deficit of unspliced mRNA (transcription has decreased, but spliced mRNA persists). By computing this ratio across all genes, each cell gets a **velocity vector** in gene expression space — a prediction of its future transcriptional state. Projecting these vectors onto the low-dimensional embedding reveals the flow of cell-state transitions, including the directionality of differentiation and the location of attractor states (stable cell types where velocity approaches zero).

The practical impact of trajectory analysis on systems biology is profound. It has revealed previously unknown intermediate cell states in differentiation, identified transcription factor cascades driving fate decisions, and uncovered bifurcation points where a single progenitor population splits into multiple lineages. Tools like **scVelo** (Bergen et al., 2020) extended RNA velocity with a dynamical model that estimates gene-specific kinetic parameters (transcription, splicing, and degradation rates), improving accuracy and enabling the recovery of latent time — a quantity closer to real biological time than pseudotime. The integration of trajectory analysis with perturbation data (CRISPR screens in single cells), spatial transcriptomics (adding tissue location to trajectory position), and multi-omics measurements (simultaneous chromatin accessibility and gene expression) is making it possible to construct comprehensive, mechanistic models of cell-state dynamics that connect regulatory network architecture to developmental outcomes.
