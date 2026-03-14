---
id: boyer-moore-algorithm-details
title: Boyer-Moore String Matching Algorithm
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: string-matching-naive-optimized
  type: hard
tags:
- strings
- matching
- algorithms
stage: formal-systems
status: draft
---

# Boyer-Moore String Matching Algorithm

## Core Idea
Boyer-Moore matches from right to left and uses two heuristics: the bad-character rule (skip based on the mismatched character) and the good-suffix rule (skip based on the matched suffix). Preprocessing is O(m + σ) where σ is alphabet size; matching is O(n/m) best-case and O(n·m) worst-case.

## How It's Best Learned
Trace Boyer-Moore by hand on a simple example, watching how right-to-left matching and the bad-character rule skip positions. Implement and compare performance to KMP on both best-case and worst-case inputs.

## Common Misconceptions
- Thinking Boyer-Moore is always faster than KMP; worst-case complexity can be poor on adversarial inputs.
- Forgetting that the good-suffix rule requires additional preprocessing; often only the bad-character rule is implemented.
- Not recognizing that Boyer-Moore's advantage grows with larger alphabets and longer patterns.
