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
- id: variable-substitution-capture-avoidance
  type: soft
- id: quantifier-instantiation-rules
  type: soft
- id: resolution-fol
  type: soft
- id: semantic-tableaux-fol
  type: soft
tags:
- first-order-logic
- decidability
- computational-complexity
stage: advanced
status: validated
---
# Decidable Fragments of First-Order Logic

## Core Idea
While full first-order logic is undecidable, certain restricted fragments are decidable—for example, the Ackermann class (formulas with a special structure of quantifiers) and monadic first-order logic (predicates of at most one argument). Studying decidable fragments reveals what restrictions on expressive power are necessary to recover decidability.

## Questions

```yaml
- question: "First-order logic with only two variable names (x and y, reused freely) is decidable. What happens if you add a third variable name?"
  type: multiple-choice
  options:
    - "The three-variable fragment is still decidable, just harder — it becomes EXPTIME-complete instead of NEXPTIME-complete"
    - "Adding a third variable restores full FOL expressiveness and undecidability"
    - "The three-variable fragment is decidable but only for finite models"
    - "Three variables make the fragment decidable for satisfiability but undecidable for validity"
  answer: 1
  explanation: "The two-variable fragment (FO²) is decidable (NEXPTIME-complete) — a surprising result given that two variables can express substantial relational structure. But adding a third variable name (FO³) is enough to encode Turing machine computations, restoring undecidability. This illustrates how sharply the decidability boundary cuts: a single variable can tip a fragment from decidable to undecidable by enabling simulation of computation. The two-variable result is not a curiosity but the precise boundary of what the quantifier variable count alone can achieve."

- question: "Modal logic is decidable. What is the connection between modal logic's decidability and the theory of decidable fragments of first-order logic?"
  type: multiple-choice
  options:
    - "Modal logic is unrelated to FOL — its decidability comes from different proof-theoretic grounds"
    - "Modal logic translates into a restricted fragment of FOL via the standard translation, and decidability of modal logic corresponds to decidability of that FOL fragment"
    - "Modal logic is decidable only for propositional (zero-order) formulas, not when quantifiers are present"
    - "Modal logic's Kripke semantics is inherently finite, making all satisfiability problems trivially decidable"
  answer: 1
  explanation: "Modal logic has a standard translation into FOL: modal formulas become FOL formulas with two variables ranging over worlds, and accessibility becomes a binary predicate. The resulting FOL fragment falls within the decidable two-variable fragment (FO²). Modal logic's decidability is therefore a consequence of its being a syntactic restriction that corresponds to a known decidable FOL fragment. This connection explains why temporal logic and description logics — also expressible as FOL fragments — can be automated."

- question: "Monadic first-order logic — where all predicates take exactly one argument — is decidable."
  type: true-false
  answer: true
  explanation: "Löwenheim proved in 1915 that the monadic fragment of FOL is decidable. With only unary predicates, you can classify objects into categories (is-red(x), is-large(x)) but cannot express relational structure between objects (is-connected-to(x,y), is-parent-of(x,y)). This limits the combinatorial complexity enough that satisfiability remains decidable. The moment you introduce binary predicates, you can start encoding relational structure that enables computation simulation, and undecidability becomes possible."

- question: "Since full first-order logic is undecidable, all fragments of first-order logic obtained by restricting the set of allowed formulas are also undecidable."
  type: true-false
  answer: false
  explanation: "Undecidability of full FOL means there exists no algorithm for the full language — not that every restriction is also undecidable. Many practically important fragments are decidable: monadic FOL (Löwenheim, 1915), the Bernays-Schönfinkel class (∃*∀*), the Ackermann class (∃*∀∃*), the two-variable fragment, and propositional logic itself. Restricting predicate arity, quantifier prefix, or variable count can block the encoding of Turing machine computations, recovering decidability. The entire field of decidable fragments demonstrates that undecidability lives in specific logical features, not in FOL-style reasoning as such."

- question: "What determines whether a fragment of first-order logic is decidable or undecidable, and why does the ability to encode Turing machine computations matter?"
  type: short-answer
  answer: "A fragment of FOL is undecidable if it can simulate arbitrary Turing machine computations — because satisfiability of a formula in that fragment can then encode the halting problem, which has no algorithmic solution. Restrictions that prevent such simulation can recover decidability. Key restrictions include: limiting predicates to unary only (monadic fragment, no relational structure between objects), limiting quantifier alternation (∃*∀* prefix allows finite satisfiability checking), or limiting the number of variable names to two (FO²). When none of these restrictions block all computation-encoding paths, undecidability follows by reduction from the halting problem."
  explanation: "The core insight is that FOL's undecidability is not inherent to having quantifiers or predicates per se — it requires enough expressive power to write down a formula that is satisfiable if and only if a Turing machine halts. Fragments that lack binary predicates, restrict quantifier alternation, or cap variable names may lack the resources to perform this encoding. The practical payoff: description logics, temporal logics, and database query languages all sit in decidable FOL fragments, making automated reasoning over them possible."
```

## Explainer

You already know that full first-order logic is undecidable: the **Entscheidungsproblem** (decision problem for FOL) has no algorithmic solution, as Church and Turing proved in 1936. There is no algorithm that takes a first-order sentence as input and decides whether it is satisfiable. But this undecidability result applies to the *full* language — it doesn't mean every restricted subset is undecidable. Many practically important fragments turn out to be decidable, sometimes even efficiently so, and understanding which fragments cross the decidability line tells us where the logical "hard core" of undecidability actually lives.

The most natural restriction is on **quantifier prefix**. The quantifier-free fragment is trivially decidable (just evaluate propositional logic). The **monadic fragment** — where all predicates take only one argument — is decidable; Löwenheim proved this in 1915. With only unary predicates, you cannot express relational structure between objects (like "x is connected to y"), so the combinatorics stay manageable. The **Ackermann class** consists of formulas with prefix ∃*∀∃* (any number of existentials, one universal block, then existentials again) and no equality — these are decidable by reduction to finite satisfiability checking. The **Bernays-Schönfinkel class** (∃*∀*) is decidable and corresponds to existential second-order logic over finite structures in disguise; these sentences are satisfiable if and only if finitely satisfiable.

A key parameter is whether the fragment can *encode* computations. Undecidability enters when a fragment can simulate the behavior of a Turing machine — then satisfiability can encode the halting problem. Fragments that avoid relational structure, limit quantifier alternation, or restrict the way variables are reused often escape this trap. The **two-variable fragment** of FOL (with only two variable names, x and y, reused freely) is decidable (NEXPTIME-complete) — this is surprising, because two variables can still express substantial relational content. Adding a third variable restores undecidability. Similarly, **modal logic** is a decidable fragment of FOL: modal formulas translate to FOL formulas in a restricted form (the *standard translation*), and decidability of the modal logic corresponds to decidability of that FOL fragment.

The practical payoff is substantial: **description logics** (the formalism behind OWL ontologies), **temporal logic** (used in model checking), and many database query languages are all decidable because they correspond to decidable fragments of FOL. When you need automated reasoning over a formal language, the first question is: which fragment of FOL does this correspond to, and does that fragment fall on the decidable side of the line? Decidable fragments are not a curiosity — they are the logical backbone of automated verification, knowledge representation, and database theory.

