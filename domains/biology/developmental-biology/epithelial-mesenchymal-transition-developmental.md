---
id: epithelial-mesenchymal-transition-developmental
title: Epithelial-Mesenchymal Transition
domain: biology
course: developmental-biology
prerequisites:
- id: cell-migration-in-development
  type: hard
- id: gastrulation
  type: hard
builds-toward: []
tags:
- EMT
- MET
- E-cadherin
- Snail
- metastasis
stage: expert
status: validated
---
# Epithelial-Mesenchymal Transition

## Core Idea
Epithelial-mesenchymal transition (EMT) is a cellular program in which polarized epithelial cells lose their cell-cell adhesions, apical-basal polarity, and epithelial gene expression, and gain migratory, invasive, mesenchymal properties. EMT is driven by transcription factors (Snail, Slug, Twist, ZEB1/2) that repress E-cadherin and activate mesenchymal genes like vimentin and N-cadherin. EMT occurs during normal development (gastrulation, neural crest delamination, heart valve formation) and is pathologically reactivated during cancer metastasis, where it enables tumor cells to invade surrounding tissues and enter the bloodstream. The reverse process (MET, mesenchymal-epithelial transition) is equally important in development and in metastatic colonization.

## Questions

```yaml
- question: "Why is downregulation of E-cadherin the hallmark molecular event of EMT?"
  type: multiple-choice
  options:
    - "E-cadherin is a protease that degrades the basement membrane"
    - "E-cadherin is the primary cell-cell adhesion molecule in epithelial tissues; its loss dissolves adherens junctions, disrupts epithelial integrity, frees cells from their neighbors, and is both necessary and sufficient for the transition from cohesive epithelial behavior to individual migratory behavior"
    - "E-cadherin blocks cell division; its loss allows proliferation"
    - "E-cadherin is a mesenchymal marker that must be removed for epithelial identity"
  answer: 1
  explanation: "E-cadherin (encoded by CDH1) is the master adhesion molecule of epithelial tissues. It mediates calcium-dependent homophilic cell-cell adhesion at adherens junctions and connects to the actin cytoskeleton through catenins. When EMT transcription factors (Snail, ZEB1/2) repress E-cadherin transcription, the adherens junctions disassemble, the cells lose their connection to neighbors, apical-basal polarity collapses (because polarity complexes are anchored at junctions), and the cells acquire the ability to migrate individually. Re-expression of E-cadherin (during MET) reverses this, restoring adhesion and epithelial character. CDH1 loss is also one of the most common genetic events in invasive lobular breast cancer."

- question: "EMT produces a complete, binary switch from epithelial to mesenchymal identity in all biological contexts."
  type: true-false
  answer: false
  explanation: "Recent research has revealed that EMT is often partial, producing cells in intermediate or 'hybrid' states that express both epithelial and mesenchymal markers simultaneously. These partial-EMT states are increasingly recognized as biologically important: in development, migrating cells often retain some cell-cell adhesion (enabling collective migration), and in cancer, partial-EMT cells at the tumor invasive front may be more metastatic than fully mesenchymal cells. EMT is better understood as a spectrum of states rather than a binary switch, with different signaling contexts producing different positions along the epithelial-mesenchymal continuum."

- question: "How does EMT contribute to cancer metastasis, and why must the reverse process (MET) also occur for successful metastatic colonization?"
  type: short-answer
  answer: "EMT enables cancer cells at the primary tumor to lose epithelial adhesion, invade through the basement membrane and surrounding stroma, and enter blood or lymphatic vessels (intravasation). The mesenchymal properties — motility, invasiveness, resistance to anoikis (cell death upon detachment) — are essential for these early metastatic steps. However, at the distant metastatic site, the cells must re-establish epithelial character (MET) to form the cell-cell adhesions and proliferative capacity needed to grow into a macroscopic metastasis. Purely mesenchymal cells are migratory but proliferate slowly; purely epithelial cells proliferate but cannot invade. Successful metastasis requires plasticity — the ability to switch between states as needed for each step of the metastatic cascade."
  explanation: "This requirement for both EMT and MET during metastasis suggests that therapeutic targeting of EMT could be counterproductive if it forces cells into a fully epithelial state at the wrong location — a concern that has complicated anti-EMT drug development. Targeting the plasticity itself (the ability to switch) may be more effective."
```

## Explainer

Epithelial tissues are defined by their organization: cells are tightly connected to each other through adherens junctions, tight junctions, and desmosomes, forming continuous sheets with defined apical (top) and basal (bottom) surfaces. This organization is essential for barrier function (skin, gut lining) and secretion (glands). Mesenchymal cells, by contrast, are loosely organized, embedded in extracellular matrix, and capable of individual migration. The **epithelial-mesenchymal transition** is the cellular program that converts one into the other — and it is one of the most consequential processes in both normal development and disease.

During development, EMT occurs at several critical moments. At **gastrulation**, cells that will form mesoderm and endoderm undergo EMT to leave the epithelial epiblast and migrate into the interior of the embryo. During **neural crest delamination**, cells at the border of the neural plate undergo EMT to become the migratory neural crest population. In **heart development**, endocardial cells undergo EMT to form the cardiac cushions that will become heart valves. In each case, the molecular mechanism involves activation of **EMT transcription factors** (Snail, Slug, Twist, ZEB1, ZEB2) by developmental signaling pathways (TGF-beta, Wnt, FGF, Notch). These transcription factors repress E-cadherin and other epithelial genes while activating mesenchymal genes (vimentin, N-cadherin, matrix metalloproteinases).

The reverse process, **MET** (mesenchymal-epithelial transition), is equally important. After neural crest cells reach their destinations, some undergo MET to form epithelial structures (like dorsal root ganglia). During kidney development, metanephric mesenchyme undergoes MET to form the epithelial nephron tubules. MET involves the reactivation of E-cadherin expression, re-establishment of cell-cell junctions and polarity, and suppression of mesenchymal genes. The ability to switch between epithelial and mesenchymal states — **epithelial plasticity** — is a fundamental property that enables the morphogenetic flexibility required during development.

In **cancer**, EMT is pathologically reactivated. Tumor cells at the invasive front of epithelial cancers often show reduced E-cadherin, increased vimentin, and nuclear localization of EMT transcription factors. These cells have acquired the ability to detach from the primary tumor, invade surrounding tissue, enter blood vessels, and survive in circulation — the early steps of metastasis. Recent work has shown that the most dangerous metastatic cells may not undergo full EMT but rather exist in **partial EMT states**, retaining some epithelial adhesion (enabling collective migration and clusters in circulation, which have higher metastatic efficiency than individual cells) while gaining enough mesenchymal character to invade. At distant sites, successful metastatic cells undergo MET to proliferate and form secondary tumors. This dynamic epithelial-mesenchymal plasticity, not a one-way EMT, drives the metastatic process.
