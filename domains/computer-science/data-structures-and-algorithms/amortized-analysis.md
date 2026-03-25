---
id: amortized-analysis
title: Amortized Analysis
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: time-space-complexity
  type: hard
- id: big-o-complexity-analysis
  type: soft
- id: asymptotic-notation-big-o-omega-theta
  type: soft
- id: binary-tree-properties-height-balance-completeness
  type: soft
- id: recurrence-relations-analysis-techniques
  type: soft
builds-toward:
- union-find
- hash-tables
tags:
- amortized
- complexity
- analysis
- aggregate
stage: advanced
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

## Questions

```yaml
- question: "A safety-critical real-time system must guarantee that every operation completes within 1 millisecond. An engineer proposes using a dynamic array (which has O(1) amortized append). Should they use it?"
  type: multiple-choice
  options:
    - "Yes — O(1) amortized means every operation takes constant time in the worst case"
    - "No — 'amortized O(1)' still allows individual append operations to take O(n) time during a resize"
    - "Yes — amortized analysis provides probabilistic guarantees that O(n) resizes rarely occur"
    - "No — dynamic arrays have O(n) amortized append because of resizing overhead"
  answer: 1
  explanation: "This is the critical practical distinction. 'O(1) amortized' means the average cost per operation over a long sequence is O(1) — but individual operations can still cost O(n) when a resize happens. A real-time system that must meet per-operation latency deadlines cannot use amortized guarantees because a single slow operation violates the deadline, even if most operations are fast. For hard real-time requirements, you need data structures with O(1) worst-case per operation. Amortized analysis is about sequences, not individual calls."

- question: "Using the aggregate method, what is the amortized cost of appending n elements to a dynamic array that starts with capacity 1 and doubles on resize?"
  type: multiple-choice
  options:
    - "O(log n) per append — because resizes happen at logarithmic intervals"
    - "O(n) per append — because the final resize copies n elements"
    - "O(1) per append — because total work is ≈ 3n across n appends"
    - "O(√n) per append — because resizes happen √n times"
  answer: 2
  explanation: "Resizes happen at sizes 1, 2, 4, 8, ..., copying 1+2+4+...+n/2 ≈ n elements total from resize operations, plus n constant-time writes for the appends themselves — roughly 3n total work. Dividing by n operations gives O(1) amortized cost per append. Option B (O(n)) is the worst-case for a single operation, not the amortized cost — it's the confusion between per-operation worst-case and amortized-per-operation that this analysis is designed to correct."

- question: "Amortized analysis and average-case analysis both describe how an algorithm performs 'on average,' so they are equivalent in what they guarantee."
  type: true-false
  answer: false
  explanation: "This is the most important misconception to dispel. Average-case analysis assumes a probability distribution over inputs and reports the expected cost for a random input. Amortized analysis makes no probabilistic assumptions — it guarantees that any sequence of n operations (no matter what inputs or access patterns) costs at most n times the amortized bound. Amortized analysis is a deterministic worst-case guarantee over sequences. A data structure with O(1) amortized cost cannot be 'unlucky' — the bound holds for every possible sequence, adversarially chosen or not."

- question: "In the accounting method of amortized analysis, operations are assigned a 'charge' (amortized cost) that may exceed their actual cost, with excess credited for future expensive operations."
  type: true-false
  answer: true
  explanation: "The accounting method charges each operation a fixed amortized cost. For cheap operations (like a simple append), the charge exceeds the actual cost, and the excess is stored as 'credit' on the data structure. When an expensive operation occurs (like a resize), it draws on this accumulated credit to cover its actual cost. As long as the total credit never goes negative, the sum of charges bounds the sum of actual costs. The key invariant is that credit is always non-negative — you can never 'borrow' from future operations."

- question: "Explain why amortized analysis is NOT the same as average-case analysis, and describe a situation where the distinction matters."
  type: short-answer
  answer: "Average-case analysis requires a probability model: it computes the expected cost when inputs are drawn from some distribution. Amortized analysis requires no probability — it bounds the total cost of any sequence of n operations by n times the amortized cost, guaranteeing this holds for all possible sequences, including adversarially constructed ones. The distinction matters when inputs may be adversarial or when the distribution is unknown. For example, a hash table with O(1) average-case lookup might be degraded to O(n) by an adversary who exploits the hash function; an amortized guarantee would hold regardless of what keys are inserted."
  explanation: "A practical example: an algorithm that is O(1) average-case might have O(n) worst-case per operation — and an adversary who controls the inputs could trigger that worst-case on every operation, making the total O(n²). An amortized guarantee of O(1) cannot be exploited this way: the total cost is O(n) regardless of the sequence, because the cost is smoothed across the sequence by design."
```

## Explainer

You already know how to analyze the worst-case time complexity of individual operations using Big-O notation. But sometimes worst-case analysis per operation is misleadingly pessimistic. Consider appending to a dynamic array that doubles its capacity when full. The occasional resize copies all n elements — O(n) work — but most appends just write to the next slot in O(1). If you report the append operation as O(n) worst-case, you dramatically overstate its typical cost. **Amortized analysis** resolves this by asking: what is the total cost of n operations, divided by n?

The simplest method is **aggregate analysis**. For the dynamic array, start with capacity 1 and append n elements. Resizes happen at sizes 1, 2, 4, 8, ..., up to n, copying 1 + 2 + 4 + ... + n ≈ 2n elements total. Add the n constant-time writes, and the total work is about 3n. Divide by n operations, and each append costs O(1) amortized. The expensive resizes are rare enough that their cost, spread across all operations, vanishes into a constant.

The **accounting method** offers a different intuition. Instead of computing totals after the fact, you assign each operation a fixed "charge" — its amortized cost — and show that the accumulated credit always covers future expenses. For dynamic array appends, charge each append 3 units: 1 unit to write the element, and 2 units saved as credit. When a resize happens, every element that needs copying has 2 units of prepaid credit sitting on it — exactly enough to cover the copy. The charges never go negative, which proves the amortized bound is valid. Think of it like paying a subscription: a steady monthly fee covers the occasional expensive repair.

The **potential method** formalizes this with a potential function Φ that maps the data structure's state to a non-negative number representing stored-up "energy." The amortized cost of an operation equals its actual cost plus the change in potential. For cheap operations, potential increases (energy stored); for expensive operations, potential decreases (energy released to pay for the work). As long as potential never drops below its initial value, the sum of amortized costs bounds the sum of actual costs. This method is the most powerful of the three — it handles complex data structures like splay trees and Fibonacci heaps where the accounting method becomes unwieldy.

The critical distinction from your prerequisite knowledge: amortized cost is not average-case cost. Average-case analysis assumes a probability distribution over inputs. Amortized analysis makes no probabilistic assumptions — it guarantees that *any* sequence of n operations costs at most n times the amortized bound. It is a worst-case guarantee over sequences, not over individual operations. This is what makes it trustworthy for algorithm design: you can rely on O(1) amortized append cost regardless of the input pattern.
