---
id: knapsack-problem-variations
title: Knapsack Problem and Pseudo-Polynomial Time
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: np-completeness-formal
  type: hard
- id: time-complexity-classes-formal
  type: soft
builds-toward:
- fixed-parameter-tractability
tags:
- np-hard
- optimization
- dynamic-programming
stage: formal-systems
status: validated
---

# Knapsack Problem and Pseudo-Polynomial Time

## Core Idea
The 0/1 knapsack problem is NP-hard in the strong sense, but admits a pseudo-polynomial time algorithm using dynamic programming. This algorithm runs in time O(nW) where W is the knapsack capacity. Pseudo-polynomial algorithms are tractable when input values are small but become exponential if values are encoded in binary, illustrating the distinction between weak and strong NP-hardness.

## How It's Best Learned
Implement the DP solution O(nW) and observe that it depends on the value W, not the bit-length of W. Try the same problem with exponentially large weights to see where the algorithm breaks down.

## Common Misconceptions
- Pseudo-polynomial algorithms solve NP-hard problems (they only work when weights are bounded).
- If W is polynomial in n, the algorithm is polynomial time (it is, but this requires W = poly(n) which is not guaranteed).

## Questions

```yaml
- question: "A dynamic programming solver for 0/1 knapsack runs in O(nW) time. You apply it to an instance with n = 50 items and W = 2^{100}. Is this computation feasible?"
  type: multiple-choice
  options:
    - "Yes — n = 50 is small, so the O(n) factor keeps the total runtime manageable"
    - "No — W = 2^{100} makes the DP table astronomically large, even though W is encoded in just ~100 bits"
    - "Yes — the algorithm is polynomial and 2^{100} is a specific finite number"
    - "No — but only because dynamic programming cannot solve NP-hard problems in general"
  answer: 1
  explanation: "The O(nW) runtime is polynomial in the numerical value W, but W = 2^{100} is encoded in only ~100 bits of input. The DP table has n × W = 50 × 2^{100} entries — vastly more than atoms in the observable universe. The algorithm is exponential in the bit-length of the input, which is the standard measure of input size. This is the definition of pseudo-polynomial: tractable when W is small as a number, but exponential when W is large (as it can be even when its binary encoding is short). Option A confuses n (number of items) with the total running time. Option C confuses 'finite' with 'feasible' and conflates numerical value with input size."

- question: "What is the crucial distinction between 'polynomial in the numerical value of the input' and 'polynomial in the input size (bit-length)'?"
  type: multiple-choice
  options:
    - "They are equivalent — the numerical value and bit-length of an integer are always proportional"
    - "The bit-length of a number W is log₂W, so an algorithm running in O(W) time is O(2^{bit-length(W)}) — exponential in input size"
    - "Input size counts only the number of items n, not the capacity W, so W is not part of the input"
    - "The distinction only matters for problems with real-valued inputs, not integer problems"
  answer: 1
  explanation: "An integer W requires ⌈log₂W⌉ bits to encode. An O(W) algorithm therefore runs in O(2^b) time where b = log₂W is the bit-length of the capacity. As W grows, b grows logarithmically, but the algorithm's runtime grows exponentially in b. This is the formal definition of pseudo-polynomial: the running time is polynomial when expressed as a function of the numerical input values, but exponential when expressed as a function of the input's binary representation length. Option A is the misconception: numerical value and bit-length differ exponentially. Option C is wrong: W is explicitly part of the problem input and must be accounted for in complexity analysis."

- question: "The 0/1 knapsack problem is weakly NP-hard, meaning there exists an algorithm that solves it in polynomial time when the item weights are bounded by a polynomial in the number of items n."
  type: true-false
  answer: true
  explanation: "Weak NP-hardness means the problem is NP-hard in general, but becomes tractable when the numeric parameters are bounded. For knapsack, if W = O(n^k) for some constant k, then the O(nW) DP algorithm runs in O(n^{k+1}) time — genuinely polynomial. More strongly, knapsack admits an FPTAS: by rounding item values to nearby multiples, you can construct a (1+ε)-approximation in polynomial time in both n and 1/ε. This is possible precisely because of the weak NP-hardness structure. Strongly NP-hard problems like 3-SAT have no numeric parameter to exploit in this way — there is no pseudo-polynomial shortcut and typically no FPTAS."

- question: "An O(nW) algorithm for the knapsack problem proves that knapsack is not NP-hard, since it can be solved in polynomial time."
  type: true-false
  answer: false
  explanation: "This is the core misconception about pseudo-polynomial algorithms. The O(nW) algorithm is polynomial in the numerical value of W but exponential in the bit-length of W, which is the correct measure of input size in complexity theory. Knapsack remains NP-hard because polynomial time is defined relative to input length (bit-length), not numerical magnitude. The existence of a pseudo-polynomial algorithm proves knapsack is weakly NP-hard — it has a special numeric structure that can be exploited when values are small — but does not resolve NP-hardness. If this argument were valid, it would also 'prove' that factoring large integers is easy, since you can check divisors up to √N in O(√N) time."

- question: "Why is the O(nW) knapsack dynamic programming algorithm called 'pseudo-polynomial' rather than 'polynomial,' even though nW is written as a product of two input quantities?"
  type: short-answer
  answer: "Polynomial time complexity is measured in the bit-length of the input, not the numerical value of input parameters. The capacity W is a number that can be as large as 2^b where b is the number of bits used to encode W. An O(nW) algorithm therefore runs in O(n · 2^b) time in the worst case — exponential in the bit-length b of the capacity. By contrast, a polynomial-time algorithm must run in time bounded by a polynomial in the total input size, which includes n items each described by weight and value (O(n log W) bits total). Since W can be exponentially large relative to its encoding, nW is not polynomial in the input size. The algorithm is 'pseudo-polynomial' because it is polynomial only when the numerical value of W is small — a condition that is not guaranteed and can be easily violated."
  explanation: "The answer should articulate the gap between 'polynomial in the numerical value' and 'polynomial in the bit-length.' A complete answer references that W requires log₂W bits to encode, so O(W) = O(2^{log W}) is exponential in the bit-length. Students who say 'it's pseudo-polynomial because W could be large' are partially right but haven't explained why 'large W' corresponds to 'exponential in input size.'"
```

