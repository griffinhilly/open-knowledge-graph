---
id: biological-motion-perception-stp
title: Biological Motion Perception and Superior Temporal Polysensory Cortex
domain: psychology
course: cognitive-neuroscience
prerequisites:
- id: motion-perception-middle-temporal-area
  type: hard
- id: face-processing-neural-systems
  type: soft
builds-toward:
- action-observation-social-perception
- biological-motion-autism-spectrum-differences
tags:
- biological-motion
- STP
- action-perception
- body-perception
stage: expert
status: validated
---

# Biological Motion Perception and Superior Temporal Polysensory Cortex

## Core Idea
The superior temporal polysensory cortex (STP), particularly in the superior temporal sulcus (STS), responds selectively to biological motion and body movements. This region integrates form information from the ventral stream with motion information from the dorsal stream to perceive animate agents. STP provides input to mentalizing regions, linking biological motion perception to social cognition.

## Questions

```yaml
- question: "A researcher shows participants two videos: (A) 12 dots moving in the pattern of a walking person, and (B) 12 scrambled dots with identical local velocity statistics. fMRI shows STS responds much more strongly to version A. What does this reveal about STS's role?"
  type: multiple-choice
  options:
    - "STS responds to any coherent motion pattern and is more active because walking has higher overall motion coherence"
    - "STS integrates body-form knowledge with motion signals to selectively detect biological agents, a computation MT alone cannot perform"
    - "STS is simply a more sensitive motion detector than MT for low-contrast stimuli"
    - "STS responds to the complexity of the motion pattern rather than its biological nature specifically"
  answer: 1
  explanation: "Because the scrambled version has identical local motion statistics, the difference in STS response cannot be explained by sensitivity to motion per se — MT handles motion regardless of what is moving. STS's selectivity requires knowledge of human body structure (from the ventral stream) combined with those motion signals. This integration is the key computation: detecting not just motion, but biologically patterned motion from a human agent."

- question: "STS responds more strongly when the sight of walking is paired with the sound of footsteps than to either cue alone. What does this support about STP's function?"
  type: multiple-choice
  options:
    - "STP is primarily an auditory region that receives visual input as secondary confirmation"
    - "Biological motion recognition requires both visual and auditory input to function — visual alone is insufficient"
    - "STP integrates multimodal cues to more reliably signal the presence of an animate agent in the environment"
    - "Footstep sounds are processed as a form of auditory motion through a parallel dorsal auditory stream"
  answer: 2
  explanation: "The 'polysensory' in STP reflects that biological agents produce correlated visual and auditory signals. STP's multimodal response does not mean vision alone is insufficient — point-light displays trigger STS responses without sound. Rather, integrating multiple cues provides a more reliable animacy signal. The 'polysensory' label signals that STP's role is agency detection from any available channel, not just visual motion processing."

- question: "STS is a convergence zone for dorsal stream (motion) and ventral stream (form) information, enabling it to detect patterns that require knowledge of both body structure and body movement."
  type: true-false
  answer: true
  explanation: "This is the anatomical logic behind STS's role in biological motion. Recognizing that a pattern of moving dots constitutes a walking human requires knowing both what the dots are doing (motion — dorsal stream) and what a human body looks like in motion (form — ventral stream). STS sits at the convergence of these two streams, which is why it is uniquely suited to this integration task."

- question: "Because MT/V5 responds strongly to coherent motion, it alone is sufficient to explain the brain's ability to recognize biological motion in point-light displays."
  type: true-false
  answer: false
  explanation: "MT responds robustly to coherent motion regardless of whether it is biological. It cannot distinguish a walking person from scrambled dots with the same motion statistics. Recognizing biological motion requires integrating motion signals with form knowledge about the human body — a computation performed by STS, not MT. This is why STS responses to biological motion exceed those to matched scrambled motion, even when MT activity is equivalent."

- question: "Why would atypical STS responses to biological motion be expected to have cascading effects on social cognition, not just on motion perception?"
  type: short-answer
  answer: "STS sends projections to the temporoparietal junction (TPJ) and medial prefrontal cortex (mPFC) — core nodes of the mentalizing network that attributes intentions and mental states to others. If STS fails to automatically flag a moving stimulus as an animate agent, the downstream mentalizing network never receives the signal to initiate social-cognitive processing. The functional chain runs from motion detection (MT) to animacy detection (STS) to intention attribution (TPJ/mPFC); STS is a necessary relay, so disrupting it affects the entire chain above it."
  explanation: "This is why STS dysfunction in autism spectrum conditions is theoretically significant — it is not simply a perceptual deficit but a potential early disruption in the pathway that normally scaffolds all subsequent social cognition. Biological motion perception is the entry point; social understanding is the destination."
```

## Explainer

You already know from the middle temporal area (MT/V5) that the dorsal visual stream handles motion processing, detecting speed and direction of moving stimuli. MT responds vigorously to a random dot field moving coherently — it extracts the motion signal regardless of what is moving. But biological motion poses a distinct problem: a person walking, dancing, or throwing is both a moving thing and a recognizable agent whose movements carry social meaning. The **superior temporal sulcus (STS)** and the surrounding **superior temporal polysensory cortex (STP)** are where the brain begins to answer the question "is that moving thing alive?"

The classic demonstration of STP's selectivity uses **point-light displays**: a person wearing reflective markers on their joints in a dark room, producing only 10-15 moving dots. Humans are immediately and automatically able to recognize these as a walking person, even in brief presentations, even upside-down versions cause recognition failure — suggesting the brain has a strong template for upright human motion specifically. Neuroimaging consistently shows that STS responses to point-light biological motion are stronger than to scrambled versions of the same dots moving with identical local motion statistics. This selectivity requires precisely the integration of form knowledge (where joints are relative to one another in a human body) with motion signals — a computation that MT alone cannot perform.

The "polysensory" in STP is not accidental. This region receives input from auditory cortex as well as visual motion and form pathways. It responds to the sound of footsteps paired with the visual motion of walking more strongly than either alone, suggesting it integrates multimodal cues about animate agency. This makes sense: in the real world, biological agents produce correlated visual and auditory motion signals, and detecting animacy from multiple channels is more reliable than from vision alone.

The downstream consequence is what makes STP theoretically important beyond motion perception. STP sends projections to the **temporoparietal junction (TPJ)** and **medial prefrontal cortex** — core nodes of the mentalizing network responsible for attributing mental states to others. The chain from motion detection (MT) → animate agent detection (STS) → mental state attribution (TPJ/mPFC) maps a plausible functional pathway from "something is moving" to "that agent has intentions." Consistent with this, disruptions to STS responses to biological motion are a reliable finding in autism spectrum conditions, with potentially cascading effects on social cognition that depend on smooth automatic detection of biological motion as the starting point.
