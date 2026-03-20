---
id: viral-replication-rna-polymerase
title: 'RNA Virus Replication: Polymerases and Strategies'
domain: biology
course: microbiology
prerequisites:
- id: viral-attachment-glycoproteins
  type: hard
- id: rna-polymerase-mechanisms
  type: hard
builds-toward:
- reverse-transcription-mechanism
tags:
- rna-virus
- replication
- polymerase
stage: advanced
status: draft
---

# RNA Virus Replication: Polymerases and Strategies

## Core Idea
RNA viruses must encode or carry an RNA-dependent RNA polymerase (RdRp) since host cells lack this enzyme. RdRps lack 3' exonuclease activity and introduce errors at high rates (10^-3 to 10^-4), generating quasi-species populations. Positive-sense RNA viruses can directly translate their genome; negative-sense RNA viruses must first synthesize mRNA.

## Explainer

You already know from RNA polymerase mechanisms that DNA-dependent RNA polymerases transcribe DNA into RNA, and from viral attachment that viruses must first bind and enter host cells before they can replicate. RNA viruses face a unique problem once inside: the host cell has no enzyme that can copy RNA from an RNA template. DNA polymerases copy DNA; RNA polymerases read DNA to make RNA. But nothing in the host's toolkit reads RNA to make RNA. This means every RNA virus must either carry its own **RNA-dependent RNA polymerase (RdRp)** into the cell or encode one in its genome for immediate translation.

The distinction between **positive-sense** and **negative-sense** RNA viruses turns on this problem. A positive-sense RNA genome — like that of poliovirus, hepatitis C, or SARS-CoV-2 — has the same polarity as mRNA. When it enters the cell, host ribosomes can immediately translate it into protein, including the RdRp the virus needs to copy itself. Think of it like delivering a message already written in the language the factory speaks: production begins on arrival. A negative-sense RNA genome — like that of influenza, Ebola, or rabies — is the complementary strand, the "mirror image" of mRNA. Ribosomes cannot read it directly. These viruses must carry pre-made RdRp molecules inside their viral particle so that the enzyme enters the cell along with the genome and can transcribe it into readable mRNA before anything else can happen.

The RdRp itself is a remarkably error-prone enzyme. Unlike DNA polymerases, which have **3′→5′ exonuclease proofreading** activity that lets them back up and correct mistakes, RdRps lack this correction mechanism. The result is a mutation rate of roughly one error per 1,000 to 10,000 nucleotides copied — orders of magnitude higher than DNA replication. For a virus with a genome of about 10,000 bases, this means nearly every new copy contains at least one mutation. Rather than being a disadvantage, this error rate generates a swarm of slightly different variants called a **quasi-species population**. Within this cloud of variants, most mutations are neutral or harmful, but a few may confer advantages — resistance to an antiviral drug, escape from an antibody, or improved binding to a host receptor.

This high mutation rate explains why RNA viruses evolve so rapidly and why influenza requires a new vaccine each year. It also explains why coronaviruses are a partial exception: they encode an additional exonuclease (nsp14) that provides some proofreading, which is why their genomes can be unusually large for RNA viruses (around 30,000 bases) without collapsing under mutational load. The tension between error rate and genome size is a fundamental constraint on RNA virus biology — too many errors and the genome cannot maintain the information it encodes, a threshold called the **error catastrophe**. Antiviral drugs like ribavirin and molnupiravir exploit exactly this vulnerability, pushing the mutation rate past the catastrophe threshold so the viral population collapses.
