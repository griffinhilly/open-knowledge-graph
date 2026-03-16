---
id: fol-compactness
title: Compactness Theorem for First-Order Logic
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: fol-soundness-completeness
  type: hard
- id: propositional-compactness
  type: soft
builds-toward:
- lowenheim-skolem-theorem
- model-theory-basics
tags:
- compactness
- FOL
- ultraproducts
- non-standard-models
stage: formal-systems
status: validated
---

# Compactness Theorem for First-Order Logic

## Core Idea
The compactness theorem for first-order logic states that an infinite set of sentences has a model if and only if every finite subset has a model. This follows from completeness (proofs are finite, so any derivation of a contradiction uses only finitely many axioms). Compactness implies that first-order logic cannot characterize the natural numbers up to isomorphism: any first-order theory with an infinite model has models of every infinite cardinality (a consequence of Löwenheim-Skolem), and non-standard models of arithmetic exist. Compactness is a fundamental limitation of first-order expressivity.

## How It's Best Learned
Construct a non-standard model of arithmetic explicitly using compactness: add a new constant c and axioms c > n for each natural number n, then apply compactness to get a model containing an 'infinite' element.

## Common Misconceptions
- Compactness does not mean all relevant information is captured finitely — it means satisfiability is finitely determined.
- Non-standard models arising from compactness are fully legitimate models; they just satisfy extra sentences the intended model does not.

## Explainer

From your study of soundness and completeness for first-order logic, you know that a sentence is provable from a set of axioms if and only if it is true in every model of those axioms. The key structural fact underlying completeness is that **proofs are finite objects**. A formal proof is a finite sequence of steps, and therefore any proof uses only finitely many axioms from the axiom set — even if the axiom set is infinite. This finiteness of proofs is the engine behind compactness.

The **compactness theorem** says: an infinite set Γ of first-order sentences has a model if and only if every finite subset of Γ has a model. The "only if" direction is trivial — if Γ has a model, every subset does too. The "if" direction is the content: if Γ itself were unsatisfiable, some finite proof of ⊥ would exist (by completeness), and that proof would use only finitely many sentences from Γ, contradicting the assumption that every finite subset is satisfiable. Compactness is essentially completeness stated contrapositively, with proofs' finiteness doing all the work.

The power of compactness comes from using it constructively to build non-standard models. The canonical example: let T be the first-order theory of arithmetic (the sentences true in ℕ) and add a new constant symbol c together with the infinitely many axioms {c > 0, c > 1, c > 2, c > 3, ...}. Any finite subset of this extended theory is satisfiable — just interpret c as a sufficiently large natural number. By compactness, the entire theory is satisfiable. But any model of it contains an element c that is larger than every standard natural number — a **non-standard natural number**. This means first-order arithmetic cannot be categorical: no first-order theory pins down ℕ up to isomorphism, since any such theory also has non-standard models.

This points to compactness as a fundamental **limitation** of first-order expressivity. You cannot write a first-order sentence that says "exactly the standard natural numbers exist," or "this element is finite," or "this sequence is well-founded" in full generality. Any first-order condition that holds in ℕ will also hold in a structure with extra infinite elements. Second-order logic, which can quantify over sets and relations, can characterize ℕ up to isomorphism — but at the cost of losing compactness. This tradeoff (expressivity vs. model-theoretic manageability) is one of the central themes of logic: first-order logic's weakness (non-categoricity) is also its strength (completeness, compactness, and the Löwenheim-Skolem theorem all depend on it).

