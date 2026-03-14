---
id: synaptic-transmission
title: Synaptic Transmission
domain: biology
course: physiology
prerequisites:
- id: action-potential
  type: hard
- id: cell-signaling-intro
  type: hard
builds-toward:
- neuromuscular-junction
- nervous-system-overview
tags:
- synapse
- neurotransmitter
- chemical synapse
- receptor
- EPSP
- IPSP
stage: formal-systems
status: validated
---

# Synaptic Transmission

## Core Idea
Synaptic transmission converts an electrical signal in a presynaptic neuron into a chemical signal that crosses the synaptic cleft and is reconverted to electrical or biochemical signals in the postsynaptic cell. When an action potential reaches an axon terminal, voltage-gated Ca²⁺ channels open and Ca²⁺ influx triggers exocytosis of neurotransmitter-loaded vesicles. Neurotransmitters diffuse across the ~20 nm cleft and bind to postsynaptic receptors: ionotropic receptors open ion channels directly (fast, milliseconds), while metabotropic receptors activate G-protein cascades (slow, seconds to minutes). The signal is terminated by reuptake into the presynaptic terminal, enzymatic degradation, or diffusion away from the cleft.

## How It's Best Learned
Trace the seven-step sequence: AP arrives → Ca²⁺ enters → vesicles dock and fuse → neurotransmitter released → binds receptor → postsynaptic current flows → signal terminated. Compare an excitatory synapse (glutamate → AMPA receptor → Na⁺ influx → depolarization → EPSP) vs. an inhibitory synapse (GABA → GABA-A receptor → Cl⁻ influx → hyperpolarization → IPSP). Explain how spatial and temporal summation at the axon hillock determines whether an action potential fires.

## Common Misconceptions
- The chemical step at the synapse is not simply a relay — it introduces gain control, modulation, and plasticity that pure electrical transmission cannot provide.
- Inhibitory synapses do not silence the postsynaptic cell passively; they actively hyperpolarize it, requiring stronger excitatory input to reach threshold.
- One neurotransmitter can be excitatory or inhibitory depending on the receptor it binds — GABA is inhibitory at GABA-A but can be excitatory in early development.
