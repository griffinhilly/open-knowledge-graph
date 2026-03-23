---
id: lysogenic-conversion-virulence-factors
title: Lysogenic Conversion and Phage-Encoded Virulence
domain: biology
course: microbiology
prerequisites:
- id: temperate-phage-lysogeny
  type: hard
- id: host-pathogen-interactions
  type: soft
tags:
- lysogenic-conversion
- virulence-factors
- phage-genes
stage: advanced
status: validated
---

# Lysogenic Conversion and Phage-Encoded Virulence

## Core Idea
Lysogenic conversion occurs when prophage-encoded genes confer new phenotypes on the host bacterium, particularly virulence factors like toxins (cholera toxin, Shiga toxin) or adhesins. These phage genes are often maintained because they benefit both phage (expansion of host niche) and bacterium (increased virulence and transmission), creating stable symbiotic relationships that shape pathogen evolution.

## Questions

```yaml
- question: "A researcher discovers a strain of Vibrio cholerae that lacks the CTXφ prophage. What can be predicted about this strain?"
  type: multiple-choice
  options:
    - "It cannot survive in the human intestine at all, since the prophage provides essential metabolic genes"
    - "It can colonize the intestinal mucosa but cannot produce cholera toxin and therefore cannot cause classical cholera"
    - "It will be identical in virulence to toxin-producing strains because virulence factors are always encoded in the core genome"
    - "It will spontaneously acquire the CTXφ prophage through mutation within the host"
  answer: 1
  explanation: "Cholera toxin is encoded by the CTXφ prophage, not the core V. cholerae chromosome. Strains lacking this prophage retain the ability to colonize — they have the colonization factors encoded in their own genome — but they cannot produce cholera toxin and therefore cannot cause the profuse watery diarrhea that defines cholera. This distinction is clinically and epidemiologically important: it means that 'V. cholerae' encompasses both virulent and avirulent strains depending solely on prophage carriage."

- question: "Why would natural selection favor a bacteriophage that carries and expresses a virulence factor gene benefiting its bacterial host?"
  type: multiple-choice
  options:
    - "Phages compete with the bacterium for host resources, so virulence genes reduce competition"
    - "A phage that makes its bacterial host more successful at colonizing and spreading to new hosts creates more copies of the phage genome, since the phage replicates every time the bacterium divides"
    - "Virulence genes are selectively neutral for the phage and accumulate by genetic drift alone"
    - "Bacteriophages always carry genes that benefit bacteria because they evolved from ancestral bacterial plasmids"
  answer: 1
  explanation: "This is evolutionary mutualism. When a prophage's host bacterium colonizes more hosts, spreads more efficiently, or evades immune clearance better, the prophage genome replicates more frequently — it travels inside the bacterium to every new host. Cholera toxin causes massive intestinal fluid secretion that flushes enormous numbers of V. cholerae into the environment, directly enhancing transmission. More transmission = more bacterial hosts carrying the prophage = more copies of the phage genome. The toxin gene benefits the phage indirectly by benefiting the bacterium it depends on."

- question: "The genes encoding the most dangerous bacterial toxins — cholera toxin, Shiga toxin, diphtheria toxin — are part of the core bacterial chromosome, conserved through millions of years of bacterial evolution."
  type: true-false
  answer: false
  explanation: "These toxins are encoded by prophages, not the core bacterial chromosome. Cholera toxin is encoded by CTXφ prophage, Shiga toxin by lambdoid prophages in E. coli O157:H7, and diphtheria toxin by the β-prophage in Corynebacterium diphtheriae. This means virulence was acquired *horizontally* — bacteria gained these toxin genes by incorporating phage DNA, not by ancestral vertical inheritance. A bacterium can therefore become virulent suddenly (by acquiring a phage) or lose virulence (by losing a prophage), rather than evolving these capabilities slowly over long timescales."

- question: "Two strains of the same bacterial species can differ dramatically in their ability to cause disease based solely on whether they carry a particular prophage."
  type: true-false
  answer: true
  explanation: "Lysogenic conversion means prophage-encoded genes can fundamentally change a bacterium's phenotype. An avirulent strain that acquires the relevant prophage can become a dangerous pathogen overnight. The examples are concrete: E. coli O157:H7 is pathogenic because it carries Shiga toxin prophages; many E. coli strains without these prophages are harmless gut commensals. This has major implications for clinical microbiology — species identification is insufficient for virulence prediction; you must also characterize prophage content."

- question: "Why does the phage-encoded origin of major bacterial toxins matter for understanding how new pathogens emerge, and what does it imply about the pace of pathogen evolution?"
  type: short-answer
  answer: "Because virulence via lysogenic conversion can be acquired rapidly through horizontal gene transfer — a single infection event — rather than through the slow accumulation of mutations over generations. A harmless bacterium can become a dangerous pathogen when it acquires a phage carrying a toxin gene. This means new virulent strains can emerge far more quickly than traditional evolutionary models predict, and pathogen emergence does not require long-term co-evolution with hosts. It also means that epidemiological tracking must consider phage movement between bacterial populations, not just bacterial evolution alone."
  explanation: "Traditional models of pathogen evolution imagined virulence arising slowly through selection on bacterial mutations. Lysogenic conversion overturns this: the critical genetic event is phage integration, which can happen in a single bacterial generation. This helps explain why dangerous pathogens sometimes appear suddenly in populations — they may be old bacteria newly armed with phage-derived weapons. It also explains why the same species can be pathogenic in one region and harmless in another, depending on local phage populations."
```

