---
id: reductions-and-undecidability
title: Reductions and Proving Undecidability
domain: computer-science
course: theory-of-computation
prerequisites:
- id: undecidable-problems
  type: hard
builds-toward:
- rice-theorem
tags:
- reductions
- undecidability
- proof-technique
stage: advanced
status: draft
---

# Reductions and Proving Undecidability

## Core Idea
A many-to-one reduction from language A to language B shows that if B is decidable, then A is decidable. Contrapositive: if A is undecidable, then B is undecidable. Reductions allow proving undecidability of new problems without reconstructing diagonalization proofs.

## Questions

```yaml
- question: "A researcher wants to prove that the problem 'does Turing machine M accept all inputs?' is undecidable. She constructs a computable function mapping any ⟨M, w⟩ to a machine M' such that M' accepts all inputs if and only if M accepts w. If her construction is correct, what can she conclude?"
  type: multiple-choice
  options:
    - "The halting problem is actually decidable, since she connected it to a new problem"
    - "'M accepts all inputs' is decidable, because she found an algorithmic connection to A_TM"
    - "'M accepts all inputs' is undecidable, because a decider for it would yield a decider for A_TM"
    - "Nothing can be concluded — reductions only prove decidability, not undecidability"
  answer: 2
  explanation: "She has constructed a reduction from A_TM to the new problem. If the new problem ('M accepts all inputs') were decidable, she could decide A_TM: given ⟨M, w⟩, apply her function to get M', then run the decider for the new problem on M'. If it accepts, M accepts w; otherwise not. But A_TM is known to be undecidable — contradiction. Therefore the new problem must be undecidable."

- question: "What is the direction of reasoning in a reduction proof that establishes B is undecidable?"
  type: multiple-choice
  options:
    - "Reduce B to A_TM, showing that A_TM is at least as hard as B"
    - "Reduce A_TM to B, then use the contrapositive: if A_TM is undecidable and reduces to B, B must be undecidable"
    - "Show that A_TM can directly simulate any instance of B without reduction"
    - "Construct a new diagonalization argument specific to B's structure"
  answer: 1
  explanation: "The key direction is: reduce FROM A_TM TO B. This establishes that B is 'at least as hard' as A_TM. By contrapositive: if B were decidable, we could use the reduction to decide A_TM (run the reduction function, then the decider for B). Since A_TM is undecidable, B cannot be decidable either. Reducing B to A_TM goes the wrong direction — it would show A_TM is at least as hard as B, which says nothing useful about B's decidability."

- question: "If there is a computable reduction from language A to language B, and B is decidable, then A must also be decidable."
  type: true-false
  answer: true
  explanation: "This is the core logical fact that makes reductions useful. To decide A: take any input w, apply the reduction function f to get f(w), then run B's decider on f(w). Since w ∈ A if and only if f(w) ∈ B, and B's decider correctly determines whether f(w) ∈ B, the combined procedure correctly decides A. The reduction 'transfers' decidability from B back to A."

- question: "To prove that problem B is undecidable using a reduction, you construct a computable function from B to A_TM — that is, you reduce B to the halting problem."
  type: true-false
  answer: false
  explanation: "The direction is reversed. You reduce FROM A_TM TO B (not B to A_TM). Reducing A_TM to B shows that B is at least as hard as A_TM. If B were decidable, you could use the reduction to decide A_TM — a known impossibility. Reducing B to A_TM would only show that A_TM is at least as hard as B, which says nothing useful about whether B itself is decidable or not."

- question: "Why is the reduction technique more useful than constructing a fresh diagonalization argument for each new undecidable problem?"
  type: short-answer
  answer: "Diagonalization is a complex, one-off argument that must be rebuilt from scratch for each problem. A reduction instead leverages the established undecidability of A_TM: once you design a computable function f that maps A_TM instances to B instances, B's undecidability follows immediately without a new diagonal argument. Reductions are also composable — if A reduces to B and B reduces to C, then C is at least as hard as A — organizing all undecidable problems into a coherent hierarchy of relative difficulty."
  explanation: "Beyond efficiency, reductions provide structural insight. They show that many apparently different problems — 'does M halt?', 'does M accept all strings?', 'does M ever print a 1?' — share the same fundamental difficulty. This is more informative than isolated undecidability proofs. The same reduction concept, tightened to polynomial-time functions, later underpins NP-completeness, so mastering reductions here pays dividends throughout the theory of computation."
```

## Explainer

From your study of undecidable problems, you know that the halting problem (A_TM) cannot be decided by any Turing machine — the diagonalization proof established this directly. But there are infinitely many other undecidable problems, and you would not want to construct a fresh diagonalization argument for each one. **Reductions** provide a systematic way to transfer undecidability from a known undecidable problem to a new one, acting as a kind of proof-by-comparison.

A **many-to-one reduction** from language A to language B is a computable function f such that for every input w, w ∈ A if and only if f(w) ∈ B. Think of f as a translator: it converts instances of problem A into instances of problem B in a way that preserves yes/no answers. If such a reduction exists and B is decidable (has a Turing machine that always halts with the correct answer), then A is also decidable — you can decide A by first applying f, then running B's decider on the result. The contrapositive is the powerful direction: if A is *undecidable* and reduces to B, then B must also be undecidable. If B were decidable, A would be too, contradicting what we know.

The standard workflow is: take a problem B that you suspect is undecidable, then construct a computable function that maps instances of A_TM (the halting problem) into instances of B. For example, to show that the problem "does Turing machine M accept the empty string?" is undecidable, you build a reduction that takes a pair ⟨M, w⟩ and constructs a new machine M' that ignores its own input and instead simulates M on w. Now M' accepts the empty string if and only if M accepts w, so deciding the empty-string problem would let you decide the halting problem — a contradiction. The art of reduction proofs lies in designing this intermediate machine that bridges the two problems.

Reductions do more than prove individual undecidability results — they organize the landscape of unsolvable problems into a hierarchy of relative difficulty. If A reduces to B, then B is "at least as hard" as A. This framework extends throughout complexity theory: the same reduction concept, with tighter constraints on the function f (polynomial-time computable, log-space computable), underpins the theories of NP-completeness and space complexity that you will encounter later. Mastering reductions here gives you a proof technique that scales across the entire field.
