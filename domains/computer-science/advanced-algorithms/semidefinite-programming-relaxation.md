---
id: semidefinite-programming-relaxation
title: Semidefinite Programming Relaxation
domain: computer-science
course: advanced-algorithms
prerequisites:
- id: approximation-algorithms-advanced
  type: hard
- id: linear-programming-algorithms
  type: hard
- id: np-completeness
  type: soft
tags:
- sdp
- semidefinite-programming
- max-cut
- goemans-williamson
stage: expert
status: validated
---

# Semidefinite Programming Relaxation

## Core Idea
Semidefinite programming (SDP) extends linear programming by optimizing a linear objective over the cone of positive semidefinite matrices. SDP relaxations produce tighter bounds than LP relaxations for many combinatorial optimization problems. The landmark result is the Goemans-Williamson algorithm for MAX-CUT: relax binary variables to unit vectors, solve the SDP to find an optimal vector configuration, then round using a random hyperplane. This achieves an approximation ratio of ~0.878, which is optimal assuming the Unique Games Conjecture. SDP relaxations also yield the best known approximations for graph coloring, MAX-SAT, and constraint satisfaction problems, and the integrality gaps of SDP hierarchies (Lasserre, Sum-of-Squares) connect to fundamental questions in computational complexity.

## Questions

```yaml
- question: "In the Goemans-Williamson MAX-CUT algorithm, each vertex i is assigned a unit vector v_i in R^n, and the SDP maximizes sum_{(i,j) in E} (1 - v_i · v_j) / 2. The rounding step picks a random hyperplane and cuts based on which side each vector falls. Why does this rounding achieve ratio ~0.878?"
  type: multiple-choice
  options:
    - "The hyperplane always cuts at least 87.8% of edges"
    - "For each edge (i,j), the probability the hyperplane separates v_i and v_j is arccos(v_i · v_j) / pi, and the ratio arccos(x)/(pi * (1-x)/2) is minimized at ~0.878 over x in [-1,1], giving a worst-case ratio of ~0.878 between the rounded solution and the SDP value"
    - "The SDP relaxation has integrality gap exactly 0.878"
    - "The random hyperplane is chosen to maximize the cut, not chosen randomly"
  answer: 1
  explanation: "The key identity: a random hyperplane through the origin separates two unit vectors v_i, v_j with probability arccos(v_i · v_j) / pi. The SDP contribution of edge (i,j) is (1 - v_i · v_j) / 2. The ratio of expected rounding benefit to SDP benefit is arccos(v_i · v_j) / (pi * (1 - v_i · v_j) / 2). This ratio depends on the angle between vectors and is minimized at approximately 0.87856 (when v_i · v_j ≈ -0.689). Since the minimum ratio holds for every edge independently, the overall expected cut is at least 0.878 * SDP_OPT >= 0.878 * OPT."

- question: "SDP relaxations are strictly more powerful than LP relaxations: for any combinatorial optimization problem, the SDP integrality gap is at most the LP integrality gap."
  type: true-false
  answer: true
  explanation: "Every LP can be written as an SDP (the positive semidefinite constraint reduces to nonnegative diagonal entries when the matrix is diagonal). So the SDP feasible region contains the LP feasible region, meaning the SDP relaxation is at least as tight. For many problems it is strictly tighter: the MAX-CUT LP relaxation has integrality gap 1/2 (every LP solution can be rounded to a cut of half the edges), while the SDP integrality gap is ~0.878. This extra power comes from the ability to capture pairwise correlations between variables through the matrix structure, which LP's linear constraints cannot express."

- question: "Explain the connection between the Unique Games Conjecture and the optimality of the Goemans-Williamson MAX-CUT algorithm."
  type: short-answer
  answer: "The Unique Games Conjecture (UGC), proposed by Khot in 2002, states that for every epsilon > 0 it is NP-hard to determine whether a unique-label constraint satisfaction problem has a solution satisfying 1-epsilon or at most epsilon of constraints. Khot, Kindler, Mossel, and O'Donnell (2007) proved that assuming the UGC, it is NP-hard to approximate MAX-CUT better than the Goemans-Williamson ratio of ~0.878. This means the SDP relaxation + hyperplane rounding is an OPTIMAL polynomial-time algorithm for MAX-CUT (assuming UGC and P != NP). More broadly, the UGC predicts that for many CSPs, the SDP integrality gap exactly characterizes the best achievable approximation ratio — making SDP relaxations the 'right' tool for these problems."
  explanation: "The UGC remains unproven but has become the central conjecture in approximation algorithm theory. If true, it provides a satisfying picture: the computational difficulty of approximating a problem is captured by the algebraic difficulty of rounding its SDP relaxation."

- question: "SDPs can be solved exactly in polynomial time using interior point methods."
  type: true-false
  answer: false
  explanation: "SDPs can be solved to arbitrary precision epsilon in time polynomial in the input size and log(1/epsilon) using interior point methods or the ellipsoid method — but not exactly in general (the optimal value may be irrational). For the purposes of approximation algorithms, polynomial-precision solutions suffice: the rounding step introduces much larger error than the SDP solver's precision. In practice, SDP solvers are significantly slower than LP solvers — the positive semidefinite constraint is harder to enforce than linear constraints — which motivates research into faster SDP algorithms and combinatorial alternatives that avoid solving SDPs altogether."
```

## Explainer

Linear programming relaxation, which you studied in approximation algorithms, replaces integer variables with continuous ones. Semidefinite programming relaxation is a more powerful generalization that replaces scalar variables with matrix variables constrained to be positive semidefinite. This extra structure captures pairwise relationships between variables — correlations, angles, inner products — that linear constraints cannot express. The result is tighter relaxations and better approximation ratios for many combinatorial problems.

The Goemans-Williamson algorithm for MAX-CUT is the most celebrated application. The integer program assigns each vertex a value in {-1, +1}, and the cut value is sum_{(i,j)} (1 - x_i * x_j) / 2. The SDP relaxation replaces scalars x_i with unit vectors v_i in R^n and optimizes sum_{(i,j)} (1 - v_i dot v_j) / 2 subject to |v_i| = 1. This can be reformulated as optimizing over a positive semidefinite matrix Y with Y_ii = 1 and Y_ij = v_i dot v_j. The SDP optimum is at least the integer optimum. The rounding step chooses a random hyperplane through the origin and assigns vertices to sides based on which side their vector falls on. The probability of separating v_i and v_j is arccos(v_i dot v_j) / pi, and the worst-case ratio of this probability to the SDP contribution (1 - v_i dot v_j)/2 is approximately 0.878.

The 0.878 ratio is remarkable because it is optimal under the Unique Games Conjecture: no polynomial-time algorithm can do better unless the conjecture fails or P = NP. This creates a tight connection between the algebraic structure of the SDP relaxation (its integrality gap) and the computational complexity of the problem (its hardness of approximation). For MAX-CUT, these match at ~0.878. For MAX-2SAT, the optimal ratio is ~0.940, again achieved by SDP rounding. The Unique Games Conjecture predicts this pattern extends broadly: the SDP integrality gap is the correct answer for many constraint satisfaction problems.

SDP hierarchies — the Lasserre hierarchy, Sum-of-Squares (SoS) — systematically strengthen SDP relaxations by adding higher-order moment constraints. After O(n) levels, the Lasserre hierarchy captures the integer hull exactly (but at exponential cost). The research frontier asks: how many levels suffice for good approximations? The Sum-of-Squares hierarchy has emerged as a unifying framework connecting approximation algorithms, proof complexity, and machine learning, with applications ranging from planted clique detection to tensor decomposition.
