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
status: validated
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

## Questions

```yaml
- question: "A gas undergoes two different processes from state A to state B: one isothermal expansion, one adiabatic expansion. Which statement is true?"
  type: multiple-choice
  options:
    - "Both ΔU and Q are identical for the two processes since the endpoints are the same"
    - "ΔU is identical for both processes; Q and W differ between them"
    - "ΔU differs because the irreversibility of each process affects the internal energy"
    - "Q is the same for both processes; only W differs depending on path"
  answer: 1
  explanation: "ΔU = U_B − U_A depends only on the thermodynamic states A and B (not on the path), so it is identical for both processes. Q and W separately are path-dependent (inexact): in the adiabatic process Q = 0 by definition, while in the isothermal process Q ≠ 0; correspondingly W differs too. The first law dU = đQ − đW expresses this: two inexact, path-dependent quantities whose difference always yields the same path-independent result. This is the central application of the exact/inexact distinction."

- question: "Internal energy U is a state function. Which statement correctly follows from this?"
  type: multiple-choice
  options:
    - "dU is inexact because it depends on the heat and work exchanged, which are path-dependent"
    - "dU is exact only for reversible processes; it is inexact for irreversible ones"
    - "dU is exact, so integrating it between two equilibrium states always gives the same result regardless of path"
    - "dU is exact, but only when the process is both quasi-static and adiabatic"
  answer: 2
  explanation: "State functions have exact differentials by definition: integrating an exact differential between two points gives the same result regardless of path. Since U depends only on the current thermodynamic state (not on history or process), dU is exact and ΔU is path-independent. The reversibility of the process is irrelevant to whether dU is exact — U is a state function under all conditions. What changes between reversible and irreversible paths is how Q and W are individually distributed, not ΔU."

- question: "An inexact differential like đQ can rarely be integrated — it is mathematically undefined as an integral."
  type: true-false
  answer: false
  explanation: "Inexact differentials can absolutely be integrated along a specific path. You can calculate the heat Q absorbed during a particular isothermal expansion by integrating đQ along that path and obtain a well-defined numerical result. What you cannot do is evaluate the integral using only the initial and final states — unlike exact differentials, the result depends on which path you take. Inexact means path-dependent, not unintegrable."

- question: "For a differential expression M dx + N dy to be exact, the cross-partial derivatives must satisfy ∂M/∂y = ∂N/∂x."
  type: true-false
  answer: true
  explanation: "This is the exactness criterion (integrability condition). When ∂M/∂y = ∂N/∂x, there exists a potential function F(x,y) such that M = ∂F/∂x and N = ∂F/∂y, and the integral along any path between the same endpoints gives the same result. When the condition fails, no such potential exists. In thermodynamics, applying this criterion to dU = T dS − P dV yields the Maxwell relations — the entire machinery of which is simply the exactness condition applied to thermodynamic state functions."

- question: "Why do thermodynamicists write đQ and đW with a bar through the d, rather than dQ and dW? What would be wrong with writing dQ?"
  type: short-answer
  answer: "Writing dQ would imply Q is a state function — that there exists a function Q(state) whose exact differential is dQ, making ΔQ path-independent. But heat is not a state function: how much heat a system exchanges depends entirely on the process (path), not just on the initial and final states. The notation đQ signals an inexact differential: there is no underlying function Q, and the integral ∫đQ is path-dependent. The same logic applies to đW."
  explanation: "The notational distinction enforces a conceptual one: dU is legitimate because U exists as a function of state variables (T, V, etc.), while Q and W do not. The first law dU = đQ − đW is an equation with one exact differential on the left and two inexact ones on the right whose difference cancels the path-dependence. Using dQ would be a mathematical claim — that a potential function Q exists — which is false in general."
```

## Explainer

In calculus you learned to write the differential of a function F(x,y) as dF = (∂F/∂x)dx + (∂F/∂y)dy. The key property is that dF is **exact**: integrating it between two points gives F(final) − F(initial), regardless of the path taken. Thermodynamics forces you to confront differentials that do not have this property — quantities like heat and work that depend on *how* you get from state A to state B, not just on where A and B are. The mathematical distinction between exact and inexact differentials is therefore not abstract: it is the formal expression of the difference between state functions and path functions.

A general differential expression M(x,y)dx + N(x,y)dy is **exact** if and only if ∂M/∂y = ∂N/∂x — the cross-partial derivatives must be equal. This is the **exactness criterion** (also called the integrability condition). When it holds, there exists a potential function F such that M = ∂F/∂x and N = ∂F/∂y, and the integral along any path between the same two endpoints gives the same result. When it fails, no such potential function exists, and different paths between the same two states give different integral values. The closed-path integral ∮ M dx + N dy equals zero for exact differentials and is generally nonzero for inexact ones.

In thermodynamics, internal energy U is a state function, so dU is exact: the change in U between two equilibrium states is path-independent. But the heat absorbed đQ and the work done đW in a process depend entirely on the specific path — compress a gas quickly (adiabatically) versus slowly (isothermally) and you do different amounts of work even though the initial and final states are identical. This is why thermodynamics uses the special notation đQ and đW (with a bar through the d): to signal that these are **inexact differentials**, not derivatives of a state function called Q or W (no such function exists in general). The first law dU = đQ − đW is an equation relating three differentials: one exact (dU) and two inexact (đQ, đW) whose difference happens to be exact.

The exactness condition has profound consequences. Starting from dU = T dS − P dV, you can apply the cross-partial condition (∂T/∂V)_S = −(∂P/∂S)_V. This is a **Maxwell relation** — one of four that emerge from requiring the mixed partials of U, H, F, and G to be equal. The entire machinery of Maxwell relations is simply the exactness condition applied to thermodynamic potentials. The most fundamental application is entropy itself: the inexact differential đQ_rev becomes exact when divided by T, yielding the exact differential dS = đQ_rev/T. An **integrating factor** (here, 1/T) converts an inexact differential into an exact one — and the fact that such a factor exists for reversible heat is the mathematical content of the second law.
