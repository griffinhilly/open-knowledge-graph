---
id: fundamental-theorem-calculus-rigorous
title: Fundamental Theorem of Calculus (Rigorous)
domain: mathematics
course: real-analysis
prerequisites:
- id: riemann-integral-properties
  type: hard
- id: rigorous-derivative-definition
  type: hard
tags:
- fundamental-theorem
- differentiation
- integration
stage: abstract-reasoning
status: draft
---

# Fundamental Theorem of Calculus (Rigorous)

## Core Idea
The Fundamental Theorem has two parts: (1) if f is continuous on [a,b] and F(x) = ∫ₐˣ f, then F'(x) = f(x); (2) if F is continuous on [a,b], differentiable on (a,b), and F' is integrable, then ∫ₐᵇ F'(x) dx = F(b) - F(a). Together, they formalize that differentiation and integration are inverse operations. The rigorous proof requires uniform continuity and Darboux integrability.
