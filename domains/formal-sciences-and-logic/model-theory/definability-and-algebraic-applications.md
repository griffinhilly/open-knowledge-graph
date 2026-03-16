---
id: definability-and-algebraic-applications
title: Definability and Applications to Algebraic Geometry
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: model-interpretation-and-satisfaction
  type: hard
- id: quantifier-elimination-decidability
  type: soft
- id: field-definition-examples
  type: soft
tags:
- definable set
- algebraic variety
- model-theoretic geometry
- Zilber-Pink
stage: advanced
status: draft
---

# Definability and Applications to Algebraic Geometry

## Core Idea
A subset of a model is definable if it can be described by a first-order formula with parameters. Model-theoretic techniques studying definable sets have powerful applications in algebraic geometry: quantifier elimination gives effective descriptions of solution sets, stability theory constrains object dimension, and saturation reveals structural rigidity. Modern applications include proofs in o-minimal geometry.

## Explainer

From your work with model interpretation and satisfaction, you know that a first-order formula φ(x₁, …, xₙ) is satisfied by tuples from a structure M. A **definable set** is simply the solution set of such a formula: the collection of all n-tuples from M satisfying φ. In the real numbers (ℝ, +, ×, 0, 1), the formula x² + y² = 1 defines the unit circle; the formula x > 0 ∧ y > 0 defines the open first quadrant; the formula ∃z(z² = x) defines the non-negative reals. Every algebraic or semialgebraic set you can write as a boolean combination of polynomial equations and inequalities is definable in this structure. The deep question is: what sets are *not* definable, and what structure does the collection of definable sets impose?

Your prerequisite on quantifier elimination is the key tool. A structure admits **quantifier elimination** if every first-order formula is equivalent, in that structure, to a quantifier-free formula. In (ℝ, +, ×, 0, 1), the Tarski-Seidenberg theorem says quantifier elimination holds — every definable set is a finite boolean combination of polynomial equalities and inequalities (a **semialgebraic set**). This has an immediate geometric payoff: the projection of a semialgebraic set is still semialgebraic, because projection corresponds to existential quantification, which quantifier elimination can eliminate. This single observation underlies much of real algebraic geometry.

The notion of **o-minimality** packages the tameness of semialgebraic geometry into an abstract model-theoretic condition. A structure (M, <, …) is **o-minimal** if every definable subset of M (using one variable) is a finite union of points and open intervals. The real numbers with semialgebraic sets are o-minimal. So is ℝ expanded by the restricted exponential and sine functions. O-minimal structures guarantee that definable sets have finite "topological complexity" — they decompose into finitely many cells, have well-behaved dimensions, and avoid pathological examples like the Cantor set. The finiteness theorem (definable families have uniformly bounded topological complexity) is a key result that has been applied in diophantine geometry.

Modern applications include the Pila-Wilkie theorem and its consequences for the Zilber-Pink conjecture, which concerns intersections of algebraic varieties with special subvarieties of Shimura varieties. The argument works by counting rational points on definable sets using o-minimal techniques, showing that "too many" rational points force an algebraic explanation. The transfer goes: algebraic geometry poses a question about number-theoretic points, model theory (o-minimality) provides a counting theorem for definable sets, and the combination gives a diophantine result. This is the hallmark of modern applications of model theory to geometry — the model-theoretic framework provides general structural theorems that, when instantiated in algebraically rich structures, yield concrete geometric and number-theoretic consequences that would be difficult to reach by purely algebraic methods.
