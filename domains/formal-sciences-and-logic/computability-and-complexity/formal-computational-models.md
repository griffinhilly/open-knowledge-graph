---
id: formal-computational-models
title: 'Formal Models of Computation: Turing Machines and Lambda Calculus'
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: church-turing-thesis-formal
  type: hard
- id: set-operations-and-notation
  type: soft
- id: set-fundamentals
  type: hard
- id: equivalence-relations-and-equivalence-classes
  type: soft
builds-toward:
- recursive-languages
- recursively-enumerable-languages
- turing-degrees-equivalence
tags:
- computation
- turing-machines
- lambda-calculus
- church-turing
stage: advanced
status: draft
---

# Formal Models of Computation: Turing Machines and Lambda Calculus

## Core Idea
Turing machines and the lambda calculus are formal models that formalize the intuitive notion of 'algorithm' and 'computable function'. The Church-Turing thesis asserts that these models, despite superficial differences, capture exactly the same class of computable functions—those computable by any reasonable mechanical process.

## How It's Best Learned
Study Turing machines and lambda calculus in parallel; show explicit translations between them. Implement a simple Turing machine simulator to build intuition.

## Common Misconceptions
- Assuming Turing completeness means all Turing-complete systems solve the same problems equally fast. They compute the same functions, not with the same complexity.
- Overlooking that Church-Turing thesis is not a theorem; it's a conjecture about what 'computable' means.

## Explainer

Your prerequisite on the Church-Turing thesis established the central claim: any function computable by a "reasonable mechanical process" is computable by a Turing machine. But what exactly is a Turing machine? And why should a completely different formalism — the lambda calculus — compute the same class of functions? Understanding both models concretely, and then seeing why they coincide, is the core payoff of this topic.

A **Turing machine** is an idealized device with three components: an infinite tape of cells (each holding a symbol from a finite alphabet), a read/write head that can move left or right one cell at a time, and a finite set of states with a transition table. At each step, the machine reads the current cell, consults its transition table to determine the next state, the symbol to write, and which direction to move the head. The machine halts when it enters a designated accepting or rejecting state. This is spare, mechanical, and concrete — you can simulate it on paper. The entire computational history of the machine is visible in the tape, the head position, and the current state. From your set-theoretic background, note that a Turing machine is formally just a tuple (Q, Σ, δ, q₀, F) where Q is a finite set of states, Σ is an alphabet, δ: Q × Σ → Q × Σ × {L,R} is the transition function, q₀ is the initial state, and F ⊆ Q is the accepting states.

The **lambda calculus** reaches the same computational universe from a completely different angle. Instead of states and tapes, everything is a function. There are only three constructs: **variables** (x), **abstractions** (λx.e, defining a function), and **applications** (e₁ e₂, applying a function to an argument). Computation proceeds by **β-reduction**: (λx.e) v reduces to e[v/x], substituting v for x in the body. Even numbers and booleans must be encoded as functions (Church encodings), which initially feels absurd but turns out to be entirely workable. The Church encoding of the number 2 is λf.λx.f(f(x)) — the function that applies f twice to x. All arithmetic, conditionals, and even recursion can be built from these three primitives alone.

What makes their equivalence surprising is that the two models look nothing alike. Turing machines are imperative: they modify state step by step. Lambda calculus is functional: it rewrites expressions by substitution. Yet every lambda calculus term can be simulated by a Turing machine (mechanically rewrite the term according to reduction rules), and every Turing machine can be encoded in the lambda calculus (represent the tape, head, and state as a data structure and iterate). The equivalence is not a coincidence — it reflects the Church-Turing thesis, which you already know is a philosophical claim rather than a theorem. No one has yet found a naturally arising computational model that computes more functions than either.

An important caution follows from the common misconception: equivalent computability does not mean equivalent complexity. A problem solvable in 10 steps on a Turing machine may require exponentially many beta-reductions in the lambda calculus, and vice versa. The class of **computable functions** — those with a halting computation — is the same for both models. But when you ask how efficiently a function can be computed, the choice of model matters enormously, and different Turing machine variants (deterministic, nondeterministic, multi-tape) define complexity classes that may differ. The models are equivalent in power, not in speed.

