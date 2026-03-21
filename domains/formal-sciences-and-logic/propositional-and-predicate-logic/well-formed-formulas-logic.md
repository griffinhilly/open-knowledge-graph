---
id: well-formed-formulas-logic
title: Well-Formed Formulas (WFF) in Propositional and First-Order Logic
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: propositional-connectives
  type: hard
- id: propositional-syntax
  type: hard
builds-toward:
- atomic-versus-complex-formulas
- logical-consequence-and-entailment
- open-and-closed-formulas-fol
tags:
- syntax
- propositional-logic
- first-order-logic
- wff
stage: formal-systems
status: draft
---

# Well-Formed Formulas (WFF) in Propositional and First-Order Logic

## Core Idea
A well-formed formula (WFF) is a syntactically valid string following the grammar rules of propositional or first-order logic. In propositional logic, WFFs are built from atomic propositions and connectives (¬, ∧, ∨, →, ↔). In first-order logic, WFFs also include terms, predicates, and quantifiers (∀, ∃), with strict rules about variable binding and scope. Understanding what counts as a valid formula is foundational to defining logical consequence, proof systems, and semantics.

## How It's Best Learned
Start with propositional WFFs using simple examples and counterexamples (e.g., 'P ∧ Q' is WFF, but '∧ P' is not). Progress to first-order by adding terms and quantifiers with exercises on spotting syntactic errors. Use recursive grammar definitions and parse trees to visualize structure.

## Common Misconceptions
- Thinking that any string of symbols with logical connectives is a WFF (no — syntax matters).
- Forgetting that quantifiers must bind variables correctly (∀x P(y) is WFF but leaves y free).
- Assuming parentheses don't matter (they do — they determine scope and precedence).

## Questions

```yaml
- question: "Which of the following strings is NOT a well-formed formula in propositional logic?"
  type: multiple-choice
  options:
    - "(P → Q)"
    - "¬(P ∧ Q)"
    - "(P ∨ ¬Q)"
    - "∧ P Q"
  answer: 3
  explanation: "WFFs in propositional logic are defined inductively: atomic propositions are WFFs; ¬φ is a WFF if φ is; (φ ∧ ψ), (φ ∨ ψ), (φ → ψ), (φ ↔ ψ) are WFFs if φ and ψ are. The string '∧ P Q' puts the connective first in prefix position — but the grammar requires binary connectives to appear *between* their operands (infix), surrounded by parentheses. It has no parse tree under the standard grammar. Options A, B, and C all follow the inductive rules and have valid parse trees."

- question: "In the first-order formula ∀x (P(x) → Q(y)), what is the status of the variables x and y?"
  type: multiple-choice
  options:
    - "Both x and y are bound by the universal quantifier"
    - "x is bound by ∀x; y is free — it is not within the scope of any quantifier"
    - "y is bound because it appears inside the parentheses of the quantifier's scope"
    - "x is free because it is the quantified variable, while y is bound by the predicate Q"
  answer: 1
  explanation: "The universal quantifier ∀x binds every occurrence of x *within its scope* — here, the entire formula (P(x) → Q(y)). x is therefore bound. y, however, has no quantifier anywhere in this formula, so it is a *free variable* — an unspecified parameter. The formula is an *open formula*, not a sentence: its truth value depends on what domain element y is assigned to. Only when all variables are bound (a *closed formula* or sentence) does the formula express a proposition that is simply true or false in a given structure."

- question: "Every syntactically valid propositional WFF corresponds to exactly one parse tree — the grammar is unambiguous when parentheses are used as required."
  type: true-false
  answer: true
  explanation: "The inductive definition of WFFs, with required parentheses around each binary connective application, ensures every WFF has a unique decomposition into its constituent parts. This is why formal logic uses parentheses that might seem excessive: '(P ∧ (Q ∨ R))' and '((P ∧ Q) ∨ R)' are different formulas with different parse trees and different truth conditions. Without parentheses, 'P ∧ Q ∨ R' is ambiguous. The unique parse tree property is what makes truth evaluation by structural induction possible."

- question: "In the first-order formula ∀x P(x) ∧ Q(y), the variable y is implicitly bound by the universal quantifier because it appears in the same formula."
  type: true-false
  answer: false
  explanation: "A quantifier only binds variables within its syntactic scope. In ∀x P(x) ∧ Q(y) (parsed as (∀x P(x)) ∧ Q(y) under standard precedence), the scope of ∀x is just P(x). The variable y in Q(y) is entirely outside that scope and is therefore free. Only ∀y or ∃y would bind y, and only if Q(y) were inside that quantifier's scope. Confusing scope with 'same formula' is a common error; the parse tree of a formula explicitly shows which quantifier governs which variables."

- question: "Why must well-formed formulas be defined by a formal inductive grammar rather than informally as 'any string of logical symbols'? What would go wrong without this definition?"
  type: short-answer
  answer: "Without a formal grammar, there is no principled way to assign a meaning (truth value) to a formula. Logical semantics, proof systems, and the definition of logical consequence all work by structural induction on the parse tree of a WFF — recursively applying rules to sub-formulas. An ill-formed string like '∧ P Q' has no parse tree, so there is no base case or recursive rule to evaluate it. The grammar provides the precise structure that makes every aspect of logic — truth tables, proofs, model theory — well-defined."
  explanation: "This is why WFFs are called 'well-formed': the contrast is with strings that are ill-formed. The formal definition is not pedantry — it is the foundation that makes logic a rigorous mathematical discipline rather than an informal reasoning practice. Every theorem about logic is ultimately a theorem about the structure of WFFs."
```

