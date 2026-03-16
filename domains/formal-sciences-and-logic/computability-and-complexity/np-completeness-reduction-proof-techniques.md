---
id: np-completeness-reduction-proof-techniques
title: Reductions for Proving NP-Completeness
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: np-completeness-formal
  type: hard
- id: polynomial-time-reductions
  type: hard
builds-toward:
- approximation-hardness-results
tags:
- reductions
- NP-completeness
- proof-techniques
stage: advanced
status: draft
---

# Reductions for Proving NP-Completeness

## Core Idea
To prove a problem L is NP-complete, show L ∈ NP and reduce a known NP-complete problem to L in polynomial time. Standard reduction templates (clique to independent set, 3-SAT to Hamiltonian path) encode one computational structure into another, allowing hardness to propagate. This technique has identified thousands of NP-complete problems across computer science.

## Explainer

From your study of NP-completeness and polynomial-time reductions, you know that a reduction from problem A to problem B means: if you can solve B efficiently, you can solve A efficiently. Equivalently, if A is hard, then B is hard — hardness flows in the direction of the reduction arrow. This asymmetry is the engine of NP-completeness proofs, and understanding it precisely is the prerequisite for reading or constructing these proofs correctly.

The proof structure is always two steps. First, show that your target problem L belongs to NP — that is, given a proposed solution, you can verify it in polynomial time. For most combinatorial problems this is easy: a proposed graph coloring can be checked in linear time, a proposed Hamiltonian cycle can be verified by tracing the path, a proposed variable assignment can be checked by evaluating each clause. Second, pick a known NP-complete problem (the source) and give a **polynomial-time many-one reduction** from it to L. This reduction is a function f that transforms every instance x of the source problem into an instance f(x) of L, such that x is a YES-instance if and only if f(x) is a YES-instance. If you can build this function in polynomial time, then solving L would let you solve the source problem — so L must be at least as hard.

The art of reduction is choosing what to reduce *from*. 3-SAT is the most common source because its clause structure maps cleanly onto many combinatorial problems. The classic **3-SAT → Clique** reduction works like this: for a formula with k clauses, build a graph where each clause contributes three nodes (one per literal), and add an edge between two nodes from different clauses whenever their literals are non-contradictory (i.e., they could both be set true simultaneously). A satisfying assignment picks one true literal per clause, giving a k-clique; conversely, any k-clique identifies a consistent assignment satisfying all k clauses. The formula is satisfiable if and only if the graph has a k-clique.

What makes this technique powerful is that the reduction does *structural translation*: the combinatorial structure of clauses and literals maps directly onto the graph structure of nodes and edges. The best reductions are not arbitrary encodings — they reveal a genuine structural similarity between problems. When you see a new NP-completeness proof, ask: which feature of the source problem maps to which feature of the target? Once you see it clearly, the polynomial-time bound is usually straightforward, and the correctness argument follows from the structural correspondence. With practice, you begin to recognize reduction templates — partition-style reductions, gadget constructions, truth-setting variables — that recur across problems and can be adapted rather than invented from scratch.
