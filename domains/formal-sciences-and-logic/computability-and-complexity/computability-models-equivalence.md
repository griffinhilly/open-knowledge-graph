---
id: computability-models-equivalence
title: Equivalence of Computational Models
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: church-turing-thesis-formal
  type: hard
- id: turing-machines-formal
  type: hard
- id: lambda-calculus
  type: hard
- id: equivalence-relations-and-equivalence-classes
  type: soft
builds-toward:
- turing-computable-vs-church-computable
- general-recursive-functions
tags:
- computability
- models-of-computation
- church-turing
stage: advanced
status: draft
---

# Equivalence of Computational Models

## Core Idea
Turing machines, lambda calculus, and mu-recursive functions all define the same class of computable functions. This foundational result—the Church-Turing thesis—establishes that no reasonable model of computation can compute anything beyond what Turing machines compute, making computability a robust, model-independent notion.

## How It's Best Learned
Compare the definitions of computation across at least two models (e.g., Turing machines and lambda calculus), then study a concrete encoding of one model into another.

## Common Misconceptions
- Thinking Church-Turing thesis is a proven theorem (it is a thesis about the limits of formal computation).
- Confusing the thesis with the claim that all algorithms can be fast (computability is about existence, not efficiency).

## Explainer

You already know what a Turing machine is: a finite-state controller reading and writing symbols on an infinite tape, moving one cell at a time. You also know lambda calculus: a system of anonymous functions that compute by substitution and reduction. These look nothing alike — one is a physical machine metaphor, the other is pure symbol manipulation. The central result of this topic is that they are nonetheless **computationally equivalent**: every function computable by one is computable by the other.

The equivalence proof works by translation. To show Turing machines and lambda calculus are equivalent, you need two directions: (1) every Turing machine computation can be simulated by a lambda expression, and (2) every lambda calculus computation can be simulated by a Turing machine. For direction (1), you encode the tape contents, head position, and machine state as a lambda term, then show that each machine step corresponds to a reduction step. For direction (2), you implement beta-reduction as a Turing machine algorithm. Neither direction is trivial, but both can be made explicit — which is what makes equivalence a theorem rather than a guess.

This same argument extends to **mu-recursive functions** (the class of functions built from zero, successor, projection, composition, primitive recursion, and minimization). They too compute exactly the same class. All three formalisms were proposed independently in the 1930s — Turing's machines in 1936, Church's lambda calculus in 1932–1936, Gödel and Kleene's recursive functions slightly later — and their equivalence was recognized almost immediately. This convergence is the empirical core of the **Church-Turing thesis**: any function that can be computed by an "effective procedure" — any finite, deterministic, mechanical process — can be computed by a Turing machine.

The Church-Turing thesis is not a theorem and cannot be proven from the formal definitions alone, because "effective procedure" is an informal intuitive concept, not a mathematical object. What the theorem establishes is that all the *formal* models we can write down agree. The thesis then asserts that our formal models have correctly captured the informal concept. This is a philosophical claim supported by overwhelming evidence — every new model of computation ever proposed has turned out to be equivalent — but it remains a thesis, not a proof. Critically, the equivalence result says nothing about *efficiency*: a function computable in O(n log n) on a RAM machine might require exponential time on a Turing machine due to the cost of simulating random access. Computability and complexity are separate questions.
