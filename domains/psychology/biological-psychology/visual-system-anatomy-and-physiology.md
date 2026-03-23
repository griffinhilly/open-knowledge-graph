---
id: visual-system-anatomy-and-physiology
title: Visual System Anatomy and Physiology
domain: psychology
course: biological-psychology
prerequisites:
- id: sensory-transduction-and-neural-coding
  type: hard
- id: photoreceptors-phototransduction
  type: soft
- id: visual-system-retina-cortex
  type: hard
tags:
- vision
- retina
- cortex
- perception
stage: formal-systems
status: validated
---

# Visual System Anatomy and Physiology

## Core Idea
The visual system begins with photoreceptors (rods and cones) in the retina that respond to light wavelength (cones) and intensity (rods). Retinal circuits extract local contrast and motion features before sending information to the brain. The lateral geniculate nucleus relays information to visual cortex where neurons are organized retinotopically (neighboring cortical neurons respond to neighboring visual field locations). V1 simple cells detect oriented edges; V2 and beyond process increasing complexity of features (curvature, color, motion, faces).

## How It's Best Learned
Examine retinal structure and rod/cone distribution across the retina. Study receptive field properties of retinal and cortical neurons. Trace anatomical projections from retina through LGN to cortical areas. Map visual field representations in cortex.

## Common Misconceptions
The eye is a camera / all visual information enters consciousness / V1 is the only visual area / color is processed only in cones.

## Questions

```yaml
- question: "A patient suffers a stroke affecting their ventral visual stream. Which deficit would you most expect?"
  type: multiple-choice
  options:
    - "Inability to perceive motion, particularly in the peripheral visual field"
    - "Inability to guide reaching movements accurately toward objects"
    - "Inability to recognize objects, faces, or identify what an object is"
    - "Loss of depth perception due to disrupted binocular disparity processing"
  answer: 2
  explanation: "The ventral stream (V1 → V2 → V4 → inferotemporal cortex) processes object identity — shape, color, and faces — answering 'what is it?' Damage produces visual agnosia, where patients can see clearly but cannot recognize or identify objects. Options A and B describe dorsal stream deficits: the dorsal stream (V1 → V2 → MT → parietal cortex) processes motion and spatial location — answering 'where is it?' Optic ataxia (impaired visually guided reaching) and motion perception deficits result from dorsal stream damage. The double dissociation between the two streams is one of the strongest pieces of evidence for their functional independence."

- question: "Why are retinal ganglion cells with center-surround receptive fields described as 'contrast detectors' rather than 'light detectors'?"
  type: multiple-choice
  options:
    - "Because they only respond to colored light, not white light"
    - "Because uniform illumination activates center and surround equally, producing little net response, while edges produce strong differential responses"
    - "Because they fire in proportion to the total number of photons hitting the retina"
    - "Because they are inhibited by any light stimulus, firing maximally in darkness"
  answer: 1
  explanation: "Center-surround organization means that a ganglion cell is excited by light in its center and inhibited by light in its surround (or vice versa for off-center cells). When uniform light illuminates the entire receptive field, the excitatory and inhibitory inputs partially cancel, yielding a weak response. But at an edge — where one side is bright and the other is dark — the center-surround imbalance is maximized, producing a strong response. This is why the retina emphasizes spatial discontinuities (edges, contours) and why you can read in dim light: contrast structure, not absolute brightness, drives perception."

- question: "Damage to the dorsal visual stream would most likely impair a patient's ability to recognize faces."
  type: true-false
  answer: false
  explanation: "Face recognition is a function of the ventral stream, specifically inferotemporal (IT) cortex. The dorsal stream (projecting through MT/V5 to parietal cortex) processes spatial location, motion, and the visual guidance of action — answering 'where is it and how do I interact with it?' Impairment of the dorsal stream produces optic ataxia (difficulty directing hand movements to objects) or motion perception deficits, not face blindness. Prosopagnosia (face recognition failure) is a ventral stream deficit. The two-stream distinction is clinically confirmed by patients who can recognize objects but cannot reach for them, and vice versa."

- question: "Retinal ganglion cells are maximally responsive to local contrast rather than to absolute light levels, allowing the visual system to function across a wide range of illumination conditions."
  type: true-false
  answer: true
  explanation: "Center-surround receptive fields implement a form of local adaptation: what matters is not the total light falling on the retina but the difference between brightness in the center and surround. This explains a well-known phenomenon: the same gray patch looks lighter or darker depending on its surrounding context. The retina sends a contrast-encoded, edge-emphasized signal to the brain, not a raw brightness map. This design compresses the enormous dynamic range of natural scenes into a manageable neural signal while preserving the spatial structure needed for object recognition."

- question: "Explain how the two major visual processing streams — ventral and dorsal — differ in function, and give an example of the kind of deficit that results from damage to each."
  type: short-answer
  answer: "The ventral stream (V1 → V4 → IT cortex) processes object identity — what something is, including shape, color, and faces. Damage causes visual agnosia: a patient can see but cannot identify objects or recognize faces despite intact basic vision. The dorsal stream (V1 → MT → parietal cortex) processes spatial location and visually guided action — where something is and how to interact with it. Damage causes optic ataxia: a patient can recognize objects but cannot accurately reach or point to them. The double dissociation shows these are functionally distinct systems for 'what' vs 'where/how.'"
  explanation: "The two-stream model explains why vision is not a single unified sense but a collection of parallel specialized processes. The dissociation becomes most apparent in neurological patients — someone with ventral damage can reach accurately for objects they cannot name, while someone with dorsal damage can name objects they cannot reach. This implies the streams operate with considerable independence, each extracting different aspects of the visual scene for different purposes."
```

