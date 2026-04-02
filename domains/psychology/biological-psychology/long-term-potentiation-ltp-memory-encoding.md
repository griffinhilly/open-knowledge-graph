---
id: long-term-potentiation-ltp-memory-encoding
title: 'Long-Term Potentiation (LTP): Synaptic Strengthening'
domain: psychology
course: biological-psychology
prerequisites:
- id: synaptic-transmission-neurotransmitter-release
  type: hard
- id: nmda-receptor-structure
  type: hard
- id: long-term-potentiation
  type: hard
- id: experience-dependent-plasticity-learning
  type: hard
- id: ribosomes-and-protein-synthesis-intro
  type: soft
- id: gene-expression-central-dogma
  type: soft
- id: ion-channels-and-neural-excitability
  type: hard
- id: calcium-signaling-neurons
  type: hard
- id: synaptic-plasticity-mechanisms
  type: hard
builds-toward:
- memory-consolidation-systems
- learning-and-experience-dependent-plasticity
tags:
- plasticity
- learning
- memory-encoding
stage: expert
status: validated
---

# Long-Term Potentiation (LTP): Synaptic Strengthening

## Core Idea
Long-term potentiation is an activity-dependent increase in synaptic strength lasting hours or longer. NMDA receptors act as coincidence detectors: they require both presynaptic glutamate release and postsynaptic depolarization to open. This triggers calcium influx that activates protein kinases, leading to insertion of AMPA receptors and increased synaptic efficacy. LTP is considered a cellular mechanism underlying associative learning and memory formation.

## How It's Best Learned
Study the molecular cascade from calcium influx through CaMKII and protein kinase C to receptor trafficking. Compare NMDA and AMPA receptor properties and why this distinction matters for Hebbian learning.

## Questions

```yaml
- question: "What makes NMDA receptors function as 'coincidence detectors' during LTP induction?"
  type: multiple-choice
  options:
    - "They open whenever glutamate binds, regardless of postsynaptic voltage"
    - "They require both presynaptic glutamate release and postsynaptic depolarization to relieve Mg2+ block and allow Ca2+ influx"
    - "They activate only after repeated stimulation over several hours"
    - "They respond only to GABA, not glutamate, at the synapse"
  answer: 1
  explanation: "At resting potential, a Mg2+ ion physically blocks the NMDA receptor channel. Glutamate binding alone is insufficient — the postsynaptic membrane must also be depolarized (typically by AMPA receptor activation) to expel the Mg2+ block. Only when BOTH conditions are met does Ca2+ flow in. This 'and gate' logic is what makes NMDA receptors molecular coincidence detectors implementing Hebbian learning."

- question: "During LTP induction, the calcium influx through NMDA receptors leads to removal of AMPA receptors from the postsynaptic membrane, weakening the synapse."
  type: true-false
  answer: false
  explanation: "The opposite is true. Calcium influx activates CaMKII and other kinases, which trigger the insertion of additional AMPA receptors into the postsynaptic membrane — specifically to the synapse from intracellular pools. More AMPA receptors means greater depolarization in response to the same glutamate release, which is the cellular basis of synaptic strengthening in LTP."

- question: "Why is LTP described as a cellular model of associative learning, and which aspect of its mechanism supports this interpretation?"
  type: short-answer
  answer: "LTP is associative because a synapse is strengthened only when pre- and postsynaptic activity coincide — implementing the Hebbian principle 'neurons that fire together, wire together.' The NMDA receptor's requirement for simultaneous glutamate binding AND postsynaptic depolarization enforces this co-activity requirement at the molecular level."
  explanation: "Classical conditioning requires that a neutral stimulus (CS) become associated with an unconditioned stimulus (US). LTP provides a mechanism: if two inputs converge on the same neuron simultaneously, their synapses are strengthened selectively. This selectivity arises from the Mg2+ block — weak or asynchronous activation cannot lift it. The NMDA receptor thus physically instantiates the 'coincidence' requirement that associative learning demands."
```

## Explainer

You already know that neurons communicate via synaptic transmission — neurotransmitter is released, binds to receptors, and either depolarizes or hyperpolarizes the postsynaptic cell. Long-term potentiation (LTP) is the discovery that this process is not fixed: a synapse can become persistently stronger based on its recent activity history. LTP is the leading cellular candidate for how learning and memory are stored in the brain.

The key to LTP lies in a special receptor: the NMDA receptor. Unlike AMPA receptors, which simply open when glutamate binds, NMDA receptors have an additional requirement — they are blocked by a Mg2+ ion at resting membrane potential. Glutamate binding is necessary but not sufficient to open them. The Mg2+ block is only relieved when the postsynaptic membrane is already depolarized (which happens when AMPA receptors are active). So the NMDA receptor opens only when two things happen simultaneously: presynaptic glutamate release AND postsynaptic depolarization. This makes it a molecular "and gate," or coincidence detector — it detects when two neurons are co-active.

When the NMDA receptor does open, calcium rushes into the postsynaptic cell. This calcium surge activates CaMKII (calcium/calmodulin-dependent protein kinase II) and PKC, which set off a signaling cascade you should recognize from intracellular signaling. The critical downstream effect is the trafficking of additional AMPA receptors to the synapse from intracellular pools. More AMPA receptors at the synapse means a larger depolarizing response to the same presynaptic glutamate release — the synapse is now stronger. This potentiation can last hours or days in early LTP, or indefinitely in late LTP, which requires new protein synthesis.

Why does this matter for learning? Hebb's rule states that "neurons that fire together, wire together." LTP is the mechanism that implements this rule. If two neurons are co-active repeatedly, the synapses between them are selectively strengthened — making that connection easier to reactivate in the future. When you learn that a bell predicts food, or that a name goes with a face, LTP-like processes at specific synapses are changing the strength of those associations. Animals with pharmacologically blocked NMDA receptors cannot form new spatial memories, which is powerful evidence that LTP-like mechanisms are necessary for learning, not just a laboratory phenomenon.
