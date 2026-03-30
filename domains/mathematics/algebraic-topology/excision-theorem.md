---
id: excision-theorem
title: The Excision Theorem
domain: mathematics
course: algebraic-topology
prerequisites:
- id: relative-homology-long-exact-sequence
  type: hard
- id: singular-homology-groups
  type: hard
builds-toward:
- mayer-vietoris-sequence
- cellular-homology
tags: [algebraic-topology, excision, relative-homology, computation]
stage: expert
status: validated
---
# The Excision Theorem

## Core Idea
The excision theorem states that if Z is a subspace of A whose closure is contained in the interior of A, then the inclusion (X \ Z, A \ Z) -> (X, A) induces isomorphisms H_n(X \ Z, A \ Z) = H_n(X, A) for all n. In other words, we can "cut out" (excise) the subspace Z from both X and A without changing the relative homology. This theorem is what gives homology its local-to-global computational power: relative homology depends only on the behavior near the boundary of A in X, not on what happens deep inside A or far from A.

## Questions

```yaml
- question: "The excision theorem says H_n(X \\ Z, A \\ Z) ≅ H_n(X, A) provided that the closure of Z is contained in the interior of A. Why is this condition necessary?"
  type: multiple-choice
  options:
    - "It ensures that Z does not touch the boundary of A, so removing Z does not change the topology near where A meets X \\ A"
    - "It ensures that X \\ Z is still a topological space"
    - "It ensures the chain groups remain finitely generated"
    - "It ensures that A \\ Z is contractible"
  answer: 0
  explanation: "The condition cl(Z) ⊂ int(A) ensures that Z is 'buried deep inside A,' far from the boundary where A meets its complement in X. Relative homology H_n(X, A) is sensitive to the topology near the boundary of A in X — it measures what happens in X that does not already happen in A. Removing Z from deep inside A changes neither the space near this boundary nor the relative chains that detect it. Without this condition, Z might intersect the boundary of A, genuinely altering the relative topology."

- question: "Excision implies that for a good pair (X, A), the relative homology H_n(X, A) is isomorphic to the reduced homology H̃_n(X/A)."
  type: true-false
  answer: true
  explanation: "For good pairs (where A is a neighborhood deformation retract), excision and the long exact sequence combine to show H_n(X, A) ≅ H̃_n(X/A). Intuitively: collapsing A to a point is the geometric version of 'modding out by A,' and relative homology is the algebraic version. Excision provides the key step by showing that the homology only sees the local behavior near the boundary of A. This result is foundational for cellular homology, where H_n(X^n, X^{n-1}) ≅ H̃_n(X^n/X^{n-1}) ≅ H̃_n(∨S^n) detects the n-cells."

- question: "In the proof of the Mayer-Vietoris sequence, excision plays which role?"
  type: multiple-choice
  options:
    - "It shows the boundary maps are zero"
    - "It identifies the relative homology H_n(X, A) with H_n(B, A ∩ B), connecting the homology of the pieces"
    - "It proves that the chain groups are free abelian"
    - "It establishes functoriality of homology"
  answer: 1
  explanation: "The Mayer-Vietoris sequence for X = A ∪ B is derived from the long exact sequence of the pair (X, A). Excision provides the crucial identification: H_n(X, A) ≅ H_n(B, A ∩ B) (excising Z = X \\ B from the pair (X, A), noting that cl(X \\ B) ⊆ int(A) when {int(A), int(B)} cover X). This identification converts the long exact sequence of (X, A) into the Mayer-Vietoris sequence, which involves only the homology groups of A, B, and A ∩ B."

- question: "Explain why excision makes homology 'local' in a way that homotopy groups are not."
  type: short-answer
  answer: "Excision says that relative homology H_n(X, A) is insensitive to changes deep inside A or far from A — it depends only on the local topology near the boundary where A meets X \\ A. This is a locality property that homotopy groups do not share: π_n(X, A) does not satisfy excision in general (the failure of excision for homotopy groups is related to the Freudenthal suspension theorem and is measured by higher connectivity conditions). Homology's local character is what makes it computationally powerful — we can decompose spaces into pieces and compute the homology of each piece independently."
  explanation: "The difference is fundamental. Homology is an 'abelian' invariant (the chain groups are abelian), and abelianization introduces the locality that excision captures. Homotopy groups, being non-abelian in general, carry global information that cannot be localized. This is why homology is easier to compute (excision + Mayer-Vietoris give systematic decomposition methods) while homotopy groups resist computation (the homotopy groups of spheres remain only partially known)."
```

## Explainer

The **excision theorem** is one of the Eilenberg-Steenrod axioms for homology theories, and it is the property that gives homology its remarkable computational power. The precise statement: if (X, A) is a pair and Z is a subset of A with cl(Z) contained in int(A), then the inclusion map (X \ Z, A \ Z) hookrightarrow (X, A) induces isomorphisms H_n(X \ Z, A \ Z) -> H_n(X, A) for all n. Equivalently (and often more useful in practice): if X = A union B with int(A) and int(B) covering X, then the inclusion (B, A intersect B) hookrightarrow (X, A) induces isomorphisms H_n(B, A intersect B) -> H_n(X, A).

The intuition behind excision is that relative homology H_n(X, A) measures the topology of X in the neighborhood of the "boundary" between A and its complement X \ A. What happens deep inside A is invisible (it is already quotiented out), and what happens far from A in X contributes nothing to the relative chains (which must have boundaries in A). Therefore, cutting out a piece Z that is buried deep inside A has no effect on the relative homology. The formal proof uses the technique of **barycentric subdivision**: singular chains can be subdivided into smaller and smaller pieces until every singular simplex maps either entirely into A or entirely into B = X \ Z, allowing chains to be decomposed into local contributions. This subdivision process does not change homology (subdivided chains are homologous to the originals), and once chains are local, the excision isomorphism follows.

The most important consequence of excision is the identification H_n(X, A) = reduced H_n(X/A) for good pairs (pairs where A is a neighborhood deformation retract in X). The proof: let X/A be the quotient space obtained by collapsing A to a point p. Then H_n(X/A, p) = H_n(X/A) for n > 0 (since a point has trivial higher homology). Excision (in the equivalent formulation) identifies H_n(X, A) with H_n(X/A, A/A) = H_n(X/A, p). This identification makes relative homology geometric: H_n(X, A) measures the holes in X that survive when we crush A to a point.

Excision is the engine behind the **Mayer-Vietoris sequence**. Given X = A union B with open cover, the long exact sequence of the pair (X, A) involves H_n(X, A). Excision identifies H_n(X, A) with H_n(B, A intersect B) (excise Z = X \ B). Substituting this into the long exact sequence and rearranging gives the Mayer-Vietoris sequence: ... -> H_n(A intersect B) -> H_n(A) direct sum H_n(B) -> H_n(X) -> H_{n-1}(A intersect B) -> ... This sequence allows computation of H_n(X) from the homology of the pieces A, B, and their intersection. Similarly, excision underlies **cellular homology**: the relative group H_n(X^n, X^{n-1}) for a CW complex is computed by excising the (n-2)-skeleton, reducing to a wedge of spheres and giving H_n(X^n, X^{n-1}) = Z^{number of n-cells}. Without excision, neither of these fundamental computational tools would exist.
