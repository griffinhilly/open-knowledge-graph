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
stage: expert
status: validated
---

# Definable Closure and Algebraic Independence

## Core Idea
In a model M, the definable closure dcl(A) is the set of elements definable by formulas with parameters from A; the algebraic closure acl(A) is the set of elements in finitely-defined sets from A. These notions generalize field-theoretic closures and provide a dimension notion for any model. Independence of sets is captured via forking: sets are independent if no element in one is algebraic over the other.

## Questions

```yaml
- question: "An element b satisfies exactly 3 distinct solutions to the formula φ(x, a₁, a₂) with parameters from A. Which closure contains b?"
  type: multiple-choice
  options:
    - "dcl(A) only — b is uniquely specified by the formula"
    - "Neither dcl(A) nor acl(A) — b must be the unique solution to be in either"
    - "acl(A) but not dcl(A) — b is in a finite definable set but is not uniquely pinned"
    - "acl(A) and dcl(A) — any element appearing in a definable formula is in both"
  answer: 2
  explanation: "dcl(A) requires b to be the *unique* solution — if φ has multiple solutions, b is not definitionally determined. acl(A) only requires b to lie in a *finite* definable set, and a set of 3 elements qualifies. So b ∈ acl(A) but b ∉ dcl(A). This is why dcl(A) ⊆ acl(A) always, but the containment can be strict."

- question: "In which model does acl(A) = A for any parameter set A (i.e., the algebraic closure adds nothing)?"
  type: multiple-choice
  options:
    - "An algebraically closed field — every finite set is already closed"
    - "A dense linear order without endpoints — no finite set of points is definable from others"
    - "A vector space over Q — linear combinations generate all elements algebraically"
    - "The integers ℤ — the division algorithm collapses all ideals to principal ones"
  answer: 1
  explanation: "In a dense linear order (like ℚ with the usual ordering), for any finite set of parameters A, the only elements whose membership in a finite definable set is forced are the parameters themselves. You cannot trap a new point in a finite definable set using only finitely many endpoints in a dense order. By contrast, in an algebraically closed field, acl(A) is the full field-theoretic algebraic closure — much larger than A."

- question: "In a stable theory, a set B is independent from C over A if and only if no element of B is algebraic over A ∪ (C minus that element)."
  type: true-false
  answer: true
  explanation: "This is the correct model-theoretic definition of independence over A. It directly mirrors field-theoretic algebraic independence: a set of elements is algebraically independent over F if no element satisfies a polynomial over F and the remaining elements. In stable theories, forking captures exactly this algebraic constraint — an element forks over A iff it is algebraically constrained by the new parameters beyond what A already forced."

- question: "The definable closure dcl(A) and the algebraic closure acl(A) always coincide in any first-order model."
  type: true-false
  answer: false
  explanation: "dcl(A) ⊆ acl(A) always, but they need not be equal. dcl(A) requires the element to be the *unique* solution to some formula with parameters from A. acl(A) only requires the element to lie in a *finite* definable set — it may not be pinned down uniquely. Dense linear orders provide the clearest example: acl(A) = A (no new elements), but in an algebraically closed field, acl(A) properly contains dcl(A) since algebraic elements satisfying polynomials of degree > 1 are in acl but not dcl."

- question: "Why does the model-theoretic independence relation (via forking) qualify as a genuine dimension theory, and what algebraic notion does it generalize?"
  type: short-answer
  answer: "Model-theoretic independence generalizes algebraic independence from field theory. In a stable theory, forking captures when an element is 'algebraically constrained' by new parameters beyond a base set A. A basis (maximal independent set) can be defined just as in field theory, and all bases have the same cardinality — the dimension of the model over A. This mirrors the vector space theorem that all bases have the same size, and the field-theory result that all transcendence bases of an extension have the same transcendence degree. The machinery works for any stable theory, not just fields."
  explanation: "The point is that dcl, acl, and independence together reconstruct 'linear algebra over a model.' The key steps are: (1) acl generalizes algebraic closure, (2) independence generalizes algebraic independence (no element is acl-dependent on the others), and (3) all maximal independent sets have the same cardinality (like vector space dimension). This gives a dimension notion valid in any stable model — including theories of graphs, groups, and combinatorial structures — wherever forking is well-behaved."
```

## Explainer

You already know from definable and algebraic closure that a model M provides two natural ways to extend a parameter set A inward. The **definable closure** dcl(A) collects every element b in M that is uniquely pinned down by some first-order formula with parameters from A — that is, the formula φ(x, ā) is satisfied by b and b alone. The **algebraic closure** acl(A) is more permissive: it collects every element b that lives in a finite set definable with parameters from A. The formula φ(x, ā) may have finitely many solutions, and b is one of them. So dcl(A) ⊆ acl(A) always. In a dense linear order, acl(A) = A itself because no finite set of points is definable from finitely many endpoints unless the point is already there. In an algebraically closed field, acl(A) is exactly the field-theoretic algebraic closure of A.

The field analogy is the right one to carry forward. In field theory, a set of elements is **algebraically independent** over a base field F if no element of the set is algebraic over F and the others — that is, no element satisfies a nonzero polynomial with coefficients in F ∪ {the others}. Model theory generalizes this: a set B is **independent over A** if no element of B is algebraic over A ∪ (B minus that element). The precise technical definition uses **forking**: B is independent from C over A if the type of B over A ∪ C does not fork over A. In stable theories, forking captures exactly the failure of algebraic independence — an element forks over A if it is algebraically constrained by the new parameters beyond what A already forced.

The payoff is a robust **dimension theory** that works for any sufficiently well-behaved model. A **basis** of M over A is a maximal independent set; all bases have the same cardinality, called the dimension (or Morley rank in the categorical case). This mirrors the fact that all bases of a vector space have the same cardinality, or all transcendence bases of a field extension have the same degree. The model-theoretic version applies not just to fields and vector spaces but to any stable theory — including certain theories of graphs, groups, and combinatorial structures — wherever forking defines a well-behaved independence relation. Recognizing that dcl, acl, and independence are three interlocking tools that together give a model-theoretic substitute for linear algebra is the central conceptual step in understanding stability theory and its applications.
