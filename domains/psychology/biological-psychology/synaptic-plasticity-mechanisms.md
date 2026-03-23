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

## Questions

```yaml
- question: "The NMDA receptor is called a 'coincidence detector.' In the context of LTP induction, what two conditions must coincide for Ca2+ to flow through it?"
  type: multiple-choice
  options:
    - "Glutamate binding and glycine co-agonist binding at two separate sites on the receptor"
    - "Glutamate release from the presynaptic terminal AND sufficient depolarization of the postsynaptic membrane to relieve the Mg2+ block"
    - "High-frequency stimulation of the presynaptic terminal AND activation of neighboring inhibitory interneurons"
    - "Simultaneous opening of NMDA receptors at two adjacent synapses on the same dendritic branch"
  answer: 1
  explanation: "The Mg2+ block is the key: at resting potential the pore is physically plugged by Mg2+, so even with glutamate bound no current flows. The block is only relieved when the postsynaptic membrane depolarizes — typically because AMPA receptors at the same synapse are already open and passing current. Ca2+ then flows only when glutamate is present (presynaptic activity) AND the postsynaptic cell is already depolarized. This dual requirement is exactly Hebb's rule implemented molecularly."

- question: "After LTP is induced at a synapse, the EPSP in response to the same glutamate input is significantly larger. The primary cellular mechanism underlying this increase is:"
  type: multiple-choice
  options:
    - "Increased neurotransmitter release from the presynaptic terminal due to calcium-dependent facilitation"
    - "Insertion of additional AMPA receptors into the postsynaptic membrane, increasing current flow for the same glutamate stimulus"
    - "Upregulation of NMDA receptor expression, increasing calcium entry on subsequent stimulations"
    - "Retraction of neighboring inhibitory synapses, reducing competition for postsynaptic current"
  answer: 1
  explanation: "LTP works primarily by increasing postsynaptic AMPA receptor number. Ca2+ entering through NMDA receptors activates CaMKII, which phosphorylates existing AMPA receptors (making them conduct more) and signals for additional AMPA receptors to be trafficked from intracellular stores to the membrane. More AMPA receptors mean a larger EPSP to the same glutamate input — the synapse is 'stronger.' This is why blocking AMPA trafficking blocks LTP even when NMDA receptors are intact."

- question: "LTD (long-term depression) and LTP (long-term potentiation) are inverse processes that use the same kinase machinery in reverse — AMPA receptors are removed by the same CaMKII that inserts them during LTP."
  type: true-false
  answer: false
  explanation: "LTP and LTD are not mirror processes and do not use the same enzymes. LTP requires large Ca2+ influx that activates kinases (especially CaMKII), leading to AMPA receptor insertion. LTD requires a smaller, more modest Ca2+ rise that instead activates phosphatases, leading to AMPA receptor removal and internalization. Different Ca2+ magnitudes activate entirely different downstream enzymes. The magnitude of the Ca2+ signal — not just its presence — determines the direction of plasticity."

- question: "Protein synthesis inhibitors block long-term memory consolidation without affecting short-term memory because only the late phase of LTP requires new protein synthesis."
  type: true-false
  answer: true
  explanation: "Early-phase LTP (hours) is achieved through post-translational modification: phosphorylation of existing AMPA receptors and receptor trafficking from internal pools. These processes do not require new protein synthesis. Late-phase LTP (days or longer) requires gene transcription and translation of new structural proteins for dendritic spine growth and synaptic remodeling. Protein synthesis inhibitors block this late phase while leaving early-phase LTP intact — directly explaining the dissociation between short-term and long-term memory in behavioral experiments."

- question: "Explain how the NMDA receptor implements Hebb's rule ('neurons that fire together, wire together') at the molecular level."
  type: short-answer
  answer: "The NMDA receptor physically detects the co-occurrence of presynaptic and postsynaptic activity. Its pore is blocked by Mg2+ at resting potential, preventing Ca2+ entry even when glutamate is bound. The Mg2+ block is relieved only when the postsynaptic membrane is sufficiently depolarized — which happens when the postsynaptic cell is already active (via AMPA receptor activation at the same synapse). So Ca2+ flows only when both presynaptic glutamate release AND postsynaptic depolarization coincide. That Ca2+ influx then activates CaMKII, driving AMPA receptor insertion and synapse strengthening."
  explanation: "Hebb's rule is not just a metaphor — it has a direct molecular implementation. The NMDA receptor acts as a molecular 'AND gate,' requiring both inputs simultaneously. Presynaptic firing alone (glutamate present, but postsynaptic cell at rest — Mg2+ block intact) produces no Ca2+ and no LTP. Postsynaptic depolarization alone (no glutamate, so NMDA receptors not bound) also fails. Only coincident activity — the precise Hebbian condition — opens the gate. The NMDA receptor thus translates correlation between pre- and postsynaptic firing into a biochemical signal that physically strengthens the connection."
```

## Explainer

The guiding idea behind synaptic plasticity is Hebb's rule, often summarized as "neurons that fire together, wire together." But the mechanism that actually implements this rule at the molecular level is the **NMDA receptor** — and understanding why requires combining everything you know about ion channels, second messengers, and synaptic transmission. The NMDA receptor is a glutamate-gated ion channel, but with a twist: at resting membrane potential, its channel pore is blocked by a Mg2+ ion that prevents current flow even when glutamate is bound. The Mg2+ block is only relieved when the postsynaptic membrane is depolarized — typically because neighboring AMPA receptors are already open and passing current. This makes the NMDA receptor a **coincidence detector**: it only passes Ca2+ when the presynaptic cell is releasing glutamate *and* the postsynaptic cell is already depolarized, i.e., when pre- and postsynaptic activity co-occur.

That Ca2+ influx is the trigger for **long-term potentiation (LTP)**. Ca2+ entering through NMDA receptors activates kinases — especially CaMKII — that phosphorylate AMPA receptors already at the synapse (making them conduct more current) and signal for additional AMPA receptors to be trafficked from intracellular pools to the postsynaptic membrane. More AMPA receptors on the membrane means a larger response to the same amount of glutamate — the synapse is stronger. This is the early phase of LTP, which can last hours. The **late phase** of LTP, lasting days or longer, requires new protein synthesis: activated kinases and transcription factors produce structural changes including growth of new dendritic spines. This is why protein synthesis inhibitors block long-term but not short-term memory.

**Long-term depression (LTD)** results from a different pattern of synaptic activity — typically lower-frequency stimulation that produces a modest rise in postsynaptic Ca2+. Where large Ca2+ transients activate kinases that insert AMPA receptors, smaller transients instead activate phosphatases that remove them. The resulting decrease in AMPA receptor surface expression weakens the synapse. Notice that LTP and LTD are not simply inverses: they have different induction protocols, involve different enzymes, and are not uniformly distributed across all synapse types. Some synapses express primarily NMDA-dependent forms of plasticity; others use mGluR-dependent or endocannabinoid-dependent mechanisms that do not follow the same rules.

Together, LTP and LTD provide synapses with a bidirectional gain control grounded in activity history. A synapse that frequently participates in coordinated firing grows stronger; one that is active without coordinated postsynaptic response is weakened. This elegantly implements a form of correlation-based learning that is believed to underlie associative memory formation — two events that co-occur repeatedly form a stronger representational link at the synaptic level. Crucially, the intracellular signaling cascades you studied earlier are not just background plumbing here: they are the computational machinery through which activity patterns at the membrane surface are translated into lasting structural change.

