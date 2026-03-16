---
id: receptor-signaling-pathways
title: Receptor Signaling Pathways (RTKs, GPCRs, and Second Messengers)
domain: biology
course: biochemistry
prerequisites:
- id: cell-signaling-intro
  type: hard
- id: hormone-signaling-mechanisms
  type: soft
builds-toward:
- metabolic-integration-hormonal-regulation
tags:
- receptor tyrosine kinase
- GPCR
- second messenger
- cAMP
- calcium
- MAP kinase
stage: advanced
status: draft
---

# Receptor Signaling Pathways (RTKs, GPCRs, and Second Messengers)

## Core Idea
Extracellular signaling molecules (growth factors, hormones, neurotransmitters) bind to cell surface receptors, initiating intracellular signaling cascades. Receptor tyrosine kinases (RTKs) dimerize upon ligand binding, autophosphorylate their cytoplasmic tails, and recruit adapter proteins (Grb2) to activate downstream kinases (Ras, MAPK/ERK cascade). GPCRs activate heterotrimeric G proteins (Gs, Gi/o, Gq/11, G12/13), which modulate second messengers (cAMP, IP3, DAG, Ca²⁺). These pathways regulate gene expression, enzyme activity, and cell behavior (proliferation, differentiation, apoptosis).

## Questions

```yaml
- question: "When a growth factor binds to a receptor tyrosine kinase (RTK), what is the immediate molecular consequence?"
  type: multiple-choice
  options: ["The receptor directly phosphorylates a transcription factor in the nucleus", "Two RTK monomers dimerize and phosphorylate each other on cytoplasmic tyrosine residues", "The receptor releases a second messenger (cAMP) into the cytoplasm", "A G protein exchanges GDP for GTP and dissociates from the receptor"]
  answer: 1
  explanation: "Ligand binding drives dimerization of two RTK monomers, and the paired kinase domains then cross-phosphorylate each other (autophosphorylation) on cytoplasmic tyrosine residues. These phosphotyrosines become docking sites for adapter proteins like Grb2. The G protein exchange mechanism (option D) belongs to GPCR signaling, not RTKs."

- question: "cAMP (cyclic AMP) is classified as a first messenger because it is the initial signal that activates an intracellular signaling pathway."
  type: true-false
  answer: false
  explanation: "cAMP is a second messenger. First messengers are extracellular signals — hormones, growth factors, or neurotransmitters — that cannot cross the plasma membrane. Second messengers like cAMP, IP3, DAG, and Ca²⁺ are intracellular molecules generated in response to receptor activation. They relay and amplify the signal inside the cell."

- question: "How does signal amplification occur in a GPCR-cAMP signaling cascade?"
  type: short-answer
  answer: "A single ligand-bound GPCR can activate many G protein molecules; each activated Gαs subunit activates one adenylyl cyclase; each adenylyl cyclase produces many cAMP molecules; each cAMP activates protein kinase A (PKA); each PKA phosphorylates many substrate proteins. Each step multiplies the signal, so one receptor-ligand binding event can alter thousands of downstream proteins."
  explanation: "This cascading amplification is a defining feature of signaling pathways. It explains why hormones present at nanomolar concentrations can produce strong cellular responses — the signal is amplified at every enzymatic step. It also means the pathway must be tightly regulated (phosphodiesterases degrade cAMP; GTPase activity of Gα turns off G proteins) to prevent runaway signaling."
```

## Explainer

Cell signaling solves a fundamental problem: how do large, charged, water-soluble molecules like hormones communicate instructions to the cell interior without physically entering the cell? The answer is a relay system. An extracellular signal (the first messenger) binds to a receptor on the cell surface, and the receptor translates that binding event into an intracellular signal (second messenger or protein phosphorylation) that spreads through the cytoplasm and nucleus.

Receptor tyrosine kinases (RTKs) are one major class of receptor. They span the plasma membrane and have a kinase domain on their cytoplasmic tail. When a ligand (like epidermal growth factor or insulin) binds, it forces two receptor monomers together into a dimer. The two kinase domains are now close enough to phosphorylate each other on tyrosine residues — a process called autophosphorylation. These phosphotyrosines act as molecular docking stations for adapter proteins like Grb2, which in turn recruit nucleotide exchange factors that activate Ras. Ras then triggers the MAPK/ERK kinase cascade, ultimately phosphorylating transcription factors and altering gene expression. The whole pathway is essentially a chain of "pass the phosphate" events.

GPCRs operate differently. They are seven-transmembrane proteins coupled to a heterotrimeric G protein (α, β, γ subunits) on the cytoplasmic face. When a ligand binds, the receptor changes shape and catalyzes exchange of GDP for GTP on the Gα subunit, causing Gα to dissociate and diffuse to its effector. Gαs activates adenylyl cyclase, which produces cAMP; Gαi inhibits it; Gαq activates phospholipase C, which generates IP3 and DAG. IP3 releases Ca²⁺ from the endoplasmic reticulum; DAG activates protein kinase C. Each of these second messengers is rapidly degraded (cAMP by phosphodiesterases; Gα self-inactivates by hydrolyzing GTP to GDP), so the signal is transient.

The key concept unifying both pathways is amplification. A single receptor-ligand binding event does not directly cause the cellular response — it sets off a chain reaction where each step generates more activated molecules than the last. One RTK phosphorylates many Ras; one active Ras activates many Raf; each Raf phosphorylates many MEK; each MEK phosphorylates many ERK. This enzymatic cascade means that picomolar concentrations of a hormone can produce a robust cellular response. The tradeoff is complexity: each step is a potential point of failure (cancer mutations often hit Ras or B-Raf) and requires tight regulation.
