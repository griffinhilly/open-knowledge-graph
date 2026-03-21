---
id: stem-cells-pluripotency
title: Stem Cells and Maintenance of Pluripotency
domain: biology
course: cell-biology
prerequisites:
- id: cell-differentiation-lineage
  type: hard
tags:
- stem-cells
- pluripotency
- self-renewal
- oct4-sox2-nanog
stage: advanced
status: draft
---

# Stem Cells and Maintenance of Pluripotency

## Core Idea
Pluripotent stem cells (embryonic stem cells, induced pluripotent stem cells) can both self-renew (divide to produce more stem cells) and differentiate into any cell type. Pluripotency is maintained by a network of transcription factors (Oct4, Sox2, Nanog) that activate pluripotency genes, silence differentiation genes, and maintain open chromatin architecture. Breaking this network (via withdrawal of cytokines like LIF, or forced expression of differentiation TFs) triggers lineage commitment. Understanding stem cell biology enables regenerative medicine and reveals how reprogramming occurs in cancer cells.

## Questions

```yaml
- question: "A fully differentiated skin cell contains the same complete genome as an embryonic stem cell but cannot give rise to neurons or muscle cells under normal conditions. The best explanation for this is:"
  type: multiple-choice
  options:
    - "The skin cell has permanently deleted the genes for neuronal and muscle proteins through DNA recombination"
    - "The skin cell's differentiation genes have been mutated by accumulated DNA damage, making reprogramming impossible"
    - "Epigenetic controls and the absence of the Oct4/Sox2/Nanog network keep differentiation genes silenced and pluripotency genes inactive"
    - "The skin cell lacks the ribosomes necessary to translate the mRNA for pluripotency transcription factors"
  answer: 2
  explanation: "Differentiation is a regulatory state, not a genetic erasure. The skin cell retains all the genes for other cell types — what has changed is their expression state. DNA methylation and histone modifications silence genes not appropriate for skin cell identity, and the Oct4/Sox2/Nanog feedback circuit that maintained pluripotency has been dismantled. Option A is disproved by Yamanaka's reprogramming experiments: if genes were deleted, introducing four transcription factors could not restore pluripotency. The whole genome is still present in each differentiated cell."

- question: "The Oct4, Sox2, and Nanog transcription factors maintain pluripotency primarily by:"
  type: multiple-choice
  options:
    - "Repairing DNA damage that would otherwise trigger differentiation"
    - "Blocking the cell cycle, preventing differentiation-inducing cell divisions"
    - "Activating pluripotency genes, repressing differentiation genes, and reinforcing each other's expression in a self-sustaining circuit"
    - "Directly producing the signaling molecules that instruct neighboring cells to remain undifferentiated"
  answer: 2
  explanation: "The Oct4/Sox2/Nanog network operates as a transcriptional master regulator: these factors bind thousands of genomic loci, activating genes needed for the undifferentiated state and repressing genes that would trigger specialization. Crucially, they also activate each other's expression, creating a positive feedback loop that is self-sustaining as long as external signals (like LIF in mouse ES cells) are present. The open chromatin architecture of pluripotent cells complements this — differentiation genes are poised but suppressed. When the circuit is disrupted, the balance tips and lineage commitment follows."

- question: "When a stem cell differentiates into a specialized cell type, it permanently deletes the genes required for all other cell fates from its genome."
  type: true-false
  answer: false
  explanation: "Differentiation involves epigenetic silencing, not genetic deletion. Differentiated cells contain the same complete genome as the fertilized egg from which they descended. Genes for irrelevant cell types are silenced through DNA methylation and repressive histone modifications, but the underlying DNA sequences are preserved. The proof is Yamanaka's 2006 demonstration: introducing just four transcription factors (Oct4, Sox2, Klf4, c-Myc) into adult skin or liver cells reprogrammed them to iPSCs with broad differentiation potential — impossible if the genes had been physically removed."

- question: "The ability to reprogram differentiated adult cells back to a pluripotent state by introducing transcription factors demonstrates that the differentiated state is maintained by regulatory controls, not by irreversible changes to the DNA sequence."
  type: true-false
  answer: true
  explanation: "Yamanaka's reprogramming experiment is definitive evidence on this point. If differentiation were caused by permanent genetic changes — gene deletions, irreversible mutations — then no combination of transcription factors could restore pluripotency. The fact that introducing Oct4, Sox2, Klf4, and c-Myc is sufficient to erase an adult cell's differentiated identity and reinstate pluripotency shows that differentiation is a regulatory state imposed on a preserved genome. Epigenetic marks (methylation, histone modifications) maintain this state but are themselves reversible under the right conditions."

- question: "Why might cancer cells sometimes reactivate pluripotency transcription factors like Oct4, and what does this suggest about the relationship between pluripotency and uncontrolled proliferation?"
  type: short-answer
  answer: "The Oct4/Sox2/Nanog network not only maintains pluripotency but also promotes self-renewal — the ability to divide indefinitely while remaining undifferentiated. Cancer cells often acquire mutations or epigenetic changes that aberrantly reactivate this network, effectively de-differentiating and gaining stem cell-like properties: uncontrolled proliferation, resistance to differentiation signals, and the ability to give rise to multiple cell types within a tumor. This explains why some aggressive cancers contain 'cancer stem cells' and why high Oct4 expression is associated with poor prognosis in several cancer types."
  explanation: "The overlap between pluripotency and cancer is not coincidental — the molecular machinery for self-renewal is the same in both contexts. What differs is the regulatory context: in normal embryonic development, the pluripotency network is under tight control and eventually dismantled as lineage commitment proceeds. In cancer, this network is reactivated out of developmental context, without the normal signals that would eventually trigger differentiation. This also explains why c-Myc, one of Yamanaka's four reprogramming factors, is one of the most commonly activated oncogenes."
```

