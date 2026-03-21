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

## Questions

```yaml
- question: "A patient with posterior parietal cortex (PPC) damage is shown a coffee cup on a table. She describes it accurately — 'a white ceramic mug with a handle' — but when she reaches for it, her hand misses by several centimeters and she cannot correct the trajectory. What best explains this pattern?"
  type: multiple-choice
  options:
    - "The PPC damage impaired visual recognition, so she cannot actually see the cup clearly"
    - "The PPC damage disrupted the coordinate transformation that converts visual location into body-centered reaching commands, leaving recognition intact"
    - "The motor cortex was also damaged, preventing accurate finger movements"
    - "She has learned to reach inaccurately through motor habit and needs retraining"
  answer: 1
  explanation: "This is the classic presentation of optic ataxia: intact recognition (ventral stream is undamaged) combined with impaired visually guided reaching (dorsal stream/PPC is damaged). The PPC is not responsible for recognizing what objects are — it converts their retinal location into the body-centered coordinates the motor system needs to reach for them. The patient can describe the cup because the ventral stream is fine; she cannot reach for it because the retinocentric-to-body-centered coordinate transformation is broken."

- question: "A researcher wears goggles that shift the visual field 15 degrees to the right. After many practice reaches, the reaches become accurate again. The goggles are then removed. What do we expect, and what does it reveal about motor learning?"
  type: multiple-choice
  options:
    - "Reaches will be immediately accurate again, because the original motor program is restored"
    - "Reaches will overshoot to the left, because the internal sensorimotor transformation was recalibrated and now applies a 15-degree correction to normal vision"
    - "Reaches will still go to the right, because the arm muscles were trained to move rightward"
    - "Reaches will be random, because removing the goggles confuses the visual system"
  answer: 1
  explanation: "The leftward aftereffect is the key evidence that motor learning updated the *internal model* — the coordinate transformation itself — not just trained the muscles to move in a particular direction. If only muscle output had changed, removing the goggles would simply restore the original calibration. Instead, the transformation now applies a correction that overshoots in the opposite direction when the original visual input returns. This demonstrates that motor learning is calibration of the sensorimotor mapping, explaining how stroke patients can re-learn reaching by recalibrating around damaged circuitry."

- question: "The posterior parietal cortex computes object location in head-centered and body-centered coordinates by combining retinal position with signals about eye orientation and head position."
  type: true-false
  answer: true
  explanation: "This is exactly the function of PPC in sensorimotor integration. Visual input arrives in a retinocentric frame — where on the retina the image falls. The PPC integrates this with proprioceptive signals and efference copies about eye and head orientation to progressively construct a body-centered representation that the motor system can work with. This multi-signal integration is why PPC lesions specifically impair reaching even when vision is intact."

- question: "Prism adaptation aftereffects are caused by retraining arm muscles to fire in a new pattern, which must then be un-trained when the prisms are removed."
  type: true-false
  answer: false
  explanation: "The aftereffect reveals that it is the *coordinate transformation* — the internal model — that was recalibrated, not the muscles themselves. If muscles were retrained to move rightward, removing the goggles would simply restore normal muscle output. Instead, the system overshoots leftward because it is now applying a corrective transformation to unshifted visual input. Motor learning in reaching is learning a new sensorimotor mapping, not conditioning specific muscle outputs."

- question: "Why does prism adaptation produce an aftereffect in the opposite direction when the goggles are removed, and what does this tell us about how the brain implements motor learning for reaching?"
  type: short-answer
  answer: "The aftereffect occurs because motor learning updated the internal model — the coordinate transformation itself — to compensate for the visual shift. When the goggles are removed, that updated transformation is still in place and applies an unnecessary correction, causing the overshoot in the opposite direction. This shows that motor learning is not about training muscles to move in a new direction but about recalibrating the sensorimotor transformation that maps visual locations to movement commands."
  explanation: "This is the central insight about motor learning as model calibration. The transformation — not the muscles — is what changes. This same mechanism explains why stroke patients can partially recover reaching ability through rehabilitation: the brain relearns the correct sensorimotor mapping to compensate for changed neural circuitry, not by rebuilding the damaged circuits but by updating the transformations implemented in surviving ones."
```

## Explainer

You know from the dorsal visual stream that the "where/how" pathway runs from primary visual cortex through the parietal lobe and is specialized for the real-time guidance of action — not for conscious recognition of what something is, but for computing where it is and how to interact with it. Sensorimotor integration during reaching is the dorsal stream doing its primary job. The computational problem it solves is harder than it first appears: a cup on a desk has a location on your retina, but your arm muscles don't care about retinal coordinates. To move your arm to the cup, the visual location must be translated into a format the motor system can use. This translation — across multiple **coordinate frames** — is what sensorimotor integration accomplishes.

The first transformation happens in the **posterior parietal cortex (PPC)**. Visual input arrives in a **retinocentric** frame: the object is located at a particular angle from the center of the fovea. The PPC combines this with information about current eye position (from proprioceptors and efference copy signals about eye movements) to compute the object's location in a **head-centered** frame. It then combines head-centered position with information about head orientation to produce a **body-centered** representation. At each stage, multiple sources of information are integrated — visual input, proprioceptive signals, efference copies — to build a coordinate representation that the reaching system can work with. Lesions to PPC (as in **optic ataxia**) specifically disrupt this transformation: patients can recognize objects normally but fail to accurately direct their reach toward them.

The second transformation runs from PPC to **premotor cortex**. The body-centered spatial representation is converted into a movement plan: not "the object is 40 cm to my right" but "move the arm in this direction by this amount." Premotor cortex integrates spatial information with the current state of the arm — where it is now, what posture it's in — to specify the required movement. **Primary motor cortex** (which you know drives the corticospinal tract) then translates the movement plan into the specific muscle activation patterns that actually execute the reach. The whole pipeline is: retinal image → spatial location (PPC) → movement plan (premotor cortex) → muscle commands (motor cortex).

A crucial insight is that the brain maintains **multiple coordinate frames simultaneously** rather than converting sequentially through a single chain. Neural population recordings show that PPC neurons carry mixed selectivity — they encode information about gaze direction, limb position, and target location in a distributed, overlapping code. This redundancy makes the system flexible: reaching from a different starting arm position, or with the gaze directed elsewhere, doesn't require a completely new computation — the existing population activity can be recombined to produce the correct output.

**Motor learning in reaching** is best understood as **calibration** of the internal model that implements these coordinate transformations. The classic demonstration is the **prism adaptation** paradigm: when you wear goggles that shift the visual field 15 degrees to the right, your initial reaches miss to the right. With practice, reaches become accurate again — but if you remove the goggles, you now reach 15 degrees to the left (the **aftereffect**). The aftereffect shows that the internal transformation itself was updated, not just muscle outputs: the new "correct" transformation overshoots when applied to the undistorted visual world. This same recalibration mechanism underlies how stroke patients regain reaching accuracy through rehabilitation — the brain relearns the correct sensorimotor mapping to compensate for the changed neural circuitry.
