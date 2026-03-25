---
id: greedy-algorithms
title: Greedy Algorithms
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: algorithm-design-basics
  type: hard
- id: time-space-complexity
  type: hard
- id: heaps-and-priority-queues
  type: soft
- id: mathematical-induction
  type: soft
- id: big-o-complexity-analysis
  type: soft
- id: knapsack-0-1-bounded
  type: soft
builds-toward:
- dijkstras-algorithm
tags:
- greedy
- algorithm-design
- optimization
- exchange-argument
stage: formal-systems
status: validated
---
# Greedy Algorithms

## Core Idea
A greedy algorithm makes the locally optimal choice at each step with the intent of finding a global optimum. Greedy algorithms work correctly when the problem has a greedy-choice property (a local optimum leads to a global optimum) and optimal substructure. Classic greedy problems include activity selection, fractional knapsack, Huffman coding, and minimum spanning trees. Correctness is typically proved via an exchange argument: showing that replacing a greedy choice with any alternative cannot improve the solution.

## How It's Best Learned
Implement activity selection (interval scheduling maximization) and Huffman encoding. For each problem, attempt a formal exchange argument for correctness before coding. Contrast greedy with DP: the 0/1 knapsack requires DP, while the fractional knapsack is solvable greedily.

## Common Misconceptions
- Greedy algorithms are not always correct; coin change with arbitrary denominations is a classic failure case.
- Proving a greedy algorithm correct requires a formal exchange argument — intuition is not sufficient and frequently misleads.
- An efficient greedy algorithm may still require a priority queue (O(log n) per step) rather than being O(1) per step.

## Questions

```yaml
- question: "You have coins of denominations [1, 6, 10] and want to make change for 12. The greedy algorithm (always pick the largest coin that fits) returns [10, 1, 1] = 3 coins. What is the actual minimum?"
  type: multiple-choice
  options: ["3 coins: [10, 1, 1]", "2 coins: [6, 6]", "2 coins: [10, 2] — but 2 doesn't exist", "4 coins: [1, 1, 1, 1, ...]"]
  answer: 1
  explanation: "The greedy solution picks 10 first, then must use two 1s — total 3 coins. But [6, 6] achieves the same 12 using only 2 coins. This is the classic failure case showing that greedy does NOT always produce the optimal solution for coin change with arbitrary denominations. Standard denominations like US coins work greedily, but this example breaks that assumption."

- question: "If a problem has both the greedy-choice property and optimal substructure, then a greedy algorithm is guaranteed to find the global optimum."
  type: true-false
  answer: true
  explanation: "These two properties are exactly what makes greedy algorithms provably correct. The greedy-choice property ensures that a locally optimal choice is always part of some globally optimal solution. Optimal substructure ensures that after making a greedy choice, the remaining subproblem also has an optimal solution that can be built greedily. Together, they allow induction over the solution construction."

- question: "What is an exchange argument, and why is it used to prove greedy algorithms correct?"
  type: short-answer
  answer: "An exchange argument shows that any optimal solution can be transformed into the greedy solution without degrading its quality. You take a hypothetical optimal solution that differs from the greedy one, swap one non-greedy choice for the corresponding greedy choice, and show the result is no worse. Repeating this exchange converts the optimal solution into the greedy solution, proving the greedy solution is also optimal."
  explanation: "Intuition that a greedy choice 'seems best' is not a proof. The exchange argument is a formal proof technique: it shows that deviating from the greedy choice cannot help, by demonstrating a swap that is value-neutral or value-improving. This is necessary because greedy algorithms lack the exhaustive search of dynamic programming, so correctness must be argued directly from the structure of the problem."
```

## Explainer

A greedy algorithm builds a solution one step at a time, always making the choice that looks best right now without reconsidering past decisions. The appeal is efficiency: greedy algorithms are typically fast and simple to implement. The danger is incorrectness: making the locally optimal choice at each step does not automatically yield a globally optimal solution unless the problem has special structure.

The two properties that guarantee correctness are **greedy-choice property** and **optimal substructure**. Optimal substructure — which you've seen in dynamic programming — means that an optimal solution to the whole problem contains optimal solutions to its subproblems. The greedy-choice property is stronger: it says that a locally optimal (greedy) choice at each step is always part of *some* globally optimal solution. When both hold, you can safely commit to each greedy decision and recurse on what remains.

The canonical example is the **activity selection problem**: given a set of intervals (events with start and end times), select the maximum number of non-overlapping events. The greedy strategy — always pick the event that ends earliest — is provably optimal. Why? After choosing the earliest-ending event, the remaining problem is identical in structure, and no other first choice could leave more room for future events. This is the greedy-choice property in action. A formal proof uses an exchange argument: take any optimal schedule that doesn't start with the earliest-ending event; swap in the earliest-ending event instead; the result is no worse (it still fits, and the remaining time is at least as large).

Contrast this with the **0/1 knapsack problem**, where items cannot be split. Greedy (take the highest value-per-weight item first) fails because committing to one item irrevocably forecloses combinations that would have been better. The fractional knapsack, where items can be broken into pieces, *does* have the greedy-choice property — you always take as much as possible of the highest ratio item — which is why it is solvable greedily while 0/1 requires dynamic programming. This contrast illustrates that the difference between greedy and DP is not about complexity but about problem structure.

In practice, many greedy algorithms require a sorted order or a priority queue to efficiently find the next best choice. Huffman coding builds an optimal prefix-free code by repeatedly merging the two lowest-frequency symbols — each merge requires finding the minimum, which is O(log n) with a min-heap, making the full algorithm O(n log n). Dijkstra's shortest-path algorithm is another greedy algorithm using a priority queue to always extend the currently shortest known path. Understanding greedy algorithms is therefore not just about knowing when they work, but about connecting the proof of correctness to the right data structure for implementation.
