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

## Questions

```yaml
- question: "A presynaptic neuron fires and releases glutamate onto a postsynaptic neuron that is at resting membrane potential (−70 mV). What happens at the synapse?"
  type: multiple-choice
  options:
    - "Both AMPA and NMDA receptors open, Ca²⁺ enters the cell, and LTP is induced"
    - "AMPA receptors open and produce a small depolarization, but NMDA receptors remain blocked by Mg²⁺ — no Ca²⁺ enters and no LTP is triggered"
    - "NMDA receptors open immediately upon glutamate binding regardless of membrane voltage, but LTP requires repeated activation"
    - "Neither receptor opens at resting potential; glutamate alone is insufficient without a co-agonist released from the postsynaptic cell"
  answer: 1
  explanation: "At resting membrane potential, a Mg²⁺ ion sits in the NMDA receptor pore and blocks ion flow even when glutamate is bound. AMPA receptors have no such voltage dependence and open normally, producing an EPSP. The Mg²⁺ block is only relieved when the postsynaptic membrane depolarizes to roughly −40 mV or above — at which point electrostatic repulsion expels the Mg²⁺. Without this depolarization, the NMDA receptor is sealed regardless of how much glutamate is present, so no Ca²⁺ enters and no LTP occurs."

- question: "What makes the NMDA receptor a 'molecular coincidence detector' for Hebbian learning?"
  type: multiple-choice
  options:
    - "It binds both glutamate and GABA, detecting convergent excitatory and inhibitory signals from multiple presynaptic neurons"
    - "It requires both glutamate binding (signaling presynaptic activity) and postsynaptic depolarization (signaling postsynaptic activity) simultaneously — the channel opens only when both conditions are met"
    - "It activates only when the postsynaptic neuron has already fired an action potential within the preceding 100 milliseconds"
    - "It detects coincident Ca²⁺ and Na⁺ influx from neighboring synapses on the same dendritic branch"
  answer: 1
  explanation: "The Mg²⁺ block is the physical mechanism of coincidence detection. Glutamate is the 'presynaptic signal' (the pre-neuron fired). Postsynaptic depolarization is the 'postsynaptic signal' (the post-neuron is active). Only when both are present simultaneously does the Mg²⁺ leave the pore and Ca²⁺ flow in. This directly implements Hebb's rule: 'neurons that fire together wire together.' A presynaptic neuron firing onto a quiet postsynaptic neuron leaves no lasting trace; a synapse active when the postsynaptic cell is already depolarized gets strengthened."

- question: "NMDA receptor-mediated Ca²⁺ influx is necessary for LTP because Ca²⁺ activates CaMKII, which drives insertion of additional AMPA receptors into the postsynaptic membrane."
  type: true-false
  answer: true
  explanation: "This is the established molecular sequence for LTP induction. Ca²⁺ entering through NMDA receptors binds calmodulin, which activates CaMKII (calcium/calmodulin-dependent protein kinase II). CaMKII phosphorylates existing AMPA receptors, increasing their conductance, and also signals for the insertion of new AMPA receptors from intracellular stores into the postsynaptic membrane. The net result is more AMPA receptors at the synapse, producing a larger EPSP in response to the same presynaptic release — this is LTP. Blocking NMDA receptors (e.g., with AP5) prevents LTP."

- question: "NMDA receptors are blocked by Mg²⁺ only at strongly depolarized membrane potentials; at resting potential they are freely permeable to Ca²⁺ whenever glutamate is bound."
  type: true-false
  answer: false
  explanation: "This is exactly backwards. At resting membrane potential (around −70 mV), Mg²⁺ sits in the pore and blocks ion flow. The block is *relieved* at depolarized potentials (above roughly −40 mV), where the positive membrane potential pushes the positively charged Mg²⁺ out of the pore. So NMDA receptors are open at depolarized potentials and blocked at rest. This counterintuitive feature — a channel that opens when the membrane is depolarized rather than closing — is what makes NMDA receptors useful as coincidence detectors."

- question: "Explain why long-term potentiation (LTP) is input-specific: why does strong activation of one synapse onto a neuron strengthen that synapse but not neighboring synapses on the same dendrite?"
  type: short-answer
  answer: "LTP is input-specific because NMDA receptors only open at synapses where both glutamate and local postsynaptic depolarization are present simultaneously. At an inactive synapse on the same neuron, no glutamate is released, so even if the postsynaptic cell is depolarized, there is no glutamate to bind the NMDA receptors — they stay shut. No Ca²⁺ enters, no CaMKII is activated, and no AMPA receptors are added. Only the specific active synapse, where both conditions coincide, receives the Ca²⁺ signal that drives potentiation."
  explanation: "This input-specificity is what makes LTP a plausible mechanism for associative memory — it can strengthen a specific pathway without indiscriminately boosting all synaptic connections onto a neuron. The NMDA receptor's requirement for local glutamate (not just global depolarization) confines the plasticity signal to the synapse where presynaptic and postsynaptic activity converged. This is the molecular implementation of the Hebbian learning rule at the synapse-specific level."
```

