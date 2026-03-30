---
id: submodular-optimization
title: Submodular Optimization
domain: computer-science
course: advanced-algorithms
prerequisites:
- id: greedy-algorithms
  type: hard
- id: approximation-algorithms-advanced
  type: hard
- id: matroid-intersection
  type: soft
tags:
- submodular-functions
- diminishing-returns
- greedy-approximation
- combinatorial-optimization
stage: expert
status: validated
---

# Submodular Optimization

## Core Idea
A set function f: 2^V -> R is submodular if it satisfies diminishing returns: for all A subset B and element x not in B, f(A + x) - f(A) >= f(B + x) - f(B). Adding an element to a smaller set helps at least as much as adding it to a larger set. Submodular functions arise naturally in coverage (how many distinct customers are reached?), information gain (how much entropy is reduced?), and network influence (how many nodes are activated?). For monotone submodular maximization subject to a cardinality constraint, the greedy algorithm achieves approximation ratio (1 - 1/e) ≈ 0.632, and this is optimal unless P = NP. Submodular minimization (the dual problem) is solvable exactly in polynomial time via the Lovász extension and convex optimization — a surprising asymmetry between maximization and minimization.

## Questions

```yaml
- question: "The greedy algorithm for monotone submodular maximization under a cardinality constraint (select k elements to maximize f) achieves approximation ratio (1 - 1/e). What drives this specific ratio?"
  type: multiple-choice
  options:
    - "The ratio comes from counting arguments about set sizes"
    - "Each greedy step captures at least 1/k of the remaining gap to OPT (by submodularity, the best single addition is at least (OPT - f(S_i))/k). After k steps, the remaining gap is at most (1 - 1/k)^k * OPT ≈ OPT/e, so f(S_k) >= (1 - 1/e) * OPT"
    - "The ratio is an artifact of the analysis and the true guarantee is 1"
    - "The ratio depends on the specific submodular function and is not universal"
  answer: 1
  explanation: "Let S_i be the greedy set after i steps and S* be the optimal k-element set. By submodularity, the marginal gain of the greedy choice at step i+1 is at least (f(S*) - f(S_i))/k (because adding each element of S* to S_i gains at least as much as adding it to S* minus itself, and the greedy picks the best one). So f(S_{i+1}) - f(S_i) >= (OPT - f(S_i))/k, which gives f(S_k) >= (1 - (1-1/k)^k) * OPT >= (1 - 1/e) * OPT. The factor (1 - 1/k)^k -> 1/e is a fundamental quantity from the analysis of geometric convergence. Feige (1998) showed that (1 - 1/e) is optimal: no polynomial algorithm achieves a better ratio unless P = NP."

- question: "Submodular MINIMIZATION (finding the set S that minimizes a submodular function f) can be solved in polynomial time, while submodular MAXIMIZATION under constraints is NP-hard."
  type: true-false
  answer: true
  explanation: "This asymmetry is remarkable. Submodular minimization is equivalent to minimizing a convex function (the Lovász extension of a submodular function is convex), so it can be solved via convex optimization techniques — the Cunningham algorithm and the Iwata-Fleischer-Fujishige algorithm both achieve polynomial time. Submodular maximization, by contrast, includes MAX-CUT and maximum coverage as special cases, which are NP-hard. The greedy (1-1/e) approximation for monotone maximization and the double-greedy 1/2 approximation for unconstrained (non-monotone) maximization are the best possible. This mirrors the asymmetry in convex optimization: minimization is easy, maximization is hard."

- question: "Explain why the maximum coverage problem (select k sets from a collection to maximize the number of covered elements) is a special case of submodular maximization, and what this implies about its approximability."
  type: short-answer
  answer: "Define f(S) = |union of sets in S| for a subcollection S of the given sets. This function is submodular because adding a set to a larger collection covers fewer NEW elements than adding it to a smaller collection (diminishing returns — elements already covered by the larger collection provide no additional benefit). It is also monotone (adding a set never decreases coverage). Maximum coverage asks to maximize this monotone submodular function subject to |S| <= k, so the greedy algorithm achieves (1-1/e)-approximation. Feige proved this is tight: no polynomial algorithm achieves (1-1/e+epsilon)-approximation for maximum coverage unless P = NP. This hardness result transfers to all monotone submodular maximization, making (1-1/e) the universal optimal ratio for this class."
  explanation: "Maximum coverage appears in facility location, sensor placement, influence maximization in social networks, and feature selection in machine learning. The clean (1-1/e) guarantee makes greedy the algorithm of choice for all these applications."

- question: "The multilinear extension of a submodular function enables continuous relaxation techniques (analogous to LP relaxation) for submodular maximization under complex constraints."
  type: true-false
  answer: true
  explanation: "The multilinear extension F(x) = E[f(R(x))] (where R(x) is a random set including each element i independently with probability x_i) extends the discrete submodular function to the continuous domain [0,1]^n. F is neither convex nor concave, but it is concave along positive directions (a consequence of submodularity). The continuous greedy algorithm (Calinescu et al.) maximizes F over a matroid polytope, then rounds the fractional solution using pipage rounding or contention resolution. This achieves (1-1/e)-approximation for monotone submodular maximization subject to matroid constraints — extending the greedy guarantee from cardinality to matroid constraints."
```

## Explainer

Submodularity is the discrete analog of concavity, and it appears wherever "diminishing returns" is a natural property. If f(S) measures the value of selecting set S, submodularity says that adding a new element to a small selection is at least as valuable as adding it to a large selection. This captures coverage functions (each new sensor covers some new area, but less as more are deployed), information-theoretic quantities (mutual information, entropy), and economic production functions.

The greedy algorithm for monotone submodular maximization under a cardinality constraint is remarkably simple: start empty, and repeatedly add the element with the largest marginal gain. The analysis shows that each step captures at least 1/k of the remaining optimality gap (where k is the cardinality bound), leading to geometric convergence that leaves at most a (1-1/k)^k ≈ 1/e fraction of the optimal value uncaptured. The resulting (1-1/e)-approximation is tight: Feige proved that no polynomial algorithm does better unless P = NP, via a reduction from MAX-3SAT. The greedy algorithm is optimal, and it is also dirt simple — a rare and satisfying coincidence.

The minimization side is strikingly different. Submodular minimization — finding arg min_S f(S) with no constraints — is solvable in strongly polynomial time. The key insight is the Lovász extension: every submodular function f has a convex extension to [0,1]^n defined by f_L(x) = E[f(X_theta)] where X_theta = {i : x_i >= theta} for uniform theta in [0,1]. Minimizing f over subsets of V is equivalent to minimizing f_L over [0,1]^n, which is a convex optimization problem. Algorithms based on the ellipsoid method or combinatorial approaches (Cunningham, Iwata-Fleischer-Fujishige) achieve polynomial time. This convexity of minimization versus the NP-hardness of maximization mirrors the broader landscape: finding valleys is easy, finding peaks is hard.

The continuous relaxation framework extends submodular optimization to complex constraints beyond cardinality. The multilinear extension F(x) extends f to the continuous cube [0,1]^n, and the continuous greedy algorithm maximizes F over a polyhedral constraint (like a matroid polytope) using gradient ascent in the fractional domain. Rounding the fractional solution back to an integer set uses techniques like pipage rounding (which moves the fractional solution to a vertex while only increasing the objective) or contention resolution schemes. This framework achieves (1-1/e)-approximation for monotone submodular maximization subject to matroid constraints, unifying and extending the classical greedy result.
