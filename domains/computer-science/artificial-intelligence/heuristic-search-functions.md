---
id: heuristic-search-functions
title: Heuristic Search Functions
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: astar-search-algorithm
  type: hard
- id: greedy-algorithms
  type: soft
builds-toward:
- local-search-optimization
- constraint-propagation
tags:
- search
- heuristics
- admissibility
- optimization
stage: advanced
status: validated
---

# Heuristic Search Functions

## Core Idea
Heuristic functions estimate the cost from a state to the goal without exploring the full search space, enabling guided search. Well-designed heuristics must be admissible (never overestimate) to guarantee optimal solutions, and consistent heuristics satisfy the triangle inequality to enable efficient pruning. The quality of the heuristic determines whether A* will terminate quickly or explore exponentially many states.

## How It's Best Learned
Study examples of admissible heuristics like Manhattan distance for grid puzzles and implement A* with different heuristics to observe how heuristic quality affects search performance.

## Common Misconceptions
A faster heuristic is always better (domination matters: h1 dominates h2 if h1(s) ≥ h2(s) for all s). Optimality requires admissibility, not just consistency.

## Questions

```yaml
- question: "You implement A* for the 8-puzzle using h(n) = 2 × Manhattan distance (doubling all heuristic estimates). Compared to standard Manhattan distance, what changes?"
  type: multiple-choice
  options:
    - "A* runs faster and still finds the optimal solution, because the stronger heuristic guides it more aggressively"
    - "A* finds the optimal solution but explores more nodes, since the inflated estimates push it toward greedy behavior"
    - "A* may no longer find the optimal solution, because doubling Manhattan distance can overestimate the true cost"
    - "A* behaves identically, since both heuristics produce the same relative ordering among states"
  answer: 2
  explanation: "Admissibility requires that h(n) never overestimate the true cost. Standard Manhattan distance satisfies this: each tile needs at least as many moves as its Manhattan distance. But 2 × Manhattan distance can exceed the true remaining cost (a tile 2 moves away can't take fewer than 2 moves, but 2 × 2 = 4 exceeds 2). With an inadmissible heuristic, A* may dismiss the optimal path by making it look more expensive than it is, and find a suboptimal solution instead. This is why the admissibility condition is precise: even a small overestimate breaks the guarantee."

- question: "For the 8-puzzle, Manhattan distance (h₂) dominates misplaced tiles (h₁), meaning h₂(n) ≥ h₁(n) for every state n. What practical consequence does this domination have for A*?"
  type: multiple-choice
  options:
    - "A* with h₂ always expands fewer nodes than A* with h₁, because the tighter lower bound prunes more of the search space"
    - "A* with h₂ is slower per node because computing Manhattan distance takes more time than counting misplaced tiles"
    - "A* with h₁ terminates faster on average because it expands nodes more freely without tight bounds"
    - "Both heuristics lead A* to expand exactly the same set of nodes, just in a different order"
  answer: 0
  explanation: "A dominating heuristic provides tighter guidance: if h₂(n) ≥ h₁(n) for all n, then A* with h₂ will not expand any node that A* with h₁ does not also expand — and it may expand strictly fewer. Intuitively, h₂ is closer to the true remaining cost, so A* can reject unpromising paths earlier. Any node A* with h₂ skips as unpromising is also skipped by h₂-A*, but not necessarily vice versa. This is why seeking the most informative admissible heuristic always pays off in reduced node expansions."

- question: "A consistent (monotone) heuristic is always admissible, but an admissible heuristic is not necessarily consistent."
  type: true-false
  answer: true
  explanation: "Consistency (h(n) ≤ cost(n,n') + h(n') for all edges) implies admissibility because the triangle inequality prevents any node from having an inflated estimate — you can prove by induction that a consistent heuristic never overestimates. The reverse does not hold: you can construct admissible heuristics that violate the triangle inequality for specific edges. However, such counterexamples are rare in practice, and most well-designed admissible heuristics (like Manhattan distance) are also consistent."

- question: "Setting h(n) = 0 for most states is inadmissible because it seldom provides any useful estimate, making it very difficult for A* to find the optimal solution."
  type: true-false
  answer: false
  explanation: "h(n) = 0 is perfectly admissible — it never overestimates (it never estimates anything at all). Admissibility only requires h(n) ≤ true cost; zero satisfies this for any nonneg cost. With h = 0, A* degenerates to Dijkstra's algorithm and still finds the optimal solution. It's a terrible heuristic in the sense of efficiency (it provides no guidance), but it is valid and correct. Confusing 'informative' with 'admissible' is a common error."

- question: "What is the relaxation technique for designing heuristics, and why does it always produce an admissible heuristic?"
  type: short-answer
  answer: "Relaxation removes one or more constraints from the original problem to create an easier version, then uses the exact optimal cost of that easier version as h(n). Because the relaxed problem has fewer restrictions, any solution to the original problem is automatically a solution to the relaxed problem. Therefore the optimal cost of the relaxed problem is at most the optimal cost of the real problem — the heuristic never overestimates, guaranteeing admissibility."
  explanation: "Manhattan distance for the 8-puzzle is the canonical example: it solves the relaxed problem where tiles can slide through each other. In the real problem, tiles block each other, so the true cost is at least as large as Manhattan distance. The power of relaxation is that it gives a systematic recipe: take your problem, identify constraints, remove some of them, and solve exactly. Any solution to the original satisfies all constraints including the ones you removed, so it's also valid in the relaxed problem. The relaxed optimal cost therefore lower-bounds the real optimal cost."
```

