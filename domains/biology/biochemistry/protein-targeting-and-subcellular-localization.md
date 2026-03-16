---
id: protein-targeting-and-subcellular-localization
title: Protein Targeting and Subcellular Localization
domain: biology
course: biochemistry
prerequisites:
- id: post-translational-modifications
  type: soft
- id: endoplasmic-reticulum-and-golgi
  type: soft
tags:
- protein targeting
- signal peptide
- ER translocation
- nuclear import
- mitochondrial targeting
stage: advanced
status: draft
---

# Protein Targeting and Subcellular Localization

## Core Idea
Proteins are targeted to their correct intracellular destinations (nucleus, mitochondria, peroxisomes, endoplasmic reticulum, extracellular space) through specific targeting sequences (signal peptides, nuclear localization signals, mitochondrial targeting sequences) recognized by transport machinery. The ER signal recognition particle (SRP) recognizes the N-terminal signal peptide and directs ribosome-nascent chain-mRNA to the translocon for co-translational translocation. Nuclear import requires nuclear pore complexes and the ran-GTP gradient. Mitochondrial proteins are typically synthesized in the cytosol and post-translationally imported via TOM and TIM complexes.

## Explainer

A eukaryotic cell is partitioned into membrane-bound compartments — the nucleus, ER, Golgi, mitochondria, lysosomes, peroxisomes — each with a distinct biochemical environment. But nearly all proteins are synthesized by ribosomes in the cytosol. This creates a logistical problem: how does each protein find its correct destination? The answer is that proteins carry built-in **address labels** — short amino acid sequences that are recognized by specific sorting machinery. From your knowledge of the ER and Golgi, you understand that proteins destined for secretion or membrane insertion must enter the endomembrane system; protein targeting explains the molecular mechanism that routes them there.

The best-understood targeting pathway is the **ER signal peptide** system. Proteins destined for the ER, Golgi, plasma membrane, lysosomes, or secretion all begin with a stretch of ~15–30 hydrophobic amino acids at their N-terminus. As this signal peptide emerges from the ribosome, the **signal recognition particle (SRP)** — a ribonucleoprotein complex — binds it and temporarily halts translation. The SRP then docks the entire ribosome-mRNA-nascent chain complex at the **SRP receptor** on the ER membrane. The growing polypeptide is threaded through a protein channel called the **translocon** (Sec61 complex) directly into the ER lumen as translation resumes. This is **co-translational translocation** — the protein enters the ER while it is still being made. Once inside, the signal peptide is cleaved off by signal peptidase. This pathway is the default route to the entire endomembrane system; from the ER, further sorting signals (like mannose-6-phosphate tags for lysosomes) direct proteins to their final destinations via vesicular transport.

Not all proteins use the ER pathway. **Nuclear proteins** carry a **nuclear localization signal (NLS)** — typically a short stretch of positively charged amino acids (lysines and arginines) — that is recognized by **importin** proteins. Importins ferry cargo through the **nuclear pore complex**, a massive channel spanning the nuclear envelope. Inside the nucleus, the small GTPase **Ran** (in its GTP-bound form) binds importin, releasing the cargo. The Ran-GTP gradient — high inside the nucleus, low in the cytoplasm — provides directionality to nuclear import and export, ensuring proteins flow the right way.

**Mitochondrial targeting** uses a different strategy altogether. Most mitochondrial proteins are encoded by nuclear genes and synthesized in the cytosol as precursors with an N-terminal **mitochondrial targeting sequence (MTS)** — an amphipathic helix with positively charged residues on one face. This sequence is recognized by the **TOM complex** (translocase of the outer membrane), which passes the unfolded protein through to the **TIM complexes** (translocase of the inner membrane) for insertion into the matrix or inner membrane. Unlike ER translocation, this is **post-translational** — the protein is fully made before import begins, and must be kept unfolded by cytosolic chaperones (like Hsp70) to thread through the narrow import channels. The MTS is cleaved after import by mitochondrial processing peptidase.

The overarching principle is that every protein's destination is encoded in its own sequence. The cell reads these molecular zip codes through specific receptors and channels, routing thousands of different proteins to the correct compartment with remarkable fidelity. When targeting goes wrong — as in certain genetic diseases where enzymes lack proper sorting signals — proteins accumulate in the wrong compartment, and the consequences can be severe, as seen in I-cell disease where lysosomal enzymes are secreted instead of delivered to lysosomes.
