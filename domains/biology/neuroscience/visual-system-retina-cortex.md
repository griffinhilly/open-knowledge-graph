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
status: draft
---

# Visual System: Retina to Visual Cortex

## Core Idea
Light activates photoreceptors → bipolar cells → ganglion cells → optic nerve → LGN → V1. Ganglion cells have center-surround fields. V1 neurons tuned to orientation, direction, spatial frequency.

## Explainer

From your study of neuron structure and synaptic transmission, you know that neurons communicate through electrical impulses converted into chemical signals at synapses. The visual system applies this machinery to an extraordinary task: transforming patterns of light into a neural representation of the world. The process begins in the **retina**, a thin sheet of neural tissue lining the back of the eye. The retina is not merely a camera sensor — it is a piece of brain tissue that performs substantial computation before any signal leaves the eye.

Light first strikes the **photoreceptors** — rods and cones — at the back of the retina. Rods handle dim-light vision and are exquisitely sensitive, while cones operate in bright light and come in three types tuned to different wavelengths, enabling color vision. When light hits a photoreceptor, it triggers a biochemical cascade that hyperpolarizes the cell (an unusual feature — most neurons depolarize when activated). This signal passes through **bipolar cells** to **retinal ganglion cells**, whose axons bundle together to form the optic nerve. Crucially, the retina also contains horizontal cells and amacrine cells that create lateral interactions, setting up the first stage of visual processing: the **center-surround receptive field**. Each ganglion cell responds best not to uniform illumination but to a spot of light surrounded by darkness (ON-center) or a dark spot surrounded by light (OFF-center). This means the retina is already encoding contrast and edges rather than raw brightness.

The axons of retinal ganglion cells travel through the optic nerve, partially cross at the **optic chiasm** (so that each hemisphere receives input from the opposite visual field), and synapse in the **lateral geniculate nucleus (LGN)** of the thalamus. The LGN preserves the retinotopic map — neighboring points in visual space are represented by neighboring neurons — and organizes inputs into layers that separate the two eyes and different processing streams (magnocellular for motion and contrast, parvocellular for color and fine detail). From the LGN, signals project to the **primary visual cortex (V1)** at the back of the brain.

In V1, the computational sophistication increases dramatically. Instead of responding to spots of light, V1 neurons are tuned to **oriented edges** — a cell might fire vigorously for a vertical bar at a specific location but not at all for a horizontal one. This orientation selectivity emerges from the convergence of multiple LGN inputs with aligned center-surround fields. Some V1 neurons are **simple cells** with clearly defined excitatory and inhibitory zones, while **complex cells** respond to oriented edges regardless of exact position within their receptive field and are often sensitive to the direction of motion. V1 also contains neurons tuned to **spatial frequency** (fine versus coarse patterns) and **binocular disparity** (the slight difference between the two eyes' views, which enables depth perception). The progression from photoreceptor to V1 illustrates a fundamental principle of sensory processing: each stage extracts increasingly abstract features from the raw input, building the foundation for object recognition, motion perception, and spatial awareness in higher visual areas.
