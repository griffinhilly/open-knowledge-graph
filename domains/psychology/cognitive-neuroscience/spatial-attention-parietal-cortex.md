---
id: spatial-attention-parietal-cortex
title: Spatial Attention and Posterior Parietal Cortex
domain: psychology
course: cognitive-neuroscience
prerequisites:
- id: attention-networks-brain
  type: hard
- id: dorsal-stream-reaching-visuomotor-control
  type: hard
builds-toward:
- prefrontal-parietal-attention-networks
- neglect-syndrome-spatial-awareness
tags:
- attention
- spatial-attention
- posterior-parietal
- IPS
- neglect
- awareness
stage: expert
status: draft
---

# Spatial Attention and Posterior Parietal Cortex

## Core Idea
The posterior parietal cortex, particularly intraparietal sulcus (IPS), encodes the location of attended objects and integrates sensory information with motor plans for attention shifts. Right-hemisphere parietal damage produces contralateral spatial neglect—patients fail to orient toward or report stimuli in the contralesional field—demonstrating parietal cortex's role in directing spatial attention and awareness. Parietal neurons show multiplicative gain modulation encoding attention state.

## Questions

```yaml
- question: "A patient with right posterior parietal damage fails to acknowledge people on their left, eats only from the right side of their plate, and marks a horizontal line's midpoint well to the right of center. What best describes this patient's deficit?"
  type: multiple-choice
  options:
    - "Cortical blindness in the left visual field due to damage to primary visual cortex"
    - "Paralysis of leftward eye movements due to damage to oculomotor control regions"
    - "Hemispatial neglect: failure of spatial representation and attentional orienting toward the contralesional side, despite intact peripheral vision"
    - "Visual agnosia for objects on the left side due to damage to the ventral object-recognition stream"
  answer: 2
  explanation: "The patient has hemispatial neglect — the critical distinction from blindness is that the primary sensory pathway may be intact; the problem is attentional and representational. Neglect patients can detect high-contrast stimuli in their neglected field under forced-choice conditions, demonstrating early visual cortex receives the input. What fails is the parietal attentional signal that brings left-side stimuli into awareness. The line-bisection error (marking right of center) is a classic neglect sign: attention is systematically biased rightward, effectively shrinking the left half. Options A and D describe primary sensory or recognition deficits, not attentional ones."

- question: "Parietal neurons modulate spatial attention through multiplicative gain rather than additive enhancement. Compared to additive enhancement, what is the key consequence of multiplicative gain?"
  type: multiple-choice
  options:
    - "Multiplicative gain creates a smaller increase in response overall, since multiplying by a factor less than 2 adds fewer spikes than a fixed additive amount"
    - "Multiplicative gain allows neurons to respond to stimuli outside their normal selectivity, expanding their receptive field"
    - "Multiplicative gain scales the entire response curve upward, amplifying signal-to-noise ratio across the full dynamic range while preserving the neuron's selectivity"
    - "Multiplicative gain lowers threshold, allowing neurons to fire to stimuli that previously fell below the activation level"
  answer: 2
  explanation: "If a neuron fires 10, 20, 40 spikes to dim, medium, and bright stimuli, multiplicative gain (×2) produces 20, 40, 80 — preserving contrast ratios and actually increasing absolute signal-to-noise differences. Additive enhancement (+10) would produce 20, 30, 50 — compressing the contrast between stimuli at high intensities. Moreover, the neuron's selectivity (what it responds to) doesn't change, only the magnitude. This mechanism propagates attention's effects throughout the processing hierarchy without altering what information is being processed — only how faithfully it is represented."

- question: "Left parietal damage causes more severe hemispatial neglect than right parietal damage, because the left hemisphere controls the dominant right hand and therefore receives more attentional resources."
  type: true-false
  answer: false
  explanation: "This reverses the clinical reality. Right parietal damage causes far more severe neglect due to a hemispheric asymmetry in spatial representation: the right hemisphere contains spatial maps for both left and right space, while the left hemisphere handles predominantly right space. When the right hemisphere is damaged, both hemispheres lose coverage of left space — there is no compensatory representation remaining. When the left hemisphere is damaged, the right hemisphere's coverage of right space is intact and its partial coverage of left space persists. The dominant-hand account confuses motor lateralization (which is left-hemisphere-dominant) with spatial representation (which is right-hemisphere-dominant)."

- question: "The intraparietal sulcus encodes spatial locations simultaneously in multiple reference frames — including retinal, head-centered, and body-centered coordinates — allowing the attention spotlight to remain anchored to objects even as the eyes and head move."
  type: true-false
  answer: true
  explanation: "Multi-frame coding is what makes parietal spatial representations useful for both perception and action. Retinal coordinates track where stimuli fall on the retina (which shifts with every eye movement); head-centered coordinates track position relative to the head; body-centered coordinates track position relative to the trunk. IPS neurons integrate retinal signals with extraretinal eye-position signals to maintain stable object representations. This allows the attention spotlight to remain locked onto an object of interest through eye movements, and to interface with motor commands for reaching (body-centered) and saccades (retinal)."

- question: "Explain why hemispatial neglect is not simply blindness in the contralesional visual field. What is the actual nature of the deficit, and what clinical evidence demonstrates the distinction?"
  type: short-answer
  answer: "Hemispatial neglect is a failure of spatial representation and attentional orienting, not a sensory deficit. Primary visual pathways (retina → LGN → V1) may be entirely intact. Under forced-choice conditions, neglect patients can detect that something appeared on their neglected side — the information reaches early visual cortex. What fails is the parietal-driven attentional process that would orient awareness toward that location. Clinical evidence: neglect patients copy only the right half of drawings even when instructed to copy the whole figure; they cross out marks only on the right side of a page with uniformly distributed marks; they can sometimes describe neglected objects under strong prompting. A truly blind patient would show none of these directional asymmetries — they simply would not see on either side."
  explanation: "The distinction between not seeing (blindness) and not attending (neglect) is fundamental to understanding parietal function. Neglect reveals that conscious perception requires not just sensory input but an active attentional mechanism that selects spatial locations for awareness — and that mechanism is mediated by the parietal cortex."
```

