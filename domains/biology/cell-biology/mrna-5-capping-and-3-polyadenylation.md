---
id: mrna-5-capping-and-3-polyadenylation
title: mRNA 5' Capping and 3' Polyadenylation
domain: biology
course: cell-biology
prerequisites:
- id: rna-types-and-structure
  type: hard
- id: transcription
  type: hard
builds-toward:
- spliceosome-and-splicing-regulation
tags:
- mRNA-processing
- capping
- polyadenylation
stage: formal-systems
status: draft
---

# mRNA 5' Capping and 3' Polyadenylation

## Core Idea
mRNA 5' capping involves addition of a 7-methylguanosine cap via an unusual 5'-5' triphosphate linkage within the first 20-50 nucleotides of transcription, protecting mRNA from 5' exonucleases and facilitating ribosome binding. 3' polyadenylation, catalyzed by cleavage and polyadenylation specificity factor (CPSF), involves endonucleolytic cleavage 10-30 nucleotides downstream of the AAUAAA signal and addition of ~200 adenine residues by poly(A) polymerase. Both modifications occur co-transcriptionally and are essential for mRNA stability, nuclear export, and efficient translation.

## How It's Best Learned
Measure cap and poly(A) tail synthesis rates in isolated transcription systems; assess their effects on mRNA stability using pulse-chase labeling. Use cap- and poly(A)-binding proteins to map modification sites.

## Common Misconceptions
- 5' cap and 3' poly(A) tail are added post-transcriptionally; they're added during transcription. - Capping requires the 5' triphosphate of the nascent RNA; the first nucleotide becomes the cap's second position.

## Questions

```yaml
- question: "A researcher introduces a point mutation that destroys the AAUAAA polyadenylation signal of a gene. Transcription of the gene proceeds normally. What is the most likely consequence for the mRNA?"
  type: multiple-choice
  options:
    - "The mRNA is produced normally but cannot be translated because ribosomes require the poly(A) signal for initiation"
    - "CPSF fails to recognize the 3' end, the transcript is not cleaved or polyadenylated, and the unprotected mRNA is rapidly degraded by 3' exonucleases"
    - "The mRNA accumulates in the nucleus because the poly(A) signal is required for nuclear export of the transcript"
    - "The mRNA is correctly processed but has a longer-than-normal poly(A) tail because the lack of a signal prevents tail shortening"
  answer: 1
  explanation: "The AAUAAA signal is the recognition sequence for CPSF (cleavage and polyadenylation specificity factor). Without it, CPSF cannot bind, the pre-mRNA is not cleaved downstream of the signal, and poly(A) polymerase has no new 3' end to extend. The unprotected 3' end is rapidly attacked by 3' exonucleases, degrading the transcript even though transcription was normal. This explains why polyadenylation is essential for mRNA stability, not just a decorative modification."

- question: "What property of the 7-methylguanosine (m7G) cap makes it effective at protecting mRNA from 5' exonuclease degradation?"
  type: multiple-choice
  options:
    - "The methyl group makes the cap too large for the exonuclease active site to accommodate"
    - "The 5'-to-5' triphosphate linkage creates a chemical structure that 5' exonucleases are not designed to recognize or cleave"
    - "The cap recruits decapping enzymes that compete with exonucleases for the 5' end"
    - "The cap causes the 5' end of the mRNA to fold back on itself, physically blocking exonuclease access"
  answer: 1
  explanation: "All other nucleotide bonds in RNA are 3'-to-5' phosphodiester bonds, which is what 5' exonucleases evolved to recognize and cleave. The m7G cap is attached via an unusual 5'-to-5' triphosphate linkage — the reverse orientation. This chemically distinct terminus does not fit the exonuclease's substrate-recognition mechanism, so the enzyme cannot initiate degradation at the 5' end. The protection is structural and chemical, not steric or competitive."

- question: "Both the 5' cap and the 3' poly(A) tail are added to mRNA after the complete transcript has been synthesized and released from RNA polymerase II."
  type: true-false
  answer: false
  explanation: "Both modifications are co-transcriptional — they occur while RNA polymerase II is still actively synthesizing the transcript. The 5' cap is added remarkably early, within the first 20–30 nucleotides of transcription. The poly(A) tail is added when the polymerase transcribes past the AAUAAA signal, triggering cleavage and polyadenylation while elongation continues. Co-transcriptional processing is functionally important because it protects the nascent transcript from degradation before it can be finished."

- question: "The 5' cap on mRNA serves a role in translation initiation, not just in protecting the mRNA from degradation."
  type: true-false
  answer: true
  explanation: "The m7G cap is recognized by eukaryotic initiation factor eIF4E, which binds the cap and then recruits other initiation factors and the small (40S) ribosomal subunit to the 5' end of the mRNA. This cap-dependent initiation is how most eukaryotic mRNAs are translated. The cap therefore serves a dual function: it protects the 5' end from exonucleases AND serves as the ribosome landing signal that initiates protein synthesis. Some viral mRNAs exploit cap-independent internal ribosome entry sites (IRES) to bypass this requirement."

- question: "Explain why the gradual shortening of the poly(A) tail by deadenylases is a useful mechanism for cells to control gene expression."
  type: short-answer
  answer: "The poly(A) tail functions as a molecular timer for mRNA lifespan. Deadenylases progressively remove adenine residues from the tail; as the tail shortens, fewer poly(A)-binding proteins can attach to protect it from 3' exonucleases. When the tail becomes too short, the mRNA is rapidly degraded. By controlling the rate of deadenylation (through RNA-binding proteins, miRNAs, and signaling pathways), cells can tune how long a particular mRNA persists and therefore how much protein is produced from it — even without changing the transcription rate."
  explanation: "This mechanism is fundamental to post-transcriptional gene regulation. Many developmental transitions, stress responses, and cell-fate decisions are controlled by regulating mRNA stability rather than transcription rate. The poly(A) tail as a degradation timer makes the cell's response faster and more tunable than relying on transcriptional repression alone, since existing mRNAs can be rapidly silenced by deadenylation."
```

