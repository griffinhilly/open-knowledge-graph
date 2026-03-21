---
id: astar-search-algorithm
title: A* Search Algorithm
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: breadth-first-search
  type: hard
- id: dijkstras-algorithm
  type: hard
tags:
- search
- graphs
- pathfinding
- heuristics
stage: advanced
status: draft
---

# A* Search Algorithm

## Core Idea
A* combines actual path cost with heuristic estimates of remaining cost to find optimal paths efficiently. It uses f(n) = g(n) + h(n), where g(n) is the cost to reach node n and h(n) estimates cost to goal. A* is complete and optimal when h(n) is admissible.

## Questions

```yaml
- question: "An A* implementation uses a heuristic that occasionally overestimates the true remaining cost to the goal. What is the consequence?"
  type: multiple-choice
  options:
    - "A* will still find the optimal path, but will explore more nodes than necessary"
    - "A* may return a suboptimal path, because the inadmissible heuristic can cause it to prematurely expand a non-optimal node"
    - "A* will fail to find any path, because an overestimating heuristic causes the priority queue to malfunction"
    - "A* will find the optimal path faster, because overestimation pushes it more aggressively toward the goal"
  answer: 1
  explanation: "Admissibility — never overestimating the true remaining cost — is the property that guarantees A* finds the optimal path. When h(n) overestimates, A* may expand a node on the optimal path before it has found the cheapest route to that node, causing it to commit to a suboptimal solution. Option D describes the appeal of inadmissible heuristics (they're faster), but the tradeoff is lost optimality. Option A is incorrect: an inadmissible heuristic doesn't just slow A* down, it can derail it entirely."

- question: "You set h(n) = 0 for every node and run A*. What does A* become in this case?"
  type: multiple-choice
  options:
    - "Breadth-first search, expanding nodes in order of depth from the start"
    - "Greedy best-first search, expanding the node closest to the goal"
    - "Dijkstra's algorithm, expanding the node with the lowest accumulated path cost g(n)"
    - "An exhaustive depth-first search with backtracking"
  answer: 2
  explanation: "With h(n) = 0 everywhere, the evaluation function reduces to f(n) = g(n) + 0 = g(n). A* then always expands the node with the smallest accumulated cost from the start — exactly what Dijkstra's algorithm does. The heuristic contributes nothing and the search expands uniformly in all directions, unguided by any estimate of where the goal lies. Setting g(n) = 0 instead would give greedy best-first search (option B), which chases the heuristic without accounting for cost already spent."

- question: "A heuristic that is consistent (monotone) is also guaranteed to be admissible."
  type: true-false
  answer: true
  explanation: "Consistency requires that h(n) ≤ cost(n, n') + h(n') for every edge from n to n'. This means h can never 'jump up' along any path in a way that would require overestimating the true cost to the goal. By induction from any goal node (where h = 0), a consistent heuristic can be shown to satisfy h(n) ≤ true cost to goal for all n — the definition of admissibility. Consistency is the stronger condition; every consistent heuristic is admissible, but not every admissible heuristic is consistent."

- question: "A* with a perfect heuristic (h(n) equals the true remaining cost exactly) may still need to explore many nodes it doesn't ultimately include in the final path."
  type: true-false
  answer: false
  explanation: "With a perfect heuristic, f(n) = g(n) + h*(n) = true total path cost through n. Every node on the optimal path has the same f value (the optimal path length), and every node NOT on the optimal path has a strictly higher f value. A* with a perfect heuristic expands only the nodes along the optimal path — zero wasted exploration. This is why heuristic quality matters so much: the closer h is to the true remaining cost (without exceeding it), the fewer nodes A* explores."

- question: "What does it mean for a heuristic to be admissible, and why is admissibility the critical property that makes A* optimal rather than merely fast?"
  type: short-answer
  answer: "An admissible heuristic never overestimates the true cost to reach the goal from any node: h(n) ≤ h*(n) for all n, where h*(n) is the true optimal remaining cost. Admissibility is critical because A* expands nodes in order of f(n) = g(n) + h(n). If h overestimates, a node on the true optimal path may appear to have a higher f value than a node on a suboptimal path, causing A* to commit to the cheaper-looking (but actually worse) route. Admissibility ensures this never happens: the true optimal path can never be made to look worse than a suboptimal alternative."
  explanation: "The intuition is a guarantee: if h never lies about the future cost, A* will never give up on a promising path too soon. Without admissibility, the heuristic can misdirect the search in ways that are impossible to detect without already knowing the optimal solution — defeating the purpose of using a heuristic at all."
```

## Explainer

You already know two graph search algorithms that A* builds on directly. **Breadth-first search** (BFS) explores nodes in order of their depth from the start — it finds the shortest path in terms of number of edges, but it ignores edge weights entirely. **Dijkstra's algorithm** fixes this by always expanding the node with the lowest accumulated cost g(n) — it finds the truly cheapest path, but it explores outward uniformly in all directions, wasting effort on paths heading away from the goal. A* combines the best of both worlds by adding a **heuristic function** h(n) that estimates how far node n is from the goal, directing the search toward promising areas of the graph.

The evaluation function **f(n) = g(n) + h(n)** is what makes A* work. Here g(n) is the actual cost of the cheapest known path from the start to node n (just like Dijkstra's), and h(n) is your best guess of the remaining cost from n to the goal. A* maintains a priority queue ordered by f(n) and always expands the node with the smallest f value. Think of it as answering the question: "Which unexplored node is on the most promising total path?" If h(n) = 0 for all nodes, A* degenerates into Dijkstra's algorithm. If g(n) = 0, it becomes a pure greedy best-first search that chases the heuristic without accounting for cost already spent.

The key property that guarantees A* finds the optimal path is **admissibility**: the heuristic must never overestimate the true cost to the goal. For pathfinding on a map, the straight-line (Euclidean) distance is admissible because you can never get somewhere faster than a straight line. Manhattan distance is admissible on a grid where you can only move in four directions. When h(n) is admissible, A* will never prematurely commit to a suboptimal path — it may explore a node with a slightly higher g(n) if the heuristic suggests the total path through it could still be cheaper. A stronger property, **consistency** (or monotonicity), requires that h(n) ≤ cost(n, n') + h(n') for every edge. Consistent heuristics guarantee that once A* expands a node, it has already found the optimal path to that node, eliminating the need to re-open closed nodes.

The practical performance of A* depends almost entirely on the quality of the heuristic. A tighter (closer to true cost) but still admissible heuristic prunes more of the search space, making A* dramatically faster. In the best case, a perfect heuristic leads A* straight to the goal along the optimal path with no wasted exploration. In the worst case (h = 0 everywhere), it examines every node Dijkstra's would. This is why designing good heuristics is the central challenge when applying A* — the algorithm itself is simple, but its effectiveness is only as good as the heuristic guiding it. A* is used extensively in game AI for pathfinding, in robotics for motion planning, and in any domain where you need optimal paths through weighted graphs and have domain knowledge to estimate remaining costs.
