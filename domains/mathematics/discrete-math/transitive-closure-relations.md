---
id: transitive-closure-relations
title: Transitive Closure and Reachability
domain: mathematics
course: discrete-math
prerequisites:
- id: binary-relations
  type: hard
- id: graph-theory-intro
  type: soft
builds-toward:
- reflexive-transitive-closure
tags:
- relations
- graph-theory
- closure
stage: formal-systems
status: draft
---

# Transitive Closure and Reachability

## Core Idea
The transitive closure of a relation R is the smallest transitive relation containing R. It adds edges wherever there is a path in the graph representation of R. The transitive closure can be computed using matrix multiplication (reaching all paths) or using DFS/BFS for reachability queries.
