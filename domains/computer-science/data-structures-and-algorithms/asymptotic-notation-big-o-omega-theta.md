---
id: asymptotic-notation-big-o-omega-theta
title: 'Asymptotic Notation: Big-O, Big-Omega, Big-Theta'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: algorithm-design-basics
  type: hard
builds-toward:
- time-complexity-classes
- space-complexity-classes
- solving-recurrence-relations-master-theorem
tags:
- complexity-analysis
- big-o
- asymptotics
stage: formal-systems
status: draft
---

# Asymptotic Notation: Big-O, Big-Omega, Big-Theta

## Core Idea
Asymptotic notation describes how algorithms' time and space usage scales with input size. Big-O provides an upper bound, Big-Omega a lower bound, and Big-Theta a tight bound. These notations ignore constant factors and focus on dominant growth rates.

## How It's Best Learned
Start with concrete examples: n² grows faster than n log n, which grows faster than n. Draw or sketch growth curves. Compare 2n vs n² for small values (n=10, 100, 1000) to see the difference. Practice classifying simple code snippets (loops, nested loops, recursion).

## Common Misconceptions
- Big-O is not the 'actual' runtime—it's a bound that ignores constants. O(2n) and O(n) are the same.
- Big-O represents worst-case, not average-case (without qualification). The notation itself is about the function, not which case.
- Confusing O(log n) with O(ln n)—both mean logarithmic, base doesn't matter for big-O.
