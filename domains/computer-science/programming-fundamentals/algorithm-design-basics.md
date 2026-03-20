---
id: algorithm-design-basics
title: Algorithm Design Basics
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: functions-defining-calling
  type: hard
- id: recursion-basics
  type: soft
- id: list-operations
  type: soft
- id: loop-control-statements
  type: soft
- id: big-o-notation
  type: soft
- id: debugging-basics
  type: soft
- id: list-comprehensions
  type: soft
- id: methods-and-attributes
  type: soft
- id: nested-loops
  type: soft
tags:
- algorithms
- pseudocode
- problem decomposition
- search
- sort
- complexity
stage: formal-systems
status: validated
---
# Algorithm Design Basics

## Core Idea
Algorithm design is the process of specifying a step-by-step procedure to solve a problem correctly and efficiently. Foundational techniques include linear search (scan until found), binary search (halve the search space each step), selection sort, and insertion sort. Before coding, writing pseudocode makes the logic explicit without syntactic noise. Algorithm correctness is verified by tracing examples; efficiency is characterized by how runtime and memory scale with input size, expressed informally with Big-O notation.

## How It's Best Learned
Implement search and sort algorithms from scratch without looking up the code. Trace them on small arrays by hand. Measure runtime experimentally on different-sized inputs and compare to Big-O predictions.

## Common Misconceptions
- Assuming the first working solution is good enough without considering efficiency.
- Skipping pseudocode and jumping to code, which embeds language-specific confusion into the logic.
- Thinking sorting is always O(n²) — comparison-based sorts can achieve O(n log n).

## Questions

```yaml
- question: "You need to find a target value in a sorted list of 1,024 elements. At most how many comparisons does binary search require?"
  type: multiple-choice
  options: ["10", "512", "1024", "32"]
  answer: 0
  explanation: "Binary search halves the search space with each comparison, so it takes at most log₂(n) comparisons. log₂(1024) = 10. This is the core efficiency advantage over linear search, which would require up to 1,024 comparisons in the worst case."

- question: "Insertion sort always runs in O(n log n) time regardless of the input."
  type: true-false
  answer: false
  explanation: "Insertion sort is O(n²) in the worst case (reverse-sorted input), because each new element may need to be compared and swapped all the way back to the start. It is O(n) on nearly-sorted input, which makes it fast in practice for small or nearly-ordered arrays — but it is not O(n log n) in general. Algorithms like merge sort achieve O(n log n) in all cases."

- question: "Why is writing pseudocode recommended before coding an algorithm?"
  type: short-answer
  answer: "Pseudocode separates the logic of the algorithm from language-specific syntax, making it easier to identify logical errors, edge cases, and termination conditions before implementation details introduce additional complexity."
  explanation: "When you code directly, syntax errors and language quirks distract from logical reasoning. Pseudocode forces you to think through 'what should happen' clearly. Translating correct pseudocode into code is mostly mechanical — the hard thinking is done. Skipping this step embeds logical confusion into implementation, making bugs harder to find."
```

## Explainer

An algorithm is a step-by-step procedure that solves a problem — but a correct answer is only half the job. A procedure that takes 10 steps for a 10-element list but 1,000,000 steps for a 1,000-element list will collapse in real use. The central design challenge is building algorithms that are both correct and efficient, and expressing that efficiency precisely using notation like O(n).

Two fundamental search strategies illustrate the stakes. Linear search scans each element from the start until a match is found — O(n) in the worst case. Binary search works only on sorted data, but eliminates half the remaining candidates at each step by comparing against the midpoint — O(log n). For a list of one million elements, binary search finds the target in at most 20 comparisons; linear search may need a million. The price of binary search is that the data must be sorted first. If you search frequently and sort once, that cost is worth paying. If you search only once, linear may be faster overall.

Sorting reveals a similar design landscape. Selection sort scans for the minimum, places it, and repeats — O(n²). Insertion sort builds a sorted prefix one element at a time — also O(n²) in the worst case, but very fast on nearly-sorted data. More sophisticated algorithms like merge sort and quicksort achieve O(n log n) by splitting the problem in half recursively. The misconception to resist is that O(n²) is always bad and O(n log n) is always better: for small inputs, the simpler algorithms often win due to lower overhead. Big-O describes asymptotic behavior for large inputs, not absolute runtime for small ones.

Pseudocode is not bureaucratic ceremony — it is a discipline that forces you to commit to the logic before getting tangled in syntax. A line like "if the list is empty, return -1" makes an edge case explicit. When you translate to Python or Java, you are filling in syntax around an already-correct structure, not discovering the structure as you type. Skipping pseudocode buries logical confusion under implementation decisions, making debugging much harder.

Tracing an algorithm by hand on a small example is the most reliable correctness check before running code. Walk through a 5-element array step by step, tracking every comparison and swap. This builds the mental model needed to debug when the algorithm fails on edge cases — empty arrays, duplicates, already-sorted inputs — that automated tests may not initially surface. Algorithm fluency is built through this kind of deliberate, slow tracing before you can reliably write code that works the first time.
