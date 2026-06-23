---
id: experience-dependent-plasticity-learning
title: Experience-Dependent Plasticity and Learning
domain: psychology
course: cognitive-neuroscience
prerequisites:
- id: neuroplasticity
  type: hard
- id: long-term-potentiation
  type: soft
- id: brain-plasticity-recovery
  type: soft
- id: synaptogenesis-and-developmental-plasticity
  type: soft
tags:
- plasticity
- learning
- experience
stage: expert
status: validated
---
# Experience-Dependent Plasticity and Learning

## Core Idea
Learning induces synaptic plasticity that strengthens or weakens connections between neurons based on experience. Long-term potentiation (LTP) increases synaptic strength through NMDA receptor calcium influx and postsynaptic changes, while long-term depression weakens synapses. Learning also recruits new neurons into circuits, expands cortical maps, and promotes dendritic spine formation. These cellular mechanisms explain how neurons change to represent learned associations, supporting new perceptual, motor, and cognitive abilities.

## Questions

```yaml
- question: "A rat learns that pressing lever A delivers food but lever B never does. Over time, synapses connecting 'lever B' activity to the reward circuit weaken. Which mechanism is primarily responsible for this weakening?"
  type: multiple-choice
  options:
    - "LTP at the lever-B synapse, which paradoxically reduces sensitivity through receptor saturation"
    - "LTD, caused by repeated presynaptic activation without corresponding postsynaptic firing at the lever-B synapse"
    - "Cortical map contraction, which physically removes the lever-B representation"
    - "NMDA receptor downregulation globally across all active synapses"
  answer: 1
  explanation: "When lever B is pressed (presynaptic activity) but no reward follows and the postsynaptic reward neuron does not fire, the coincidence condition for full NMDA receptor activation is not met. The moderate Ca²⁺ influx activates phosphatases rather than kinases, removing AMPA receptors from the synapse — this is LTD. LTD is the pruning mechanism that eliminates predictively irrelevant synaptic connections, ensuring only associations that reliably predict outcomes are strengthened."

- question: "During LTP induction, why must both the presynaptic and postsynaptic cells be active at nearly the same time?"
  type: multiple-choice
  options:
    - "Simultaneous activity is needed to activate adenylyl cyclase in the presynaptic terminal"
    - "NMDA receptors require both glutamate binding (signaling presynaptic activity) and postsynaptic depolarization (removing Mg²⁺ block) to pass calcium"
    - "Only presynaptic activity is required; postsynaptic activity is needed only for LTD"
    - "Simultaneous activity triggers retrograde endocannabinoid signaling that opens postsynaptic AMPA receptors"
  answer: 1
  explanation: "NMDA receptors are coincidence detectors: glutamate from the presynaptic neuron binds the receptor, but the channel stays blocked by Mg²⁺ unless the postsynaptic membrane is sufficiently depolarized. When both cells are active simultaneously, the Mg²⁺ block is relieved and Ca²⁺ floods in. This Ca²⁺ influx activates CaMKII, leading to phosphorylation of existing AMPA receptors and trafficking of new ones into the synapse — strengthening the connection. This is the molecular implementation of Hebbian plasticity."

- question: "Cortical maps representing body regions are fixed after early childhood and can seldom be reorganized by adult experience."
  type: true-false
  answer: false
  explanation: "Cortical maps remain experience-dependent throughout adulthood. Studies of expert Braille readers show enlarged cortical representation of reading fingers compared to non-readers. Conversely, if a finger is amputated, the cortical area previously devoted to it is gradually invaded by representations of adjacent fingers. This adult map plasticity is driven by the same LTP/LTD mechanisms that govern synaptic plasticity — sustained use of a body region drives LTP at relevant connections, expanding that region's cortical territory."

- question: "LTD removes AMPA receptors from synapses that are activated without coincident postsynaptic firing."
  type: true-false
  answer: true
  explanation: "When a synapse is activated (glutamate released, NMDA receptor partially engaged) but the postsynaptic cell doesn't depolarize enough to fully relieve the Mg²⁺ block, only a moderate Ca²⁺ influx occurs. This lower calcium signal activates phosphatases rather than kinases, which dephosphorylate AMPA receptors and trigger their internalization. The synapse is weakened. This is the mechanistic basis for LTD and explains why predictively irrelevant synaptic connections are pruned during learning."

- question: "Why is LTD just as important as LTP for learning, and what would happen to learning if only LTP could occur?"
  type: short-answer
  answer: "LTP strengthens associations that co-occur, but without LTD, all activated synapses would eventually saturate — every connection would become maximally strong and the network would lose its ability to discriminate between different patterns. LTD provides selectivity: it prunes synapses that are active but not predictively correlated with outcomes, ensuring that only meaningful associations are preserved. A brain that only potentiated would progressively lose specificity, storing noise as readily as signal."
  explanation: "LTD is the pruning mechanism that gives the learning process its specificity. The interplay between LTP (strengthen co-active pathways) and LTD (weaken inconsistently active pathways) is what allows neural circuits to refine their representations. Without LTD, learning would be like writing on a whiteboard where you can only add text but never erase — the board quickly becomes unreadable."
```

