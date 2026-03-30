---
id: approximation-algorithms-advanced
title: Approximation Algorithms (LP Relaxation and Primal-Dual)
domain: computer-science
course: advanced-algorithms
prerequisites:
- id: np-completeness
  type: hard
- id: linear-programming-algorithms
  type: hard
- id: greedy-algorithms
  type: hard
- id: hardness-of-approximation
  type: soft
tags:
- approximation-algorithms
- lp-relaxation
- primal-dual
- integrality-gap
stage: expert
status: validated
---

# Approximation Algorithms (LP Relaxation and Primal-Dual)

## Core Idea
Approximation algorithms provide provably near-optimal solutions to NP-hard optimization problems in polynomial time. LP relaxation replaces integer constraints with continuous ones, solves the resulting linear program, and then rounds the fractional solution to an integer solution — the integrality gap bounds the worst-case approximation ratio. The primal-dual method constructs feasible primal and dual solutions simultaneously, using complementary slackness conditions to guide the algorithm and weak duality to prove the approximation guarantee. For vertex cover, LP relaxation yields a 2-approximation (round all variables >= 1/2); for set cover, randomized rounding of the LP relaxation gives an O(log n)-approximation matching the hardness of approximation lower bound. These techniques transform optimization problems into algebraic ones where duality theory provides the performance guarantee.

## Questions

```yaml
- question: "The LP relaxation of the minimum vertex cover problem has an integrality gap of exactly 2. What does this mean, and why does it immediately yield a 2-approximation algorithm?"
  type: multiple-choice
  options:
    - "The LP relaxation always returns a solution with cost exactly twice the integer optimum"
    - "The ratio between the optimal integer solution and the optimal fractional solution is at most 2 for all instances, and rounding all fractional variables >= 1/2 to 1 (and others to 0) produces a valid vertex cover with cost at most 2 times the LP optimum, which is at most 2 times the integer optimum"
    - "The LP relaxation runs in time O(n^2) instead of O(n)"
    - "Every vertex cover can be converted to a fractional solution by dividing all values by 2"
  answer: 1
  explanation: "For any edge (u,v), the LP constraint x_u + x_v >= 1 means at least one of x_u, x_v is >= 1/2. Rounding all variables >= 1/2 to 1 covers every edge (at least one endpoint rounds to 1). The cost of the rounded solution is at most 2 * LP_OPT because each variable at most doubles. Since LP_OPT <= OPT_integer (relaxation only makes the feasible region larger), the rounded solution costs at most 2 * OPT. The integrality gap is exactly 2 because some instances (e.g., odd cycles) have LP_OPT = n/2 but OPT = ceil(n/2), with ratio approaching 2."

- question: "In the primal-dual method for approximation algorithms, the dual solution provides a LOWER BOUND on the optimal value, while the primal solution provides the actual (feasible) solution with an UPPER BOUND."
  type: true-false
  answer: true
  explanation: "This is the heart of the primal-dual approach. For a minimization problem, weak duality says: any feasible dual solution value <= optimal primal value. So the dual gives a lower bound on OPT. The algorithm constructs a feasible primal (integer) solution and a feasible dual solution such that primal_cost <= alpha * dual_value for some factor alpha. Then primal_cost <= alpha * dual_value <= alpha * OPT, proving an alpha-approximation. The algorithm never needs to solve the LP — it just needs to produce feasible primal and dual solutions with a bounded ratio."

- question: "Explain why randomized rounding of an LP relaxation for set cover achieves O(log n)-approximation, and why this is essentially optimal."
  type: short-answer
  answer: "Solve the LP relaxation, which assigns fractional values x_S to each set S. Include each set independently with probability x_S. An element covered by sets of total fractional value v is uncovered with probability at most product(1 - x_S) <= e^(-v) <= e^(-1) (since LP feasibility requires sum >= 1 for each element). Repeating O(log n) times (or scaling probabilities by c*log n) ensures every element is covered with high probability, at expected cost O(log n) * LP_OPT. Since LP_OPT <= OPT, this gives O(log n)-approximation. This is essentially optimal: the hardness result of Dinur and Steurer (2014) shows set cover cannot be approximated better than (1-epsilon) * ln n unless P = NP. The LP relaxation's integrality gap is also Theta(log n), so LP-based methods cannot do better."
  explanation: "The argument uses the inequality 1-x <= e^(-x) and the fact that LP feasibility constrains the total fractional coverage of each element to be at least 1. Randomized rounding converts fractional coverage into probabilistic coverage, and log n repetitions handle the union bound over n elements."

- question: "The primal-dual method requires explicitly solving a linear program before constructing the approximation."
  type: true-false
  answer: false
  explanation: "A major advantage of the primal-dual method is that it does NOT require solving the LP. Instead, it directly constructs feasible primal and dual solutions through a combinatorial algorithm — typically growing the dual solution until some constraint becomes tight, then adding the corresponding primal element. The LP and its dual are used only in the ANALYSIS to prove the approximation ratio. This makes primal-dual algorithms combinatorial, often simpler, and sometimes faster than LP-based rounding approaches. Classic examples include the primal-dual 2-approximation for the feedback vertex set problem and Jain's iterative rounding for Steiner network."
```

## Explainer

NP-hardness tells you that finding optimal solutions is (almost certainly) intractable. Approximation algorithms respond by asking: how close to optimal can we get in polynomial time? The answer depends on the problem, and the most powerful tools for both designing approximation algorithms and proving their guarantees come from linear programming duality.

LP relaxation is the most natural approach. Formulate the optimization problem as an integer linear program (ILP), drop the integrality constraints to get a linear program (LP), solve it, and round the fractional solution to an integer one. The LP optimum is a lower bound on the ILP optimum (for minimization), so if rounding increases the cost by at most a factor alpha, you have an alpha-approximation. For vertex cover, the rounding is simple: every vertex with LP value >= 1/2 enters the cover. Every edge is covered (its LP constraint forces at least one endpoint to >= 1/2), and the cost at most doubles. The factor of 2 is tight for this rounding scheme because the LP's integrality gap is exactly 2.

The primal-dual method is more sophisticated and often yields combinatorial algorithms. Instead of solving the LP, you simultaneously construct a feasible primal solution (the approximate answer) and a feasible dual solution (the lower bound certificate). The algorithm typically grows dual variables until some dual constraint becomes tight, then adds the corresponding primal element. Weak duality guarantees that the dual objective is a lower bound on the optimum, so if the primal cost is at most alpha times the dual objective, you have an alpha-approximation. The beauty is that the LP is never solved — it appears only in the proof. This yields fast, combinatorial algorithms with provable guarantees.

The deepest results in approximation algorithms connect the integrality gap of an LP (or SDP) relaxation to the hardness of approximation. The Unique Games Conjecture, if true, implies that for many problems the integrality gap of the natural SDP relaxation exactly characterizes the best achievable approximation ratio. For set cover, the Theta(log n) approximation ratio matches both the LP integrality gap and the hardness lower bound — the LP relaxation captures the problem's approximability perfectly. Understanding these connections between relaxation strength, rounding techniques, and computational hardness is the central project of modern approximation algorithm theory.
