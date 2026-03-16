---
id: synaptic-plasticity-long-term-potentiation-depression
title: 'Synaptic Plasticity: Long-Term Potentiation and Depression'
domain: health-and-human-development
course: anatomy-and-physiology
prerequisites:
- id: synaptic-transmission-neurotransmitter-dynamics
  type: hard
- id: neural-anatomy-and-organization
  type: hard
builds-toward:
- memory-consolidation
tags:
- synaptic-plasticity
- LTP
- LTD
stage: abstract-reasoning
status: draft
---

# Synaptic Plasticity: Long-Term Potentiation and Depression

## Core Idea
Synaptic strength changes through activity-dependent plasticity: long-term potentiation (LTP) strengthens synapses when postsynaptic stimulation enables NMDA-mediated Ca²⁺ influx, activating kinases that phosphorylate and insert AMPA receptors. Long-term depression (LTD) weakens synapses through opposite mechanisms. The pattern and timing of pre- and postsynaptic activity determines whether potentiation or depression occurs, encoding stimulus relationships and enabling learning.

## Explainer

From your study of synaptic transmission, you know that a synapse communicates by releasing neurotransmitter into a cleft, where it binds receptors on the postsynaptic membrane and alters ion conductance. **Synaptic plasticity** is the capacity of that communication to be strengthened or weakened based on recent activity — a mechanism that lets neural circuits change in response to experience. The key principle is that synaptic strength is not fixed hardware; it is continuously adjustable software written by patterns of neural activity.

**Long-term potentiation (LTP)** is triggered by high-frequency or coincident pre- and postsynaptic activity, and its mechanism hinges on a molecular coincidence detector: the **NMDA receptor**. Like AMPA receptors, NMDA receptors are glutamate-gated ion channels, but with a critical difference: at resting membrane potentials, a magnesium ion physically blocks the channel even when glutamate is bound. The Mg²⁺ block is only relieved when the postsynaptic membrane is already depolarized — which happens when AMPA receptors nearby are already activated. This means the NMDA receptor opens only when glutamate arrives *and* the postsynaptic cell is already active — it detects the coincidence of pre- and postsynaptic firing. When both conditions are met, Ca²⁺ flows through the NMDA channel, activating protein kinases (particularly CaMKII) that phosphorylate existing AMPA receptors and trigger insertion of additional AMPA receptors into the postsynaptic membrane. More AMPA receptors means a larger response to the same presynaptic signal — the synapse is potentiated. This potentiation can last hours, days, or permanently.

**Long-term depression (LTD)** is the mirror process. Weak or asynchronous stimulation produces modest Ca²⁺ influx through NMDA receptors — lower amplitude, slower time course than LTP-triggering stimulation. This low-level Ca²⁺ signal preferentially activates phosphatases rather than kinases, which dephosphorylate AMPA receptors and trigger their internalization (removal from the membrane). The synapse becomes weaker. The same receptor, the same ion, the same channel — but amplitude and timing determine whether the outcome is potentiation or depression.

This timing-dependence has a precise formulation called **spike-timing-dependent plasticity (STDP)**: if the presynaptic neuron fires just before the postsynaptic neuron (pre then post), LTP results; if the order reverses (post then pre), LTD results. The logic is causal: a synapse strengthens when its activity appears to have caused the postsynaptic response, and weakens when it fired too late to have been the cause. This elegantly instantiates the Hebbian maxim that "neurons that fire together wire together" — and its corollary, neurons that fire out of phase weaken their connection. The asymmetric timing window, typically tens of milliseconds, is the biological implementation of associative learning at the cellular scale.

The link to memory consolidation — your builds-toward topic — lies in the hippocampus, where LTP is the most studied and best-documented example. The formation of new explicit memories depends on hippocampal synaptic strengthening driven by these same NMDA/AMPA mechanisms. Blocking NMDA receptors in the hippocampus impairs new memory formation without affecting retrieval of old memories, demonstrating that LTP is not just a laboratory curiosity but the actual cellular substrate of learning.
