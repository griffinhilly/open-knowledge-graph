---
id: walks-paths-cycles
title: Walks, Trails, Paths, and Cycles in Graphs
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-connectivity-components
  type: hard
builds-toward:
- euler-paths-circuits
- hamiltonian-paths-cycles
tags:
- graph-theory
- walks-paths
stage: formal-systems
status: draft
---

# Walks, Trails, Paths, and Cycles in Graphs

## Core Idea
A walk is a sequence of vertices where consecutive vertices are connected by edges. A trail is a walk with distinct edges. A path is a walk with distinct vertices. A cycle is a closed walk with no repeated vertices (except first and last). These distinctions are fundamental in analyzing graph structure.

## Explainer

From your study of graph connectivity, you know that two vertices are connected when you can get from one to the other by following edges. But "getting from one to the other" can mean many different things depending on what you're allowed to revisit. The vocabulary of walks, trails, paths, and cycles draws these distinctions precisely, and the differences matter enormously for the theorems that follow.

A **walk** is the most permissive: a sequence of vertices v₀, v₁, …, vₖ where each consecutive pair is adjacent. Nothing is forbidden — you may traverse the same edge multiple times, visit the same vertex multiple times, anything goes. A **trail** adds one restriction: all edges must be distinct. You can still revisit a vertex, but you cannot travel the same edge twice. Think of a trail as "the roads I've driven with no repeated roads." A **path** is stricter still: all vertices must be distinct (which automatically means all edges are distinct too, since revisiting a vertex would require revisiting an incident edge or a self-loop). A path is the "road trip where I never enter the same city twice."

A **cycle** is a closed path: you start and end at the same vertex, and all intermediate vertices are distinct. A closed trail (returning to start with no repeated edges but possibly repeated vertices) is called an **Eulerian circuit**, which is the subject of the next topic in your graph theory sequence. The hierarchy is clean: every path is a trail, every trail is a walk, but not every walk is a trail and not every trail is a path.

Why do these distinctions matter? Many graph problems are stated as: "does there exist a walk/trail/path of type X?" and the answer can be radically different for each type. A graph has an **Eulerian trail** (traversing every edge exactly once) if and only if it has exactly 0 or 2 vertices of odd degree — a beautiful theorem that depends entirely on the "no repeated edges" requirement. By contrast, finding a **Hamiltonian path** (visiting every vertex exactly once) is NP-complete in general — a structurally similar question that is computationally intractable. The distinction between these two classical problems is precisely the distinction between trails and paths: same spirit, wildly different difficulty. Getting the vocabulary right is the prerequisite to stating these theorems precisely.
