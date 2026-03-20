---
id: neuroplasticity
title: Neuroplasticity
domain: psychology
course: biological-psychology
prerequisites:
- id: synaptic-transmission
  type: hard
- id: brain-lobes-and-functions
  type: soft
- id: cerebral-cortex-organization
  type: soft
- id: neuron-structure-and-function
  type: soft
- id: glial-cells-and-support
  type: soft
- id: critical-periods-plasticity
  type: hard
tags:
- LTP
- LTD
- synaptic-plasticity
- cortical-reorganization
- learning
- development
stage: advanced
status: validated
---
# Neuroplasticity

## Core Idea
Neuroplasticity is the brain's capacity to change its structure and function in response to experience, learning, or injury. At the synaptic level, long-term potentiation (LTP) — strengthening of synapses through repeated co-activation — is the leading cellular model of learning and memory. Structural plasticity includes dendritic spine growth, axonal sprouting, and, in limited brain regions, adult neurogenesis (notably the hippocampal dentate gyrus). At the cortical level, sensory and motor maps reorganize after skill acquisition or limb amputation. Critical periods are developmental windows of heightened plasticity when specific experiences have outsized, lasting effects.

## How It's Best Learned
Hebb's rule ('neurons that fire together wire together') provides the intuitive core of LTP. Contrast the high plasticity of the infant brain with the more constrained adult brain, while noting that adult plasticity is real and forms the basis of rehabilitation after stroke and brain injury.

## Common Misconceptions
- 'We only use 10% of our brain' is false and unrelated to neuroplasticity; virtually all regions are active at appropriate times.
- Neuroplasticity is not uniformly beneficial — maladaptive plasticity underlies chronic pain, addiction, and post-traumatic stress disorder.

## Questions

```yaml
- question: "Long-term potentiation (LTP) is best described as which of the following?"
  type: multiple-choice
  options:
    - "The death of neurons following prolonged activation, clearing space for new connections"
    - "A permanent and irreversible strengthening of all synapses throughout the brain"
    - "The strengthening of a synapse when pre- and postsynaptic neurons repeatedly fire together"
    - "The brain's ability to grow entirely new cortical lobes after injury"
  answer: 2
  explanation: "LTP occurs at specific synapses when repeated co-activation causes the postsynaptic neuron to insert more AMPA receptors, making future transmission easier. It is not permanent (LTD — long-term depression — can reverse it), it does not affect all synapses globally, and it does not produce new lobes. Hebb's rule summarizes the principle: neurons that fire together wire together."

- question: "Neuroplasticity always produces beneficial changes in the brain."
  type: true-false
  answer: false
  explanation: "Neuroplasticity is a mechanism, not a direction. The same synaptic-strengthening processes that underlie learning also underlie maladaptive changes: chronic pain syndromes (where pain circuits are sensitized even without ongoing injury), addiction (where reward pathways are reshaped to prioritize drugs over other stimuli), and PTSD (where fear circuits become overly sensitized to trauma-associated cues). Whether plasticity is adaptive or maladaptive depends entirely on which circuits are being reinforced and in what context."

- question: "A concert violinist has a dramatically expanded cortical representation of their left-hand fingers in both the motor and somatosensory cortex compared to non-musicians. What does this illustrate, and what cellular mechanism underlies it?"
  type: short-answer
  answer: "It illustrates use-dependent cortical reorganization: cortical maps expand for body parts and movements that are used most intensively. The cellular mechanism is LTP-based synaptic strengthening — repeated co-activation of neurons in the left-hand pathways strengthens those synapses and recruits neighboring cortical territory, physically expanding the map."
  explanation: "Cortical representations are not fixed at birth. The motor and somatosensory homunculi are dynamic maps that reflect actual use patterns. Musicians, Braille readers, and taxi drivers all show measurable cortical map changes corresponding to their expertise. This is also why targeted rehabilitation (e.g., constraint-induced movement therapy after stroke) can partially restore function by forcing use of the affected limb and driving plasticity in the damaged region."
```

## Explainer

You've learned how synaptic transmission works — an action potential arrives at the presynaptic terminal, neurotransmitters are released, and they bind to receptors on the postsynaptic cell. Neuroplasticity is the discovery that this process is not fixed: the strength of synaptic connections changes based on experience, and the brain's very structure reorganizes in response to what you do repeatedly. This is the cellular basis of learning and memory.

The most important mechanism is **long-term potentiation (LTP)**. When a synapse is repeatedly activated — especially when the pre- and postsynaptic neurons fire at nearly the same time — the postsynaptic cell inserts more AMPA receptors into the synapse. This makes future signals stronger: the same presynaptic input now produces a larger response. The simplest summary is Hebb's rule: *neurons that fire together wire together*. The NMDA receptor plays a central role here — it acts as a coincidence detector, requiring simultaneous pre- and postsynaptic activity to open. When it opens, calcium flows in and triggers the molecular cascade that leads to receptor insertion and synaptic strengthening. LTP can be reversed by long-term depression (LTD), which removes receptors when a synapse is weakly or asymmetrically activated — allowing the brain to also weaken connections that are no longer useful.

At larger scales, neuroplasticity shows up as **cortical map reorganization**. The primary motor cortex and somatosensory cortex contain maps of the body (the homunculi), but these maps are dynamic. Musicians who practice intensively develop larger cortical representations of their playing fingers. After amputation, the cortical territory formerly representing the missing limb is gradually taken over by neighboring areas, sometimes causing phantom limb sensations. Stroke rehabilitation exploits this: forcing patients to use an affected limb (even when it's easier not to) drives activity-dependent plasticity in surviving tissue, allowing partial functional recovery.

Two important boundary conditions: first, **critical periods** are developmental windows when plasticity is dramatically heightened and certain inputs have outsized, lasting effects. The classic example is binocular vision — if one eye is deprived of input during a specific early window, the cortical representation of that eye shrinks permanently and normal depth perception never develops. Missing the critical period means the plasticity opportunity is largely gone, even if input is restored later. Second — and this is a common misconception — neuroplasticity is not inherently good. The same mechanisms that produce learning also produce maladaptive changes. Chronic pain arises partly because pain-signaling circuits undergo LTP and become sensitized. Addiction involves the dopamine reward pathway being reshaped so that drug-associated cues drive behavior more powerfully than natural rewards. PTSD reflects overly strengthened fear circuits. Plasticity is a tool; whether it helps or harms depends on what is being reinforced.
