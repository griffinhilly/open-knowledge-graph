---
id: dorsal-visual-stream-action
title: The Dorsal Stream and Action Control
domain: psychology
course: cognitive-neuroscience
prerequisites:
- id: visual-processing-pathway
  type: hard
- id: motor-cortex
  type: soft
builds-toward:
- sensorimotor-integration-reaching
tags:
- vision
- action
- reaching
stage: expert
status: draft
---

# The Dorsal Stream and Action Control

## Core Idea
The dorsal visual stream (occipital → parietal cortex) converts visual information into motor commands for hand and eye movements. It encodes object location, orientation, and size needed for reaching and grasping. Posterior parietal cortex transforms visual coordinates into motor coordinates, while premotor cortex uses these signals to control action. Damage to dorsal stream regions produces optic ataxia—inability to reach toward visual targets despite normal vision.

## Questions

```yaml
- question: "A patient can identify objects, name them, and describe their properties accurately, but when reaching for them consistently misses by several centimeters despite normal visual acuity. This pattern most likely indicates damage to:"
  type: multiple-choice
  options:
    - "Inferotemporal cortex, which stores visual object representations"
    - "Primary visual cortex (V1), affecting the resolution of visual input"
    - "Posterior parietal cortex, disrupting visuomotor coordinate transformation"
    - "Primary motor cortex, impairing execution of reaching movements"
  answer: 2
  explanation: "This is the hallmark of optic ataxia — accurate object perception with inaccurate visually guided reaching. The patient's intact identification confirms that the ventral stream and object representations are functioning normally. The deficit is specifically in converting visual target location into motor coordinates, which is the function of posterior parietal cortex (PPC) in the dorsal stream. If primary motor cortex were damaged, the deficit would appear across all reaching regardless of whether targets were visual."

- question: "Why is 'how pathway' a more accurate label for the dorsal stream than the traditional 'where pathway'?"
  type: multiple-choice
  options:
    - "The dorsal stream processes high-frequency spatial details, not low-frequency location information"
    - "The dorsal stream computes real-time metric information for motor control, not conscious spatial representation"
    - "The dorsal stream does not actually process spatial location — it only processes motion"
    - "The 'where' label was based on lesion studies in primates that do not generalize to humans"
  answer: 1
  explanation: "The 'where' label implies the dorsal stream represents spatial location for conscious awareness. But the key function is converting visual input into action-relevant parameters — distance to target, grip aperture, object orientation — in real time and largely outside awareness. These computations are fundamentally different from perceptual spatial representation. You do not consciously calculate grip width when reaching for a cup; the dorsal stream performs these motor-format computations automatically. 'How' captures this functional role more precisely."

- question: "A patient with visual form agnosia (ventral stream damage) cannot recognize or identify objects by sight, yet they accurately calibrate their grip aperture when reaching for those objects."
  type: true-false
  answer: true
  explanation: "This is the double dissociation that confirms the independence of vision-for-action and vision-for-perception. The ventral stream handles object identity; the dorsal stream handles action parameters like grip width. When the ventral stream is damaged, perceptual identification fails but the dorsal stream can still compute appropriate grip apertures from the object's physical properties (size, orientation). This demonstrates that the action system does not require conscious object recognition — it operates on visual input processed through a completely separate pathway."

- question: "The visuomotor transformations performed by the dorsal stream rely on conscious awareness of the target's location in order to produce accurate reaching movements."
  type: true-false
  answer: false
  explanation: "The dorsal stream operates largely outside conscious awareness. When you reach for your coffee cup, you do not consciously compute the distance from your hand to the cup, calculate required finger aperture, or track the trajectory of your arm. These computations happen automatically and continuously, driven by real-time visual input processed by the dorsal stream and posterior parietal cortex. Conscious spatial awareness is a ventral-stream phenomenon. The dissociation is precisely that action and perception are served by parallel, largely independent systems running on the same visual input."

- question: "What does the double dissociation between optic ataxia and visual form agnosia demonstrate about the relationship between visual perception and visually guided action?"
  type: short-answer
  answer: "The double dissociation shows that vision-for-action and vision-for-perception are functionally and anatomically independent systems. Optic ataxia (dorsal stream damage) impairs reaching despite intact object recognition — demonstrating that the action system is dissociable from the perceptual system. Visual form agnosia (ventral stream damage) impairs object recognition while leaving visually guided action intact — demonstrating that the action system does not depend on conscious perception. Together, these cases confirm that the same visual input is processed in two distinct ways by two distinct pathways for two distinct purposes."
  explanation: "A single dissociation (one direction) could be explained by one system being a component of another, or by one being more 'fragile.' The double dissociation — each system can be independently damaged — is the strong evidence for genuine functional independence. It rules out the simpler explanation that perception and action share a single system, with one being more vulnerable. This finding reshaped our understanding of vision from a single unified system to a collection of specialized parallel processors."
```

## Explainer

From your study of the visual processing pathway, you know that the visual system splits after primary visual cortex (V1) into two broad processing streams. The ventral stream projects toward inferotemporal cortex and handles object identification — the "what" pathway, answering the question "what is that object?" The dorsal stream projects toward posterior parietal cortex and has traditionally been called the "where" pathway. But that label is misleading. A better characterization is the **"how" pathway** — it does not simply represent spatial location for conscious awareness; it converts visual information into the format required for motor action.

The key insight is that vision-for-action requires different computations than vision-for-recognition. To identify an apple, you need categorical representation — shape, color, texture organized into a concept. To *grasp* an apple, you need precise metric information that updates in real-time: the current distance from your hand to the object, the exact width and orientation of the object's graspable surface, and the required finger aperture. These computations must happen quickly, automatically, and largely outside conscious awareness — every time you reach for your coffee cup, you don't consciously calculate its distance or adjust your grip aperture deliberately. The dorsal stream provides this service continuously.

**Posterior parietal cortex (PPC)**, especially the intraparietal sulcus, is the critical integration zone. It receives visual input from dorsal visual areas and proprioceptive input about current limb position, and it performs **visuomotor coordinate transformation** — translating the retinal position of a target into a body-centered or hand-centered frame of reference that motor circuits can use. From PPC, signals project to premotor cortex and then to primary motor cortex, forming the complete sensorimotor loop. Crucially, this loop operates in parallel with (and largely independently from) the ventral stream's conscious object representations.

The clinical case of **optic ataxia** provides the sharpest evidence for this dissociation. Patients with damage to posterior parietal cortex (typically from bilateral occipitoparietal lesions) cannot accurately reach toward visual targets — they miss by several centimeters, despite correctly identifying the target and having normal primary visual acuity. The visual perception is intact; the visual-to-motor transformation is broken. The double dissociation is equally revealing: patients with ventral stream damage (visual form agnosia) cannot identify objects but can calibrate grip aperture correctly when reaching for them — demonstrating that the action system does not depend on conscious recognition. Together, these cases confirm that vision-for-action is a functionally and anatomically distinct system from vision-for-perception, running on the same visual input but processing it in fundamentally different ways for fundamentally different purposes.
