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

## Questions

```yaml
- question: "A researcher treats T cells with a blocking antibody against LFA-1 (a T cell adhesion molecule) before mixing them with antigen-presenting cells. Based on your understanding of synapse formation, what would you expect?"
  type: multiple-choice
  options:
    - "T cells would activate normally because LFA-1 is only involved in T cell migration, not activation"
    - "T cells would fail to form stable contact with APCs, preventing the sustained interaction needed for synapse assembly and robust activation"
    - "T cells would form synapses normally but with a disorganized cSMAC lacking CD28 costimulatory signals"
    - "T cell activation would be enhanced because LFA-1 normally competes with TCR for signaling space"
  answer: 1
  explanation: "LFA-1/ICAM-1 adhesion is the first step in stabilizing T cell-APC contact. When a T cell encounters an APC, initial TCR-peptide-MHC interactions are individually weak and transient. LFA-1 binding to ICAM-1 slows the interaction, giving TCRs time to scan the APC surface and accumulate enough engagements to trigger synapse organization. Without LFA-1, contact is too brief and unstable to allow the cytoskeletal reorganization and SMAC formation needed for robust signaling. Blocking LFA-1 is therefore an effective way to suppress T cell responses, and this principle is exploited therapeutically (e.g., efalizumab targets LFA-1 in autoimmune disease)."

- question: "Large phosphatases like CD45 are actively excluded from the cSMAC during immunological synapse formation. Why is this spatial exclusion important for T cell activation?"
  type: multiple-choice
  options:
    - "CD45 would compete with TCR for peptide-MHC binding if it were in the cSMAC"
    - "Excluding CD45 from the center allows sustained phosphorylation of TCR signaling molecules without immediate dephosphorylation, amplifying the weak activation signal"
    - "CD45 is needed at the periphery to recruit adhesion molecules that maintain synapse stability"
    - "CD45 exclusion prevents premature apoptosis of the T cell during prolonged APC contact"
  answer: 1
  explanation: "The cSMAC concentrates TCR complexes, kinases (like Lck and ZAP-70), and costimulatory molecules that drive phosphorylation-dependent signaling. CD45 is a phosphatase that would immediately reverse these phosphorylation events. By excluding CD45 to the distal SMAC (dSMAC), the synapse creates a protected signaling compartment where phosphorylated signaling intermediates can accumulate and persist. This spatial segregation — kinases at center, phosphatases at periphery — is the molecular mechanism by which many individually weak TCR-peptide-MHC interactions (each contributing small, brief phosphorylation events) are integrated into a sustained, threshold-crossing activation signal."

- question: "The immunological synapse allows a T cell to commit to activation based on many individually weak TCR-peptide-MHC interactions, rather than requiring a single high-affinity binding event."
  type: true-false
  answer: true
  explanation: "This integration function is the central purpose of the synapse. A T cell may have only 30,000 TCRs, and each TCR-peptide-MHC interaction has relatively low affinity (lasting seconds to minutes). Without some mechanism for integrating these signals, the T cell could not achieve the sustained signaling threshold needed for activation. The synapse solves this by concentrating TCR complexes in the cSMAC, excluding phosphatases that would quench signals, and persisting for hours — enabling the accumulation of weak signals into a decisive activation response. This is why disrupting synapse architecture (not just TCR binding) impairs T cell activation."

- question: "The cSMAC is the primary site of sustained TCR signaling throughout the duration of the immunological synapse."
  type: true-false
  answer: false
  explanation: "This is a common misconception. TCR microclusters form at the periphery (dSMAC) and are the primary sites of active signaling as they stream centripetally toward the cSMAC. By the time TCR complexes reach the cSMAC, signaling is partially winding down — the cSMAC functions significantly as a site of signal termination and TCR internalization (downregulation), not purely signal amplification. The pSMAC (adhesion ring) seals the interface, and the dSMAC is where new TCR activation events initiate. The synapse is a dynamic signaling conveyor belt, not a static amplifier."

- question: "How does the spatial organization of the immunological synapse — with signaling molecules concentrated in the center and phosphatases excluded to the periphery — solve the problem of individually weak TCR-peptide-MHC interactions?"
  type: short-answer
  answer: "Individual TCR-peptide-MHC interactions are short-lived and each produces only a brief, small phosphorylation event — insufficient alone to trigger activation. The synapse solves this by concentrating many TCR complexes in the cSMAC while actively excluding the phosphatase CD45 from this region. In this protected compartment, each weak phosphorylation event persists longer before being reversed, and many such events accumulate simultaneously. Over the hours that the synapse persists, thousands of individually insufficient signals are integrated into the sustained, high-level signaling cascade required for T cell commitment to activation."
  explanation: "This question targets the functional logic of synapse architecture — why the bull's-eye organization is not arbitrary but mechanistically explains how T cells solve a real biophysical problem. Students who understand this can connect synapse structure to activation thresholds, to why disrupting adhesion molecules suppresses immunity, and to why some immunosuppressive drugs target synapse assembly rather than TCR binding directly."
```

## Explainer

From your study of TCR structure and T cell activation, you know that a T cell recognizes antigen only when peptide is presented on MHC by an antigen-presenting cell (APC), and that costimulatory signals through receptors like CD28 are required for full activation. But how does a T cell — which may have only 30,000 TCRs on its surface, each with relatively low affinity for its peptide-MHC ligand — generate a signal strong enough to commit to activation? The answer lies in the spatial organization of the contact interface between T cell and APC, a structure called the **immunological synapse**.

When a T cell encounters an APC displaying its cognate peptide-MHC, initial contact is mediated by **adhesion molecules** — particularly **LFA-1** on the T cell binding **ICAM-1** on the APC. These interactions stabilize the cell-cell contact and buy time for TCRs to scan the APC surface. If enough TCRs engage peptide-MHC, the T cell undergoes dramatic cytoskeletal reorganization: the **microtubule-organizing center (MTOC)** reorients toward the APC, and the actin cytoskeleton drives the formation of a flattened contact zone. Within minutes, this interface self-organizes into a characteristic bull's-eye pattern of concentric rings called **supramolecular activation clusters (SMACs)**.

The mature synapse has a defined architecture. The **central SMAC (cSMAC)** contains concentrated TCR-peptide-MHC complexes along with the costimulatory receptor CD28 and signaling molecules like PKC-θ. Surrounding this is the **peripheral SMAC (pSMAC)**, a ring of LFA-1/ICAM-1 adhesion pairs that functions like a gasket, sealing the interface and creating a confined signaling compartment. Beyond this lies the **distal SMAC (dSMAC)**, enriched in large phosphatases like CD45 that are actively excluded from the cSMAC — their removal from the center allows sustained phosphorylation of signaling molecules without immediate dephosphorylation. This spatial segregation of kinases (center) from phosphatases (periphery) is a key mechanism by which the synapse amplifies and sustains weak TCR signals.

The immunological synapse is not merely a static structure — it is a dynamic signaling platform. TCR microclusters form at the periphery and stream centripetally toward the cSMAC, actively signaling along the way. The cSMAC itself may function partly as a site of signal termination and receptor internalization, creating a balance between new signal generation and signal extinction. The synapse persists for the duration of T cell activation — typically 6 to 30 hours for naive T cells — and its stability correlates with the strength of activation. This prolonged, organized contact explains how a T cell integrates many individually weak TCR-peptide-MHC interactions into a decisive activation signal, and why disrupting synapse formation (through blocking LFA-1, for instance) can suppress T cell responses.
