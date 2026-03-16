---
id: hippocampal-spatial-memory
title: Hippocampus and Spatial Memory
domain: biology
course: neuroscience
prerequisites:
- id: hippocampus-memory-consolidation
  type: hard
- id: long-term-potentiation
  type: hard
builds-toward:
- episodic-memory
- navigation
- cognitive-maps
tags:
- hippocampus
- place-cells
- grid-cells
stage: advanced
status: draft
---

# Hippocampus and Spatial Memory

## Core Idea
The hippocampus encodes spatial environments through place cells (firing in specific locations) and forms episodic memories. Place cell firing is driven by visual-vestibular input; remapping between environments is rapid. Grid cells in medial entorhinal cortex fire in triangular lattices, providing a metric for distance.

## How It's Best Learned
Record place cells while animals navigate. Map place fields and analyze remapping.

## Common Misconceptions
Hippocampus stores memories permanently—it consolidates for transfer to cortex. Place cells encode fixed maps—they flexibly remap.

## Explainer

You already know that the hippocampus plays a central role in memory consolidation — transforming short-term experiences into lasting memories through mechanisms involving long-term potentiation. Spatial memory is one of the most thoroughly studied examples of this function, and it reveals the hippocampus not just as a general-purpose memory device but as a system that builds and maintains **cognitive maps** of the environment.

The foundational discovery came from John O'Keefe in the 1970s: individual hippocampal neurons, now called **place cells**, fire selectively when an animal occupies a specific location in its environment. A given place cell might fire vigorously when a rat is in the northwest corner of a maze and remain silent everywhere else. That region of active firing is the cell's **place field**. Collectively, the population of active place cells forms a map — at any moment, the pattern of firing across the population tells you where the animal is. This is not a blueprint stored somewhere and read out; it is an emergent representation created by the coordinated activity of thousands of neurons, each contributing its spatial tuning. The mechanism depends on the same LTP-based synaptic strengthening you have already studied: repeated experience in an environment stabilizes the pattern of which cells fire where.

One of the most striking properties of place cells is **remapping**. When an animal is moved to a new environment — even one that looks similar — the hippocampus rapidly generates an entirely new map. A cell that fired in the northwest corner of room A might fire in the center of room B, or not at all. This is called **global remapping**, and it means each environment gets a distinct neural representation, preventing interference between spatial memories. Subtler changes (like altering the color of the walls) can produce **rate remapping**, where the same cells remain active in the same locations but change their firing rates, encoding that something about the context has changed without discarding the spatial framework.

The spatial picture became richer with the discovery of **grid cells** in the medial entorhinal cortex, which provides the hippocampus with its primary cortical input. Grid cells fire in a remarkably regular pattern: as an animal moves through space, each grid cell activates at multiple locations arranged in a perfect triangular (hexagonal) lattice. Different grid cells have lattices of different spacings and orientations, tiling the environment at multiple scales. Grid cells are thought to provide the hippocampus with a **metric framework** — a coordinate system for measuring distances and directions — while place cells use this input, combined with sensory landmarks, to create the unique maps for each environment. Together, place cells and grid cells form a neural positioning system that supports not only navigation but also the encoding of episodic memories, where spatial context ("where it happened") is a fundamental organizing dimension.
