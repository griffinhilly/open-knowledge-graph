---
id: rates-of-change-partial-derivatives
title: Interpreting Partial Derivatives as Rates of Change
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: partial-derivatives
  type: hard
builds-toward:
- directional-derivatives-gradient
- gradient-vector-properties
tags:
- rates-of-change
- interpretation
- applications
stage: formal-systems
status: draft
---

# Interpreting Partial Derivatives as Rates of Change

## Core Idea
∂f/∂x represents how fast f increases per unit change in x when y is held fixed. Geometrically, it is the slope of the curve obtained by intersecting the surface z = f(x,y) with a plane of constant y. Understanding partial derivatives as directional rates prepares for the gradient vector.

## Explainer

From your study of partial derivatives, you know the mechanical procedure: to compute ∂f/∂x, hold y fixed and differentiate with respect to x as if y were a constant. But what does the resulting number actually *mean* about the function f? The interpretation is what makes partial derivatives analytically useful.

The partial derivative ∂f/∂x at a point (a, b) is the **instantaneous rate of change** of f in the x-direction at that point. Concretely, if f(x, y) measures the temperature at location (x, y), then ∂f/∂x at (a, b) tells you how fast the temperature changes as you walk eastward through (a, b), holding your north-south position fixed at y = b. More precisely: if you take a tiny step Δx in the x-direction, f changes by approximately (∂f/∂x) · Δx. The partial derivative is the proportionality constant — the rate per unit step.

Geometrically, fix y = b and look at the surface z = f(x, y). The vertical plane y = b slices this surface in a curve — a cross-section — described by z = f(x, b), a function of x alone. The partial derivative ∂f/∂x at (a, b) is exactly the slope of the tangent line to this cross-sectional curve at x = a. So partial differentiation reduces the multivariable problem to a single-variable one: you're just differentiating f along a chosen slice of the surface. The constraint "y held fixed" means you're restricting attention to the slice y = b.

The two partial derivatives ∂f/∂x and ∂f/∂y measure rates of change in the two coordinate directions — but these are just two special directions out of infinitely many. The **gradient vector** ∇f = ⟨∂f/∂x, ∂f/∂y⟩ packages both partials and points in the direction of steepest ascent of the surface. When you study directional derivatives next, you'll see that the rate of change in any direction u = ⟨cos θ, sin θ⟩ is ∇f · u — a dot product of the gradient with the direction. Partial derivatives are thus the building blocks: understand each one as a rate of change along a coordinate axis, and the gradient becomes the object that combines all such rates into a single vector capturing the full local behavior of f.
