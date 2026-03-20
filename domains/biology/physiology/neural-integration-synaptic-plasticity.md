---
id: neural-integration-synaptic-plasticity
title: Neural Integration and Synaptic Plasticity
domain: biology
course: physiology
prerequisites:
- id: synaptic-transmission
  type: hard
- id: long-term-potentiation
  type: hard
builds-toward:
- motor-control-spinal-coordination
- sensory-neural-coding-perception
- hypothalamic-neuroendocrine-integration
tags:
- synaptic
- plasticity
- learning
- memory
- integration
stage: advanced
status: draft
---

# Neural Integration and Synaptic Plasticity

## Core Idea
Neurons integrate signals from many synapses through spatial and temporal summation to decide whether to fire. Synaptic plasticity—the ability of synapses to strengthen or weaken—underlies learning and memory. Both pre- and post-synaptic mechanisms contribute to changes in synaptic efficacy over time and are essential for nervous system adaptation.

## How It's Best Learned
Compare AMPA and NMDA receptor roles in LTP. Use a simple circuit model to trace how multiple inputs summate. Examine how calcium influx triggers molecular cascades that strengthen synapses.

## Common Misconceptions
Assuming all synapses strengthen equally with use—different neurons exhibit different plasticity rules. Thinking LTP is purely postsynaptic when presynaptic factors (transmitter release) also change.

## Explainer

From your study of synaptic transmission and long-term potentiation, you understand that neurons communicate through chemical synapses and that repeated activation can strengthen these connections. Neural integration and synaptic plasticity are the principles that explain how the nervous system turns this basic signaling machinery into computation, learning, and memory.

**Neural integration** is how a single neuron decides whether to fire. A typical neuron in the central nervous system receives thousands of synaptic inputs — some excitatory (producing EPSPs that depolarize the membrane) and some inhibitory (producing IPSPs that hyperpolarize it). The neuron's membrane acts as a leaky integrator: it sums these inputs in two ways. **Spatial summation** occurs when EPSPs from different synapses arrive simultaneously and their depolarizations add together at the axon hillock. **Temporal summation** occurs when a single synapse fires rapidly enough that each EPSP arrives before the previous one has fully decayed. If the combined depolarization at the axon hillock reaches threshold, the neuron fires an action potential. If not, the signal dies. This all-or-none decision is the fundamental computation of the nervous system, and the balance of excitation and inhibition determines what information gets transmitted and what gets filtered out.

**Synaptic plasticity** adds a time dimension to this integration. Rather than having fixed synaptic weights, neurons adjust connection strength based on experience. **Long-term potentiation (LTP)** at glutamatergic synapses is the best-studied example. At resting conditions, AMPA receptors carry the bulk of excitatory current while NMDA receptors remain blocked by magnesium ions. When a synapse is strongly activated — enough to substantially depolarize the postsynaptic membrane — the magnesium block is relieved, NMDA receptors open, and calcium floods into the dendritic spine. This calcium influx activates CaMKII and other kinases that insert additional AMPA receptors into the postsynaptic membrane and enhance their conductance, making the synapse more responsive to future stimulation. The beauty of this mechanism is that it requires *coincidence*: the presynaptic neuron must release glutamate at the same time the postsynaptic neuron is sufficiently depolarized. This coincidence detection is the molecular basis of **Hebb's rule** — "neurons that fire together wire together."

Plasticity is not a one-way street. **Long-term depression (LTD)** weakens synapses that are activated without sufficient postsynaptic depolarization, typically through low-frequency stimulation that produces modest calcium influx activating phosphatases instead of kinases. The balance between LTP and LTD allows neural circuits to continuously recalibrate: frequently co-activated pathways strengthen while unused connections weaken, sharpening the network's representation of relevant information. Presynaptic plasticity further modulates these circuits — changes in neurotransmitter release probability, vesicle pool size, and retrograde signaling (such as endocannabinoids) all adjust synaptic gain. Together, integration and plasticity explain how the same neural hardware can learn a new language, adapt to injury, form associations between a sound and a reward, and forget information that is no longer relevant.
