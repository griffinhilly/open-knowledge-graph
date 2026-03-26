---
id: open-and-closed-formulas-fol
title: Open and Closed Formulas in First-Order Logic
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: first-order-logic-syntax
  type: hard
- id: variable-binding-and-scope
  type: hard
builds-toward:
- ground-terms-and-formulas
- quantifier-instantiation-rules
- variable-substitution-capture-avoidance
tags:
- first-order-logic
- variables
- binding
- scope
stage: formal-systems
status: validated
---

# Open and Closed Formulas in First-Order Logic

## Core Idea
A closed formula (or sentence) in first-order logic is a formula where every variable is bound by a quantifier; an open formula has at least one free (unbound) variable. For example, ∀x P(x) is closed, but P(x) and ∃y Q(x, y) are open (in the latter, x is free). Closed formulas are meaningful as statements: they are either true or false in a structure. Open formulas need an assignment of values to free variables to determine truth value.

## How It's Best Learned
Use concrete examples with marked quantifiers. Identify bound vs. free variables systematically, drawing scope lines for quantifiers. Emphasize that truth value of a closed formula is structure-relative (no variable assignment needed), while truth of an open formula depends on both the structure and variable assignment.

## Common Misconceptions
- Thinking all formulas must be closed (many proof systems and model-theoretic arguments involve open formulas).
- Confusing the same variable name in nested quantifiers (∀x ∃x P(x) binds two different instances).
- Believing a free variable is always 'undefined' (it's not — its truth value depends on the chosen assignment).

## Questions

```yaml
- question: "Which of the following is a closed formula (sentence) in first-order logic?"
  type: multiple-choice
  options:
    - "P(x) ∧ Q(y)"
    - "∃y (y · y = x)"
    - "∀x ∃y (x + y = 0)"
    - "∀x P(x) → Q(z)"
  answer: 2
  explanation: "Option C is the only sentence: both x and y are bound by their respective quantifiers (∀x and ∃y), so there are no free variables. Option A has x and y free. Option B has x free (y is bound by ∃y but x has no quantifier). Option D has z free (even though x is bound by ∀x). A closed formula requires every variable occurrence to be within the scope of a quantifier that binds it."

- question: "A logician writes the formula ∃y (y · y = x) and asks whether it is true or false. What information is needed to answer?"
  type: multiple-choice
  options:
    - "Only the domain (the structure), since the existential quantifier handles y"
    - "Both the domain (structure) and a specific assignment of a value to the free variable x"
    - "Nothing — the formula is neither true nor false because it is open"
    - "Only the value of y, since it appears in the predicate"
  answer: 1
  explanation: "This is an open formula: y is bound by ∃y, but x is free. The truth value depends on both the structure (which determines what values are in the domain) and the variable assignment (which assigns a specific value to x). For example, in the natural numbers, the formula is true when x is assigned a perfect square and false otherwise. Open formulas are not meaningless — they have truth values relative to a structure and assignment, not on their own."

- question: "The truth value of a closed formula (sentence) in a given structure is determined solely by the structure itself, without reference to any variable assignment."
  type: true-false
  answer: true
  explanation: "A sentence has no free variables — all variables are bound by quantifiers, which internally specify their range of values. The quantifiers handle the 'what does x refer to?' question internally, so no external assignment is needed. This is precisely why sentences are the natural objects of logical theorems, axioms, and model theory: '∀x (x > 0 → x² > 0)' is either true or false in the natural numbers, period, with no additional information needed."

- question: "A free variable in a formula means the formula has no truth value and is logically meaningless until most variables are bound by quantifiers."
  type: true-false
  answer: false
  explanation: "Free variables are not undefined — they are parameters awaiting an assignment. Given a structure and a variable assignment (a function mapping free variables to domain elements), any formula, open or closed, has a determinate truth value. The open formula P(x) is meaningful: it is true of exactly the elements x in the domain that satisfy P. In fact, open formulas are central to predicate logic — they define predicates, and substituting terms for free variables is how universal instantiation works."

- question: "Explain the difference between a sentence (closed formula) and an open formula in first-order logic, and explain why sentences are the natural objects of logical axioms rather than open formulas."
  type: short-answer
  answer: "A sentence (closed formula) has no free variables — every variable is bound by a quantifier. Its truth value is determined entirely by the structure, with no variable assignment needed. An open formula has at least one free variable; its truth value depends on both the structure and an assignment of values to those free variables. Axioms are sentences because an axiom must make a definite claim that is true or false in a model — not a conditional claim that depends on what values free variables happen to have. If an axiom contained free variables, its truth would be assignment-dependent, which would undermine its role as a fixed foundational statement."
  explanation: "This distinction is fundamental to model theory. When we say 'the Peano axioms are true in the natural numbers,' each axiom is a sentence that can be evaluated as true or false without ambiguity. An open formula like 'x > 0' cannot serve this role — it is true for some elements of the domain and false for others. The shift from open to closed formulas is what allows logic to make structural claims rather than merely describing conditions on individual elements."
```

## Explainer

From your study of first-order logic syntax and variable binding, you know that quantifiers bind variables — ∀x means "for all values of x" and ∃x means "there exists a value of x." The open/closed distinction is simply careful bookkeeping: which variables in a formula are bound by a quantifier, and which are left "dangling"? A **closed formula** (or **sentence**) has no free variables — every variable occurrence is within the scope of some quantifier binding it. An **open formula** has at least one **free variable** — an occurrence not captured by any enclosing quantifier.

A few examples sharpen the distinction. The formula ∀x (x > 0 → ∃y (y · y = x)) is a sentence: both x and y are bound. The formula x > 0 is open: x appears with no quantifier. The formula ∃y (y · y = x) is also open: y is bound by ∃y, but x is free. In this last formula, whether the statement is true depends on what value x has — in the natural numbers, it is true when x is a perfect square and false otherwise. The free variable x is like an input to a predicate: it awaits an assignment before the formula has a definite truth value.

The practical significance is immediate: sentences can be evaluated as true or false in a structure directly, with no additional information. "For all x, x · 1 = x" is true in the natural numbers, period. But "x · 1 = x" is an open formula that becomes meaningful only when you supply a **variable assignment** — a function from free variables to elements of the domain. Together, a structure and a variable assignment determine the truth value of any formula, open or closed. For sentences, the assignment is irrelevant (quantifiers handle all variables internally), which is why sentences are the natural objects of logical theorems, axioms, and model theory.

The distinction has deep consequences for proof systems. **Substitution** — replacing a free variable with a term — is how universal instantiation works: from ∀x P(x) you derive P(t) by substituting term t for x. But substitution must be **capture-avoiding**: if t contains a variable y, and y would fall inside a ∀y quantifier after substitution, the free y in t would be "captured" by that quantifier, changing the formula's meaning. The rules for safe substitution are precisely about tracking which variables are free in which subformulas. Mastering open and closed formulas is therefore not a mere syntactic exercise — it is the prerequisite for every formal proof rule and semantic argument you will encounter in predicate logic.
