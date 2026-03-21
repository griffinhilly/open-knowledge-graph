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

## Questions

```yaml
- question: "In ℝ with the standard topology, what is the closure of the set of rational numbers ℚ?"
  type: multiple-choice
  options:
    - "ℚ itself, since rationals form a closed subset of ℝ"
    - "ℝ, because every real number is a limit point of ℚ"
    - "The algebraic numbers, since irrationals cannot be limits of rational sequences"
    - "The closure is undefined because ℚ is not bounded"
  answer: 1
  explanation: "ℚ is dense in ℝ — every real number can be approximated arbitrarily closely by rationals. Formally, every x ∈ ℝ is a limit point of ℚ: every open interval around x contains a rational. So cl(ℚ) = ℚ ∪ {all limit points} = ℝ. Option A is wrong because ℚ is not closed — its complement (the irrationals) is not open. This example shows that a 'small' countable set can have closure equal to the entire uncountable space."

- question: "Let A = (0, 1) and B = (1, 2) be open intervals in ℝ. Which statement correctly describes their closures?"
  type: multiple-choice
  options:
    - "cl(A ∩ B) = cl(A) ∩ cl(B) = {1}, showing closure distributes over intersections"
    - "cl(A ∪ B) = cl(A) ∪ cl(B) = [0, 2], but cl(A ∩ B) = ∅ while cl(A) ∩ cl(B) = {1}"
    - "cl(A ∩ B) = cl(A) ∪ cl(B) = [0, 1] ∪ [1, 2]"
    - "cl(A) ∩ cl(B) = ∅ because A and B do not overlap"
  answer: 1
  explanation: "A ∩ B = ∅, so cl(A ∩ B) = cl(∅) = ∅. But cl(A) = [0,1] and cl(B) = [1,2], so cl(A) ∩ cl(B) = {1} ≠ ∅. This shows cl(A ∩ B) ⊊ cl(A) ∩ cl(B) — containment is strict, not equality. The closure operator distributes exactly over unions: cl(A ∪ B) = cl(A) ∪ cl(B) = [0,2]. But for intersections, the closures of the pieces can 'see' a common boundary point ({1}) that the pieces themselves never reach."

- question: "Applying the closure operator twice gives the same result as applying it once: cl(cl(A)) = cl(A) for any set A."
  type: true-false
  answer: true
  explanation: "True — this is idempotence, the third Kuratowski axiom. cl(A) is already a closed set (it is an intersection of closed sets, and arbitrary intersections of closed sets are closed). The closure of a closed set is itself. Once you have captured all limit points of A to form cl(A), there are no new limit points to add — cl(A) already contains all its own limit points by definition of being closed."

- question: "For any two sets A and B in a topological space, cl(A ∩ B) = cl(A) ∩ cl(B)."
  type: true-false
  answer: false
  explanation: "False. The correct statement is only the containment cl(A ∩ B) ⊆ cl(A) ∩ cl(B). The counterexample is A = (0,1) and B = (1,2): A ∩ B = ∅, so cl(A ∩ B) = ∅, but cl(A) ∩ cl(B) = [0,1] ∩ [1,2] = {1} ≠ ∅. The closures of the two pieces share the boundary point 1 even though the pieces themselves are disjoint. Equality holds for unions (cl(A ∪ B) = cl(A) ∪ cl(B)) but only inclusion holds for intersections."

- question: "Why is cl(ℚ) = ℝ in the standard topology on ℝ, and what does this say about ℚ's relationship to ℝ?"
  type: short-answer
  answer: "Every real number x is a limit point of ℚ: for any open interval (x − ε, x + ε), there exists a rational number inside it (the Archimedean property guarantees this). So every x ∈ ℝ belongs to ℚ ∪ {limit points of ℚ} = cl(ℚ). Since cl(ℚ) ⊆ ℝ trivially, we get cl(ℚ) = ℝ. This means ℚ is dense in ℝ — a set is dense in a space precisely when its closure equals the whole space."
  explanation: "Density is a fundamental concept: ℚ is 'everywhere' in ℝ in the sense that you can get arbitrarily close to any real number using rationals. This is why analysis works — theorems about real numbers are often proved by taking limits of rational approximations. The closure operation makes 'density' precise: S is dense in X if and only if cl(S) = X."
```

## Explainer

You know that a set is closed if and only if it contains all its limit points — the points that sequences from the set can converge toward. But what if a set is not closed? The **closure** operation "completes" the set by adjoining exactly the missing limit points: it produces the smallest closed set that contains A. Think of it as surrounding A with all the points that A is trying to reach but hasn't quite captured yet.

There are two equivalent ways to define cl(A), and switching between them depending on the problem is a key technique. The **lattice definition**: cl(A) = ∩ {F : F is closed and F ⊇ A}. This intersection works because arbitrary intersections of closed sets are closed (from your prerequisite), so the intersection is itself a closed set, and it's the smallest one containing A. The **limit point definition**: cl(A) = A ∪ {all limit points of A}, where x is a limit point of A if every open set containing x intersects A. In metric spaces these coincide with the sequential limit definition: x ∈ cl(A) iff there is a sequence in A converging to x.

Examples make the definition concrete. In ℝ: cl((0, 1)) = [0, 1] (the open interval's closure adds its two boundary points). cl(ℚ) = ℝ (every real number is a limit of rationals, so every real is a limit point of ℚ — the rationals are **dense** in ℝ, meaning their closure is all of ℝ). cl({1/n : n ≥ 1}) = {0} ∪ {1/n : n ≥ 1} (the only new limit point is 0, approached by the sequence 1, 1/2, 1/3, …). The closure of an already-closed set is itself, which is the content of the **idempotence** property: cl(cl(A)) = cl(A).

The four **Kuratowski closure axioms** characterize what a closure operator must be: (1) cl(∅) = ∅, (2) A ⊆ cl(A), (3) cl(cl(A)) = cl(A), (4) cl(A ∪ B) = cl(A) ∪ cl(B). Remarkably, any function satisfying these four axioms on a power set defines a topology — so the closure operator is an alternative, equivalent starting point for the whole theory. Notice the asymmetry between unions and intersections: cl(A ∪ B) = cl(A) ∪ cl(B) holds exactly, but cl(A ∩ B) ⊆ cl(A) ∩ cl(B) is only an inclusion. The counterexample: A = (0, 1) and B = (1, 2). Their intersection is empty, so cl(A ∩ B) = ∅. But cl(A) ∩ cl(B) = [0, 1] ∩ [1, 2] = {1}. The closure of the pieces sees their common boundary point even when the pieces themselves don't meet.
