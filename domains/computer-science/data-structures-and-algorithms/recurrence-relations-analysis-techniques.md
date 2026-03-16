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
- solving-recurrence-relations-master-theorem
tags:
- recursion
- recurrence
- analysis
stage: formal-systems
status: draft
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

## Explainer

When you write a recursive algorithm, the code itself tells you what happens at each level — divide the input, do some work, recurse on smaller pieces. But to know the algorithm's overall running time, you need to translate that recursive structure into a mathematical equation and solve it. This equation is a **recurrence relation**: it expresses T(n), the time to solve a problem of size n, in terms of the time to solve smaller subproblems plus the non-recursive work at the current level.

Take binary search as a starting example. At each step, you compare the target to the middle element (O(1) work), then recurse on one half. The recurrence is T(n) = T(n/2) + O(1). Merge sort is different: you split the array in two, recurse on both halves, then merge the results in O(n) time. Its recurrence is T(n) = 2T(n/2) + O(n). Notice how the recurrence captures two things your Big-O prerequisite taught you to care about — how many subproblems you create and how much work you do at each level. The base case, typically T(1) = O(1), anchors the recursion.

The **recursion tree** method is the most intuitive way to solve these. Draw each recursive call as a node, labeling it with the non-recursive work at that level. For merge sort, the root does O(n) work and spawns two children, each doing O(n/2) work. Each of those spawns two more at O(n/4). At every level, the total work sums to O(n), and there are log₂(n) levels, giving O(n log n) total. For binary search, each level does O(1) work with one child, so the total across log₂(n) levels is O(log n). The tree makes the pattern visible: you sum the work across all levels.

The **substitution method** takes a guess-and-verify approach. You hypothesize that T(n) = O(n log n) for merge sort, substitute into the recurrence, and prove by induction that the bound holds. This is rigorous but requires a good initial guess — which is why the recursion tree is often used first to build intuition, then substitution to prove it formally. For recurrences that fit the pattern T(n) = aT(n/b) + O(n^d), the **master theorem** gives the answer directly by comparing log_b(a) to d. If they are equal, you get O(n^d log n). If log_b(a) is larger, the recursive calls dominate. If d is larger, the non-recursive work dominates. Merge sort has a = 2, b = 2, d = 1, and since log₂(2) = 1 = d, you immediately get O(n log n). Learning to set up the recurrence correctly — identifying a, b, and the cost of the non-recursive work — is the core skill. The solving techniques are mechanical once the recurrence is right.
