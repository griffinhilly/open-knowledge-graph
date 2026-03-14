---
id: articulation-points-cut-vertices
title: Articulation Points and Bridges in Graphs
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: depth-first-search
  type: hard
tags:
- graphs
- articulation
- connectivity
stage: formal-systems
status: draft
---

# Articulation Points and Bridges in Graphs

## Core Idea
An articulation point (cut vertex) is a vertex whose removal disconnects the graph. A bridge is an edge with the same property. Tarjan's algorithm identifies them in a single DFS pass by tracking discovery time and lowest reachable time. Critical for network reliability and resilience.

## How It's Best Learned
Implement DFS-based articulation point detection. Verify on graphs with known cut vertices (e.g., a tree has internal nodes as articulation points). Apply to network reliability problems.

## Common Misconceptions
- Assuming high-degree vertices are always articulation points; degree alone doesn't determine criticality.
- Not understanding why discovery and low times suffice; the key insight is reachability to descendants.
- Forgetting special cases like the root of the DFS tree and bridges.
