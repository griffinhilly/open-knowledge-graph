---
id: connected-components
title: Connected Components
domain: mathematics
course: topology
prerequisites:
- id: connectedness-definition-examples
  type: hard
builds-toward:
- fundamental-group-definition
tags:
- components
- equivalence-classes
- decomposition
stage: advanced
status: draft
---

# Connected Components

## Core Idea
The connected component of a point x is the largest connected subset containing x—formally, the union of all connected subsets that contain x. Connected components partition any topological space into maximal connected pieces, and they are always closed sets. This decomposition reveals the global structure of a space: a space is connected if and only if it has exactly one component. In totally disconnected spaces like the Cantor set, every component is a single point. The number and nature of connected components provide a coarse but powerful topological invariant.

## How It's Best Learned
Draw examples: identify the components of the real line minus a few points, then of a union of disjoint circles. Move to the topologist's sine curve to see that components can be connected but not path-connected, sharpening the distinction.

## Common Misconceptions
Students often assume connected components must be open—they are always closed but not necessarily open. Also, path-components and connected components can differ; path-connectedness is strictly stronger than connectedness.

