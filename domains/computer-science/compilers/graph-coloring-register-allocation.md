---
id: graph-coloring-register-allocation
title: Graph Coloring Register Allocation
domain: computer-science
course: compilers
prerequisites:
- id: instruction-selection-techniques
  type: hard
- id: register-allocation
  type: hard
builds-toward:
- code-emission-target-generation
tags:
- register-allocation
- graph-coloring
- backend
stage: advanced
status: draft
---

# Graph Coloring Register Allocation

## Core Idea
Register allocation models the problem as a graph coloring problem: nodes are variables, edges connect variables that interfere (are live simultaneously), and colors are registers. Finding a k-coloring is NP-hard, so practical allocators use heuristics like spill-cost-driven node selection.

## How It's Best Learned
Implement graph-coloring register allocation including live variable analysis, interference graph construction, and spilling.
