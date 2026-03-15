---
id: connectivity-components-discrete
title: Connectivity and Connected Components
domain: mathematics
course: discrete-math
prerequisites:
- id: connected-components
  type: hard
- id: graph-fundamentals-discrete
  type: hard
builds-toward:
- trees-and-tree-properties
tags:
- connectivity
- components
- bridges
- articulation-points
stage: formal-systems
status: draft
---

# Connectivity and Connected Components

## Core Idea
A graph is connected if a path exists between any two vertices. Connected components partition vertices into maximal connected subgraphs. Bridges are edges whose removal increases the number of components; articulation points are vertices with this property.

## How It's Best Learned
Use depth-first search (DFS) or breadth-first search (BFS) to find connected components. Identify bridges and articulation points algorithmically. Recognize that a connected graph on n vertices has at least n−1 edges (a tree).

## Common Misconceptions
Being connected is not the same as being complete. A tree is minimally connected (n vertices, n−1 edges). A single isolated vertex is its own component.