## Explainer

You already know the propositional connectives — ¬, ∧, ∨, →, ↔ — and the basic syntax of propositional logic. A **well-formed formula (WFF)** is the precise definition of what counts as a grammatically legal string in a logical language. The point is that not every sequence of symbols is meaningful: "∧ P Q ¬" is not a formula any more than "the cat sat the" is a sentence. WFFs are defined by an inductive grammar that tells you exactly which strings are legal.

For **propositional logic**, the grammar is simple. Every atomic proposition (P, Q, R, …) is a WFF. If φ is a WFF, then ¬φ is a WFF. If φ and ψ are WFFs, then (φ ∧ ψ), (φ ∨ ψ), (φ → ψ), and (φ ↔ ψ) are WFFs. That's it — nothing else is a WFF. This inductive definition is powerful because it gives every formula a unique **parse tree**: a tree whose leaves are atomic propositions and whose internal nodes are connectives. The parse tree makes the meaning of a formula unambiguous and is the structure used when evaluating formulas with truth tables.

**First-order logic** extends this with three new ingredients: **terms** (built from variables, constants, and function symbols), **predicates** (applied to terms to make atomic formulas), and **quantifiers** (∀x and ∃x, which bind the variable x). An atomic formula in FOL is something like P(f(x), c) — a predicate applied to terms. Complex FOL formulas are then built by applying connectives and quantifiers: ∀x ∃y (R(x,y) ∧ ¬P(y)) is a WFF; ∀P(x) is not (you cannot quantify over predicates in first-order logic).

The subtlest new concept in FOL WFFs is **variable binding and scope**. In ∀x (P(x) → Q(x)), both occurrences of x are *bound* by the universal quantifier — they are not free variables, just formal placeholders. In ∀x P(x) ∧ Q(y), the variable y is *free* — it is not bound by any quantifier and acts like an unspecified parameter. A formula with no free variables is called a **sentence** (or **closed formula**); it is either true or false in a given structure. A formula with free variables has a truth value only once the free variables are assigned specific elements from the domain. This distinction matters enormously: sentences express propositions about a structure, while open formulas express properties of elements.

Understanding WFFs is foundational because every subsequent concept in logic — truth, satisfaction, proof, consequence — is defined by induction on the structure of WFFs. When you evaluate a formula's truth value, you recurse through its parse tree. When you define what a proof is, you build it up from WFFs step by step. The grammar of WFFs is the backbone on which all of logic hangs.
