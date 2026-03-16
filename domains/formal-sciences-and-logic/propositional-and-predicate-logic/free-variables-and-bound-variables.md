---
id: free-variables-and-bound-variables
title: Free Variables and Bound Variables
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: universal-quantifier-semantics
  type: hard
- id: existential-quantifier-semantics
  type: hard
builds-toward:
- substitution-and-instantiation
- variable-binding-and-scope
tags:
- syntax
- semantics
- variables
stage: formal-systems
status: draft
---

# Free Variables and Bound Variables

## Core Idea
A variable x is bound if it appears within the scope of ∀x or ∃x; otherwise it is free. Bound variables are placeholders—renaming them does not change the formula's meaning. Free variables affect truth conditions; a sentence (no free variables) has a definite truth value in a structure, while an open formula does not.

## How It's Best Learned
Visually mark quantifier scopes in complex formulas. Identify which variable occurrences are bound vs. free. Observe that ∀x P(x, y) is true iff P(a, y) holds for all a, showing free y remains unquantified.

## Common Misconceptions
Thinking a formula with free variables is incomplete or invalid. Confusing variable name with binding status. Not recognizing that free variables parameterize a family of formulas.

## Explainer

From your study of quantifier semantics, you know that ∀x φ(x) means "φ holds for every element x in the domain," and ∃x φ(x) means "φ holds for at least one element." Both quantifiers *bind* the variable x: once you write ∀x or ∃x, any subsequent occurrence of x inside the scope of that quantifier refers to the quantifier's element, not to any external assignment. A variable occurrence is **bound** if it falls within the scope of a matching quantifier, and **free** if it does not.

Consider the formula ∀x (P(x, y) → Q(x)). The variable x is bound — every occurrence of x is inside the ∀x scope. The variable y, however, appears with no quantifier binding it: it is free. The formula as a whole is an **open formula**: its truth value depends on what value you assign to y. If your domain is the integers and P(x, y) means "x < y" and Q(x) means "x > 0," then the formula says "every number less than y is positive," which is true when y = 1 but false when y = -5. The free variable y acts like a *parameter* — the formula defines a property that y may or may not satisfy.

When every variable in a formula is bound, the formula is a **sentence**, and it has a definite truth value in any given structure — no external parameter assignment is needed. ∀x ∃y (x < y) is a sentence; it is true in the integers and false in any finite domain. The bound/free distinction is thus what separates "statements about everything" from "conditions that something might satisfy." A sentence is a claim about a structure; an open formula is a predicate that may be satisfied by particular values.

An important technical point is **alpha-equivalence**: bound variable names are arbitrary. The formula ∀x P(x) and ∀z P(z) are the same formula — renaming a bound variable everywhere in its scope leaves meaning unchanged. This is why bound variables are called *dummy variables*. Free variables, by contrast, cannot be renamed without potentially changing the formula's meaning. When you perform **substitution** — replacing a free variable x with a term t — you must be careful that t contains no variables that would become accidentally bound. For example, substituting y for x in ∀y (x < y) would turn it into ∀y (y < y), which is completely different. This is the **variable capture** problem, and guarding against it (by renaming bound variables first) is one of the main syntactic disciplines of formal logic.
