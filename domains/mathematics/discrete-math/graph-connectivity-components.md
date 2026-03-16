---
id: graph-connectivity-components
title: Connectivity and Connected Components
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-theory-fundamentals
  type: hard
builds-toward:
- walks-paths-cycles
- euler-paths-circuits
tags:
- graph-theory
- connectivity
stage: formal-systems
status: draft
---

# Connectivity and Connected Components

## Core Idea
A graph is connected if there exists a path between every pair of vertices. Connected components are maximal connected subgraphs. Vertex connectivity and edge connectivity measure how many vertices or edges must be removed to disconnect a graph.

## Explainer

You already know that a graph is a collection of **vertices** (nodes) and **edges** (connections between them). Connectivity is about asking a deceptively simple question: can you get from any vertex to any other vertex by traveling along edges? If yes, the graph is **connected**. If some pairs of vertices have no path between them — think of islands with no bridges — the graph is **disconnected**.

The useful structure inside a disconnected graph is its **connected components**: the maximal chunks that are internally connected. "Maximal" means you've included every vertex you can reach — you can't expand the component any further without leaving the connected region. Think of a social network where some people know each other and others are completely unaware of each other's existence. Each isolated social circle is a connected component. Every vertex belongs to exactly one component, and the components partition the graph.

Once you understand what connectivity means, the natural follow-up is: how *robust* is it? Two key measures capture this. **Edge connectivity** κ'(G) is the minimum number of edges you'd need to remove to disconnect the graph (or isolate a vertex). **Vertex connectivity** κ(G) is the minimum number of vertices whose removal disconnects the graph. Intuitively, a graph where you can sever it by removing just one edge (called a **bridge**) is fragile; a graph where you'd need to remove many edges is robust. These measures matter in network design — an internet router network needs high connectivity so that no single cable failure splits the network.

There's a useful inequality relating these measures: κ(G) ≤ κ'(G) ≤ δ(G), where δ(G) is the minimum vertex degree. This says vertex connectivity is the hardest to achieve: removing vertices is strictly more powerful than removing edges (because removing a vertex also removes all its incident edges). A graph achieving κ(G) = δ(G), like the complete graph Kₙ, is as connected as theoretically possible given its minimum degree. These ideas feed directly into the study of Euler paths, which require specific connectivity conditions to exist.
