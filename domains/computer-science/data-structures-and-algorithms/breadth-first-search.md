---
id: breadth-first-search
title: Breadth-First Search (BFS)
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: queues-data-structure
  type: hard
- id: graph-adjacency-list-matrix-representations
  type: hard
- id: tree-traversals
  type: soft
- id: queue-adt-circular-implementation
  type: hard
builds-toward:
- dijkstras-algorithm
- topological-sort
tags:
- BFS
- graph-traversal
- shortest-path
- level-order
stage: formal-systems
status: validated
---
# Breadth-First Search (BFS)

## Core Idea
Breadth-first search (BFS) explores a graph layer by layer, visiting all neighbors of a node before moving deeper. It uses a queue and a visited set, running in O(V + E) time for V vertices and E edges. BFS finds the shortest path in terms of edge count between two nodes in an unweighted graph. It also determines connected components, checks bipartiteness, and forms the basis for Dijkstra's algorithm when extended to weighted graphs.

## How It's Best Learned
Implement BFS on both adjacency list and adjacency matrix representations. Trace through a small graph by hand showing the queue state at each step. Then add path reconstruction using a parent-pointer array.

## Common Misconceptions
- BFS finds shortest paths only in unweighted graphs; for weighted graphs, Dijkstra's algorithm is needed.
- The visited set must be marked before enqueuing a node, not after dequeuing, to prevent the same node from being added to the queue multiple times.

## Questions

```yaml
- question: "Which data structure is central to BFS and explains why it explores a graph layer by layer?"
  type: multiple-choice
  options: ["Stack", "Queue", "Priority queue", "Hash map"]
  answer: 1
  explanation: "A queue's FIFO (first-in, first-out) ordering ensures that all nodes at distance d are fully processed before any node at distance d+1 is dequeued. A stack would produce DFS behavior instead, going deep before going wide."

- question: "BFS finds the shortest weighted path between two nodes in any graph."
  type: true-false
  answer: false
  explanation: "BFS finds the shortest path measured in number of edges (hops), which is only meaningful as a distance when all edges have equal weight. For weighted graphs where edges have different costs, Dijkstra's algorithm is required."

- question: "Why must a node be marked as visited before it is enqueued, rather than after it is dequeued?"
  type: short-answer
  answer: "If marking is deferred until dequeue, multiple neighbors can enqueue the same unvisited node before any of them is processed, causing the node to be visited multiple times. Marking before enqueue ensures each node enters the queue at most once."
  explanation: "This is one of the most common BFS implementation bugs. The visited check and the enqueue operation must be atomic from the graph's perspective: the moment you decide to enqueue a node, mark it so no other neighbor can also enqueue it."
```

## Explainer

BFS is built directly on top of the queue data structure you already know. The queue's FIFO property is not incidental — it is precisely what produces the layer-by-layer exploration. When you enqueue all unvisited neighbors of the current node, those neighbors sit behind any nodes already in the queue from the previous layer. By the time you process them, you will have finished their entire layer first. This is why BFS is sometimes called "level-order traversal" on trees.

The algorithm has three moving parts: a **queue** that drives the traversal order, a **visited set** that prevents cycles from looping forever, and a **parent pointer array** (optional but useful) that lets you reconstruct the path after the search finishes. Start by enqueuing the source node and marking it visited. Then repeatedly dequeue a node, check if it is the target, and enqueue all its unvisited neighbors (marking each visited immediately on enqueue). Stop when the queue is empty or the target is found.

BFS guarantees the **shortest path by edge count** in unweighted graphs. The argument is simple: the source is at distance 0, its neighbors are at distance 1, their unvisited neighbors are at distance 2, and so on. Because each node is processed in non-decreasing distance order, the first time BFS reaches a target node it has taken the minimum number of edges to get there. This guarantee disappears in weighted graphs because a longer path (more edges) might have lower total cost — that is where Dijkstra's algorithm takes over.

The time complexity is O(V + E): every vertex is enqueued and dequeued at most once (O(V)), and every edge is examined at most twice, once from each endpoint (O(E)). The space complexity is also O(V) for the queue and visited set. This makes BFS practical even for large graphs, as long as they fit in memory.

A subtle but important implementation detail: mark nodes visited *before* enqueuing, not after dequeuing. If you wait until dequeue, two different neighbors of the same node can both see it as unvisited and both enqueue it, leading to redundant (or incorrect) processing. The rule is: the moment you decide to enqueue a node is the moment it is "claimed" and should be marked.

