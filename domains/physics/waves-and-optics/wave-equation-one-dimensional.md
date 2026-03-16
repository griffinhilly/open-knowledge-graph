---
id: wave-equation-one-dimensional
title: The One-Dimensional Wave Equation
domain: physics
course: waves-and-optics
prerequisites:
- id: partial-derivatives
  type: hard
- id: chain-rule-multivariable
  type: hard
- id: wave-equation-pde
  type: hard
builds-toward:
- harmonic-wave-time-dependence
- plane-electromagnetic-waves
tags:
- waves
- pde
- mathematics
stage: formal-systems
status: draft
---

# The One-Dimensional Wave Equation

## Core Idea
The wave equation ∂²u/∂t² = v²∂²u/∂x² describes how wave displacement evolves in space and time. Any function of the form u(x,t) = f(x - vt) + g(x + vt) satisfies this equation, representing waves traveling in both directions at speed v. This fundamental equation emerges from Newton's laws applied to continuous media and is the basis for understanding all linear wave phenomena.

## How It's Best Learned
Derive it for a vibrating string using force balance on a small element. Then verify that sinusoidal and simple linear functions satisfy it.

## Common Misconceptions
The wave equation is not the same as the equation of motion for a simple harmonic oscillator—the double spatial derivative encodes how neighboring regions couple.

## Questions

```yaml
- question: "Which of the following functions is a solution to the 1D wave equation ∂²u/∂t² = v²∂²u/∂x²?"
  type: multiple-choice
  options: ["u(x,t) = A·sin(x)·cos(t) only if v=1", "u(x,t) = A·exp(−x²)", "u(x,t) = A·sin(kx − ωt) for any k,ω with ω/k = v", "u(x,t) = A·(x² + t²)"]
  answer: 2
  explanation: "Any function of the form f(x − vt) or g(x + vt) satisfies the wave equation. A·sin(kx − ωt) = A·sin(k(x − (ω/k)t)) has the form f(x − vt) provided v = ω/k. The Gaussian exp(−x²) has no t-dependence and does not satisfy the equation. The polynomial x² + t² fails because its second derivatives in x and t give 2 and 2, but 2 ≠ v²·2 in general."

- question: "The 1D wave equation and the simple harmonic oscillator equation are essentially the same — both describe oscillatory motion and have sinusoidal solutions."
  type: true-false
  answer: false
  explanation: "The SHO equation is an ODE: d²x/dt² = −ω²x, describing a single point oscillating in time. The wave equation is a PDE with second derivatives in both space and time: ∂²u/∂t² = v²∂²u/∂x². The spatial derivative encodes coupling between neighboring locations — disturbances propagate. A pulse that is zero at t=0 can arrive at a distant point later, which the SHO equation cannot describe at all."

- question: "In the derivation of the wave equation from a vibrating string, what physical quantity determines the wave speed v, and what does this tell you about wave propagation in stiffer vs. heavier strings?"
  type: short-answer
  answer: "The wave speed is v = sqrt(T/μ), where T is the string tension and μ is the mass per unit length. A stiffer (higher tension) string carries waves faster; a heavier (larger μ) string carries waves slower. Wave speed is set by the medium's restoring force and inertia, not by the wave's amplitude or shape."
  explanation: "This connects the mathematical wave equation to the physical derivation. Force balance on a small string element gives the restoring force proportional to tension times the curvature ∂²u/∂x², while Newton's second law gives the inertia term μ·∂²u/∂t². Dividing by μ and identifying v² = T/μ produces the wave equation. The same structure — restoring force / inertia — appears in all linear wave systems."
```

## Explainer

You already know how to take partial derivatives and how the chain rule handles composite functions. The 1D wave equation, ∂²u/∂t² = v²∂²u/∂x², is a partial differential equation (PDE) that connects the second derivative of a field u (displacement, pressure, electric field) in time to its second derivative in space. The constant v is the wave speed — a property of the medium, not the wave itself.

The cleanest way to understand the equation is to derive it from a physical model. Imagine a flexible string under tension T with mass per unit length μ. Consider a tiny segment of the string at position x. The net upward force on the segment comes from the difference in tension pulling on its two ends — proportional to the curvature ∂²u/∂x² of the string times the tension T. By Newton's second law, this equals the segment's mass (μ·dx) times its acceleration ∂²u/∂t². Rearranging gives ∂²u/∂t² = (T/μ)·∂²u/∂x², which is the wave equation with v = sqrt(T/μ). The double spatial derivative is not an accident — it captures how neighboring string segments are coupled through tension.

The general solution is d'Alembert's formula: u(x, t) = f(x − vt) + g(x + vt) for any twice-differentiable functions f and g. You can verify this by direct substitution: the chain rule gives ∂²f(x − vt)/∂t² = v²f''(x − vt) and ∂²f(x − vt)/∂x² = f''(x − vt), so the equation is satisfied. The function f(x − vt) represents a disturbance of any shape traveling in the +x direction at speed v — a Gaussian pulse, a triangular bump, or a sine wave all work equally well. The function g(x + vt) travels in the −x direction. The superposition of both represents the most general wave pattern.

A key misconception to avoid: the wave equation is not the simple harmonic oscillator (SHO) equation written in two variables. The SHO, d²x/dt² = −ω²x, governs a single point bobbing up and down — it has no spatial structure. The wave equation describes how disturbances at one location propagate to neighboring locations because of the ∂²u/∂x² coupling term. A localized pulse at x=0 at t=0 can arrive at x=10 later; this spatial propagation is precisely what the double spatial derivative encodes, and it is entirely absent from the SHO equation.

Sinusoidal solutions — harmonic waves of the form A·sin(kx − ωt) — are special cases of the general solution where f(x − vt) = A·sin(k(x − vt)) with ω = kv. These will be the building blocks for analyzing reflection, interference, and standing waves in subsequent topics. The wave equation's linearity means solutions can be superposed freely — two waves can pass through each other without interaction, each obeying the equation independently.
