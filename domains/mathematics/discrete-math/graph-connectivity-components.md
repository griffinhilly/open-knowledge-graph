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
status: validated
---

# Connectivity and Connected Components

## Core Idea
A graph is connected if there exists a path between every pair of vertices. Connected components are maximal connected subgraphs. Vertex connectivity and edge connectivity measure how many vertices or edges must be removed to disconnect a graph.

## Questions

```yaml
- question: "A social network graph has 1,000 vertices and 3 connected components. What does this tell you?"
  type: multiple-choice
  options:
    - "Exactly 3 vertices are isolated (have no edges connecting them to others)"
    - "There are 3 groups of vertices such that paths exist within each group but no path connects any vertex in one group to any vertex in another"
    - "The graph has exactly 997 edges, since each component contributes one fewer edge than vertices"
    - "Removing any single edge would split the graph into exactly 3 components"
  answer: 1
  explanation: "A connected component is a maximal set of vertices where every pair is connected by a path. Three components mean the 1,000 vertices partition into three groups: paths exist within each group, but no path connects a vertex in one group to any vertex in another. In social network terms, there are three isolated social circles with no links between them. Option A misidentifies isolated vertices with components (a component can be large). Option C misapplies the tree edge-count formula. Option D describes a bridge, which relates to removing one edge from a connected graph — a separate concept."

- question: "Graph G has vertex connectivity κ(G) = 2 and edge connectivity κ'(G) = 3. What does this tell you about G?"
  type: multiple-choice
  options:
    - "The values are impossible — vertex connectivity always equals edge connectivity in any graph"
    - "You need to remove at least 3 edges but only 2 vertices to disconnect G — vertex removal is strictly more powerful because removing a vertex also removes all its incident edges"
    - "G has exactly 3 edges and 2 vertices forming its minimum cut"
    - "The minimum degree of G is 2, so removing any 3-edge cut automatically removes 2 vertices"
  answer: 1
  explanation: "The inequality κ(G) ≤ κ'(G) ≤ δ(G) holds for all graphs: vertex connectivity is at most edge connectivity, which is at most minimum degree. Removing a vertex deletes all its incident edges simultaneously, making vertex removal at least as powerful as edge removal for disconnecting a graph. Here κ(G) = 2 < κ'(G) = 3 means there exists a set of 2 vertices whose removal disconnects G, but no set of 2 edges can disconnect it — you need 3 edges. These values are entirely consistent with the inequality and show the graph is more vulnerable to targeted vertex removal than to edge removal."

- question: "A connected graph has exactly one connected component."
  type: true-false
  answer: true
  explanation: "True. A graph is connected if and only if there exists a path between every pair of vertices — which is exactly the condition for all vertices to belong to a single connected component. Connected components partition the vertex set into maximal connected subsets, and a connected graph means this partition has exactly one part: the entire graph. Conversely, a disconnected graph has two or more components, meaning at least one pair of vertices has no connecting path."

- question: "In a connected graph, there can be at most one path between any pair of vertices."
  type: true-false
  answer: false
  explanation: "False. 'Connected' only requires that at least one path exists between every pair of vertices — it says nothing about uniqueness. Even a simple cycle (triangle) provides two distinct paths between every pair of vertices (clockwise and counterclockwise). Trees are the special case where exactly one simple path exists between every pair of vertices — but that is because trees are connected *and* acyclic. In general, connected graphs can have many paths between any pair, and higher connectivity (more redundant paths) corresponds to greater robustness."

- question: "Explain the concept of a 'bridge' in a graph and why network designers try to eliminate bridges from critical infrastructure."
  type: short-answer
  answer: "A bridge is an edge whose removal disconnects the graph — it is the sole connection between two parts of the network. Equivalently, a graph has a bridge if and only if its edge connectivity κ'(G) = 1. In critical infrastructure (internet routing, power grids, transportation networks), a bridge is a single point of failure: if that one cable, road, or link fails, the network splits into isolated components with no alternative route. Network designers eliminate bridges by adding redundant connections, ensuring κ'(G) ≥ 2 so that no single edge failure can disconnect the network."
  explanation: "The practical significance of connectivity measures is greatest in infrastructure design. A network with κ'(G) = 1 is extremely fragile — one cable cut can sever communication between entire regions. Internet backbone networks are designed for high edge and vertex connectivity so traffic can re-route around both accidental failures and targeted attacks. The inequality κ(G) ≤ κ'(G) ≤ δ(G) also warns designers that any node with only one or two connections limits the entire network's connectivity, no matter how well the rest of the graph is connected."
```

## Explainer

You already know that a graph is a collection of **vertices** (nodes) and **edges** (connections between them). Connectivity is about asking a deceptively simple question: can you get from any vertex to any other vertex by traveling along edges? If yes, the graph is **connected**. If some pairs of vertices have no path between them — think of islands with no bridges — the graph is **disconnected**.

The useful structure inside a disconnected graph is its **connected components**: the maximal chunks that are internally connected. "Maximal" means you've included every vertex you can reach — you can't expand the component any further without leaving the connected region. Think of a social network where some people know each other and others are completely unaware of each other's existence. Each isolated social circle is a connected component. Every vertex belongs to exactly one component, and the components partition the graph.

Once you understand what connectivity means, the natural follow-up is: how *robust* is it? Two key measures capture this. **Edge connectivity** κ'(G) is the minimum number of edges you'd need to remove to disconnect the graph (or isolate a vertex). **Vertex connectivity** κ(G) is the minimum number of vertices whose removal disconnects the graph. Intuitively, a graph where you can sever it by removing just one edge (called a **bridge**) is fragile; a graph where you'd need to remove many edges is robust. These measures matter in network design — an internet router network needs high connectivity so that no single cable failure splits the network.

There's a useful inequality relating these measures: κ(G) ≤ κ'(G) ≤ δ(G), where δ(G) is the minimum vertex degree. This says vertex connectivity is the hardest to achieve: removing vertices is strictly more powerful than removing edges (because removing a vertex also removes all its incident edges). A graph achieving κ(G) = δ(G), like the complete graph Kₙ, is as connected as theoretically possible given its minimum degree. These ideas feed directly into the study of Euler paths, which require specific connectivity conditions to exist.
