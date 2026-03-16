---
id: short-term-plasticity-presynaptic
title: 'Short-Term Synaptic Plasticity: Facilitation and Depression'
domain: biology
course: neuroscience
prerequisites:
- id: synaptic-transmission
  type: hard
- id: voltage-clamp-recording
  type: soft
builds-toward:
- critical-developmental-periods
tags:
- synaptic-plasticity
- presynaptic-mechanisms
- temporal-dynamics
stage: advanced
status: draft
---

# Short-Term Synaptic Plasticity: Facilitation and Depression

## Core Idea
Short-term plasticity operates on timescales of 100 ms to seconds through presynaptic (residual Ca2+, release probability changes) and postsynaptic (receptor desensitization) mechanisms. Synaptic facilitation increases transmission during high-frequency activity, while depression decreases it, allowing neurons to encode temporal patterns of input.

## Explainer

You already understand that synaptic transmission involves calcium-triggered vesicle fusion and that voltage-clamp recording allows you to measure synaptic currents precisely. **Short-term plasticity** refers to changes in synaptic strength that last from tens of milliseconds to a few minutes — far shorter than the hours-to-lifetime changes of LTP and LTD. These rapid, reversible adjustments mean that synapses are not fixed-gain relays; instead, the strength of a synapse depends on its recent history of activity. This gives neural circuits a built-in ability to filter, amplify, or adapt to temporal patterns in their inputs.

**Synaptic facilitation** occurs when a second action potential arrives shortly after the first and produces a larger postsynaptic response. The mechanism is elegantly simple: calcium. When the first action potential triggers Ca²⁺ influx into the presynaptic terminal, the calcium is cleared by pumps and buffers, but not instantaneously — a residual calcium signal lingers for tens of milliseconds. When the second action potential arrives during this window, its calcium influx adds to the residual calcium, producing a higher peak Ca²⁺ concentration. Because vesicle fusion probability is a steep, nonlinear function of calcium concentration (roughly proportional to Ca²⁺ raised to the fourth power), even a modest increase in peak calcium can dramatically increase the number of vesicles released. The result is a progressively larger postsynaptic response with each successive stimulus in a train — the synapse "facilitates."

**Synaptic depression** is the opposite: repeated stimulation produces progressively smaller responses. The dominant presynaptic mechanism is **vesicle depletion** — each round of release draws from a limited pool of readily releasable vesicles, and if stimulation is fast enough, release outpaces replenishment. Synapses with a high initial release probability are especially prone to depression because they empty their vesicle pool quickly. Postsynaptic receptor desensitization also contributes: prolonged or repeated exposure to neurotransmitter causes ionotropic receptors to enter a non-conducting conformation, reducing the postsynaptic response even if transmitter release is constant. In practice, most synapses show a mixture of facilitation and depression, with the balance depending on the synapse type, initial release probability, and stimulation frequency.

The functional consequences of short-term plasticity are profound. A **facilitating synapse** acts as a high-pass filter — it responds weakly to isolated, low-frequency inputs but strongly to bursts of high-frequency activity. This means it selectively transmits information carried in bursts. A **depressing synapse** acts as a low-pass or adaptation filter — it responds strongly to the onset of activity but then attenuates, effectively signaling changes or novelty rather than sustained input. Many sensory systems exploit depressing synapses to implement adaptation: a constant stimulus produces a diminishing neural response, freeing the circuit to detect new changes against the background. In the auditory brainstem, short-term depression at the calyx of Held synapse helps neurons encode the onset timing of sounds with microsecond precision, discarding sustained input that carries less spatial information. Short-term plasticity thus transforms synapses from simple connectors into temporal filters that shape what information passes through a circuit.
