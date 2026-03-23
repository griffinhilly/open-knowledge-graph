---
id: transcription-initiation-prokaryotes
title: 'Prokaryotic Transcription Initiation: Sigma Factors and Promoters'
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: transcription
  type: hard
- id: gene-regulation-prokaryotes
  type: soft
builds-toward:
- transcription-elongation-and-termination
- promoters-enhancers-and-regulatory-regions
tags:
- sigma-factors
- pribnow-box
- -10-element
- -35-element
- promoter-specificity
stage: formal-systems
status: draft
---

# Prokaryotic Transcription Initiation: Sigma Factors and Promoters

## Core Idea
In prokaryotes, transcription initiation requires sigma factors—dissociable subunits that confer promoter-specific DNA recognition to the core RNA polymerase. Sigma factors recognize consensus sequences upstream of the transcription start site: the -10 region (Pribnow box, consensus TATAAT) and the -35 region (consensus TTGACA). Different sigma factors (σ70 for housekeeping genes, σ32 for heat-shock, σ54 for nitrogen metabolism) recognize distinct promoter variants, enabling global gene regulation in response to stress. Sigma factor dissociates after synthesis of ~8-10 nucleotides of transcript, allowing the polymerase core to transition to elongation.

## Questions

```yaml
- question: "A researcher engineers an E. coli strain where sigma⁷⁰ is covalently attached to the core RNA polymerase and cannot dissociate. Which of the following best predicts the consequences for gene regulation?"
  type: multiple-choice
  options:
    - "All transcription stops immediately because sigma must cycle off for elongation to proceed"
    - "Only stress-response genes are affected since sigma⁷⁰ controls only housekeeping gene transcription"
    - "Stress responses fail because alternative sigma factors cannot displace sigma⁷⁰ from the core polymerase, and initiation becomes slower because sigma cannot recycle to new promoters"
    - "Gene expression is unaffected since sigma only assists with promoter finding but is not required for regulation"
  answer: 2
  explanation: "Sigma factor dissociation after initiation serves two critical functions: it allows alternative sigma factors to compete for the core polymerase (enabling regulatory reprogramming during stress), and it allows the released sigma to associate with a new core polymerase and initiate again at another promoter (recycling). If sigma⁷⁰ cannot dissociate, the core polymerase is permanently committed to sigma⁷⁰ promoters — stress responses controlled by σ³², σˢ, or σ⁵⁴ cannot be activated because those sigma factors cannot access the core enzyme. The cell loses the ability to globally reprogram its transcriptional output in response to environmental change, which is the primary function of the interchangeable sigma factor system."

- question: "Why is the AT-rich consensus sequence (TATAAT) of the -10 element functionally important for transcription initiation, rather than being an arbitrary recognition code?"
  type: multiple-choice
  options:
    - "A-T base pairs are specifically recognized by sigma factor's DNA-binding domain but are invisible to non-specific DNA-binding proteins, providing selectivity"
    - "A-T base pairs have only two hydrogen bonds compared to three for G-C pairs, making the -10 region easier to melt apart — which is required to form the open complex and expose the template strand"
    - "The TATAAT sequence encodes the start codon region that the ribosome will later recognize on the mRNA"
    - "AT-rich regions attract RNA polymerase through electrostatic interactions more effectively than GC-rich regions"
  answer: 1
  explanation: "The functional importance of the AT-rich -10 element is thermodynamic, not just recognition-based. After sigma factor positions the holoenzyme at the promoter (closed complex), the DNA must locally unwind to form the open complex — a bubble of single-stranded DNA that exposes the template strand for synthesis. A-T base pairs are weaker (2 hydrogen bonds vs. 3 for G-C) and require less energy to separate. Placing the most easily melted sequence at the -10 element — precisely where strand separation must begin — is not coincidental. It reduces the energy barrier for open complex formation. This principle is conserved across bacteria: -10 elements universally tend to be AT-rich regardless of the exact consensus."

- question: "The core RNA polymerase in E. coli can bind DNA and synthesize RNA efficiently, but requires a sigma factor specifically to recognize and bind promoter sequences at the -10 and -35 elements."
  type: true-false
  answer: true
  explanation: "This is the central division of labor in prokaryotic transcription initiation. The core enzyme (α₂ββ'ω) has all the catalytic machinery needed to polymerize RNA and can bind DNA nonspecifically, but it lacks the structural domains that make specific contacts with promoter elements. Sigma factor supplies these: it makes direct contacts with the -35 element and the -10 element in the major groove of DNA, positioning the holoenzyme precisely at the transcription start site. This modularity is the key to bacterial gene regulation — swapping sigma factors changes which promoters are recognized without altering the core catalytic machinery."

- question: "Each of E. coli's different sigma factors (σ⁷⁰, σ³², σ⁵⁴) associates with a dedicated RNA polymerase molecule, so the cell maintains separate pools of holoenzyme for different gene classes."
  type: true-false
  answer: false
  explanation: "All sigma factors compete for the same limited pool of core RNA polymerase. There is one core enzyme; sigma factors are interchangeable subunits. When cellular conditions change (heat shock, nitrogen starvation, stationary phase), the concentration or activity of specific alternative sigma factors changes, and they outcompete sigma⁷⁰ for core polymerase binding. Because all sigma factors share the same pool of core enzyme, upregulating one sigma factor effectively reprograms the entire transcriptional output — a simple but powerful form of global regulation that would be impossible if each sigma factor had its own dedicated polymerase."

- question: "Why do sigma factors dissociate from the RNA polymerase after initiation rather than remaining attached throughout elongation? What two functional advantages does this dissociation provide?"
  type: short-answer
  answer: "Sigma dissociates because it is not needed for elongation — the core polymerase can synthesize RNA processively once it has cleared the promoter — and its retention would actively interfere with elongation by keeping the polymerase tethered to the promoter sequence. Two functional advantages follow: (1) Recycling — released sigma factor can immediately associate with another core polymerase and initiate at a new promoter, so the cell needs far fewer sigma molecules than core polymerase molecules (sigma acts catalytically with respect to initiation events); (2) Competitive regulation — once sigma dissociates, the free core polymerase can be captured by a different sigma factor, enabling rapid global reprogramming of transcription in response to stress without requiring new synthesis of core enzyme."
  explanation: "The recycling advantage is often underappreciated. During active growth, a few thousand sigma⁷⁰ molecules can service many more core polymerase molecules because each initiation event releases the sigma factor. If sigma remained attached, every elongating polymerase would permanently sequester one sigma molecule, requiring the cell to produce far more sigma protein. The regulatory advantage is equally important: the competition between sigma factors for the core enzyme means that changing the cellular abundance of a single alternative sigma factor can redirect a substantial fraction of total transcriptional capacity to a new gene program, which is energetically efficient and fast."
```

