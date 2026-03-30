---
id: jordan-curve-theorem-homological
title: Jordan Curve Theorem (Homological Proof)
domain: mathematics
course: algebraic-topology
prerequisites:
- id: singular-homology-groups
  type: hard
- id: mayer-vietoris-sequence
  type: hard
- id: excision-theorem
  type: soft
- id: borsuk-ulam-theorem
  type: soft
builds-toward: []
tags: [algebraic-topology, jordan-curve-theorem, separation, applications]
stage: expert
status: validated
---
# Jordan Curve Theorem (Homological Proof)

## Core Idea
The Jordan curve theorem states that every simple closed curve in the plane R^2 divides it into exactly two connected components (a bounded "inside" and an unbounded "outside"), with the curve as their common boundary. While intuitively obvious, the theorem is notoriously hard to prove for arbitrary continuous curves. The homological proof uses the Mayer-Vietoris sequence and the homology of S^2 to establish the separation property, generalizing naturally to the Jordan-Brouwer separation theorem: any embedded S^{n-1} in S^n separates S^n into exactly two components.

## Questions

```yaml
- question: "The Jordan curve theorem seems obvious. Why is a rigorous proof difficult?"
  type: multiple-choice
  options:
    - "Because continuous curves can be arbitrarily pathological — space-filling curves, curves with positive area, wildly oscillating curves — and the theorem must hold for all of them"
    - "Because the theorem is actually false for some curves"
    - "Because the plane has complicated topology"
    - "Because the definition of 'inside' is ambiguous"
  answer: 0
  explanation: "The difficulty lies in the generality of 'continuous simple closed curve.' Such curves can be extremely wild: they can have infinite length, positive Lebesgue measure (the Osgood curve), or oscillate infinitely often at every scale (like space-filling curves, though space-filling curves are not injective so they are not simple). The theorem must handle ALL continuous injections of S^1 into R^2, including those that defy geometric intuition. For smooth or polygonal curves, the theorem is much easier. The homological proof handles all cases uniformly because homology is defined for arbitrary continuous maps."

- question: "The generalization to higher dimensions (Jordan-Brouwer separation theorem) states: any embedding of S^{n-1} in S^n separates S^n into exactly two components."
  type: true-false
  answer: true
  explanation: "This is the natural higher-dimensional generalization. An embedded (n-1)-sphere in S^n divides S^n into two open connected components whose common boundary is the embedded sphere. The homological proof generalizes cleanly: using the Mayer-Vietoris sequence on the decomposition S^n = U ∪ V where U is the complement of a closed disk neighborhood and V is a neighborhood of the embedded sphere, one computes H_0(S^n \\ S^{n-1}) and shows it has rank 2 (two connected components). The proof uses Alexander duality in its most general form."

- question: "The homological proof of the Jordan curve theorem uses Alexander duality. What does Alexander duality say in this context?"
  type: multiple-choice
  options:
    - "H_k(S^n \\ K) ≅ H̃^{n-k-1}(K) for any compact subspace K ⊂ S^n"
    - "The fundamental group of the complement equals the homology of the curve"
    - "The curve and its complement have the same Euler characteristic"
    - "Every closed curve in S^2 is homologous to zero"
  answer: 0
  explanation: "Alexander duality states H_k(S^n \\ K) ≅ H̃^{n-k-1}(K) (reduced Cech cohomology). For the Jordan curve theorem: K = C ≅ S^1 embedded in S^2. Then H_0(S^2 \\ C) ≅ H̃^0(S^1) ≅ Z. Since H_0 counts connected components minus one (in reduced form), H̃_0(S^2 \\ C) ≅ Z means there are exactly 2 components. Alexander duality reduces the 'separation' question (about the complement) to a cohomology computation of the embedded object itself."

- question: "A figure-eight (two circles touching at a point) in the plane divides the plane into three regions. Explain why this does not contradict the Jordan curve theorem."
  type: short-answer
  answer: "The Jordan curve theorem applies only to SIMPLE closed curves — continuous injections of S^1 into R^2. A figure-eight is not a simple closed curve: it is the image of a curve that passes through the intersection point twice, so the parametrizing map S^1 → R^2 is not injective at that point. The figure-eight is instead the image of a continuous map that is not an embedding. The theorem makes no claim about non-simple curves, and indeed a non-simple curve can divide the plane into any number of regions."
  explanation: "This is a common source of confusion. The power of the Jordan curve theorem lies in its universality for simple curves — it applies even to incredibly pathological continuous injections. But the simplicity (injectivity) condition is essential. Without it, curves can self-intersect and create arbitrarily many regions."
```

## Explainer

The **Jordan curve theorem** (JCT) states that if C is a simple closed curve in R^2 (the image of a continuous injection gamma : S^1 -> R^2), then R^2 \ C has exactly two connected components, one bounded and one unbounded, and C is the common boundary of both. Equivalently, working in S^2 = R^2 union {infinity} (the one-point compactification), the complement S^2 \ C has exactly two connected components. The theorem was stated by Jordan in 1887, and the first correct proof was given by Veblen in 1905. Modern proofs using homology are considerably cleaner.

The homological approach proves the more general **Jordan-Brouwer separation theorem**: if h : S^{n-1} -> S^n is an embedding (a homeomorphism onto its image), then S^n \ h(S^{n-1}) has exactly two connected components. The proof uses **Alexander duality**, which relates the homology of the complement S^n \ K to the cohomology of the compact subspace K. Specifically, H_k(S^n \ K; Z) = H^{n-k-1}(K; Z) (with Cech cohomology for full generality). For K = h(S^{n-1}) = S^{n-1}: H_0(S^n \ S^{n-1}) = H^{n-1}(S^{n-1}) = Z (in reduced homology, this gives exactly two components). The full Alexander duality also shows H_k(S^n \ S^{n-1}) = 0 for k > 0, so each component is homologically trivial.

An alternative proof uses the **Mayer-Vietoris sequence** more directly. One version proceeds by induction, building up the simple closed curve from simpler arcs and using Mayer-Vietoris to track how the homology of the complement changes at each stage. The key step is showing that the complement of an arc (homeomorphic image of [0,1]) in S^n is connected and has trivial homology — i.e., arcs do not separate S^n. Then, decomposing S^1 into two arcs and applying Mayer-Vietoris to the complement of their union gives the separation result.

The theorem has several important extensions and related results. The **Schoenflies theorem** (in dimension 2) strengthens the JCT by saying that the closure of each component is homeomorphic to a closed disk D^2 — not just that there are two components, but that each component is "shaped like a disk." In higher dimensions (n >= 3), the Schoenflies theorem fails without additional hypotheses: the **Alexander horned sphere** is an embedding of S^2 in S^3 whose complement has two components, but one component is not simply connected (and hence not homeomorphic to a ball). This shows that the Jordan-Brouwer separation theorem (homological statement) generalizes cleanly, but the Schoenflies theorem (topological characterization of the components) requires additional conditions (such as the embedded sphere being "locally flat").

The homological proof of the Jordan curve theorem is a triumph of the algebraic topology method: a statement that is "intuitively obvious" for smooth curves but fiendishly difficult for arbitrary continuous curves becomes a straightforward computation when translated into the language of homology and Alexander duality. The proof treats all continuous curves uniformly and generalizes to all dimensions, demonstrating the power of homological methods for establishing topological facts that resist elementary proof techniques.
