---
id: propositional-compactness
title: Compactness Theorem for Propositional Logic
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: propositional-soundness-completeness
  type: hard
- id: normal-forms-cnf-dnf
  type: soft
builds-toward:
- fol-compactness
- model-theory-basics
tags:
- compactness
- infinite-sets
- satisfiability
- finiteness
stage: formal-systems
status: validated
---

# Compactness Theorem for Propositional Logic

## Core Idea
The compactness theorem states that an infinite set of propositional formulas is satisfiable if and only if every finite subset of it is satisfiable. This connects local (finite) reasoning to global (infinite) conclusions and is one of the most powerful tools in mathematical logic. It follows naturally from completeness: any proof uses only finitely many formulas. Compactness has striking applications — for instance, it can be used to show that if a graph-coloring problem has no finite obstruction, it has a valid coloring — and it is the key lemma behind many model-theoretic constructions.

## How It's Best Learned
Prove compactness from completeness (proofs are finite objects). Then work through at least one non-trivial application, such as constructing non-standard models or proving König's infinity lemma.

## Common Misconceptions
- Compactness does not mean finite sets are all that matter; infinite sets are fully meaningful, but finitely testable.
- The theorem's converse direction (finite satisfiability implies global satisfiability) is the non-trivial and surprising direction.

## Explainer

You already know that a set of propositional formulas is **satisfiable** if there is some truth assignment making all of them simultaneously true, and you know from soundness and completeness that provability and truth coincide for propositional logic. The **compactness theorem** builds on completeness to answer a question about infinite sets: if you cannot find a contradiction in any finite portion of an infinite theory, must the whole thing be consistent?

The answer is yes. Formally: an infinite set Σ of propositional formulas is satisfiable if and only if every **finite subset** of Σ is satisfiable. The forward direction is trivial — if Σ has a model, every subset does too. The surprising direction is the converse: finite satisfiability everywhere implies a global satisfying assignment exists. This is called "compactness" by analogy with topology — the logic behaves like a compact space, where a property holding at every finite scale propagates to the whole.

The cleanest proof runs through completeness. Any proof of a contradiction from Σ uses only finitely many formulas from Σ (proofs are finite objects). So if every finite subset of Σ is satisfiable (and hence consistent), no finite subset can prove a contradiction, so Σ itself cannot prove a contradiction, so by completeness Σ is satisfiable. The key observation is that proofs are finite, which means contradictions can only "see" finitely many assumptions at once.

The applications are striking. Suppose you want to 4-color an infinite planar graph but can't do it all at once. Compactness lets you argue locally: introduce a propositional variable for each "node gets color c" assignment, write finitely many formulas encoding valid 4-coloring for each finite subgraph, and observe that every finite subgraph is colorable (by the finite 4-color theorem). By compactness, the infinite graph is colorable too. The same argument proves König's infinity lemma, constructs non-standard models of arithmetic, and builds models with unusual properties — all by specifying infinitely many requirements that are finitely consistent.

Compactness also clarifies the *limits* of propositional logic. It implies that propositional logic cannot express the property "this graph is finite" or "this number is a standard natural number" — any finite set of formulas satisfied by finite structures can always be extended (by compactness) to a model with a non-standard, infinite element. This is not a bug but a feature: it is precisely the gap that separates propositional logic's infinite models from their finite approximations, and it will recur in full force when you study compactness for first-order logic.
