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
stage: advanced
status: draft
---

# Viral Replication Strategies: RNA vs DNA Viruses

## Core Idea
DNA viruses typically replicate in the nucleus using host DNA polymerase and repair machinery (herpesviruses) or encoding their own DNA polymerases (poxviruses). RNA viruses require RNA-dependent RNA polymerases (RdRps) to synthesize RNA; positive-sense RNA viruses can directly serve as mRNA for immediate translation, while negative-sense viruses must first synthesize complementary mRNA. Reverse-transcribing viruses (retroviruses) uniquely use reverse transcriptase to synthesize DNA from RNA templates.

## Questions

```yaml
- question: "A newly isolated virus enters a cell and immediately begins producing viral proteins without any prior RNA synthesis step. Its genome can be directly read by host ribosomes. Which type of virus is this, and why is no prior RNA synthesis needed?"
  type: multiple-choice
  options:
    - "A negative-sense RNA virus that pre-loaded its RdRp and immediately transcribed its genome upon entry"
    - "A positive-sense RNA virus whose genome is already in the same orientation as mRNA and can be directly translated by ribosomes the moment it enters the cytoplasm"
    - "A retrovirus that integrated its genome before this observation was made"
    - "A DNA virus whose genome was already in the nucleus being transcribed by host RNA polymerase"
  answer: 1
  explanation: "The key diagnostic features are: immediate protein production, no RNA synthesis step first, and the genome directly readable by ribosomes. Only a positive-sense RNA genome satisfies all three conditions — it is chemically equivalent to mRNA and can be engaged by ribosomes immediately. Negative-sense RNA viruses (option A) must first be transcribed into positive-sense mRNA by pre-packaged RdRp before any translation can occur. Retroviruses must first reverse-transcribe and integrate before gene expression. DNA viruses require nuclear entry and transcription by RNA polymerase. The head start that positive-sense genomes provide — immediate translation without a prior synthesis step — is a significant advantage in the early stages of infection."

- question: "Why must negative-sense RNA viruses package RdRp molecules inside their virions, while positive-sense RNA viruses do not need to do this?"
  type: multiple-choice
  options:
    - "Negative-sense RNA is chemically unstable and requires enzymatic protection during cell entry and uncoating"
    - "Negative-sense RNA cannot be read by host ribosomes — it must be transcribed into complementary positive-sense mRNA first; without pre-packaged RdRp, no viral proteins could ever be made; positive-sense RNA viruses encode RdRp as one of the first proteins ribosomes produce from the incoming genome"
    - "Positive-sense RNA viruses replicate in the nucleus where host polymerases are available, while negative-sense viruses replicate in the cytoplasm where no polymerases exist"
    - "Host cells degrade negative-sense RNA with antiviral RNases unless it is bound to RdRp for protection"
  answer: 1
  explanation: "This question targets the logic of genome polarity. A negative-sense genome is the antisense strand — host ribosomes cannot translate it. Before any viral protein can be made, the genome must be copied into positive-sense mRNA. But making that copy requires RdRp, and RdRp is a viral protein — which cannot yet exist because no viral proteins have been made. This chicken-and-egg problem is solved by packaging RdRp molecules inside the virion itself, so they are immediately available upon cell entry. Positive-sense RNA viruses bypass this entirely: the incoming genome is translated directly, and RdRp is among the first proteins produced."

- question: "All RNA viruses must encode their own RNA-dependent RNA polymerase because host cells contain no enzyme capable of copying RNA from an RNA template."
  type: true-false
  answer: true
  explanation: "This is a foundational constraint on RNA virus biology. The central dogma of molecular biology — DNA → RNA → protein — describes the normal information flow in cells, but cells have no need to copy RNA from an RNA template in their normal metabolism. Therefore, no host RdRp exists. Every RNA virus, regardless of whether it is positive-sense, negative-sense, double-stranded, or segmented, must either encode its own RdRp in its genome or carry pre-made RdRp molecules in the virion. This also explains why RdRp is a primary antiviral drug target — it has no host equivalent, so inhibiting it is highly selective."

- question: "HIV achieves persistent lifelong infection by integrating into the host chromosome as a provirus; antiretroviral drugs that block reverse transcription will eliminate the integrated provirus from all infected cells."
  type: true-false
  answer: false
  explanation: "Antiretroviral drugs block active reverse transcription — they prevent new infections of cells and prevent already-infected actively replicating cells from producing new virions. But they have no effect on cells that are already latently infected, where the provirus sits quietly in the chromosome with no active viral replication. Long-lived latently infected CD4⁺ T cells form a stable reservoir that persists indefinitely, unaffected by drugs that target viral enzymes. Any interruption of therapy allows these reservoirs to reactivate. Eliminating the proviral reservoir — not just suppressing active replication — is the central challenge in achieving a functional HIV cure."

- question: "Explain why HIV is extremely difficult to cure despite the availability of highly effective antiretroviral therapy, based on its replication strategy."
  type: short-answer
  answer: "HIV is a retrovirus that uses reverse transcriptase to copy its RNA genome into DNA, which then integrates permanently into the host cell's chromosome as a provirus. Once integrated, the provirus is indistinguishable from normal host genomic DNA and is replicated passively every time the cell divides. Antiretroviral therapy blocks reverse transcription and viral assembly in actively replicating virus, preventing new infections and maintaining low viral load. However, it has no mechanism to act on latently infected cells where the provirus is dormant — no viral enzymes are active, no viral proteins are made, and the immune system has nothing to target. Long-lived latently infected memory T cells harbor these proviruses for decades. If treatment stops, latent proviruses reactivate and produce new virus. A cure would require either purging the latent reservoir ('shock and kill' strategies) or permanently silencing it, neither of which has been achieved reliably."
  explanation: "The lack of proofreading by reverse transcriptase also means HIV mutates at a very high rate during active replication, which drives rapid evolution of drug resistance and makes vaccine design extremely difficult. These two features — integration and high mutation rate — both stem directly from the retroviral replication strategy."
```

