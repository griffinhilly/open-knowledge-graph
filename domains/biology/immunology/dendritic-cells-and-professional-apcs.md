---
id: dendritic-cells-and-professional-apcs
title: Dendritic Cells and Professional Antigen-Presenting Cells
domain: biology
course: immunology
prerequisites:
- id: antigen-presentation-mechanisms
  type: hard
- id: major-histocompatibility-complex
  type: hard
- id: innate-immunity-overview
  type: soft
builds-toward:
- mhc-class-i-presentation
- mhc-class-ii-presentation
- follicular-helper-t-cells-tfh
tags:
- dendritic-cells
- APCs
- innate-adaptive-bridge
- antigen-presentation
stage: advanced
status: validated
---

# Dendritic Cells and Professional Antigen-Presenting Cells

## Core Idea
Dendritic cells are professional antigen-presenting cells that bridge innate and adaptive immunity. They capture antigens through pattern recognition, process them via MHC pathways, and present them to T cells with appropriate costimulation. Dendritic cell maturation and migration from tissues to secondary lymphoid organs are critical for initiating effective adaptive immune responses.

## How It's Best Learned
Study DC development from bone marrow precursors, the molecular signals that trigger maturation (TLR activation), and how they compete with other APCs to activate T cells.

## Common Misconceptions
Not all APCs are dendritic cells—macrophages and B cells also present antigen. DC maturation requires costimulatory upregulation, not just antigen uptake alone.

## Questions

```yaml
- question: "A dendritic cell in peripheral tissue takes up antigen from a dying cell, but no pathogen-associated molecular patterns (PAMPs) or TLR signals are present. What is the most likely immunological outcome?"
  type: multiple-choice
  options:
    - "The DC migrates to the lymph node and activates naive T cells, because antigen uptake is the trigger for migration"
    - "The DC presents antigen but cannot activate T cells due to low costimulatory molecule expression, potentially inducing T cell tolerance instead"
    - "The DC activates T cells via MHC class I only, since class II requires TLR signaling to load"
    - "The DC undergoes apoptosis because antigen uptake without infection signals the cell to self-destruct"
  answer: 1
  explanation: "Immature DCs are efficient antigen capturers but poor T cell activators. Without TLR-mediated maturation signals, the DC does not upregulate costimulatory molecules (CD80/CD86) or increase surface MHC expression, and it does not acquire CCR7 to migrate to lymph nodes. An immature DC presenting antigen to a naive T cell without costimulation (signal 2) typically induces anergy or tolerance in the T cell rather than activation — a mechanism that normally prevents autoimmunity by tolerizing T cells against self-antigens presented in the absence of infection. The misconception in option A conflates antigen uptake with the maturation trigger."

- question: "What is the key functional difference between an immature and a mature dendritic cell?"
  type: multiple-choice
  options:
    - "Immature DCs present antigen on MHC class I; mature DCs present on MHC class II"
    - "Immature DCs are found in lymph nodes; mature DCs patrol peripheral tissues"
    - "Immature DCs excel at capturing antigen but lack costimulatory molecules; mature DCs lose phagocytic capacity but gain the ability to activate naive T cells"
    - "Immature DCs activate CD8+ T cells; mature DCs activate CD4+ T cells"
  answer: 2
  explanation: "The two phases represent a functional switch: immature DCs in peripheral tissues are optimized for antigen capture (high phagocytic activity, macropinocytosis) but express low MHC and almost no B7 costimulatory molecules, so they cannot effectively activate T cells. TLR-mediated maturation reverses these priorities: phagocytic capacity decreases, MHC class I and II and costimulatory molecules (CD80, CD86) are dramatically upregulated, CCR7 is expressed to drive migration to lymph nodes, and the DC becomes capable of delivering both signal 1 (MHC-peptide) and signal 2 (costimulation) to naive T cells. Options A and D confuse class I/II with maturation state; option B reverses the tissue distribution."

- question: "Because dendritic cells constitutively express MHC class II molecules at most stages of their development, they can effectively activate naive T cells at any point in their life cycle."
  type: true-false
  answer: false
  explanation: "MHC class II expression alone is not sufficient for naive T cell activation. Immature DCs do express MHC class II, but at very low levels, and critically, they express almost no costimulatory molecules (B7/CD80/CD86). Naive T cell activation requires two signals: signal 1 (MHC-peptide binding the TCR) and signal 2 (costimulatory molecule binding CD28 on the T cell). Without signal 2, the T cell receiving signal 1 alone is typically driven into anergy or tolerance. Only after TLR-mediated maturation do DCs express sufficient MHC and costimulatory molecules to reliably activate naive T cells."

- question: "Dendritic cells can cross-present exogenous antigens on MHC class I molecules, allowing them to activate CD8+ cytotoxic T cells against pathogens that have not directly infected the dendritic cell itself."
  type: true-false
  answer: true
  explanation: "Cross-presentation is a specialized capability of dendritic cells (and some macrophages) that routes exogenously acquired antigen — taken up from infected or dying cells — into the MHC class I presentation pathway, which normally presents only endogenous (intracellular) peptides. This is immunologically critical: viruses and tumors that avoid infecting dendritic cells would otherwise escape CD8+ T cell recognition. Cross-presentation allows DCs to survey the entire tissue environment and initiate cytotoxic T cell responses against any cell type that is infected or transformed, making DCs indispensable for antiviral and antitumor immunity."

- question: "Why is it not sufficient for a dendritic cell to simply display antigen on MHC molecules to activate a naive T cell? What additional signal is required, and why does this requirement matter biologically?"
  type: short-answer
  answer: "T cell activation requires two signals: signal 1 is the MHC-peptide complex binding the T cell receptor, and signal 2 is costimulation via B7 molecules (CD80/CD86) on the APC binding CD28 on the T cell. Without signal 2, signal 1 alone typically induces T cell anergy or tolerance rather than activation. This two-signal requirement is biologically critical because it prevents inappropriate immune responses against self-antigens: immature DCs in tissues routinely present self-peptides on MHC, but without infection-triggered costimulatory upregulation, self-reactive T cells are tolerized rather than activated. The costimulation requirement thus serves as a gating mechanism ensuring that T cell responses are mounted only when genuine infection signals (PAMPs detected by TLRs) are present."
  explanation: "The two-signal model explains both normal immunity and autoimmune risk. In infection, PAMPs trigger DC maturation, costimulatory upregulation, and T cell activation — a productive response. In steady state, self-antigens are presented without costimulation, tolerizing autoreactive T cells. When this gate fails — for example if self-antigens are presented during inflammatory conditions that aberrantly upregulate costimulatory molecules — autoimmunity can result. Therapies that block costimulatory pathways (like CTLA-4-Ig) exploit this biology to treat autoimmune diseases and prevent transplant rejection."
```

