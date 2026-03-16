---
id: nmda-receptor-calcium
title: NMDA Receptors and Ca2+-Dependent Signaling in Synaptic Plasticity
domain: biology
course: neuroscience
prerequisites:
- id: long-term-potentiation
  type: hard
builds-toward:
- dendritic-spine-plasticity
- hippocampus-memory-consolidation
tags:
- synaptic-plasticity
- calcium-signaling
- NMDA-receptors
- molecular-mechanisms
stage: advanced
status: draft
---

# NMDA Receptors and Ca2+-Dependent Signaling in Synaptic Plasticity

## Core Idea
NMDA-type glutamate receptors are voltage-dependent and require both glutamate binding and postsynaptic depolarization to open, allowing substantial Ca2+ influx. This coincidence-detection property makes NMDA receptors ideal sensors for Hebbian learning: they signal when presynaptic (glutamate) and postsynaptic (depolarization) events occur together, triggering LTP and other plastic changes.

## Explainer

You already understand that long-term potentiation (LTP) is a lasting increase in synaptic strength following high-frequency stimulation, and that it is a leading cellular model of learning and memory. The NMDA receptor is the molecular device that makes LTP possible — it is the synapse's **coincidence detector**, and understanding how it works reveals why synapses strengthen only when the right conditions are met simultaneously.

Most excitatory synapses in the brain use glutamate as their neurotransmitter and have two major types of glutamate receptor sitting in the postsynaptic membrane: **AMPA receptors** and **NMDA receptors**. AMPA receptors are straightforward — glutamate binds, the channel opens, Na⁺ flows in, and the membrane depolarizes. They mediate the fast excitatory postsynaptic potential you observe in normal synaptic transmission. NMDA receptors are different in a crucial way: even when glutamate binds, the channel remains blocked by a Mg²⁺ ion sitting in the pore. This **voltage-dependent magnesium block** means that at resting membrane potential (around −70 mV), NMDA receptors are effectively sealed shut despite having glutamate bound. Only when the postsynaptic membrane is sufficiently depolarized — typically to around −40 mV or above — does the Mg²⁺ ion get expelled from the pore by electrostatic repulsion, allowing the channel to conduct.

This dual requirement — glutamate binding *and* postsynaptic depolarization — is what makes the NMDA receptor a coincidence detector. Glutamate in the synaptic cleft signals that the presynaptic neuron has fired. Depolarization of the postsynaptic membrane signals that the postsynaptic neuron is also active (either firing or receiving strong input from other synapses). The NMDA receptor opens only when both conditions are true simultaneously. When it does open, it admits not just Na⁺ but also a substantial influx of **Ca²⁺ ions**. This calcium entry is the key signaling event: Ca²⁺ activates intracellular enzymes — particularly **CaMKII** (calcium/calmodulin-dependent protein kinase II) — which phosphorylate existing AMPA receptors to increase their conductance and drive the insertion of additional AMPA receptors into the postsynaptic membrane. More AMPA receptors mean a larger postsynaptic response to the same amount of glutamate, which is the expression of LTP.

The beauty of this mechanism is its selectivity. A synapse that releases glutamate onto a quiescent postsynaptic neuron will activate AMPA receptors and produce a small depolarization, but the Mg²⁺ block will keep NMDA receptors shut — no Ca²⁺ enters, no strengthening occurs. A synapse where the postsynaptic neuron is depolarized but no presynaptic glutamate arrives also fails to open NMDA receptors. Only the specific combination of presynaptic activity and postsynaptic depolarization triggers the Ca²⁺ signal that strengthens that particular synapse. This is the molecular implementation of Hebb's rule — "neurons that fire together wire together" — and it explains why LTP is input-specific: only the active synapses on a depolarized neuron are potentiated, while neighboring inactive synapses on the same neuron are left unchanged.
