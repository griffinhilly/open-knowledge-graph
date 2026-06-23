---
id: sensory-cortical-streams
title: Sensory Cortical Processing Streams
domain: biology
course: neuroscience
prerequisites:
- id: cortical-organization
  type: hard
- id: color-vision-perception
  type: soft
- id: sensory-neural-coding-perception
  type: soft
tags:
- visual-cortex
- streams
- ventral
- dorsal
stage: advanced
status: validated
---

# Sensory Cortical Processing Streams

## Core Idea
Sensory information flows through parallel streams with distinct functions. The visual system has a ventral 'what' stream (inferior temporal cortex) processing object identity and a dorsal 'where' stream (parietal cortex) processing spatial location and motor control. Similar functional segregation occurs in auditory and somatosensory cortex.

## How It's Best Learned
Compare receptive field properties across streams. Use lesion studies to isolate stream functions.

## Common Misconceptions
Streams are segregated—they interact extensively. All visual information goes to V1 first—some routes bypass V1.

## Questions

```yaml
- question: "A patient with brain damage can accurately reach out and pick up a pencil placed on a table, and can use it to write — but cannot identify it as a pencil, describe its shape, or name what it is used for. Which processing stream is most likely damaged?"
  type: multiple-choice
  options:
    - "The dorsal stream — because reaching and grasping require dorsal stream function, which is impaired"
    - "The ventral stream — the patient can use the pencil (dorsal stream intact for action guidance) but cannot recognize or name it (ventral stream, responsible for object identity, is damaged)"
    - "Primary visual cortex — because the failure to name objects suggests a fundamental visual deficit"
    - "Both streams equally — because writing requires integrating both 'what' and 'where' information"
  answer: 1
  explanation: "This is a classic presentation of visual agnosia — the selective inability to recognize objects despite intact visual acuity and intact visuomotor function. The patient's ability to reach accurately for the pencil and use it demonstrates that the dorsal stream (spatial processing and action guidance) is intact. The inability to identify, name, or describe the pencil indicates ventral stream damage: the pathway from V1 through V4 to inferotemporal cortex, responsible for object identity, shape, and color recognition, is disrupted. The double dissociation between 'can act on it, cannot recognize it' is the diagnostic signature of selective ventral stream damage."

- question: "Why is the label 'where stream' considered an oversimplification of what the dorsal visual pathway actually does?"
  type: multiple-choice
  options:
    - "Because the dorsal stream also processes object color and texture in addition to location"
    - "Because the dorsal stream is better characterized as a 'how' pathway — it computes spatial transformations needed to guide actions such as reaching, grasping, and navigation, not merely an abstract sense of spatial location"
    - "Because spatial location is actually processed in the ventral stream through scene context"
    - "Because 'where' implies conscious awareness of location, but the dorsal stream operates largely unconsciously"
  answer: 1
  explanation: "The original Ungerleider and Mishkin framework labeled the streams 'what' and 'where.' Milner and Goodale later revised this to 'what' and 'how,' based on evidence that the dorsal stream computes the specific spatial parameters needed for motor action — grip aperture, hand orientation, trajectory — rather than providing conscious spatial knowledge. A patient with dorsal stream damage (optic ataxia) can say 'the pencil is to the left' (conscious spatial knowledge preserved) but cannot accurately reach for it (action-specific computation damaged). This dissociation shows the dorsal stream is about visuomotor transformation, not location representation per se."

- question: "Damage to the dorsal stream can produce optic ataxia — a condition in which patients can identify objects but cannot accurately reach for them — demonstrating that the dorsal stream is specifically involved in visually guided action rather than object recognition."
  type: true-false
  answer: true
  explanation: "Optic ataxia is one of the key lesion dissociations that established the functional separation of the two streams. Patients have intact ventral stream function (they can recognize and name objects) but impaired dorsal stream function (they cannot use visual information to guide reaching movements, even toward objects they can clearly see and identify). This is the mirror image of visual agnosia, where dorsal stream function is intact (accurate reaching) and ventral stream is damaged (no recognition). These double dissociations are the strongest evidence that the streams perform genuinely distinct computations."

- question: "The ventral and dorsal visual streams operate independently as sealed parallel channels, with no information exchange between them once visual input diverges from V1."
  type: true-false
  answer: false
  explanation: "This is explicitly identified as a misconception in the topic. Extensive cross-connections allow information to flow between the ventral and dorsal streams throughout the visual hierarchy. Many natural visual tasks require the coordinated action of both streams — for example, recognizing an object (ventral) and then reaching for it in a specific orientation (dorsal) requires information about what the object is to inform how to grasp it. The segregation of the streams is functional and relative, not absolute. Additionally, some visual processing bypasses V1 entirely through subcortical routes (e.g., superior colliculus to pulvinar), further demonstrating that the two-stream model is an approximation of a more complex parallel and interactive architecture."

- question: "Describe what a patient with 'visual agnosia' can and cannot do, and explain what this pattern reveals about how visual processing is organized in the cortex."
  type: short-answer
  answer: "A patient with visual agnosia can see clearly — they can navigate around furniture, respond to moving objects, and accurately reach for things placed in front of them. What they cannot do is recognize, name, or describe what they are looking at: they cannot say a pencil is a pencil, cannot identify faces (prosopagnosia), or cannot categorize objects by shape or function. This pattern reveals that visual processing is functionally segregated: the ability to use visual information to guide action (dorsal stream, intact) is dissociated from the ability to identify what one is seeing (ventral stream, damaged). The ventral stream — from V1 through V4 to inferotemporal cortex — performs the computations required for object identity and recognition, and these computations are not necessary for visuomotor control."
  explanation: "Visual agnosia is theoretically important because it rules out the alternative explanation that all visual processing occurs in a unified system and recognition failures reflect a general visual deficit. The patient's intact reaching behavior demonstrates that visual information about object location and shape is available to the motor system even when it is not available for conscious recognition. This dissociation is only possible if separate neural pathways handle these two aspects of vision — which is exactly the two-stream model."
```

