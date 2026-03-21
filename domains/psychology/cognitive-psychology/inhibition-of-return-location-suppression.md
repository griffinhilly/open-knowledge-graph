---
id: inhibition-of-return-location-suppression
title: Inhibition of Return and Spatial Attention Suppression
domain: psychology
course: cognitive-psychology
prerequisites:
- id: attention-selective
  type: hard
- id: spatial-attention-parietal-cortex
  type: soft
builds-toward:
- attention-networks-brain
tags:
- attention
- spatial-suppression
- memory
stage: advanced
status: draft
---

# Inhibition of Return and Spatial Attention Suppression

## Core Idea
After attention shifts away from a location, that location becomes temporarily inhibited—people are slower to respond to stimuli at the previously attended location than at new locations. This inhibition-of-return effect prevents wasteful re-scanning and represents an implicit spatial memory of where attention has been. It operates outside awareness and reflects evolutionary adaptation to search efficiently in visual environments.

## How It's Best Learned
Measure reaction times to targets at previously attended vs. new locations as a function of the time interval since attention shifted away. Plotting reaction time curves reveals the temporal dynamics of inhibition.

## Common Misconceptions
- Assuming attention simply moves to new locations; inhibition shows attention also leaves marks on previous locations.
- Confusing inhibition-of-return with fatigue or reduced processing resources; it's location-specific, not general.

## Questions

```yaml
- question: "A peripheral cue flashes in the left visual field, drawing attention there. 150ms later, a target appears at the same cued location. How should reaction time to this target compare to a target at an uncued location?"
  type: multiple-choice
  options:
    - "Slower — the previously attended location is already being suppressed by IOR"
    - "Faster — the cue has primed attention at that location"
    - "No difference — spatial priming effects take at least 400ms to emerge"
    - "Slower — visual adaptation to the cue reduces sensitivity there"
  answer: 1
  explanation: "At 150ms post-cue, the visual system is still in the attentional facilitation window (roughly 0–200ms), where the previously cued location shows enhanced processing. IOR — the suppression — emerges later, beyond approximately 300–400ms, after attention has disengaged and shifted elsewhere. Option A reflects the common misconception that IOR begins immediately; in fact, facilitation always precedes inhibition."

- question: "Patients with right parietal damage no longer show slower responses at previously attended locations in their left visual field. What does this finding most directly support?"
  type: multiple-choice
  options:
    - "That IOR is caused by photoreceptor fatigue local to the attended region"
    - "That parietal cortex is part of the mechanism underlying IOR's spatial suppression"
    - "That IOR requires conscious awareness, which these patients lack"
    - "That IOR is a peripheral rather than central attentional phenomenon"
  answer: 1
  explanation: "Disrupted IOR following right parietal damage directly implicates parietal cortex in the suppression mechanism — the same circuitry that mediates spatial orienting and spatial representation. This also rules out photoreceptor fatigue (a peripheral, receptor-level effect) and consciousness (IOR operates outside awareness in unimpaired participants). The clinical finding links IOR to the broader dorsal attention network."

- question: "Inhibition of return serves an adaptive foraging function by tagging previously visited locations, biasing attention toward unexplored areas of the visual scene."
  type: true-false
  answer: true
  explanation: "This is the core functional logic of IOR. A visual forager scanning for food or predators would waste time rescanning already-checked locations. IOR provides an implicit 'visited recently' spatial tag that suppresses those locations, systematically biasing attention outward toward new, unexplored regions. This foraging account explains the evolutionary rationale for what is otherwise a counterintuitive reversal of attentional facilitation."

- question: "Inhibition of return reflects a general depletion of attentional resources following a cue, which slows responses across all locations in the visual field."
  type: true-false
  answer: false
  explanation: "IOR is location-specific, not a global resource-depletion effect. Responses at new, never-attended locations are unimpaired — or faster. The inhibition tags the previously attended spatial position specifically, leaving the rest of the visual field unaffected. Confusing IOR with resource fatigue is one of the listed Common Misconceptions: fatigue would impair all subsequent detection, whereas IOR suppresses only the specific prior location."

- question: "Why do researchers describe inhibition of return as an 'implicit spatial memory' rather than simply saying attention has moved elsewhere?"
  type: short-answer
  answer: "Because previously attended locations are not merely neutral — they are actively suppressed, making responses there slower than at entirely new locations that were never attended. This suppression persists for hundreds of milliseconds and follows locations across eye movements, functioning as a spatial record of where attention has been."
  explanation: "If IOR were just 'attention moved elsewhere,' previously cued and new locations would be equally fast after attention leaves. The fact that previously cued locations are reliably slower than fresh locations reveals an active inhibitory trace — not the absence of attention but a positive suppression. This transforms the model of attention from a spotlight that selects present targets into a dynamic system that tracks and suppresses its own prior history."
```

## Explainer

From your study of selective attention, you know that the visual system enhances processing at attended locations — orienting a spotlight of attention toward a location speeds detection and discrimination of stimuli appearing there. From spatial attention research, you know this orienting is supported by parietal cortex and the superior colliculus, and that it can be driven reflexively by sudden-onset stimuli or voluntarily by goals. **Inhibition of return (IOR)** describes what happens after attention leaves a location: rather than simply becoming neutral again, the previously attended position becomes transiently *suppressed*, making responses to targets there slower than responses to entirely new locations. Attention doesn't just move toward; it leaves an inhibitory footprint behind.

The temporal dynamics of IOR have a distinctive signature. For the first ~100–200 milliseconds after a peripheral cue draws attention to a location, there is **attentional facilitation** — targets at that location are detected faster. If attention then disengages and shifts elsewhere, this advantage reverses. Beyond approximately 300–400 milliseconds post-cue, responses to targets at the previously cued location are *slower* than responses to targets at new, uncued locations. This is the IOR effect proper. It persists for several hundred milliseconds to seconds, builds gradually as facilitation fades, and — crucially — operates even for reflexive cues that never attract sustained voluntary attention. The inhibition is tied to a location tag, not to the cue's sensory properties, and it follows the location across eye movements.

The **functional logic** of IOR is elegant. A foraging animal scanning a visual environment for food or predators faces a spatial search problem: how do you avoid wasting time rescanning locations you've already checked when the target isn't there? IOR provides an implicit solution — a "visited recently" tag on previously attended locations, implemented as transient suppression that biases attention forward toward new, unchecked regions. The search becomes foraging-efficient, systematically moving outward rather than circling back. This is implicit: people experience no conscious sense of suppression. Yet the bias reliably shapes behavior, distributed across the superior colliculus and dorsal parietal attention networks.

IOR enriches the conception of attention from a spotlight that selects current targets to a dynamic system that also tracks where it has been. Attentional selection is not memoryless — it is a sequential process with a spatial history, and IOR is one mechanism coordinating that history. Clinical populations with attentional disorders show instructive IOR abnormalities: patients with right parietal damage and spatial neglect show disrupted or absent IOR in the neglected hemifield, linking the suppression mechanism directly to the same parietal circuitry that mediates spatial orienting and the spatial representation of the environment.
