---
id: connectedness-definition-examples
title: 'Connectedness: Definition and Examples'
domain: mathematics
course: topology
prerequisites:
- id: open-sets-in-topological-spaces
  type: hard
- id: closed-sets-in-topological-spaces
  type: hard
builds-toward:
- path-connectedness
- connected-components
tags:
- connectedness
- connected-spaces
- disconnected
stage: advanced
status: draft
---

# Connectedness: Definition and Examples

## Core Idea
A topological space is connected if it cannot be written as a union of two disjoint nonempty open sets. Equivalently, the only subsets that are both open and closed (clopen) are the empty set and the whole space. Connectedness captures the intuitive idea that a space is "in one piece." The real line ℝ is connected, but ℝ minus a point is not—removing any point splits it into two open rays. The continuous image of a connected space is connected, which is why the intermediate value theorem holds: a continuous function on a connected domain cannot skip values. Connectedness is a topological invariant preserved under homeomorphisms.

## How It's Best Learned
Prove that ℝ is connected using the least upper bound property, then show ℚ is disconnected by exhibiting a clopen set. Working through these two cases builds a concrete understanding of the definition before moving to more exotic spaces.

## Common Misconceptions
Connected does not mean path-connected. The topologist's sine curve is connected but not path-connected. Students also sometimes think removing a point always disconnects a space—this is true for ℝ but false for ℝ² (which remains connected after removing any single point).