## Explainer

From your study of cell differentiation, you know that cells progressively narrow their identity — a fertilized egg can become anything, but a mature neuron or muscle cell is locked into its fate. Stem cells sit at the top of this hierarchy. A **pluripotent** stem cell retains the ability to become virtually any cell type in the body, while simultaneously being able to divide and produce more copies of itself. This dual capacity — **self-renewal** plus **differentiation potential** — is what makes stem cells biologically extraordinary and medically valuable.

The molecular basis of pluripotency centers on a small network of **transcription factors**, most importantly **Oct4**, **Sox2**, and **Nanog**. These proteins bind to thousands of gene promoters throughout the genome, activating genes that maintain the undifferentiated state and repressing genes that would trigger specialization. They also reinforce each other's expression, creating a self-sustaining feedback loop. As long as this circuit is active, the cell remains pluripotent. The chromatin itself cooperates: pluripotent cells maintain an unusually open chromatin architecture, keeping differentiation genes accessible but silent — poised to activate but held in check.

Differentiation begins when this network is disrupted. External signals — the withdrawal of growth factors like **LIF (leukemia inhibitory factor)** in mouse embryonic stem cells, or exposure to specific morphogens — tip the balance. Oct4 and Nanog levels fall, silenced differentiation genes become active, and the cell commits to a lineage: ectoderm, mesoderm, or endoderm. Once committed, epigenetic changes (DNA methylation, histone modification) lock in the new identity, making the transition effectively irreversible under normal conditions.

The discovery that differentiation can be reversed was transformative. In 2006, Shinya Yamanaka showed that introducing just four transcription factors (Oct4, Sox2, Klf4, and c-Myc) into ordinary adult cells could reprogram them back to a pluripotent state, creating **induced pluripotent stem cells (iPSCs)**. This demonstrated that differentiation is not the permanent erasure of potential — it is a reversible regulatory state maintained by epigenetic controls. iPSCs open the door to patient-specific cell therapies without the ethical concerns of embryonic stem cells, and they reveal why cancer cells sometimes reactivate pluripotency genes: the same transcription factor network that maintains stem cell identity can, when aberrantly reactivated, drive uncontrolled proliferation.
