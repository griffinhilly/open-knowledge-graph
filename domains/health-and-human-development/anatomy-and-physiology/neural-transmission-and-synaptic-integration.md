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
stage: formal-systems
status: draft
---

# Neural Transmission and Synaptic Integration

## Core Idea
Synaptic transmission is unidirectional: action potentials in the presynaptic terminal cause neurotransmitter release, which binds receptors on the postsynaptic membrane. Excitatory transmission depolarizes the postsynaptic cell; inhibitory transmission hyperpolarizes it. Summation—temporal (rapid successive inputs) or spatial (simultaneous inputs from many synapses)—integrates synaptic inputs to determine whether the postsynaptic neuron fires.

## Questions

```yaml
- question: "A neuron receives five simultaneous EPSPs, each depolarizing the membrane by 3 mV. The threshold is 15 mV above resting potential. Which statement best describes what happens at the axon hillock?"
  type: multiple-choice
  options:
    - "No action potential fires because no single EPSP is strong enough"
    - "An action potential fires because the summed depolarization reaches threshold"
    - "An action potential fires because five inputs always exceed threshold"
    - "The neuron fires five separate action potentials, one per EPSP"
  answer: 1
  explanation: "This is spatial summation: simultaneous inputs from multiple synapses are added algebraically at the axon hillock. Five EPSPs of 3 mV each sum to 15 mV, exactly reaching threshold. Option A reflects the common misconception that each EPSP must independently trigger firing. Option C is wrong because five inputs don't automatically exceed threshold — it depends on their amplitudes. Option D confuses the number of inputs with the number of output spikes."

- question: "GABA opens chloride channels on a postsynaptic neuron. Which factor determines whether this produces an inhibitory postsynaptic potential?"
  type: multiple-choice
  options:
    - "Whether GABA is classified as an inhibitory neurotransmitter"
    - "The direction of Cl⁻ flow, determined by the electrochemical gradient across the membrane"
    - "Whether the neuron is excitatory or inhibitory"
    - "The number of GABA molecules released by the presynaptic terminal"
  answer: 1
  explanation: "The sign of the postsynaptic effect depends entirely on which ions flow and in which direction — determined by the electrochemical gradient, not by the neurotransmitter's classification. At typical resting potentials, the Cl⁻ equilibrium potential is near or below resting potential, so Cl⁻ flows in and hyperpolarizes the membrane. Option A gets the causation backward. Option C confuses the identity of the neuron with the effect at a specific synapse."

- question: "Inhibitory postsynaptic potentials (IPSPs) prevent the neuron from ever firing, regardless of how many excitatory inputs arrive."
  type: true-false
  answer: false
  explanation: "IPSPs don't permanently silence a neuron — they make firing less likely by pushing the membrane potential away from threshold. The axon hillock sums all EPSPs and IPSPs algebraically. If excitatory inputs are sufficiently numerous or strong, they can overcome the hyperpolarizing pull of IPSPs and still bring the membrane to threshold. IPSPs are probabilistic influences on the integration, not absolute vetoes."

- question: "The axon hillock integrates excitatory and inhibitory inputs algebraically, firing only when the net depolarization reaches threshold."
  type: true-false
  answer: true
  explanation: "The axon hillock is the decision point of the neuron. It sums all incoming EPSPs (depolarizing) and IPSPs (hyperpolarizing) simultaneously. Because the axon hillock has the lowest threshold for action potential initiation (highest density of voltage-gated Na⁺ channels), it is where this algebraic integration determines whether a spike is generated. This is the core logic of neural integration."

- question: "Why is a single EPSP typically insufficient to fire a neuron, and what two mechanisms allow neurons to integrate inputs and fire reliably?"
  type: short-answer
  answer: "A single EPSP is only a few millivolts in amplitude, well below the ~15–20 mV depolarization needed to reach threshold. Neurons integrate via spatial summation (simultaneous EPSPs from multiple synapses add at the axon hillock) and temporal summation (rapidly repeated inputs from the same synapse overlap before each decays, accumulating depolarization)."
  explanation: "This is the core logic of the synapse as a computational device. Because single EPSPs are subthreshold, the nervous system uses summation to require coincident or repeated activity before producing output. This threshold requirement filters noise and ensures that only coordinated input — not random spontaneous release — drives a neuron to fire."
```

## Explainer

You already know that the action potential is an all-or-nothing electrical event that travels down an axon without decrement. What happens at the end of that axon is fundamentally different in kind — a **chemical synapse** converts the electrical signal into a chemical signal, which is then converted back into electrical information at the postsynaptic cell. This chemical intermediary is not merely a relay; it is a computation. Understanding how the synapse works requires tracking energy through each step: the electrical signal at the terminal, the calcium-triggered **vesicle fusion**, the diffusion of neurotransmitter across the synaptic cleft (a gap of only ~20 nm), and the binding to **ligand-gated ion channels** or metabotropic receptors on the postsynaptic membrane.

When a neurotransmitter binds an ionotropic (ligand-gated) receptor, it opens a channel that allows specific ions to flow down their electrochemical gradients. Whether the result is excitatory or inhibitory depends entirely on which ions flow. **Excitatory postsynaptic potentials (EPSPs)** typically result from the opening of Na⁺ or mixed cation channels: Na⁺ rushes in (because it is both more concentrated outside and attracted by the negative interior), depolarizing the membrane. **Inhibitory postsynaptic potentials (IPSPs)** result from Cl⁻ influx (via GABA_A receptors) or K⁺ efflux (via glycine or GABA_B receptors), hyperpolarizing or clamping the membrane near the Cl⁻ equilibrium potential. The key principle is that direction of flow and ionic selectivity determine the sign of the postsynaptic effect.

A single EPSP is typically far too small to trigger an action potential — its amplitude is millivolts, while the threshold sits ~15–20 mV above the resting potential. This is where **summation** becomes the essential logic operation of the nervous system. **Spatial summation** occurs when inputs from multiple different synapses arrive simultaneously; each EPSP adds to the others at the axon hillock, where the decision to fire is made. **Temporal summation** occurs when the same synapse fires in rapid succession, and the slow decay of each EPSP overlaps with the next. The axon hillock integrates all incoming EPSPs and IPSPs algebraically — excitatory inputs push the membrane toward threshold, inhibitory inputs hold it back. If the summed input at the hillock reaches threshold, an action potential fires. If not, it does not.

This integration logic explains a great deal about neural circuit behavior. Inhibitory interneurons can veto a circuit's output with precise timing, creating **feedforward inhibition** (arriving before excitation) or **feedback inhibition** (triggered by the circuit's own output). **Presynaptic inhibition** is a more subtle mechanism: an axoaxonic synapse can hyperpolarize the terminal of an excitatory neuron, reducing calcium influx and thus neurotransmitter release — effectively turning down the volume on an input before it even reaches the postsynaptic cell. These mechanisms give neural circuits fine-grained control over information flow, enabling functions like sensory filtering, contrast enhancement, and gain control.

The behavior of any single synapse is also not fixed — **synaptic plasticity** means that the strength of a connection changes with use. Short-term changes arise from depletion of vesicle pools (synaptic depression) or calcium accumulation facilitating more release (synaptic facilitation). Long-term changes like **long-term potentiation (LTP)** involve structural and molecular modifications at the synapse and underlie learning and memory. Understanding synaptic integration gives you the cellular substrate for understanding how experience reshapes the brain: not through rewiring the map of connections wholesale, but through adjusting the weight of each synaptic vote in the constant polling that every neuron conducts at its axon hillock.

