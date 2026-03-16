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
builds-toward:
- lysogenic-conversion-virulence-factors
tags:
- temperate-phage
- lysogeny
- integration
stage: formal-systems
status: draft
---

# Temperate Phages and Lysogenic Pathways

## Core Idea
Temperate phages like lambda have the option to undergo either lytic replication or lysogenic integration where the phage DNA becomes a prophage in the host chromosome. Integration is controlled by a genetic switch involving competing repressor and lytic transcription factors; the prophage is stably maintained through chromosomal replication and passively transmitted to daughter cells.

## Explainer

You already know the lytic cycle: a phage attaches, injects its DNA, hijacks the host machinery, replicates furiously, and lyses the cell to release new phage particles. But not every phage infection ends in immediate destruction. **Temperate phages** — lambda phage being the classic example — face a decision point after injecting their DNA. They can go lytic, or they can choose a quieter path: **lysogeny**, in which the phage DNA integrates directly into the host chromosome and rides along as a passive passenger called a **prophage**.

The decision between lysis and lysogeny is governed by a remarkably elegant **genetic switch**. Two competing regulatory proteins fight for control. The **CI repressor** (also called the lambda repressor) binds to operator regions on the phage DNA and blocks transcription of lytic genes, locking the phage into a dormant state. Meanwhile, **Cro protein** promotes lytic gene expression and represses CI. Which protein wins depends on conditions at the moment of infection — factors like the number of phage particles per cell (multiplicity of infection), nutrient availability, and host stress signals tip the balance. When CI wins, the phage integrates; when Cro wins, the lytic cycle proceeds.

Once the prophage is integrated, it behaves almost like an ordinary stretch of bacterial chromosome. Every time the host cell divides and replicates its DNA, the prophage replicates along with it and is inherited by both daughter cells — no new phage particles are made, no lysis occurs. The CI repressor is continuously produced at low levels to maintain this quiet state, effectively keeping all lytic genes silenced. This is why you can have an entire bacterial population carrying a prophage without any sign of phage activity.

The prophage is not permanently trapped, however. If the host cell encounters severe stress — DNA damage from UV light, for instance — the bacterial SOS response activates RecA protein, which stimulates cleavage of the CI repressor. With CI destroyed, the lytic genes are derepressed, the prophage excises from the chromosome (the reverse of integration, catalyzed by excisionase), and the phage enters the lytic cycle. This **induction** event is the prophage's escape hatch: when the host is doomed, the phage abandons ship. Occasionally, excision is imprecise and carries adjacent bacterial genes along with the phage DNA — the basis of specialized transduction you may have encountered as a prerequisite concept.
