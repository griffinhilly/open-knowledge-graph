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
stage: formal-systems
status: draft
---

# Bacteriophage Lytic and Lysogenic Cycles

## Core Idea
Bacteriophages undergo either lytic cycles (rapid replication, host cell lysis, phage release) or lysogenic cycles (integration into the bacterial chromosome as prophages). In lysogeny, prophage DNA replicates along with host DNA and is inherited by daughter cells until induction (stress or specific signals) triggers excision and the lytic cycle. Temperate phages can alternate between cycles; lysogenic conversion allows phages to transfer virulence genes, antibiotic resistance, and metabolic capabilities.

## Explainer

From your study of viral replication, you know the general logic of how viruses hijack host machinery to reproduce. **Bacteriophages** (phages for short) are viruses that infect bacteria, and they face the same fundamental challenge as all viruses: they cannot replicate on their own and must commandeer a living cell's ribosomes, energy supply, and raw materials. What makes phage biology especially interesting is that many phages have evolved two distinct reproductive strategies and can switch between them depending on conditions — a flexibility that has profound consequences for bacterial evolution.

The **lytic cycle** is the more straightforward strategy. A phage attaches to specific receptors on the bacterial surface, injects its DNA into the cell, and immediately takes over. Phage genes redirect the host's transcription and translation machinery to produce phage proteins and replicate phage DNA, while host DNA is often degraded to provide nucleotides. New phage particles self-assemble inside the cell, and phage-encoded **lysozymes** then digest the peptidoglycan cell wall from within, bursting (lysing) the cell and releasing dozens to hundreds of new phages that infect neighboring bacteria. The entire cycle — from infection to lysis — can take as little as 20–30 minutes. Phages that are locked into this strategy are called **virulent phages** (T4 is a classic example), and they are obligate killers.

**Temperate phages** like bacteriophage λ (lambda) have a second option: the **lysogenic cycle**. Instead of immediately destroying the host, the phage integrates its DNA into the bacterial chromosome at a specific attachment site, becoming a **prophage**. In this integrated state, the phage DNA is replicated passively as part of the host chromosome every time the bacterium divides — the phage essentially hitches a ride, copied faithfully into every daughter cell without any phage proteins being produced. A key molecular player is the **CI repressor protein**, which the prophage constitutively expresses to silence its own lytic genes. As long as CI repressor levels remain high, the phage stays dormant. But when the host cell experiences severe stress — DNA damage from UV radiation, for instance, activates the bacterial SOS response, which triggers degradation of CI repressor — the prophage **excises** from the chromosome and enters the lytic cycle, destroying the now-compromised host to produce new phages that can find healthier hosts.

The lysogenic cycle has consequences that extend far beyond the phage itself. When a prophage integrates, it can carry genes that change the host bacterium's phenotype — a process called **lysogenic conversion**. Some of the most dangerous bacterial toxins are encoded not by the bacterium's own chromosome but by prophages: the toxin that causes diphtheria (*Corynebacterium diphtheriae*), cholera toxin (*Vibrio cholerae*), and the Shiga toxin of *E. coli* O157:H7 are all prophage-encoded. This means that a harmless bacterial strain can become a deadly pathogen through a single phage infection event. Phages are also agents of **transduction** — when a prophage excises imprecisely, it can accidentally package adjacent bacterial genes into phage particles and deliver them to new host cells, driving horizontal gene transfer. This dual nature of phages — as both destroyers and genetic engineers of bacteria — makes them central players in microbial ecology and evolution.
