---
id: bounded-linear-operators
title: Bounded Linear Operators
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: banach-spaces-definition
  type: hard
- id: vector-spaces
  type: soft
builds-toward:
- operator-norm
- linear-functionals-dual-spaces
tags:
- functional-analysis
- operators
stage: advanced
status: draft
---

# Bounded Linear Operators

## Core Idea
A linear operator T: X → Y between normed spaces is bounded if ‖T(x)‖_X ≤ C‖x‖_X for all x, or equivalently if T maps the unit ball to a bounded set. Bounded operators are continuous and form a natural subclass of linear maps.

## Explainer

In finite-dimensional spaces, every linear map is automatically continuous — this is a theorem you may have encountered. But once you move to infinite-dimensional Banach spaces, linearity no longer guarantees continuity. You can construct linear maps that send a sequence of vectors with bounded norms to a sequence with unbounded output norms. A **bounded linear operator** is a linear map that rules out this pathology by imposing an explicit norm control: there exists a constant C such that ‖T(x)‖ ≤ C‖x‖ for every input x.

The condition ‖T(x)‖ ≤ C‖x‖ has an elegant geometric reading: T cannot stretch vectors by more than a factor of C. Equivalently, the image of the unit ball {x : ‖x‖ ≤ 1} is contained in a ball of radius C in the output space. This is precisely why bounded operators are continuous: if xₙ → x (i.e., ‖xₙ − x‖ → 0), then ‖T(xₙ) − T(x)‖ = ‖T(xₙ − x)‖ ≤ C‖xₙ − x‖ → 0. Continuity follows immediately from the norm bound — the two conditions are equivalent for linear maps.

The **operator norm** ‖T‖ = sup{‖T(x)‖ : ‖x‖ ≤ 1} captures the sharpest such constant C, the maximum stretch factor over all unit vectors. The space of all bounded linear operators from X to Y, written B(X, Y), inherits a norm from this definition. When Y = X, B(X, X) is not just a normed space but a Banach algebra — operators can be composed, and the operator norm satisfies ‖ST‖ ≤ ‖S‖‖T‖. This algebraic structure is the foundation for spectral theory, where you study how operators act like generalized scalars.

From your study of Banach spaces, you know completeness is what separates "nice" infinite-dimensional spaces from poorly behaved ones. Boundedness of operators reflects the same philosophy: it is the right finiteness condition for linear maps between Banach spaces. Unbounded operators do appear in mathematics — notably as differential operators in quantum mechanics — but they require careful domain restrictions and substantially more technical machinery. In functional analysis, bounded operators are the default setting, the controlled regime where the theory runs smoothly.
