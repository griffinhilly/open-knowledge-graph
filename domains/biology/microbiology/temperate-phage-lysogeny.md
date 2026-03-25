---
id: temperate-phage-lysogeny
title: Temperate Phages and Lysogenic Pathways
domain: biology
course: microbiology
prerequisites:
- id: viral-replication-cycle
  type: hard
- id: specialized-transduction-excision
  type: soft
- id: bacteriophage-and-lysogenic-cycles
  type: soft
builds-toward:
- lysogenic-conversion-virulence-factors
tags:
- temperate-phage
- lysogeny
- integration
stage: advanced
status: validated
---
# Temperate Phages and Lysogenic Pathways

## Core Idea
Temperate phages like lambda have the option to undergo either lytic replication or lysogenic integration where the phage DNA becomes a prophage in the host chromosome. Integration is controlled by a genetic switch involving competing repressor and lytic transcription factors; the prophage is stably maintained through chromosomal replication and passively transmitted to daughter cells.

## Questions

```yaml
- question: "A bacterium harboring a lambda prophage is exposed to UV radiation. Which outcome is most likely?"
  type: multiple-choice
  options:
    - "Nothing happens — the CI repressor protects the phage DNA from UV-induced damage"
    - "The prophage induces into the lytic cycle after RecA-mediated cleavage of the CI repressor"
    - "The prophage excises but remains as a circular episome without replicating"
    - "The bacterium immediately lyses because UV light directly activates lytic gene expression"
  answer: 1
  explanation: "UV damage activates the bacterial SOS response, which stimulates RecA protein. RecA then promotes autocatalytic cleavage of the CI repressor. With CI destroyed, lytic genes are derepressed, the prophage excises (via excisionase), and the phage enters the lytic cycle. The CI repressor maintains lysogeny under normal conditions but is deliberately designed to be destroyed when the host is under mortal threat."

- question: "During stable lysogeny, what is the function of the CI repressor?"
  type: multiple-choice
  options:
    - "It degrades phage structural proteins to prevent accidental particle assembly"
    - "It catalyzes site-specific recombination to keep the prophage integrated in the chromosome"
    - "It binds operator regions on the phage chromosome and silences lytic gene transcription"
    - "It activates host restriction enzymes to destroy any re-infecting phage particles"
  answer: 2
  explanation: "The CI repressor (lambda repressor) binds to OL and OR operator sites on the phage DNA, blocking transcription of lytic cycle genes — including those encoding Cro protein, replication proteins, and structural components. Low-level continuous CI production maintains this silenced state through cell divisions. Integration is catalyzed by integrase, not CI, and CI does not degrade proteins or activate restriction systems."

- question: "During lysogeny, the prophage DNA replicates along with the host chromosome every time the bacterium divides, and each daughter cell inherits a copy."
  type: true-false
  answer: true
  explanation: "Once integrated, the prophage is indistinguishable from any chromosomal locus — it is replicated by the host's own DNA polymerase and partitioned into both daughter cells at division. No new phage particles are produced. This passive inheritance is why a single infection event can spread a prophage through an entire bacterial population over generations without any sign of lytic activity."

- question: "When lambda phage first infects a bacterium, the lytic cycle automatically occurs because the CI repressor is not yet present at the start of infection."
  type: true-false
  answer: false
  explanation: "The lytic vs. lysogenic decision is made during the initial infection, not after CI builds up. Both CI and Cro proteins are transcribed shortly after phage DNA injection, and their relative accumulation — shaped by multiplicity of infection, host nutritional state, and other signals — determines which pathway dominates. High multiplicity of infection favors lysogeny; well-fed, rapidly growing hosts favor lysis. The phage does not simply default to lysis because CI is initially absent."

- question: "Why does severe DNA damage to the bacterial host cell trigger a dormant prophage to enter the lytic cycle?"
  type: short-answer
  answer: "DNA damage activates the bacterial SOS response, which induces RecA protein to stimulate autocatalytic cleavage of the CI repressor. With CI destroyed, lytic genes are derepressed and the phage switches to replication — it escapes from a host that is likely doomed."
  explanation: "The CI repressor is the molecular switch maintaining lysogeny, and it is engineered to be destroyed precisely when host viability is threatened. The phage does not directly detect DNA damage; instead, it monitors host stress indirectly via RecA activity. This is adaptive: abandoning a doomed host and producing many progeny phage particles is far better than replicating passively with a cell that is about to die."
```

## Explainer

You already know the lytic cycle: a phage attaches, injects its DNA, hijacks the host machinery, replicates furiously, and lyses the cell to release new phage particles. But not every phage infection ends in immediate destruction. **Temperate phages** — lambda phage being the classic example — face a decision point after injecting their DNA. They can go lytic, or they can choose a quieter path: **lysogeny**, in which the phage DNA integrates directly into the host chromosome and rides along as a passive passenger called a **prophage**.

The decision between lysis and lysogeny is governed by a remarkably elegant **genetic switch**. Two competing regulatory proteins fight for control. The **CI repressor** (also called the lambda repressor) binds to operator regions on the phage DNA and blocks transcription of lytic genes, locking the phage into a dormant state. Meanwhile, **Cro protein** promotes lytic gene expression and represses CI. Which protein wins depends on conditions at the moment of infection — factors like the number of phage particles per cell (multiplicity of infection), nutrient availability, and host stress signals tip the balance. When CI wins, the phage integrates; when Cro wins, the lytic cycle proceeds.

Once the prophage is integrated, it behaves almost like an ordinary stretch of bacterial chromosome. Every time the host cell divides and replicates its DNA, the prophage replicates along with it and is inherited by both daughter cells — no new phage particles are made, no lysis occurs. The CI repressor is continuously produced at low levels to maintain this quiet state, effectively keeping all lytic genes silenced. This is why you can have an entire bacterial population carrying a prophage without any sign of phage activity.

The prophage is not permanently trapped, however. If the host cell encounters severe stress — DNA damage from UV light, for instance — the bacterial SOS response activates RecA protein, which stimulates cleavage of the CI repressor. With CI destroyed, the lytic genes are derepressed, the prophage excises from the chromosome (the reverse of integration, catalyzed by excisionase), and the phage enters the lytic cycle. This **induction** event is the prophage's escape hatch: when the host is doomed, the phage abandons ship. Occasionally, excision is imprecise and carries adjacent bacterial genes along with the phage DNA — the basis of specialized transduction you may have encountered as a prerequisite concept.
