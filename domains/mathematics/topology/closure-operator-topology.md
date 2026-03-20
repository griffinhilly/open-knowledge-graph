---
id: closure-operator-topology
title: Closure of Sets
domain: mathematics
course: topology
prerequisites:
- id: closed-sets-definition-examples
  type: hard
builds-toward:
- boundary-set-topology
- dense-sets-topology-definition
tags:
- closure
- operators
stage: formal-systems
status: draft
---

# Closure of Sets

## Core Idea
The closure of A, denoted cl(A) or Ā, is the intersection of all closed sets containing A (the smallest closed set containing A). cl(A) consists of A together with all its limit points. Properties: cl(cl(A)) = cl(A), A ⊆ cl(A), cl(A ∪ B) = cl(A) ∪ cl(B), cl(A ∩ B) ⊆ cl(A) ∩ cl(B).

## Explainer

You know that a set is closed if and only if it contains all its limit points — the points that sequences from the set can converge toward. But what if a set is not closed? The **closure** operation "completes" the set by adjoining exactly the missing limit points: it produces the smallest closed set that contains A. Think of it as surrounding A with all the points that A is trying to reach but hasn't quite captured yet.

There are two equivalent ways to define cl(A), and switching between them depending on the problem is a key technique. The **lattice definition**: cl(A) = ∩ {F : F is closed and F ⊇ A}. This intersection works because arbitrary intersections of closed sets are closed (from your prerequisite), so the intersection is itself a closed set, and it's the smallest one containing A. The **limit point definition**: cl(A) = A ∪ {all limit points of A}, where x is a limit point of A if every open set containing x intersects A. In metric spaces these coincide with the sequential limit definition: x ∈ cl(A) iff there is a sequence in A converging to x.

Examples make the definition concrete. In ℝ: cl((0, 1)) = [0, 1] (the open interval's closure adds its two boundary points). cl(ℚ) = ℝ (every real number is a limit of rationals, so every real is a limit point of ℚ — the rationals are **dense** in ℝ, meaning their closure is all of ℝ). cl({1/n : n ≥ 1}) = {0} ∪ {1/n : n ≥ 1} (the only new limit point is 0, approached by the sequence 1, 1/2, 1/3, …). The closure of an already-closed set is itself, which is the content of the **idempotence** property: cl(cl(A)) = cl(A).

The four **Kuratowski closure axioms** characterize what a closure operator must be: (1) cl(∅) = ∅, (2) A ⊆ cl(A), (3) cl(cl(A)) = cl(A), (4) cl(A ∪ B) = cl(A) ∪ cl(B). Remarkably, any function satisfying these four axioms on a power set defines a topology — so the closure operator is an alternative, equivalent starting point for the whole theory. Notice the asymmetry between unions and intersections: cl(A ∪ B) = cl(A) ∪ cl(B) holds exactly, but cl(A ∩ B) ⊆ cl(A) ∩ cl(B) is only an inclusion. The counterexample: A = (0, 1) and B = (1, 2). Their intersection is empty, so cl(A ∩ B) = ∅. But cl(A) ∩ cl(B) = [0, 1] ∩ [1, 2] = {1}. The closure of the pieces sees their common boundary point even when the pieces themselves don't meet.
