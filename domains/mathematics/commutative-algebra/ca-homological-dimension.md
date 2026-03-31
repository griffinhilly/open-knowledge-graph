---
id: ca-homological-dimension
title: Homological Dimension
domain: mathematics
course: commutative-algebra
prerequisites:
- id: ca-exact-sequences
  type: hard
- id: ca-regular-sequences
  type: hard
- id: ca-flatness
  type: soft
builds-toward: []
tags:
- projective-dimension
- injective-dimension
- global-dimension
- free-resolution
- auslander-buchsbaum
- serre-theorem
- regular-local-ring
stage: expert
status: validated
---

# Homological Dimension

## Core Idea
The projective dimension of a module M measures how far M is from being projective, via the minimum length of a projective resolution. The global dimension of a ring R is the supremum of projective dimensions of all modules. Serre's theorem -- that a Noetherian local ring is regular if and only if it has finite global dimension -- was the first major application of homological algebra to commutative algebra, and the Auslander-Buchsbaum formula pd(M) + depth(M) = depth(R) connects projective dimension to the concrete notion of regular sequences.

## Questions

```yaml
- question: "What is the global dimension of a field k?"
  type: multiple-choice
  options:
    - "0"
    - "1"
    - "Infinite"
    - "Undefined"
  answer: 0
  explanation: "Over a field, every module is free (hence projective), so every module has projective dimension 0. The global dimension is the supremum of all projective dimensions, which is 0. More generally, a ring has global dimension 0 if and only if it is semisimple (every module is projective)."

- question: "The projective dimension of Z/nZ as a Z-module is 1 for any n ≥ 2."
  type: true-false
  answer: true
  explanation: "The short exact sequence 0 → Z →^n Z → Z/nZ → 0 is a projective (in fact free) resolution of Z/nZ of length 1. Since Z/nZ is not projective (it is not a direct summand of a free Z-module, being finite), its projective dimension is exactly 1. Over a PID, every module has projective dimension at most 1."

- question: "State the Auslander-Buchsbaum formula and explain its significance."
  type: short-answer
  answer: "For a finitely generated module M of finite projective dimension over a Noetherian local ring (R, m): pd(M) + depth(M) = depth(R). It says projective dimension and depth are complementary measures of complexity, summing to a constant (the depth of the ring)."
  explanation: "The formula connects homological algebra (projective dimension, computed from resolutions) to commutative algebra (depth, computed from regular sequences). For instance, if R is Cohen-Macaulay of dimension d, and M has pd(M) = r, then depth(M) = d - r. The formula also proves that regular local rings have finite global dimension, since depth(R) = dim(R) bounds pd(M) for all M."

- question: "A Noetherian local ring is regular if and only if it has finite global dimension."
  type: true-false
  answer: true
  explanation: "This is Serre's theorem, proved using homological methods in the 1950s. The 'only if' direction: a regular local ring of dimension d has global dimension d (the residue field has a Koszul resolution of length d). The 'if' direction is deeper: finite global dimension implies the residue field has finite projective dimension, which forces the ring to be regular via the Auslander-Buchsbaum formula."

- question: "What is the global dimension of the polynomial ring k[x_1, ..., x_n] over a field?"
  type: short-answer
  answer: "n. The Hilbert syzygy theorem states that every finitely generated module over k[x_1, ..., x_n] has a free resolution of length at most n, and the residue field k = k[x_1,...,x_n]/(x_1,...,x_n) achieves this bound."
  explanation: "The Koszul complex on (x_1, ..., x_n) provides an explicit free resolution of k of length n. The Hilbert syzygy theorem is the global version: no module needs a longer resolution. This matches the Krull dimension n, consistent with the general fact that gl.dim(R) = dim(R) for regular rings."
```

## Explainer

**Homological dimension** quantifies the complexity of modules through resolutions. A **projective resolution** of an R-module M is an exact sequence ... → P_2 → P_1 → P_0 → M → 0 where each P_i is projective. The **projective dimension** pd(M) is the minimum length of such a resolution (or infinity if no finite resolution exists). Similarly, the **injective dimension** id(M) is the minimum length of an injective resolution 0 → M → E^0 → E^1 → .... The **global dimension** gl.dim(R) is the supremum of pd(M) over all R-modules M, equivalently the supremum of id(M) over all modules.

The **Auslander-Buchsbaum formula** is the central result connecting homological and commutative algebra. For a finitely generated module M over a Noetherian local ring (R, m), if pd(M) < ∞, then pd(M) + depth(M) = depth(R). This formula has immediate consequences: since depth(M) ≥ 0, we get pd(M) ≤ depth(R) ≤ dim(R), bounding projective dimension by the dimension of the ring. For a regular local ring of dimension d, depth(R) = d, so every finitely generated module has projective dimension at most d. The formula also shows that M is free (pd = 0) if and only if depth(M) = depth(R), a criterion used constantly in practice.

**Serre's theorem** is the crown jewel of homological commutative algebra: a Noetherian local ring (R, m) is regular if and only if gl.dim(R) < ∞. The forward direction constructs the Koszul complex on a regular system of parameters, giving an explicit free resolution of the residue field k = R/m of length dim(R). The reverse direction is deeper: if gl.dim(R) = d < ∞, then pd(k) = d, and the Auslander-Buchsbaum formula gives depth(R) = d. A careful analysis of Tor groups then shows dim_k(m/m^2) = d, which is the definition of regularity. Before Serre's theorem, it was not known whether the localization of a regular local ring is again regular. Serre's homological characterization made this immediate: localization cannot increase global dimension.

The **Hilbert syzygy theorem** is the global version for polynomial rings: every finitely generated module over k[x_1, ..., x_n] has a free resolution of length at most n. This is equivalent to saying gl.dim(k[x_1, ..., x_n]) = n. The theorem was originally proved by Hilbert using his basis theorem and explicit construction of syzygies (relations among generators). In modern terms, it follows from the fact that k[x_1, ..., x_n] localized at (x_1, ..., x_n) is a regular local ring of dimension n, combined with the fact that global dimension can be computed locally. The interplay between the Hilbert syzygy theorem, Serre's theorem, and the Auslander-Buchsbaum formula forms the homological backbone of modern commutative algebra, connecting abstract resolution theory to concrete invariants like depth and dimension.
