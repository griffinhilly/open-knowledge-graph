---
id: borsuk-ulam-theorem
title: The Borsuk-Ulam Theorem
domain: mathematics
course: algebraic-topology
prerequisites:
- id: degree-theory-maps-spheres
  type: hard
- id: singular-homology-groups
  type: hard
- id: homotopy-exact-sequence-fibration
  type: soft
builds-toward:
- jordan-curve-theorem-homological
tags: [algebraic-topology, borsuk-ulam, antipodal-maps, applications]
stage: expert
status: validated
---
# The Borsuk-Ulam Theorem

## Core Idea
The Borsuk-Ulam theorem states that for every continuous map f : S^n -> R^n, there exists a point x in S^n such that f(x) = f(-x): some pair of antipodal points must map to the same value. Equivalently, there is no continuous map S^n -> S^{n-1} that commutes with the antipodal map. This theorem has striking consequences: it implies the ham sandwich theorem (any n measurable sets in R^n can be simultaneously bisected by a single hyperplane) and that at any moment, there exist two antipodal points on Earth with identical temperature and pressure.

## Questions

```yaml
- question: "The Borsuk-Ulam theorem for n = 1 says: every continuous map f: S^1 → R has f(x) = f(-x) for some x. This is a consequence of which elementary theorem?"
  type: multiple-choice
  options:
    - "The mean value theorem"
    - "The intermediate value theorem, applied to g(x) = f(x) - f(-x)"
    - "The Bolzano-Weierstrass theorem"
    - "The extreme value theorem"
  answer: 1
  explanation: "Define g(x) = f(x) - f(-x). Then g(-x) = f(-x) - f(x) = -g(x), so g is an odd function on S^1. Since g is continuous and g(-x) = -g(x), if g(x_0) > 0 for some x_0, then g(-x_0) < 0, and by the intermediate value theorem (applied to g along any path from x_0 to -x_0), there exists a point where g = 0, meaning f(x) = f(-x). The higher-dimensional version requires algebraic topology because the intermediate value theorem does not generalize directly."

- question: "The Borsuk-Ulam theorem implies that no subset of R^n is homeomorphic to S^n."
  type: true-false
  answer: true
  explanation: "If S^n embedded in R^n, the inclusion would give a continuous injection i: S^n → R^n. But Borsuk-Ulam says any continuous f: S^n → R^n must satisfy f(x) = f(-x) for some x ≠ -x. An injection cannot satisfy this (it maps distinct points to distinct values). Therefore no continuous injection S^n → R^n exists. This is a generalization of the invariance of domain: S^n cannot be 'flattened' into R^n without some pair of antipodal points colliding."

- question: "The ham sandwich theorem states: given n measurable sets in R^n, there exists a single hyperplane that simultaneously bisects all n sets. This follows from Borsuk-Ulam."
  type: true-false
  answer: true
  explanation: "A hyperplane in R^n is determined by a unit normal vector v ∈ S^{n-1} and an offset d ∈ R. For each v, there is a unique offset d_i(v) that bisects the i-th set. Define f: S^{n-1} → R^{n-1} by f(v) = (d_1(v) - d_n(v), ..., d_{n-1}(v) - d_n(v)). By Borsuk-Ulam applied to f: S^{n-1} → R^{n-1}, there exists v with f(v) = f(-v). Since d_i(-v) = -d_i(v) (reflecting the normal reverses the hyperplane), this gives d_i(v) - d_n(v) = -(d_i(v) - d_n(v)) for each i, forcing all differences to be zero. A careful argument then gives a hyperplane bisecting all n sets."

- question: "State the equivalent 'no equivariant map' formulation of the Borsuk-Ulam theorem and explain why it is equivalent to the antipodal coincidence version."
  type: short-answer
  answer: "Equivalent formulation: there is no continuous map g: S^n → S^{n-1} satisfying g(-x) = -g(x) (equivariant with respect to the antipodal action). Equivalence: if f: S^n → R^n had f(x) ≠ f(-x) for all x, then g(x) = (f(x) - f(-x))/|f(x) - f(-x)| would be a continuous equivariant map S^n → S^{n-1}. Conversely, an equivariant map g: S^n → S^{n-1} composed with the inclusion S^{n-1} ↪ R^n would give a map with no antipodal coincidence. So the two versions are contrapositives."
  explanation: "The equivariant formulation is often more useful for proofs. The nonexistence of equivariant maps S^n → S^{n-1} can be proved using the homology of real projective spaces (quotienting by the Z/2Z antipodal action) or using degree theory: an equivariant map would induce a map RP^n → RP^{n-1} with specific properties on homology that lead to a contradiction."
```

## Explainer

The **Borsuk-Ulam theorem** is one of the most elegant and applicable results in algebraic topology. The antipodal coincidence version states: for any continuous map f : S^n -> R^n, there exists a point x with f(x) = f(-x). In the n = 2 case, this has the beautiful meteorological interpretation: at any moment, there exist two antipodal points on the Earth's surface with identical temperature and atmospheric pressure (modeling temperature and pressure as continuous functions from S^2 to R^2).

The proof for general n uses the theory of the antipodal action on spheres and projective spaces. The Z/2Z-action on S^n given by x -> -x is free (no fixed points), and the quotient is real projective space RP^n = S^n / (x ~ -x). A continuous equivariant map g : S^n -> S^{n-1} (satisfying g(-x) = -g(x)) would descend to a continuous map g-bar : RP^n -> RP^{n-1} on the quotients. The key topological input is about the cohomology (or homology with Z/2Z coefficients) of projective spaces: H^k(RP^n; Z/2Z) = Z/2Z for 0 <= k <= n, and the generator alpha in H^1 satisfies alpha^n != 0 in H^n. The induced map g-bar^* would have to be an isomorphism on H^1 (by the equivariance condition), hence send alpha to alpha, and therefore send alpha^n != 0 to alpha^n. But alpha^n in H^n(RP^{n-1}; Z/2Z) = 0 (since RP^{n-1} has no cohomology in degree n). Contradiction.

The **ham sandwich theorem** is the most famous application. Given n measurable sets (or "ingredients") in R^n (think: bread, ham, cheese in R^3 for n = 3), there exists a single hyperplane that simultaneously bisects all n sets into equal-volume halves. The proof parametrizes hyperplanes by their normal direction on S^{n-1} and uses Borsuk-Ulam to find a direction where all n bisecting offsets agree. This result is used in computational geometry (fair division algorithms) and in measure theory.

Another important consequence is that S^n does not embed in R^n: any continuous map S^n -> R^n must send some pair of antipodal points to the same image, so no such map can be injective. This is a stronger statement than the invariance of dimension (which says R^n is not homeomorphic to R^m for n != m) and provides a clean topological obstruction to "dimensionally reducing" spheres.

The Borsuk-Ulam theorem also has discrete combinatorial analogues. The **necklace splitting problem** (splitting a necklace with n types of beads fairly between two people using at most n cuts) follows from a discrete version of Borsuk-Ulam. Tucker's lemma (a combinatorial analogue on triangulated spheres) is equivalent to the Borsuk-Ulam theorem and is used in fair division algorithms and computational complexity (the PPAD complexity class). These connections between continuous topology and discrete mathematics demonstrate the unexpected reach of the Borsuk-Ulam theorem beyond its original setting.