## Explainer

The 0/1 knapsack problem asks: given n items each with a weight and a value, and a capacity W, which items should you pack to maximize value without exceeding the capacity? You already know this is NP-hard. But it behaves differently from problems like graph 3-coloring or SAT in a subtle and instructive way: it has a dynamic programming solution that appears — but isn't quite — polynomial.

The DP algorithm builds a table where entry (i, w) stores the maximum value achievable using the first i items with weight budget w. Filling this table takes O(nW) time. For small W — say, items with weights in the hundreds — this is perfectly practical. The confusion arises because complexity is measured in the **bit-length** of the input, not the numerical value of the numbers. W can be encoded in log₂W bits, meaning that if W = 2^{100}, the input is only about 100 bits long but the DP table has 2^{100} entries. The algorithm's running time is exponential in the input size. This is what **pseudo-polynomial time** means: polynomial in the numerical value of the input, but potentially exponential in the bit-length.

This distinction separates **weakly NP-hard** problems from **strongly NP-hard** ones. Knapsack is weakly NP-hard: hard in general, but tractable when input values are bounded by a polynomial in n. By contrast, 3-SAT is strongly NP-hard — no pseudo-polynomial shortcut exists because the problem has no natural numeric parameter to exploit. The significance for approximation is that weakly NP-hard problems often admit an FPTAS. For knapsack, you can round the item values to nearby multiples, making W effectively small enough for the DP to run in polynomial time in both n and 1/ε — giving a (1+ε)-approximation for any ε > 0 at polynomial cost.

The knapsack problem is also a useful lens on the relationship between DP and NP-hardness more generally. Dynamic programming solves many optimization problems efficiently by exploiting **optimal substructure** — the property that the optimal solution to the whole problem can be built from optimal solutions to subproblems. For knapsack, this structure exists, but the state space (the table size) depends on the input values rather than just their count. When the values are bounded, the DP is fast. When they are unbounded, the DP is exponential, and we are back to the NP-hard baseline. The lesson: DP does not bypass NP-hardness; it works within it when the problem's numeric structure allows.
