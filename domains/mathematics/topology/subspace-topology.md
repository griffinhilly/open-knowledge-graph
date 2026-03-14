---
id: subspace-topology
title: Subspace Topology
domain: mathematics
course: topology
prerequisites:
- id: topological-spaces-definition
  type: hard
builds-toward:
- metric-topology
tags:
- constructions
- subsets
stage: advanced
status: draft
---

# Subspace Topology

## Core Idea
For a subset A of topological space (X, τ), the subspace topology is τ_A = {U ∩ A : U ∈ τ}. Open sets in A are precisely intersections of A with open sets in X. This is the natural way to topologize any subset, ensuring open sets in A correspond to points 'locally around them' in X.
