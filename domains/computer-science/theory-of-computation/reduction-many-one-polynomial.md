---
id: reduction-many-one-polynomial
title: Polynomial Many-One Reductions
domain: computer-science
course: theory-of-computation
prerequisites:
- id: np-completeness
  type: hard
- id: boolean-satisfiability-and-reductions
  type: hard
tags:
- reductions
- hardness
- complexity-classes
stage: advanced
status: validated
---

# Polynomial Many-One Reductions

## Core Idea
A polynomial many-one reduction from L₁ to L₂ is a polynomial-time computable function f where x ∈ L₁ ⟺ f(x) ∈ L₂, formalizing 'problem L₁ is no harder than L₂.' If L₂ is polynomial-solvable and L₁ reduces to L₂, then L₁ is solvable in polynomial time. NP-completeness is defined via such reductions: a problem is NP-complete if in NP and all NP problems reduce to it. Reductions form the backbone of complexity theory, transferring difficulty between problems.

## Questions

```yaml
- question: "A researcher proves that problem A polynomial-time many-one reduces to problem B. Which conclusion is valid?"
  type: multiple-choice
  options:
    - "If A is in P, then B is in P"
    - "If B is in P, then A is in P"
    - "If A is NP-complete, then B is also NP-complete"
    - "Both A and B must be in NP"
  answer: 1
  explanation: "A reduces to B means: given any instance of A, we can transform it into an instance of B in polynomial time, preserving yes/no answers. Therefore, if B has an efficient solver, we can solve A efficiently: apply the reduction function, then call B's solver. So B in P implies A in P. Option A is backwards — A being easy tells us nothing about B. Option C is close but incomplete: if A is NP-hard and A reduces to B, then B is NP-hard; but NP-completeness also requires B to be in NP, which isn't implied by the reduction alone."

- question: "To prove that INDEPENDENT SET is NP-hard, a researcher performs a reduction. What is the correct direction, and what does a successful reduction prove?"
  type: multiple-choice
  options:
    - "INDEPENDENT SET reduces to 3-SAT (a known NP-complete problem), proving INDEPENDENT SET is in P"
    - "3-SAT reduces to INDEPENDENT SET, proving that if INDEPENDENT SET could be solved efficiently, 3-SAT could too — so INDEPENDENT SET is at least as hard as 3-SAT"
    - "3-SAT reduces to INDEPENDENT SET, proving that 3-SAT is NP-hard because INDEPENDENT SET is already a hard problem"
    - "The direction does not matter; a reduction between any two problems proves they are equally hard"
  answer: 1
  explanation: "To prove B (INDEPENDENT SET) is NP-hard, you reduce a known NP-hard problem A (3-SAT) TO B. The logic: if there were an efficient algorithm for B, the reduction would give an efficient algorithm for A, contradicting A's NP-hardness. Therefore B must be hard too. Reducing in the other direction (B to A) would only prove A is at least as hard as B, which we already knew. Option D is a common misconception: direction matters critically. 'A reduces to B' and 'B reduces to A' have completely different implications."

- question: "If problem A polynomial-time reduces to problem B, then A is harder than B."
  type: true-false
  answer: false
  explanation: "The reduction shows A is *no harder than* B — not that A is harder. If A reduces to B, it means B is at least as capable as A: any efficient solver for B can solve A via the reduction. B is the 'harder' one (at least as hard as A). The confusion is common because reductions feel like they put A 'on top of' B, but the hardness flows the other way: the target of the reduction (B) is the one that must be powerful enough to handle the source (A)."

- question: "The 'many-one' in polynomial many-one reduction means the reduction function f should map different instances of A to different instances of B (i.e., f should be injective)."
  type: true-false
  answer: false
  explanation: "'Many-one' means the opposite: multiple different inputs to A can map to the same input for B — f need not be injective, and often isn't. The 'many-to-one' mapping is what gives the name. The only requirements are that f is polynomial-time computable and that x ∈ A ⟺ f(x) ∈ B. The function can collapse many distinct A-instances to the same B-instance. Bijectivity (one-to-one and onto) would be a Turing reduction or an isomorphism, which is a strictly stronger notion than many-one reduction."

- question: "Explain why it matters that the reduction function f in a polynomial many-one reduction runs in polynomial time."
  type: short-answer
  answer: "The purpose of the reduction is to transfer complexity-theoretic hardness between problems. If an efficient solver for B exists and A reduces to B, the reduction gives an efficient algorithm for A: compute f(x) in polynomial time, then run B's solver in polynomial time, totaling polynomial time for A. If f took exponential time, this argument breaks down — the combined cost would be exponential regardless of B's efficiency, and the reduction would be useless for proving A is polynomially solvable. Similarly, if we are trying to prove B is NP-hard by reducing a known NP-hard problem A to B, an exponential-time f would not demonstrate that B is inherently hard — you could already solve A with brute force in that time. The polynomial bound on f is what makes the reduction meaningful as a hardness argument."
  explanation: "Polynomial time is the class boundary that complexity theory cares about. The reduction must preserve this boundary: transforming the question from 'is A hard?' to 'is B hard?' only works if the transformation itself is cheap (polynomial)."
```

## Explainer

You have already seen reductions used to prove NP-completeness, and you know how SAT reductions work in practice. A **polynomial many-one reduction** (also called a Karp reduction) is the precise formal tool underlying all of that work. The idea is deceptively simple: to reduce problem A to problem B, you build a polynomial-time function f that transforms every instance x of A into an instance f(x) of B, such that x is a yes-instance of A if and only if f(x) is a yes-instance of B. You never run B's solver — you just translate the question.

The "many-one" in the name means the function f maps inputs to outputs but need not be injective: many different inputs to A can map to the same input for B. The "polynomial" means f must be computable in polynomial time, ensuring the translation itself is efficient. This is critical because if f took exponential time to compute, the reduction would be useless for complexity classification — you would have already spent more time than a brute-force search.

The power of reductions flows in two directions. In the **easy direction**, if you know how to solve B efficiently and you can reduce A to B, then you can solve A efficiently: compute f(x) in polynomial time, then solve f(x) using B's algorithm in polynomial time. In the **hard direction** — and this is how reductions are most often used — if you know A is hard (say, NP-complete) and you can reduce A to B, then B must be at least as hard as A. If B were easy, you could solve A easily via the reduction, contradicting A's hardness. This is exactly how NP-completeness proofs work: you take a known NP-complete problem, reduce it to your target problem, and conclude the target is NP-hard.

A concrete example: to show that CLIQUE is NP-hard, you reduce 3-SAT to CLIQUE. Given a 3-SAT formula, you construct a graph where each literal in each clause becomes a vertex, edges connect compatible literals from different clauses, and the formula is satisfiable if and only if the graph contains a clique of size k (the number of clauses). The construction runs in polynomial time, the equivalence holds in both directions, and the reduction is complete. Notice that you never solve either problem — you just show that an efficient CLIQUE solver would imply an efficient 3-SAT solver, which would imply P = NP.
