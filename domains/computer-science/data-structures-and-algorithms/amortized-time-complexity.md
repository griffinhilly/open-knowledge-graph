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

## Questions

```yaml
- question: "A colleague says 'dynamic array insertion is O(n) because resizing copies all existing elements.' What is the most accurate response?"
  type: multiple-choice
  options:
    - "They are wrong — resizing only moves a pointer, not all elements"
    - "They are right about the worst-case single-operation cost, but misleading because resizing is rare enough that the amortized cost per insertion is O(1)"
    - "They are correct — dynamic arrays are O(n) insertion and should be avoided"
    - "They are wrong — the copying cost is O(log n) because doublings are exponential"
  answer: 1
  explanation: "The colleague correctly identifies that a single insertion during a resize costs O(n). But reporting only the worst single-operation cost gives a misleading picture. Amortized analysis shows that over n insertions, total copying cost is at most 2n (geometric series), so the amortized cost per insertion is O(1). The expensive resize is real, but it's paid for by the many cheap O(1) insertions that preceded it. This is precisely why amortized analysis exists: to give a realistic per-operation cost when the worst case is rare."

- question: "What is the most important distinction between amortized analysis and average-case analysis?"
  type: multiple-choice
  options:
    - "Amortized analysis applies only to data structures; average-case applies to algorithms"
    - "Amortized analysis assumes random inputs; average-case analysis works for adversarial inputs"
    - "Amortized analysis gives a deterministic guarantee over any input sequence; average-case analysis requires an assumption about input distribution"
    - "Amortized analysis uses the potential method; average-case analysis uses expected value calculations"
  answer: 2
  explanation: "The crucial distinction is probabilistic vs. deterministic. Average-case says: 'if inputs are drawn from distribution X, the expected cost is Y' — a pathological sequence might do far worse. Amortized says: 'for ANY sequence of n operations, total cost is at most n × (amortized bound)' — no probability, no distributional assumption. This deterministic guarantee is strictly stronger for data structure design, where you can't control what operation sequences a user will perform."

- question: "A data structure with an amortized O(1) insertion cost may occasionally perform a single insertion that takes O(n) time."
  type: true-false
  answer: true
  explanation: "Amortized analysis describes long-run averages, not individual operation costs. A dynamic array does exactly this: most insertions are O(1), but resizes copy all n elements in O(n). The amortized O(1) bound guarantees that over a long sequence, the average cost per insertion is O(1) — expensive operations are rare enough and cheap ones numerous enough to average out. Mistaking 'amortized O(1)' for 'every operation is O(1)' is a common misreading of what amortized analysis guarantees."

- question: "Amortized analysis and average-case analysis give identical guarantees for dynamic array insertion, so they can be used interchangeably."
  type: true-false
  answer: false
  explanation: "While both happen to give O(1) for dynamic array insertion, they rest on fundamentally different foundations. Amortized analysis guarantees O(1) per insertion for *any* sequence of operations — deterministically. Average-case analysis would require assuming a distribution over operation sequences — probabilistically. For a pathological sequence deliberately designed to trigger many resizes, average-case bounds might not hold, but amortized bounds still do. They are not equivalent methods and cannot be used interchangeably in general."

- question: "Use the aggregate method to explain why inserting n elements into a dynamic array (which doubles capacity when full) has O(1) amortized cost per insertion."
  type: short-answer
  answer: "Start with capacity 1. Resizes occur at sizes 1, 2, 4, 8, ..., up to n, with copying costs 1, 2, 4, 8, ..., n respectively. Total copying cost = 1 + 2 + 4 + ... + n ≤ 2n (geometric series). Add n for the n individual insertions: total cost = O(n). Divide by n operations: amortized cost per insertion = O(1)."
  explanation: "The key insight is that doubling makes resizes exponentially rare. The kth resize costs 2^k copies but takes 2^k insertions to trigger, so each copy is paid for by exactly one prior insertion. If instead the array grew by 1 each time, resizes would occur at every step: total cost = 1 + 2 + 3 + ... + n = O(n²), giving O(n) amortized per insertion — dramatically worse. The doubling strategy is what makes the amortized O(1) bound possible."
```

## Explainer

You know from big-O analysis how to characterize the worst-case cost of a single operation. But sometimes worst-case analysis per operation is misleadingly pessimistic. Consider a dynamic array (like Python's `list` or Java's `ArrayList`). When the array is full and you insert a new element, it must allocate a new array of double the size, copy all existing elements over, and then insert. That single insertion costs O(n). If you only report worst-case per operation, you'd say insertion is O(n) — which makes dynamic arrays sound terrible. But that expensive copy only happens once every n insertions. The other n-1 insertions are O(1). **Amortized analysis** captures this reality: it spreads the cost of expensive operations across the cheap ones to give a per-operation cost that reflects long-term behavior.

The simplest way to build intuition is the **aggregate method**. Count the total cost of n operations, then divide by n. For the dynamic array, start with capacity 1. After 1 insertion, you resize (cost 1). After 2 insertions, resize again (cost 2). After 4, resize (cost 4). After 8, resize (cost 8). The total copying cost over n insertions is 1 + 2 + 4 + 8 + ... + n = 2n - 1, which is O(n). Add the n constant-time insertions themselves, and the total is O(n). Divide by n operations: the amortized cost per insertion is O(1). The expensive operations are rare enough that they vanish into the average.

The **accounting method** (also called the banker's method) makes this more rigorous by assigning a fixed "charge" to each operation. For dynamic array insertion, charge each insertion 3 units instead of 1. One unit pays for the insertion itself. The other 2 units are saved as "credit" stored on the element. When a resize happens, each element that needs to be copied spends its saved credit to pay for the copy. As long as the total credit never goes negative — meaning you never spend more than you've charged — the amortized cost per operation is valid. This method is powerful because it proves the amortized bound without needing to know the exact sequence of operations in advance.

The **potential method** formalizes the same idea mathematically. You define a **potential function** Φ that maps the state of the data structure to a non-negative number (think of it as stored energy, like a compressed spring). The amortized cost of an operation is its actual cost plus the change in potential: â_i = c_i + Φ(D_i) - Φ(D_{i-1}). Cheap operations that increase potential are "charged extra" (building up energy), and expensive operations that decrease potential are "subsidized" (releasing stored energy). For the dynamic array, Φ = 2 × (number of elements) - (capacity) works perfectly: it grows during cheap insertions and drops to zero during resizes, exactly absorbing the copying cost.

The critical distinction to internalize is that amortized analysis is not probabilistic. Unlike average-case analysis, which assumes inputs are drawn from some distribution, amortized bounds hold for *any* sequence of operations. There is no randomness, no assumption about input patterns. The guarantee is deterministic: over any sequence of n operations, the total cost will not exceed n times the amortized bound. This makes amortized analysis strictly stronger than average-case analysis for data structure design, which is why it is the standard tool for analyzing structures like dynamic arrays, splay trees, and union-find with path compression.
