---
id: axiom-of-regularity
title: Axiom of Regularity (Foundation)
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: zfc-axioms-overview
  type: hard
builds-toward:
- von-neumann-ordinals
- transfinite-induction
tags:
- ZFC
- regularity
- foundation
- well-founded
- cumulative hierarchy
stage: formal-systems
status: validated
---

# Axiom of Regularity (Foundation)

## Core Idea
The axiom of regularity (or foundation) states that every non-empty set A contains an element m ∈ A that is disjoint from A (i.e., m ∩ A = ∅). This immediately rules out x ∈ x for any set x, and eliminates all infinite descending ∈-chains x₁ ∋ x₂ ∋ x₃ ∋ ···. Regularity structures the entire universe of sets into a cumulative hierarchy V = ∪_α V_α, where V₀ = ∅, V_{α+1} = P(V_α), and V_λ = ∪_{β<λ} V_β at limit stages. While regularity does not affect ordinary mathematics (no normal mathematical object has x ∈ x), it is essential for the clean theory of ordinals and ranks.

## How It's Best Learned
Prove from regularity that no set is an element of itself, then that there is no two-element cycle (a ∈ b and b ∈ a). Build the cumulative hierarchy V₀, V₁, V₂, V₃, V_ω explicitly for several stages. Contrast with non-well-founded set theories (like Aczel's AFA) to appreciate what regularity contributes.

## Common Misconceptions
- Regularity is independent of the other ZFC axioms — dropping it gives a consistent theory.
- Regularity does not ban 'conceptual' self-reference; it is a structural axiom about the membership relation ∈ only.
