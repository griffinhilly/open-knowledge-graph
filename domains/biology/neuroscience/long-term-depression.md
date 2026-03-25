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
- id: dendritic-spine-plasticity
  type: soft
builds-toward:
- spike-timing-dependent-plasticity
tags:
- synaptic-plasticity
- learning
stage: expert
status: validated
---
# Long-Term Depression

## Core Idea
Lasting decrease from low-frequency stimulation. Moderate Ca2+ elevation activates phosphatases (calcineurin) that remove AMPA receptors, weakening transmission.

## Questions

```yaml
- question: "A synapse receives high-frequency stimulation, producing large, rapid calcium transients. Another synapse receives low-frequency stimulation (1 Hz for several minutes), producing a moderate, sustained calcium elevation. What determines which synapse undergoes LTP vs LTD?"
  type: multiple-choice
  options:
    - "The type of receptor activated — AMPA receptors drive LTP while NMDA receptors drive LTD"
    - "Whether calcium enters at all — LTP requires calcium but LTD does not"
    - "The amount and pattern of calcium elevation — high transients activate kinases (LTP) while moderate sustained elevation activates phosphatases (LTD)"
    - "The direction of the change — LTP is always initiated by the presynaptic cell while LTD requires a postsynaptic signal"
  answer: 2
  explanation: "The BCM threshold model: both LTP and LTD are triggered by calcium entering through NMDA receptors, but the amount of calcium determines the outcome. Large, rapid calcium transients from high-frequency stimulation activate CaMKII and other kinases, inserting AMPA receptors and strengthening the synapse (LTP). Moderate, sustained calcium from low-frequency stimulation activates calcineurin and PP1 (phosphatases), removing AMPA receptors and weakening the synapse (LTD). The calcium signal itself encodes the plasticity direction."

- question: "If calcineurin activity is pharmacologically blocked during low-frequency stimulation, what would you expect to observe?"
  type: multiple-choice
  options:
    - "Enhanced LTD — removing calcineurin allows other phosphatases to act more strongly"
    - "LTP instead of LTD — kinases now dominate unopposed"
    - "LTD is prevented or reduced — AMPA receptor internalization requires calcineurin-mediated dephosphorylation"
    - "No change — calcineurin is not involved in synaptic plasticity"
  answer: 2
  explanation: "Calcineurin (protein phosphatase 2B) is a key enzyme that, when activated by moderate calcium, dephosphorylates proteins that normally anchor AMPA receptors at the postsynaptic membrane. This triggers endocytosis of AMPA receptors — the mechanistic basis of LTD. Blocking calcineurin prevents this dephosphorylation step, so AMPA receptors remain at the synapse and LTD is impaired. This pharmacological approach has been used experimentally to confirm calcineurin's causal role."

- question: "LTD and LTP both require calcium entry through NMDA receptors, but they differ in the amount and pattern of calcium elevation produced."
  type: true-false
  answer: true
  explanation: "True. This is the central insight of the BCM model of bidirectional synaptic plasticity. NMDA receptors act as the common gateway for both processes, but the downstream signaling diverges based on calcium amplitude and timing. High, brief calcium → kinase pathway → LTP. Low, sustained calcium → phosphatase pathway → LTD. The same receptor mediates opposite outcomes depending on the pattern of activation — a feature of enormous computational power."

- question: "LTD weakens synapses by reducing glutamate release from the presynaptic terminal."
  type: true-false
  answer: false
  explanation: "LTD is primarily a postsynaptic phenomenon. The weakening occurs through AMPA receptor internalization (endocytosis) at the postsynaptic membrane — fewer receptors means smaller electrical responses to the same amount of glutamate. Glutamate release from the presynaptic terminal is not reduced. This distinction matters: LTD changes the postsynaptic sensitivity to neurotransmitter, not the amount of neurotransmitter released. (Some presynaptic forms of LTD do exist, particularly at specific synapses, but the canonical NMDA-dependent cerebellar and hippocampal LTD is postsynaptic.)"

- question: "Explain why a brain that could only undergo LTP — but not LTD — would have severely impaired learning ability."
  type: short-answer
  answer: "Without LTD, synaptic strength can only increase. Over time, all synapses would approach maximum strength (saturation), making it impossible to encode new information — every input would produce the same maximal response, destroying the signal-to-noise ratio that allows discrimination between patterns. LTD provides the erasure and pruning that keeps synaptic weights in a dynamic range. In the cerebellum, LTD is the mechanism for correcting motor errors. In the hippocampus, it allows old associations to be overwritten. Without LTD, the network becomes a one-way ratchet: good at remembering early experiences, unable to adapt."
  explanation: "This tests whether students grasp LTD's functional role, not just its mechanism. The point is that strengthening and weakening are equally necessary for computation — a synapse scale with only one direction is useless for storing variable information."
```

## Explainer

From your understanding of postsynaptic currents and the distinction between ionotropic and metabotropic receptors, you know that synaptic transmission produces measurable electrical responses and that different receptor types trigger different intracellular signaling pathways. **Long-term depression (LTD)** is the complementary process to long-term potentiation (LTP) — while LTP strengthens synapses, LTD weakens them. Both are essential: a brain that could only strengthen synapses would quickly saturate, with every connection at maximum strength and no ability to discriminate signal from noise. LTD provides the erasure, refinement, and forgetting that keep neural circuits functional.

The key to understanding LTD lies in **calcium concentration**. Both LTP and LTD are triggered by calcium entering the postsynaptic neuron through NMDA receptors, but the *amount* of calcium determines which direction the synapse moves. High-frequency stimulation (like a burst of rapid firing) produces large, fast calcium transients that activate **kinases** — enzymes like CaMKII that add phosphate groups to proteins. These kinases drive AMPA receptor insertion into the postsynaptic membrane, strengthening the synapse (LTP). Low-frequency stimulation (typically around 1 Hz for several minutes) produces a modest, sustained calcium elevation that instead activates **phosphatases** — enzymes like **calcineurin** (protein phosphatase 2B) and PP1 that remove phosphate groups. These phosphatases trigger the internalization of AMPA receptors: the receptors are pulled out of the postsynaptic membrane via endocytosis and either recycled or degraded. Fewer AMPA receptors in the membrane means smaller excitatory postsynaptic currents in response to the same amount of glutamate release — the synapse has been weakened.

This calcium-threshold model — sometimes called the **BCM theory** after Bienenstock, Cooper, and Munro — provides an elegant explanation for bidirectional plasticity at a single synapse. The postsynaptic neuron effectively reads its own calcium signal to decide whether to strengthen or weaken: brief, intense calcium means "this connection is important, keep it," while prolonged, moderate calcium means "this connection is not contributing usefully, weaken it." The threshold between LTP and LTD is itself adjustable through **metaplasticity** — a synapse's recent history of activity shifts the threshold, preventing runaway potentiation or depression.

LTD is not merely a laboratory curiosity — it plays critical roles in real neural computation. In the cerebellum, LTD at parallel fiber–Purkinje cell synapses is the primary mechanism for **motor learning**: when a movement produces an error, climbing fiber signals trigger LTD that weakens the synaptic connections responsible for the incorrect motor command. In the hippocampus, LTD contributes to memory flexibility by allowing old associations to be overwritten with new ones. During development, LTD helps refine neural circuits by weakening inappropriate connections — for example, eliminating synapses that carry poorly correlated visual input during the critical period of visual cortex development. Without LTD, the brain would be a one-way ratchet, accumulating synaptic strength without the ability to prune, refine, or adapt.
