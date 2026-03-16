---
id: visual-attention-mechanisms
title: Neural Mechanisms of Visual Attention
domain: psychology
course: cognitive-neuroscience
prerequisites:
- id: attention-selective
  type: hard
- id: visual-processing-pathway
  type: hard
builds-toward:
- attention-networks-brain
tags:
- attention
- vision
- selection
stage: advanced
status: draft
---

# Neural Mechanisms of Visual Attention

## Core Idea
Spatial attention enhances neural responses at attended locations through top-down modulation. Frontal eye fields send attention-directing signals that amplify sensory processing in posterior visual areas, sharpening receptive fields and suppressing unattended information. Parietal cortex transforms attention-related spatial signals into sensorimotor coordinates. Temporal attention similarly enhances processing of expected stimulus onset times, revealing that attention operates across multiple dimensions.

## Explainer

You already know that selective attention is the process by which the brain prioritizes some inputs over others, and that visual processing runs in parallel streams through the ventral ("what") and dorsal ("where/how") pathways. The neural mechanism of attention bridges those two pieces of knowledge: attention is the brain's way of dynamically allocating processing resources within those pathways, and the control signals come from outside the visual system entirely.

The key insight is that attention acts like a **gain control mechanism** in early visual cortex. When you covertly shift attention to a location (without moving your eyes), neurons in V1, V2, and V4 whose **receptive fields** cover that location increase their firing rate — even before a stimulus appears there. When a stimulus does appear, attended stimuli drive stronger, more reliable responses than unattended ones. This happens not because the stimulus is stronger, but because the cortex is *prepared* to respond to it. Simultaneously, the spatial resolution of processing improves: receptive fields at the attended location effectively shrink and sharpen, enhancing discrimination of fine detail. Unattended locations are not merely deemphasized — they are actively suppressed, particularly when they contain distractors.

The source of these top-down signals is the **frontal eye field (FEF)**, located in premotor frontal cortex. The FEF is classically known as a saccade control region, but it sends preparatory signals to visual areas even when no eye movement is made — pure covert attention. FEF neurons encode priority maps: locations weighted by behavioral relevance, combining top-down goals (you're looking for a red target) with bottom-up salience (something moving in the periphery). These priority signals travel backward through the visual hierarchy, selectively amplifying processing at the coded locations. **Parietal cortex** (specifically the posterior parietal cortex, including areas like LIP and the right-lateralized temporoparietal junction) performs a crucial transformation: it converts spatial attention signals from retinal or head-centered coordinates into a format that can guide reach, grasp, and covert orienting — connecting "where to attend" to "where to act." Damage to the right parietal cortex causes **hemispatial neglect**, where patients fail to attend to or report stimuli on the contralateral side, confirming parietal cortex's essential role.

**Temporal attention** extends this framework to the time dimension. Just as spatial attention prepares the cortex for stimuli at a particular location, temporal attention prepares it for stimuli at a particular moment. When the onset of a stimulus is rhythmically predictable, neural oscillations in visual cortex entrain to that rhythm, with the excitability peak aligning to the expected stimulus time. This enhances detection of on-time stimuli and creates a trough of excitability just after the expected moment. The unifying principle across spatial and temporal attention is the same: the brain does not passively receive sensory input but actively prepares for expected inputs, allocating processing resources before the stimulus arrives. This predictive amplification is what makes attention the mechanism through which expectation and perception are coupled.
