---
id: synaptic-transmission-neurotransmitter-release
title: Synaptic Transmission and Neurotransmitter Release
domain: psychology
course: biological-psychology
prerequisites:
- id: action-potential-and-neural-signaling
  type: hard
- id: neurotransmitter-synthesis-storage
  type: hard
- id: synaptic-vesicle-release-exocytosis
  type: hard
- id: exocytosis-snare-proteins-membrane-fusion
  type: hard
builds-toward:
- receptor-subtypes-and-signaling
- synaptic-plasticity-mechanisms
- gaba-glutamate-neurotransmission-balance
tags:
- synapses
- communication
- vesicle-dynamics
stage: formal-systems
status: draft
---

# Synaptic Transmission and Neurotransmitter Release

## Core Idea
Synaptic transmission couples electrical signals in the presynaptic neuron to chemical release of neurotransmitters, which then act on postsynaptic receptors. Calcium influx through voltage-gated channels triggers SNARE-mediated exocytosis of vesicles. The strength of transmission depends on presynaptic calcium, vesicle availability, and postsynaptic receptor density.

## Explainer

The fundamental challenge the nervous system faces is this: neurons communicate electrically within themselves but chemically between each other. The synapse is where the handoff happens — and understanding that handoff requires connecting the electrical story you already know (action potentials, membrane potential) to a precise molecular machine. Think of synaptic transmission as a triggered release system: the electrical signal sets a timer, and when the impulse arrives, a burst of chemistry follows.

When an **action potential** travels down the axon and reaches the axon terminal, it depolarizes the membrane of the presynaptic bouton. Embedded in that terminal membrane are **voltage-gated calcium channels** — channels that stay closed at resting potential but open in response to depolarization. Calcium (Ca²⁺) floods in from the extracellular space, where its concentration is much higher. This calcium influx is the critical trigger. The faster and larger the calcium entry, the more neurotransmitter gets released. Calcium concentration directly controls the probability that a synaptic vesicle will fuse with the membrane.

This is where your knowledge of SNARE proteins and exocytosis connects. Synaptic vesicles — membrane-bound sacs loaded with neurotransmitter molecules during synthesis — are primed near the active zone, positioned at the presynaptic membrane but not yet fused. The **SNARE complex** (involving synaptobrevin on the vesicle, syntaxin and SNAP-25 on the target membrane) physically zippers together when calcium binds to synaptotagmin, pulling the vesicle into the plasma membrane. The vesicle opens, its contents spill into the **synaptic cleft**, and neurotransmitter molecules diffuse across the narrow gap to postsynaptic receptors. The whole sequence from action potential to transmitter release takes less than a millisecond.

**Transmission strength** is not fixed — it is dynamically regulated at each of three points. First, presynaptic calcium: anything that amplifies or reduces calcium entry (such as modulatory receptors on the terminal) will scale up or down how much neurotransmitter is released per action potential. Second, **vesicle availability**: the readily-releasable pool of docked vesicles near the active zone is finite. Rapid repeated firing can deplete this pool faster than vesicles are replenished, causing short-term synaptic depression. Third, **postsynaptic receptor density**: more receptors means more response for the same amount of transmitter. This three-way control — calcium, vesicle supply, receptor count — gives the synapse remarkable dynamic range and is the molecular substrate for forms of plasticity you will study next.
