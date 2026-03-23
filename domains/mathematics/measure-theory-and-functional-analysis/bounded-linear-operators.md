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
stage: expert
status: validated
---

# Bounded Linear Operators

## Core Idea
A linear operator T: X → Y between normed spaces is bounded if ‖T(x)‖_X ≤ C‖x‖_X for all x, or equivalently if T maps the unit ball to a bounded set. Bounded operators are continuous and form a natural subclass of linear maps.

## Questions

```yaml
- question: "Let X and Y be infinite-dimensional Banach spaces, and let T: X → Y be a linear map. Which statement is correct?"
  type: multiple-choice
  options:
    - "T is automatically continuous, since linearity implies continuity in any normed space"
    - "T is continuous if and only if it is bounded — that is, if there exists C such that ‖T(x)‖ ≤ C‖x‖ for all x"
    - "T is continuous if and only if it maps Cauchy sequences to Cauchy sequences"
    - "T cannot be continuous because infinite-dimensional spaces are not compact"
  answer: 1
  explanation: "In finite-dimensional spaces, every linear map is automatically continuous — this is a special theorem about finite dimensions. In infinite-dimensional spaces, this fails: you can construct linear maps that send bounded sequences to unbounded sequences. The correct statement is that, for linear maps between normed spaces, continuity and boundedness are equivalent conditions. The norm bound ‖T(x)‖ ≤ C‖x‖ is the precise condition that rules out pathological behavior. Option C is true for metric spaces generally but is not the standard formulation for linear maps."

- question: "What is the geometric interpretation of the condition ‖T(x)‖ ≤ C‖x‖ for all x in the domain?"
  type: multiple-choice
  options:
    - "T preserves angles between vectors — it maps orthogonal vectors to orthogonal vectors"
    - "T maps the unit ball to a bounded set — the image of every bounded set is bounded"
    - "T is an isometry — it preserves the norm of every vector"
    - "T maps every vector to a vector of smaller norm"
  answer: 1
  explanation: "The condition ‖T(x)‖ ≤ C‖x‖ says that T cannot stretch vectors by more than a factor of C. Equivalently, the image of the unit ball {x : ‖x‖ ≤ 1} is contained in a ball of radius C in the output space — a bounded set. This is the geometric content of boundedness: T cannot send bounded inputs to unbounded outputs. An isometry (option C) would require ‖T(x)‖ = ‖x‖ exactly, which is much stronger. Option D is false — bounded operators can increase norms, just not without limit."

- question: "For linear maps between normed spaces, continuity and boundedness are equivalent conditions."
  type: true-false
  answer: true
  explanation: "This equivalence is one of the first fundamental theorems of functional analysis. If T is bounded (‖T(x)‖ ≤ C‖x‖), then for any convergent sequence xₙ → x: ‖T(xₙ) − T(x)‖ = ‖T(xₙ − x)‖ ≤ C‖xₙ − x‖ → 0, so T is continuous. Conversely, if T is continuous at 0, a simple argument shows T must be bounded. The key is that linearity links behavior at one point (0) to behavior everywhere, so local continuity implies global boundedness. This equivalence fails for nonlinear maps."

- question: "Every linear map between infinite-dimensional Banach spaces is bounded."
  type: true-false
  answer: false
  explanation: "This is the central misconception. In finite-dimensional spaces, the theorem that all linear maps are continuous holds because finite-dimensional spaces are topologically simple. In infinite-dimensional spaces, you can construct linear maps using a Hamel basis that are demonstrably unbounded — they send a sequence of unit vectors to vectors with norms growing without bound. Differential operators (like d/dx on function spaces) are the canonical examples from applications: they are linear but unbounded on natural function spaces. The distinction between bounded and unbounded operators is one of the main reasons functional analysis is non-trivial."

- question: "Why does the proof that a bounded linear operator is continuous work, and why can this argument not be applied to show that an arbitrary linear map is continuous?"
  type: short-answer
  answer: "If ‖T(x)‖ ≤ C‖x‖ for all x, then for any sequence xₙ → x: ‖T(xₙ) − T(x)‖ = ‖T(xₙ − x)‖ ≤ C‖xₙ − x‖ → 0. The bound C allows the norm of the input difference to control the norm of the output difference, giving continuity. For a general linear map without a uniform bound, the constant C might not exist or might be infinite — meaning for some sequence of inputs approaching 0, the outputs might not approach 0."
  explanation: "The whole point of the boundedness condition is that it provides the uniform constant C needed to make the epsilon-delta argument work globally. Without a uniform C, you might have ‖T(xₙ)‖ → ∞ even as ‖xₙ‖ → 0, which is exactly what happens for unbounded operators. Linearity alone maps 0 to 0 (T(0) = T(0+0) = 2T(0) implies T(0) = 0), but it does not control behavior near 0 uniformly across all directions in an infinite-dimensional space."
```

## Explainer

In finite-dimensional spaces, every linear map is automatically continuous — this is a theorem you may have encountered. But once you move to infinite-dimensional Banach spaces, linearity no longer guarantees continuity. You can construct linear maps that send a sequence of vectors with bounded norms to a sequence with unbounded output norms. A **bounded linear operator** is a linear map that rules out this pathology by imposing an explicit norm control: there exists a constant C such that ‖T(x)‖ ≤ C‖x‖ for every input x.

The condition ‖T(x)‖ ≤ C‖x‖ has an elegant geometric reading: T cannot stretch vectors by more than a factor of C. Equivalently, the image of the unit ball {x : ‖x‖ ≤ 1} is contained in a ball of radius C in the output space. This is precisely why bounded operators are continuous: if xₙ → x (i.e., ‖xₙ − x‖ → 0), then ‖T(xₙ) − T(x)‖ = ‖T(xₙ − x)‖ ≤ C‖xₙ − x‖ → 0. Continuity follows immediately from the norm bound — the two conditions are equivalent for linear maps.

The **operator norm** ‖T‖ = sup{‖T(x)‖ : ‖x‖ ≤ 1} captures the sharpest such constant C, the maximum stretch factor over all unit vectors. The space of all bounded linear operators from X to Y, written B(X, Y), inherits a norm from this definition. When Y = X, B(X, X) is not just a normed space but a Banach algebra — operators can be composed, and the operator norm satisfies ‖ST‖ ≤ ‖S‖‖T‖. This algebraic structure is the foundation for spectral theory, where you study how operators act like generalized scalars.

From your study of Banach spaces, you know completeness is what separates "nice" infinite-dimensional spaces from poorly behaved ones. Boundedness of operators reflects the same philosophy: it is the right finiteness condition for linear maps between Banach spaces. Unbounded operators do appear in mathematics — notably as differential operators in quantum mechanics — but they require careful domain restrictions and substantially more technical machinery. In functional analysis, bounded operators are the default setting, the controlled regime where the theory runs smoothly.
