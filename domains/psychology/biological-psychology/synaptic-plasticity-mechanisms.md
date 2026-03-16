---
id: synaptic-plasticity-mechanisms
title: Synaptic Plasticity Mechanisms
domain: psychology
course: biological-psychology
prerequisites:
- id: intracellular-signaling-and-second-messengers
  type: hard
- id: long-term-potentiation
  type: soft
- id: ion-channels-and-neural-excitability
  type: hard
- id: protein-synthesis
  type: hard
- id: synaptic-transmission
  type: hard
builds-toward:
- learning-and-memory-at-synaptic-level
tags:
- LTP
- LTD
- plasticity
- AMPA
- NMDA
stage: formal-systems
status: draft
---

# Synaptic Plasticity Mechanisms

## Core Idea
Long-term potentiation (LTP) and long-term depression (LTD) are activity-dependent changes in synaptic strength lasting hours to days or longer. NMDA-receptor-dependent LTP involves: (1) co-activation of pre- and postsynaptic neurons removes Mg2+ block of NMDA channels, (2) Ca2+ influx activates kinases, (3) AMPA receptors are inserted into the postsynaptic membrane, strengthening the synapse. LTD involves different triggers that lead to receptor removal. These mechanisms are hypothesized to underlie learning and memory formation.

## How It's Best Learned
Examine dual-electrode recordings showing pairing-induced synaptic strengthening and weakening. Use NMDA or AMPA receptor antagonists to block specific forms of plasticity. Study AMPA receptor trafficking using imaging. Compare different induction protocols (frequency, timing, intensity).

## Common Misconceptions
All plasticity is spike-timing dependent / synapses only get stronger / plasticity requires protein synthesis always / LTP and LTD are inverse processes at all synapses.

## Explainer

The guiding idea behind synaptic plasticity is Hebb's rule, often summarized as "neurons that fire together, wire together." But the mechanism that actually implements this rule at the molecular level is the **NMDA receptor** — and understanding why requires combining everything you know about ion channels, second messengers, and synaptic transmission. The NMDA receptor is a glutamate-gated ion channel, but with a twist: at resting membrane potential, its channel pore is blocked by a Mg2+ ion that prevents current flow even when glutamate is bound. The Mg2+ block is only relieved when the postsynaptic membrane is depolarized — typically because neighboring AMPA receptors are already open and passing current. This makes the NMDA receptor a **coincidence detector**: it only passes Ca2+ when the presynaptic cell is releasing glutamate *and* the postsynaptic cell is already depolarized, i.e., when pre- and postsynaptic activity co-occur.

That Ca2+ influx is the trigger for **long-term potentiation (LTP)**. Ca2+ entering through NMDA receptors activates kinases — especially CaMKII — that phosphorylate AMPA receptors already at the synapse (making them conduct more current) and signal for additional AMPA receptors to be trafficked from intracellular pools to the postsynaptic membrane. More AMPA receptors on the membrane means a larger response to the same amount of glutamate — the synapse is stronger. This is the early phase of LTP, which can last hours. The **late phase** of LTP, lasting days or longer, requires new protein synthesis: activated kinases and transcription factors produce structural changes including growth of new dendritic spines. This is why protein synthesis inhibitors block long-term but not short-term memory.

**Long-term depression (LTD)** results from a different pattern of synaptic activity — typically lower-frequency stimulation that produces a modest rise in postsynaptic Ca2+. Where large Ca2+ transients activate kinases that insert AMPA receptors, smaller transients instead activate phosphatases that remove them. The resulting decrease in AMPA receptor surface expression weakens the synapse. Notice that LTP and LTD are not simply inverses: they have different induction protocols, involve different enzymes, and are not uniformly distributed across all synapse types. Some synapses express primarily NMDA-dependent forms of plasticity; others use mGluR-dependent or endocannabinoid-dependent mechanisms that do not follow the same rules.

Together, LTP and LTD provide synapses with a bidirectional gain control grounded in activity history. A synapse that frequently participates in coordinated firing grows stronger; one that is active without coordinated postsynaptic response is weakened. This elegantly implements a form of correlation-based learning that is believed to underlie associative memory formation — two events that co-occur repeatedly form a stronger representational link at the synaptic level. Crucially, the intracellular signaling cascades you studied earlier are not just background plumbing here: they are the computational machinery through which activity patterns at the membrane surface are translated into lasting structural change.

