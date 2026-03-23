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
stage: expert
status: validated
---

# Hippocampus and Spatial Memory

## Core Idea
The hippocampus encodes spatial environments through place cells (firing in specific locations) and forms episodic memories. Place cell firing is driven by visual-vestibular input; remapping between environments is rapid. Grid cells in medial entorhinal cortex fire in triangular lattices, providing a metric for distance.

## How It's Best Learned
Record place cells while animals navigate. Map place fields and analyze remapping.

## Common Misconceptions
Hippocampus stores memories permanently—it consolidates for transfer to cortex. Place cells encode fixed maps—they flexibly remap.

## Questions

```yaml
- question: "A rat learns to navigate maze A over several days, developing a stable pattern of place cell activity. It is then placed in maze B, which has the same shape but different wall colors and odors. What will happen to the place cell population?"
  type: multiple-choice
  options:
    - "The same place cells will fire in the same relative locations, since the maze shape is identical"
    - "The place cells will fire randomly until the rat learns the new maze"
    - "An entirely new map will be generated — cells that fired in maze A may fire in different locations or not at all in maze B"
    - "Place cells will be silent in maze B because the rat already has a map from maze A"
  answer: 2
  explanation: "This is global remapping: when an animal enters a genuinely novel environment, the hippocampus generates a completely new population-level map. Cells that fired in specific locations in maze A reorganize to new fields or go silent in maze B. This is not failure or confusion — it is the system's solution to the problem of memory interference. Each distinct environment gets a distinct neural representation, preventing the maps from overlapping and degrading. The remapping is rapid and complete, not gradual, and it means the hippocampus can store many separate spatial memories without them corrupting each other."

- question: "Grid cells in the medial entorhinal cortex are thought to contribute to spatial memory primarily by providing what to the hippocampus?"
  type: multiple-choice
  options:
    - "A catalog of visual landmarks from the environment"
    - "A metric coordinate framework — regularly spaced firing fields that allow distances and directions to be computed"
    - "Emotional salience signals that mark which locations in a map are important"
    - "Direct input from the vestibular system about head direction"
  answer: 1
  explanation: "Grid cells fire at multiple locations arranged in a precise triangular (hexagonal) lattice as an animal moves through space. Different grid cells have different lattice spacings and orientations, effectively tiling the environment at multiple scales. This regular, metric structure is thought to provide the hippocampus with a coordinate system for computing distances and directions — a kind of internal ruler. Place cells combine this metric input from grid cells with sensory landmark information to build unique, context-specific maps. Grid cells supply the geometric scaffold; place cells construct the environment-specific representation on top of it."

- question: "A single hippocampal place cell fires throughout an entire environment at a roughly uniform rate, signaling the animal's general presence in that space."
  type: true-false
  answer: false
  explanation: "Place cells are spatially tuned: each cell fires selectively within a restricted region of the environment called its place field, which might cover only a fraction of a large space. Outside the place field, the cell is largely silent. It is the *population* of place cells — each contributing its own localized firing — that provides a complete spatial map. At any location, only a subset of place cells are active, and the identity of that active subset uniquely encodes position. Thinking of spatial coding as distributed across a population is essential; no single cell represents the whole environment."

- question: "Global remapping — generating an entirely new place cell map for a novel environment — occurs rapidly and prevents spatial memories from different environments from interfering with each other."
  type: true-false
  answer: true
  explanation: "Global remapping is thought to be the hippocampus's solution to the interference problem: if the same cells fired in the same places across different environments, the maps would overlap and degrade. Instead, each environment gets an orthogonal (statistically independent) representation — the same cell population generates a completely different firing pattern configuration. This decorrelation means dozens or hundreds of distinct spatial memories can be stored without corrupting each other. The remapping is rapid (apparent within seconds of entering a new environment) and is one of the key computational advantages of the hippocampal spatial coding strategy."

- question: "Why is it inaccurate to say that the hippocampus permanently stores spatial memories, and what actually happens to those memories over time?"
  type: short-answer
  answer: "The hippocampus plays a time-limited role in spatial memory. It is critical for initially encoding spatial memories and for consolidation — the process of stabilizing and organizing memories during sleep and rest, involving hippocampal replay of place cell sequences. Over time, however, well-consolidated spatial memories are transferred to and can be retrieved from neocortical areas, particularly retrosplenial and parietal cortices. The hippocampus becomes less critical for accessing remote spatial memories (those formed long ago) while remaining essential for recent ones. Patients with hippocampal damage lose recently formed memories but can often still access old, well-consolidated ones — a temporal gradient that reflects this consolidation-and-transfer process."
  explanation: "This relates to the standard model of systems consolidation (Squire's model), where the hippocampus acts as a temporary binding site that gradually transfers representations to distributed cortical storage. The misconception that 'memories are stored in the hippocampus permanently' conflates the site of initial encoding and consolidation with the final storage location. For spatial memories in particular, the cortical storage eventually allows retrieval without hippocampal involvement."
```

## Explainer

You already know that the hippocampus plays a central role in memory consolidation — transforming short-term experiences into lasting memories through mechanisms involving long-term potentiation. Spatial memory is one of the most thoroughly studied examples of this function, and it reveals the hippocampus not just as a general-purpose memory device but as a system that builds and maintains **cognitive maps** of the environment.

The foundational discovery came from John O'Keefe in the 1970s: individual hippocampal neurons, now called **place cells**, fire selectively when an animal occupies a specific location in its environment. A given place cell might fire vigorously when a rat is in the northwest corner of a maze and remain silent everywhere else. That region of active firing is the cell's **place field**. Collectively, the population of active place cells forms a map — at any moment, the pattern of firing across the population tells you where the animal is. This is not a blueprint stored somewhere and read out; it is an emergent representation created by the coordinated activity of thousands of neurons, each contributing its spatial tuning. The mechanism depends on the same LTP-based synaptic strengthening you have already studied: repeated experience in an environment stabilizes the pattern of which cells fire where.

One of the most striking properties of place cells is **remapping**. When an animal is moved to a new environment — even one that looks similar — the hippocampus rapidly generates an entirely new map. A cell that fired in the northwest corner of room A might fire in the center of room B, or not at all. This is called **global remapping**, and it means each environment gets a distinct neural representation, preventing interference between spatial memories. Subtler changes (like altering the color of the walls) can produce **rate remapping**, where the same cells remain active in the same locations but change their firing rates, encoding that something about the context has changed without discarding the spatial framework.

The spatial picture became richer with the discovery of **grid cells** in the medial entorhinal cortex, which provides the hippocampus with its primary cortical input. Grid cells fire in a remarkably regular pattern: as an animal moves through space, each grid cell activates at multiple locations arranged in a perfect triangular (hexagonal) lattice. Different grid cells have lattices of different spacings and orientations, tiling the environment at multiple scales. Grid cells are thought to provide the hippocampus with a **metric framework** — a coordinate system for measuring distances and directions — while place cells use this input, combined with sensory landmarks, to create the unique maps for each environment. Together, place cells and grid cells form a neural positioning system that supports not only navigation but also the encoding of episodic memories, where spatial context ("where it happened") is a fundamental organizing dimension.
