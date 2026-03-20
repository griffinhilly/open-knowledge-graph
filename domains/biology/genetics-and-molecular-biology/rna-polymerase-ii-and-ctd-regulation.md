---
id: rna-polymerase-ii-and-ctd-regulation
title: RNA Polymerase II CTD and Coupling to mRNA Processing
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: transcription-initiation-eukaryotes
  type: hard
- id: gene-regulation-eukaryotes
  type: soft
builds-toward:
- rna-processing-5-cap-3-poly-a
- small-rnas-mirna-and-rnai
tags:
- ctd
- phosphorylation
- capping-complex
- splicing-factors
- elongation-control
stage: advanced
status: draft
---

# RNA Polymerase II CTD and Coupling to mRNA Processing

## Core Idea
RNA polymerase II's carboxy-terminal domain (CTD), containing multiple repeats (~26-52 copies) of a heptapeptide sequence (YSPTSPS), undergoes dynamic phosphorylation during transcription initiation and elongation at serines 2 and 5 and tyrosine 1. CTD phosphorylation patterns recruit distinct factors: Ser5 phosphorylation recruits 5' capping enzymes, while Ser2 phosphorylation recruits splicing factors and 3' end processing machinery. This coupling coordinates transcription with mRNA processing, linking initiation, elongation, and termination mechanistically. Transcription elongation is regulated by DSIF and NELF complexes, which pause RNA polymerase II until relieved by P-TEFb kinase (CDK9/Cyclin T), enabling rapid transcriptional responses to stress and developmental signals.

## Explainer

From your study of eukaryotic transcription initiation, you know that RNA polymerase II (Pol II) is recruited to promoters through general transcription factors assembling at the TATA box and surrounding elements. But Pol II does far more than synthesize RNA — it serves as a mobile coordination platform for the entire mRNA maturation pipeline. The key to this coordination is the **carboxy-terminal domain (CTD)**, a long, flexible tail extending from the largest subunit of Pol II. In humans, the CTD contains 52 tandem repeats of the heptapeptide sequence Tyr-Ser-Pro-Thr-Ser-Pro-Ser (YSPTSPS). Think of these repeats as a string of landing pads, each capable of being chemically modified to recruit different processing machinery at different stages of transcription.

The CTD operates through a **phosphorylation code**. When Pol II first assembles at the promoter as part of the preinitiation complex, the CTD is unphosphorylated — this hypophosphorylated form is what general transcription factors recognize. Once transcription begins, the kinase activity of TFIIH phosphorylates **Serine 5** (Ser5) of the heptapeptide repeats. This Ser5 phosphorylation acts as a molecular beacon that recruits the **capping enzyme complex**, which adds the 7-methylguanosine cap to the 5' end of the nascent transcript. As Pol II moves into productive elongation, Ser5 phosphorylation gradually decreases while **Serine 2** (Ser2) phosphorylation increases, catalyzed by the kinase P-TEFb (CDK9/Cyclin T). Ser2 phosphorylation recruits **splicing factors** and, later, **3' end processing machinery** including cleavage and polyadenylation factors. The result is an elegant temporal handoff: capping happens first (near the promoter), splicing occurs co-transcriptionally (during elongation), and polyadenylation occurs at the end.

Before Pol II can enter productive elongation, it must overcome a checkpoint known as **promoter-proximal pausing**. Shortly after initiation, the negative elongation factors **NELF** and **DSIF** bind to the polymerase and stall it approximately 30–60 nucleotides downstream of the transcription start site. The polymerase sits there, poised but frozen, until a signal releases it. That signal is P-TEFb, which phosphorylates both NELF (causing its release) and DSIF (converting it from a pausing factor to a positive elongation factor), as well as Ser2 of the CTD. This pause-and-release mechanism gives the cell a powerful regulatory switch: genes can be loaded with a paused polymerase, ready to fire instantly in response to stress, developmental cues, or signaling cascades — much faster than assembling the entire preinitiation complex from scratch.

The beauty of the CTD system is that it converts the linear act of transcription into a coordinated assembly line. Rather than requiring separate recruitment events for capping, splicing, and polyadenylation, the polymerase itself carries the instructions — written in phosphorylation marks — for which processing factors to recruit and when. This coupling explains why mRNA processing is so efficient in vivo compared to in vitro systems: the CTD ensures that each processing step happens at precisely the right moment as the polymerase traverses the gene.
