---
id: transcription-elongation-and-termination
title: Transcription Elongation and Termination
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: transcription
  type: hard
builds-toward:
- rna-processing-5-cap-3-poly-a
- transcription-initiation-eukaryotes
tags:
- elongation
- rho-independent-termination
- rho-dependent-termination
- hairpin-structure
stage: formal-systems
status: draft
---

# Transcription Elongation and Termination

## Core Idea
After initiation, RNA polymerase synthesizes RNA in the 5' to 3' direction, moving processively along the template DNA strand while maintaining the transcription bubble. In prokaryotes, transcription terminates at specific sites marked by termination signals: rho-independent (intrinsic) termination involves a GC-rich palindromic sequence in the RNA transcript that forms a stable hairpin structure, destabilizing the RNA-DNA hybrid and causing release; rho-dependent termination requires the Rho protein, a helicase that translocates along nascent RNA and disrupts the polymerase when transcription pauses. In eukaryotes, termination involves cleavage of the transcript by CPSF complex in response to polyadenylation signals (typically AAUAAA), mechanistically distinct from prokaryotic termination and coupled to 3' end processing.

## Explainer

You already understand that transcription begins when RNA polymerase binds a promoter and opens the DNA double helix. But initiation is just the starting gun — the polymerase must then travel thousands of nucleotides along the template, synthesizing RNA continuously, and eventually stop at exactly the right place. **Elongation** and **termination** are the two phases that govern this journey and its endpoint.

During elongation, RNA polymerase moves along the template strand in the 3' to 5' direction, reading DNA and building the complementary RNA in the 5' to 3' direction. The enzyme maintains a small **transcription bubble** — roughly 12–14 base pairs of unwound DNA — and an RNA-DNA hybrid of about 8–9 base pairs within that bubble. As the polymerase advances, it unwinds DNA ahead of itself and re-anneals it behind, extruding the growing RNA transcript out through an exit channel. The process is highly processive: once elongation begins, the polymerase typically does not fall off until it encounters a termination signal. Think of it as a zipper slider that unzips DNA ahead and re-zips it behind, leaving a thread of RNA trailing out the side.

In prokaryotes, transcription terminates by two distinct mechanisms. **Rho-independent (intrinsic) termination** relies on a signal encoded in the DNA itself: a GC-rich palindromic sequence followed by a run of adenines on the template strand (uracils in the RNA). The palindrome causes the nascent RNA to fold into a stable **hairpin structure** — a stem-loop held together by strong G-C base pairs. This hairpin, forming right at the exit channel of the polymerase, acts like a physical roadblock that destabilizes the enzyme. At the same time, the polymerase is sitting on a stretch of rU-dA base pairs, which are the weakest in nucleic acid chemistry. The combination of the hairpin's mechanical tug and the fragile RNA-DNA hybrid is enough to peel the transcript away, releasing both the RNA and the polymerase from the DNA. **Rho-dependent termination** uses a different strategy: the Rho protein, a hexameric helicase, loads onto a specific unstructured region of the nascent RNA called the **rut site** (rho utilization site) and translocates along the transcript in the 5' to 3' direction, chasing the polymerase. When the polymerase pauses — often at a site lacking a strong hairpin — Rho catches up and uses its helicase activity to unwind the RNA-DNA hybrid, forcing the transcript to release.

Eukaryotic termination is mechanistically distinct and tightly coupled to RNA processing. Rather than relying on hairpins or helicase chase, eukaryotic cells use a **polyadenylation signal** — typically the sequence AAUAAA — as the termination cue. When RNA polymerase II transcribes past this signal, the CPSF (cleavage and polyadenylation specificity factor) complex recognizes it, cleaves the RNA downstream, and hands the cut end to poly(A) polymerase for tail addition. The polymerase itself continues transcribing briefly past the cleavage site, but without the stabilizing connection to the functional transcript, it is eventually dislodged — likely by a "torpedo" exonuclease that degrades the remaining RNA dangling from the polymerase and destabilizes the elongation complex. This coupling of termination to 3' processing ensures that every mature eukaryotic mRNA receives the poly(A) tail it needs for stability and export.
