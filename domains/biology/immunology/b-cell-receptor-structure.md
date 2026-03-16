---
id: b-cell-receptor-structure
title: B Cell Receptor Structure and Signaling
domain: biology
course: immunology
prerequisites:
- id: b-cell-development-maturation
  type: hard
- id: cell-signaling-intro
  type: hard
- id: protein-secondary-structure
  type: soft
builds-toward:
- antibody-structure-and-function
tags:
- adaptive
- b-cell
- receptor
- signaling
stage: advanced
status: draft
---

# B Cell Receptor Structure and Signaling

## Core Idea
The B cell receptor (BCR) is membrane-bound immunoglobulin plus CD19/CD21 coreceptors and Ig-α/Ig-β signaling chains. BCR engagement without costimulation leads to anergy; engagement plus toll-like receptor signaling or CD40 ligation activates the B cell. BCR crosslinking activates Src family kinases, leading to calcium release and transcription factor activation.

## Explainer

You know from B cell development that B cells arise in the bone marrow and undergo a selection process that eliminates self-reactive clones. The molecule at the center of this selection — and of every subsequent encounter with antigen — is the **B cell receptor (BCR)**. Structurally, the BCR is a membrane-anchored immunoglobulin molecule: it has the same heavy-chain and light-chain architecture as a secreted antibody, but its heavy chain includes a hydrophobic transmembrane segment that anchors it in the plasma membrane. Each B cell displays roughly 50,000–100,000 copies of its BCR, all with identical antigen specificity.

However, the immunoglobulin portion of the BCR cannot signal on its own — its cytoplasmic tail is only about three amino acids long, far too short to recruit intracellular signaling machinery. Signaling depends on a pair of associated transmembrane proteins called **Igα** (CD79a) and **Igβ** (CD79b), which form a disulfide-linked heterodimer. Each chain contains an **immunoreceptor tyrosine-based activation motif (ITAM)** in its cytoplasmic tail. When antigen binds the BCR, clustering of receptors brings these ITAMs into proximity, and Src-family kinases (primarily Lyn) phosphorylate the tyrosine residues within the ITAMs. This phosphorylation creates docking sites for the kinase **Syk**, which then phosphorylates downstream adaptor proteins, triggering a signaling cascade that activates phospholipase Cγ2, releases intracellular calcium, and ultimately turns on transcription factors like NF-κB and NFAT.

The BCR does not work in isolation. A **coreceptor complex** consisting of CD19, CD21 (complement receptor 2), and CD81 dramatically lowers the threshold for B cell activation. When an antigen is tagged with complement fragment C3d, CD21 binds C3d while the BCR simultaneously binds the antigen. This co-engagement brings CD19 into the signaling cluster, amplifying the signal by roughly 1,000-fold. This is why complement-opsonized antigens are far more immunogenic than naked antigens — the coreceptor turns a whisper into a shout.

Critically, the outcome of BCR signaling depends on context. BCR engagement alone — without costimulatory signals from helper T cells (via CD40 ligand) or innate pattern-recognition receptors (like toll-like receptors) — drives the B cell into **anergy**, a state of functional unresponsiveness. This ensures that B cells recognizing self-antigens in the absence of danger signals are silenced rather than activated. Only when BCR signaling is accompanied by a second signal does the B cell proliferate, undergo class switching, and differentiate into antibody-secreting plasma cells or memory B cells.