## Explainer

You already understand that long-term potentiation (LTP) is a lasting increase in synaptic strength following high-frequency stimulation, and that it is a leading cellular model of learning and memory. The NMDA receptor is the molecular device that makes LTP possible — it is the synapse's **coincidence detector**, and understanding how it works reveals why synapses strengthen only when the right conditions are met simultaneously.

Most excitatory synapses in the brain use glutamate as their neurotransmitter and have two major types of glutamate receptor sitting in the postsynaptic membrane: **AMPA receptors** and **NMDA receptors**. AMPA receptors are straightforward — glutamate binds, the channel opens, Na⁺ flows in, and the membrane depolarizes. They mediate the fast excitatory postsynaptic potential you observe in normal synaptic transmission. NMDA receptors are different in a crucial way: even when glutamate binds, the channel remains blocked by a Mg²⁺ ion sitting in the pore. This **voltage-dependent magnesium block** means that at resting membrane potential (around −70 mV), NMDA receptors are effectively sealed shut despite having glutamate bound. Only when the postsynaptic membrane is sufficiently depolarized — typically to around −40 mV or above — does the Mg²⁺ ion get expelled from the pore by electrostatic repulsion, allowing the channel to conduct.

This dual requirement — glutamate binding *and* postsynaptic depolarization — is what makes the NMDA receptor a coincidence detector. Glutamate in the synaptic cleft signals that the presynaptic neuron has fired. Depolarization of the postsynaptic membrane signals that the postsynaptic neuron is also active (either firing or receiving strong input from other synapses). The NMDA receptor opens only when both conditions are true simultaneously. When it does open, it admits not just Na⁺ but also a substantial influx of **Ca²⁺ ions**. This calcium entry is the key signaling event: Ca²⁺ activates intracellular enzymes — particularly **CaMKII** (calcium/calmodulin-dependent protein kinase II) — which phosphorylate existing AMPA receptors to increase their conductance and drive the insertion of additional AMPA receptors into the postsynaptic membrane. More AMPA receptors mean a larger postsynaptic response to the same amount of glutamate, which is the expression of LTP.

The beauty of this mechanism is its selectivity. A synapse that releases glutamate onto a quiescent postsynaptic neuron will activate AMPA receptors and produce a small depolarization, but the Mg²⁺ block will keep NMDA receptors shut — no Ca²⁺ enters, no strengthening occurs. A synapse where the postsynaptic neuron is depolarized but no presynaptic glutamate arrives also fails to open NMDA receptors. Only the specific combination of presynaptic activity and postsynaptic depolarization triggers the Ca²⁺ signal that strengthens that particular synapse. This is the molecular implementation of Hebb's rule — "neurons that fire together wire together" — and it explains why LTP is input-specific: only the active synapses on a depolarized neuron are potentiated, while neighboring inactive synapses on the same neuron are left unchanged.
