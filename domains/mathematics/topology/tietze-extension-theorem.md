---
id: tietze-extension-theorem
title: Tietze Extension Theorem
domain: mathematics
course: topology
prerequisites:
- id: urysohns-lemma
  type: hard
builds-toward:
- metrization-theorems
tags:
- tietze
- extension
stage: formal-systems
status: draft
---

# Tietze Extension Theorem

## Core Idea
In a normal space, every continuous function f: A → ℝ from a closed subset A extends to a continuous function F: X → ℝ.

## Explainer

Urysohn's lemma, your prerequisite, tells you that in a normal space, disjoint closed sets can be separated by a continuous real-valued function — there is a function g: X → [0,1] that equals 0 on one closed set and 1 on the other. The Tietze extension theorem is a natural generalization: instead of asking whether a particular simple function (the 0-on-A, 1-on-B separator) can be built, it asks whether an arbitrary continuous function defined on a closed subset can be extended to the whole space.

To see why normality matters, think about what could go wrong. Suppose A is a closed subset of X and f: A → ℝ is continuous. Extending f to X means finding F: X → ℝ continuous with F|_A = f — agreeing with f on A, behaving continuously on the rest of X. On the interior of A, the values of F are forced. On X \ A (which is open), F has freedom. The difficulty is on the boundary: as you approach A from outside, F must match what f is doing inside A. Normality provides exactly the separation power needed to build this extension: it ensures closed sets can be distinguished by continuous functions (via Urysohn), which can be assembled into an approximation of f and successively refined.

The constructive proof of Tietze uses Urysohn's lemma iteratively. You approximate f by a sequence of continuous functions defined on all of X, each reducing the approximation error by a factor of 2/3 on A. The series converges uniformly to an extension F. This "uniform approximation by Urysohn functions" technique is a model for many existence arguments in analysis: rather than writing down the answer, you build it as a limit of manageable pieces. The key insight is that Urysohn's lemma is the atomic building block — the ability to extend indicator-like functions — and Tietze shows that more complex functions are just combinations of these atoms.

The theorem has two equivalent formulations: the extension can be arranged to map X → [−1,1] when f maps A → [−1,1] (bounded case), or X → ℝ when f: A → ℝ (unbounded case). Both follow from the same argument. The geometric content is that **normal spaces are functionally rich** — they support enough continuous functions to interpolate from any closed subset to the ambient space. This is not trivially true in general: without normality (or some separation axiom), continuous functions can be scarce and extensions may fail. The Tietze theorem connects to your next topic of metrization: one characterization of metrizable spaces is that they are normal, and normality combined with second-countability is exactly what the Urysohn metrization theorem needs. Tietze is thus part of the chain showing that normal spaces behave like metric spaces in their function theory.
