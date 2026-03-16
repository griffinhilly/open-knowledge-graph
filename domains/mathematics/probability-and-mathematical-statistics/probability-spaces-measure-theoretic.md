---
id: probability-spaces-measure-theoretic
title: Probability Spaces (Measure-Theoretic Definition)
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: sigma-algebras-measurable-sets
  type: hard
- id: probability-axioms
  type: hard
builds-toward:
- random-variables-as-measurable-functions
- expectation-measure-theoretic
- conditional-expectation
tags:
- probability
- measure-theory
- foundations
stage: advanced
status: draft
---

# Probability Spaces (Measure-Theoretic Definition)

## Core Idea
A probability space is a triple (Ω, ℱ, P) where Ω is a sample space, ℱ is a sigma-algebra of events, and P is a probability measure satisfying σ-additivity: P(∪ₙAₙ) = ΣₙP(Aₙ) for disjoint countable unions. This measure-theoretic definition extends the axioms of probability to handle infinite sample spaces. It provides the rigorous foundation for modern probability theory.

## How It's Best Learned
Review the axioms of probability first. Then see how sigma-algebras enable handling infinite sample spaces rigorously. Work examples: discrete spaces, ℝ with Borel sets, ℝⁿ.

## Common Misconceptions
- Thinking the axioms alone guarantee countable additivity; countable additivity must be stated explicitly. - Confusing the sample space with the event space; ℱ ⊆ P(Ω). - Assuming any partition of Ω generates a sigma-algebra.
