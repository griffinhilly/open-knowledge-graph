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
status: validated
---

# Toll-Like Receptors and TLR Signaling

## Core Idea
Toll-like receptors (TLRs) are the most well-characterized PRR family, with 10 functional human TLRs recognizing diverse PAMPs including lipopolysaccharides, peptidoglycans, and nucleic acids. TLRs signal through MyD88-dependent and TRIF-dependent pathways leading to activation of NF-κB and IRF transcription factors. This drives production of pro-inflammatory cytokines and type I interferons.

## Questions

```yaml
- question: "TLRs 7 and 8 are located in endosomal membranes rather than on the cell surface. This endosomal location is functionally appropriate because:"
  type: multiple-choice
  options:
    - "The low pH of the endosome stabilizes RNA-receptor binding and enhances signaling"
    - "Single-stranded viral RNA is only exposed after a virus is internalized and its protein coat is stripped in the endosome"
    - "Cell surface location would make TLRs 7 and 8 vulnerable to cleavage by extracellular proteases"
    - "Endosomal TLRs require co-stimulation from surface TLRs before they can initiate signaling"
  answer: 1
  explanation: "The location of a TLR must match where its ligand is encountered. Single-stranded RNA from viruses (TLR7/8) and double-stranded RNA from viral replication (TLR3) are not accessible on the cell surface — they are hidden inside viral particles until the virus is internalized and degraded in the endosome. Placing these TLRs in the endosomal membrane positions the receptor exactly where the ligand becomes detectable. This also reduces the risk of erroneously detecting self RNA circulating extracellularly."

- question: "A patient with a homozygous loss-of-function mutation in MyD88 presents with recurrent, severe bacterial infections. The most likely immunological explanation is:"
  type: multiple-choice
  options:
    - "Inability to produce type I interferons, leaving the patient vulnerable to viral infections"
    - "Failure of most TLRs to activate NF-κB, eliminating the pro-inflammatory cytokine response needed to fight pyogenic bacteria"
    - "Loss of complement activation, preventing opsonization of bacteria"
    - "Selective impairment of antifungal responses, because MyD88 is specifically required for fungal PAMP signaling"
  answer: 1
  explanation: "MyD88 is the adaptor protein used by most TLRs (all except TLR3, and partially TLR4) to activate NF-κB. NF-κB drives expression of TNF-α, IL-1, IL-6, and other pro-inflammatory cytokines that recruit neutrophils and macrophages to sites of bacterial infection. Without MyD88, this response is severely impaired, leaving patients unable to mount the initial inflammatory response to pyogenic bacteria. Type I interferon production via TRIF (used by TLR3 and TLR4) is preserved, which is why viral immunity is less affected."

- question: "The MyD88-dependent and TRIF-dependent TLR signaling pathways both ultimately activate NF-κB, which drives production of both pro-inflammatory cytokines and type I interferons."
  type: true-false
  answer: false
  explanation: "The two pathways activate distinct transcription factors with distinct outputs. MyD88 activates NF-κB, driving pro-inflammatory cytokines (TNF-α, IL-1, IL-6). TRIF activates IRF3 and IRF7, driving type I interferons (IFN-α/β) — the antiviral cytokines that induce an antiviral state in neighboring cells. These are not the same response: one is inflammatory (recruiting immune cells), the other is antiviral (blocking viral replication). TLR4 is unique in activating both pathways, which is why LPS triggers both inflammation and an interferon response."

- question: "TLR4 is uniquely potent as an immune stimulus in Gram-negative sepsis partly because it is the only TLR that activates both the MyD88 and TRIF signaling pathways simultaneously."
  type: true-false
  answer: true
  explanation: "Most TLRs use exclusively either MyD88 (inflammatory cytokines via NF-κB) or TRIF (type I interferons via IRF3). TLR4 is exceptional: upon LPS binding, it recruits both adaptors, activating NF-κB (inflammation) AND IRF3 (type I interferons). This dual activation amplifies the immune response synergistically. In sepsis, massive LPS exposure triggers this combined response system-wide, producing the cytokine storm that characterizes septic shock. Understanding TLR4's dual pathway also explains why it is a major drug target for modulating the sepsis response."

- question: "Why does the division of TLRs between cell-surface and endosomal locations represent an elegant design for distinguishing bacterial from viral threats?"
  type: short-answer
  answer: "Bacterial threats are typically extracellular — their PAMPs (LPS, peptidoglycan, flagellin) are exposed on the bacterial surface and accessible to receptors on the outer face of the cell. Cell-surface TLRs (TLR1, 2, 4, 5, 6) are positioned to detect exactly these extracellular structures. Viral threats are initially invisible: intact viral particles don't expose their nucleic acid contents to the outside world. Only after endocytosis and vesicle acidification are viral proteins stripped and nucleic acids exposed. Endosomal TLRs (TLR3, 7, 8, 9) are positioned inside the cell precisely where and when viral nucleic acids become detectable."
  explanation: "This compartmentalization also reduces autoimmunity risk. Self DNA and RNA are present throughout the cytoplasm and extracellular space. Placing nucleic acid-sensing TLRs in endosomes means they are less likely to encounter self nucleic acids (which are not normally routed through the endosomal pathway) and more likely to encounter pathogen-derived nucleic acids (which arrive via endocytosis of pathogens). When this system fails — as in systemic lupus erythematosus, where self DNA enters endosomes — inappropriate TLR9 activation can contribute to autoimmune pathology."
```

