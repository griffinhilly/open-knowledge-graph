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

## Questions

```yaml
- question: "In the formula ∀x (P(x, y) → ∃x Q(x, z)), which variables are free?"
  type: multiple-choice
  options:
    - "x only — it appears in both quantifiers"
    - "y and z — they appear without a binding quantifier in this formula"
    - "y only — z is implicitly bound by the inner ∃x"
    - "No variables are free — all variables are bound by some quantifier"
  answer: 1
  explanation: "A variable is free if it appears outside the scope of any quantifier that binds it. In this formula: x is bound by both ∀x and ∃x (the inner ∃x rebinds x within its scope). The variable y appears in P(x, y) — it falls within ∀x's scope, but ∀x only binds x, not y. Similarly, z appears in Q(x, z) within ∃x's scope, but ∃x only binds x. Neither y nor z has a quantifier in this formula. They are both free. The formula is an open formula whose truth value depends on the values assigned to y and z."

- question: "A logician substitutes the term y for the variable x in the formula ∀y (x < y), producing ∀y (y < y). What has gone wrong?"
  type: multiple-choice
  options:
    - "The substitution is invalid because x was already bound by ∀x"
    - "Variable capture: the free variable y became accidentally bound by ∀y, changing the formula's meaning"
    - "The resulting formula ∀y (y < y) is logically equivalent to the original, so no error occurred"
    - "The substitution should have used a fresh variable name, but the resulting meaning is still the same"
  answer: 1
  explanation: "This is the variable capture problem — one of the main syntactic dangers in predicate logic. Before substitution, x was free in ∀y (x < y) and y was free in the term being substituted. After substituting y for x, the previously free y became trapped inside the scope of ∀y, turning it from a free parameter into a bound variable. The original formula (for a specific value of x) says 'every y is greater than x'; the result ∀y (y < y) says 'every element is less than itself,' which is false in any standard ordering. The correct procedure is to first rename the bound variable: ∀y becomes ∀z, giving ∀z (x < z), then substitute to get ∀z (y < z)."

- question: "Bound variables can be renamed throughout their scope without changing the formula's meaning — ∀x P(x) and ∀z P(z) express the same proposition."
  type: true-false
  answer: true
  explanation: "True. This is alpha-equivalence: bound variables are 'dummy variables' — their names are arbitrary labels with no semantic significance. The quantifier ∀x P(x) says 'for every element in the domain, P holds of it.' The name x is just a placeholder referring to the element the quantifier ranges over. Renaming x to z throughout (replacing ∀x with ∀z and every bound occurrence of x with z) produces an identical claim. This is analogous to the fact that ∫₀¹ x² dx and ∫₀¹ t² dt are the same integral — the variable name is a dummy."

- question: "A formula with free variables is incomplete or invalid — it cannot be meaningfully evaluated until all variables are bound by quantifiers."
  type: true-false
  answer: false
  explanation: "False. Open formulas (formulas with free variables) are perfectly well-formed and meaningful — they are predicates or conditions that may be satisfied by particular assignments of values to free variables. The formula x > 5 is an open formula; it is true when x = 7 and false when x = 3. Free variables parameterize a family of claims. An open formula becomes a sentence (with a definite truth value) only when all free variables are either bound by quantifiers or assigned specific values, but the open formula itself is valid and useful — it is how predicates are defined in predicate logic."

- question: "Why does a sentence (a formula with no free variables) have a definite truth value in a given structure, while an open formula does not?"
  type: short-answer
  answer: "A sentence's truth value depends only on the structure (the domain and the interpretation of relation symbols), because every variable occurrence is controlled by a quantifier that ranges over the domain — no external assignment is needed. An open formula contains free variables that refer to unspecified elements of the domain. Without knowing what values those free variables take, the formula's truth cannot be determined. The same open formula P(x) might be true for some elements and false for others. To get a truth value, you must either quantify the free variables (turning the formula into a sentence) or provide a specific variable assignment."
  explanation: "This distinction is foundational for semantics in predicate logic. Sentences are claims about structures; open formulas are predicates that characterize subsets of domains. When we say 'x > 5 defines a predicate,' we mean: for each value of x, the predicate is either satisfied or not. Quantifiers convert predicates into sentences: ∀x (x > 5) is a sentence (false if the domain is all integers, true if the domain is {6, 7, 8, ...}). The free-variable / bound-variable distinction is what separates 'a property something might have' from 'a claim that is true or false.'"
```

## Explainer

From your study of quantifier semantics, you know that ∀x φ(x) means "φ holds for every element x in the domain," and ∃x φ(x) means "φ holds for at least one element." Both quantifiers *bind* the variable x: once you write ∀x or ∃x, any subsequent occurrence of x inside the scope of that quantifier refers to the quantifier's element, not to any external assignment. A variable occurrence is **bound** if it falls within the scope of a matching quantifier, and **free** if it does not.

Consider the formula ∀x (P(x, y) → Q(x)). The variable x is bound — every occurrence of x is inside the ∀x scope. The variable y, however, appears with no quantifier binding it: it is free. The formula as a whole is an **open formula**: its truth value depends on what value you assign to y. If your domain is the integers and P(x, y) means "x < y" and Q(x) means "x > 0," then the formula says "every number less than y is positive," which is true when y = 1 but false when y = -5. The free variable y acts like a *parameter* — the formula defines a property that y may or may not satisfy.

When every variable in a formula is bound, the formula is a **sentence**, and it has a definite truth value in any given structure — no external parameter assignment is needed. ∀x ∃y (x < y) is a sentence; it is true in the integers and false in any finite domain. The bound/free distinction is thus what separates "statements about everything" from "conditions that something might satisfy." A sentence is a claim about a structure; an open formula is a predicate that may be satisfied by particular values.

An important technical point is **alpha-equivalence**: bound variable names are arbitrary. The formula ∀x P(x) and ∀z P(z) are the same formula — renaming a bound variable everywhere in its scope leaves meaning unchanged. This is why bound variables are called *dummy variables*. Free variables, by contrast, cannot be renamed without potentially changing the formula's meaning. When you perform **substitution** — replacing a free variable x with a term t — you must be careful that t contains no variables that would become accidentally bound. For example, substituting y for x in ∀y (x < y) would turn it into ∀y (y < y), which is completely different. This is the **variable capture** problem, and guarding against it (by renaming bound variables first) is one of the main syntactic disciplines of formal logic.
