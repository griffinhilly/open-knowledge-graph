---
id: uniform-boundedness-principle
title: Uniform Boundedness Principle
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: banach-spaces-definition
  type: hard
tags:
- functional-analysis
stage: abstract-reasoning
status: draft
---

# Uniform Boundedness Principle

## Core Idea
The uniform boundedness principle (Banach-Steinhaus) states that if a family of bounded linear operators {Tᵢ : X → Y} between Banach spaces is pointwise bounded, then the operators are uniformly bounded in norm. This powerful tool controls infinite families of operators.

## Explainer

Imagine a family of linear operators {Tᵢ}. You observe that for every fixed vector x, the outputs Tᵢ(x) are bounded — no single input can be stretched arbitrarily far by any Tᵢ. The question is: does this pointwise control imply global control? Could the operator norms ‖Tᵢ‖ themselves be unbounded, with each operator Tᵢ having a very large norm, just not realized on the particular vector x you tested? The **uniform boundedness principle** (also called the Banach-Steinhaus theorem) answers: no. Pointwise boundedness forces uniform boundedness — there exists a single constant C such that ‖Tᵢ‖ ≤ C for all i.

This is a genuinely surprising fact. The hypothesis is weak: you only know that for each fixed x, the numbers {‖Tᵢ(x)‖} form a bounded set (depending on x). The conclusion is strong: there is one bound that works simultaneously for all operators and all unit vectors. The proof uses the **Baire category theorem**, a key property of complete metric spaces (Banach spaces are complete by definition). The completeness of X prevents the "bad" scenario where the operator norms blow up, because that blowup would require the input space to be covered by a countable union of closed nowhere-dense sets — which the Baire theorem forbids.

Why does this matter? The principle provides a powerful sanity check for infinite families of operators. In Fourier analysis, for instance, the partial sums Sₙ(f) of a Fourier series define a family of linear operators on function spaces. If these operators were pointwise bounded for every f, uniform boundedness would follow automatically. Conversely, the failure of uniform boundedness implies there must exist some input x (in fact a "generic" one in a Baire category sense) for which pointwise boundedness fails — the Fourier series diverges at that point. The theorem converts information about operator norms into information about function behavior.

The key role of completeness in the Banach space assumption should not be overlooked. If X were only a normed space (not complete), the theorem fails: you can construct pointwise bounded families whose norms are unbounded on an incomplete space. Completeness is the structural feature that forces the global bound to exist. This is typical of Banach space theory — the theorems are finely tuned to the complete setting, and the payoff for insisting on completeness is access to powerful tools like this one, the open mapping theorem, and the closed graph theorem.
