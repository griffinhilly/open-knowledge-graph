---
id: immunological-synapse-formation
title: Immunological Synapse and T Cell-APC Interaction
domain: biology
course: immunology
prerequisites:
- id: t-cell-receptor-structure-and-function
  type: hard
- id: t-cell-activation-costimulation
  type: hard
- id: cell-signaling-intro
  type: soft
builds-toward:
- t-cell-activation-costimulation
- th1-th2-th17-responses
tags:
- immunological-synapse
- T-APC-interaction
- TCR-clustering
- cytoskeletal-reorganization
stage: advanced
status: draft
---

# Immunological Synapse and T Cell-APC Interaction

## Core Idea
The immunological synapse is an organized interface between a T cell and antigen-presenting cell where TCR and costimulatory signals converge. The synapse exhibits a central supramolecular activation cluster (cSMAC) with TCR and CD28, surrounded by peripheral regions with adhesion molecules and phosphatase. This spatial organization ensures robust, sustained T cell activation and prevents premature termination of the signal.

## How It's Best Learned
Use two-photon microscopy and superresolution imaging findings to understand real-time synapse dynamics. Consider how different TCR affinities affect synapse stability.

## Common Misconceptions
Synapses form and persist for minutes to hours, not seconds. A single synapse is sufficient to activate a T cell; sustained TCR signaling does not require multiple synapses.

## Explainer

From your study of TCR structure and T cell activation, you know that a T cell recognizes antigen only when peptide is presented on MHC by an antigen-presenting cell (APC), and that costimulatory signals through receptors like CD28 are required for full activation. But how does a T cell — which may have only 30,000 TCRs on its surface, each with relatively low affinity for its peptide-MHC ligand — generate a signal strong enough to commit to activation? The answer lies in the spatial organization of the contact interface between T cell and APC, a structure called the **immunological synapse**.

When a T cell encounters an APC displaying its cognate peptide-MHC, initial contact is mediated by **adhesion molecules** — particularly **LFA-1** on the T cell binding **ICAM-1** on the APC. These interactions stabilize the cell-cell contact and buy time for TCRs to scan the APC surface. If enough TCRs engage peptide-MHC, the T cell undergoes dramatic cytoskeletal reorganization: the **microtubule-organizing center (MTOC)** reorients toward the APC, and the actin cytoskeleton drives the formation of a flattened contact zone. Within minutes, this interface self-organizes into a characteristic bull's-eye pattern of concentric rings called **supramolecular activation clusters (SMACs)**.

The mature synapse has a defined architecture. The **central SMAC (cSMAC)** contains concentrated TCR-peptide-MHC complexes along with the costimulatory receptor CD28 and signaling molecules like PKC-θ. Surrounding this is the **peripheral SMAC (pSMAC)**, a ring of LFA-1/ICAM-1 adhesion pairs that functions like a gasket, sealing the interface and creating a confined signaling compartment. Beyond this lies the **distal SMAC (dSMAC)**, enriched in large phosphatases like CD45 that are actively excluded from the cSMAC — their removal from the center allows sustained phosphorylation of signaling molecules without immediate dephosphorylation. This spatial segregation of kinases (center) from phosphatases (periphery) is a key mechanism by which the synapse amplifies and sustains weak TCR signals.

The immunological synapse is not merely a static structure — it is a dynamic signaling platform. TCR microclusters form at the periphery and stream centripetally toward the cSMAC, actively signaling along the way. The cSMAC itself may function partly as a site of signal termination and receptor internalization, creating a balance between new signal generation and signal extinction. The synapse persists for the duration of T cell activation — typically 6 to 30 hours for naive T cells — and its stability correlates with the strength of activation. This prolonged, organized contact explains how a T cell integrates many individually weak TCR-peptide-MHC interactions into a decisive activation signal, and why disrupting synapse formation (through blocking LFA-1, for instance) can suppress T cell responses.
