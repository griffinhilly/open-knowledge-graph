---
id: complexity-class-p-definition
title: 'Complexity Class P: Polynomial Time'
domain: computer-science
course: theory-of-computation
prerequisites:
- id: p-vs-np-problem
  type: hard
- id: time-complexity-classes
  type: soft
- id: asymptotic-notation-big-o-omega-theta
  type: soft
builds-toward:
- complexity-class-np-definition
tags:
- p-class
- polynomial-time
- tractable
- efficient
- definition
stage: advanced
status: draft
---

# Complexity Class P: Polynomial Time

## Core Idea
The class P contains languages decided by deterministic TMs in polynomial time. P represents problems solvable efficiently in theory (sorting, shortest paths, primality testing). P is robust: all standard polynomial-time models (RAM, circuits, multi-tape TMs) agree on P due to polynomial equivalence. P is widely believed tractable; whether P = NP is the central open problem in CS.

## Explainer

From your study of time complexity and Big-O notation, you know how to measure the growth rate of an algorithm's running time as a function of input size. **The complexity class P** draws a line in the sand: it contains exactly those decision problems (yes/no questions) that can be solved by a deterministic Turing machine in time bounded by some polynomial function of the input length. If the input has n bits, a problem is in P if there exists an algorithm that always halts with the correct answer in at most n^k steps for some fixed constant k — whether that is n², n³, or n^100.

The polynomial boundary is not chosen because polynomial-time algorithms are always fast in practice. An algorithm running in n^50 time is technically in P but completely impractical. The significance of P is **theoretical robustness**. Every reasonable model of deterministic computation — single-tape Turing machines, multi-tape machines, random-access machines, Boolean circuits — agrees on which problems are polynomial-time solvable. Switching between these models may square or cube the running time, but a polynomial of a polynomial is still a polynomial. This means P is not an artifact of one particular machine model; it captures something fundamental about what is efficiently computable.

Concrete problems in P anchor the abstraction. Sorting an array of n elements takes O(n log n) time — solidly polynomial. Finding the shortest path in a graph with n nodes and m edges takes O(n² ) or O(m + n log n) depending on the algorithm. Testing whether a number with n digits is prime was proved to be in P by the AKS algorithm in 2002, settling a long-standing question. Linear programming, matching in bipartite graphs, and determining whether two strings are anagrams are all in P. What unites them is the existence of a step-by-step procedure that systematically reaches the answer without needing to guess or explore exponentially many possibilities.

The importance of P becomes clear when contrasted with problems that appear to resist polynomial-time solution. Many natural problems — scheduling, graph coloring, Boolean satisfiability — seem to require brute-force search over exponentially many candidates. These problems sit in the class NP, where solutions can be *verified* quickly but (as far as anyone knows) not *found* quickly. Whether P equals NP — whether every problem whose solution can be checked in polynomial time can also be *solved* in polynomial time — is the most important open question in theoretical computer science. If P = NP, the distinction between finding and verifying would collapse, with profound consequences for cryptography, optimization, and mathematics itself.
