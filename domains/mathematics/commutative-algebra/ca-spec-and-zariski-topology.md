---
id: ca-spec-and-zariski-topology
title: Spec and the Zariski Topology
domain: mathematics
course: commutative-algebra
prerequisites:
- id: ca-prime-and-maximal-ideals
  type: hard
- id: ca-localization
  type: hard
- id: ca-ideal-operations
  type: soft
builds-toward: []
tags:
- spectrum
- zariski-topology
- structure-sheaf
- affine-scheme
- generic-point
- irreducible
- locally-ringed-space
stage: expert
status: validated
---

# Spec and the Zariski Topology

## Core Idea
The prime spectrum Spec R of a commutative ring R, equipped with the Zariski topology and the structure sheaf O_X, is an affine scheme -- the fundamental geometric object in modern algebraic geometry. Closed sets correspond to radical ideals via V(I) = {P in Spec R : P ⊇ I}, and the distinguished open sets D(f) = {P : f not in P} form a basis. The structure sheaf assigns to each open set U the ring of "functions regular on U," with stalks O_{X,P} = R_P (the localization at P). This construction transforms commutative algebra into geometry, with ring homomorphisms becoming continuous maps and localization becoming restriction to open sets.

## Questions

```yaml
- question: "What are the points of Spec Z?"
  type: multiple-choice
  options:
    - "The positive integers"
    - "The prime numbers 2, 3, 5, 7, ... together with the generic point (0)"
    - "The maximal ideals (2), (3), (5), ... only"
    - "The elements of Z"
  answer: 1
  explanation: "Spec Z consists of all prime ideals of Z: the zero ideal (0) and the ideals (p) for each prime number p. The point (0) is the 'generic point' -- its closure is all of Spec Z. The points (p) are the closed points (maximal ideals). The topology has closed sets V(n) = {(p) : p divides n} for each integer n."

- question: "In the Zariski topology on Spec R, the closed sets are exactly the sets of the form V(I) for some ideal I."
  type: true-false
  answer: true
  explanation: "The Zariski topology is defined by declaring V(I) = {P in Spec R : P ⊇ I} to be closed for each ideal I. One verifies: V(R) = ∅, V(0) = Spec R, V(∩I_α) = ∪V(I_α), and V(I + J) = V(I) ∩ V(J). Moreover, V(I) = V(√I), so closed sets correspond bijectively to radical ideals."

- question: "Describe the Zariski topology on Spec k[x] where k is an algebraically closed field."
  type: short-answer
  answer: "Spec k[x] has one generic point (0) and closed points (x - a) for each a in k. The closed sets are: all of Spec k[x], finite sets of closed points, and the empty set. The generic point (0) is dense -- it lies in every nonempty open set."
  explanation: "Since k[x] is a PID over an algebraically closed field, the nonzero primes are (x - a) for a in k (the maximal ideals). The closed sets V(f) for nonzero f consist of the finitely many (x - a) where a is a root of f. So the topology on closed points is the cofinite topology. The generic point (0) has closure V(0) = Spec k[x], making it dense."

- question: "The stalk of the structure sheaf O_X at a prime P in Spec R is the local ring R_P."
  type: true-false
  answer: true
  explanation: "The structure sheaf is defined so that O_X(D(f)) = R_f (the localization inverting f), and the stalk at P is the direct limit over all open neighborhoods of P, which computes to R_P (the localization at the complement of P). This is the key property making (Spec R, O_X) a locally ringed space."

- question: "Explain what it means for Spec R to be irreducible and relate this to a property of R."
  type: short-answer
  answer: "Spec R is irreducible (not the union of two proper closed subsets) if and only if the nilradical √(0) is a prime ideal. For a reduced ring (no nilpotents), this is equivalent to R being a domain. An irreducible Spec R has a unique generic point, namely the nilradical."
  explanation: "If Spec R = V(I) ∪ V(J) with neither equal to Spec R, then IJ ⊆ √(0) but neither I nor J is in √(0), contradicting primality. Conversely, if √(0) is prime, any decomposition Spec R = V(I) ∪ V(J) = V(IJ) forces IJ ⊆ √(0), so I or J lies in √(0), making one factor all of Spec R. The generic point η = √(0) is the unique point whose closure is Spec R."
```

## Explainer

The **prime spectrum** Spec R of a commutative ring R is the set of all prime ideals of R, equipped with the **Zariski topology**. The closed sets are V(I) = {P in Spec R : P ⊇ I} for ideals I of R, and V establishes an inclusion-reversing bijection between radical ideals of R and closed subsets of Spec R. The open sets D(f) = Spec R \\ V(f) = {P : f not in P} for elements f in R form a basis of the topology. The resulting topological space is generally not Hausdorff -- in fact, the closure of a point P is V(P), so a point is closed if and only if P is a maximal ideal. Non-maximal primes have non-trivial closures and serve as "generic points" of irreducible closed subsets.

The topology alone loses too much information -- many non-isomorphic rings can have homeomorphic spectra. The essential additional datum is the **structure sheaf** O_X, which assigns to each open set U a ring O_X(U) of "regular functions on U." On the basic open sets, O_X(D(f)) = R_f (the localization of R inverting f). The stalk at a point P is O_{X,P} = R_P, the localization at P, which is a local ring. The pair (Spec R, O_X) is a **locally ringed space** called an **affine scheme**, and the category of affine schemes is contravariantly equivalent to the category of commutative rings. This equivalence -- Grothendieck's fundamental insight -- means every theorem in commutative algebra has a geometric translation and vice versa.

Ring-theoretic properties translate into geometric properties of Spec R through this dictionary. R is a domain if and only if Spec R is irreducible (when R is reduced). R is Noetherian if and only if Spec R is a Noetherian topological space (every descending chain of closed sets stabilizes). The Krull dimension of R equals the topological dimension of Spec R (the supremum of lengths of chains of irreducible closed subsets). Localization at a prime P corresponds to passing to the local ring at P -- "zooming in" on the point P. The residue field R_P/PR_P at P is the "function field" at that point.

The Zariski topology has peculiar properties from the viewpoint of general topology -- it is almost never Hausdorff, and it is quasi-compact (every open cover has a finite subcover) by a direct argument using the fact that D(f) sets form a basis. But for algebraic geometry, these properties are features, not bugs. The non-Hausdorff nature allows generic points, which encode the function field of an irreducible variety. Quasi-compactness is the scheme-theoretic analogue of "affine varieties are determined by finitely many equations." The construction generalizes: gluing affine schemes along open subsets produces general **schemes**, and the entire edifice of modern algebraic geometry -- coherent sheaves, cohomology, moduli spaces -- is built on this foundation of Spec, the Zariski topology, and the structure sheaf.
