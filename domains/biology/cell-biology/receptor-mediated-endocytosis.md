---
id: receptor-mediated-endocytosis
title: Receptor-Mediated Endocytosis and Clathrin-Coated Vesicles
domain: biology
course: cell-biology
prerequisites:
- id: endomembrane-system-integration
  type: soft
- id: cell-signaling-intro
  type: soft
builds-toward:
- protein-trafficking-secretion
tags:
- endocytosis
- clathrin
- cargo-internalization
- receptor-internalization
stage: formal-systems
status: draft
---

# Receptor-Mediated Endocytosis and Clathrin-Coated Vesicles

## Core Idea
Receptor-mediated endocytosis selectively internalizes ligand-bound receptors by recruiting adaptor proteins (AP2) that stabilize clathrin, a trimeric protein that polymerizes into a polyhedral lattice. This lattice deforms the membrane into a vesicle; dynamin proteins pinch off the vesicle. Clathrin rapidly uncoats (removed by auxilin and Hsp70), and the uncoated vesicle fuses with early endosomes, where cargo is sorted: receptors are recycled or degraded, and internalized ligands are processed or degraded.

## Questions

```yaml
- question: "A cell's LDL receptors are internalized via receptor-mediated endocytosis. In the endosome, most receptors dissociate from LDL (due to acidic pH) and are recycled back to the plasma membrane. What is the functional consequence of this recycling?"
  type: multiple-choice
  options:
    - "Cholesterol uptake is permanently terminated because LDL is now trapped inside the cell"
    - "The cell loses sensitivity to future LDL signals because receptors accumulate in endosomes"
    - "The cell maintains its capacity to bind and internalize LDL in subsequent rounds of endocytosis"
    - "Clathrin accumulates inside the cell over time because it cannot re-associate with the membrane"
  answer: 2
  explanation: "Receptor recycling returns functional receptors to the cell surface, replenishing the supply available for future ligand capture. This is how the cell maintains sustained uptake capacity — each receptor can make multiple rounds of endocytosis. The alternative fate (degradation in lysosomes) would permanently reduce receptor number and dampen the cell's responsiveness. The LDL receptor undergoes hundreds of cycles over its lifetime. Option D is wrong because clathrin is actively uncoated by Hsp70/auxilin immediately after vesicle formation and the free triskelions return to the cytoplasmic pool for reuse."

- question: "Which component is directly responsible for physically deforming the plasma membrane into a curved pit during receptor-mediated endocytosis?"
  type: multiple-choice
  options:
    - "Dynamin, which wraps around the membrane and forces it to curve inward"
    - "AP2 adaptor proteins, which bridge receptor tails to the membrane and pull it inward"
    - "Clathrin triskelions, which polymerize into a lattice on the cytoplasmic face and impose curvature on the membrane"
    - "Hsp70 chaperones, which unfold membrane proteins to create flexibility for bending"
  answer: 2
  explanation: "Clathrin's triskelion structure spontaneously assembles into a polyhedral cage-like lattice. As clathrin polymerizes on the inner leaflet of the plasma membrane, the geometric constraints of the lattice force the membrane to curve inward, forming the clathrin-coated pit. Dynamin (option A) acts later — it wraps around the *neck* of the nearly complete pit and uses GTP hydrolysis to pinch off the vesicle. AP2 (option B) links receptors to clathrin but does not itself deform the membrane. The curvature is a direct mechanical consequence of clathrin lattice geometry."

- question: "Receptor-mediated endocytosis internalizes a sample of extracellular fluid and its contents whenever membrane invagination occurs, similar to macropinocytosis."
  type: true-false
  answer: false
  explanation: "Receptor-mediated endocytosis is inherently selective: it specifically captures molecules that are bound to cell-surface receptors. The ligand must first bind its cognate receptor; this binding event recruits AP2 and triggers clathrin assembly only at that site. Molecules in the extracellular fluid that lack a receptor partner are not efficiently captured. This selectivity is what distinguishes receptor-mediated endocytosis from macropinocytosis (bulk fluid uptake) and constitutive endocytosis, and it is why the cell can concentrate specific cargo hundreds of times relative to the extracellular fluid."

- question: "The mildly acidic pH (around 6.0) inside early endosomes serves a functional purpose in receptor-mediated endocytosis by promoting ligand-receptor dissociation, which enables receptor recycling."
  type: true-false
  answer: true
  explanation: "Many receptor-ligand complexes have pH-sensitive binding affinities — they bind tightly at neutral extracellular pH (~7.4) but release at the mildly acidic endosomal pH (~6.0). This acid-triggered dissociation is not incidental; it is essential for sorting. Once the ligand is released in the endosome, the free receptor can be packaged into recycling vesicles and returned to the cell surface, while the ligand (e.g., LDL) is routed to late endosomes and lysosomes for processing. The pH gradient thus directly enables the cell to decouple receptor fate from cargo fate."

- question: "After a signaling receptor like EGFR is internalized by receptor-mediated endocytosis, what determines whether the receptor is recycled or degraded, and why does this choice matter for cell signaling?"
  type: short-answer
  answer: "The sorting decision occurs at the early endosome and is governed by ubiquitination of the receptor's cytoplasmic tail. Heavily ubiquitinated receptors are recognized by the ESCRT machinery, sorted into multivesicular bodies, and ultimately delivered to lysosomes for degradation — permanently reducing receptor number and dampening future signaling. Minimally ubiquitinated or unmodified receptors are packaged into recycling tubules and returned to the plasma membrane. The functional consequence is profound: recycling maintains or restores the cell's sensitivity to the ligand, while degradation constitutes signal termination and downregulation of the pathway. Cells use this sorting decision to tune how long and how strongly they respond to growth factors and other extracellular signals."
  explanation: "This receptor-fate decision is a major mechanism of signal regulation. Overactivated growth factor signaling (e.g., in cancer) is often linked to mutations that impair receptor ubiquitination and degradation, causing continuous recycling and sustained signaling. Viruses exploit the same pathway in reverse — hijacking endocytosis for cell entry but then escaping lysosomal degradation by fusing with the endosomal membrane."
```

