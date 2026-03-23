---
id: cell-adhesion-tissue
title: Cell Adhesion Molecules and Tissue Interactions
domain: biology
course: cell-biology
prerequisites:
- id: cell-migration-motility
  type: soft
builds-toward:
- gap-junctions-communication
tags:
- cell-adhesion
- extracellular-matrix
- integrins
- cadherins
stage: formal-systems
status: validated
---

# Cell Adhesion Molecules and Tissue Interactions

## Core Idea
Cells adhere to each other and the extracellular matrix through adhesion molecules: cadherins mediate calcium-dependent, homophilic cell-cell contacts and are critical for tissue integrity; integrins are heterodimeric receptors that bind matrix proteins (collagen, fibronectin, laminin) and couple the matrix to the cytoskeleton. Adhesion is not passive; signals from the matrix (through integrins) and cell-cell contacts (through cadherins) regulate gene expression, cell survival, and proliferation. Loss of adhesion is a hallmark of metastatic cancer; restoration of adhesion is a goal of therapeutic intervention.

## Questions

```yaml
- question: "A circulating white blood cell is normally non-adhesive in the bloodstream, but rapidly becomes adhesive and latches onto an inflamed vessel wall. Which mechanism best explains this switch?"
  type: multiple-choice
  options:
    - "Inside-out integrin signaling — intracellular signals change integrin conformation from a low-affinity to a high-affinity state"
    - "Outside-in integrin signaling — matrix proteins on the vessel wall bind integrins and trigger intracellular adhesion cascades"
    - "E-cadherin upregulation — the white blood cell expresses E-cadherin that binds matching E-cadherin on the endothelium"
    - "Calcium influx — elevated intracellular calcium activates cadherin bonds between the cell and the vessel wall"
  answer: 0
  explanation: "Inside-out signaling is the mechanism by which intracellular signals change an integrin's conformation from a bent, low-affinity state to an extended, high-affinity state — enabling rapid on-demand adhesion to extracellular ligands. This is exactly how leukocytes become adhesive during inflammation. Outside-in signaling (option B) runs in the opposite direction: matrix binding triggers intracellular cascades. Cadherins mediate cell-cell adhesion, not immune cell adhesion to blood vessel walls, and their activation requires calcium but not conformational switching in the same way."

- question: "A researcher uses EDTA (a calcium chelator) to dissociate an epithelial tissue into single cells. What is the most direct molecular explanation?"
  type: multiple-choice
  options:
    - "Cadherin-mediated adhesion requires calcium; removing it causes cadherin bonds between cells to fall apart"
    - "Integrins require calcium to bind collagen and fibronectin; removing it breaks all cell-matrix contacts"
    - "Calcium powers mitochondrial ATP synthesis; removing it depletes energy and stops all active adhesion processes"
    - "Calcium stabilizes the lipid bilayer; removing it causes plasma membranes to dissolve"
  answer: 0
  explanation: "Cadherins are calcium-dependent — their extracellular domains require calcium ions to fold into the correct conformation for homophilic binding. Remove calcium and cadherin bonds collapse immediately, which is why EDTA (which chelates calcium) is the standard lab method for dissociating epithelial tissues. While integrins are also affected by calcium removal, the primary mechanism for disrupting epithelial cell-cell contacts specifically is cadherin inactivation."

- question: "Cell adhesion molecules serve only a structural role — holding cells together like molecular glue — without influencing cell behavior or fate."
  type: true-false
  answer: false
  explanation: "Adhesion molecules are active signaling receptors. Integrins, when bound to matrix proteins, activate focal adhesion kinase (FAK) and downstream cascades that regulate cell survival, proliferation, and gene expression. Cells deprived of matrix contact often die by apoptosis (anoikis) precisely because they lose these survival signals. Cadherins similarly signal through catenins that intersect with Wnt signaling pathways. Adhesion does not just hold cells in place — it tells them where they are and whether they should live, divide, or differentiate."

- question: "Downregulation of E-cadherin in epithelial tumor cells is associated with increased invasiveness and metastatic potential."
  type: true-false
  answer: true
  explanation: "E-cadherin maintains the adhesive bonds between epithelial cells, organizing them into coherent sheets. When tumor cells downregulate E-cadherin — often through epithelial-mesenchymal transition (EMT) — they lose these connections, acquire a more migratory phenotype, and can invade surrounding tissue and enter the bloodstream to seed distant metastases. E-cadherin is sometimes called a 'suppressor of invasion' for this reason, and its loss is one of the hallmarks of metastatic cancer."

- question: "Explain why 'outside-in' integrin signaling is important beyond simply maintaining physical attachment to the extracellular matrix."
  type: short-answer
  answer: "Outside-in signaling links the state of the extracellular environment to intracellular decisions about survival, proliferation, and gene expression. When integrins bind matrix proteins, they activate focal adhesion kinase (FAK) and downstream cascades that function as survival signals — cells lacking matrix contact often undergo apoptosis (anoikis). This means adhesion is not just an anchor: it is a sensor that informs the cell whether it is in the correct tissue context. Different matrix compositions trigger different signaling outputs, which is why cells behave differently in different extracellular environments."
  explanation: "The bidirectionality of integrin signaling makes adhesion a two-way communication channel between cell and environment. Inside-out signaling allows cells to rapidly modulate their grip on the matrix in response to internal signals (as in leukocyte activation). Outside-in signaling allows the matrix to instruct the cell about its context. Together, these mechanisms mean that the physical connection between a cell and its surroundings is inseparable from the biochemical information flowing across that connection."
```

