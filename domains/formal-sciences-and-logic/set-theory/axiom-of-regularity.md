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

## Explainer

From your overview of ZFC, you know that the axioms collectively define what "set" means. Most axioms are constructive — they tell you how to build new sets from old ones. The axiom of regularity is different: it is a *restriction*, ruling out pathological configurations of the membership relation ∈. Specifically, it requires every non-empty set A to have an **∈-minimal element**: some m ∈ A such that m shares no members with A (m ∩ A = ∅). The immediate consequence is that no set can contain itself: if x ∈ x, then {x} is a non-empty set with no ∈-minimal element (since x ∩ {x} = {x} ≠ ∅), violating regularity.

The axiom also eliminates **infinite descending ∈-chains**. If x₁ ∋ x₂ ∋ x₃ ∋ ··· were such a chain, the set {x₁, x₂, x₃, …} would have no ∈-minimal element (every xᵢ contains xᵢ₊₁, so xᵢ ∩ {x₁, x₂, …} ≠ ∅). The membership relation ∈ is therefore **well-founded**: every non-empty class has an ∈-minimal element. Well-foundedness is what makes inductive and recursive definitions over sets work cleanly — it is the set-theoretic analogue of mathematical induction over the natural numbers.

The positive consequence of regularity is the **cumulative hierarchy** V = ∪_α V_α. Define V₀ = ∅, V_{α+1} = P(V_α) (the power set of the previous level), and at limit ordinals V_λ = ∪_{β < λ} V_β. Regularity guarantees that every set x has a **rank** — the least ordinal α such that x ∈ V_{α+1}. Rank 0 sets are elements of V₁ = {∅}, so rank 0 is just ∅. Rank 1 sets are subsets of V₁: {∅}, so the only rank 1 set is {∅}. Rank 2 sets are subsets of V₂ = {∅, {∅}}. The natural numbers, when defined as von Neumann ordinals, live at ω, and the hierarchy continues into the transfinite. Every mathematical object you will encounter in this course lives somewhere in V.

Regularity is independent of the other ZFC axioms: dropping it yields a consistent theory (ZFC without foundation), and adding its negation (allowing x ∈ x or infinite descending chains) gives **non-well-founded set theory** (like Aczel's Anti-Foundation Axiom). Non-well-founded sets have applications in modeling circular data structures and coinductive processes. But for the purposes of this course — ordinal arithmetic, transfinite induction, inner models — regularity is essential scaffolding.
