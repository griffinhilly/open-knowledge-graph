---
id: time-complexity-p-class
title: Time Complexity and the P Class
domain: computer-science
course: theory-of-computation
prerequisites:
- id: rice-theorem
  type: soft
- id: church-turing-thesis
  type: hard
builds-toward:
- nondeterministic-polynomial-time
- np-completeness
tags:
- time-complexity
- p-class
- polynomial
stage: abstract-reasoning
status: draft
---

# Time Complexity and the P Class

## Core Idea
The complexity class P consists of languages decidable by a deterministic Turing machine in polynomial time. Problems in P have efficient algorithmic solutions. P is considered the class of 'practically solvable' problems, though it includes problems solvable in quadratic, cubic, or higher polynomial time.

## Explainer

Up to this point, computability theory has asked a binary question: *can* a problem be solved by a Turing machine at all? The class P shifts the question to: *how fast* can it be solved? From the Church-Turing thesis, you know that Turing machines capture the full power of computation. **Time complexity** measures how many steps a Turing machine uses as a function of input length, and the class **P** collects all decision problems solvable in polynomial time — meaning the number of steps is bounded by some polynomial n^k in the input size n.

Why polynomial time? The choice is not arbitrary. Polynomial-time algorithms scale manageably: if the input doubles in size, an O(n²) algorithm takes about four times as long, and an O(n³) algorithm takes about eight times as long. Exponential-time algorithms, by contrast, can become unusable even for moderate inputs — an O(2ⁿ) algorithm on an input of size 100 requires more steps than there are atoms in the observable universe. The polynomial/exponential divide turns out to be remarkably robust: it is preserved across all reasonable models of computation (multi-tape TMs, RAMs, etc.), a property known as the **extended Church-Turing thesis**. A problem solvable in polynomial time on one reasonable model is solvable in polynomial time on any other.

Familiar problems in P include sorting a list (O(n log n)), searching a sorted array (O(log n)), finding shortest paths in a graph (Dijkstra's algorithm, O(n² ) or better), determining whether a number is prime (the AKS algorithm, polynomial in the number of digits), and solving systems of linear equations (Gaussian elimination, O(n³)). These problems span different domains but share the property that their running time grows at a manageable rate. P is defined using Turing machines and worst-case analysis, but in practice, a problem being in P is strong evidence that it admits practical algorithms.

P serves as the foundation for the entire landscape of complexity theory. It is the baseline against which harder classes are defined. NP, which you'll study next, asks what happens when you allow nondeterminism — when the machine can "guess" a solution and then verify it in polynomial time. The question of whether P equals NP is really asking whether the power to verify solutions efficiently is the same as the power to find them efficiently. Every subsequent complexity class you encounter — NP, coNP, PSPACE, EXP — is defined in relation to P, making it the central reference point of computational complexity.
