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

## Questions

```yaml
- question: "A patient can recognize a coffee cup, describe its shape, and name it correctly, but when reaching for it produces misguided arm movements and incorrect grip aperture. A second patient reaches with accurate trajectory and correctly scaled grip but cannot name the cup or describe its function. Which patient has dorsal stream damage?"
  type: multiple-choice
  options:
    - "The first patient — impaired recognition indicates a 'where/how' system failure"
    - "The second patient — accurate reaching means the dorsal stream is intact, so it must be damaged elsewhere"
    - "The first patient — the reaching and grasping impairments point to a broken visuomotor system"
    - "Both patients have dorsal stream damage because both show some visual deficit"
  answer: 2
  explanation: "The first patient has optic ataxia, the signature of dorsal stream (posterior parietal cortex) damage: recognition is intact (ventral stream works), but the visuomotor transformation that guides reaching and grip scaling fails. The second patient has visual agnosia from ventral stream damage: the dorsal stream correctly guides action without conscious object recognition. This double dissociation is the strongest evidence that the two streams operate independently."

- question: "A visual illusion makes a disk appear 20% larger than it actually is. A person reaches to grasp the disk. Which outcome best demonstrates dorsal-ventral stream dissociation?"
  type: multiple-choice
  options:
    - "The person reports the disk looks larger AND opens their grip wider — both streams are fooled by perception"
    - "The person reports the disk looks larger but grip aperture matches the disk's actual size — grasping uses the dorsal stream's egocentric calculation, not the ventral percept"
    - "The person reports the disk looks normal AND grip aperture is accurate — the illusion is too weak to affect either stream"
    - "The person opens their grip wider but reports no size distortion — the dorsal stream overrides ventral perception"
  answer: 1
  explanation: "Grasping uses the dorsal stream's online egocentric calculations, which are based on the actual retinal geometry, not the ventral stream's perceptual interpretation that the illusion distorts. So the illusion fools conscious perception (ventral) but not grip scaling (dorsal). This is exactly the pattern observed in experiments using the Ebbinghaus illusion — a real-world demonstration that what you 'see' and what your hand 'knows' can diverge."

- question: "Dorsal stream spatial representations persist across days, giving the brain a stable allocentric map of where objects are in the environment."
  type: true-false
  answer: false
  explanation: "Dorsal stream representations are egocentric (relative to the observer's body) and transient — they are continuously updated as the observer moves and are discarded once the action is complete. This is unlike ventral stream object memories, which persist across time and viewing angles. A stable allocentric map would be useless for real-time motor control, where what matters is the object's position relative to your current hand location, not some abstract fixed frame."

- question: "A patient with posterior parietal cortex damage would likely show difficulty recognizing familiar faces but would be able to reach accurately toward objects."
  type: true-false
  answer: false
  explanation: "Posterior parietal cortex is the core of the dorsal stream, so its damage produces optic ataxia — impaired reaching and grasping despite intact recognition. Face recognition is a ventral stream function (especially fusiform face area). The described pattern is the opposite of what posterior parietal damage produces. A patient with ventral stream damage might show prosopagnosia (face recognition failure) while retaining accurate motor guidance."

- question: "Why must the dorsal stream encode object location in an egocentric reference frame rather than an allocentric one?"
  type: short-answer
  answer: "Motor commands operate in body-centered coordinates: the arm moves relative to the shoulder, the hand opens relative to the wrist. To translate visual information into action, the brain needs to know where the object is relative to the body, not relative to some external landmark. An allocentric representation ('the cup is 10 cm from the plate') cannot directly specify a motor command; an egocentric one ('the cup is 35 cm in front of my shoulder at 15° elevation') can."
  explanation: "This is why egocentric coding is not a limitation of the dorsal stream but its core design feature. The continuous, real-time updating of the egocentric map reflects the fact that every body movement changes the spatial relationship between the observer and the object. The moment you rotate your shoulder, the arm-centered coordinates for the target change — and the dorsal stream recalculates accordingly."
```

## Explainer

You know from the visual cortex hierarchy that visual information divides early into two processing streams: the ventral stream for object recognition ("what") and the dorsal stream for spatial processing and action ("where/how"). The dorsal stream's specialization for action means it solves a fundamentally different problem than object recognition. Recognizing that an object is a coffee cup doesn't tell your hand how to grasp it — for that, your brain needs the cup's precise location relative to your hand, its orientation, its size, and the right finger configuration to pick it up. This is what the dorsal stream provides: a continuously updated **egocentric spatial map** for guiding action in real time.

The pathway runs from V1 through motion- and depth-sensitive intermediate areas into the **posterior parietal cortex**, particularly the intraparietal sulcus (IPS) and its specialized subregions. The **anterior intraparietal area (AIP)** is specifically involved in grasping: it receives visual information about object shape and projects to premotor cortex to configure the appropriate hand posture *before* contact. You open your fingers to the right width for a glass as you reach toward it, not after you touch it — this predictive grip scaling requires dorsal stream processing. **LIP** (lateral intraparietal area) maintains spatial priority maps for eye movements. Together these parietal regions transform raw visual signals into movement-specific commands.

The critical distinction between dorsal and ventral stream coding is **reference frame**. Ventral stream representations are largely allocentric — objects are identified independently of where you are. Dorsal stream representations are egocentric — locations are encoded relative to the observer's body, in the coordinate frame that matters for action. Your hand doesn't care that the cup is 20 cm from the plate; it needs to know the cup is 40 cm in front of your shoulder. This egocentric frame is also transient: dorsal spatial representations update continuously as you move and are discarded once the action is complete, unlike ventral object memories that persist across time and viewpoint.

The cleanest evidence for this dissociation comes from neurological double dissociations. Patients with ventral stream damage (**visual agnosia**) cannot recognize objects — they can't name a cup or describe its function — but reach for it with correctly scaled grip aperture and accurate trajectory. Patients with dorsal stream damage (**optic ataxia**, typically from posterior parietal lesions) can recognize objects and describe them but reach with misguided arm movements and incorrect grip. Each stream can function independently of the other, and each fails independently when damaged. Optic ataxia also explains why optical illusions that distort conscious size perception often fail to fool your grasp — because grasping uses the dorsal stream's egocentric online calculations, not the ventral stream's perceptual representations that the illusion exploits.
