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
stage: formal-systems
status: validated
---

# Position Effect Variegation and Chromatin Context

## Core Idea
Position effect variegation (PEV) is the mosaic expression of a gene when relocated adjacent to heterochromatin, where some cells express the gene (euchromatic state) and others silence it (heterochromatic spreading). The silenced state can be inherited through cell divisions as an epigenetic mark. PEV demonstrates that chromatin state is position-dependent and can override intrinsic cis-regulatory elements, with major implications for understanding how chromosomal context affects gene expression.

## Questions

```yaml
- question: "A Drosophila fly carries an intact white gene, but a chromosomal inversion has placed it adjacent to pericentric heterochromatin. Instead of uniformly red eyes, the fly has a mosaic of red and white patches. What is the most direct explanation?"
  type: multiple-choice
  options:
    - "The chromosomal inversion introduced random point mutations in the white gene in different cells during development"
    - "Heterochromatin spreading stochastically silences white in some cells during early development; the silent chromatin state is then clonally inherited, producing patches of uniform color"
    - "The inversion disrupted the white gene's promoter in some cells but not others due to DNA replication errors"
    - "Mosaic expression always occurs near centromeres because reduced recombination prevents proper gene regulation"
  answer: 1
  explanation: "The white gene sequence is completely intact — only its chromosomal neighborhood has changed. Heterochromatin spreads from its boundary stochastically, reaching the gene in some early progenitor cells but halting before it in others. Crucially, once heterochromatin engulfs the gene in a cell, the silenced state is epigenetically inherited through all subsequent cell divisions — so each clone derived from a silenced progenitor produces a patch of white ommatidia. This is the mechanistic heart of PEV: stochastic establishment followed by deterministic clonal inheritance."

- question: "A researcher discovers a mutation (Su(var)) that suppresses PEV — flies carrying this mutation show more uniformly red eyes than wild-type PEV flies. What does this tell you about the mutated gene's function?"
  type: multiple-choice
  options:
    - "The gene is specifically required for transcription of the white gene — its loss allows white to be expressed even near heterochromatin"
    - "The gene is likely a component of heterochromatin formation or spreading — its loss impairs the ability of heterochromatin to propagate and silence adjacent genes"
    - "The mutation corrects the chromosomal inversion, restoring white to its original euchromatic location"
    - "The gene prevents chromosomal inversions during development, so its mutation reduces the frequency of PEV-causing rearrangements"
  answer: 1
  explanation: "Suppressor of variegation (Su(var)) mutations reduce silencing, making eyes more uniformly red. This means the mutated gene normally promotes heterochromatin formation or spreading. The genetic screen for Su(var) mutations was historically decisive in identifying heterochromatin components: Su(var)3-9 encodes the H3K9 methyltransferase; Su(var)2-5 encodes HP1. These are now known to be core components of the H3K9me → HP1 recruitment → spreading cycle. PEV-based genetic screens essentially wrote the molecular rulebook for heterochromatin biology."

- question: "PEV demonstrates that gene expression depends not only on a gene's DNA sequence and cis-regulatory elements, but on its chromosomal neighborhood — the same intact gene can be active or silent depending on its genomic location."
  type: true-false
  answer: true
  explanation: "True, and this is the foundational principle of PEV. The white gene in variegating flies has an intact coding sequence, intact promoter, and all cis-regulatory elements — yet it is silenced in some cells purely because heterochromatin has spread to its new chromosomal location. This demonstrates that chromatin state (euchromatic vs. heterochromatic) is an independent layer of gene regulation that can override the gene's own regulatory information."

- question: "The mosaic pattern in PEV — patches of red and white ommatidia rather than individual randomly scattered red and white cells — occurs because the chromosomal inversion affects different cells differently during replication."
  type: true-false
  answer: false
  explanation: "False. The patches arise because the heterochromatic silencing decision is made once in an early progenitor cell and then faithfully inherited through all subsequent mitoses of that cell's descendants. The stochasticity is in the initial establishment event; inheritance after that is deterministic. If the pattern arose from random independent events in each ommatidium, we would expect scattered individual cells rather than coherent clonal patches. The patchy pattern is direct evidence that chromatin states are epigenetically heritable."

- question: "Why does the mosaic pattern in PEV consist of distinct patches of uniformly red or white ommatidia, rather than individual red and white cells scattered randomly? What does this pattern reveal about the mechanism of silencing?"
  type: short-answer
  answer: "The patchy pattern reveals that heterochromatin silencing is established stochastically in early developmental progenitor cells, then inherited faithfully through all subsequent cell divisions. When an early eye progenitor cell is in the heterochromatic state (white silenced), all cells descended from it will also be silenced — producing a coherent white patch of clonally related ommatidia. When a progenitor escapes heterochromatin spreading, all its descendants remain active — producing a red patch. If silencing were re-decided independently in each mature ommatidium, you would see individual cells randomly red or white with no patch structure. The patches are the fingerprint of clonal epigenetic inheritance."
  explanation: "This reasoning connects the visible phenotype directly to the molecular mechanism. Patch size also carries information: larger patches suggest silencing was established earlier in development (more cell divisions since the decision), while smaller patches suggest later establishment. This has been used to infer how early in eye development PEV silencing occurs."
```