## Explainer

You already know that the innate immune system uses **pattern recognition receptors (PRRs)** to detect conserved molecular signatures on pathogens. Toll-like receptors are the best-understood family of PRRs and serve as the first line of molecular sensing — they are the alarm system that tells your innate immune cells "a pathogen is here, and here is roughly what kind." Understanding TLRs means understanding how the body converts pathogen detection into an inflammatory and antiviral response.

Humans have **10 functional TLRs** (TLR1 through TLR10), and their division by location is the first organizing principle. TLRs 1, 2, 4, 5, and 6 sit on the **cell surface** and detect components of microbial cell walls and flagella — structures that are exposed on the outside of bacteria and fungi. TLR4, for instance, recognizes **lipopolysaccharide (LPS)** from Gram-negative bacteria, which is why even tiny amounts of LPS trigger powerful inflammatory responses. TLRs 3, 7, 8, and 9 are found inside the cell, in **endosomal membranes**, where they detect nucleic acids — double-stranded RNA (TLR3), single-stranded RNA (TLR7/8), and unmethylated CpG DNA (TLR9). This intracellular location makes sense: viral nucleic acids are only exposed after a virus has been internalized and its coat stripped away in the endosome. The location of the receptor matches where you would expect to encounter the ligand.

When a TLR binds its ligand, it dimerizes and recruits adaptor proteins that initiate one of two major signaling cascades. The **MyD88-dependent pathway** is used by most TLRs and activates the transcription factor **NF-κB**, which drives expression of pro-inflammatory cytokines like TNF-α, IL-1, and IL-6 — the molecules that recruit neutrophils, activate macrophages, and produce fever. The **TRIF-dependent pathway** (used primarily by TLR3 and TLR4) activates **IRF3/IRF7** transcription factors, leading to production of **type I interferons** (IFN-α and IFN-β) — the antiviral cytokines that put neighboring cells into a defensive state. TLR4 is unique in that it activates both pathways, which partly explains why LPS is such a potent immune stimulus and why Gram-negative sepsis produces such dramatic systemic inflammation.

The clinical significance of TLRs extends in two directions. Deficiencies in TLR signaling (such as MyD88 mutations) leave patients vulnerable to pyogenic bacterial infections because they cannot mount an adequate inflammatory response. Conversely, excessive or inappropriate TLR activation contributes to sepsis, autoimmune diseases, and chronic inflammation. This dual role — essential for defense but dangerous in excess — is a recurring theme in innate immunity that you will encounter repeatedly as you study cytokines and the inflammatory response.
