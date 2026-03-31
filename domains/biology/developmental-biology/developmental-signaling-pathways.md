---
id: developmental-signaling-pathways
title: Developmental Signaling (Wnt/Hedgehog/Notch/BMP)
domain: biology
course: developmental-biology
prerequisites:
- id: cell-signaling-intro
  type: hard
- id: induction-and-competence
  type: hard
builds-toward:
- chromatin-in-development
- regeneration-biology
tags:
- Wnt
- Hedgehog
- Notch
- BMP
- developmental-signaling
stage: expert
status: validated
---
# Developmental Signaling (Wnt/Hedgehog/Notch/BMP)

## Core Idea
Four signaling pathways — Wnt, Hedgehog (Hh), Notch, and BMP/TGF-beta — are the core communication toolkit of animal development, used iteratively from gastrulation through organogenesis. Each operates through a distinct mechanism: Wnt stabilizes beta-catenin to activate TCF/LEF transcription factors; Hedgehog relieves Patched-mediated repression of Smoothened to activate Gli transcription factors; Notch uses direct cell-cell contact and receptor cleavage to release the Notch intracellular domain (NICD) as a transcription factor; BMP/TGF-beta signals through receptor serine/threonine kinases that phosphorylate Smad transcription factors. These pathways are reused in different tissues and at different times, with the cellular response determined by context — which other transcription factors are present and which chromatin regions are accessible.

## Questions

```yaml
- question: "The Notch pathway differs from Wnt, Hedgehog, and BMP signaling in a fundamental way. What is this difference?"
  type: multiple-choice
  options:
    - "Notch signaling requires direct physical contact between the signal-sending and signal-receiving cells, because the ligand (Delta/Jagged) and receptor (Notch) are both transmembrane proteins — no diffusible morphogen is involved"
    - "Notch is the only pathway that uses transcription factors"
    - "Notch signaling is unique to vertebrates; the other pathways exist in all animals"
    - "Notch does not involve gene expression changes"
  answer: 0
  explanation: "Wnt, Hedgehog, and BMP all use secreted, diffusible ligands that can act over distances (morphogen gradients). Notch requires juxtacrine signaling — the Delta/Jagged ligand on one cell's surface directly engages the Notch receptor on the adjacent cell's surface. This mechanical interaction triggers proteolytic cleavage of Notch, releasing its intracellular domain (NICD), which translocates to the nucleus and activates transcription. This contact-dependent mechanism makes Notch uniquely suited for local cell-fate decisions between immediate neighbors (like lateral inhibition), while the other pathways can pattern tissues over longer ranges."

- question: "When Wnt ligand binds its receptor Frizzled and co-receptor LRP5/6, it prevents the destruction complex from degrading beta-catenin. Without Wnt, beta-catenin is constitutively destroyed."
  type: true-false
  answer: true
  explanation: "The Wnt pathway is unusual in that the 'default' state (no signal) involves active destruction of the key effector. The destruction complex (APC, Axin, GSK3-beta, CK1) phosphorylates beta-catenin, marking it for ubiquitination and proteasomal degradation. When Wnt ligand engages Frizzled and LRP5/6, Axin is recruited to the membrane, disrupting the destruction complex. Unphosphorylated beta-catenin accumulates, enters the nucleus, binds TCF/LEF transcription factors, and activates target genes. This 'double-negative' logic (signal inhibits an inhibitor) means that mutations inactivating APC (a component of the destruction complex) constitutively activate Wnt signaling — this is the initiating event in most colorectal cancers."

- question: "Why are the same four signaling pathways reused throughout development rather than the organism evolving specialized pathways for each organ?"
  type: short-answer
  answer: "Reusing a small toolkit of well-characterized pathways is more evolvable than inventing new pathways for each context. The pathways themselves provide the signaling logic (activate/repress target genes), while specificity comes from the cellular context — which transcription factors are already present, which chromatin regions are accessible, and which pathway components are expressed. A cell in the neural tube and a cell in the limb bud can both receive Shh signaling but interpret it differently because they express different transcription factors. This context-dependent interpretation means evolutionary innovation can occur by changing when and where a pathway is active (regulatory mutations) without redesigning the signal transduction machinery. This is far more mutationally accessible than evolving new receptor-ligand pairs."
  explanation: "This principle — versatile reuse of a limited toolkit — is one of the core insights of evo-devo. It explains why loss-of-function mutations in developmental signaling pathways tend to have pleiotropic effects (disrupting multiple organs that use the same pathway) and why gain-of-function mutations in these pathways are common drivers of cancer."
```

## Explainer

If you could watch a developing embryo and highlight every cell that is sending or receiving a Wnt, Hedgehog, Notch, or BMP signal, virtually the entire embryo would light up at every stage. These four pathways are the workhorses of animal development, used and reused from the earliest cell fate decisions through the final refinements of organ architecture. Understanding their mechanisms and how cells interpret them in context is foundational to developmental biology.

**Wnt signaling** (canonical pathway) controls cell proliferation, stem cell maintenance, and axis patterning. Its logic is based on a "destruction complex" — in the absence of Wnt ligand, the complex (APC, Axin, GSK3-beta) phosphorylates beta-catenin, targeting it for degradation. When Wnt binds Frizzled and LRP5/6, the destruction complex is inactivated, beta-catenin accumulates and enters the nucleus, and target genes are activated. This pathway maintains intestinal stem cells, patterns the AP axis, and drives limb development. Constitutive activation (by APC mutations) is the initiating event in most colorectal cancers.

**Hedgehog signaling** patterns the neural tube, limb, and many other organs. The unique feature is the primary cilium — a cellular antenna where signal transduction occurs. Without Hedgehog ligand, the receptor Patched inhibits the co-receptor Smoothened. Hedgehog binding to Patched relieves this inhibition, Smoothened activates Gli transcription factors, and target genes are expressed. The concentration of Hedgehog signal determines which target genes are activated, enabling morphogen-gradient patterning. Sonic Hedgehog (Shh) is the key vertebrate ligand, patterning ventral neural tube cell types and digit identity.

**Notch signaling** is the only juxtacrine pathway — it requires direct cell contact. The ligand (Delta or Jagged) on one cell binds the Notch receptor on a neighboring cell, triggering proteolytic cleavage that releases the Notch intracellular domain (NICD). NICD enters the nucleus and activates target genes (like Hes and Hey). Because Notch requires contact, it operates strictly between adjacent cells, making it ideal for **lateral inhibition** — ensuring that neighboring cells adopt different fates. Classic examples include the spacing of neural precursors in Drosophila and the differentiation of intestinal cell types.

**BMP/TGF-beta signaling** patterns the dorsal-ventral axis, drives bone and cartilage formation, and regulates cell growth and apoptosis. BMP ligands bind type I and type II serine/threonine kinase receptors, which phosphorylate Smad transcription factors. Phosphorylated Smads complex with Co-Smad (Smad4), enter the nucleus, and regulate target gene expression. BMP signaling is counteracted by secreted antagonists (Chordin, Noggin) from the organizer — this opposition between BMP and its inhibitors is one of the most ancient patterning mechanisms in animal development. Each of these pathways is simple in its molecular logic but generates extraordinary diversity through context-dependent interpretation.
