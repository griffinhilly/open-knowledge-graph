---
id: double-integrals
title: 'Double Integrals: Definition and Setup'
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: definite-integral-definition
  type: hard
- id: functions-of-several-variables
  type: hard
builds-toward:
- iterated-integrals-fubini
- double-integrals-rectangular-regions
tags:
- double-integrals
- riemann-sum
- definition
stage: formal-systems
status: draft
---

# Double Integrals: Definition and Setup

## Core Idea
The double integral ∬_R f(x, y) dA extends integration to 2D: partition region R into small rectangles, form Riemann sums by approximating f as constant on each, and take the limit as partition size shrinks. The result measures the volume under the surface z = f(x, y).

## Explainer

A single definite integral ∫_a^b f(x)dx measures the signed area under a 1D curve. The double integral ∬_R f(x, y) dA extends this to two dimensions: instead of area, you accumulate **volume** under the surface z = f(x, y) above a planar region R. The construction mirrors the 1D Riemann sum you already know, scaled up by one dimension.

The definition partitions R into small rectangles of area ΔA = Δx · Δy. On each rectangle, pick a sample point (xᵢⱼ, yᵢⱼ) and approximate the solid above that rectangle as a thin box of height f(xᵢⱼ, yᵢⱼ) and volume f(xᵢⱼ, yᵢⱼ) · ΔA. The **Riemann sum** ∑ᵢ∑ⱼ f(xᵢⱼ, yᵢⱼ)ΔA approximates the total volume by summing all boxes. Taking the limit as rectangle dimensions shrink to zero gives ∬_R f(x, y) dA — if the limit exists independently of partition choice and sample points, f is integrable over R.

A critical conceptual point: the double integral is a single limit, not two nested limits. The **Fubini theorem** (your next topic) is what allows you to compute double integrals as iterated single integrals — but that is a theorem, not the definition. Keeping definition and computation method separate matters when you encounter situations where the order of integration must be swapped, or when working with non-rectangular regions that require careful setup.

When f can be negative, the double integral gives signed volume: regions where f < 0 subtract from the total. When f = 1 everywhere, ∬_R 1 dA = area(R) — the integral degenerates to measuring the region itself. More broadly, double integrals compute mass (when f is a density), electric charge, probability, center of mass, and many other quantities distributed over a 2D region. The setup skill — identifying R, understanding the geometry of the solid, and recognizing what f represents — is what separates successful integration from mechanical symbol manipulation.
