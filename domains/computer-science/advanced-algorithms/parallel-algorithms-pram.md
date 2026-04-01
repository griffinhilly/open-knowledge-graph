---
id: parallel-algorithms-pram
title: Parallel Algorithms and the PRAM Model
domain: computer-science
course: advanced-algorithms
prerequisites:
- id: big-o-complexity-analysis
  type: hard
- id: divide-and-conquer-strategy
  type: hard
- id: merge-sort
  type: soft
- id: breadth-first-search
  type: soft
tags:
- parallel-algorithms
- pram
- work-depth
- nc-complexity
- brents-theorem
- parallel-prefix
stage: expert
status: validated
---

# Parallel Algorithms and the PRAM Model

## Core Idea
The PRAM (Parallel Random Access Machine) is the standard theoretical model for shared-memory parallel computation: p processors operate synchronously on a shared memory, executing one instruction per step. The key complexity measures are work (total operations across all processors) and depth (longest chain of sequential dependencies, also called span or parallel time). Brent's theorem connects these: any algorithm with work W and depth D can be executed on p processors in time O(W/p + D). The complexity class NC (Nick's Class) captures problems solvable in polylogarithmic depth with polynomial work -- the parallel analog of P. Classic results include O(log n)-depth parallel prefix sums, O(log^2 n)-depth sorting networks, and the striking fact that some problems in P appear to be inherently sequential (P-complete problems), admitting no significant parallel speedup.

## Questions

```yaml
- question: "An algorithm performs W = O(n) total work and has depth D = O(log n). Using Brent's theorem, what is the running time on p = n / log n processors?"
  type: multiple-choice
  options:
    - "O(n)"
    - "O(log n)"
    - "O(log^2 n)"
    - "O(n / log n)"
  answer: 1
  explanation: "Brent's theorem gives time O(W/p + D) = O(n / (n/log n) + log n) = O(log n + log n) = O(log n). This is optimal: with n/log n processors, we achieve O(log n) parallel time while keeping the total work O(n), which matches the sequential lower bound. The algorithm is said to be work-efficient because its total work equals the best sequential algorithm's running time. Work-efficiency is the gold standard in parallel algorithm design -- it means no computation is wasted."

- question: "The class NC contains exactly those problems solvable in O(log^k n) depth with O(n^c) total work for constants k and c. A problem that is P-complete under logspace reductions is in NC if and only if NC = P."
  type: true-false
  answer: true
  explanation: "P-complete problems are the hardest problems in P with respect to logspace (or NC) reductions. If any P-complete problem were in NC, then every problem in P would reduce to it in NC, placing all of P in NC. Since NC is contained in P (polylog depth with polynomial work implies polynomial sequential time), this would give NC = P. The canonical P-complete problem is the Circuit Value Problem (evaluating a given Boolean circuit on a given input). The widespread belief that NC != P means these problems are considered inherently sequential -- they resist efficient parallelization."

- question: "The parallel prefix (scan) operation computes all prefix sums of an array of n elements. What are its work and depth, and why is this operation fundamental to parallel algorithm design?"
  type: short-answer
  answer: "Parallel prefix computes all prefix sums (y_i = x_1 + x_2 + ... + x_i for i = 1..n) in O(n) work and O(log n) depth, matching the sequential lower bound for work while achieving exponential parallel speedup in depth. The operation generalizes beyond addition to any associative operator (max, min, AND, OR, concatenation). It is fundamental because a vast number of parallel algorithms reduce to prefix computation: parallel compaction (removing gaps from arrays), radix sort, carry-lookahead addition, tree computations, and load balancing. Parallel prefix is to parallel algorithms what divide-and-conquer is to sequential algorithms -- a universal building block."
  explanation: "The Blelloch up-sweep / down-sweep construction builds a balanced binary tree over the input. The up-sweep computes partial sums bottom-up (log n levels, n/2 + n/4 + ... = n-1 operations). The down-sweep propagates prefix sums top-down, again in log n levels with O(n) work. The construction is work-efficient (O(n) total work = sequential optimum) and achieves O(log n) depth. By Brent's theorem, this runs in O(n/p + log n) time on p processors."

- question: "PRAM models differ in how they handle concurrent memory access. The EREW (Exclusive Read Exclusive Write) model is strictly weaker than CRCW (Concurrent Read Concurrent Write) -- some problems require asymptotically more depth on EREW than CRCW."
  type: true-false
  answer: true
  explanation: "The CRCW PRAM can compute the OR of n bits in O(1) depth (all processors write 1 to a shared cell if their bit is 1, using priority or arbitrary write resolution). On the EREW PRAM, computing OR requires Omega(log n) depth because information from n inputs must be combined through a tree of exclusive operations. More precisely, any CRCW algorithm with depth D can be simulated on an EREW PRAM with depth O(D * log n), so the models differ by at most a logarithmic factor. This hierarchy (EREW subset CREW subset CRCW) parallels practical considerations: concurrent writes require more complex hardware or software coordination."

- question: "Why is work-efficiency considered more important than minimizing depth in practical parallel algorithm design?"
  type: short-answer
  answer: "A work-efficient algorithm (total work matching the best sequential algorithm) ensures that adding processors yields proportional speedup via Brent's theorem: time = O(W/p + D). If the work exceeds the sequential optimum by a factor c (work-inefficient), the algorithm wastes computation, and the parallel running time can never beat the sequential time by more than a factor of p/c regardless of depth. In practice, the number of processors p is finite, so the W/p term dominates for large inputs, making work-efficiency the primary determinant of real-world parallel performance. An algorithm with O(n log n) work and O(log n) depth is often worse in practice than one with O(n) work and O(log^2 n) depth when p is moderate."
  explanation: "This connects to Amdahl's Law and the broader principle that parallelism helps only when work is not wasted. The ideal parallel algorithm is simultaneously work-efficient (W equals sequential optimal) and has polylogarithmic depth. Some problems admit such algorithms (prefix sums, list ranking, connected components via Shiloach-Vishkin), while others seem to require a work-depth tradeoff."
```

