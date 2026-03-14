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
- id: big-o-notation
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
