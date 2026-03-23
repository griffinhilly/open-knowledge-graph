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
stage: formal-systems
status: validated
---

# Formal Models of Computation: Turing Machines and Lambda Calculus

## Core Idea
Turing machines and the lambda calculus are formal models that formalize the intuitive notion of 'algorithm' and 'computable function'. The Church-Turing thesis asserts that these models, despite superficial differences, capture exactly the same class of computable functions—those computable by any reasonable mechanical process.

## How It's Best Learned
Study Turing machines and lambda calculus in parallel; show explicit translations between them. Implement a simple Turing machine simulator to build intuition.

## Common Misconceptions
- Assuming Turing completeness means all Turing-complete systems solve the same problems equally fast. They compute the same functions, not with the same complexity.
- Overlooking that Church-Turing thesis is not a theorem; it's a conjecture about what 'computable' means.

## Questions

```yaml
- question: "A function f is known to be computable by a Turing machine in 100 steps. Which of the following is guaranteed about computing f using an equivalent lambda calculus term?"
  type: multiple-choice
  options:
    - "It will also require exactly 100 beta-reductions, since both models are equivalent"
    - "It will require at most 100 beta-reductions, since equivalent models are equally efficient"
    - "It will correctly compute f, but the number of beta-reductions may be exponentially larger or smaller — equivalence is about computability, not complexity"
    - "The lambda calculus cannot simulate this Turing machine because it lacks a tape mechanism"
  answer: 2
  explanation: "The Church-Turing equivalence guarantees that both models compute the same class of functions — whatever a Turing machine computes, a lambda calculus term computes. But equivalence in computational power says nothing about efficiency. A 100-step Turing machine computation might require thousands of beta-reductions to simulate, or vice versa. Complexity (how long it takes) is a separate question from computability (whether it terminates with the right answer)."

- question: "Which statement correctly characterizes the relationship between Turing machines and the lambda calculus?"
  type: multiple-choice
  options:
    - "They are equivalent in the functions they can compute, but this equivalence is a proven mathematical theorem with no remaining uncertainty"
    - "The lambda calculus can compute a strict superset of Turing-computable functions, since it handles higher-order functions that Turing machines cannot"
    - "They compute exactly the same class of functions; the Church-Turing thesis asserts this coincidence reflects the true boundary of mechanical computation, though this claim is a conjecture rather than a theorem"
    - "Turing machines are strictly more powerful because they have an infinite tape, while lambda calculus terms are finite expressions"
  answer: 2
  explanation: "Every lambda calculus term can be simulated by a Turing machine (mechanically apply reduction rules), and every Turing machine can be encoded in the lambda calculus (represent tape and state as data). This proves both directions of the equivalence. However, the broader claim — that these models capture *all* mechanical computation — is the Church-Turing *thesis*, a philosophical conjecture about what 'computable' means, not a formal theorem. No one has proved it or refuted it, because 'mechanical computation' has no prior formal definition to prove it against."

- question: "The Church-Turing thesis is a proven mathematical theorem establishing that Turing machines compute all and only the computable functions."
  type: true-false
  answer: false
  explanation: "The Church-Turing thesis is a conjecture, not a theorem. It asserts that any function computable by a 'reasonable mechanical process' is computable by a Turing machine — but 'reasonable mechanical process' has no prior formal definition, so there is nothing to prove the thesis against in a strict logical sense. The equivalence between specific formal models (Turing machines, lambda calculus, recursive functions) is proven. The broader claim that these models capture all of computation is an empirical observation and philosophical commitment, not a mathematical derivation."

- question: "If two computational models are Turing-equivalent, they will solve any given problem with the same number of computational steps."
  type: true-false
  answer: false
  explanation: "Turing equivalence means the models compute the same class of functions — both halt on the same inputs and produce the same outputs. It says nothing about efficiency. A Turing machine might solve a problem in polynomial time while an equivalent lambda calculus simulation requires exponential beta-reductions, or vice versa. This is why complexity theory studies specific machine models carefully: different Turing machine variants (deterministic, nondeterministic, multi-tape) can define different complexity classes even though they all compute the same functions."

- question: "What does it mean for two computational models to be 'equivalent,' and what does equivalence explicitly NOT imply?"
  type: short-answer
  answer: "Two models are computationally equivalent if they compute exactly the same class of functions: for every function one can compute (halting with the correct output on all valid inputs), the other can compute it too. Equivalence does NOT imply equal efficiency — the same function may require very different numbers of steps in each model. It also does not imply that programs in one model are easily translated into the other in a practical sense, only that a translation exists in principle."
  explanation: "The distinction between 'what can be computed' and 'how efficiently it can be computed' is foundational in theoretical CS. Computability theory (can it be done at all?) and complexity theory (how much resource does it take?) are separate disciplines. The Church-Turing equivalence results belong to computability; they say nothing about polynomial vs. exponential time, which is the domain of complexity classes like P, NP, and PSPACE."
```

## Explainer

Your prerequisite on the Church-Turing thesis established the central claim: any function computable by a "reasonable mechanical process" is computable by a Turing machine. But what exactly is a Turing machine? And why should a completely different formalism — the lambda calculus — compute the same class of functions? Understanding both models concretely, and then seeing why they coincide, is the core payoff of this topic.

A **Turing machine** is an idealized device with three components: an infinite tape of cells (each holding a symbol from a finite alphabet), a read/write head that can move left or right one cell at a time, and a finite set of states with a transition table. At each step, the machine reads the current cell, consults its transition table to determine the next state, the symbol to write, and which direction to move the head. The machine halts when it enters a designated accepting or rejecting state. This is spare, mechanical, and concrete — you can simulate it on paper. The entire computational history of the machine is visible in the tape, the head position, and the current state. From your set-theoretic background, note that a Turing machine is formally just a tuple (Q, Σ, δ, q₀, F) where Q is a finite set of states, Σ is an alphabet, δ: Q × Σ → Q × Σ × {L,R} is the transition function, q₀ is the initial state, and F ⊆ Q is the accepting states.

The **lambda calculus** reaches the same computational universe from a completely different angle. Instead of states and tapes, everything is a function. There are only three constructs: **variables** (x), **abstractions** (λx.e, defining a function), and **applications** (e₁ e₂, applying a function to an argument). Computation proceeds by **β-reduction**: (λx.e) v reduces to e[v/x], substituting v for x in the body. Even numbers and booleans must be encoded as functions (Church encodings), which initially feels absurd but turns out to be entirely workable. The Church encoding of the number 2 is λf.λx.f(f(x)) — the function that applies f twice to x. All arithmetic, conditionals, and even recursion can be built from these three primitives alone.

What makes their equivalence surprising is that the two models look nothing alike. Turing machines are imperative: they modify state step by step. Lambda calculus is functional: it rewrites expressions by substitution. Yet every lambda calculus term can be simulated by a Turing machine (mechanically rewrite the term according to reduction rules), and every Turing machine can be encoded in the lambda calculus (represent the tape, head, and state as a data structure and iterate). The equivalence is not a coincidence — it reflects the Church-Turing thesis, which you already know is a philosophical claim rather than a theorem. No one has yet found a naturally arising computational model that computes more functions than either.

An important caution follows from the common misconception: equivalent computability does not mean equivalent complexity. A problem solvable in 10 steps on a Turing machine may require exponentially many beta-reductions in the lambda calculus, and vice versa. The class of **computable functions** — those with a halting computation — is the same for both models. But when you ask how efficiently a function can be computed, the choice of model matters enormously, and different Turing machine variants (deterministic, nondeterministic, multi-tape) define complexity classes that may differ. The models are equivalent in power, not in speed.

