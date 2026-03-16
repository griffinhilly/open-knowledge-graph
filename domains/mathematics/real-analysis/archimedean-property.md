---
id: archimedean-property
title: The Archimedean Property
domain: mathematics
course: real-analysis
prerequisites:
- id: ordered-field-axioms
  type: hard
- id: supremum-and-infimum
  type: hard
builds-toward:
- density-of-rationals
tags:
- archimedean
- properties
- infinite
stage: advanced
status: draft
---

# The Archimedean Property

## Core Idea
The Archimedean Property states that for any positive real numbers a and b, there exists a natural number n such that na > b. This means no element is infinitely large relative to another, and it implies that the natural numbers are unbounded above in ℝ. It is a consequence of the completeness axiom.

## Explainer

From your study of ordered field axioms, you know that ℝ is an ordered field — addition and multiplication interact with the ordering in the standard ways. But the ordered field axioms alone do not rule out exotic behavior. There exist ordered fields containing elements larger than every natural number — so-called **infinitely large** elements — and elements positive yet smaller than 1/n for every natural number n — **infinitesimal** elements. The rational numbers ℝ and ℚ do not contain such elements, but other ordered fields do. The Archimedean Property is precisely the statement that rules them out.

The property says: given any two positive reals a and b, you can always "reach" b by taking enough copies of a. Formally, there exists n ∈ ℕ with na > b. Think of a as a unit of measurement and b as a distance to cover. No matter how tiny your unit, repeated application eventually surpasses any fixed distance. This is the intuition behind the statement "you can measure any length with a ruler, given enough patience." An ordered field lacking this property would have an element b so large that no multiple of 1 ever exceeds it — b would be genuinely infinite.

The Archimedean Property is not an axiom of ℝ — it is a **theorem**, proved from the completeness of ℝ (the least upper bound property you studied as the supremum axiom). The argument is clean: suppose ℕ were bounded above in ℝ. Then by completeness, ℕ has a supremum, call it M. Since M − 1 < M is not an upper bound, some natural number n satisfies n > M − 1, so n + 1 > M. But n + 1 ∈ ℕ, contradicting M being an upper bound. Therefore ℕ has no upper bound in ℝ, which is exactly the Archimedean Property with a = 1.

Two important corollaries follow immediately. First, for any ε > 0 there exists n ∈ ℕ with 1/n < ε — the sequence 1/n can be made arbitrarily small. This is used constantly in analysis to construct approximations. Second, for any real x there exists an integer n with n > x — the integers are cofinal in ℝ. Together, these two facts undergird nearly every ε-N argument you will write: you choose N large enough so that 1/N < ε, and this choice is always available precisely because of the Archimedean Property.
