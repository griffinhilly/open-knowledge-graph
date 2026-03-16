---
id: t-cell-activation-costimulation
title: T Cell Activation and Costimulatory Signals
domain: biology
course: immunology
prerequisites:
- id: t-cell-receptor-structure
  type: hard
- id: antigen-presentation-mechanisms
  type: hard
- id: cytokines-and-chemokines
  type: soft
builds-toward:
- cd4-t-helper-cells
- cd8-cytotoxic-t-cells
- regulatory-t-cells-immune-tolerance
tags:
- adaptive
- t-cell
- activation
- signaling
stage: advanced
status: draft
---

# T Cell Activation and Costimulatory Signals

## Core Idea
T cell activation requires two signals: TCR engagement with MHC-peptide (signal 1) and costimulation via CD28 binding CD80/CD86 on antigen-presenting cells (signal 2). Signal 1 alone leads to anergy (functional inactivation). Costimulation induces IL-2 production and IL-2 receptor upregulation, driving proliferation and differentiation.

## Questions

```yaml
- question: "A T cell's TCR engages an MHC-peptide complex on an antigen-presenting cell, but the APC lacks CD80 and CD86 expression. What is the most likely outcome for the T cell?"
  type: multiple-choice
  options: ["Full activation with IL-2 secretion", "Anergy — functional inactivation without response", "Immediate apoptosis via Fas-FasL signaling", "Differentiation into a regulatory T cell"]
  answer: 1
  explanation: "Without CD80/CD86, CD28 cannot deliver signal 2. TCR engagement (signal 1) alone drives T cell anergy — the cell is rendered functionally unresponsive rather than activated. This is a deliberate safeguard against autoimmunity: self-reactive T cells that encounter antigen without proper APC context are silenced rather than expanded."

- question: "The requirement for two signals (TCR engagement plus CD28 costimulation) before a T cell fully activates serves as a safeguard against inappropriate immune responses to self-tissue."
  type: true-false
  answer: true
  explanation: "Normal self-tissues typically express MHC-peptide but lack the co-stimulatory molecules CD80/CD86, which are upregulated on APCs primarily during infection or inflammation. A T cell that recognizes self-antigen in the absence of costimulation becomes anergic rather than activated, preventing autoimmune attack on healthy tissue."

- question: "What cytokine does costimulation primarily induce T cells to produce, and why is that cytokine's receptor also upregulated at the same time?"
  type: short-answer
  answer: "Costimulation induces IL-2 production. The IL-2 receptor (IL-2R, specifically the high-affinity alpha chain CD25) is upregulated simultaneously so the activated T cell can respond to the IL-2 it secretes in an autocrine loop, driving its own proliferation and differentiation."
  explanation: "IL-2 is the primary T cell growth factor. Producing IL-2 without upregulating its receptor would be wasteful; co-upregulation creates an autocrine positive-feedback loop that amplifies the activated T cell clone rapidly. This two-step logic — produce the signal and the receptor simultaneously — is a recurring theme in lymphocyte activation."
```

## Explainer

T cell activation is a deliberate two-key security system. A T cell that recognizes antigen through its T cell receptor (TCR) receives what is called signal 1 — confirmation that the right peptide-MHC complex is present. But signal 1 alone is not enough. Without a second, independent signal, the T cell does not activate; instead, it enters a state of anergy, becoming functionally deaf to further stimulation. The reason for this stringency is immunological self-tolerance: self-tissues display peptide-MHC complexes too, and the immune system must not attack them.

Signal 2 is delivered by costimulation: the T cell surface receptor CD28 binds to CD80 or CD86 expressed on the antigen-presenting cell. Critically, CD80/CD86 are not constitutively expressed on every cell — they are upregulated on dendritic cells, macrophages, and B cells in response to infection, inflammation, or Toll-like receptor activation. This means costimulation is a proxy for "a genuine immune threat is present," not just "antigen is present." Self-tissue under normal conditions lacks these ligands, so self-reactive T cells that escape thymic deletion get silenced here instead.

When both signals arrive together, the T cell undergoes a dramatic shift. The transcription factor NFAT is dephosphorylated and enters the nucleus, driving IL-2 gene expression. Simultaneously, the high-affinity IL-2 receptor (which includes the CD25 alpha chain) is upregulated on the cell surface. The T cell thus both produces IL-2 and expresses the receptor to respond to it — a tight autocrine loop that fuels rapid clonal expansion over hours to days.

The downstream consequences of full activation depend on context: CD4+ T cells receiving costimulation in the presence of different cytokines differentiate into distinct helper subsets (Th1, Th2, Th17, Tfh), each specialized for different threats. CD8+ T cells become cytotoxic killers. Without costimulation, none of this differentiation occurs — the two-signal requirement is a filter that gates the entire adaptive immune response.

Understanding this checkpoint has direct therapeutic relevance. Blocking costimulation (e.g., with CTLA-4-Ig, which competes with CD28 for CD80/CD86) suppresses transplant rejection and autoimmunity. Conversely, anti-CTLA-4 antibodies (like ipilimumab) remove an inhibitory signal that mimics the absence of costimulation, reinvigorating exhausted anti-tumor T cells. The two-signal model is not just textbook biology — it is an active target in modern immunotherapy.
