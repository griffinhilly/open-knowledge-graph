---
id: toll-like-receptors
title: Toll-Like Receptors and TLR Signaling
domain: biology
course: immunology
prerequisites:
- id: pattern-recognition-receptors
  type: hard
builds-toward:
- inflammatory-response-cellular
- cytokines-and-chemokines
tags:
- innate
- signaling
- pattern-recognition
stage: advanced
status: draft
---

# Toll-Like Receptors and TLR Signaling

## Core Idea
Toll-like receptors (TLRs) are the most well-characterized PRR family, with 10 functional human TLRs recognizing diverse PAMPs including lipopolysaccharides, peptidoglycans, and nucleic acids. TLRs signal through MyD88-dependent and TRIF-dependent pathways leading to activation of NF-κB and IRF transcription factors. This drives production of pro-inflammatory cytokines and type I interferons.

## Explainer

You already know that the innate immune system uses **pattern recognition receptors (PRRs)** to detect conserved molecular signatures on pathogens. Toll-like receptors are the best-understood family of PRRs and serve as the first line of molecular sensing — they are the alarm system that tells your innate immune cells "a pathogen is here, and here is roughly what kind." Understanding TLRs means understanding how the body converts pathogen detection into an inflammatory and antiviral response.

Humans have **10 functional TLRs** (TLR1 through TLR10), and their division by location is the first organizing principle. TLRs 1, 2, 4, 5, and 6 sit on the **cell surface** and detect components of microbial cell walls and flagella — structures that are exposed on the outside of bacteria and fungi. TLR4, for instance, recognizes **lipopolysaccharide (LPS)** from Gram-negative bacteria, which is why even tiny amounts of LPS trigger powerful inflammatory responses. TLRs 3, 7, 8, and 9 are found inside the cell, in **endosomal membranes**, where they detect nucleic acids — double-stranded RNA (TLR3), single-stranded RNA (TLR7/8), and unmethylated CpG DNA (TLR9). This intracellular location makes sense: viral nucleic acids are only exposed after a virus has been internalized and its coat stripped away in the endosome. The location of the receptor matches where you would expect to encounter the ligand.

When a TLR binds its ligand, it dimerizes and recruits adaptor proteins that initiate one of two major signaling cascades. The **MyD88-dependent pathway** is used by most TLRs and activates the transcription factor **NF-κB**, which drives expression of pro-inflammatory cytokines like TNF-α, IL-1, and IL-6 — the molecules that recruit neutrophils, activate macrophages, and produce fever. The **TRIF-dependent pathway** (used primarily by TLR3 and TLR4) activates **IRF3/IRF7** transcription factors, leading to production of **type I interferons** (IFN-α and IFN-β) — the antiviral cytokines that put neighboring cells into a defensive state. TLR4 is unique in that it activates both pathways, which partly explains why LPS is such a potent immune stimulus and why Gram-negative sepsis produces such dramatic systemic inflammation.

The clinical significance of TLRs extends in two directions. Deficiencies in TLR signaling (such as MyD88 mutations) leave patients vulnerable to pyogenic bacterial infections because they cannot mount an adequate inflammatory response. Conversely, excessive or inappropriate TLR activation contributes to sepsis, autoimmune diseases, and chronic inflammation. This dual role — essential for defense but dangerous in excess — is a recurring theme in innate immunity that you will encounter repeatedly as you study cytokines and the inflammatory response.