## Explainer

From your study of the viral replication cycle, you know that every virus must hijack a host cell's machinery to copy its genome and produce new virions. The fundamental question that divides viral strategies is: what kind of genome does the virus carry, and how does it get from that genome to mRNA that ribosomes can translate? This is the logic behind the **Baltimore classification** system, which groups viruses by genome type (DNA or RNA, single- or double-stranded) and replication strategy.

**DNA viruses** face the most familiar situation. Host cells already have DNA polymerases designed to copy DNA, so many DNA viruses simply deliver their genome to the nucleus and co-opt the existing replication and transcription machinery. Herpesviruses do exactly this — they slip their DNA into the nucleus, where host RNA polymerase transcribes viral genes just as it would host genes. The tradeoff is that these viruses depend on the host cell being in a replication-competent state. Some DNA viruses, like poxviruses, take a more independent approach: they replicate entirely in the cytoplasm using their own encoded DNA polymerase and transcription enzymes, making them unusually self-sufficient but requiring a much larger genome to carry all that machinery.

**RNA viruses** face a problem that DNA viruses do not: host cells have no enzyme that copies RNA from an RNA template. RNA viruses must therefore encode their own **RNA-dependent RNA polymerase (RdRp)** — an enzyme with no cellular equivalent. The critical distinction among RNA viruses is genome polarity. A **positive-sense** RNA genome reads like mRNA and can be directly translated by ribosomes the moment it enters the cytoplasm — poliovirus and SARS-CoV-2 work this way, giving them a head start because the first proteins made include the RdRp needed to copy the genome. A **negative-sense** RNA genome is the complementary strand and cannot be read by ribosomes; viruses like influenza and Ebola must carry RdRp molecules inside their virion so that the enzyme is immediately available to transcribe the genome into readable mRNA upon entry.

**Retroviruses** like HIV represent the most surprising strategy. They carry a positive-sense RNA genome but do not translate it directly. Instead, they use **reverse transcriptase** — an enzyme that synthesizes DNA from an RNA template, reversing the normal flow of genetic information. The resulting DNA copy integrates into the host chromosome, becoming a permanent part of the cell's genome. This integrated **provirus** is then transcribed by normal host RNA polymerase whenever the cell divides, making retroviral infections essentially lifelong. The lack of proofreading in reverse transcriptase also means retroviruses mutate rapidly, which is why HIV evolves drug resistance so quickly and why no single vaccine has eradicated it. Each replication strategy — DNA, positive-sense RNA, negative-sense RNA, reverse-transcribing — represents a different solution to the same fundamental problem: how to express and copy a genome using a cell that was never designed to cooperate.
