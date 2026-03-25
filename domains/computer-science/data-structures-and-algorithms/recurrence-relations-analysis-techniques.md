---
id: recurrence-relations-analysis-techniques
title: Analyzing Recursive Algorithms via Recurrence Relations
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: recursion-basics
  type: hard
- id: asymptotic-notation-big-o-omega-theta
  type: hard
builds-toward:
- divide-and-conquer-strategy
- dynamic-programming-intro
- recurrence-relations-analysis-techniques
tags:
- recursion
- recurrence
- analysis
stage: formal-systems
status: validated
---

# Analyzing Recursive Algorithms via Recurrence Relations

## Core Idea
Recursive algorithms can be analyzed by setting up recurrence relations—equations describing the running time T(n) in terms of T(n/2), T(n-1), or other smaller inputs. Solving these relations (via substitution, recurrence trees, or the master theorem) yields closed-form complexity bounds.

## How It's Best Learned
Trace recursive calls for small inputs, build a recurrence tree to visualize, then apply master theorem or substitution method. Compare on examples like T(n) = T(n/2) + O(n) for binary search.

## Common Misconceptions
- Forgetting the base case in recurrences.
- Misidentifying the non-recursive work term.
- Assuming all recursive algorithms have the same complexity structure.

## Questions

```yaml
- question: "An algorithm splits a problem of size n into 3 subproblems of size n/3 and does O(n) work combining them. Using the master theorem with T(n) = aT(n/b) + O(n^d), what is the overall time complexity?"
  type: multiple-choice
  options:
    - "O(n) — the combining work dominates"
    - "O(n log n) — since log₃(3) = 1 = d, the work is balanced across levels"
    - "O(n²) — three subproblems causes quadratic growth"
    - "O(log n) — dividing into thirds accelerates convergence"
  answer: 1
  explanation: "Here a = 3, b = 3, d = 1. log₃(3) = 1 = d, so we are in the balanced case of the master theorem, giving O(n^d × log n) = O(n log n). When log_b(a) equals d, the work at each level of the recursion tree sums to the same amount (O(n)), and there are O(log n) levels, producing the O(n log n) result. This is the same case as merge sort — the split ratio and number of subproblems happen to balance. A common mistake is to assume more subproblems always means higher complexity; what matters is whether the recursive work or non-recursive work dominates."

- question: "A student writes a recursive algorithm with the recurrence T(n) = T(n-1) + O(1). A classmate writes one with T(n) = T(n/2) + O(1). Which claim is correct?"
  type: multiple-choice
  options:
    - "Both are O(log n) since both make a single recursive call"
    - "Both are O(n) since both reduce the problem by a constant factor"
    - "The first is O(n) and the second is O(log n) — subtracting 1 vs dividing by 2 differs dramatically"
    - "The first is O(n log n) because n levels each require O(log n) overhead"
  answer: 2
  explanation: "Subtracting 1 from n means n levels until the base case — total O(n). Dividing by 2 means log₂(n) levels — total O(log n). This is a critical difference that many students miss because both recurrences involve a 'single recursive call.' The size of the subproblem matters enormously: T(n-1) produces a linear number of calls (think linear search), while T(n/2) produces logarithmically few (think binary search). Always check whether the size reduction is additive (n - constant → O(n) levels) or multiplicative (n/b → O(log n) levels)."

- question: "A recurrence relation for an algorithm must include a base case to be well-defined, but the base case does not affect the asymptotic complexity."
  type: true-false
  answer: true
  explanation: "True, with an important nuance. The base case (typically T(1) = O(1) or T(1) = c) anchors the recursion and is necessary to avoid infinite regress. However, it contributes only a constant to the total work and doesn't change the big-O class — O(1) absorbed into the leading terms of O(n), O(n log n), etc., is negligible. That said, forgetting the base case when writing the recurrence is a common error that can make a correctly set-up recurrence appear ill-defined. The base case matters for correctness of the recurrence formulation, even if it doesn't change the asymptotic result."

- question: "In the recursion tree for merge sort T(n) = 2T(n/2) + O(n), the total work at every level of the tree is O(n), and there are O(log n) levels, giving O(n log n) overall."
  type: true-false
  answer: true
  explanation: "Correct. At the root, the non-recursive work is O(n) (merging two halves). At the next level, there are 2 nodes each doing O(n/2) work — total O(n). At the next level, 4 nodes each doing O(n/4) — still O(n) total. This constant-per-level work holds all the way down. Since the tree has log₂(n) levels (halving n until reaching size 1), the total is O(n) × O(log n) = O(n log n). This is the intuition behind why the balanced case of the master theorem gives O(n^d log n): costs are distributed evenly across levels."

- question: "Why is correctly setting up the recurrence relation — identifying a, b, and the non-recursive work — the most important step in analyzing a recursive algorithm, rather than the choice of solving technique?"
  type: short-answer
  answer: "The recurrence is a faithful translation of the algorithm's structure into math. Getting a (number of subproblems), b (size reduction factor), and the cost of non-recursive work right is the analytical judgment — it requires understanding what the algorithm actually does. Once the recurrence is correct, solving it via recursion tree, substitution, or master theorem is largely mechanical. An incorrect recurrence will yield a formally valid but wrong complexity answer regardless of how carefully you apply the master theorem."
  explanation: "A common pattern is to misidentify the non-recursive work — for example, treating the merge step in merge sort as O(1) instead of O(n), which would falsely suggest O(log n) complexity. Or miscounting subproblems: an algorithm that makes 4 recursive calls on n/2-sized inputs (T(n) = 4T(n/2) + O(n)) is dramatically different from one making 2 calls (merge sort), even though both 'divide by 2.' The solving technique just mechanically extracts the answer once the recurrence correctly encodes the algorithm's recursive structure."
```

