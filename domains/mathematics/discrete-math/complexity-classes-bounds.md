---
id: complexity-classes-bounds
title: Complexity Classes and Asymptotic Analysis
domain: mathematics
course: discrete-math
prerequisites:
- id: algorithm-analysis-big-o
  type: hard
tags:
- algorithms
- complexity
stage: formal-systems
status: draft
---

# Complexity Classes and Asymptotic Analysis

## Core Idea
Standard complexity classes ordered by growth: O(1) constant, O(log n) logarithmic, O(n) linear, O(n log n), O(n²) quadratic, O(2^n) exponential, O(n!) factorial. Each class represents fundamentally different algorithm scalability and feasibility on large inputs.

## Explainer

You already know that big-O notation describes how an algorithm's runtime grows relative to input size n. Complexity classes organize that idea into a hierarchy of qualitatively different behaviors. The key insight is that these classes are not just faster or slower versions of each other — they represent fundamentally different scalability. An O(n²) algorithm and an O(n) algorithm are not just "one slower" — at n = 1,000,000, the O(n) algorithm might take a second while the O(n²) takes 11 days.

Start at the bottom of the hierarchy. **O(1) constant** time means the algorithm takes the same effort regardless of input size — looking up an element in a hash table, or reading the first item of a list. **O(log n) logarithmic** time is nearly as good: binary search on a sorted list of a billion items takes about 30 comparisons, because each comparison halves the remaining search space. Any time you can discard half the problem at each step, you get a logarithm. **O(n) linear** time means you must touch every element once — scanning a list for a value, computing a sum. This is the natural floor for problems that require reading all their input.

The middle classes represent common algorithmic tradeoffs. **O(n log n)** is the complexity of efficient comparison-based sorting algorithms (merge sort, heapsort). It's the cost of repeatedly halving — you do O(log n) work, and you must do it for each of the O(n) elements. **O(n²) quadratic** arises from nested loops over the input — comparing every element to every other element. Bubble sort and insertion sort are O(n²). For n = 10,000 items, that's 100 million operations — still manageable. At n = 1,000,000, it's a trillion.

The upper classes are qualitatively infeasible for large inputs. **O(2^n) exponential** means the work doubles with each additional element. Brute-force search over all subsets of n items, solving the traveling salesman problem by checking all routes — these are O(2^n). For n = 50, that's over a quadrillion operations. **O(n!) factorial** is worse still — generating all permutations of n items. For n = 20, that's over 2 quintillion operations. These classes are not just "slow" — they are computationally intractable for any realistic input. The dividing line between polynomial time (O(n^k) for some fixed k) and superpolynomial time (O(2^n), O(n!)) is the central distinction in theoretical computer science, and it motivates the entire P vs NP question.
