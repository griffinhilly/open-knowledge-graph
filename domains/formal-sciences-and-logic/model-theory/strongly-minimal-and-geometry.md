---
id: strongly-minimal-and-geometry
title: Strongly Minimal Sets and Geometric Structure
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: stability-theory-introduction
  type: hard
- id: definability-and-algebraic-applications
  type: hard
builds-toward:
- o-minimality-and-tame-geometry
- applications-ordered-fields-algebraically-closed
tags:
- strongly-minimal
- geometry
- stability
stage: advanced
status: draft
---

# Strongly Minimal Sets and Geometric Structure

## Core Idea
A definable set is strongly minimal if every definable subset is either finite or has finite complement. The theory of strongly minimal sets provides a geometric framework where dimension is well-defined and obeys matroid laws like linear algebra. ACF (algebraically closed fields) exemplifies strongly minimal geometry where geometry corresponds to algebraic geometry.

## Explainer

From stability theory, you know that stable theories have well-controlled type spaces — types do not "branch" in the way they do in unstable theories, and this constrains how models can differ from one another. **Strongly minimal** theories push stability to an extreme: not only is type behavior controlled, but every definable set is as simple as possible. A set D is **strongly minimal** if for every formula φ(x, ā) with parameters ā from D, the set φ(D, ā) is either finite or cofinite (has finite complement). There is no "middle ground" — no definable subset can have both infinite size and infinite complement. This rigidity is what makes strongly minimal sets amenable to geometric analysis.

The canonical example is ℂ as an algebraically closed field (or more precisely, the theory ACF₀ or ACFₚ). The strongly minimal set is the universe itself: any definable subset of an algebraically closed field is a Boolean combination of zero sets of polynomials, and by the Nullstellensatz, a polynomial in one variable has finitely many roots — so any quantifier-free definable subset of the line is finite or cofinite. This is not a coincidence: it reflects a deep connection between model-theoretic simplicity and the algebraic geometry of varieties. Your prerequisite on definability and algebraic applications showed how definable sets correspond to algebraic sets; strong minimality sharpens this to a precise tameness condition.

The geometric framework comes from the notion of **algebraic closure** internal to the model. In a strongly minimal structure, define acl(A) — the **algebraic closure** of a parameter set A — as the set of all elements satisfying a formula with finitely many solutions over A. This is analogous to the algebraic closure of a field, but defined purely model-theoretically. The operation acl satisfies the **matroid axioms** (exchange principle, monotonicity, finite character), so it defines a genuine **pregeometry** on the strongly minimal set. Dimension in this pregeometry is well-defined: the dimension of a tuple ā over a set B is the size of a maximal subset of ā that is "independent" over B (no element is in the algebraic closure of B and the others).

This dimension theory is what makes strongly minimal sets so powerful. Just as in linear algebra over a field, where dimension classifies vector spaces up to isomorphism and the dimension of a subspace plus the dimension of the quotient equals the total, strongly minimal structures are classified by dimension. Two models of a strongly minimal theory with the same uncountable cardinality κ are isomorphic: they are both just "κ-dimensional" copies of the pregeometry. This gives strongly minimal theories a categorical structure at uncountable cardinals — a property called **uncountable categoricity** (ℵ₁-categoricity and beyond) — which Morley's theorem characterizes as equivalent to ω-stability over the whole theory.

The deeper significance is that strong minimality provides a model of **pure geometric abstraction**: a structure where "independence" and "dimension" have clear meanings, combinatorial geometry controls the model-theoretic behavior, and algebraic geometry is a special case. From here, the study of **o-minimality** (where definable sets are finite unions of intervals rather than finite/cofinite sets) generalizes the same geometric intuition to ordered structures, and the applications to algebraically closed fields connect model theory directly to algebraic geometry and number theory.

