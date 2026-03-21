---
id: euler-circuits-and-paths
title: Eulerian Circuits and Paths
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-connectivity
  type: hard
- id: graph-theory-intro
  type: hard
builds-toward:
- hamiltonian-circuits
tags:
- euler-circuit
- euler-path
- eulerian-graph
- konigsberg-bridges
stage: formal-systems
status: validated
---

# Eulerian Circuits and Paths

## Core Idea
An Eulerian circuit is a closed walk traversing every edge exactly once; an Eulerian path is an open walk doing the same. Euler's theorem (1736) states: a connected graph has an Eulerian circuit if and only if every vertex has even degree, and an Eulerian path (but not circuit) if and only if exactly two vertices have odd degree. The Königsberg bridge problem — can one cross all seven bridges without repeating any? — was Euler's original motivation and arguably the founding problem of graph theory.

## How It's Best Learned
Attempt Eulerian circuits on small graphs by hand before seeing the theorem. Verify Euler's condition on several examples. Connect to practical route-planning problems (mail delivery, snow plowing) where the goal is to traverse all edges with minimum repetition.

## Common Misconceptions
- Confusing Eulerian circuits (edges traversed once) with Hamiltonian circuits (vertices visited once) — these are fundamentally different problems with very different theories.
- Thinking even degree is sufficient without the connectivity requirement.

## Questions

```yaml
- question: "A connected graph has five vertices with degrees 2, 4, 3, 3, 4. Which of the following is correct?"
  type: multiple-choice
  options:
    - "It has both an Eulerian circuit and an Eulerian path"
    - "It has an Eulerian path but not an Eulerian circuit, starting and ending at the two odd-degree vertices"
    - "It has neither an Eulerian circuit nor an Eulerian path"
    - "It has an Eulerian circuit because the majority of vertices have even degree"
  answer: 1
  explanation: "Two vertices have odd degree (the two vertices of degree 3); the others have even degree. Euler's theorem says: an Eulerian circuit requires ALL vertices to have even degree — that fails here. An Eulerian path requires EXACTLY TWO odd-degree vertices — that holds here. So the graph has an Eulerian path (starting at one degree-3 vertex and ending at the other) but no Eulerian circuit. Option D is a common misconception: the condition must hold for every vertex, not a majority."

- question: "Why does an Eulerian circuit require every vertex to have even degree?"
  type: multiple-choice
  options:
    - "Even-degree vertices are computationally easier to traverse in graph algorithms"
    - "Every time a circuit passes through a vertex (neither starting nor ending there), it uses one edge to arrive and one to depart — consuming exactly two edges, requiring the degree to be even"
    - "Odd-degree vertices cannot be connected to even-degree vertices in a valid graph"
    - "The Hamiltonian path condition requires all degrees to be even"
  answer: 1
  explanation: "This is the local argument that makes Euler's theorem work. For a closed walk (circuit) traversing every edge exactly once, each interior passage through a vertex uses exactly two edges (one in, one out). The starting/ending vertex also needs a balanced count because the walk must return. If any vertex has odd degree, it cannot be perfectly balanced — the walk must either start or end there, preventing a closed circuit. This is why the condition is both necessary and sufficient."

- question: "A graph that has an Eulerian circuit necessarily also has a Hamiltonian circuit."
  type: true-false
  answer: false
  explanation: "Eulerian and Hamiltonian circuits are fundamentally different problems. An Eulerian circuit traverses every EDGE exactly once; a Hamiltonian circuit visits every VERTEX exactly once. A graph can have one without the other. More importantly, Eulerian circuit existence is solvable in linear time (just check the degree condition and connectivity), while Hamiltonian circuit existence is NP-complete. The surface similarity between the two problems is misleading — they have completely different theories."

- question: "In a connected graph with exactly two odd-degree vertices, those two vertices must be the start and end points of any Eulerian path through the graph."
  type: true-false
  answer: true
  explanation: "Euler's theorem for paths: a connected graph has an Eulerian path if and only if it has exactly two odd-degree vertices. The reason these must be the endpoints is the same local argument used for circuits: every intermediate vertex is entered and exited an equal number of times (requiring even degree). Only the starting vertex (one extra exit at the beginning) and the ending vertex (one extra entry at the end) can have odd degree. So the two odd-degree vertices are necessarily the endpoints of any Eulerian path."

- question: "The Königsberg bridge problem asks whether you can cross all seven bridges exactly once. Explain why this is impossible, using the concept of vertex degree."
  type: short-answer
  answer: "Euler modeled the problem as a graph where the four landmasses are vertices and the seven bridges are edges. He found that all four vertices have odd degree (3 or 5 bridges each). For an Eulerian path to exist, at most two vertices can have odd degree; for a circuit, none can. With four odd-degree vertices, neither an Eulerian path nor a circuit is possible — so no such walk across all bridges exists."
  explanation: "This is the founding application of graph theory: translating a physical puzzle into a graph and then applying a structural condition. Euler's key insight was that the impossibility was not a matter of insufficient cleverness but a provable mathematical fact about the graph's degree sequence. The generalization — any graph with more than two odd-degree vertices has no Eulerian path — follows directly from the local balance argument."
```

## Explainer

Euler's theorem is one of the most elegant results in graph theory: a complete solution to a natural traversal problem, given by a single, easy-to-check condition. You've studied graph connectivity and the basic vocabulary of graphs. Now the question is: can you plan a walk that uses every edge exactly once? Think of the graph as a map where edges are streets and vertices are intersections — you want a route that covers every street exactly once, ideally returning to where you started.

The key insight comes from thinking locally about each vertex. Every time a walk passes through a vertex (entering, then leaving), it consumes two edges — one in, one out. For a **circuit** (a closed walk that returns to its starting vertex) to traverse every edge exactly once, every vertex must balance its arrivals and departures perfectly. This forces every vertex to have **even degree** — an equal number of edges on each side of any passage. If any vertex has odd degree, it cannot be perfectly balanced, meaning the walk must either start or end there, making a closed circuit impossible.

Euler's theorem converts this local observation into a complete characterization. For a connected graph: it has an **Eulerian circuit** if and only if every vertex has even degree; it has an **Eulerian path** (open walk through every edge once) if and only if exactly two vertices have odd degree — those two are the start and end of the path. Connectivity is also required: you cannot traverse edges in a component you can never reach. The Königsberg bridge problem, which motivated Euler's 1736 paper, had four land masses each with an odd number of bridge connections — so no Eulerian path was possible, proving the famous walk impossible.

One distinction is critical to keep sharp: **Eulerian** circuits cover every **edge** once, while **Hamiltonian** circuits visit every **vertex** once. These problems sound related but are fundamentally different in difficulty. Eulerian circuit existence is solvable in linear time — just check that all degrees are even and the graph is connected. Hamiltonian circuit existence is NP-complete, with no known efficient algorithm. The degree condition works for Euler because edges are "used up" as you traverse them, allowing a clean local argument to close the analysis. No comparable local condition exists for Hamilton, which is why the two problems, despite their surface similarity, have completely different theories.
