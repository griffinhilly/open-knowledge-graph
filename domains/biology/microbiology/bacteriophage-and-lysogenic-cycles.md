---
id: bacteriophage-and-lysogenic-cycles
title: Bacteriophage Lytic and Lysogenic Cycles
domain: biology
course: microbiology
prerequisites:
- id: viral-replication-cycle
  type: hard
- id: bacterial-chromosome-structure-and-organization
  type: hard
builds-toward:
- emerging-infectious-diseases
- microbial-genetics-overview
tags:
- bacteriophages
- lytic-cycle
- lysogeny
- phage-biology
stage: advanced
status: draft
---

# Bacteriophage Lytic and Lysogenic Cycles

## Core Idea
Bacteriophages undergo either lytic cycles (rapid replication, host cell lysis, phage release) or lysogenic cycles (integration into the bacterial chromosome as prophages). In lysogeny, prophage DNA replicates along with host DNA and is inherited by daughter cells until induction (stress or specific signals) triggers excision and the lytic cycle. Temperate phages can alternate between cycles; lysogenic conversion allows phages to transfer virulence genes, antibiotic resistance, and metabolic capabilities.

## Questions

```yaml
- question: "A harmless E. coli laboratory strain is infected by a temperate phage carrying a toxin gene. The bacteria survive, show no signs of phage activity, and divide normally. Six months later, descendants of these bacteria are found to produce a potent toxin. What is the most likely explanation?"
  type: multiple-choice
  options:
    - "The phage repeatedly reinfected each generation of bacteria, gradually inserting the toxin gene more stably over time"
    - "The toxin gene mutated into the bacterial chromosome spontaneously, triggered by the initial phage infection"
    - "The phage integrated into the bacterial chromosome as a prophage (lysogeny), and the toxin gene was expressed as part of lysogenic conversion, inherited by all daughter cells"
    - "Viral DNA causes spontaneous mutations that occasionally generate toxin-producing variants after long incubation periods"
  answer: 2
  explanation: "This is lysogeny followed by lysogenic conversion. The phage integrated into the bacterial chromosome as a prophage — silenced by CI repressor — and has been replicated passively with every cell division for six months. The toxin gene carried by the prophage is now expressed as part of the bacterial genome, a process called lysogenic conversion. Every daughter cell inherits both the prophage and its toxin-encoding genes. This is exactly how harmless bacteria become dangerous pathogens: diphtheria toxin, cholera toxin, and Shiga toxin are all prophage-encoded."

- question: "A population of lysogenic bacteria carrying lambda prophage is exposed to UV radiation. What is the most likely outcome?"
  type: multiple-choice
  options:
    - "The prophage remains dormant because UV radiation damages bacterial DNA but cannot affect integrated phage DNA"
    - "UV permanently eliminates the prophage by causing double-strand breaks in the bacterial chromosome at the integration site"
    - "The prophage becomes more stably integrated as the bacteria mount a stress response protecting chromosomal DNA"
    - "UV triggers the bacterial SOS response, which degrades CI repressor, inducing the prophage to excise and enter the lytic cycle"
  answer: 3
  explanation: "UV radiation causes DNA damage that activates the SOS response — the bacterial emergency repair system. A key SOS component, RecA, becomes activated and cleaves the CI repressor protein that was keeping all lytic genes silenced. Without CI repressor, lytic genes are derepressed: the prophage excises from the chromosome and initiates the lytic cycle, producing hundreds of new phages and lysing the cell. This induction is adaptive for the phage: a damaged host is a poor long-term host, so the phage abandons ship to find healthier bacteria."

- question: "Prophage DNA is replicated passively along with the host bacterial chromosome at every cell division, allowing the phage genome to persist across generations without producing any phage particles."
  type: true-false
  answer: true
  explanation: "True. This is the defining feature of lysogeny. The prophage is treated as just another segment of the bacterial chromosome by the host's replication machinery. CI repressor silences all lytic and structural genes, so no phage proteins are made and no particles are assembled. The prophage hitches a free ride, copied faithfully into every daughter cell, potentially for thousands of generations — until induction triggers excision and the lytic cycle."

- question: "Virulent phages like T4 can choose between lytic and lysogenic cycles depending on host cell conditions, just like temperate phages."
  type: true-false
  answer: false
  explanation: "False. Virulent phages are obligate lytic killers — they lack the genetic machinery (CI repressor, integration systems like integrase and attP/attB sites) required for lysogeny. Once a virulent phage infects a bacterium, it always proceeds through the lytic cycle and kills the host. Only temperate phages have the regulatory circuitry to 'decide' between lytic and lysogenic outcomes based on environmental conditions (host nutritional state, multiplicity of infection, etc.). This is a fundamental distinction between the two types."

- question: "Why is lysogenic conversion medically significant? Use a specific example to illustrate why understanding this process matters for bacterial pathogenesis."
  type: short-answer
  answer: "Lysogenic conversion is the process by which a prophage's genes alter the phenotype of its bacterial host, often in ways that directly affect virulence. Medically, this means that a completely harmless bacterial strain can be transformed into a deadly pathogen by a single phage infection event — without any mutation in the bacterium's own genome. For example, Vibrio cholerae strains without a specific prophage (CTXφ) are non-pathogenic; infection by CTXφ introduces the cholera toxin gene as part of the prophage, and lysogenic conversion makes the bacterium capable of causing epidemic cholera. Similarly, Corynebacterium diphtheriae is harmless without its prophage, which carries the diphtheria toxin gene. This matters because it explains how new pathogenic strains can emerge suddenly, why antibiotic-treated patients can sometimes worsen (inducing lytic cycles releases more toxin), and why virulence cannot always be predicted from bacterial genome sequence alone — the phage is the missing piece."
  explanation: "The concept challenges the assumption that a bacterium's danger is fixed by its own genome. Prophages are mobile genetic elements that can be acquired, transferred between strains, and induced — making them dynamic determinants of pathogenicity rather than static features."
```