## Explainer

You already understand that antigen presentation is the process by which immune cells display processed peptide fragments on MHC molecules for T cell recognition, and you know the structural basis of MHC class I and class II molecules. **Dendritic cells (DCs)** are the most important cells that perform this function — they are the primary link between the innate immune system, which detects pathogens nonspecifically, and the adaptive immune system, which mounts targeted responses. Without dendritic cells, T cells would rarely encounter the antigens they need to become activated.

The life cycle of a dendritic cell has two distinct phases. In their **immature** state, DCs reside in peripheral tissues — skin (where they are called Langerhans cells), mucosal surfaces, and organ interstitia — acting as sentinels. Immature DCs are voracious phagocytes: they constantly sample their environment through macropinocytosis, receptor-mediated endocytosis, and phagocytosis, internalizing pathogens, debris, and dying cells. However, immature DCs are poor at activating T cells because they express low levels of MHC and almost no costimulatory molecules (B7/CD80/CD86). They capture antigen efficiently but cannot yet present it effectively.

**Maturation** is triggered when pattern recognition receptors — particularly **Toll-like receptors (TLRs)** — detect pathogen-associated molecular patterns such as bacterial lipopolysaccharide or viral double-stranded RNA. This signal transforms the dendritic cell: it stops capturing new antigen, upregulates MHC class I and II molecules loaded with the captured pathogen's peptides, dramatically increases expression of costimulatory molecules (CD80, CD86) and the chemokine receptor CCR7, and begins migrating through lymphatic vessels toward the nearest **secondary lymphoid organ** — typically a lymph node. There, the mature DC presents antigen to naive T cells. Because the DC now expresses both the MHC-peptide complex (signal 1) and costimulatory molecules (signal 2), it can fully activate T cells rather than inducing tolerance.

Dendritic cells are not the only **professional antigen-presenting cells** — macrophages and B cells also express MHC class II and can present antigen. But DCs are uniquely suited to *initiate* adaptive responses because of their migration behavior and their ability to cross-present exogenous antigens on MHC class I (activating CD8+ T cells against viruses and tumors that the DC itself is not infected by). Macrophages primarily present antigen to already-activated T cells arriving at infection sites, and B cells present antigen to receive T cell help for antibody production. The division of labor is clear: dendritic cells start the adaptive response, while macrophages and B cells participate in executing it.
