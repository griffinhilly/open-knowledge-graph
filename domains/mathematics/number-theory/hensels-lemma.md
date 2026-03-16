---
id: hensels-lemma
title: Hensel's Lemma
domain: mathematics
course: number-theory
prerequisites:
- id: introduction-p-adic-numbers
  type: hard
- id: quadratic-congruences
  type: soft
tags:
- hensels-lemma
- lifting-solutions
- p-adic-numbers
stage: advanced
status: draft
---

# Hensel's Lemma

## Core Idea
If f(x) ≡ 0 (mod p) has a solution a with f'(a) ≢ 0 (mod p), then a lifts uniquely to a solution in ℤ_p. This enables solving congruences modulo p^k iteratively and extends to polynomial equations over p-adic numbers.

## Explainer

Hensel's Lemma is the p-adic analog of Newton's method. Recall how Newton's method finds real roots: start near a root, use the tangent line (the derivative) to get a better approximation, repeat. Hensel's Lemma is the same idea, but working modulo increasing powers of p rather than over the real line. The key principle is **lifting**: a solution mod p can be refined to a solution mod p², then mod p³, and so on — as long as the derivative is nonzero at the solution.

Concretely, suppose f(a) ≡ 0 (mod p) and f'(a) ≢ 0 (mod p). Can we find b ≡ a (mod p) with f(b) ≡ 0 (mod p²)? Write b = a + tp for some integer t. Taylor-expanding modulo p²: f(a + tp) ≡ f(a) + tp · f'(a) (mod p²). Setting this to zero gives t ≡ −f(a)/p · (f'(a))⁻¹ (mod p). Since f(a) ≡ 0 (mod p), the quantity f(a)/p is an integer; and since f'(a) ≢ 0 (mod p), its inverse exists modulo p. So t is uniquely determined mod p, and b = a + tp is the unique lift of a to a solution mod p². The same argument applies repeatedly, lifting from mod p^k to mod p^{k+1} at each stage.

The condition f'(a) ≢ 0 (mod p) is what makes uniqueness possible. When the derivative vanishes at the solution, lifting may fail entirely (no solution mod p²) or branch into multiple lifts — exactly as Newton's method fails near a repeated real root. When the condition holds, the lift is unique at every stage, meaning the single root in ℤ/pℤ extends to a unique element of ℤ_p — a p-adic integer. Hensel's Lemma is thus a constructive bridge from your knowledge of p-adic numbers to concrete computations: a root that "looks good" mod p (with nonvanishing derivative) extends all the way into the p-adic integers with no ambiguity.

A classic application connects directly to quadratic congruences: does x² ≡ a (mod p^k) have a solution for all k ≥ 1? By Hensel, it suffices to check that x² ≡ a (mod p) has a solution x₀ and that the derivative 2x₀ is nonzero mod p — i.e., x₀ ≢ 0 (mod p). When p is odd and a is a quadratic residue mod p, both conditions hold, so the solution lifts to all p-adic levels. Hensel's Lemma therefore turns the question "does this congruence have solutions at arbitrarily high powers of p?" into a single computation mod p.
