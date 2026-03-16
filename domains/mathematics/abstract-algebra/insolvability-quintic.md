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

## Explainer

For centuries, mathematicians sought a "quintic formula" — a combination of +, −, ×, ÷, and radicals (nth roots) that, given the five coefficients of a degree-5 polynomial, produces its roots. The quadratic formula has existed since antiquity. Cardano and Ferrari found formulas for cubics and quartics in the 16th century. But no one could crack degree 5. Abel proved in 1824 that no such formula exists. Galois explained exactly why.

From the Fundamental Theorem of Galois Theory you know that a polynomial is **solvable by radicals** if and only if its Galois group is a **solvable group** — meaning it has a composition series where each successive quotient is abelian (cyclic of prime order). The proof strategy is: find a specific degree-5 polynomial whose Galois group is S₅, the symmetric group on 5 elements, and then show S₅ is not solvable.

Why is S₅ not solvable? A group is solvable if its derived series eventually reaches the trivial group. The derived series of S₅ starts at S₅, then reaches A₅ (the alternating group of even permutations), and stops: [S₅, S₅] = A₅ and [A₅, A₅] = A₅. A₅ equals its own commutator subgroup because A₅ is **simple** — it has no normal subgroups except itself and {e}. A non-trivial simple non-abelian group cannot be solvable. Since the derived series gets stuck at A₅ and never reaches {e}, S₅ is not solvable.

The conclusion follows from the Galois correspondence: any radical extension corresponds to a tower of field extensions where each step adjoins an nth root, producing a solvable Galois group at each level. If the Galois group of a polynomial is not solvable, no such tower can split the polynomial completely. A general quintic has Galois group S₅, which is not solvable — so no radical expression can express its roots. This does not mean quintics have no roots (the Fundamental Theorem of Algebra guarantees five complex roots); it means those roots cannot be written in terms of radicals. Numerical methods, or special functions like the Bring radical, are required instead.
