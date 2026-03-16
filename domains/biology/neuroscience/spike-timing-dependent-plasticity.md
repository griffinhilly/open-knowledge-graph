---
id: spike-timing-dependent-plasticity
title: Spike-Timing-Dependent Plasticity
domain: biology
course: neuroscience
prerequisites:
- id: long-term-potentiation
  type: hard
- id: long-term-depression
  type: hard
- id: nmda-receptor-structure
  type: hard
builds-toward:
- hebbian-learning
- circuit-development
- learning-memory
tags:
- stdp
- spike-timing
- causality
stage: advanced
status: draft
---

# Spike-Timing-Dependent Plasticity

## Core Idea
Spike-timing-dependent plasticity is Hebbian learning where timing of presynaptic and postsynaptic spikes determines synaptic change: presynaptic firing before postsynaptic (causal, positive Δt) causes LTP; reverse timing causes LTD. The learning window spans tens of milliseconds and reflects NMDA receptor-mediated calcium signaling.

## How It's Best Learned
Use voltage clamp with precise spike pairings. Plot plasticity magnitude vs. spike timing.

## Common Misconceptions
STDP always follows one rule—rules vary across synapses. All synapses use STDP—it's one of several plasticity mechanisms.

## Explainer

You already know that LTP strengthens synapses and LTD weakens them, and that NMDA receptors act as coincidence detectors requiring both glutamate binding and postsynaptic depolarization to open. **Spike-timing-dependent plasticity (STDP)** adds a crucial dimension to this picture: it is not just *whether* two neurons are active together that matters, but *the precise order and timing* of their firing. This transforms Hebb's vague "fire together, wire together" principle into a quantitative rule with a direction.

The core STDP rule is elegant. If the **presynaptic neuron fires first** and the **postsynaptic neuron fires shortly after** (within roughly 10–20 milliseconds), the synapse is strengthened — this is LTP. The logic is causal: the presynaptic cell may have *caused* the postsynaptic cell to fire, so the connection is reinforced. If the order is reversed — postsynaptic fires first, then presynaptic — the synapse is weakened via LTD. Here, the presynaptic input arrived too late to have contributed to the postsynaptic spike, so it is pruned. The magnitude of the change depends on the **time interval (Δt)**: the closer together the spikes, the larger the effect; at intervals beyond about 40–50 milliseconds, the plasticity window closes and no change occurs.

The mechanism relies directly on the NMDA receptor properties you studied. When the presynaptic spike arrives first, it releases glutamate that binds NMDA receptors. The postsynaptic spike, arriving milliseconds later, provides the depolarization needed to expel the Mg²⁺ block from the NMDA channel. The result is a large, fast calcium influx that activates **CaMKII** and other kinases, driving AMPA receptor insertion and LTP. When the timing is reversed, the postsynaptic depolarization has already faded by the time glutamate arrives, so NMDA receptors open under weaker depolarization conditions. The resulting modest, slow calcium signal preferentially activates **phosphatases** (like calcineurin) rather than kinases, triggering AMPA receptor internalization and LTD. The same receptor, responding to the same two signals, produces opposite outcomes depending purely on temporal order — calcium amplitude and kinetics are the switch.

STDP has profound computational implications. It means that synapses automatically detect and reinforce **causal relationships** in neural activity: inputs that reliably predict a neuron's firing get strengthened, while inputs that consistently arrive too late get weakened. This is exactly the kind of learning rule needed for the brain to extract temporal structure from sensory experience — to learn that one sound predicts another, that a visual motion pattern implies a trajectory, or that a sequence of muscle activations produces a coordinated movement. However, STDP is not a universal law. Different synapse types and brain regions show variations: some inhibitory synapses have inverted STDP rules (reversed timing produces LTP), and some synapses show symmetric windows where timing order does not matter. The "classic" STDP curve — asymmetric, with LTP for pre-before-post and LTD for post-before-pre — is the most common pattern at excitatory cortical and hippocampal synapses, but the brain uses multiple plasticity rules tuned to the computational needs of each circuit.
