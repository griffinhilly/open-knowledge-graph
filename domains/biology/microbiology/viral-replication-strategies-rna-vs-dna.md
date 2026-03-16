---
id: viral-replication-strategies-rna-vs-dna
title: 'Viral Replication Strategies: RNA vs DNA Viruses'
domain: biology
course: microbiology
prerequisites:
- id: viral-replication-cycle
  type: hard
- id: viral-replication-dna-polymerase
  type: hard
- id: viral-replication-rna-polymerase
  type: hard
builds-toward:
- viral-pathogenesis-and-disease
- emerging-infectious-diseases
tags:
- viral-replication
- rna-viruses
- dna-viruses
- polymerase
stage: formal-systems
status: draft
---

# Viral Replication Strategies: RNA vs DNA Viruses

## Core Idea
DNA viruses typically replicate in the nucleus using host DNA polymerase and repair machinery (herpesviruses) or encoding their own DNA polymerases (poxviruses). RNA viruses require RNA-dependent RNA polymerases (RdRps) to synthesize RNA; positive-sense RNA viruses can directly serve as mRNA for immediate translation, while negative-sense viruses must first synthesize complementary mRNA. Reverse-transcribing viruses (retroviruses) uniquely use reverse transcriptase to synthesize DNA from RNA templates.

## Explainer

From your study of the viral replication cycle, you know that every virus must hijack a host cell's machinery to copy its genome and produce new virions. The fundamental question that divides viral strategies is: what kind of genome does the virus carry, and how does it get from that genome to mRNA that ribosomes can translate? This is the logic behind the **Baltimore classification** system, which groups viruses by genome type (DNA or RNA, single- or double-stranded) and replication strategy.

**DNA viruses** face the most familiar situation. Host cells already have DNA polymerases designed to copy DNA, so many DNA viruses simply deliver their genome to the nucleus and co-opt the existing replication and transcription machinery. Herpesviruses do exactly this — they slip their DNA into the nucleus, where host RNA polymerase transcribes viral genes just as it would host genes. The tradeoff is that these viruses depend on the host cell being in a replication-competent state. Some DNA viruses, like poxviruses, take a more independent approach: they replicate entirely in the cytoplasm using their own encoded DNA polymerase and transcription enzymes, making them unusually self-sufficient but requiring a much larger genome to carry all that machinery.

**RNA viruses** face a problem that DNA viruses do not: host cells have no enzyme that copies RNA from an RNA template. RNA viruses must therefore encode their own **RNA-dependent RNA polymerase (RdRp)** — an enzyme with no cellular equivalent. The critical distinction among RNA viruses is genome polarity. A **positive-sense** RNA genome reads like mRNA and can be directly translated by ribosomes the moment it enters the cytoplasm — poliovirus and SARS-CoV-2 work this way, giving them a head start because the first proteins made include the RdRp needed to copy the genome. A **negative-sense** RNA genome is the complementary strand and cannot be read by ribosomes; viruses like influenza and Ebola must carry RdRp molecules inside their virion so that the enzyme is immediately available to transcribe the genome into readable mRNA upon entry.

**Retroviruses** like HIV represent the most surprising strategy. They carry a positive-sense RNA genome but do not translate it directly. Instead, they use **reverse transcriptase** — an enzyme that synthesizes DNA from an RNA template, reversing the normal flow of genetic information. The resulting DNA copy integrates into the host chromosome, becoming a permanent part of the cell's genome. This integrated **provirus** is then transcribed by normal host RNA polymerase whenever the cell divides, making retroviral infections essentially lifelong. The lack of proofreading in reverse transcriptase also means retroviruses mutate rapidly, which is why HIV evolves drug resistance so quickly and why no single vaccine has eradicated it. Each replication strategy — DNA, positive-sense RNA, negative-sense RNA, reverse-transcribing — represents a different solution to the same fundamental problem: how to express and copy a genome using a cell that was never designed to cooperate.
