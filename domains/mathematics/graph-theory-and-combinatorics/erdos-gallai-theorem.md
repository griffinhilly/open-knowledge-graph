---
id: erdos-gallai-theorem
title: Erdős-Gallai Theorem
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: degree-sequences
  type: hard
tags:
- graph-theory
- degree-sequences
- extremal
stage: formal-systems
status: draft
---

# Erdős-Gallai Theorem

## Core Idea
The Erdős-Gallai theorem provides a necessary and sufficient condition for a sequence of non-negative integers to be graphical: the sequence must be non-increasing, have even sum, and satisfy a specific inequality at each prefix. This completely characterizes which sequences can be realized as degree sequences of simple graphs.

## How It's Best Learned
Apply the theorem to several candidate sequences—both known-graphical and non-graphical. Verify the inequality holds at each step to develop intuition.

## Common Misconceptions
Just checking that the sum is even is insufficient; many even-sum sequences fail the prefix inequalities and are not graphical.