## Explainer

From your study of the endomembrane system, you know that cells shuttle material between compartments using membrane-bound vesicles. **Receptor-mediated endocytosis** is the cell's precision import system — rather than indiscriminately engulfing whatever is outside, the cell uses surface receptors to select specific molecules for internalization. The classic example is the **LDL receptor**, which binds cholesterol-carrying LDL particles from the blood and pulls them into the cell. This selectivity is what distinguishes receptor-mediated endocytosis from simple phagocytosis or pinocytosis: only molecules recognized by receptors are efficiently captured.

The mechanical process works like a self-assembling cage. When a ligand binds its receptor, the receptor's cytoplasmic tail recruits **adaptor protein complexes (AP2)**, which serve as a bridge between the receptor and **clathrin** — a three-legged protein (called a triskelion) that spontaneously polymerizes into a lattice resembling a soccer ball. As clathrin molecules assemble on the membrane's inner surface, they force the membrane to curve inward, forming a **clathrin-coated pit**. The pit deepens until it becomes a sphere connected to the cell surface by only a thin neck. At this point, **dynamin**, a GTPase, wraps around the neck like a molecular garotte and uses GTP hydrolysis to pinch the vesicle free from the membrane. The entire process — from ligand binding to vesicle release — takes about one to two minutes.

Once inside, the clathrin coat is rapidly removed by the chaperone **Hsp70** (recruited by auxilin), because clathrin's job is done and the coat would prevent the vesicle from fusing with its target compartment. The uncoated vesicle delivers its contents to an **early endosome**, where the slightly acidic pH (around 6.0) causes many ligands to release from their receptors. This is where sorting happens: the cell can **recycle** the receptor back to the surface for another round of uptake, send the receptor to **late endosomes and lysosomes** for degradation (downregulating the signal), or route the ligand to different compartments for processing. The fate of the receptor determines the cell's sensitivity to future signals — recycling maintains responsiveness, while degradation dampens it.

This pathway is not just a nutrient import system; it is deeply intertwined with **cell signaling**. Many signaling receptors — including growth factor receptors like EGFR — are internalized by clathrin-mediated endocytosis after ligand binding. Internalization can either terminate the signal (by delivering the receptor to lysosomes for destruction) or sustain it (signaling continues from endosomes). Viruses and toxins have also evolved to hijack this pathway: influenza virus binds cell-surface receptors and rides the endocytic machinery into the cell, using the acidic endosomal environment to trigger membrane fusion and release its genome. Understanding receptor-mediated endocytosis is therefore essential for understanding both normal physiology and disease mechanisms.
