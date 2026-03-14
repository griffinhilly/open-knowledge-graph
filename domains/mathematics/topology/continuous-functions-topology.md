---
id: continuous-functions-topology
title: Continuous Functions in Topological Spaces
domain: mathematics
course: topology
prerequisites:
- id: open-sets-topology
  type: hard
- id: closed-sets-topology
  type: soft
builds-toward:
- homeomorphisms-topological-equivalence
- open-and-closed-maps
tags:
- functions
- continuity
stage: advanced
status: draft
---

# Continuous Functions in Topological Spaces

## Core Idea
f : X → Y is continuous if preimages of open sets in Y are open in X. Equivalently, preimages of closed sets are closed. This topological definition abstracts the ε-δ definition and depends only on topology, not distance.

## How It's Best Learned
Verify that ε-δ continuity on ℝ matches the topological definition. Then explore unusual topologies where standard functions become discontinuous (or continuous).

## Common Misconceptions
- Thinking 'image of open is open' defines continuity (that's an open map, not continuous).
- Assuming continuity requires a metric (topology suffices).
