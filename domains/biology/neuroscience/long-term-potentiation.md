---
id: long-term-potentiation
title: Long-Term Potentiation
domain: biology
course: neuroscience
prerequisites:
- id: postsynaptic-currents-epsc-ipsc
  type: hard
- id: ionotropic-vs-metabotropic-receptors
  type: hard
builds-toward:
- spike-timing-dependent-plasticity
- hippocampus-memory
tags:
- synaptic-plasticity
- learning
stage: expert
status: validated
---

# Long-Term Potentiation

## Core Idea
Lasting increase in synaptic strength from high-frequency stimulation. Ca2+ influx through NMDA receptors activates kinases (CaMKII) that insert AMPA receptors on postsynaptic membrane.

## Questions

```yaml
- question: "What makes the NMDA receptor act as a 'coincidence detector' during LTP induction?"
  type: multiple-choice
  options:
    - "It opens only when intracellular Ca²⁺ levels are already elevated"
    - "It requires both glutamate binding (presynaptic activity) AND postsynaptic depolarization to conduct current"
    - "It is activated only by high-frequency stimulation, never by single action potentials"
    - "It can only open after it physically associates with CaMKII"
  answer: 1
  explanation: "At resting membrane potential, a Mg²⁺ ion physically blocks the NMDA receptor channel even when glutamate is bound. The Mg²⁺ block is only relieved when the postsynaptic membrane is sufficiently depolarized (by summed AMPA receptor activity). This dual requirement — glutamate present AND postsynaptic depolarization — means the NMDA receptor only passes current when the pre- and postsynaptic cells are active simultaneously, the molecular implementation of Hebb's rule."

- question: "Long-term potentiation increases synaptic strength primarily by inserting additional AMPA receptors into the postsynaptic density."
  type: true-false
  answer: true
  explanation: "CaMKII, activated by Ca²⁺ influx through unblocked NMDA receptors, both phosphorylates existing AMPA receptors (increasing their conductance) and traffics additional AMPA receptors from intracellular pools to the postsynaptic membrane. More AMPA receptors means a larger EPSC for the same amount of glutamate released, which is the cellular mechanism underlying the potentiated synapse."

- question: "Why does LTP induction require high-frequency stimulation rather than a single presynaptic action potential?"
  type: short-answer
  answer: "A single presynaptic spike produces only a small EPSP via AMPA receptors, which is insufficient to depolarize the postsynaptic membrane enough to relieve the Mg²⁺ block from NMDA receptors. High-frequency stimulation causes temporal summation of EPSPs, achieving the threshold depolarization needed to expel Mg²⁺ and allow Ca²⁺ influx through NMDA receptors."
  explanation: "Temporal summation during rapid firing is the mechanism by which high-frequency protocols (e.g., 100 Hz tetanic stimulation) cross the depolarization threshold required to unblock NMDA receptors. This is directly connected to the concept of EPSP summation from postsynaptic currents — the NMDA receptor's Mg²⁺ block acts as a gate that only opens when summated inputs are strong enough."
```

## Explainer

Long-term potentiation (LTP) is one of the most thoroughly studied forms of synaptic plasticity and is widely considered the cellular basis of learning and memory. To understand it, recall what you know about ionotropic receptors and postsynaptic currents: when glutamate is released from a presynaptic terminal, it binds to AMPA receptors on the postsynaptic membrane and generates an excitatory postsynaptic current (EPSC). Under normal, low-frequency stimulation, this EPSC is transient and predictable. LTP is what happens when that synapse is repeatedly or strongly activated: it becomes durably more sensitive to the same input.

The key to LTP lies in a second glutamate receptor type that you have learned about: the NMDA receptor. NMDA receptors are ionotropic and highly permeable to Ca²⁺, but they carry a critical restriction at resting membrane potentials — a Mg²⁺ ion physically blocks the channel pore even when glutamate is bound. The Mg²⁺ block is only relieved when the postsynaptic membrane is sufficiently depolarized. This makes the NMDA receptor a molecular "coincidence detector": it only admits Ca²⁺ when the presynaptic terminal is simultaneously releasing glutamate AND the postsynaptic cell is already strongly depolarized by summed AMPA activity. This dual requirement is the molecular implementation of Hebb's rule — "neurons that fire together, wire together" — and it explains why LTP is input-specific and associative.

Once Ca²⁺ enters through unblocked NMDA receptors, it activates CaMKII (calcium/calmodulin-dependent protein kinase II). CaMKII then acts on two targets: it phosphorylates existing AMPA receptors at the synapse (increasing their single-channel conductance) and recruits additional AMPA receptors from intracellular vesicle pools to the postsynaptic density. The net result is that the same amount of glutamate now drives a larger EPSC — the synapse has been potentiated. If you recorded from this neuron before and after LTP induction, you would see the EPSC amplitude increase by 50–100%, and this increase can persist for hours to days without further stimulation.

High-frequency stimulation is required for induction precisely because the NMDA receptor's Mg²⁺ block sets a threshold. A single presynaptic spike generates a small EPSP through AMPA receptors that is insufficient to depolarize the membrane enough to expel Mg²⁺. Repeated, rapid firing causes temporal summation of EPSPs until the threshold depolarization is reached. In the hippocampus — where LTP was first described by Bliss and Lømo in 1973 — theta-burst stimulation (brief bursts of spikes at ~5 Hz, mimicking natural hippocampal firing during exploration) is particularly effective, suggesting this mechanism is actively recruited during spatial learning and memory formation.

LTP research has had a profound impact well beyond neuroscience. It provided the first mechanistic link between neural activity patterns and a lasting change in synaptic efficacy, giving cellular substance to the idea that memory is stored in the connections between neurons. Understanding LTP also illuminates why conditions that disrupt NMDA receptor function or Ca²⁺ signaling — such as Alzheimer's disease or certain drugs — can impair learning and memory consolidation.