## Explainer

You already understand temperate phage biology — how a bacteriophage can integrate its genome into the bacterial chromosome as a **prophage** and replicate passively with the host rather than immediately killing it. Lysogenic conversion is the surprising twist: while sitting quietly in the bacterial genome, the prophage expresses genes that change what the bacterium can do, often transforming a harmless commensal into a dangerous pathogen. Some of the most feared bacterial toxins in medicine are not bacterial genes at all — they are phage genes.

The clearest examples make the concept concrete. **Cholera toxin** — the AB toxin that causes the profuse watery diarrhea of cholera — is encoded by the CTXφ prophage integrated into the *Vibrio cholerae* chromosome. Without this phage, *V. cholerae* can colonize the intestine but cannot cause cholera. **Shiga toxin**, which causes the hemolytic uremic syndrome in *E. coli* O157:H7 infections, is encoded by lambdoid prophages. **Diphtheria toxin**, produced by *Corynebacterium diphtheriae*, is carried by the β-prophage. **Botulinum toxin** in some strains of *Clostridium botulinum* is phage-encoded. In each case, the toxin gene is not part of the core bacterial genome — it arrived via phage infection and integration, meaning that virulence was acquired horizontally rather than evolving from within.

Why would a phage carry a toxin gene? The answer lies in **evolutionary mutualism**. A prophage that makes its host bacterium more successful — better at colonizing, evading the immune system, or spreading to new hosts — is itself more successful, because the phage genome replicates every time the bacterium divides. Cholera toxin causes massive fluid secretion in the human intestine, which increases the concentration of *V. cholerae* shed into the environment and enhances transmission to new hosts. More transmission means more bacterial hosts carrying the prophage, which means more copies of the phage genome. The phage and bacterium form a **coevolutionary partnership** where the phage contributes virulence factors and the bacterium provides replication machinery and environmental access.

This concept has profound implications for how we think about pathogen evolution and classification. A single bacterial species can exist in both virulent and avirulent forms depending on whether it carries a particular prophage — strain typing therefore requires knowing the phage content, not just the bacterial species. Lysogenic conversion also means that new pathogens can emerge rapidly through horizontal gene transfer without waiting for slow mutational processes. When you encounter clinical scenarios involving toxin-mediated diseases, ask: is this toxin chromosomal, or was it delivered by a phage? The answer often reshapes how we understand the epidemiology and evolution of the disease.
