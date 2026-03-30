---
id: lefschetz-fixed-point-theorem
title: The Lefschetz Fixed Point Theorem
domain: mathematics
course: algebraic-topology
prerequisites:
- id: degree-theory-maps-spheres
  type: hard
- id: brouwer-fixed-point-theorem-homological
  type: hard
- id: euler-characteristic-homology
  type: hard
- id: singular-homology-groups
  type: hard
builds-toward: []
tags: [algebraic-topology, lefschetz-number, fixed-points, trace, applications]
stage: expert
status: validated
---
# The Lefschetz Fixed Point Theorem

## Core Idea
The Lefschetz fixed point theorem generalizes the Brouwer fixed point theorem from disks to arbitrary compact polyhedra. For a continuous map f : X -> X on a compact triangulable space, the Lefschetz number L(f) = sum(-1)^n tr(f_* : H_n(X; Q) -> H_n(X; Q)) is defined as the alternating sum of traces of the induced maps on rational homology. If L(f) != 0, then f has at least one fixed point. The Brouwer theorem is the special case X = D^n, where L(f) = 1 for any f (since D^n is contractible).

## Questions

```yaml
- question: "A map f: S^2 → S^2 has degree 3. What is its Lefschetz number, and does it have a fixed point?"
  type: multiple-choice
  options:
    - "L(f) = 4, so f has a fixed point"
    - "L(f) = 2, so f has a fixed point"
    - "L(f) = 0, so the theorem gives no information"
    - "L(f) = 1 - 0 + 3 = 4, so f has a fixed point"
  answer: 3
  explanation: "H_0(S^2) = Z (f_* is identity, trace = 1), H_1(S^2) = 0 (trace = 0), H_2(S^2) = Z (f_* is multiplication by 3, trace = 3). So L(f) = 1 - 0 + 3 = 4 ≠ 0. By the Lefschetz theorem, f has a fixed point. In fact, L(f) = 1 + (-1)^n · deg(f) = 1 + deg(f) for maps of S^n (since f_* on H_0 always has trace 1 and on H_n has trace deg(f)). For S^2: L(f) = 1 + deg(f)."

- question: "The Lefschetz number of the identity map id: X → X equals the Euler characteristic χ(X)."
  type: true-false
  answer: true
  explanation: "For the identity map, the induced map id_* on each H_n(X; Q) is the identity, whose trace equals the dimension dim_Q(H_n(X; Q)) = b_n (the n-th Betti number). So L(id) = Σ(-1)^n b_n = χ(X). This connects the Lefschetz fixed point theorem to the Euler characteristic: if χ(X) ≠ 0, then the identity map has a fixed point — which is trivially true (every point is fixed). The nontrivial content is for maps OTHER than the identity."

- question: "The antipodal map a: S^{2k} → S^{2k} on an even-dimensional sphere has L(a) = 1 + (-1)^{2k}(-1)^{2k+1} = 1 - 1 = 0. Does this mean the antipodal map has a fixed point?"
  type: multiple-choice
  options:
    - "Yes, L(a) = 0 forces a fixed point"
    - "No, L(a) = 0 means the theorem gives no information — and indeed the antipodal map has NO fixed points"
    - "Yes, because the Euler characteristic of S^{2k} is 2"
    - "No, because deg(a) = -1"
  answer: 1
  explanation: "L(a) = 0 means the Lefschetz theorem is inconclusive — it does NOT assert that fixed points exist or don't exist. In this case, the antipodal map a(x) = -x on S^{2k} indeed has no fixed points (a(x) = x would require x = -x, only possible for x = 0 which is not on the sphere). So the theorem correctly gives no information. The converse of the Lefschetz theorem is false: L(f) = 0 does not imply f is fixed-point-free."

- question: "A continuous map f: T^2 → T^2 on the torus induces f_*: H_1(T^2; Q) → H_1(T^2; Q), which is a 2×2 matrix A with integer entries. Express L(f) in terms of A."
  type: short-answer
  answer: "L(f) = tr(f_*|H_0) - tr(f_*|H_1) + tr(f_*|H_2). On H_0 ≅ Q, f_* is the identity (trace 1). On H_1 ≅ Q^2, f_* is the matrix A (trace = tr(A)). On H_2 ≅ Q, f_* is multiplication by det(A) (the map on the top homology of an oriented surface is multiplication by the determinant of the map on H_1). So L(f) = 1 - tr(A) + det(A)."
  explanation: "For the torus, the formula L(f) = 1 - tr(A) + det(A) where A is the 2×2 matrix of f_* on H_1 is explicit and computable. For example, the identity has A = I, giving L = 1 - 2 + 1 = 0 — consistent with the fact that translations on the torus are fixed-point-free and homotopic to the identity (and χ(T^2) = 0). A map with A = [[2,0],[0,2]] has L = 1 - 4 + 4 = 1 ≠ 0, so it must have a fixed point."
```

## Explainer

The **Lefschetz fixed point theorem** is a far-reaching generalization of the Brouwer fixed point theorem. Where Brouwer applies only to the disk (or more generally, convex compact sets), the Lefschetz theorem works for any compact triangulable space X and gives a numerical criterion for the existence of fixed points. The key quantity is the **Lefschetz number** L(f) = sum_{n >= 0} (-1)^n tr(f_{*,n}), where f_{*,n} : H_n(X; Q) -> H_n(X; Q) is the induced map on rational homology and tr denotes the trace of the linear map.

The theorem states: if L(f) != 0, then f has at least one fixed point. The contrapositive — if f is fixed-point-free, then L(f) = 0 — is often more useful for showing that certain maps MUST have fixed points. The converse is false: L(f) = 0 does not guarantee that f is fixed-point-free (translations on the torus have L = 0 but the identity is the only fixed-point-free map with L = 0 up to homotopy considerations).

**Recovery of Brouwer's theorem**: for X = D^n (the closed disk), H_0(D^n; Q) = Q and H_k(D^n; Q) = 0 for k > 0. Any map f : D^n -> D^n induces f_* = id on H_0 (since D^n is connected), so L(f) = tr(id) = 1 != 0. Therefore every continuous self-map of the disk has a fixed point — Brouwer's theorem.

For **maps of spheres** f : S^n -> S^n with degree d: H_0 = Q (trace 1), H_n = Q (trace d), all others zero. So L(f) = 1 + (-1)^n d. For n even: L(f) = 1 + d, which is zero only when d = -1. For n odd: L(f) = 1 - d, which is zero only when d = 1. The antipodal map on S^{2k} has degree (-1)^{2k+1} = -1, giving L = 0, consistent with the antipodal map being fixed-point-free. The antipodal map on S^{2k+1} has degree (-1)^{2k+2} = 1, giving L = 0 as well — and indeed the antipodal map on odd spheres is homotopic to the identity via rotation and need not have a fixed point (though it happens to be fixed-point-free).

The proof of the Lefschetz theorem uses the **simplicial approximation** of f and a careful count of coincidences between the map and the identity on each simplex. The trace of f_* on homology, by the Hopf trace formula, equals an alternating sum of "local fixed point indices" whenever the fixed points are isolated — the Lefschetz number is a global algebraic count of fixed points, with each fixed point weighted by a local index. When this algebraic count is nonzero, there must be at least one genuine fixed point. The theorem connects beautifully to the Euler characteristic (L(id) = chi(X)), to degree theory (via the trace on top homology), and to the Atiyah-Bott fixed point theorem in differential geometry (a smooth generalization using the Dolbeault complex). It is one of the most satisfying results in algebraic topology, demonstrating how global topological information (the traces on homology) constrains the local behavior (existence of fixed points) of continuous maps.