## Explainer

You already know that sensory transduction converts physical energy into neural signals, and from your study of photoreceptors you know that **rods** are sensitive to low light intensities while **cones** (concentrated in the fovea) mediate color vision and fine spatial detail. The important insight here is that the retina is not a passive camera sensor — it is an active preprocessing station that performs significant computation before signals ever leave the eye.

The key structure enabling this preprocessing is the **center-surround receptive field** of retinal ganglion cells. Retinal circuits wire photoreceptors through bipolar and horizontal cells such that each ganglion cell is excited by light in a small central region and inhibited by light in a surrounding annulus (or vice versa). This arrangement makes ganglion cells maximally sensitive to local contrast rather than absolute light levels — they fire vigorously at edges (where brightness shifts abruptly) and are relatively indifferent to uniform illumination. This is why you can read in a dimly lit room: your visual system extracts contrast structure, not raw brightness. The retina thus sends a compressed, edge-emphasized representation of the visual scene down the optic nerve.

Signals from the two optic nerves partially cross at the **optic chiasm** — fibers from the nasal retina (carrying temporal visual field information) cross to the opposite hemisphere, while temporal retina fibers stay ipsilateral. The result is that everything in your left visual field is processed by your right hemisphere and vice versa. Signals then relay through the **lateral geniculate nucleus** (LGN) of the thalamus, which is organized into six layers: the two magnocellular (M) layers carry motion and coarse spatial information; the four parvocellular (P) layers carry color and fine detail. This segregation is maintained into cortex.

In **primary visual cortex (V1)**, neurons respond to oriented edges — a breakthrough discovered by Hubel and Wiesel using moving light bars. **Simple cells** have elongated receptive fields that respond to edges at a specific orientation and location; **complex cells** are less position-specific but still orientation-selective. V1 is organized retinotopically: neighboring neurons respond to neighboring locations in the visual field, with the fovea overrepresented. Beyond V1, visual processing diverges into two major streams. The **ventral stream** (V1 → V2 → V4 → IT cortex) processes object identity — shape, color, faces — answering "what is it?" The **dorsal stream** (V1 → V2 → MT/V5 → parietal cortex) processes spatial location and motion — answering "where is it and how do I interact with it?" Damage to these streams selectively impairs different capacities: ventral stream damage produces visual agnosia (inability to recognize objects); dorsal stream damage produces optic ataxia (inability to guide actions to objects) despite intact recognition.