## Explainer

From your study of A* search, you know that A* evaluates nodes using f(n) = g(n) + h(n), where g(n) is the cost so far and h(n) is the heuristic estimate of the remaining cost to the goal. The entire performance of A* — whether it finds the optimal solution quickly or degenerates into exhaustive search — hinges on the quality of h(n). A heuristic function is your way of injecting problem-specific knowledge into a general search algorithm, telling it which directions look promising without actually exploring them.

The most important property of a heuristic is **admissibility**: h(n) must never overestimate the true cost to reach the goal. If h always underestimates (or exactly equals) the true remaining cost, A* is guaranteed to find the optimal solution. Intuitively, an admissible heuristic is optimistic — it never makes a path look worse than it actually is, so A* will never dismiss the optimal path prematurely. The trivial heuristic h(n) = 0 is always admissible (it is maximally optimistic), but it gives A* no guidance, reducing it to Dijkstra's algorithm. The ideal heuristic would equal the true cost exactly — then A* would march straight to the goal without exploring a single unnecessary node. Real heuristics fall between these extremes.

Consider the 8-puzzle (sliding tiles). Two classic heuristics are **misplaced tiles** (count how many tiles are not in their goal position) and **Manhattan distance** (sum the number of horizontal and vertical moves each tile needs to reach its goal position). Both are admissible because neither can overestimate — a tile that is out of place needs at least one move, and the Manhattan distance of each tile is a lower bound on its actual moves because it ignores the constraint that other tiles block the way. Manhattan distance **dominates** misplaced tiles: for every state, Manhattan distance is greater than or equal to misplaced tiles. This domination is precisely what makes it the better heuristic. A dominating heuristic is closer to the true cost, so A* expands fewer nodes — it has tighter guidance about which paths to pursue.

A stronger property than admissibility is **consistency** (also called monotonicity): for every node n and successor n', the heuristic satisfies h(n) ≤ cost(n, n') + h(n'). This is the triangle inequality — the estimated cost from n to the goal should not exceed the cost of stepping to n' plus the estimate from n'. Consistent heuristics guarantee that when A* expands a node, it has already found the optimal path to that node, so nodes never need to be re-expanded. Every consistent heuristic is admissible, but not every admissible heuristic is consistent (though counterexamples are rare in practice). When designing heuristics, a powerful technique is **relaxation**: remove some constraints from the original problem, solve the easier version, and use its cost as h(n). Manhattan distance, for instance, is the exact solution to a relaxed 8-puzzle where tiles can pass through each other. This relaxation approach systematically generates admissible heuristics for any problem where you can formalize the constraints.
