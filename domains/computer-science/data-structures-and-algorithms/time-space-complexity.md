---
id: time-space-complexity
title: Time and Space Complexity
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: big-o-notation
  type: hard
- id: algorithm-design-basics
  type: hard
- id: recursion-basics
  type: soft
- id: algorithm-complexity
  type: soft
- id: logarithms-intro
  type: soft
builds-toward:
- amortized-analysis
- merge-sort
- quicksort
- binary-search-algorithm
tags:
- complexity
- big-o
- analysis
- performance
stage: formal-systems
status: draft
---

# Time and Space Complexity

## Core Idea
Time complexity measures how an algorithm's runtime grows as input size increases, while space complexity measures how much memory it uses. Both are expressed using Big-O notation to describe worst-case, average-case, or best-case behavior. Analyzing complexity lets us compare algorithms and choose the most efficient solution for a given problem size. Common complexity classes include O(1), O(log n), O(n), O(n log n), O(n²), and O(2ⁿ).

## How It's Best Learned
Start by analyzing simple loops and nested loops, counting operations as a function of n before abstracting to Big-O. Compare concrete runtimes against theoretical predictions for small inputs. Practice deriving complexity for recursion using substitution or the Master Theorem.

## Common Misconceptions
- Big-O describes worst-case by convention, but average-case and best-case are also meaningful and often reported separately.
- O(n log n) and O(n²) feel similar for small n but diverge dramatically at scale.
- Space complexity includes both auxiliary space and input space; often only auxiliary space is analyzed.
