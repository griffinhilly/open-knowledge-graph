---
id: insolvability-quintic
title: Insolvability of the Quintic
domain: mathematics
course: abstract-algebra
prerequisites:
- id: fundamental-theorem-galois-theory
  type: hard
tags:
- quintic
- insolvable
- galois-theory
- radical-extensions
stage: advanced
status: draft
---

# Insolvability of the Quintic

## Core Idea
There is no formula in terms of radicals for the roots of a general quintic polynomial. The proof uses Galois theory: the symmetric group S₅ is not solvable, so no solvable extension can contain all roots of a general quintic.

## Questions

```yaml
- question: "A student claims that since the quintic is 'unsolvable,' the equation x⁵ - 1 = 0 has no solutions. What is wrong with this claim?"
  type: multiple-choice
  options:
    - "x⁵ - 1 = 0 actually has no real solutions, so the student is partly correct"
    - "The insolvability result applies only to degree-6 and higher polynomials, not quintics"
    - "x⁵ - 1 = 0 has roots expressible by radicals; insolvability applies only to the general quintic with Galois group S₅"
    - "The Fundamental Theorem of Algebra only guarantees roots for polynomials over the reals, not over the complex numbers"
  answer: 2
  explanation: "The insolvability result says the *general* quintic — one with Galois group S₅ — cannot be solved by radicals. Specific quintics can be solvable: x⁵ - 1 = 0 has roots that are fifth roots of unity, expressible as e^(2πik/5), and its Galois group is Z₅, which is abelian and hence solvable. Moreover, every degree-5 polynomial has exactly five complex roots by the Fundamental Theorem of Algebra — insolvability only says those roots cannot always be written using radicals, not that they don't exist."

- question: "Why is A₅ the critical obstacle in proving that S₅ is not solvable?"
  type: multiple-choice
  options:
    - "A₅ is larger than S₅, so the derived series cannot pass through it"
    - "A₅ is abelian, so the derived series reaches {e} too quickly to represent radical extensions"
    - "A₅ is simple and non-abelian — it equals its own commutator subgroup, so the derived series gets stuck and never reaches {e}"
    - "A₅ contains S₅ as a normal subgroup, preventing the composition series from terminating"
  answer: 2
  explanation: "A group is solvable if its derived series — the sequence G, [G,G], [[G,G],[G,G]], … — eventually reaches the trivial group {e}. For S₅, the derived series goes S₅ → A₅ → A₅ → ⋯. It gets stuck at A₅ because A₅ is simple: it has no proper non-trivial normal subgroups, which means its commutator subgroup is itself. A simple non-abelian group (like A₅) cannot be solvable, because solvability requires each quotient in the derived series to be abelian. Since A₅ is the 'terminal obstacle,' the series never reaches {e}, and S₅ is not solvable."

- question: "The insolvability of the quintic proves that degree-5 polynomials have no roots."
  type: true-false
  answer: false
  explanation: "This is the most important misconception to dispel. The Fundamental Theorem of Algebra guarantees that every degree-5 polynomial has exactly five roots in the complex numbers. Insolvability is not about existence of roots — it is about expressibility. The roots of a general quintic exist and can be approximated numerically to arbitrary precision; what cannot be done is write them as a finite combination of field operations and radicals starting from the coefficients. Special functions like the Bring radical can express quintic roots, just not radicals."

- question: "A polynomial is solvable by radicals if and only if its Galois group is a solvable group — one whose derived series terminates at the trivial group."
  type: true-false
  answer: true
  explanation: "This is the Fundamental Theorem of Galois Theory applied to radical solvability. A solvable group has a composition series with abelian (specifically cyclic of prime order) quotients, which corresponds precisely to a tower of field extensions where each step adjoins an nth root. Going up such a tower produces a splitting field for the polynomial via radicals. If the Galois group is not solvable — as with S₅ — no such tower can exist, and the polynomial cannot be solved by radicals. The group-theoretic condition and the field-theoretic condition are exactly equivalent."

- question: "Why is A₅ unsolvable as a group, and how does this prove that a general quintic cannot be solved by radicals?"
  type: short-answer
  answer: "A₅ is simple and non-abelian: its only normal subgroups are {e} and A₅ itself. This means A₅ equals its own commutator subgroup [A₅, A₅] = A₅, so the derived series of A₅ never decreases — it stays at A₅ forever. Because the derived series of S₅ reaches A₅ and then stalls (since A₅ = [A₅, A₅]), the derived series of S₅ never reaches {e}, making S₅ not solvable. Since a polynomial is solvable by radicals iff its Galois group is solvable, and the general quintic has Galois group S₅ (which is not solvable), no radical expression can produce its roots."
  explanation: "The simplicity of A₅ is the key fact that makes A₅ — and hence S₅ — unsolvable. Simplicity means there is no way to 'factor out' A₅ into smaller pieces via normal subgroup quotients, which is exactly what solvability requires. This is why the same argument fails for degree 4: S₄ is solvable (its derived series is S₄ → A₄ → V₄ → {e} → ⋯, where V₄ is the Klein four-group), which corresponds to the existence of the quartic formula."
```

## Explainer

For centuries, mathematicians sought a "quintic formula" — a combination of +, −, ×, ÷, and radicals (nth roots) that, given the five coefficients of a degree-5 polynomial, produces its roots. The quadratic formula has existed since antiquity. Cardano and Ferrari found formulas for cubics and quartics in the 16th century. But no one could crack degree 5. Abel proved in 1824 that no such formula exists. Galois explained exactly why.

From the Fundamental Theorem of Galois Theory you know that a polynomial is **solvable by radicals** if and only if its Galois group is a **solvable group** — meaning it has a composition series where each successive quotient is abelian (cyclic of prime order). The proof strategy is: find a specific degree-5 polynomial whose Galois group is S₅, the symmetric group on 5 elements, and then show S₅ is not solvable.

Why is S₅ not solvable? A group is solvable if its derived series eventually reaches the trivial group. The derived series of S₅ starts at S₅, then reaches A₅ (the alternating group of even permutations), and stops: [S₅, S₅] = A₅ and [A₅, A₅] = A₅. A₅ equals its own commutator subgroup because A₅ is **simple** — it has no normal subgroups except itself and {e}. A non-trivial simple non-abelian group cannot be solvable. Since the derived series gets stuck at A₅ and never reaches {e}, S₅ is not solvable.

The conclusion follows from the Galois correspondence: any radical extension corresponds to a tower of field extensions where each step adjoins an nth root, producing a solvable Galois group at each level. If the Galois group of a polynomial is not solvable, no such tower can split the polynomial completely. A general quintic has Galois group S₅, which is not solvable — so no radical expression can express its roots. This does not mean quintics have no roots (the Fundamental Theorem of Algebra guarantees five complex roots); it means those roots cannot be written in terms of radicals. Numerical methods, or special functions like the Bring radical, are required instead.
