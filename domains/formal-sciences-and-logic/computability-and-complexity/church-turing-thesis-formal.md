---
id: church-turing-thesis-formal
title: The Church-Turing Thesis
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: turing-machines-formal
  type: hard
- id: lambda-calculus
  type: soft
- id: general-recursive-functions
  type: soft
- id: functions-and-function-properties
  type: soft
- id: recursion-on-finite-structures
  type: soft
- id: set-fundamentals
  type: soft
- id: mathematical-induction
  type: soft
- id: algorithm-analysis-big-o
  type: soft
- id: mu-recursive-functions
  type: soft
builds-toward:
- halting-problem-formal
- computability-reductions
tags:
- computability
- philosophy-of-computation
- models-of-computation
stage: advanced
status: validated
---

# The Church-Turing Thesis

## Core Idea
The Church-Turing thesis is the informal claim that every effectively computable function — any function a human could compute by following a definite mechanical procedure — is computable by a Turing machine. It is a thesis, not a theorem, because 'effectively computable' cannot be formally defined without circularity. The robustness of the thesis is supported by the fact that Turing machines, lambda calculus, recursive functions, register machines, and all other proposed models of computation have been proven to compute exactly the same class of functions.

## How It's Best Learned
Study the historical context: Church proposed lambda calculus, Turing proposed Turing machines, and Kleene proposed recursive functions, all independently in the 1930s, and they were shown equivalent. Then consider hypothetical counterexamples (hypercomputation, quantum computation) and why none have succeeded in surpassing the Church-Turing bound.

## Common Misconceptions
- The thesis does not claim every physically realizable process is Turing-computable — it specifically concerns idealized mechanical procedures.
- It is not provably false by definition; it is an empirical generalization subject to revision if a more powerful but still 'mechanical' model were discovered.

## Questions

```yaml
- question: "Why is the Church-Turing thesis called a 'thesis' rather than a 'theorem'?"
  type: multiple-choice
  options: ["It has been proven for all known models of computation but not for future ones", "The concept 'effectively computable' cannot be formally defined without circularity, so the claim cannot be formally proved", "Mathematicians informally agreed not to attempt a proof", "It was proposed before the formal definition of a Turing machine existed"]
  answer: 1
  explanation: "A theorem requires a precise formal statement. The thesis links Turing computability (formal) to 'effective computability' (informal — what a person can compute by following a definite procedure). Defining 'effective computability' precisely without essentially invoking Turing machines would be circular, making the thesis an empirical claim rather than a mathematical one."

- question: "The Church-Turing thesis implies that quantum computers can solve problems that Turing machines can seldom solve at most."
  type: true-false
  answer: false
  explanation: "Quantum computers can solve some problems *faster* (e.g., integer factorization), but they compute the same *class* of functions as Turing machines. Every function computable by a quantum computer is also computable by a Turing machine — just potentially much more slowly. The halting problem remains undecidable for quantum computers just as for classical ones. The thesis is about computability, not efficiency."

- question: "What is the primary empirical evidence that supports the Church-Turing thesis, even though it cannot be formally proved?"
  type: short-answer
  answer: "The convergence of independently invented models of computation — Turing machines, Church's lambda calculus, Kleene's general recursive functions, register machines, and others — all turned out to compute exactly the same class of functions, despite being motivated by completely different mathematical intuitions."
  explanation: "The robustness of this convergence across fully independent formalisms is strong evidence that the boundary of computability reflects something objective about mechanical procedure, not an artifact of any particular model. No model ever proposed that is intuitively 'mechanical' has been shown to compute strictly more than Turing machines."
```

## Explainer

By the time you study the Church-Turing thesis, you have already built Turing machines and seen how they simulate surprisingly complex computations. You might wonder: is there some other reasonable computational model that could do things Turing machines cannot? The Church-Turing thesis answers with a sweeping claim: no. Every function that any intuitively mechanical process can compute, a Turing machine can also compute.

The key word is 'intuitively.' The thesis links a precise mathematical object — the Turing machine — to the informal notion of an *effective procedure*: a computation a human could carry out with pencil and paper, following definite rules, with no creative leaps required. Because 'effective procedure' is informal, the thesis cannot be a theorem in the ordinary sense. You cannot formally prove that a precise object is equivalent to an informal concept without first formalizing that concept — but any formalization would essentially define 'effective procedure' as 'Turing-computable,' making the argument circular. This is precisely what makes it a *thesis* rather than a theorem.

What makes the thesis compelling is robustness. In the 1930s, Church, Turing, and Kleene each independently proposed their own models of computation — lambda calculus, Turing machines, and general recursive functions — motivated by entirely different mathematical intuitions. When compared, all three turned out to compute exactly the same functions. Register machines, word rewriting systems, cellular automata, and every other 'reasonable' model ever proposed have been proven equivalent. No one has ever found an 'intuitively mechanical' process that surpasses Turing computability.

A persistent misconception is that quantum computers refute the thesis. They do not, for a precise reason: quantum computers can solve some problems *faster*, but they cannot solve problems that are Turing-uncomputable. The halting problem is undecidable for quantum computers just as for classical ones. The Church-Turing thesis concerns the boundary between computable and uncomputable, not computational efficiency. There is a separate and more speculative 'physical Church-Turing thesis' about efficiency — but it is not the same claim.

The philosophical weight of the thesis is significant. It suggests that there is a single, natural boundary to computation — that the class of computable functions is a robust, objective mathematical entity rather than an artifact of any particular formalism. This is why results like the undecidability of the halting problem generalize confidently: when we prove that no Turing machine can solve the halting problem, we are effectively claiming that no mechanical procedure of any kind can solve it, because any such procedure would be Turing-equivalent.