## Explainer

From your study of cortical organization, you know that the cerebral cortex is parceled into functionally distinct areas and that sensory information is processed through hierarchical stages. From color vision and perception, you know that the visual system extracts features like wavelength and contrast early in processing. The concept of **cortical processing streams** explains what happens next: rather than a single pipeline that progressively builds a complete picture of the world, sensory cortex splits information into parallel channels that emphasize different aspects of a stimulus.

The visual system provides the clearest example. After initial processing in the primary visual cortex (V1), visual information diverges into two major pathways. The **ventral stream** flows from V1 through areas V2 and V4 into the inferior temporal cortex. This pathway is specialized for recognizing **what** something is — its shape, color, texture, and identity. Neurons along the ventral stream have progressively larger receptive fields and respond to increasingly complex features: simple edges in V1, contours and surface properties in V4, and whole objects and faces in inferotemporal cortex. Damage to the ventral stream produces **visual agnosia** — patients can see objects clearly, describe their features, and navigate around them, but cannot recognize or name what they are looking at.

The **dorsal stream** flows from V1 through area V5/MT into the posterior parietal cortex. This pathway processes **where** something is and **how** to interact with it — spatial location, motion, and the visual guidance of actions like reaching and grasping. Neurons in area MT are highly sensitive to the direction and speed of motion, while parietal areas integrate visual information with motor planning. Damage to the dorsal stream produces **optic ataxia** — patients can identify objects but cannot accurately reach for them — and **akinetopsia**, the inability to perceive motion (the world appears as a series of frozen snapshots).

The ventral/dorsal distinction is sometimes oversimplified as "what vs. where," but the reality is richer. The dorsal stream is better described as a "how" pathway — it computes the spatial transformations needed for action, not just an abstract sense of location. Moreover, the two streams are not sealed off from each other. Extensive cross-connections allow information to flow between them, and many perceptual tasks require both streams working in concert. A similar principle of parallel functional streams has been identified in the auditory cortex (a "what" stream for sound identity and a "where" stream for sound localization) and in somatosensory processing. The general principle is that the cortex decomposes complex sensory input into parallel channels optimized for different behavioral demands, then recombines them as needed for unified perception and action.
