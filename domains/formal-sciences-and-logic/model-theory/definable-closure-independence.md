---
id: definable-closure-independence
title: Definable Closure and Algebraic Independence
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: definable-algebraic-closure
  type: hard
- id: stability-theory-introduction
  type: soft
builds-toward:
- morley-rank-and-degree
tags:
- definable-closure
- algebraic-closure
- independence
- dimension
stage: abstract-reasoning
status: draft
---

# Definable Closure and Algebraic Independence

## Core Idea
In a model M, the definable closure dcl(A) is the set of elements definable by formulas with parameters from A; the algebraic closure acl(A) is the set of elements in finitely-defined sets from A. These notions generalize field-theoretic closures and provide a dimension notion for any model. Independence of sets is captured via forking: sets are independent if no element in one is algebraic over the other.

## Explainer

You already know from definable and algebraic closure that a model M provides two natural ways to extend a parameter set A inward. The **definable closure** dcl(A) collects every element b in M that is uniquely pinned down by some first-order formula with parameters from A — that is, the formula φ(x, ā) is satisfied by b and b alone. The **algebraic closure** acl(A) is more permissive: it collects every element b that lives in a finite set definable with parameters from A. The formula φ(x, ā) may have finitely many solutions, and b is one of them. So dcl(A) ⊆ acl(A) always. In a dense linear order, acl(A) = A itself because no finite set of points is definable from finitely many endpoints unless the point is already there. In an algebraically closed field, acl(A) is exactly the field-theoretic algebraic closure of A.

The field analogy is the right one to carry forward. In field theory, a set of elements is **algebraically independent** over a base field F if no element of the set is algebraic over F and the others — that is, no element satisfies a nonzero polynomial with coefficients in F ∪ {the others}. Model theory generalizes this: a set B is **independent over A** if no element of B is algebraic over A ∪ (B minus that element). The precise technical definition uses **forking**: B is independent from C over A if the type of B over A ∪ C does not fork over A. In stable theories, forking captures exactly the failure of algebraic independence — an element forks over A if it is algebraically constrained by the new parameters beyond what A already forced.

The payoff is a robust **dimension theory** that works for any sufficiently well-behaved model. A **basis** of M over A is a maximal independent set; all bases have the same cardinality, called the dimension (or Morley rank in the categorical case). This mirrors the fact that all bases of a vector space have the same cardinality, or all transcendence bases of a field extension have the same degree. The model-theoretic version applies not just to fields and vector spaces but to any stable theory — including certain theories of graphs, groups, and combinatorial structures — wherever forking defines a well-behaved independence relation. Recognizing that dcl, acl, and independence are three interlocking tools that together give a model-theoretic substitute for linear algebra is the central conceptual step in understanding stability theory and its applications.
