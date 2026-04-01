---
id: separation-logic
title: Separation Logic
domain: computer-science
course: formal-methods
prerequisites:
- id: hoare-logic
  type: hard
- id: predicate-logic-introduction
  type: hard
- id: frame-problem-verification
  type: soft
builds-toward:
- concurrency-verification
tags:
- separating-conjunction
- heap-reasoning
- frame-rule
- local-reasoning
- memory-safety
stage: expert
status: validated
---
# Separation Logic

## Core Idea
Separation logic extends Hoare logic with spatial connectives for reasoning about programs that manipulate heap memory. Its central operator, the separating conjunction P * Q, asserts that the heap can be split into two disjoint parts, one satisfying P and the other satisfying Q. This enables local reasoning: a specification for a function describes only the heap fragment the function touches, and the frame rule automatically extends this to any larger heap. Separation logic makes it practical to verify pointer-manipulating programs — linked lists, trees, graphs — that are intractable in standard Hoare logic.

## Questions

```yaml
- question: "What does the separating conjunction P * Q assert about the heap?"
  type: multiple-choice
  options:
    - "P and Q both hold for the entire heap"
    - "The heap can be divided into two disjoint regions, one satisfying P and the other satisfying Q"
    - "Either P or Q holds for the heap, but not both"
    - "P holds for the heap and Q holds for the stack"
  answer: 1
  explanation: "The separating conjunction P * Q requires the heap to split into two parts with NO shared cells — one part satisfies P, the other satisfies Q. This disjointness is what distinguishes it from ordinary conjunction (P and Q, which says both hold for the same heap) and enables reasoning about ownership and aliasing. If x points to 5 in one part and y points to 7 in the other, the * guarantees x and y are different addresses."

- question: "The frame rule in separation logic states: if {P} C {Q} then {P * R} C {Q * R}, provided C does not modify variables free in R. Why is this rule central to scalability?"
  type: short-answer
  answer: "The frame rule enables local reasoning: you prove a specification for C that mentions only the heap cells C actually accesses (the footprint). The frame R represents the rest of the heap, which is automatically preserved. This means you can verify each function in isolation against its small footprint, then compose proofs without re-verifying the entire heap — making verification modular and scalable to large programs."
  explanation: "Without the frame rule, every specification would need to describe the entire heap, and adding a new data structure would require re-proving every existing function. The frame rule's guarantee that untouched heap is preserved is what makes separation logic practical for real codebases. Tools like Facebook's Infer use this principle to analyze millions of lines of code by reasoning locally about each function."

- question: "Standard Hoare logic cannot easily handle pointer aliasing (two variables pointing to the same memory cell). How does separation logic address this?"
  type: short-answer
  answer: "The separating conjunction x -> v * y -> w inherently asserts that x and y point to different cells (disjoint heap regions). This makes non-aliasing the default in separation logic specifications. When aliasing IS intended, it must be expressed explicitly, typically by using a single points-to assertion x -> v and noting that y = x. This reversal of defaults — non-aliasing unless stated otherwise — eliminates the combinatorial explosion of aliasing cases that plagues standard Hoare logic."
  explanation: "In standard Hoare logic, if you have two pointers x and y, you must consider whether they alias (point to the same cell) or not, and proofs branch on every such possibility. With n pointers, this creates 2^(n choose 2) cases. Separation logic's * operator makes disjointness structural: x -> v * y -> w cannot be satisfied if x = y because the heap regions must be disjoint. This eliminates aliasing cases from proofs entirely unless aliasing is explicitly introduced."
```

## Explainer

Standard Hoare logic works well for programs that manipulate simple variables, but it struggles with heap-manipulating programs. The root problem is **aliasing**: when two pointers might refer to the same memory cell, modifying one might silently modify the other. In standard logic, you must track all possible aliasing relationships, leading to a combinatorial explosion. **Separation logic**, introduced by John Reynolds and Peter O'Hearn around 2000, solves this with a new logical connective designed specifically for heap reasoning.

The key innovation is the **separating conjunction**, written P * Q. It asserts that the current heap can be partitioned into two **disjoint** sub-heaps, one satisfying P and the other satisfying Q. The points-to predicate x -> v says that address x holds value v and nothing else is in the heap (it describes a single-cell heap). So x -> 5 * y -> 7 means x points to 5, y points to 7, and crucially x != y because the heaps are disjoint. Non-aliasing is baked into the logic's structure rather than stated as a side condition.

The most powerful consequence is the **frame rule**: if {P} C {Q} holds, then {P * R} C {Q * R} holds for any frame R whose free variables are not modified by C. This enables **local reasoning** — you write a specification mentioning only the heap cells the function actually touches (its "footprint"), and the frame rule automatically extends correctness to any larger heap. A linked-list reversal function only needs to specify the list it reverses; the frame rule guarantees it leaves all other heap data untouched. This modularity is what makes separation logic scale to large programs: you verify each component against its small footprint and compose the results.

Separation logic has had enormous practical impact. **Facebook's Infer** (now Meta's) analyzes millions of lines of C, C++, Java, and Objective-C code using a separation logic engine, automatically finding memory safety bugs like null dereferences, use-after-free, and resource leaks. **Concurrent separation logic** extends the framework to multi-threaded programs by treating the separating conjunction as an ownership discipline: if thread A owns heap region P and thread B owns region Q, and P * Q holds, the threads cannot interfere because they operate on disjoint memory. This insight connects separation logic to type-theoretic notions of ownership, as seen in Rust's borrow checker, which enforces similar discipline at the type level.

The practical workflow mirrors Floyd-Hoare verification but with spatial assertions. The programmer annotates functions with pre/postconditions expressed in separation logic (describing the shape of heap structures — "this is a linked list from x to null," "this is a binary tree rooted at t"). Verification tools compute VCs using these spatial specifications, and specialized solvers discharge them. Finding the right spatial invariants for data structures — describing their heap layout inductively — is the main challenge, analogous to finding loop invariants in standard Hoare logic but richer because the invariants describe heap shapes rather than arithmetic relationships.