## Explainer

From your understanding of cell migration, you know that cells interact physically with their surroundings through integrin-based focal adhesions and cytoskeletal dynamics. Cell adhesion builds on this concept: rather than just enabling movement, adhesion molecules create the stable connections that hold tissues together and allow cells to communicate with their neighbors and the extracellular matrix. Without adhesion, a tissue would be nothing more than a bag of loose cells.

The two major families of adhesion molecules serve different purposes. **Cadherins** are cell-to-cell adhesion proteins that require calcium ions to function — remove the calcium, and cadherin bonds fall apart, which is why the chelating agent EDTA is used to dissociate tissues in the lab. Cadherins are **homophilic**, meaning E-cadherin on one cell binds to E-cadherin on an adjacent cell. Different tissues express different cadherins: epithelial cells express E-cadherin, neural cells express N-cadherin, and this differential expression is one mechanism by which cells of the same type find and stick to each other during development, a phenomenon called **cell sorting**. On the intracellular side, cadherins connect to the actin cytoskeleton through adaptor proteins called catenins (α-, β-, and p120-catenin), creating a continuous mechanical link from one cell's cytoskeleton through the adhesion junction to the next cell's cytoskeleton.

**Integrins** handle cell-to-matrix adhesion. They are **heterodimers** — each composed of one α and one β subunit — and their particular combination determines which matrix protein they bind (collagen, fibronectin, laminin, and others). A remarkable feature of integrins is **bidirectional signaling**. In "outside-in" signaling, binding to the extracellular matrix triggers intracellular signaling cascades through focal adhesion kinase (FAK) that regulate cell survival, proliferation, and gene expression. In "inside-out" signaling, intracellular signals change the integrin's conformation from a bent, low-affinity state to an extended, high-affinity state, allowing the cell to rapidly modulate its grip on the matrix. This is how a circulating white blood cell, initially non-adhesive, can quickly latch onto an inflamed blood vessel wall.

The importance of adhesion becomes starkly visible in disease. In **metastatic cancer**, tumor cells typically downregulate E-cadherin (often through a process called **epithelial-mesenchymal transition**), loosening their connections to neighboring cells and enabling them to invade surrounding tissue and enter the bloodstream. Conversely, genetic defects in integrins cause diseases like **leukocyte adhesion deficiency**, where immune cells cannot adhere to blood vessel walls and therefore cannot reach sites of infection. These examples illustrate that adhesion is not merely structural glue — it is an active signaling system that tells cells where they are, whether they should survive, and how they should behave.