## Explainer

From your study of transcription, you know that RNA polymerase synthesizes RNA from a DNA template. In prokaryotes like *E. coli*, there is only one core RNA polymerase (composed of subunits α₂ββ'ω), and it handles all transcription — mRNA, rRNA, and tRNA alike. But here is the problem: the core enzyme can bind DNA nonspecifically and can elongate RNA, yet it cannot recognize promoters on its own. It needs a detachable guide to find the right starting points. That guide is the **sigma factor (σ)**, and the combination of core polymerase plus sigma factor is called the **holoenzyme**.

The sigma factor works by recognizing two specific DNA sequences upstream of the transcription start site. The **-10 element** (also called the **Pribnow box**, consensus sequence TATAAT) sits approximately 10 base pairs upstream of where transcription begins, and the **-35 element** (consensus TTGACA) sits about 35 base pairs upstream. Sigma factor makes direct contact with both of these sequences in the major groove of the DNA. The AT-rich nature of the -10 element is functionally important: A-T base pairs have only two hydrogen bonds (compared to three for G-C pairs), making this region easier to melt apart — and strand separation is exactly what must happen for the polymerase to access the template strand. Once sigma recognizes the promoter, the holoenzyme forms a **closed complex** (DNA still double-stranded), then transitions to an **open complex** as the DNA around the -10 region unwinds to create a transcription bubble of roughly 12–14 base pairs.

The elegance of the sigma factor system lies in its modularity. *E. coli* has seven different sigma factors, each recognizing a distinct set of promoter sequences. The primary sigma factor, **σ⁷⁰**, drives transcription of housekeeping genes — the thousands of genes needed for routine growth and metabolism. But when the cell faces environmental stress, alternative sigma factors take over. **σ³²** (RpoH) is stabilized during heat shock and redirects polymerase to promoters controlling chaperones and proteases. **σ⁵⁴** (RpoN) recognizes a completely different promoter architecture (with a -24/-12 element instead of -35/-10) and requires an activator protein to catalyze open complex formation. **σˢ** (RpoS) accumulates during stationary phase and starvation, redirecting transcription toward stress survival genes. Because all sigma factors compete for the same limited pool of core polymerase, increasing the concentration of one sigma factor effectively reprograms the cell's entire transcriptional output — a simple but powerful form of global gene regulation.

After the holoenzyme synthesizes approximately 8–10 nucleotides of RNA, the sigma factor's grip on the promoter weakens and it **dissociates**, leaving the core polymerase to continue elongation on its own. The released sigma factor is then free to associate with another core polymerase and initiate transcription at a new promoter. This recycling mechanism means the cell needs far fewer sigma factors than polymerase molecules — sigma acts catalytically with respect to initiation events. The entire system illustrates a recurring theme in prokaryotic biology: achieving regulatory sophistication through combinatorial use of a small number of interchangeable parts rather than through the elaborate multiprotein assemblies characteristic of eukaryotic transcription.