## Explainer

Neuroplasticity — your prerequisite concept — is the brain's general capacity to change in response to experience. But "the brain can change" is a very broad claim. Experience-dependent plasticity makes it specific: it describes *what changes*, *why it changes*, and *how those changes support learning*. The key bridge between the two concepts is **long-term potentiation (LTP)**, the synaptic mechanism that converts experience into durable structural change.

You know the cellular mechanism of LTP: coincident pre- and postsynaptic activity opens **NMDA receptors**, allowing Ca²⁺ influx into the postsynaptic spine. This calcium signal triggers kinase activity (particularly CaMKII), which phosphorylates existing AMPA receptors (making them more responsive) and drives trafficking of new AMPA receptors into the synapse. The result is a strengthened connection — the same presynaptic input now produces a larger postsynaptic response. What connects this to *learning* is the Hebbian insight: cells that consistently fire together (because they're activated by the same stimulus or sequence of events) repeatedly co-activate their shared synapse, meeting the coincidence condition that opens NMDA receptors and inducing LTP. The synapse that supports the learned association literally grows stronger.

LTP produces both **functional** and **structural** changes. The functional change — more AMPA receptors — is fast. The structural change — new dendritic spines, growth of existing spines, sometimes even new axonal boutons — takes hours but is more durable. This structural consolidation is what makes memories persist beyond the window of kinase activity. Learning also drives **cortical map expansion**: when a body region is repeatedly stimulated (as in Braille reading), the cortical area devoted to that finger expands at the expense of adjacent representations. This map plasticity is experience-dependent in the most literal sense — use the finger more, the map grows; amputate the finger, the map is invaded by neighbors. The same principle applies to motor learning: pianists show enlarged cortical representation of the finger movements they have practiced most.

**Long-term depression (LTD)** is the complement of LTP and equally important for learning. LTD occurs when a synapse is repeatedly activated without coincident postsynaptic firing — the presynaptic cell fires, but the postsynaptic cell doesn't reach threshold. Moderate Ca²⁺ influx (insufficient to trigger CaMKII) instead activates phosphatases that remove AMPA receptors from the synapse, weakening the connection. LTD ensures that not all synapses strengthen simultaneously — only the ones that are predictively correlated with outcomes are preserved. LTD is the pruning mechanism at the circuit level, analogous to synaptic pruning during development but operating throughout adulthood.

The full picture of experience-dependent plasticity is therefore a coordinated multi-level process: individual synapses strengthen (LTP) or weaken (LTD) based on activity patterns, spines grow or retract to support these changes, cortical maps reorganize to reflect patterns of use, and in the hippocampus, adult **neurogenesis** adds new neurons that can be recruited into newly formed memories. Learning doesn't just use the brain — it physically reshapes it. The learner who has practiced a skill for thousands of hours has a brain that is measurably different from a novice's, not because of intelligence, but because sustained experience-dependent plasticity has built a more efficient, more responsive circuit for that domain.
