---
id: visual-system-retina-cortex
title: 'Visual System: Retina to Visual Cortex'
domain: biology
course: neuroscience
prerequisites:
- id: synaptic-transmission
  type: hard
- id: neuron-structure-and-function
  type: hard
tags:
- sensory-systems
- vision
stage: advanced
status: validated
---

# Visual System: Retina to Visual Cortex

## Core Idea
Light activates photoreceptors → bipolar cells → ganglion cells → optic nerve → LGN → V1. Ganglion cells have center-surround fields. V1 neurons tuned to orientation, direction, spatial frequency.

## Questions

```yaml
- question: "An ON-center retinal ganglion cell is tested with three stimuli: (A) uniform bright light over its entire receptive field, (B) a small bright spot covering only the center, (C) a small bright spot covering only the surround. Which produces the strongest response?"
  type: multiple-choice
  options:
    - "A — the cell responds to overall brightness, so more light is always better"
    - "B — the center-surround organization means the cell responds best to a bright spot in its center with no surround stimulation"
    - "C — the surround region is larger and therefore drives the cell more strongly"
    - "A and B equally — spot and diffuse illumination produce identical responses"
  answer: 1
  explanation: "ON-center cells are designed to encode contrast, not absolute brightness. The surround exerts inhibition via horizontal cells; illuminating it suppresses the cell's response. A small bright spot on the center with a dark surround provides maximum excitation from the center with no inhibitory cancellation from the surround — the optimal stimulus. Uniform illumination (stimulus A) is actually a poor driver because the surround inhibition partially cancels the center excitation. This center-surround organization explains why the visual system is so sensitive to edges and borders while being relatively indifferent to overall illumination levels."

- question: "How does simple cell orientation selectivity in V1 arise from inputs with circular, non-oriented receptive fields?"
  type: multiple-choice
  options:
    - "V1 cells receive orientation information directly from specialized photoreceptors tuned to different angles"
    - "A simple cell receives excitatory input from a row of LGN neurons whose circular center-surround fields are spatially aligned; an edge at that orientation simultaneously activates all of them"
    - "Orientation selectivity is created by feedback connections from higher visual areas back to V1"
    - "V1 cells inherit orientation selectivity from the LGN, which already processes oriented edges"
  answer: 1
  explanation: "This is Hubel and Wiesel's explanation: simple cells in V1 receive convergent input from multiple LGN neurons whose circular center-surround fields happen to be arranged in a straight line across the visual field. An edge oriented along that line simultaneously falls on the center of each LGN neuron, producing a strong combined response. An edge perpendicular to the line stimulates some centers and some surrounds, producing a weak net response. LGN neurons themselves have circular, non-oriented receptive fields — orientation selectivity is an emergent property of the convergent wiring in V1."

- question: "The retina functions primarily as a passive sensor that transmits a faithful pixel-by-pixel representation of the visual image to the brain for later processing."
  type: true-false
  answer: false
  explanation: "The retina is a piece of brain tissue that performs substantial computation before any signal leaves the eye. Center-surround receptive fields — set up by lateral inhibition from horizontal and amacrine cells — already encode local contrast rather than raw brightness. The retina doesn't send a picture; it sends a spatial map emphasizing edges, borders, and changes in illumination. By the time signals leave the optic nerve, significant feature extraction has already occurred. The analogy to a camera sensor is misleading: a camera captures raw intensity values, while the retina transmits a processed representation of spatial contrast."

- question: "After the partial decussation at the optic chiasm, each cerebral hemisphere primarily receives visual input from the opposite visual hemifield (from both eyes), rather than from the opposite eye."
  type: true-false
  answer: true
  explanation: "At the optic chiasm, axons from the nasal half of each retina (which sees the temporal visual field) cross to the opposite hemisphere, while axons from the temporal half of each retina (which sees the nasal visual field) stay ipsilateral. The result is that the left hemisphere receives all input from the right visual field — from the temporal retina of the right eye and the nasal retina of the left eye — and vice versa. The organizing principle is visual hemifield, not eye. This is why a lesion in the right primary visual cortex causes blindness in the left visual field of both eyes."

- question: "Why do retinal ganglion cells encode contrast through center-surround receptive fields rather than simply responding to absolute light intensity, and why is this computationally useful?"
  type: short-answer
  answer: "Absolute light intensity varies enormously with overall illumination (a white page looks very different in sunlight vs. dim room), but the information needed for object recognition lies in spatial contrasts — the differences between adjacent regions that mark edges, borders, and surfaces. Center-surround organization, created by lateral inhibition from horizontal cells, makes ganglion cells selective for local contrast: they respond strongly when the center and surround receive different illumination levels (as at an edge) but weakly when both are uniformly lit. This makes the retinal output largely invariant to changes in overall illumination while highlighting the spatially structured differences that the brain needs. It is an efficient solution to the dynamic range problem: the visual system operates across a million-fold range of light intensities, and encoding contrast rather than absolute intensity allows meaningful responses throughout that range."
  explanation: "Center-surround organization also contributes to edge enhancement: a boundary between a light and dark region is emphasized because the ganglion cells at the boundary have their center and surround differentially stimulated. This pre-processing in the retina reduces the information the brain must process by discarding redundant (uniform) regions and highlighting informative (boundary) regions — a principle related to efficient coding theory."
```