## Explainer

When you write a recursive algorithm, the code itself tells you what happens at each level — divide the input, do some work, recurse on smaller pieces. But to know the algorithm's overall running time, you need to translate that recursive structure into a mathematical equation and solve it. This equation is a **recurrence relation**: it expresses T(n), the time to solve a problem of size n, in terms of the time to solve smaller subproblems plus the non-recursive work at the current level.

Take binary search as a starting example. At each step, you compare the target to the middle element (O(1) work), then recurse on one half. The recurrence is T(n) = T(n/2) + O(1). Merge sort is different: you split the array in two, recurse on both halves, then merge the results in O(n) time. Its recurrence is T(n) = 2T(n/2) + O(n). Notice how the recurrence captures two things your Big-O prerequisite taught you to care about — how many subproblems you create and how much work you do at each level. The base case, typically T(1) = O(1), anchors the recursion.

The **recursion tree** method is the most intuitive way to solve these. Draw each recursive call as a node, labeling it with the non-recursive work at that level. For merge sort, the root does O(n) work and spawns two children, each doing O(n/2) work. Each of those spawns two more at O(n/4). At every level, the total work sums to O(n), and there are log₂(n) levels, giving O(n log n) total. For binary search, each level does O(1) work with one child, so the total across log₂(n) levels is O(log n). The tree makes the pattern visible: you sum the work across all levels.

The **substitution method** takes a guess-and-verify approach. You hypothesize that T(n) = O(n log n) for merge sort, substitute into the recurrence, and prove by induction that the bound holds. This is rigorous but requires a good initial guess — which is why the recursion tree is often used first to build intuition, then substitution to prove it formally. For recurrences that fit the pattern T(n) = aT(n/b) + O(n^d), the **master theorem** gives the answer directly by comparing log_b(a) to d. If they are equal, you get O(n^d log n). If log_b(a) is larger, the recursive calls dominate. If d is larger, the non-recursive work dominates. Merge sort has a = 2, b = 2, d = 1, and since log₂(2) = 1 = d, you immediately get O(n log n). Learning to set up the recurrence correctly — identifying a, b, and the cost of the non-recursive work — is the core skill. The solving techniques are mechanical once the recurrence is right.