## Explainer

From your study of higher-order chromatin structure, you know that the genome is organized into **euchromatin** (open, transcriptionally active) and **heterochromatin** (condensed, transcriptionally silent) domains. From DNA methylation and epigenetic silencing, you know that chemical modifications to DNA and histones can stably repress gene expression across cell divisions. **Position effect variegation** (PEV) is a dramatic natural experiment that reveals what happens when a normally active gene is placed at the boundary between these two chromatin states.

The classic example comes from *Drosophila* genetics. The *white* gene controls eye pigmentation — flies with a functional copy have red eyes, and loss-of-function mutants have white eyes. In certain chromosomal rearrangements (inversions or translocations), the *white* gene is moved from its normal euchromatic location to a position adjacent to pericentric heterochromatin. The result is striking: instead of uniformly red or white eyes, the fly develops a **mosaic** pattern of red and white patches — some ommatidia (eye facets) are red, others are white, producing a mottled or "variegated" appearance. The gene itself is completely intact; only its chromosomal neighborhood has changed.

The mechanism is **heterochromatin spreading**. Heterochromatin is not a static boundary — it tends to propagate along the chromosome through a self-reinforcing cycle. Methyltransferases like Su(var)3-9 add repressive histone marks (particularly H3K9 methylation), which recruit **HP1** (Heterochromatin Protein 1), which in turn recruits more Su(var)3-9, extending the silent chromatin further. When a gene like *white* sits near heterochromatin, this spreading wave may or may not reach the gene in any given cell during development. In cells where heterochromatin spreads far enough to engulf *white*, the gene is silenced — producing white ommatidia. In cells where spreading halts before reaching the gene, *white* remains active — producing red ommatidia. Because the decision is made early in development and is then **epigenetically inherited** through subsequent cell divisions, each clone of cells derived from a single progenitor is uniformly red or white, producing the characteristic patchy pattern.

PEV has been a goldmine for identifying chromatin regulators. Genetic screens for **suppressors of variegation** — Su(var) mutations that reduce silencing and make eyes more uniformly red — identified many of the key heterochromatin components: Su(var)3-9 (the H3K9 methyltransferase), Su(var)2-5 (HP1), and histone deacetylases. Conversely, **enhancers of variegation** — E(var) mutations that increase silencing — identified chromatin remodelers and histone acetyltransferases that normally oppose heterochromatin spreading. PEV thus provides a foundational framework for understanding that gene expression depends not only on a gene's sequence and its cis-regulatory elements, but critically on its **chromosomal context** — a principle with direct relevance to understanding how chromosomal rearrangements in cancer and transgene silencing in biotechnology can alter gene expression without changing the DNA sequence itself.