## Explainer

Sequential algorithm analysis asks one question: how many steps does the algorithm take? Parallel algorithm analysis asks two: **work** (total operations, summed over all processors) and **depth** (the longest chain of dependent operations that must execute sequentially). These two measures capture fundamentally different aspects of an algorithm's parallelizability. An algorithm with small depth can exploit many processors simultaneously, while an algorithm with small work avoids wasting computation. The ideal is both: work matching the best sequential algorithm and polylogarithmic depth.

**Brent's theorem** bridges theory and practice by showing that any algorithm with work W and depth D can run on p processors in O(W/p + D) time. The W/p term represents the work distributed evenly among processors; the D term represents the inherent sequential bottleneck. When p is much smaller than W/D (the algorithm's parallelism), the running time is approximately W/p -- linear speedup. When p exceeds W/D, adding more processors does not help because the algorithm is depth-bound. This theorem justifies focusing on work-efficient algorithms (W equal to sequential optimal): they guarantee that any available parallelism translates to proportional speedup.

The **PRAM model** provides the theoretical framework. It assumes p processors sharing a common memory, operating in lockstep. PRAM variants differ in memory access rules: EREW (exclusive read, exclusive write) is the most restrictive and models real hardware most closely; CRCW (concurrent read, concurrent write) is the most permissive and simplifies algorithm design. The difference matters: computing the OR of n bits takes O(1) depth on CRCW (every processor with a 1-bit writes concurrently) but Omega(log n) on EREW. In general, CRCW can be simulated on EREW with a logarithmic slowdown, so the models are polynomially equivalent but the constant factors in depth differ.

The **parallel prefix** (scan) operation is the workhorse of PRAM algorithms. Given an array [x_1, ..., x_n] and an associative operator, it computes all prefixes [x_1, x_1 + x_2, ..., x_1 + ... + x_n] in O(n) work and O(log n) depth. This deceptively simple primitive underlies an enormous range of parallel algorithms: array compaction (removing marked elements while preserving order), load balancing, segmented operations, tree computations (Euler tour technique), and even sorting. Once you can do parallel prefix, many problems that seem inherently sequential yield to elegant parallel solutions.

The complexity class **NC** formalizes "efficiently parallelizable": problems solvable with polynomial work and polylogarithmic depth. NC is contained in P (polylog depth, polynomial work implies polynomial sequential time), but whether NC equals P is a major open question. **P-complete problems** -- like the Circuit Value Problem (evaluating a Boolean circuit) -- are the hardest problems in P for parallel computation: they are in NC only if NC = P. The existence of P-complete problems suggests that some polynomial-time computations are inherently sequential, resisting any significant parallel speedup. This parallels the NP-completeness story: just as NP-complete problems are believed to require superpolynomial sequential time, P-complete problems are believed to require polynomial (not polylogarithmic) parallel depth.
