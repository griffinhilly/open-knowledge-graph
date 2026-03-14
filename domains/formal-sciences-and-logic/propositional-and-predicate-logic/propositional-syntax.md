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
