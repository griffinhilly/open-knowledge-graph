---
id: euler-circuits-applications
title: Euler Paths, Euler Circuits, and Applications
domain: mathematics
course: discrete-math
prerequisites:
- id: euler-paths-circuits
  type: hard
builds-toward:
- hamiltonian-cycles-discrete
tags:
- Euler-path
- Euler-circuit
- degree
- Chinese-postman
stage: formal-systems
status: draft
---

# Euler Paths, Euler Circuits, and Applications

## Core Idea
An Euler path visits every edge exactly once; an Euler circuit closes back to its start. A connected graph has an Euler circuit iff all vertices have even degree; an Euler path exists iff exactly 0 or 2 vertices have odd degree. The Chinese postman problem seeks a shortest walk covering all edges.

## How It's Best Learned
Check degree conditions to determine Euler path/circuit existence before searching. Construct Euler circuits using Hierholzer's algorithm. Apply to street traversal (postman, parade routes) and circuit design.

## Common Misconceptions
Euler paths traverse edges, not vertices. A graph can have many Euler paths/circuits if the conditions hold. The bridge-crossing puzzle (Königsberg) famously has no Euler circuit.