## Explainer

From your study of viral replication, you know the general logic of how viruses hijack host machinery to reproduce. **Bacteriophages** (phages for short) are viruses that infect bacteria, and they face the same fundamental challenge as all viruses: they cannot replicate on their own and must commandeer a living cell's ribosomes, energy supply, and raw materials. What makes phage biology especially interesting is that many phages have evolved two distinct reproductive strategies and can switch between them depending on conditions — a flexibility that has profound consequences for bacterial evolution.

The **lytic cycle** is the more straightforward strategy. A phage attaches to specific receptors on the bacterial surface, injects its DNA into the cell, and immediately takes over. Phage genes redirect the host's transcription and translation machinery to produce phage proteins and replicate phage DNA, while host DNA is often degraded to provide nucleotides. New phage particles self-assemble inside the cell, and phage-encoded **lysozymes** then digest the peptidoglycan cell wall from within, bursting (lysing) the cell and releasing dozens to hundreds of new phages that infect neighboring bacteria. The entire cycle — from infection to lysis — can take as little as 20–30 minutes. Phages that are locked into this strategy are called **virulent phages** (T4 is a classic example), and they are obligate killers.

**Temperate phages** like bacteriophage λ (lambda) have a second option: the **lysogenic cycle**. Instead of immediately destroying the host, the phage integrates its DNA into the bacterial chromosome at a specific attachment site, becoming a **prophage**. In this integrated state, the phage DNA is replicated passively as part of the host chromosome every time the bacterium divides — the phage essentially hitches a ride, copied faithfully into every daughter cell without any phage proteins being produced. A key molecular player is the **CI repressor protein**, which the prophage constitutively expresses to silence its own lytic genes. As long as CI repressor levels remain high, the phage stays dormant. But when the host cell experiences severe stress — DNA damage from UV radiation, for instance, activates the bacterial SOS response, which triggers degradation of CI repressor — the prophage **excises** from the chromosome and enters the lytic cycle, destroying the now-compromised host to produce new phages that can find healthier hosts.

The lysogenic cycle has consequences that extend far beyond the phage itself. When a prophage integrates, it can carry genes that change the host bacterium's phenotype — a process called **lysogenic conversion**. Some of the most dangerous bacterial toxins are encoded not by the bacterium's own chromosome but by prophages: the toxin that causes diphtheria (*Corynebacterium diphtheriae*), cholera toxin (*Vibrio cholerae*), and the Shiga toxin of *E. coli* O157:H7 are all prophage-encoded. This means that a harmless bacterial strain can become a deadly pathogen through a single phage infection event. Phages are also agents of **transduction** — when a prophage excises imprecisely, it can accidentally package adjacent bacterial genes into phage particles and deliver them to new host cells, driving horizontal gene transfer. This dual nature of phages — as both destroyers and genetic engineers of bacteria — makes them central players in microbial ecology and evolution.
