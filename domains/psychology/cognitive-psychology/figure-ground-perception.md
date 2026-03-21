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
stage: advanced
status: draft
---

# Figure-Ground Segmentation

## Core Idea
Figure-ground segmentation is the perceptual ability to separate foreground objects (figure) from background (ground). This fundamental organizing principle allows us to isolate relevant objects from complex visual scenes despite ambiguous physical boundaries, driven by both stimulus properties and top-down expectations.

## Questions

```yaml
- question: "A researcher shows participants an image where a small, convex, symmetrical region sits inside a larger surrounding area. Which region will most viewers perceive as the figure, and why?"
  type: multiple-choice
  options:
    - "The larger surrounding area — it dominates the visual field and thus captures figure status"
    - "The small, convex, symmetrical region — smallness, convexity, and symmetry all bias the visual system toward assigning figure status"
    - "Both regions equally — figure-ground assignment requires deliberate attention"
    - "Neither region — figure-ground only emerges with recognizable objects"
  answer: 1
  explanation: "Smallness, convexity, and symmetry are stimulus properties that reliably bias the visual system toward assigning figure status. The larger surrounding region tends to be perceived as ground. The common misconception is that the larger or more visually dominant region becomes the figure — in fact, it is typically the opposite: figures tend to be smaller, bounded regions surrounded by a ground."

- question: "What does the fact that viewers cannot perceive both interpretations of Rubin's vase simultaneously reveal about figure-ground segmentation?"
  type: multiple-choice
  options:
    - "That one interpretation is objectively correct and the other is an illusion"
    - "That figure-ground assignment is made by the visual system, and competing assignments are mutually suppressive — not properties of the stimulus itself"
    - "That the visual system requires prior knowledge of vases to resolve the ambiguity"
    - "That figure-ground segmentation is a learned skill that improves with practice"
  answer: 1
  explanation: "The mutual exclusivity of the two percepts is the key insight: you cannot see vase AND faces at the same time. This proves that figure and ground are not properties of the light pattern but interpretive assignments made by the visual system. The competing neural representations (border ownership signals assigned to opposite sides) are mutually suppressive — when one wins, the other is inhibited. The physical stimulus is unchanged throughout; only the brain's assignment shifts."

- question: "Figure and ground are objective properties of a visual scene — they are determined by the physical contrast between regions in the image."
  type: true-false
  answer: false
  explanation: "Figure and ground are perceptual assignments made by the visual system, not objective properties of the stimulus. Ambiguous figures like Rubin's vase demonstrate this: the same physical image produces two different percepts depending on how the visual system assigns figure and ground status. Border ownership neurons in V2/V4 encode which side of a contour belongs to the figure — and this can be reversed for the same contour. The percept is a construction, not a readout."

- question: "Figure-ground segmentation must occur before other Gestalt grouping principles like continuity or closure can operate, because grouping principles apply to surfaces and objects — and surfaces must first be assigned to either figure or ground."
  type: true-false
  answer: true
  explanation: "This is the hierarchical logic of perceptual organization. You cannot apply continuity (grouping elements along a smooth path) or closure (completing incomplete contours into objects) until you have first decided which regions belong to figures and which belong to ground. Figure-ground segmentation is the foundation of visual object processing — it separates the 'what' (the figure to be recognized) from the contextual background."

- question: "Why is figure-ground segmentation considered more fundamental than other Gestalt grouping principles, and what neural mechanism underlies the assignment of figure status?"
  type: short-answer
  answer: "Figure-ground segmentation is more fundamental because all other perceptual grouping operations (proximity, similarity, continuity, closure) apply to objects — and objects must first be isolated from their background before they can be organized. Neurally, border ownership signals in areas V2 and V4 encode not just the presence of a contour but which side of the contour belongs to the figure. Two neurons responding to the same edge with opposite border ownership assignments encode entirely different perceptual interpretations."
  explanation: "The key is the logical priority: you cannot ask 'how are these elements grouped?' until you have answered 'which elements belong to foreground objects and which belong to the background?' Border ownership neurons are the neural substrate of this assignment — they were discovered by Rüdiger von der Heydt and are among the clearest examples of how perception involves active interpretation rather than passive registration."
```

## Explainer

From your study of Gestalt principles, you know that the visual system spontaneously organizes sensory inputs into structured wholes using rules like proximity, similarity, continuity, and closure. Figure-ground segmentation is the most fundamental of all perceptual organizing operations — it is what the visual system must accomplish before any of the other Gestalt grouping rules can even operate. You cannot apply continuity or closure to a set of contours until you have first decided which surfaces belong to objects (the **figure**) and which belong to the background (the **ground**).

Several stimulus properties bias the visual system toward assigning figure status. Regions that are **smaller** tend to be seen as figure; the larger surrounding region tends to be ground. **Convex** contours (curves that bulge outward) are more likely to be assigned to figures than concave contours. **Symmetry** promotes figure assignment. Regions that are **lower in the visual field** tend to be seen as figure (consistent with objects resting on surfaces). **Motion** powerfully segregates figure from ground — a region that moves independently from its surroundings almost always captures figure status. None of these cues is infallible, and when they conflict, the visual system must resolve the ambiguity through a competitive process among candidate interpretations.

The classic demonstrations of figure-ground ambiguity — **Rubin's vase** (which alternates between two profiles and a vase), or Escher's interlocking tessellations — are informative precisely because they reveal what is normally invisible: the perceptual system is always making an interpretive decision, not merely reading off objective properties of the image. The alternating percepts in ambiguous figures share the same physical stimulus, proving that figure and ground are assignments made by the visual system, not properties of the light pattern itself. You cannot see both interpretations simultaneously, which indicates that the neural representations of "figure" and "ground" are mutually suppressive.

At the neural level, **border ownership signals** in areas V2 and V4 are central to figure-ground computation. Neurons in these areas respond to contours but also encode which side of the contour belongs to the figure — two neurons responding to the same edge but with opposite border ownership assignments signal entirely different perceptual interpretations. These border ownership signals emerge quickly (within ~25 ms of the initial response) but are strongly modulated by **top-down feedback** from higher areas: prior knowledge, context, and attention can tip the figure-ground competition in one direction. Understanding figure-ground is essential for what comes next — object recognition depends on first isolating the object from its background, segmenting its boundaries, and computing the surface properties that define its shape.
