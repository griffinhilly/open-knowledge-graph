---
id: working-memory-prefrontal-parietal-mechanisms
title: 'Working Memory: Prefrontal-Parietal Neural Mechanisms'
domain: psychology
course: cognitive-neuroscience
prerequisites:
- id: working-memory-prefrontal-circuits
  type: hard
- id: working-memory-model
  type: hard
- id: differential-equations-intro
  type: soft
builds-toward:
- working-memory-capacity-limits-neural-mechanisms
- interference-resolution-working-memory
tags:
- working-memory
- prefrontal
- parietal
- maintenance
- manipulation
- capacity
stage: advanced
status: draft
---

# Working Memory: Prefrontal-Parietal Neural Mechanisms

## Core Idea
Working memory maintenance and manipulation depend on sustained firing of prefrontal and parietal neurons that represent task-relevant information across delays. These networks show flexible, task-dependent tuning that rapidly adapts to current goals, distinct from the stable tuning of sensory and motor areas. Working memory capacity limitations reflect the number of items that can be robustly represented in these networks simultaneously.

## Explainer

You have already studied Baddeley's working memory model — the phonological loop, visuospatial sketchpad, episodic buffer, and central executive — and you have studied the basic prefrontal circuits that support maintenance. This topic goes deeper into the neural implementation: what are prefrontal and parietal neurons actually doing during the seconds you hold information in mind, and what sets a physical limit on how much you can hold?

The key discovery, made by Fuster and Goldman-Rakic using single-unit recording in primates, is **delay-period activity**: neurons in the dorsolateral prefrontal cortex (dlPFC) fire persistently throughout a delay period in which an animal must remember a stimulus location to make a later response. This sustained firing continues even when the stimulus is long gone from view and before the response is required — the neuron is representing the memory, not just responding to the cue or executing the action. Different neurons are tuned to different spatial locations (their firing is spatially selective), and the accuracy of the animal's subsequent response correlates with the stability of this firing. The prefrontal cortex is, in this sense, literally "holding" the information in the activity of its neurons.

**Parietal cortex** (particularly the intraparietal sulcus and inferior parietal lobule) plays a complementary role. Where prefrontal neurons tend to show flexible, goal-dependent tuning that changes with task demands, parietal neurons show more stable, sensory-derived representations — they map items in space or code their visual features more directly. The working memory network is a prefrontal-parietal circuit: parietal cortex provides high-quality sensory representations of the items, prefrontal cortex maintains them against interference, updates them when goals change, and coordinates their use in guiding behavior. Damage to either region impairs working memory, but in slightly different ways.

Capacity limits become interpretable at the neural level through the concept of **representational interference**. Fusi and Wang, using computational models, showed that recurrent prefrontal circuits can maintain a small number of distinct activity patterns simultaneously, but adding more items causes interference — the patterns partially overlap and corrupt each other. This matches behavioral data showing that working memory capacity saturates around 3–4 items in most paradigms. Capacity is not a slot count imposed from outside; it is the natural consequence of how many distinct stable states the prefrontal-parietal network can simultaneously sustain without mutual interference. This also explains why **similarity** between items degrades working memory — similar items recruit overlapping neural populations, increasing interference and leading to blending or loss of items from the maintained set.
