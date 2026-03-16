---
id: structures-and-interpretations
title: Structures and Interpretations
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: formulas-and-well-formed-expressions
  type: hard
- id: set-membership-and-notation
  type: soft
builds-toward:
- satisfaction-in-structures
- model-interpretation-and-satisfaction
tags:
- semantics
- models
- first-order-logic
stage: formal-systems
status: draft
---

# Structures and Interpretations

## Core Idea
A structure M consists of a non-empty domain D and an interpretation function I assigning to each constant a member of D, to each n-ary function symbol a function D^n → D, and to each n-ary predicate a relation on D^n. An interpretation specifies what symbols mean. The same formula can be true in some structures and false in others.

## How It's Best Learned
Construct small explicit models with finite domains. Evaluate formulas in them. Observe how changing a predicate's interpretation changes which formulas are satisfied.

## Explainer

When you first learned propositional logic, a truth assignment gave meaning to variables: "let P be true, let Q be false." In predicate logic, formulas talk about *objects* — "there exists an x such that..." or "for all x, if P(x) then Q(x)." To evaluate such formulas, you need to know what the objects are and what the predicates mean. That is precisely what a **structure** provides.

A **structure** M has two components. First, a **domain** D — a non-empty set of objects, the "universe" of discourse. This can be anything: the natural numbers, a set of five people, an abstract set {a, b, c}. Second, an **interpretation function** I that assigns concrete meanings to the non-logical symbols. For each constant symbol c, I(c) is a specific element of D. For each n-ary function symbol f, I(f) is an actual function Dⁿ → D. For each n-ary predicate symbol P, I(P) is a relation — a subset of Dⁿ. Together, D and I determine whether any closed formula is true or false.

Consider the formula ∀x ∀y (R(x,y) → R(y,x)). Over the domain D = {1, 2, 3} with R interpreted as the "less than" relation {(1,2), (1,3), (2,3)}, this formula is *false* — R(1,2) holds but R(2,1) does not. Change the interpretation of R to the equality relation {(1,1), (2,2), (3,3)}, and the same formula becomes *true*. The formula itself has not changed; only the structure has. This is the key insight: a formula is not true or false on its own — it is true or false *in a specific structure*.

From your prerequisite on well-formed expressions, you know how formulas are built syntactically from variables, connectives, and quantifiers. A structure provides the semantic layer that gives those formulas meaning. **Satisfaction** (M ⊨ φ) is the technical relation connecting structures and formulas: M satisfies φ when φ is true in M under the given interpretation. This opens the door to the central questions of model theory and formal semantics: which structures satisfy a given formula? Can we construct a structure that satisfies all the axioms of a given theory? Can two different structures satisfy exactly the same formulas? All of these questions are answered by reasoning carefully about how structures and interpretations work.
