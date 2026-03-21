---
id: dijkstra-algorithm
title: Dijkstra's Shortest Path Algorithm
domain: mathematics
course: discrete-math
prerequisites:
- id: shortest-paths-unweighted-graphs
  type: hard
- id: big-o-notation
  type: soft
tags:
- shortest-paths
- algorithms
- weighted-graphs
stage: formal-systems
status: draft
---

# Dijkstra's Shortest Path Algorithm

## Core Idea
Dijkstra's algorithm finds the shortest path in a weighted graph with non-negative edge weights using a greedy approach: always extend the shortest known path. Using a priority queue, it runs in O((V+E) log V) time and is widely applied in GPS navigation and routing.

## Questions

```yaml
- question: "You run Dijkstra's algorithm on a graph that contains one edge with weight -3. What is the risk?"
  type: multiple-choice
  options:
    - "The algorithm crashes because priority queues cannot store negative keys"
    - "The algorithm runs correctly but is slower than usual"
    - "The algorithm may return incorrect shortest paths because settling a node is no longer guaranteed to be final"
    - "The algorithm works as long as the negative edge is not on the shortest path"
  answer: 2
  explanation: "Dijkstra's correctness rests on the greedy guarantee: once a node is pulled from the priority queue, its recorded distance is final. This holds only because all edge weights are non-negative — no future path can be cheaper than the one already settled. A negative edge breaks this: a later path through a negative-weight edge could undercut an already-finalized distance. The algorithm won't crash, but it may report a non-optimal path. Bellman-Ford handles negative weights correctly."

- question: "Why does Dijkstra's algorithm use a priority queue (min-heap) instead of the regular FIFO queue used in BFS?"
  type: multiple-choice
  options:
    - "A priority queue is required to handle graphs with cycles; a FIFO queue would loop infinitely"
    - "BFS visits all neighbors at once, which doesn't work for weighted graphs; the priority queue ensures we always extend the cheapest known path next"
    - "Priority queues are faster than FIFO queues for all graph traversal tasks"
    - "The FIFO queue cannot store weighted edges, so a priority queue is used as a workaround"
  answer: 1
  explanation: "BFS works for unweighted graphs because every edge costs 1 — the first time you reach a node is the cheapest route. With unequal weights, the first-found path is not guaranteed to be cheapest. The priority queue ensures that among all currently-known paths, we always extend the one with the smallest total cost so far. This is the greedy insight: committing to the cheapest frontier node is always safe when weights are non-negative."

- question: "Dijkstra's algorithm may return incorrect shortest paths if any edge in the graph has a negative weight."
  type: true-false
  answer: true
  explanation: "The correctness proof depends entirely on the invariant that once a node is settled (pulled from the priority queue), its distance is final. With non-negative weights, this holds because adding more edges can only increase total cost. A negative edge breaks the invariant: a path through that edge might later be discovered to be cheaper than what was already settled. The algorithm produces wrong answers in such cases — not a crash, just incorrect output."

- question: "Dijkstra's algorithm visits nodes in the order they were first discovered, just like BFS."
  type: true-false
  answer: false
  explanation: "BFS visits nodes in discovery order (FIFO). Dijkstra visits nodes in order of their current best-known distance from the source. A node discovered early might have a large initial estimate and be visited late; a node discovered later might jump to the front of the priority queue because it has a very low total cost path. This is the fundamental difference: Dijkstra is driven by cost, not by discovery order."

- question: "Explain the greedy guarantee behind Dijkstra's correctness: why is it safe to permanently finalize a node's shortest distance when it is extracted from the priority queue?"
  type: short-answer
  answer: "When a node is pulled from the priority queue, it has the smallest current distance among all unvisited nodes. Any alternative path to that node would have to go through other unvisited nodes first — but those nodes all have equal or greater distance. Since edge weights are non-negative, adding more edges can only increase or maintain the total cost, never decrease it. Therefore, no future path can be cheaper than the one already recorded. The finalization is safe precisely because costs cannot decrease as you extend a path."
  explanation: "This greedy guarantee is what makes Dijkstra efficient and correct simultaneously. It allows us to 'close' each node permanently in one pass rather than revisiting it. The non-negative weight requirement is not an arbitrary restriction — it is exactly the condition that makes the guarantee valid. Negative edges allow future paths to be cheaper than settled ones, which is why Bellman-Ford (which doesn't finalize nodes permanently) is needed for those cases."
```

## Explainer

You already know how to find shortest paths in an unweighted graph using BFS — explore layer by layer, and the first time you reach a node is guaranteed to be the shortest. But BFS only works because every edge has the same "cost" (1). Once edges have different weights, a path with more hops might actually be cheaper than a path with fewer. Dijkstra's algorithm solves this generalization by replacing BFS's queue with a **priority queue** (min-heap), always processing whichever unvisited node currently has the smallest known total distance from the source.

The algorithm maintains a table of "best known distances" to every node, all initialized to infinity except the source node which starts at 0. Each round, you pull out the node with the smallest distance, then examine all its neighbors. For each neighbor, you compute the candidate distance: (distance to current node) + (edge weight to neighbor). If this candidate is better than what's already recorded for that neighbor, you update the table — this is called **relaxing an edge**. Repeat until all nodes are settled. The insight behind correctness is the greedy guarantee: once a node is pulled from the priority queue, its recorded distance is final. This works because all edge weights are non-negative — no future path through other nodes can be shorter, since distances can only increase as you add more edges.

Consider a simple road network where you want to drive from city A to city D. Direct path A→D costs 10. Alternatively, A→B costs 2, B→C costs 3, C→D costs 4 — a total of 9. BFS would find A→D first (one hop) and call it optimal. Dijkstra correctly discovers the three-hop path is cheaper. It does this by settling A first, then B (distance 2), then C (distance 5), then D via C (distance 9), only then seeing that the direct A→D edge gives distance 10, which is worse.

The non-negative weight requirement is not a minor technicality — it's load-bearing. If negative edges existed, settling a node would no longer be final: a later path going through a negative edge could undercut an already-settled distance. For graphs with negative weights, the **Bellman-Ford algorithm** handles this correctly (at higher cost: O(VE)). The O((V+E) log V) complexity of Dijkstra comes from performing up to E edge relaxations, each of which requires a priority queue update costing O(log V). This efficiency makes it practical for real-world networks with millions of nodes, which is why it underlies GPS routing, internet packet forwarding (OSPF), and shortest-path queries in maps.
