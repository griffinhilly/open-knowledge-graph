---
id: amortized-analysis
title: Amortized Analysis
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: time-space-complexity
  type: hard
- id: big-o-notation
  type: soft
- id: algorithm-complexity
  type: soft
- id: amortized-time-complexity
  type: soft
builds-toward:
- union-find
- hash-tables
tags:
- amortized
- complexity
- analysis
- aggregate
stage: formal-systems
status: validated
---

# Amortized Analysis

## Core Idea
Amortized analysis determines the average cost per operation over a sequence of operations, even when individual operations vary in cost. The key insight is that expensive operations (like resizing a dynamic array) happen infrequently enough that their cost is spread — amortized — over many cheap operations. Three common methods are aggregate analysis, the accounting method, and the potential method. Dynamic array append is O(1) amortized even though periodic resizing costs O(n).

## How It's Best Learned
Study the dynamic array append operation as the canonical example. Work through both the aggregate method (total cost / n operations) and the accounting method (assign credits to operations) to build intuition for each approach.

## Common Misconceptions
- Amortized cost is not the same as average-case cost; it applies to sequences of operations on a single data structure, not random inputs.
- An operation with O(1) amortized cost can still be O(n) in the worst case for a single call — real-time systems must account for this.

## Explainer

You already know how to analyze the worst-case time complexity of individual operations using Big-O notation. But sometimes worst-case analysis per operation is misleadingly pessimistic. Consider appending to a dynamic array that doubles its capacity when full. The occasional resize copies all n elements — O(n) work — but most appends just write to the next slot in O(1). If you report the append operation as O(n) worst-case, you dramatically overstate its typical cost. **Amortized analysis** resolves this by asking: what is the total cost of n operations, divided by n?

The simplest method is **aggregate analysis**. For the dynamic array, start with capacity 1 and append n elements. Resizes happen at sizes 1, 2, 4, 8, ..., up to n, copying 1 + 2 + 4 + ... + n ≈ 2n elements total. Add the n constant-time writes, and the total work is about 3n. Divide by n operations, and each append costs O(1) amortized. The expensive resizes are rare enough that their cost, spread across all operations, vanishes into a constant.

The **accounting method** offers a different intuition. Instead of computing totals after the fact, you assign each operation a fixed "charge" — its amortized cost — and show that the accumulated credit always covers future expenses. For dynamic array appends, charge each append 3 units: 1 unit to write the element, and 2 units saved as credit. When a resize happens, every element that needs copying has 2 units of prepaid credit sitting on it — exactly enough to cover the copy. The charges never go negative, which proves the amortized bound is valid. Think of it like paying a subscription: a steady monthly fee covers the occasional expensive repair.

The **potential method** formalizes this with a potential function Φ that maps the data structure's state to a non-negative number representing stored-up "energy." The amortized cost of an operation equals its actual cost plus the change in potential. For cheap operations, potential increases (energy stored); for expensive operations, potential decreases (energy released to pay for the work). As long as potential never drops below its initial value, the sum of amortized costs bounds the sum of actual costs. This method is the most powerful of the three — it handles complex data structures like splay trees and Fibonacci heaps where the accounting method becomes unwieldy.

The critical distinction from your prerequisite knowledge: amortized cost is not average-case cost. Average-case analysis assumes a probability distribution over inputs. Amortized analysis makes no probabilistic assumptions — it guarantees that *any* sequence of n operations costs at most n times the amortized bound. It is a worst-case guarantee over sequences, not over individual operations. This is what makes it trustworthy for algorithm design: you can rely on O(1) amortized append cost regardless of the input pattern.
