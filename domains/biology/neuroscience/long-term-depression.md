---
id: long-term-depression
title: Long-Term Depression
domain: biology
course: neuroscience
prerequisites:
- id: postsynaptic-currents-epsc-ipsc
  type: hard
- id: ionotropic-vs-metabotropic-receptors
  type: hard
builds-toward:
- spike-timing-dependent-plasticity
tags:
- synaptic-plasticity
- learning
stage: advanced
status: draft
---

# Long-Term Depression

## Core Idea
Lasting decrease from low-frequency stimulation. Moderate Ca2+ elevation activates phosphatases (calcineurin) that remove AMPA receptors, weakening transmission.

## Explainer

From your understanding of postsynaptic currents and the distinction between ionotropic and metabotropic receptors, you know that synaptic transmission produces measurable electrical responses and that different receptor types trigger different intracellular signaling pathways. **Long-term depression (LTD)** is the complementary process to long-term potentiation (LTP) — while LTP strengthens synapses, LTD weakens them. Both are essential: a brain that could only strengthen synapses would quickly saturate, with every connection at maximum strength and no ability to discriminate signal from noise. LTD provides the erasure, refinement, and forgetting that keep neural circuits functional.

The key to understanding LTD lies in **calcium concentration**. Both LTP and LTD are triggered by calcium entering the postsynaptic neuron through NMDA receptors, but the *amount* of calcium determines which direction the synapse moves. High-frequency stimulation (like a burst of rapid firing) produces large, fast calcium transients that activate **kinases** — enzymes like CaMKII that add phosphate groups to proteins. These kinases drive AMPA receptor insertion into the postsynaptic membrane, strengthening the synapse (LTP). Low-frequency stimulation (typically around 1 Hz for several minutes) produces a modest, sustained calcium elevation that instead activates **phosphatases** — enzymes like **calcineurin** (protein phosphatase 2B) and PP1 that remove phosphate groups. These phosphatases trigger the internalization of AMPA receptors: the receptors are pulled out of the postsynaptic membrane via endocytosis and either recycled or degraded. Fewer AMPA receptors in the membrane means smaller excitatory postsynaptic currents in response to the same amount of glutamate release — the synapse has been weakened.

This calcium-threshold model — sometimes called the **BCM theory** after Bienenstock, Cooper, and Munro — provides an elegant explanation for bidirectional plasticity at a single synapse. The postsynaptic neuron effectively reads its own calcium signal to decide whether to strengthen or weaken: brief, intense calcium means "this connection is important, keep it," while prolonged, moderate calcium means "this connection is not contributing usefully, weaken it." The threshold between LTP and LTD is itself adjustable through **metaplasticity** — a synapse's recent history of activity shifts the threshold, preventing runaway potentiation or depression.

LTD is not merely a laboratory curiosity — it plays critical roles in real neural computation. In the cerebellum, LTD at parallel fiber–Purkinje cell synapses is the primary mechanism for **motor learning**: when a movement produces an error, climbing fiber signals trigger LTD that weakens the synaptic connections responsible for the incorrect motor command. In the hippocampus, LTD contributes to memory flexibility by allowing old associations to be overwritten with new ones. During development, LTD helps refine neural circuits by weakening inappropriate connections — for example, eliminating synapses that carry poorly correlated visual input during the critical period of visual cortex development. Without LTD, the brain would be a one-way ratchet, accumulating synaptic strength without the ability to prune, refine, or adapt.
