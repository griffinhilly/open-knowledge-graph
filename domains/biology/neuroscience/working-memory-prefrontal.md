---
id: working-memory-prefrontal
title: Working Memory and Prefrontal Cortex
domain: biology
course: neuroscience
prerequisites:
- id: primary-motor-cortex
  type: hard
- id: cortical-organization
  type: soft
builds-toward:
- attention-control
- cognitive-flexibility
tags:
- working-memory
- prefrontal-cortex
- maintenance
stage: advanced
status: validated
---

# Working Memory and Prefrontal Cortex

## Core Idea
Prefrontal cortex (PFC) maintains task-relevant information across delays through sustained firing of pyramidal cells organized into functional subgroups. Different PFC regions encode task rules, stimulus-response mappings, and expected outcomes. Working memory capacity (~7 items) is limited by the balance between signal strength and noise.

## How It's Best Learned
Use delayed-response tasks; record PFC during memory delay. Map population codes for maintained information.

## Common Misconceptions
Working memory is stored in PFC—PFC maintains activity patterns. Attention makes memories permanent—sustained attention is required.

## Questions

```yaml
- question: "In a delayed-response task, a monkey watches food hidden under one of two cups, waits 15 seconds, and then reaches. During the delay, a brief loud noise is introduced. The monkey reaches for the wrong cup. The neuroscientific explanation is:"
  type: multiple-choice
  options:
    - "The memory trace decayed passively from a short-term storage buffer during the long delay"
    - "The hippocampus failed to consolidate the spatial memory into long-term storage before the delay ended"
    - "The distraction interrupted the sustained PFC neuronal firing that was actively maintaining the spatial information online"
    - "The loud noise activated competing motor programs in premotor cortex that overrode the stored location"
  answer: 2
  explanation: "Working memory in the PFC exists as sustained firing — neurons continue firing throughout the delay period to keep spatial information 'online.' This firing is vulnerable to disruption: a distractor can knock the population out of its maintained state, and the information collapses immediately. This is not passive decay (option A) but active disruption of an active process. The hippocampus (option B) is involved in consolidating long-term memories, not maintaining brief working memories during delays."

- question: "A patient with PFC damage cannot hold a phone number in mind long enough to dial it, but their long-term memory for facts and events is intact. Which conclusion best fits this pattern?"
  type: multiple-choice
  options:
    - "Working memory and long-term memory are the same system; PFC damage only affects recently encoded memories within hours of learning"
    - "Working memory depends on active sustained PFC firing to maintain information online, while long-term memory involves different structures and mechanisms that are unaffected"
    - "The PFC stores phone numbers in synaptic weight changes; the intact long-term memory shows that the PFC is not truly damaged"
    - "Long-term memory is localized entirely in the PFC; the preserved long-term memory in this patient shows the case is atypical"
  answer: 1
  explanation: "This double dissociation — impaired working memory, intact long-term memory — supports the conclusion that they are distinct systems with different neural substrates. PFC damage disrupts the active maintenance mechanism (sustained firing) that keeps information online for immediate use, while hippocampal-cortical systems supporting long-term memory consolidation are unaffected. Long-term memories don't 'live' in PFC as active firing; they are stored in synaptic changes elsewhere."

- question: "The prefrontal cortex stores working memory information in lasting synaptic weight changes, similar to how long-term memories are consolidated in hippocampal circuits."
  type: true-false
  answer: false
  explanation: "Working memory in PFC is maintained by sustained action potential firing — neurons remain active throughout the delay period to represent information that is no longer perceptually present. This is fundamentally different from long-term memory consolidation, which requires synaptic potentiation and structural changes over hours to days. When PFC firing is disrupted (by distraction, cooling, or direct interference), working memory vanishes instantly — exactly what you'd expect for a system based on ongoing activity rather than permanent structural storage."

- question: "Working memory capacity is limited partly because each additional item loaded requires a separate neural population to sustain firing, and competing populations interfere with each other's signal fidelity."
  type: true-false
  answer: true
  explanation: "The biophysical basis of the ~4-7 item capacity limit lies in the competition between simultaneously maintained representations. Each sustained firing population must maintain its signal against background neural noise and against interference from other active populations. As more items are loaded, the signal-to-noise ratio for each representation degrades. This explains both the capacity ceiling and why adding a single item beyond capacity can cause multiple items to fail simultaneously."

- question: "Why is it more accurate to say the prefrontal cortex 'actively maintains' working memory rather than 'stores' it, and what does this distinction predict about the effects of distraction?"
  type: short-answer
  answer: "Working memory exists as ongoing neural activity — sustained firing of PFC pyramidal neurons that must be continuously maintained against noise and competing signals. Unlike storage, which is passive and persistent, active maintenance is fragile: anything that interrupts the firing pattern (a distractor, cooling the cortex, magnetic stimulation) immediately destroys the representation. This predicts that distraction during a delay will cause immediate forgetting, not gradual decay — which is exactly what experiments show."
  explanation: "The storage metaphor implies a box where information sits until retrieved. The active maintenance view implies a process that must be continuously run. These have different predictions: a storage system would survive brief interruptions; an active maintenance system would not. The fragility of working memory to distraction — and the specificity of that disruption to ongoing delay activity — is strong evidence for the active-maintenance account."
```

## Explainer

You already know that the cerebral cortex is organized into functionally distinct regions, and that the primary motor cortex generates the commands that drive voluntary movement. The **prefrontal cortex** (PFC) sits anterior to motor areas and serves a fundamentally different purpose: rather than executing actions, it holds information "online" so you can use it to guide those actions. Think of it as a mental workspace — a whiteboard where you temporarily pin the facts, rules, and goals needed for whatever you are doing right now. This capacity is called **working memory**, and it is what allows you to remember a phone number long enough to dial it, follow the thread of a conversation, or keep track of which step you are on in a multi-step procedure.

The neural basis of working memory is **sustained firing**. When a piece of information enters working memory, a population of pyramidal neurons in the PFC continues to fire throughout the delay period — even after the original stimulus is gone. Imagine a delayed-response task: a monkey sees food hidden under one of two cups, then waits through a delay before being allowed to reach. During that delay, specific PFC neurons fire persistently, encoding "left cup" or "right cup." If those neurons stop firing — because of distraction, interference, or experimental disruption — the animal reaches for the wrong cup. The information literally exists as ongoing neural activity, not as a stored trace the way long-term memories are consolidated in hippocampal and cortical circuits.

Different subregions of the PFC maintain different kinds of information. The **dorsolateral prefrontal cortex** is particularly involved in maintaining spatial locations and task rules — the "what am I supposed to do" aspect of a task. The **ventrolateral PFC** contributes more to maintaining object identity and feature information. And the **orbitofrontal** and **medial prefrontal** regions encode expected outcomes and reward values, helping the system decide which information is worth holding onto. This division of labor means working memory is not a single box but a distributed workspace with specialized compartments.

A critical feature of working memory is its strict **capacity limit** — famously around seven items (plus or minus two), though more recent estimates suggest the true limit is closer to four independent chunks. This limit arises from the biophysics of sustained firing: each maintained item requires a group of neurons to keep firing against a background of noise and competing signals. As more items are loaded, the signals interfere with each other, degrading the fidelity of each representation. This is why you can hold a seven-digit phone number in mind but struggle with a ten-digit one, and why any distraction during the maintenance period can cause the information to collapse. The PFC does not passively store information — it actively fights to maintain it, and that active maintenance is the bottleneck that makes working memory both powerful and limited.
