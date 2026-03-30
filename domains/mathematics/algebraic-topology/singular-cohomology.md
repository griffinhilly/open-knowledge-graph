---
id: singular-cohomology
title: Singular Cohomology
domain: mathematics
course: algebraic-topology
prerequisites:
- id: cochain-complexes-cohomology
  type: hard
- id: singular-homology-groups
  type: hard
builds-toward:
- cup-product
- universal-coefficient-theorem
- poincare-duality
tags: [algebraic-topology, singular-cohomology, topological-invariants, duality]
stage: expert
status: validated
---
# Singular Cohomology

## Core Idea
Singular cohomology H^n(X; G) is defined by applying Hom(-, G) to the singular chain complex of X. It inherits all the computational tools of singular homology (long exact sequences, Mayer-Vietoris, excision) in dualized form, with arrows reversed. Singular cohomology is the natural home for duality theorems, multiplicative structures, and obstruction theory. Its pairing with homology via the Kronecker pairing provides a bridge between the two theories.

## Questions

```yaml
- question: "The long exact sequence for the pair (X, A) in cohomology runs: ... → H^n(X, A; G) → H^n(X; G) → H^n(A; G) → H^{n+1}(X, A; G) → ... How do the arrows compare to the homology long exact sequence?"
  type: multiple-choice
  options:
    - "The arrows point in the same direction as in homology"
    - "The arrows between spaces are reversed (maps go from the larger space to the subspace), and the connecting homomorphism increases dimension by 1 instead of decreasing it"
    - "Only the connecting homomorphism changes direction"
    - "The cohomology sequence is not exact"
  answer: 1
  explanation: "In homology, the long exact sequence has i_*: H_n(A) → H_n(X) (inclusion pushes forward) and ∂: H_n(X,A) → H_{n-1}(A) (connecting homomorphism decreases dimension). In cohomology, the Hom functor reverses arrows: i*: H^n(X) → H^n(A) (restriction to subspace pulls back), and the connecting homomorphism δ: H^n(A) → H^{n+1}(X,A) increases dimension. Cohomology is contravariant — it pulls back along maps rather than pushing forward."

- question: "The Kronecker pairing ⟨−, −⟩: H^n(X; Z) × H_n(X; Z) → Z is defined by evaluating a cocycle on a cycle. This pairing is always a perfect pairing (non-degenerate on both sides)."
  type: true-false
  answer: false
  explanation: "The Kronecker pairing is well-defined and natural, but it is NOT a perfect pairing in general. When H_n(X) has torsion, the pairing has a nontrivial kernel on the cohomology side: torsion elements in H^n pair trivially with all cycles. The universal coefficient theorem makes this precise: the free part of H^n pairs perfectly with the free part of H_n, but torsion in H^n comes from H_{n-1} and does not pair with H_n at all. Over a field, the pairing IS perfect."

- question: "Singular cohomology is contravariant: a continuous map f: X → Y induces f*: H^n(Y) → H^n(X), reversing the direction."
  type: true-false
  answer: true
  explanation: "A continuous map f: X → Y induces a chain map f_#: C_n(X) → C_n(Y) (by composition: σ ↦ f ∘ σ). Applying Hom(−, G) reverses the arrow: f^#: C^n(Y) → C^n(X) is defined by f^#(φ) = φ ∘ f_# (precomposition). This induces f*: H^n(Y) → H^n(X) on cohomology. Contravariance is essential: the cup product on H^*(X) is natural with respect to pullback (f*(α ∪ β) = f*(α) ∪ f*(β)), which would not work covariantly."

- question: "Compute H^*(S^n; Z) and explain why the cohomology ring structure is trivial for spheres."
  type: short-answer
  answer: "H^k(S^n; Z) = Z for k = 0 and k = n, and 0 otherwise (same as homology, since the homology groups are free abelian and the universal coefficient theorem gives an isomorphism). The cohomology ring H^*(S^n; Z) ≅ Z[α]/(α^2) where α ∈ H^n is the generator: the only possible cup product of positive-degree classes would be α ∪ α ∈ H^{2n}(S^n), but H^{2n}(S^n) = 0 for dimensional reasons (2n > n when n > 0), so α^2 = 0. The ring structure is 'trivial' in the sense that all products of positive-degree classes vanish."
  explanation: "This triviality is specific to spheres and is a consequence of having cohomology concentrated in just two degrees. Compare with CP^n, which has H^*(CP^n; Z) ≅ Z[α]/(α^{n+1}) with α ∈ H^2 — here α^k ≠ 0 for k ≤ n, giving a rich ring structure. The cup product becomes a powerful distinguishing invariant precisely for spaces whose cohomology is spread across multiple degrees."
```

## Explainer

**Singular cohomology** with coefficients in an abelian group G is constructed by dualizing the singular chain complex: C^n(X; G) = Hom(C_n(X), G), the group of all homomorphisms from the singular n-chain group to G. A singular n-cochain assigns an element of G to each singular n-simplex in X. The coboundary d^n : C^n -> C^{n+1} is defined by (d^n f)(sigma) = f(d_{n+1} sigma), and the cohomology groups H^n(X; G) = ker(d^n)/im(d^{n-1}) measure the failure of cocycles (cochains vanishing on boundaries) to be coboundaries.

All the computational tools of singular homology have cohomological counterparts, obtained by applying Hom and using the functorial properties. There is a **long exact sequence** for pairs: ... -> H^n(X, A) -> H^n(X) -> H^n(A) -> H^{n+1}(X, A) -> ..., with arrows reversed relative to the homology version. There is a **Mayer-Vietoris sequence** for cohomology: ... -> H^n(X) -> H^n(A) direct sum H^n(B) -> H^n(A intersect B) -> H^{n+1}(X) -> ..., again with reversed arrows. Excision holds for cohomology (it is inherited from the chain-level excision). These tools are used to compute cohomology in exactly the same way as their homological counterparts, with the direction of maps reversed throughout.

The **contravariance** of cohomology — the fact that a map f : X -> Y induces f* : H^n(Y) -> H^n(X) in the reverse direction — is not a defect but a feature. It means cohomology classes are "pulled back" along maps, which is the correct behavior for quantities that assign values to cycles. A differential form on Y (in the de Rham setting) pulls back to a differential form on X via f; a characteristic class of a vector bundle pulls back to a characteristic class of the pullback bundle. Contravariance is natural for "measurement" or "evaluation" type quantities, which is why cohomology (not homology) is the correct framework for obstruction theory, characteristic classes, and sheaf theory.

The **Kronecker pairing** <,> : H^n(X; G) x H_n(X; Z) -> G, defined by evaluating a cocycle representative on a cycle representative, gives a natural bilinear map between cohomology and homology. When G = Z and the homology is free abelian, this pairing identifies H^n(X; Z) with Hom(H_n(X; Z), Z), the algebraic dual. When there is torsion, the universal coefficient theorem introduces a correction term from Ext. Over a field, cohomology and homology are perfectly dual, but over Z, the torsion information in cohomology comes from the torsion of H_{n-1} (shifted by one degree), giving cohomology a slightly different "view" of the same space.

The most important distinguishing feature of singular cohomology is that it carries a natural **ring structure** via the cup product, which will be developed in the next topic. This ring structure makes H^*(X) a graded ring, and the ring structure is a strictly finer invariant than the individual cohomology groups — spaces with isomorphic cohomology groups can have non-isomorphic cohomology rings. The cup product is the reason cohomology, rather than homology, is the primary algebraic tool in much of modern topology.
