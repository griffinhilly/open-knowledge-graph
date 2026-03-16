---
id: pattern-recognition-receptors
title: Pattern Recognition Receptors (PRRs)
domain: biology
course: immunology
prerequisites:
- id: innate-immunity-overview
  type: hard
- id: cell-signaling-intro
  type: hard
builds-toward:
- toll-like-receptors
- complement-system-overview
tags:
- innate
- signaling
- pattern-recognition
stage: advanced
status: draft
---

# Pattern Recognition Receptors (PRRs)

## Core Idea
Pattern recognition receptors are germline-encoded sensors that detect pathogen-associated molecular patterns (PAMPs) and damage-associated molecular patterns (DAMPs). PRR families include toll-like receptors, NOD-like receptors, and lectin receptors on both cell surfaces and intracellular compartments. PRR engagement initiates signaling cascades that produce inflammatory mediators and type I interferons.

## How It's Best Learned
Study specific PRRs and their ligands (TLR4 for LPS, TLR3 for dsRNA, dectin-1 for β-glucans) before generalizing to the broader PRR family concept.

## Common Misconceptions
Not all PRRs are on the cell surface; many function intracellularly. PAMPs are not inherently dangerous—they are simply evolutionary-conserved structures that distinguish pathogens from host.

## Explainer

From your study of innate immunity, you know that the innate immune system provides rapid, nonspecific defense against pathogens without requiring prior exposure. From cell signaling, you understand that receptors on cell surfaces detect extracellular signals and activate intracellular cascades. **Pattern recognition receptors (PRRs)** sit at the intersection of these two concepts: they are the molecular sensors that allow innate immune cells to detect infection and tissue damage, translating microbial recognition into inflammatory and antimicrobial responses within minutes.

The fundamental insight behind PRRs is that pathogens share conserved molecular structures that are absent from host cells. These structures are called **pathogen-associated molecular patterns (PAMPs)** — examples include lipopolysaccharide (LPS) on Gram-negative bacteria, peptidoglycan on Gram-positive bacteria, double-stranded RNA produced during viral replication, and β-glucans in fungal cell walls. These molecules are ideal targets for innate recognition because they are essential for microbial survival (so pathogens cannot easily mutate them away), they are shared across broad classes of microbes (so a small number of receptors covers many pathogens), and they are structurally distinct from anything the host produces. PRRs also detect **damage-associated molecular patterns (DAMPs)** — molecules released from dying or stressed host cells, such as ATP, uric acid, and HMGB1 — enabling the immune system to respond to tissue injury even in the absence of infection.

PRRs are classified into several families based on their structure, location, and the types of patterns they recognize. **Toll-like receptors (TLRs)** are the best-characterized family, with 10 members in humans. Surface TLRs (TLR1, 2, 4, 5, 6) detect microbial membrane components — TLR4 recognizes LPS, TLR2 recognizes lipoproteins and peptidoglycan, TLR5 recognizes flagellin. Endosomal TLRs (TLR3, 7, 8, 9) detect nucleic acids that become accessible only after a pathogen has been engulfed and degraded in endosomes — TLR3 senses double-stranded RNA, TLR7/8 sense single-stranded RNA, and TLR9 senses unmethylated CpG DNA. **NOD-like receptors (NLRs)** are cytoplasmic sensors that detect intracellular bacterial components; some NLRs assemble into multi-protein complexes called **inflammasomes** that activate caspase-1 and drive production of the inflammatory cytokines IL-1β and IL-18. **RIG-I-like receptors (RLRs)** are cytoplasmic sensors of viral RNA that induce type I interferon production, establishing an antiviral state. **C-type lectin receptors (CLRs)** like Dectin-1 recognize carbohydrate structures, particularly fungal β-glucans.

When a PRR binds its ligand, it activates intracellular signaling cascades — most commonly through adaptor proteins like **MyD88** and **TRIF** — that converge on transcription factors including **NF-κB**, **IRF3**, and **AP-1**. NF-κB drives expression of pro-inflammatory cytokines (TNF-α, IL-1, IL-6) and chemokines that recruit neutrophils and other immune cells to the site of infection. IRF3 drives production of **type I interferons** (IFN-α/β), which establish an antiviral state in neighboring cells and activate natural killer cells. The specificity of the response — whether predominantly inflammatory or antiviral — depends on which PRRs are engaged and which signaling pathways they activate. This is why the innate immune system, despite having far fewer receptors than the adaptive system, can mount qualitatively different responses to bacteria, viruses, and fungi: different pathogens trigger different combinations of PRRs, producing distinct cytokine profiles that shape both the immediate innate response and the subsequent adaptive immune response.
