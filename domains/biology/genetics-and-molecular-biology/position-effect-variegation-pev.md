---
id: position-effect-variegation-pev
title: Position Effect Variegation and Chromatin Context
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: chromatin-fiber-higher-order-structure
  type: hard
- id: dna-methylation-and-epigenetic-silencing
  type: hard
builds-toward:
- long-noncoding-rna-mechanisms
tags:
- position-effect-variegation
- heterochromatin
- epigenetic-silencing
- chromatin-context
stage: advanced
status: draft
---

# Position Effect Variegation and Chromatin Context

## Core Idea
Position effect variegation (PEV) is the mosaic expression of a gene when relocated adjacent to heterochromatin, where some cells express the gene (euchromatic state) and others silence it (heterochromatic spreading). The silenced state can be inherited through cell divisions as an epigenetic mark. PEV demonstrates that chromatin state is position-dependent and can override intrinsic cis-regulatory elements, with major implications for understanding how chromosomal context affects gene expression.

## Explainer

From your study of higher-order chromatin structure, you know that the genome is organized into **euchromatin** (open, transcriptionally active) and **heterochromatin** (condensed, transcriptionally silent) domains. From DNA methylation and epigenetic silencing, you know that chemical modifications to DNA and histones can stably repress gene expression across cell divisions. **Position effect variegation** (PEV) is a dramatic natural experiment that reveals what happens when a normally active gene is placed at the boundary between these two chromatin states.

The classic example comes from *Drosophila* genetics. The *white* gene controls eye pigmentation — flies with a functional copy have red eyes, and loss-of-function mutants have white eyes. In certain chromosomal rearrangements (inversions or translocations), the *white* gene is moved from its normal euchromatic location to a position adjacent to pericentric heterochromatin. The result is striking: instead of uniformly red or white eyes, the fly develops a **mosaic** pattern of red and white patches — some ommatidia (eye facets) are red, others are white, producing a mottled or "variegated" appearance. The gene itself is completely intact; only its chromosomal neighborhood has changed.

The mechanism is **heterochromatin spreading**. Heterochromatin is not a static boundary — it tends to propagate along the chromosome through a self-reinforcing cycle. Methyltransferases like Su(var)3-9 add repressive histone marks (particularly H3K9 methylation), which recruit **HP1** (Heterochromatin Protein 1), which in turn recruits more Su(var)3-9, extending the silent chromatin further. When a gene like *white* sits near heterochromatin, this spreading wave may or may not reach the gene in any given cell during development. In cells where heterochromatin spreads far enough to engulf *white*, the gene is silenced — producing white ommatidia. In cells where spreading halts before reaching the gene, *white* remains active — producing red ommatidia. Because the decision is made early in development and is then **epigenetically inherited** through subsequent cell divisions, each clone of cells derived from a single progenitor is uniformly red or white, producing the characteristic patchy pattern.

PEV has been a goldmine for identifying chromatin regulators. Genetic screens for **suppressors of variegation** — Su(var) mutations that reduce silencing and make eyes more uniformly red — identified many of the key heterochromatin components: Su(var)3-9 (the H3K9 methyltransferase), Su(var)2-5 (HP1), and histone deacetylases. Conversely, **enhancers of variegation** — E(var) mutations that increase silencing — identified chromatin remodelers and histone acetyltransferases that normally oppose heterochromatin spreading. PEV thus provides a foundational framework for understanding that gene expression depends not only on a gene's sequence and its cis-regulatory elements, but critically on its **chromosomal context** — a principle with direct relevance to understanding how chromosomal rearrangements in cancer and transgene silencing in biotechnology can alter gene expression without changing the DNA sequence itself.
