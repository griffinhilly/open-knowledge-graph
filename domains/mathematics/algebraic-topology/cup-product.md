---
id: cup-product
title: The Cup Product
domain: mathematics
course: algebraic-topology
prerequisites:
- id: singular-cohomology
  type: hard
- id: cochain-complexes-cohomology
  type: hard
builds-toward:
- poincare-duality
tags: [algebraic-topology, cup-product, cohomology-ring, multiplicative-structure]
stage: expert
status: validated
---
# The Cup Product

## Core Idea
The cup product is a bilinear operation H^p(X; R) x H^q(X; R) -> H^{p+q}(X; R) that gives the cohomology groups the structure of a graded ring. Defined at the cochain level by (f cup g)(sigma) = f(front p-face of sigma) * g(back q-face of sigma), the cup product is associative, has an identity (the class in H^0), and satisfies graded commutativity: alpha cup beta = (-1)^{pq} beta cup alpha. The resulting cohomology ring H^*(X; R) is a strictly finer topological invariant than the individual cohomology groups and distinguishes spaces that homology alone cannot.

## Questions

```yaml
- question: "CP^2 and S^2 ∨ S^4 have the same homology groups: H_0 = H_2 = H_4 = Z, all others zero. How does the cup product distinguish them?"
  type: multiple-choice
  options:
    - "The cup product on CP^2 has a generator α ∈ H^2 with α ∪ α ≠ 0 in H^4, while on S^2 ∨ S^4 all cup products of positive-degree classes are zero"
    - "The cup products are isomorphic but the spaces differ in homotopy groups"
    - "CP^2 has torsion in cohomology that S^2 ∨ S^4 does not"
    - "The cup product only distinguishes orientable from non-orientable spaces"
  answer: 0
  explanation: "H^*(CP^2; Z) ≅ Z[α]/(α^3) where α ∈ H^2 is a generator and α^2 generates H^4. The ring has a nontrivial product. H^*(S^2 ∨ S^4; Z) has generators β ∈ H^2 and γ ∈ H^4, but β^2 = 0 (it maps to H^4 of S^2, which is trivial) and β ∪ γ = 0 for dimensional reasons. The ring is a square-zero extension. This algebraic difference reflects a genuine topological difference: CP^2 cannot be decomposed as a wedge sum, while S^2 ∨ S^4 is explicitly built as one."

- question: "The cup product is graded commutative: α ∪ β = (-1)^{pq} β ∪ α for α ∈ H^p and β ∈ H^q."
  type: true-false
  answer: true
  explanation: "Graded commutativity (also called supercommutativity) means that swapping two classes introduces a sign that depends on their degrees. For two even-degree classes, the product commutes. For two odd-degree classes, the product anti-commutes: α ∪ α = -α ∪ α, which implies 2(α ∪ α) = 0 (so α^2 is 2-torsion or zero). This sign convention arises naturally from the combinatorics of the front-face/back-face decomposition and is compatible with the Koszul sign rule that pervades graded algebra."

- question: "At the cochain level, the cup product of f ∈ C^p and g ∈ C^q is defined by (f ∪ g)(σ) = f(σ|[v_0,...,v_p]) · g(σ|[v_p,...,v_{p+q}]). Why does this descend to a well-defined operation on cohomology?"
  type: multiple-choice
  options:
    - "Because the coboundary of a cup product satisfies the Leibniz rule: d(f ∪ g) = (df) ∪ g + (-1)^p f ∪ (dg)"
    - "Because all cochains are cocycles"
    - "Because the cup product commutes with all chain maps"
    - "Because Hom is an exact functor"
  answer: 0
  explanation: "The Leibniz rule d(f ∪ g) = (df) ∪ g + (-1)^p f ∪ (dg) is the key identity. It implies: if f and g are cocycles (df = 0, dg = 0), then d(f ∪ g) = 0, so the cup product of cocycles is a cocycle. Furthermore, if f is a coboundary (f = dh), then f ∪ g = (dh) ∪ g = d(h ∪ g) - (-1)^{p-1} h ∪ (dg) = d(h ∪ g) when g is a cocycle, so the cup product of a coboundary with a cocycle is a coboundary. Therefore the cup product descends to cohomology."

- question: "Explain why the cup product makes cohomology a strictly finer invariant than homology for distinguishing topological spaces."
  type: short-answer
  answer: "Cohomology groups, as abelian groups, carry the same information as homology groups (related by the universal coefficient theorem). But the cup product introduces multiplicative relationships between classes in different degrees that have no homological analogue. Two spaces can have isomorphic cohomology groups in every degree but non-isomorphic cohomology rings, because the cup product structure detects how cohomology classes 'interact.' This multiplicative structure encodes topological features like the linking and intersection of submanifolds, the non-decomposability of spaces, and the complexity of fiber bundle structures."
  explanation: "The classic example — CP^2 vs S^2 ∨ S^4 — shows this concretely. Both have the same graded group Z ⊕ 0 ⊕ Z ⊕ 0 ⊕ Z, but the ring structures differ. There is no ring homomorphism between Z[α]/(α^3) and Z[β, γ]/(β^2, βγ, γ^2) that preserves degree, so the spaces are distinguishable. No amount of information about individual homology/cohomology groups can capture this difference."
```

