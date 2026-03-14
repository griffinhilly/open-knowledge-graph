---
id: continuity-topological-definition
title: Continuity in Topological Spaces
domain: mathematics
course: topology
prerequisites:
- id: open-sets-definition-examples
  type: hard
- id: neighborhoods-topology-definition
  type: soft
builds-toward:
- homeomorphisms-definition-properties
- quotient-maps-definition
tags:
- continuity
- maps
stage: abstract-reasoning
status: draft
---

# Continuity in Topological Spaces

## Core Idea
A function f: X → Y is continuous if the preimage of every open set in Y is open in X. Equivalently: the preimage of every closed set is closed; f is continuous at x if for every neighborhood V of f(x), there exists a neighborhood U of x with f(U) ⊆ V. This generalizes ε-δ continuity and is the natural definition in topology.
