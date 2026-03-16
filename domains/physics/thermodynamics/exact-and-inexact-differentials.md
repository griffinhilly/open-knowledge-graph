---
id: exact-and-inexact-differentials
title: Exact and Inexact Differentials
domain: physics
course: thermodynamics
prerequisites:
- id: path-functions-vs-state-functions
  type: hard
- id: partial-derivatives
  type: soft
builds-toward:
- maxwell-relations-thermodynamics
- legendre-transformations-potentials
tags:
- mathematics
- differentials
- path-dependence
stage: formal-systems
status: draft
---

# Exact and Inexact Differentials

## Core Idea
An exact differential dZ represents a state function—integrating it between two states always yields the same result regardless of path, symbolized by the line integral ∮ dZ = 0 around any closed path. An inexact differential đQ (heat) or đW (work) depends on the path taken and cannot be written as a state function differential; this is indicated by the bar through the d. Recognizing which differentials are exact is essential for identifying which quantities are state functions.

## How It's Best Learned
Test exactness using the condition ∂M/∂y = ∂N/∂x for a differential M dx + N dy. Apply to internal energy and heat in simple thermodynamic processes.

## Common Misconceptions
- Writing dQ when Q is not a state function; the symbol đQ is correct.
- Thinking inexact differentials cannot be integrated.
- Confusing inexact differentials with non-conservative forces in mechanics.

## Explainer

In calculus you learned to write the differential of a function F(x,y) as dF = (∂F/∂x)dx + (∂F/∂y)dy. The key property is that dF is **exact**: integrating it between two points gives F(final) − F(initial), regardless of the path taken. Thermodynamics forces you to confront differentials that do not have this property — quantities like heat and work that depend on *how* you get from state A to state B, not just on where A and B are. The mathematical distinction between exact and inexact differentials is therefore not abstract: it is the formal expression of the difference between state functions and path functions.

A general differential expression M(x,y)dx + N(x,y)dy is **exact** if and only if ∂M/∂y = ∂N/∂x — the cross-partial derivatives must be equal. This is the **exactness criterion** (also called the integrability condition). When it holds, there exists a potential function F such that M = ∂F/∂x and N = ∂F/∂y, and the integral along any path between the same two endpoints gives the same result. When it fails, no such potential function exists, and different paths between the same two states give different integral values. The closed-path integral ∮ M dx + N dy equals zero for exact differentials and is generally nonzero for inexact ones.

In thermodynamics, internal energy U is a state function, so dU is exact: the change in U between two equilibrium states is path-independent. But the heat absorbed đQ and the work done đW in a process depend entirely on the specific path — compress a gas quickly (adiabatically) versus slowly (isothermally) and you do different amounts of work even though the initial and final states are identical. This is why thermodynamics uses the special notation đQ and đW (with a bar through the d): to signal that these are **inexact differentials**, not derivatives of a state function called Q or W (no such function exists in general). The first law dU = đQ − đW is an equation relating three differentials: one exact (dU) and two inexact (đQ, đW) whose difference happens to be exact.

The exactness condition has profound consequences. Starting from dU = T dS − P dV, you can apply the cross-partial condition (∂T/∂V)_S = −(∂P/∂S)_V. This is a **Maxwell relation** — one of four that emerge from requiring the mixed partials of U, H, F, and G to be equal. The entire machinery of Maxwell relations is simply the exactness condition applied to thermodynamic potentials. The most fundamental application is entropy itself: the inexact differential đQ_rev becomes exact when divided by T, yielding the exact differential dS = đQ_rev/T. An **integrating factor** (here, 1/T) converts an inexact differential into an exact one — and the fact that such a factor exists for reversible heat is the mathematical content of the second law.
