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
stage: advanced
status: draft
---

# Receptor-Mediated Endocytosis and Clathrin-Coated Vesicles

## Core Idea
Receptor-mediated endocytosis selectively internalizes ligand-bound receptors by recruiting adaptor proteins (AP2) that stabilize clathrin, a trimeric protein that polymerizes into a polyhedral lattice. This lattice deforms the membrane into a vesicle; dynamin proteins pinch off the vesicle. Clathrin rapidly uncoats (removed by auxilin and Hsp70), and the uncoated vesicle fuses with early endosomes, where cargo is sorted: receptors are recycled or degraded, and internalized ligands are processed or degraded.

## Explainer

From your study of the endomembrane system, you know that cells shuttle material between compartments using membrane-bound vesicles. **Receptor-mediated endocytosis** is the cell's precision import system — rather than indiscriminately engulfing whatever is outside, the cell uses surface receptors to select specific molecules for internalization. The classic example is the **LDL receptor**, which binds cholesterol-carrying LDL particles from the blood and pulls them into the cell. This selectivity is what distinguishes receptor-mediated endocytosis from simple phagocytosis or pinocytosis: only molecules recognized by receptors are efficiently captured.

The mechanical process works like a self-assembling cage. When a ligand binds its receptor, the receptor's cytoplasmic tail recruits **adaptor protein complexes (AP2)**, which serve as a bridge between the receptor and **clathrin** — a three-legged protein (called a triskelion) that spontaneously polymerizes into a lattice resembling a soccer ball. As clathrin molecules assemble on the membrane's inner surface, they force the membrane to curve inward, forming a **clathrin-coated pit**. The pit deepens until it becomes a sphere connected to the cell surface by only a thin neck. At this point, **dynamin**, a GTPase, wraps around the neck like a molecular garotte and uses GTP hydrolysis to pinch the vesicle free from the membrane. The entire process — from ligand binding to vesicle release — takes about one to two minutes.

Once inside, the clathrin coat is rapidly removed by the chaperone **Hsp70** (recruited by auxilin), because clathrin's job is done and the coat would prevent the vesicle from fusing with its target compartment. The uncoated vesicle delivers its contents to an **early endosome**, where the slightly acidic pH (around 6.0) causes many ligands to release from their receptors. This is where sorting happens: the cell can **recycle** the receptor back to the surface for another round of uptake, send the receptor to **late endosomes and lysosomes** for degradation (downregulating the signal), or route the ligand to different compartments for processing. The fate of the receptor determines the cell's sensitivity to future signals — recycling maintains responsiveness, while degradation dampens it.

This pathway is not just a nutrient import system; it is deeply intertwined with **cell signaling**. Many signaling receptors — including growth factor receptors like EGFR — are internalized by clathrin-mediated endocytosis after ligand binding. Internalization can either terminate the signal (by delivering the receptor to lysosomes for destruction) or sustain it (signaling continues from endosomes). Viruses and toxins have also evolved to hijack this pathway: influenza virus binds cell-surface receptors and rides the endocytic machinery into the cell, using the acidic endosomal environment to trigger membrane fusion and release its genome. Understanding receptor-mediated endocytosis is therefore essential for understanding both normal physiology and disease mechanisms.