## Explainer

The **cup product** gives cohomology a multiplicative structure that transforms H^*(X; R) = direct sum H^n(X; R) from a sequence of abelian groups into a graded ring. At the cochain level, for f in C^p(X; R) and g in C^q(X; R), the cup product f cup g in C^{p+q}(X; R) is defined on a singular (p+q)-simplex sigma : Delta^{p+q} -> X by (f cup g)(sigma) = f(sigma|_{[v_0, ..., v_p]}) * g(sigma|_{[v_p, ..., v_{p+q}]}). Here sigma|_{[v_0, ..., v_p]} is the front p-face (restriction to the first p+1 vertices) and sigma|_{[v_p, ..., v_{p+q}]} is the back q-face (restriction to the last q+1 vertices). The product of the values in R uses the ring multiplication.

The cup product descends to cohomology because of the **Leibniz rule** (also called the derivation property): d(f cup g) = (df) cup g + (-1)^p f cup (dg). This formula implies that the cup product of two cocycles is a cocycle, and that the cup product of a cocycle with a coboundary (or vice versa) is a coboundary. Therefore the operation [f] cup [g] = [f cup g] is well-defined on cohomology classes and is independent of the choice of cocycle representatives. The resulting operation H^p(X; R) x H^q(X; R) -> H^{p+q}(X; R) is bilinear, associative, and has a two-sided identity (the class 1 in H^0(X; R) = R for connected X).

A crucial property is **graded commutativity**: for alpha in H^p and beta in H^q, we have alpha cup beta = (-1)^{pq} beta cup alpha. When both p and q are even, the product commutes. When both are odd, it anti-commutes. This is proved at the cochain level using chain homotopies that relate the front-face/back-face decomposition to its reverse. Graded commutativity has important consequences: if alpha in H^p with p odd, then alpha cup alpha = -alpha cup alpha, so 2(alpha cup alpha) = 0. Over Z, this means alpha^2 is 2-torsion (or zero). Over Z/2Z, the distinction between commutativity and anti-commutativity disappears, which is why mod-2 cohomology is often technically simpler.

The cup product is **natural** with respect to continuous maps: for f : X -> Y, we have f*(alpha cup beta) = f*(alpha) cup f*(beta). This means f* : H^*(Y; R) -> H^*(X; R) is a ring homomorphism. This is a significant strengthening of functoriality: not only does f induce a group homomorphism in each degree, it preserves the entire multiplicative structure. The ring homomorphism property is the reason the cup product is such a powerful invariant — it provides additional constraints that any continuous map must satisfy.

The power of the cup product as a topological invariant is illustrated by the standard example of CP^2 versus S^2 wedge S^4. Both spaces have identical cohomology groups (Z in degrees 0, 2, and 4; zero elsewhere). But the cohomology ring of CP^2 is Z[alpha]/(alpha^3), where alpha in H^2 is a generator and alpha^2 is the nonzero generator of H^4. The cohomology ring of S^2 wedge S^4 is Z[beta, gamma]/(beta^2, beta*gamma, gamma^2), where beta in H^2 and gamma in H^4 are generators and all products of positive-degree elements vanish. These rings are not isomorphic: in one, the degree-4 generator is a square of the degree-2 generator; in the other, it is independent. This algebraic difference reflects a genuine topological difference and cannot be detected by any invariant that looks only at individual homology groups.
