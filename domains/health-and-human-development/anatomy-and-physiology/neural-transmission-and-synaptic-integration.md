---
id: neural-transmission-and-synaptic-integration
title: Neural Transmission and Synaptic Integration
domain: health-and-human-development
course: anatomy-and-physiology
prerequisites:
- id: neural-anatomy-and-organization
  type: hard
- id: action-potential
  type: hard
- id: synaptic-transmission
  type: hard
- id: neurotransmitter-synthesis-storage
  type: soft
builds-toward:
- sensory-transduction-and-encoding
- motor-control-and-neural-activation
- autonomic-nervous-system-physiology
tags:
- synapse
- neurotransmitter
- epsc
- ipsc
- summation
stage: abstract-reasoning
status: draft
---

# Neural Transmission and Synaptic Integration

## Core Idea
Synaptic transmission is unidirectional: action potentials in the presynaptic terminal cause neurotransmitter release, which binds receptors on the postsynaptic membrane. Excitatory transmission depolarizes the postsynaptic cell; inhibitory transmission hyperpolarizes it. Summation—temporal (rapid successive inputs) or spatial (simultaneous inputs from many synapses)—integrates synaptic inputs to determine whether the postsynaptic neuron fires.

## Explainer

You already know that the action potential is an all-or-nothing electrical event that travels down an axon without decrement. What happens at the end of that axon is fundamentally different in kind — a **chemical synapse** converts the electrical signal into a chemical signal, which is then converted back into electrical information at the postsynaptic cell. This chemical intermediary is not merely a relay; it is a computation. Understanding how the synapse works requires tracking energy through each step: the electrical signal at the terminal, the calcium-triggered **vesicle fusion**, the diffusion of neurotransmitter across the synaptic cleft (a gap of only ~20 nm), and the binding to **ligand-gated ion channels** or metabotropic receptors on the postsynaptic membrane.

When a neurotransmitter binds an ionotropic (ligand-gated) receptor, it opens a channel that allows specific ions to flow down their electrochemical gradients. Whether the result is excitatory or inhibitory depends entirely on which ions flow. **Excitatory postsynaptic potentials (EPSPs)** typically result from the opening of Na⁺ or mixed cation channels: Na⁺ rushes in (because it is both more concentrated outside and attracted by the negative interior), depolarizing the membrane. **Inhibitory postsynaptic potentials (IPSPs)** result from Cl⁻ influx (via GABA_A receptors) or K⁺ efflux (via glycine or GABA_B receptors), hyperpolarizing or clamping the membrane near the Cl⁻ equilibrium potential. The key principle is that direction of flow and ionic selectivity determine the sign of the postsynaptic effect.

A single EPSP is typically far too small to trigger an action potential — its amplitude is millivolts, while the threshold sits ~15–20 mV above the resting potential. This is where **summation** becomes the essential logic operation of the nervous system. **Spatial summation** occurs when inputs from multiple different synapses arrive simultaneously; each EPSP adds to the others at the axon hillock, where the decision to fire is made. **Temporal summation** occurs when the same synapse fires in rapid succession, and the slow decay of each EPSP overlaps with the next. The axon hillock integrates all incoming EPSPs and IPSPs algebraically — excitatory inputs push the membrane toward threshold, inhibitory inputs hold it back. If the summed input at the hillock reaches threshold, an action potential fires. If not, it does not.

This integration logic explains a great deal about neural circuit behavior. Inhibitory interneurons can veto a circuit's output with precise timing, creating **feedforward inhibition** (arriving before excitation) or **feedback inhibition** (triggered by the circuit's own output). **Presynaptic inhibition** is a more subtle mechanism: an axoaxonic synapse can hyperpolarize the terminal of an excitatory neuron, reducing calcium influx and thus neurotransmitter release — effectively turning down the volume on an input before it even reaches the postsynaptic cell. These mechanisms give neural circuits fine-grained control over information flow, enabling functions like sensory filtering, contrast enhancement, and gain control.

The behavior of any single synapse is also not fixed — **synaptic plasticity** means that the strength of a connection changes with use. Short-term changes arise from depletion of vesicle pools (synaptic depression) or calcium accumulation facilitating more release (synaptic facilitation). Long-term changes like **long-term potentiation (LTP)** involve structural and molecular modifications at the synapse and underlie learning and memory. Understanding synaptic integration gives you the cellular substrate for understanding how experience reshapes the brain: not through rewiring the map of connections wholesale, but through adjusting the weight of each synaptic vote in the constant polling that every neuron conducts at its axon hillock.

