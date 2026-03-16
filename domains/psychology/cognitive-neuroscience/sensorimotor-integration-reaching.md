---
id: sensorimotor-integration-reaching
title: Sensorimotor Integration and Reaching
domain: psychology
course: cognitive-neuroscience
prerequisites:
- id: dorsal-visual-stream-action
  type: hard
- id: motor-cortex
  type: soft
tags:
- sensorimotor
- action
- reaching
stage: advanced
status: draft
---

# Sensorimotor Integration and Reaching

## Core Idea
Reaching for an object requires transforming visual information about object location into motor commands. Posterior parietal cortex converts retinocentric (eye-centered) visual coordinates into body-centered coordinates, while premotor cortex further transforms these into muscle commands. Neural populations maintain multiple coordinate frames simultaneously, implementing coordinate transformations flexibly. Motor learning involves calibration of these sensorimotor transformations, explaining why reaching accuracy improves with practice and how reaching can be re-learned after brain damage.

## Explainer

You know from the dorsal visual stream that the "where/how" pathway runs from primary visual cortex through the parietal lobe and is specialized for the real-time guidance of action — not for conscious recognition of what something is, but for computing where it is and how to interact with it. Sensorimotor integration during reaching is the dorsal stream doing its primary job. The computational problem it solves is harder than it first appears: a cup on a desk has a location on your retina, but your arm muscles don't care about retinal coordinates. To move your arm to the cup, the visual location must be translated into a format the motor system can use. This translation — across multiple **coordinate frames** — is what sensorimotor integration accomplishes.

The first transformation happens in the **posterior parietal cortex (PPC)**. Visual input arrives in a **retinocentric** frame: the object is located at a particular angle from the center of the fovea. The PPC combines this with information about current eye position (from proprioceptors and efference copy signals about eye movements) to compute the object's location in a **head-centered** frame. It then combines head-centered position with information about head orientation to produce a **body-centered** representation. At each stage, multiple sources of information are integrated — visual input, proprioceptive signals, efference copies — to build a coordinate representation that the reaching system can work with. Lesions to PPC (as in **optic ataxia**) specifically disrupt this transformation: patients can recognize objects normally but fail to accurately direct their reach toward them.

The second transformation runs from PPC to **premotor cortex**. The body-centered spatial representation is converted into a movement plan: not "the object is 40 cm to my right" but "move the arm in this direction by this amount." Premotor cortex integrates spatial information with the current state of the arm — where it is now, what posture it's in — to specify the required movement. **Primary motor cortex** (which you know drives the corticospinal tract) then translates the movement plan into the specific muscle activation patterns that actually execute the reach. The whole pipeline is: retinal image → spatial location (PPC) → movement plan (premotor cortex) → muscle commands (motor cortex).

A crucial insight is that the brain maintains **multiple coordinate frames simultaneously** rather than converting sequentially through a single chain. Neural population recordings show that PPC neurons carry mixed selectivity — they encode information about gaze direction, limb position, and target location in a distributed, overlapping code. This redundancy makes the system flexible: reaching from a different starting arm position, or with the gaze directed elsewhere, doesn't require a completely new computation — the existing population activity can be recombined to produce the correct output.

**Motor learning in reaching** is best understood as **calibration** of the internal model that implements these coordinate transformations. The classic demonstration is the **prism adaptation** paradigm: when you wear goggles that shift the visual field 15 degrees to the right, your initial reaches miss to the right. With practice, reaches become accurate again — but if you remove the goggles, you now reach 15 degrees to the left (the **aftereffect**). The aftereffect shows that the internal transformation itself was updated, not just muscle outputs: the new "correct" transformation overshoots when applied to the undistorted visual world. This same recalibration mechanism underlies how stroke patients regain reaching accuracy through rehabilitation — the brain relearns the correct sensorimotor mapping to compensate for the changed neural circuitry.