## Explainer

From your study of attention networks, you know that attention operates through distinct systems — alerting (maintaining vigilance), orienting (selecting spatial locations), and executive (resolving conflict). The parietal cortex is the neurobiological heart of the **orienting network**, specifically the selection and shifting of attention across space. From your prerequisite on the dorsal visual stream, you know that this pathway — running from early visual cortex through posterior parietal cortex — computes the spatial locations of objects and transforms that information into action-oriented coordinates. Spatial attention brings these two prerequisites together: parietal cortex both represents where things are and controls where attention points.

The key structure is the **intraparietal sulcus (IPS)**, a deep crease in the posterior parietal cortex containing multiple sub-areas that respond to the locations of attended stimuli across different modalities (visual, auditory, touch). When you covertly shift attention to the right side of space — without moving your eyes — IPS neurons representing that region increase their firing. Crucially, IPS represents space in multiple reference frames simultaneously: retinal coordinates (relative to current gaze), head-centered coordinates, and body-centered coordinates. This multi-frame coding allows the attention spotlight to remain anchored to objects even as your eyes and head move, and to interface with motor planning for eye movements (**saccades**) and arm reaches toward attended locations.

The most dramatic demonstration of parietal cortex's role in spatial attention is **hemispatial neglect**, which occurs after right parietal damage. Neglect patients behave as if the left half of space has ceased to exist. They eat only from the right side of their plate, shave or apply makeup only to the right side of their face, and when asked to bisect a horizontal line, they place the mark well to the right of center. This is not blindness — sensory pathways may be intact — and it is not paralysis. It is a failure of **spatial representation and attentional orienting**: the damaged right hemisphere can no longer generate the attentional signal needed to bring left-side locations into awareness. The right hemisphere in humans handles both right and left space, while the left hemisphere handles only right space, which is why right-hemisphere damage produces far more severe neglect than left-hemisphere damage.

At the level of individual neurons, parietal cells encode spatial attention through **multiplicative gain modulation**: rather than simply adding activation when attention is directed to their preferred location, they scale their entire response curve upward. A neuron that fires 10 spikes to a dim stimulus and 20 to a bright stimulus might fire 30 and 60 respectively when attention is directed to its location. This multiplication amplifies the signal-to-noise ratio throughout the visual processing hierarchy without changing what the neuron is selective for — it simply processes attended information more faithfully. This gain mechanism, propagated forward through the ventral stream, explains how spatial attention sharpens perception and recognition of attended objects.
