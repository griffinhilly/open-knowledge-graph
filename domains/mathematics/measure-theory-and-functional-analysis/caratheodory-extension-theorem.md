---
id: caratheodory-extension-theorem
title: Carathéodory's Extension Theorem
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: outer-measure-definition
  type: hard
builds-toward:
- lebesgue-outer-measure
tags:
- measure-theory
- extension-theorems
stage: advanced
status: draft
---

# Carathéodory's Extension Theorem

## Core Idea
Carathéodory's theorem states that any outer measure μ* induces a measure on the σ-algebra of 'μ*-measurable' sets (those satisfying μ*(A) = μ*(A∩E) + μ*(A∩Eᶜ)). This is the standard method for constructing Lebesgue measure from an elementary definition.

## How It's Best Learned
Work through the proof that μ*-measurable sets form a σ-algebra and that μ* restricted to it is σ-additive.

## Common Misconceptions
The Carathéodory condition is non-obvious; it's not automatic that the μ*-measurable sets form a σ-algebra without this specific requirement.

## Explainer

The fundamental challenge in measure theory is getting measure to work on enough sets. You've defined outer measure, which assigns a "size" to every subset of ℝ — but outer measure is too permissive. It's defined on all subsets, and on pathological sets it fails to be additive: μ*(A ∪ B) might not equal μ*(A) + μ*(B) even for disjoint A and B. Carathéodory's theorem provides the key insight for rescuing this: rather than trying to fix outer measure, identify the subcollection of sets where it does behave well, and show that subcollection is a σ-algebra on which outer measure is a genuine measure.

The definition of **μ*-measurability** is the heart of the theorem. A set E is called μ*-measurable if it "splits" every other set A perfectly in the sense that μ*(A) = μ*(A ∩ E) + μ*(A ∩ Eᶜ). In plain language: E divides every test set A into two pieces whose outer measures add up correctly. For "nice" sets like intervals, this holds — if you split a test set by an interval, the pieces' sizes add up as expected. The condition is designed precisely to exclude the pathological sets where subadditivity fails to be equality.

The theorem then delivers two results in sequence. First, the collection ℳ of all μ*-measurable sets is a **σ-algebra**: it contains the empty set, is closed under complements (if E works as a splitter, so does Eᶜ), and is closed under countable unions. Second, the restriction of μ* to ℳ is **σ-additive** — it's a genuine measure. These two facts together mean you've constructed a complete measure space (X, ℳ, μ) starting from nothing more than an outer measure.

For Lebesgue measure specifically, the construction works as follows: define the outer measure of any set by covering it with countable unions of intervals and taking the infimum of total length. Apply Carathéodory's theorem. The resulting σ-algebra contains all open sets, all closed sets, and all their countable unions and intersections — the Borel σ-algebra — plus additional "null sets." Every Borel set is Lebesgue measurable, and the measure agrees with ordinary length on intervals. The theorem transforms an elementary, intuitive definition (length of a covering) into a rigorous, complete measure theory. It's the engine behind the entire Lebesgue integration program you'll build on next.
