---
id: beth-definability-implicit-explicit
title: 'Beth Definability: From Implicit to Explicit Definitions'
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: craig-lyndon-interpolation
  type: hard
builds-toward:
- definable-closure-independence
tags:
- Beth
- definability
- implicit
- explicit
- elimination
stage: abstract-reasoning
status: draft
---

# Beth Definability: From Implicit to Explicit Definitions

## Core Idea
Beth's theorem states that if a predicate is implicitly defined by a theory (uniquely determined up to isomorphism), then it is explicitly definable (there is a formula φ such that the theory entails the predicate equals φ). This theorem bridges implicit definability (uniqueness up to models) and explicit definability (provable equivalence), with deep connections to model-theoretic properties.

## Explainer

You have already encountered Craig's interpolation theorem, which says that whenever one formula logically implies another, there is an intermediate formula — built from the shared vocabulary — that lies between them. Beth's definability theorem is a striking application of this same machinery to the question of what it means for a theory to "pin down" a predicate.

Start with a concrete example. Suppose you have a theory T in a language that includes a binary relation symbol R, and you notice that any two models of T that agree on all the other symbols must agree on R as well — R is completely determined by the rest. In that case, we say R is **implicitly defined** by T: it is uniquely determined up to the structure of the models, even though you have not written down a formula that says what R actually is. The question Beth's theorem answers is: if R is implicitly defined, can you always make that definition **explicit** — that is, can you find a single formula φ(x, y) in the language without R such that T entails ∀x∀y (R(x,y) ↔ φ(x,y))?

The answer is yes, and the proof proceeds directly from Craig's interpolation theorem. The argument goes roughly like this: implicit definability of R by T is exactly the statement that two copies of T — one in which R plays one role and one in which R' plays another — together imply R = R'. By Craig interpolation, there must be an interpolant, a formula in the shared language (which lacks R and R'), that separates the two. Unpacking what this interpolant says gives the explicit definition of R. The connection illuminates why interpolation is not just a curiosity but a structural fact about how syntax and semantics interact.

**Beth's theorem** matters practically for the question of **eliminability**: when can a defined predicate be removed from a theory without loss? If you introduce a new predicate symbol R as shorthand and your theory implicitly defines R in terms of existing vocabulary, then R is always eliminable — every statement about R translates into a statement about the underlying vocabulary. This is a prerequisite for modularity in formal systems. When implicit and explicit definability come apart (as they do for some extensions of first-order logic), the logic lacks the interpolation property, which is itself a signature of expressive pathology. Beth definability thus serves as a diagnostic tool for measuring how tightly syntax and semantics are coupled in a given logical system.
