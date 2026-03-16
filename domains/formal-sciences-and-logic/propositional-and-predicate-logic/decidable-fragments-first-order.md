---
id: decidable-fragments-first-order
title: Decidable Fragments of First-Order Logic
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: decidability-and-undecidability
  type: hard
- id: first-order-logic-syntax
  type: soft
tags:
- first-order-logic
- decidability
- computational-complexity
stage: formal-systems
status: draft
---

# Decidable Fragments of First-Order Logic

## Core Idea
While full first-order logic is undecidable, certain restricted fragments are decidable—for example, the Ackermann class (formulas with a special structure of quantifiers) and monadic first-order logic (predicates of at most one argument). Studying decidable fragments reveals what restrictions on expressive power are necessary to recover decidability.

## Explainer

You already know that full first-order logic is undecidable: the **Entscheidungsproblem** (decision problem for FOL) has no algorithmic solution, as Church and Turing proved in 1936. There is no algorithm that takes a first-order sentence as input and decides whether it is satisfiable. But this undecidability result applies to the *full* language — it doesn't mean every restricted subset is undecidable. Many practically important fragments turn out to be decidable, sometimes even efficiently so, and understanding which fragments cross the decidability line tells us where the logical "hard core" of undecidability actually lives.

The most natural restriction is on **quantifier prefix**. The quantifier-free fragment is trivially decidable (just evaluate propositional logic). The **monadic fragment** — where all predicates take only one argument — is decidable; Löwenheim proved this in 1915. With only unary predicates, you cannot express relational structure between objects (like "x is connected to y"), so the combinatorics stay manageable. The **Ackermann class** consists of formulas with prefix ∃*∀∃* (any number of existentials, one universal block, then existentials again) and no equality — these are decidable by reduction to finite satisfiability checking. The **Bernays-Schönfinkel class** (∃*∀*) is decidable and corresponds to existential second-order logic over finite structures in disguise; these sentences are satisfiable if and only if finitely satisfiable.

A key parameter is whether the fragment can *encode* computations. Undecidability enters when a fragment can simulate the behavior of a Turing machine — then satisfiability can encode the halting problem. Fragments that avoid relational structure, limit quantifier alternation, or restrict the way variables are reused often escape this trap. The **two-variable fragment** of FOL (with only two variable names, x and y, reused freely) is decidable (NEXPTIME-complete) — this is surprising, because two variables can still express substantial relational content. Adding a third variable restores undecidability. Similarly, **modal logic** is a decidable fragment of FOL: modal formulas translate to FOL formulas in a restricted form (the *standard translation*), and decidability of the modal logic corresponds to decidability of that FOL fragment.

The practical payoff is substantial: **description logics** (the formalism behind OWL ontologies), **temporal logic** (used in model checking), and many database query languages are all decidable because they correspond to decidable fragments of FOL. When you need automated reasoning over a formal language, the first question is: which fragment of FOL does this correspond to, and does that fragment fall on the decidable side of the line? Decidable fragments are not a curiosity — they are the logical backbone of automated verification, knowledge representation, and database theory.