## Explainer

From your study of transcription, you know that RNA polymerase II synthesizes a pre-mRNA strand by reading the template DNA. But the raw transcript that emerges from the polymerase is vulnerable — exonucleases in the nucleus would quickly degrade it from either end, and ribosomes in the cytoplasm would have no way to recognize it as a legitimate message. The **5' cap** and **3' poly(A) tail** solve both problems by adding protective structures to each end of the mRNA, and they do so while transcription is still in progress, not after it finishes.

The **5' cap** is added remarkably early — as soon as the first 20–30 nucleotides have emerged from RNA polymerase II. A capping enzyme removes the terminal phosphate from the 5' end of the nascent RNA, then attaches a guanosine nucleotide in an unusual **5'-to-5' triphosphate linkage** (most nucleotide bonds are 3'-to-5'). This reversed orientation makes the cap chemically distinct from anything an exonuclease expects to encounter, effectively blocking degradation from the 5' end. A methyltransferase then adds a methyl group to the guanosine, creating the **7-methylguanosine (m⁷G) cap**. Later, when the mRNA reaches the cytoplasm, this cap is what the ribosome recognizes: eukaryotic translation initiation factor eIF4E binds the cap and recruits the small ribosomal subunit, making the cap essential for translation to begin.

At the other end, the **3' poly(A) tail** is produced by a two-step process. As RNA polymerase II transcribes past a conserved **AAUAAA signal sequence**, a protein complex called CPSF (cleavage and polyadenylation specificity factor) recognizes this signal and cleaves the pre-mRNA about 10–30 nucleotides downstream. The enzyme **poly(A) polymerase** then adds approximately 200 adenine nucleotides to the new 3' end, one at a time, without any DNA template. This poly(A) tail is bound by poly(A)-binding proteins that protect it from 3' exonuclease attack and, together with the 5' cap, form a loop structure that enhances translation efficiency.

Together, these two modifications transform a fragile, anonymous RNA strand into a recognized, protected, export-ready messenger. The cap says "start translating here," the poly(A) tail says "this message is complete and stable," and both are required for the mRNA to pass through nuclear pores into the cytoplasm. Over time, the poly(A) tail is gradually shortened by deadenylases — this shortening is a molecular clock that determines mRNA lifespan. Once the tail is too short to bind protective proteins, the mRNA is rapidly degraded, giving cells precise control over how long each message persists.
