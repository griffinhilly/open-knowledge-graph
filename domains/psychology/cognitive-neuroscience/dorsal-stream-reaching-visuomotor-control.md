---
id: dorsal-stream-reaching-visuomotor-control
title: Dorsal Stream and Visuomotor Control
domain: psychology
course: cognitive-neuroscience
prerequisites:
- id: dorsal-visual-stream-action
  type: hard
- id: visual-cortex-hierarchical-organization
  type: hard
builds-toward:
- spatial-attention-parietal-cortex
- motor-control-posterior-parietal-cortex
tags:
- vision
- motor-control
- dorsal-stream
- visuomotor
- reaching
- grasping
stage: advanced
status: draft
---

# Dorsal Stream and Visuomotor Control

## Core Idea
The dorsal visual pathway, from V1 through parietal cortex, specializes in transforming visual information into action and navigation. It encodes object location relative to the observer and body, guides reaching and grasping movements, and maintains spatial maps for eye movements and navigation. Unlike the ventral stream's object identity representations, dorsal stream coding is egocentric and action-centered.

## Explainer

You know from the visual cortex hierarchy that visual information divides early into two processing streams: the ventral stream for object recognition ("what") and the dorsal stream for spatial processing and action ("where/how"). The dorsal stream's specialization for action means it solves a fundamentally different problem than object recognition. Recognizing that an object is a coffee cup doesn't tell your hand how to grasp it — for that, your brain needs the cup's precise location relative to your hand, its orientation, its size, and the right finger configuration to pick it up. This is what the dorsal stream provides: a continuously updated **egocentric spatial map** for guiding action in real time.

The pathway runs from V1 through motion- and depth-sensitive intermediate areas into the **posterior parietal cortex**, particularly the intraparietal sulcus (IPS) and its specialized subregions. The **anterior intraparietal area (AIP)** is specifically involved in grasping: it receives visual information about object shape and projects to premotor cortex to configure the appropriate hand posture *before* contact. You open your fingers to the right width for a glass as you reach toward it, not after you touch it — this predictive grip scaling requires dorsal stream processing. **LIP** (lateral intraparietal area) maintains spatial priority maps for eye movements. Together these parietal regions transform raw visual signals into movement-specific commands.

The critical distinction between dorsal and ventral stream coding is **reference frame**. Ventral stream representations are largely allocentric — objects are identified independently of where you are. Dorsal stream representations are egocentric — locations are encoded relative to the observer's body, in the coordinate frame that matters for action. Your hand doesn't care that the cup is 20 cm from the plate; it needs to know the cup is 40 cm in front of your shoulder. This egocentric frame is also transient: dorsal spatial representations update continuously as you move and are discarded once the action is complete, unlike ventral object memories that persist across time and viewpoint.

The cleanest evidence for this dissociation comes from neurological double dissociations. Patients with ventral stream damage (**visual agnosia**) cannot recognize objects — they can't name a cup or describe its function — but reach for it with correctly scaled grip aperture and accurate trajectory. Patients with dorsal stream damage (**optic ataxia**, typically from posterior parietal lesions) can recognize objects and describe them but reach with misguided arm movements and incorrect grip. Each stream can function independently of the other, and each fails independently when damaged. Optic ataxia also explains why optical illusions that distort conscious size perception often fail to fool your grasp — because grasping uses the dorsal stream's egocentric online calculations, not the ventral stream's perceptual representations that the illusion exploits.
