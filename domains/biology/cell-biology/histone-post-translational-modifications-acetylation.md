---
id: histone-post-translational-modifications-acetylation
title: 'Histone Post-Translational Modifications: Acetylation'
domain: biology
course: cell-biology
prerequisites:
- id: histone-modifications-epigenetic
  type: hard
- id: post-translational-modifications
  type: hard
builds-toward:
- mrna-5-capping-and-3-polyadenylation
tags:
- histone-acetylation
- epigenetics
- transcription
stage: advanced
status: draft
---

# Histone Post-Translational Modifications: Acetylation

## Core Idea
Histone acetylation, catalyzed by histone acetyltransferases (HATs) and reversed by histone deacetylases (HDACs), neutralizes positive charges on histone tails, weakening electrostatic histone-DNA interactions and opening chromatin for transcription. Acetylation marks (H3K9ac, H4K16ac) are broadly associated with active transcription and are often deposited co-transcriptionally by elongation-associated HATs. The reversibility and rapid kinetics of acetylation (occurring within minutes) make it a dynamic switch for rapid gene activation in response to cellular signals, contrasting with slower, more permanent DNA methylation changes.

## How It's Best Learned
Measure histone acetylation dynamics using real-time fluorescence microscopy of acetyl-histone marks; identify HAT and HDAC substrates biochemically. Assess effects of HDAC inhibitors (valproate, trichostatin A) on acetylation patterns and gene expression.

## Common Misconceptions
- Acetylation directly opens chromatin; it weakens histone-DNA contacts, but chromatin remodeling complexes are often required for full opening. - All histone acetylation is activating; some marks are contextual and can associate with repression.

## Explainer

You already know that histone tails carry a variety of chemical modifications — methylation, phosphorylation, ubiquitination — and that these marks collectively influence whether chromatin is open or closed. Acetylation is one of the fastest-acting and most well-understood of these modifications, and understanding its mechanism comes down to a single electrostatic principle.

Histone tails are rich in lysine residues, which carry a positive charge at physiological pH. DNA, meanwhile, is a polyanion — its phosphate backbone is strongly negative. This charge complementarity is what holds DNA tightly wound around the histone octamer. **Histone acetyltransferases (HATs)** transfer an acetyl group from acetyl-CoA onto the amino group of lysine, neutralizing the positive charge. With that electrostatic grip weakened, the DNA loosens from the histone surface, making the underlying sequence more accessible to transcription factors, RNA polymerase, and chromatin remodeling complexes. The reverse reaction is catalyzed by **histone deacetylases (HDACs)**, which remove the acetyl group and restore the positive charge, re-tightening the chromatin.

The most commonly studied acetylation marks — **H3K9ac** (acetylation of lysine 9 on histone H3) and **H4K16ac** — are strongly associated with active transcription. When RNA polymerase elongates through a gene, elongation-associated HATs travel with it, depositing acetylation marks co-transcriptionally. This creates a self-reinforcing loop: transcription brings HATs, which open chromatin further, which facilitates more transcription. But this is not a one-way ratchet. HDACs are constantly working to remove acetyl marks, meaning that a gene must be continuously signaled to stay active. When the signal stops, HDACs quickly deacetylate the histones, and the gene returns to a more closed state.

This rapid reversibility — acetylation and deacetylation occurring on the scale of minutes — distinguishes histone acetylation from modifications like DNA methylation, which can persist through cell divisions. Think of acetylation as a light switch: quick on, quick off, responding to immediate cellular signals like growth factors or stress. DNA methylation, by contrast, is more like rewiring the circuit. This dynamic quality is why HDAC inhibitors (drugs like trichostatin A and valproate) have such dramatic effects on gene expression — they block the "off" switch, causing widespread and persistent gene activation that can be therapeutically useful in cancer treatment.
