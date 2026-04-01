---
id: exponential-time-hypothesis
title: Exponential Time Hypothesis
domain: computer-science
course: advanced-algorithms
prerequisites:
- id: np-completeness
  type: hard
- id: complexity-class-p-definition
  type: hard
- id: boolean-satisfiability-and-reductions
  type: soft
tags:
- exponential-time-hypothesis
- seth
- lower-bounds
- conditional-hardness
stage: expert
status: validated
---

# Exponential Time Hypothesis

## Core Idea
The Exponential Time Hypothesis (ETH), proposed by Impagliazzo and Paturi, conjectures that k-SAT requires 2^(Omega(n)) time. The Strong Exponential Time Hypothesis (SETH) strengthens this: there is no sequence of algorithms (one per k) such that k-SAT is solvable in 2^((1 - epsilon_k) k n) time for all k, where epsilon_k approaches 0. Equivalently, for infinitely many k, every k-SAT solver requires 2^((1 - o(1)) k n) time. These hypotheses are widely believed but unproven, sitting between P != NP and the strong claim that exponential time is fundamentally necessary. ETH and SETH enable conditional hardness: assuming the hypothesis, one can prove lower bounds on the running time of other problems by reduction, explaining why decades of algorithmic research have not substantially improved brute-force algorithms for many classical problems (3-SUM, Longest Common Subsequence, all-pairs shortest paths).

## Questions

```yaml
- question: "The Strong Exponential Time Hypothesis (SETH) is stronger than P != NP. If SETH is false (i.e., some k-SAT algorithm achieves 2^((1 - epsilon) k n) for all k with epsilon > 0), what would that imply?"
  type: multiple-choice
  options:
    - "P = NP"
    - "There exists a subexponential-time algorithm for k-SAT for each fixed k, but this does not imply P = NP — it only says that the exponential dependence on clause size k can be reduced"
    - "All NP-hard problems have subexponential-time algorithms"
    - "SETH is logically equivalent to P != NP, so disproving SETH proves P = NP"
  answer: 1
  explanation: "SETH is a quantitative strengthening of P != NP. It says that not only is k-SAT exponential in n (which follows from P != NP), but the exponential base is 2^(Omega(k)), meaning the dependence on k is unavoidable. If SETH is false, there are algorithms with running time like 2^(0.9 * k * n), which is subexponential in k for fixed n. This does not contradict P != NP (since for fixed k the dependence on n is still exponential). However, a false SETH would have profound implications for the fine-grained complexity hierarchy — it would suggest that brute-force algorithms for SAT and related problems can be substantially improved in ways currently unknown."

- question: "ETH (not SETH) conjectures that 3-SAT requires 2^(Omega(n)) time. Under ETH, can one-SAT and two-SAT have algorithms substantially faster than 2^(cn) for some c > 0?"
  type: true-false
  answer: true
  explanation: "ETH only makes a claim about one specific problem (3-SAT, or equivalently, all k-SAT with unbounded k). It does not directly constrain the complexity of k-SAT for small fixed k. In fact, 2-SAT is solvable in O(n^2) polynomial time via strongly connected components, and 1-SAT (unit propagation) is trivial. SETH is the hypothesis that makes quantitative claims about ALL k, preventing exponential speedups as k varies. ETH allows for the possibility that 2-SAT, 4-SAT, etc. have drastically faster algorithms than 3-SAT, even if 3-SAT is hard."

- question: "Explain why ETH and SETH are called 'conditional' rather than 'unconditional' hypotheses, and how they are used to prove lower bounds for other problems."
  type: short-answer
  answer: "ETH and SETH are conjectures — unproven assumptions about complexity. Unlike unconditional lower bounds (which hold in all models of computation), conditional hardness says: 'IF the hypothesis is true, THEN this problem requires at least this much time.' Researchers use fine-grained reductions to show that faster algorithms for other problems would contradict SETH. For example, if 3-SUM could be solved in O(n^1.99) time, then (via a known reduction) 3-SAT could be solved faster than SETH predicts, contradicting SETH. Thus, under SETH, 3-SUM requires O(n^2) time. This is not proven hardness but a rigorous conditional statement: the assumptions explain empirical hardness observed across many classical problems."
  explanation: "The conditional approach is practical for algorithm design: problems that reduce to 3-SAT or 3-SUM are guaranteed hard under SETH, giving evidence that fast algorithms may not exist. This is weaker than unconditional hardness but much stronger than saying 'we haven't found a fast algorithm yet.'"

- question: "The Fine-Grained Complexity Conjecture (FGC) is that all NP-hard problems reduce to each other under fine-grained reductions. If FGC is true, then all NP-hard problems require essentially the same exponential time (possibly with different polynomial factors)."
  type: true-false
  answer: false
  explanation: "FGC is not universally accepted and is likely false. While many problems do reduce to k-SAT or 3-SUM and are thereby tied under SETH/3-SUM conjecture, some NP-hard problems may require fundamentally different time — for example, some may be solvable in 2^(sqrt(n)) (like certain graph coloring algorithms), while others seem to require 2^(Omega(n)). The fine-grained complexity landscape is stratified: different problems are believed to have different exponential bases or polynomial dependencies, explaining why the problem space is not flat. ETH and SETH describe specific hard anchors, not a universal hierarchy."
```

## Explainer

The Exponential Time Hypothesis is a precision sharpening of P != NP. While P != NP merely says that k-SAT cannot be solved in polynomial time, ETH and SETH make specific quantitative claims: the running time must be exponential in n, and moreover, the exponential base grows with k (for SETH). These hypotheses are not proven, but they are widely believed based on decades of algorithmic research: all known SAT solvers, despite substantial engineering, have exponential worst-case complexity.

ETH states that there is no 2^(o(n)) algorithm for 3-SAT — in other words, you cannot beat 2^(cn) for any arbitrarily small constant c > 0. This is weaker than claiming 2^(n) is necessary (you could have 2^(0.5 n)), but it rules out subexponential-time solutions. SETH goes further: it asserts that for each k, the exponent in the 2^(e * k * n) running time cannot be reduced — the dependence on k is fundamental. SETH is equivalent to: for every epsilon > 0, there exists k such that k-SAT requires 2^((1 - epsilon) * k * n) time.

The power of ETH and SETH lies in their use as anchors for conditional lower bounds. Suppose you want to prove that problem X cannot be solved faster than O(n^2). A direct lower bound (e.g., information-theoretic) might be infeasible. Instead, construct a fine-grained reduction: a algorithm that, given an O(n^1.99) solver for X, constructs an O(2^(0.99 n)) solver for 3-SAT, contradicting ETH. Thus, under ETH, X requires Omega(n^2) time. This conditional approach has been devastatingly effective: 3-SUM, Longest Common Subsequence, Edit Distance, All-Pairs Shortest Paths, and hundreds of other natural problems are now known to be hard under SETH or 3-SUM conjecture.

The reductions use many techniques: hardness amplification (taking a single hard instance and repeating it with independence), gadget construction (replacing variables with subproblems), and composition. A successful reduction is surprising: it shows that two seemingly unrelated problems (SAT and substring matching, for instance) are algorithmically equivalent at the exponential level, tied together by the underlying hardness assumptions. The fine-grained complexity landscape reveals that the difficulty of computational problems is not binary (polynomial vs. exponential) but stratified: different problems cluster around different hardness anchors (SETH, 3-SUM, Orthogonal Vectors), explaining why some problems resist faster algorithms despite intense effort while others yield to clever algorithms.

The status of SETH remains open, but the conditional hardness web it enables is robust and reveals deep structure in computational difficulty.
