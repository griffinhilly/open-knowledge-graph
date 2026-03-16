---
id: figure-ground-perception
title: Figure-Ground Segmentation
domain: psychology
course: cognitive-psychology
prerequisites:
- id: perceptual-organization-gestalt-principles
  type: hard
- id: visual-cortex-hierarchical-organization
  type: soft
builds-toward:
- visual-object-recognition-categorical
tags:
- perception
- visual
- segmentation
stage: formal-systems
status: draft
---

# Figure-Ground Segmentation

## Core Idea
Figure-ground segmentation is the perceptual ability to separate foreground objects (figure) from background (ground). This fundamental organizing principle allows us to isolate relevant objects from complex visual scenes despite ambiguous physical boundaries, driven by both stimulus properties and top-down expectations.

## Explainer

From your study of Gestalt principles, you know that the visual system spontaneously organizes sensory inputs into structured wholes using rules like proximity, similarity, continuity, and closure. Figure-ground segmentation is the most fundamental of all perceptual organizing operations — it is what the visual system must accomplish before any of the other Gestalt grouping rules can even operate. You cannot apply continuity or closure to a set of contours until you have first decided which surfaces belong to objects (the **figure**) and which belong to the background (the **ground**).

Several stimulus properties bias the visual system toward assigning figure status. Regions that are **smaller** tend to be seen as figure; the larger surrounding region tends to be ground. **Convex** contours (curves that bulge outward) are more likely to be assigned to figures than concave contours. **Symmetry** promotes figure assignment. Regions that are **lower in the visual field** tend to be seen as figure (consistent with objects resting on surfaces). **Motion** powerfully segregates figure from ground — a region that moves independently from its surroundings almost always captures figure status. None of these cues is infallible, and when they conflict, the visual system must resolve the ambiguity through a competitive process among candidate interpretations.

The classic demonstrations of figure-ground ambiguity — **Rubin's vase** (which alternates between two profiles and a vase), or Escher's interlocking tessellations — are informative precisely because they reveal what is normally invisible: the perceptual system is always making an interpretive decision, not merely reading off objective properties of the image. The alternating percepts in ambiguous figures share the same physical stimulus, proving that figure and ground are assignments made by the visual system, not properties of the light pattern itself. You cannot see both interpretations simultaneously, which indicates that the neural representations of "figure" and "ground" are mutually suppressive.

At the neural level, **border ownership signals** in areas V2 and V4 are central to figure-ground computation. Neurons in these areas respond to contours but also encode which side of the contour belongs to the figure — two neurons responding to the same edge but with opposite border ownership assignments signal entirely different perceptual interpretations. These border ownership signals emerge quickly (within ~25 ms of the initial response) but are strongly modulated by **top-down feedback** from higher areas: prior knowledge, context, and attention can tip the figure-ground competition in one direction. Understanding figure-ground is essential for what comes next — object recognition depends on first isolating the object from its background, segmenting its boundaries, and computing the surface properties that define its shape.
