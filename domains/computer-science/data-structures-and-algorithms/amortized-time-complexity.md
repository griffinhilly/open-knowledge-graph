---
id: amortized-time-complexity
title: Amortized Time Complexity
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: big-o-complexity-analysis
  type: hard
tags:
- amortization
- worst-case
- average-case
- data-structures
stage: formal-systems
status: draft
---

# Amortized Time Complexity

## Core Idea
Amortized analysis computes the average cost per operation over a sequence of operations, even when individual operations have wildly different costs. For instance, dynamic array resizing might be O(n) once every n insertions, but the amortized cost per insertion is O(1). This smooths spiky worst-cases into a realistic per-operation average.

## How It's Best Learned
Learn the accounting method: assign different costs to operations and verify the total budget never goes negative. Practice the potential method: track a 'potential' that absorbs expensive operations. Apply both to dynamic arrays, stack-based algorithms, and union-find structures.

## Common Misconceptions
- Amortized time is the same as average-case analysis (amortized guarantees hold for any sequence; average-case assumes random input). - A single operation might actually run in the amortized time (amortized describes the long-term average, not individual operation cost).
