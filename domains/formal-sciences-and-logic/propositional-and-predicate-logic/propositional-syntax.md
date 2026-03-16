---
id: propositional-syntax
title: Propositional Logic Syntax
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: statements-and-logical-connectives
  type: hard
- id: conditional-and-biconditional
  type: hard
builds-toward:
- propositional-semantics
- natural-deduction-propositional
- first-order-logic-syntax
tags:
- syntax
- well-formed-formulas
- connectives
- formal-language
stage: formal-systems
status: validated
---

# Propositional Logic Syntax

## Core Idea
Propositional logic syntax defines the exact grammar for constructing well-formed formulas (WFFs) from atomic propositions and logical connectives (¬, ∧, ∨, →, ↔). A WFF is built inductively: every atomic proposition is a WFF, and if φ and ψ are WFFs then so are ¬φ, (φ ∧ ψ), and so on. This purely syntactic definition makes no reference to meaning — a formula is either grammatically valid or it is not. The distinction between syntax (shape of formulas) and semantics (meaning of formulas) is one of the deepest ideas in formal logic.

## How It's Best Learned
Write out the inductive grammar rule explicitly, then practice identifying which strings are WFFs and which are not. Parse formulas into syntax trees to build intuition for structure before worrying about meaning.

## Common Misconceptions
- Confusing syntax with semantics: a formula can be syntactically well-formed yet always false.
- Forgetting that connectives have fixed arity — ∧ is binary, ¬ is unary.
- Precedence ambiguity: ¬p ∧ q means (¬p) ∧ q, not ¬(p ∧ q).

## Questions

```yaml
- question: "Which of the following strings is NOT a well-formed formula (WFF) of propositional logic?"
  type: multiple-choice
  options: ["¬(p ∧ q)", "p → (q ∨ r)", "p ∧ ∧ q", "(p ↔ q) ∧ ¬r"]
  answer: 2
  explanation: "The string 'p ∧ ∧ q' is not a WFF because ∧ is a binary connective that requires a complete WFF on each side. After the first ∧, the parser expects a WFF, but encounters another ∧ instead — so the grammar rule cannot be applied. The other three strings all parse correctly according to the inductive definition: they are built from atomic propositions by applying connectives to sub-WFFs."

- question: "The formula ¬p ∧ q is logically equivalent to ¬(p ∧ q)."
  type: true-false
  answer: false
  explanation: "By precedence, ¬ binds more tightly than ∧, so ¬p ∧ q parses as (¬p) ∧ q — meaning 'p is false AND q is true.' The formula ¬(p ∧ q) means 'it is not the case that both p and q are true,' which by De Morgan's law is equivalent to ¬p ∨ ¬q. These are different formulas with different truth tables. This is one of the most common precedence errors in formal logic."

- question: "The formula p ∧ ¬p is syntactically well-formed even though it is always false. Explain why being a contradiction does not affect syntactic well-formedness."
  type: short-answer
  answer: "Syntax only checks grammatical structure, not truth values. By the inductive definition: p is a WFF (atomic proposition), ¬p is a WFF (negation applied to a WFF), and p ∧ ¬p is a WFF (conjunction of two WFFs). Whether the formula is true, false, or contingent is a semantic question determined by assigning truth values — a completely separate layer of analysis. Syntax and semantics are deliberately kept apart in formal logic."
  explanation: "The syntax/semantics distinction is foundational in formal logic. A grammar defines which strings are legal formulas; separately, a semantics assigns meanings (truth values under interpretations) to those formulas. Contradictions, tautologies, and contingent formulas are all equally well-formed — the grammar does not filter by logical status."
```

## Explainer

When you first learned about logical connectives — AND, OR, NOT, if-then — you probably wrote them in English or with informal symbols. Propositional logic syntax is the step of making this completely precise: defining a formal grammar that specifies, with no ambiguity, exactly which strings of symbols count as legal formulas. This matters because a proof system needs to know unambiguously what it is operating on.

The grammar is defined *inductively*. Start with a set of atomic propositions — call them p, q, r, or p₁, p₂, ... — which are the simplest WFFs. Then, if φ and ψ are already WFFs, the following are also WFFs: ¬φ (negation), (φ ∧ ψ) (conjunction), (φ ∨ ψ) (disjunction), (φ → ψ) (conditional), and (φ ↔ ψ) (biconditional). Nothing else is a WFF. This inductive definition means every WFF has a unique *parse tree* — a tree showing how the formula was built up from atoms — and that tree is the formula's structure.

The most important idea in this topic is the distinction between *syntax* and *semantics*. Syntax is about the shape of formulas: is this string grammatically valid? Semantics is about meaning: what does this formula *say*, and is it true? These are completely separate questions. The string "p ∧ ¬p" is syntactically well-formed — it satisfies the grammar — but semantically it is a contradiction, always false. The string "p ∧ ∧ q" is syntactically invalid and has no semantic value at all. A good logician keeps these layers cleanly separated.

Precedence conventions exist to reduce parentheses. Without them, even a simple formula like ¬p ∧ q → r would require full parenthesization: ((¬p) ∧ q) → r. The standard precedence ordering is: ¬ binds tightest, then ∧, then ∨, then →, then ↔. So ¬p ∧ q → r parses as ((¬p) ∧ q) → r. A very common error is treating ¬p ∧ q as ¬(p ∧ q); always apply the precedence rules before interpreting a formula.

Once you can reliably parse WFFs and draw their syntax trees, you are ready for propositional semantics — the study of which truth-value assignments make WFFs true. The clean separation of syntax from semantics is what lets formal logic give precise answers to questions like "Is this argument valid?" and "Is there any truth assignment that makes both φ and ψ true simultaneously?" You will use this syntactic foundation throughout natural deduction, model theory, and first-order logic.
