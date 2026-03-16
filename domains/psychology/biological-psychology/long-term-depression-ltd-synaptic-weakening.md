---
id: long-term-depression-ltd-synaptic-weakening
title: 'Long-Term Depression (LTD): Synaptic Weakening'
domain: psychology
course: biological-psychology
prerequisites:
- id: synaptic-transmission-neurotransmitter-release
  type: hard
- id: long-term-potentiation-ltp-memory-encoding
  type: soft
- id: long-term-depression
  type: hard
- id: ion-channels-and-neural-excitability
  type: hard
- id: calcium-signaling-neurons
  type: hard
builds-toward:
- memory-consolidation-systems
- learning-and-experience-dependent-plasticity
tags:
- plasticity
- learning
- synaptic-weakening
stage: formal-systems
status: draft
---

# Long-Term Depression (LTD): Synaptic Weakening

## Core Idea
Long-term depression is an activity-dependent decrease in synaptic strength that complements LTP. Low-frequency stimulation or postsynaptic activation alone (without strong presynaptic input) triggers modest calcium elevation through NMDA receptors, activating phosphatases that remove AMPA receptors. LTD is essential for circuit refinement, prevention of runaway excitation, and forgetting of irrelevant information.

## Explainer

You already understand LTP — the synaptic strengthening that encodes memories through NMDA receptor activation, calcium influx, and AMPA receptor insertion. LTD is the mirror process: it *weakens* synapses. The key to understanding both is not which molecules are recruited, but *how much* calcium enters the postsynaptic cell. The same NMDA receptors are involved, but the outcome depends on the calcium concentration they produce.

The **calcium threshold model** captures this elegantly. High-frequency presynaptic stimulation drives large calcium spikes, which activate kinases (like CaMKII) that insert more AMPA receptors into the synapse — that's LTP. But low-frequency stimulation, or postsynaptic activation that occurs without synchronized strong presynaptic input, produces only a modest calcium rise. This lower calcium level preferentially activates **phosphatases** (like protein phosphatase 1 and calcineurin) rather than kinases. Phosphatases do the opposite of kinases: they remove phosphate groups from AMPA receptors, triggering their **internalization** — the receptors are removed from the synapse membrane and stored inside the cell. With fewer AMPA receptors at the synapse, the postsynaptic response to subsequent stimulation is weaker. The synapse has been depressed.

The biological logic of LTD becomes clear when you consider what would happen without it. If LTP only ever strengthened synapses, the system would saturate — every synapse would max out, and the network would lose its capacity to encode new distinctions. LTD provides the complementary "write-down" operation. It is especially prominent in the cerebellum, where it underlies motor learning: when a climbing fiber (error signal) co-activates a cerebellar Purkinje cell alongside a weak parallel fiber input, that parallel fiber synapse is depressed. This is how the cerebellum adjusts motor programs — repeatedly activating unhelpful pathways weakens them while correct pathways are strengthened.

At the systems level, LTD contributes to **synaptic homeostasis** and **circuit refinement** during development. During sleep, for instance, widespread synaptic downscaling (a form of global LTD) is thought to prevent network saturation and consolidate the most important memories by weakening weaker synaptic traces. The result is a nervous system that is not simply an accumulation of reinforced pathways, but a dynamically sculpted network that can forget irrelevant detail while preserving meaningful signal.