## Explainer

From your study of neuron structure and synaptic transmission, you know that neurons communicate through electrical impulses converted into chemical signals at synapses. The visual system applies this machinery to an extraordinary task: transforming patterns of light into a neural representation of the world. The process begins in the **retina**, a thin sheet of neural tissue lining the back of the eye. The retina is not merely a camera sensor — it is a piece of brain tissue that performs substantial computation before any signal leaves the eye.

Light first strikes the **photoreceptors** — rods and cones — at the back of the retina. Rods handle dim-light vision and are exquisitely sensitive, while cones operate in bright light and come in three types tuned to different wavelengths, enabling color vision. When light hits a photoreceptor, it triggers a biochemical cascade that hyperpolarizes the cell (an unusual feature — most neurons depolarize when activated). This signal passes through **bipolar cells** to **retinal ganglion cells**, whose axons bundle together to form the optic nerve. Crucially, the retina also contains horizontal cells and amacrine cells that create lateral interactions, setting up the first stage of visual processing: the **center-surround receptive field**. Each ganglion cell responds best not to uniform illumination but to a spot of light surrounded by darkness (ON-center) or a dark spot surrounded by light (OFF-center). This means the retina is already encoding contrast and edges rather than raw brightness.

The axons of retinal ganglion cells travel through the optic nerve, partially cross at the **optic chiasm** (so that each hemisphere receives input from the opposite visual field), and synapse in the **lateral geniculate nucleus (LGN)** of the thalamus. The LGN preserves the retinotopic map — neighboring points in visual space are represented by neighboring neurons — and organizes inputs into layers that separate the two eyes and different processing streams (magnocellular for motion and contrast, parvocellular for color and fine detail). From the LGN, signals project to the **primary visual cortex (V1)** at the back of the brain.

In V1, the computational sophistication increases dramatically. Instead of responding to spots of light, V1 neurons are tuned to **oriented edges** — a cell might fire vigorously for a vertical bar at a specific location but not at all for a horizontal one. This orientation selectivity emerges from the convergence of multiple LGN inputs with aligned center-surround fields. Some V1 neurons are **simple cells** with clearly defined excitatory and inhibitory zones, while **complex cells** respond to oriented edges regardless of exact position within their receptive field and are often sensitive to the direction of motion. V1 also contains neurons tuned to **spatial frequency** (fine versus coarse patterns) and **binocular disparity** (the slight difference between the two eyes' views, which enables depth perception). The progression from photoreceptor to V1 illustrates a fundamental principle of sensory processing: each stage extracts increasingly abstract features from the raw input, building the foundation for object recognition, motion perception, and spatial awareness in higher visual areas.
