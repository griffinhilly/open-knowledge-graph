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

## Questions

```yaml
- question: "A negative-sense RNA virus infects a cell. Which event must occur FIRST before any viral protein can be produced?"
  type: multiple-choice
  options:
    - "Host ribosomes directly translate the viral genome into viral proteins, including the RdRp"
    - "The RdRp packaged inside the viral particle transcribes the negative-sense genome into positive-sense mRNA"
    - "The host cell's DNA-dependent RNA polymerase transcribes the viral genome into mRNA"
    - "The viral genome integrates into the host chromosome so that the host transcription machinery can copy it"
  answer: 1
  explanation: "A negative-sense RNA genome is the complementary strand of mRNA — host ribosomes cannot translate it directly. The virus must carry pre-made RdRp molecules inside its particle so that, immediately upon entry, the enzyme can transcribe the genome into positive-sense mRNA. Only then can ribosomes translate viral proteins. Option A describes positive-sense viruses, which can be translated directly. Option C is wrong because the host's RNA polymerase reads DNA templates, not RNA. Option D describes retroviruses, which use a completely different strategy (reverse transcription). The need to package RdRp is a defining feature that distinguishes negative-sense from positive-sense RNA viruses."

- question: "An antiviral drug is developed that increases the error rate of the influenza RdRp by 10-fold. Why might this be therapeutically effective?"
  type: multiple-choice
  options:
    - "Higher mutation rates allow the virus to evolve new immune-evasion variants faster, but the drug also triggers a stronger immune response that clears the infection"
    - "Higher mutation rates generate more immunogenic variants that stimulate a more robust antibody response"
    - "Pushing the mutation rate past an error catastrophe threshold causes the viral population to accumulate too many deleterious mutations to maintain functional genomes, collapsing the population"
    - "Higher mutation rates slow viral replication because the RdRp must restart more often after making errors"
  answer: 2
  explanation: "This drug strategy — called lethal mutagenesis — exploits the error catastrophe threshold. RNA viruses already replicate near the upper limit of tolerable mutation rates; nearly every genome copy has at least one mutation. A further 10-fold increase pushes most genome copies past the point where they can encode functional proteins. The quasi-species population, which normally contains a few viable variants, becomes overwhelmed by defective genomes and collapses. Drugs like ribavirin and molnupiravir work by this mechanism. Option A is backwards: more immune-evasion variants would make the drug counterproductive."

- question: "A positive-sense RNA virus can begin producing viral proteins immediately after its genome enters the host cell cytoplasm, without requiring any pre-packaged viral enzymes."
  type: true-false
  answer: true
  explanation: "A positive-sense RNA genome has the same polarity as mRNA — it is directly readable by host ribosomes. When the genome enters the cytoplasm, ribosomes can begin translating it immediately, producing viral proteins including the RdRp needed for genome replication. This is a significant advantage: the virus needs to carry less machinery into the cell and can begin the replication cycle faster. Poliovirus, SARS-CoV-2, and hepatitis C are positive-sense RNA viruses that exploit this strategy."

- question: "Because RNA viruses lack proofreading, all RNA viruses evolve at the same mutation rate, making them equally prone to rapid antigenic change."
  type: true-false
  answer: false
  explanation: "Coronaviruses are an important exception: they encode a 3'→5' exonuclease (nsp14) that provides proofreading activity. This reduces their mutation rate compared to most other RNA viruses and is why coronaviruses can maintain unusually large RNA genomes (~30,000 bases) without collapsing under mutational load — larger genomes require lower error rates to preserve the encoded information. Influenza, HIV, and poliovirus lack this proofreading and do evolve at the typical high RNA virus mutation rate. Mutation rate in RNA viruses is not uniform; it reflects which additional error-correction mechanisms the virus has evolved."

- question: "Why must negative-sense RNA viruses package RdRp molecules inside their viral particles, whereas positive-sense RNA viruses do not need to?"
  type: short-answer
  answer: "Positive-sense RNA genomes have the same polarity as mRNA, so host ribosomes can translate them immediately upon entry — including translating the RdRp gene to produce the enzyme. Negative-sense RNA genomes are the complementary strand and cannot be translated by ribosomes. The RdRp must transcribe the genome into readable mRNA before any viral protein can be made. Since no host enzyme performs this RNA→RNA transcription, the RdRp must be brought into the cell pre-assembled inside the viral particle, or no transcription could ever begin."
  explanation: "This question tests whether students understand the problem each virus class faces rather than just memorizing the answer. The logic is: host cells have no RdRp → RdRp must come from the virus → but if you can't make proteins yet (because your genome isn't readable), you can't synthesize RdRp → therefore the enzyme must already be present. Positive-sense viruses escape this chicken-and-egg problem by having a genome that can directly recruit ribosomes. Negative-sense viruses solve it by pre-packaging the enzyme. The solution each class uses is a direct consequence of the fundamental constraint."
```

## Explainer

You already know from RNA polymerase mechanisms that DNA-dependent RNA polymerases transcribe DNA into RNA, and from viral attachment that viruses must first bind and enter host cells before they can replicate. RNA viruses face a unique problem once inside: the host cell has no enzyme that can copy RNA from an RNA template. DNA polymerases copy DNA; RNA polymerases read DNA to make RNA. But nothing in the host's toolkit reads RNA to make RNA. This means every RNA virus must either carry its own **RNA-dependent RNA polymerase (RdRp)** into the cell or encode one in its genome for immediate translation.

The distinction between **positive-sense** and **negative-sense** RNA viruses turns on this problem. A positive-sense RNA genome — like that of poliovirus, hepatitis C, or SARS-CoV-2 — has the same polarity as mRNA. When it enters the cell, host ribosomes can immediately translate it into protein, including the RdRp the virus needs to copy itself. Think of it like delivering a message already written in the language the factory speaks: production begins on arrival. A negative-sense RNA genome — like that of influenza, Ebola, or rabies — is the complementary strand, the "mirror image" of mRNA. Ribosomes cannot read it directly. These viruses must carry pre-made RdRp molecules inside their viral particle so that the enzyme enters the cell along with the genome and can transcribe it into readable mRNA before anything else can happen.

The RdRp itself is a remarkably error-prone enzyme. Unlike DNA polymerases, which have **3′→5′ exonuclease proofreading** activity that lets them back up and correct mistakes, RdRps lack this correction mechanism. The result is a mutation rate of roughly one error per 1,000 to 10,000 nucleotides copied — orders of magnitude higher than DNA replication. For a virus with a genome of about 10,000 bases, this means nearly every new copy contains at least one mutation. Rather than being a disadvantage, this error rate generates a swarm of slightly different variants called a **quasi-species population**. Within this cloud of variants, most mutations are neutral or harmful, but a few may confer advantages — resistance to an antiviral drug, escape from an antibody, or improved binding to a host receptor.

This high mutation rate explains why RNA viruses evolve so rapidly and why influenza requires a new vaccine each year. It also explains why coronaviruses are a partial exception: they encode an additional exonuclease (nsp14) that provides some proofreading, which is why their genomes can be unusually large for RNA viruses (around 30,000 bases) without collapsing under mutational load. The tension between error rate and genome size is a fundamental constraint on RNA virus biology — too many errors and the genome cannot maintain the information it encodes, a threshold called the **error catastrophe**. Antiviral drugs like ribavirin and molnupiravir exploit exactly this vulnerability, pushing the mutation rate past the catastrophe threshold so the viral population collapses.
