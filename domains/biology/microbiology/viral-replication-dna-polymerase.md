---
id: viral-replication-dna-polymerase
title: DNA Virus Replication Strategies and Polymerases
domain: biology
course: microbiology
prerequisites:
- id: viral-attachment-glycoproteins
  type: hard
- id: dna-replication
  type: hard
tags:
- dna-virus
- replication
- polymerase
stage: advanced
status: draft
---

# DNA Virus Replication Strategies and Polymerases

## Core Idea
DNA viruses employ diverse replication strategies: some use host DNA polymerase in the nucleus, while others carry their own DNA polymerase and replicate in the cytoplasm. Viral replication is rapid and often lacks proofreading, leading to high mutation rates and antigenic drift in persistent viruses like herpesviruses and poxviruses.

## Explainer

From your study of DNA replication, you know the core machinery: a DNA polymerase that reads a template strand and synthesizes a complementary copy, assisted by primase, helicase, and other factors. DNA viruses face the same fundamental challenge — they must copy their genomes — but they have evolved strikingly different strategies for solving it, and the strategy a virus uses shapes nearly everything about its biology.

The first major division is between viruses that **borrow the host's replication machinery** and those that **bring their own**. Small DNA viruses like polyomaviruses and papillomaviruses carry compact genomes with few genes, so they rely heavily on host DNA polymerase. The catch is that host DNA polymerase is only active during S phase of the cell cycle, which means these viruses must either wait for the cell to divide naturally or actively push the cell into S phase — which is why many of these viruses encode oncoproteins that drive cell proliferation and, occasionally, cancer. These viruses replicate in the nucleus, where the host replication machinery resides.

At the other extreme, large DNA viruses like **poxviruses** encode their own DNA polymerase plus a full complement of replication enzymes. This independence means they can replicate entirely in the cytoplasm, never needing to enter the nucleus at all — a remarkable feat for a DNA virus. **Herpesviruses** fall in between: they replicate in the nucleus but encode their own DNA polymerase, giving them partial independence from host enzymes. This viral polymerase is the target of antiviral drugs like acyclovir, which is phosphorylated by a herpesvirus-specific thymidine kinase and then selectively inhibits the viral polymerase over the host enzyme.

A critical consequence of viral polymerase usage is **fidelity**. Host DNA polymerases have robust 3′→5′ exonuclease proofreading and achieve error rates around one mistake per billion bases. Many viral DNA polymerases lack this proofreading entirely, or have reduced proofreading activity, resulting in mutation rates orders of magnitude higher. While most mutations are deleterious, the sheer volume of viral progeny means that advantageous mutations — those enabling immune evasion, drug resistance, or expanded host range — arise frequently. This elevated mutation rate drives **antigenic drift**, the gradual accumulation of surface protein changes that lets persistent viruses like herpesviruses evade immune surveillance over years of chronic infection.
