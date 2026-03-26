---
id: algorithm-complexity
title: Algorithm Analysis and Complexity Classes
domain: mathematics
course: discrete-math
prerequisites:
- id: big-o-notation
  type: hard
- id: recurrence-relations
  type: soft
builds-toward:
- divide-and-conquer-recurrences
tags:
- algorithm-analysis
- time-complexity
- P-vs-NP
- NP-complete
- sorting-algorithms
stage: formal-systems
status: validated
---

# Algorithm Analysis and Complexity Classes

## Core Idea
Algorithm analysis applies Big-O notation to classify algorithms by their time and space requirements as functions of input size n. Linear search is O(n); binary search is O(log n); comparison-based sorting is Ω(n log n), achieved by merge sort and heap sort. The complexity classes P (problems solvable in polynomial time) and NP (problems whose solutions are verifiable in polynomial time) frame the central open question of theoretical computer science: whether P = NP. NP-complete problems — the hardest problems in NP — include SAT, graph coloring, and Hamiltonian circuits.

## How It's Best Learned
Analyze familiar algorithms step by step, deriving their complexity by counting operations as a function of n. Understand binary search's O(log n) cost from the halving argument. Discuss P vs. NP conceptually: why verifying a solution is often easier than finding one.

## Common Misconceptions
- Thinking O(n²) is always worse than O(n log n) for all n — for small inputs, constants dominate.
- Confusing the complexity of an algorithm with the complexity of a problem (the problem's complexity is the minimum over all correct algorithms).
- Believing NP stands for 'not polynomial' — NP means solutions are verifiable in polynomial time.

## Questions

```yaml
- question: "What does 'NP' stand for in the complexity class NP?"
  type: multiple-choice
  options: ["Not Polynomial", "Non-deterministic Polynomial", "Nearly Polynomial", "Nondeterministic Provable"]
  answer: 1
  explanation: "NP stands for Nondeterministic Polynomial time. It refers to problems that a nondeterministic Turing machine could solve in polynomial time — equivalently, problems whose proposed solutions can be *verified* in polynomial time by a deterministic machine. 'Not Polynomial' is the most common misconception; NP actually includes problems that may or may not be solvable in polynomial time (that's the open P vs NP question)."

- question: "For large input sizes, an O(n²) algorithm is generally slower than an O(n log n) algorithm."
  type: true-false
  answer: false
  explanation: "Big-O describes asymptotic behavior — how runtime grows as n approaches infinity. For small n, constants and lower-order terms dominate, so an O(n²) algorithm with a tiny constant can outperform an O(n log n) algorithm with a large one. The statement is eventually true for sufficiently large n, but 'always' is wrong. In practice, the crossover point matters, which is why algorithm selection depends on expected input size."

- question: "Explain in your own words why binary search runs in O(log n) time."
  type: short-answer
  answer: "Binary search halves the search space at each step. Starting with n elements, after one comparison you have n/2 remaining; after two, n/4; and so on. The number of steps needed to reduce n to 1 is log₂(n), because you are asking 'how many times can I halve n before reaching 1?' — which is the definition of the base-2 logarithm."
  explanation: "The halving argument is the key intuition. Any algorithm that discards a constant fraction of its remaining work at each step will have logarithmic complexity. This is why binary search, balanced BST operations, and many divide-and-conquer algorithms share the O(log n) signature — they all reduce the problem size multiplicatively rather than additively."
```

## Explainer

You already know Big-O notation — the language for describing how an algorithm's resource use grows as input size grows. Algorithm complexity analysis applies that language systematically to compare algorithms and, at a deeper level, to classify the problems themselves. The key shift is from "how fast is this algorithm?" to "how fast *can* any algorithm for this problem be?"

Start with sorting. Algorithms like bubble sort and insertion sort run in O(n²) in the worst case: they compare each element against roughly every other element. Merge sort and heap sort achieve O(n log n) by exploiting divide-and-conquer structure — they split the problem, solve each half, and merge, doing O(n) merge work at O(log n) levels of recursion. The remarkable fact is that this is *optimal*: any comparison-based sorting algorithm must perform at least Ω(n log n) comparisons in the worst case. You can prove this with an information-theoretic argument — there are n! possible orderings of n elements, and each comparison eliminates at most half the possibilities, so you need at least log₂(n!) ≈ n log n comparisons to identify the correct one. No sorting algorithm that works only by comparison can do better.

Binary search achieves O(log n) by a different divide-and-conquer insight: at each step, it compares the target against the middle element and discards the half that cannot contain the target. Starting with n elements, each comparison halves the search space — after k comparisons, at most n/2^k elements remain. You need k large enough that n/2^k = 1, which gives k = log₂(n). Any algorithm that multiplicatively shrinks its remaining work at each step will have logarithmic complexity.

The classification of problems into complexity classes P and NP is one of the deepest open questions in mathematics. P is the class of problems solvable in polynomial time — O(n^k) for some fixed k. NP is the class of problems whose *solutions can be verified* in polynomial time. Finding a Hamiltonian circuit (a path visiting every vertex exactly once) in a graph is hard — no polynomial algorithm is known. But if someone hands you a proposed circuit, you can verify in O(n) time that it visits every vertex exactly once. This asymmetry between finding and checking is what defines NP. Whether P = NP — whether every problem whose solution is easy to verify is also easy to solve — is unresolved. Most complexity theorists believe P ≠ NP, but no one has proved it.

NP-complete problems sit at the hardest end of NP: they are in NP, and every problem in NP can be reduced to them in polynomial time, meaning a polynomial algorithm for any NP-complete problem would imply P = NP. SAT (can a boolean formula be satisfied?), graph coloring, and the traveling salesman problem are all NP-complete. In practice, this means that if you encounter an NP-complete problem in an application, you should not expect to find an efficient exact algorithm — the field instead turns to approximation algorithms, heuristics, or exploiting special structure in real-world instances.
