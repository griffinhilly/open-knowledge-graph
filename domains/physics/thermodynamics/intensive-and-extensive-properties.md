---
id: intensive-and-extensive-properties
title: Intensive and Extensive Properties
domain: physics
course: thermodynamics
prerequisites:
- id: thermodynamic-processes
  type: soft
builds-toward:
- state-variables-and-functions
- molar-heat-capacities
tags:
- scaling
- properties
- composition
stage: formal-systems
status: draft
---

# Intensive and Extensive Properties

## Core Idea
Intensive properties (like temperature and pressure) are independent of the amount of substance in a system and remain unchanged when the system is divided into smaller parts. Extensive properties (like mass, volume, and internal energy) scale proportionally with the amount of substance and are additive for subsystems. Understanding this distinction is crucial for scaling laws and for defining specific (per-unit-mass) or molar quantities.

## How It's Best Learned
Imagine dividing a system in half: which properties remain the same? Which double? Explore molar quantities (U_m, V_m) and specific quantities (u, v). Use homogeneity of thermodynamic functions.

## Common Misconceptions
- Thinking entropy is always extensive (it is, but entropy density is intensive).
- Confusing density (intensive) with mass (extensive).
- Assuming all measurable quantities are either intensive or extensive.

## Explainer

From your introduction to **thermodynamic processes**, you have been working with quantities like temperature, pressure, volume, and energy. Now it is time to notice a fundamental difference in how these quantities behave when you scale a system. The distinction between **extensive** and **intensive** properties is not a bookkeeping detail — it is a structural feature of thermodynamics that constrains the form every thermodynamic equation can take.

The clearest way to see the difference is the **bisection test**: mentally cut your system in half and ask what happens to each property. Temperature? Same in both halves — it does not depend on how much material is present. Pressure? Same. These are **intensive** properties: they characterize the state of matter at a point and are independent of system size. Now ask about volume: each half has half the original volume. Internal energy U? Also halved. Entropy S? Halved. Mass? Halved. These are **extensive** properties: they add up when you combine subsystems and scale proportionally with the amount of substance. Mathematically, an extensive quantity X satisfies X(λN, λV, λS, ...) = λX(N, V, S, ...) for any scale factor λ — it is a homogeneous function of degree 1 in the extensive variables.

This scaling property has a powerful consequence known as the **Euler relation** for thermodynamics. Differentiating U(λS, λV, λN) = λU with respect to λ and setting λ = 1 gives: U = TS − PV + μN, where T = ∂U/∂S, P = −∂U/∂V, and μ = ∂U/∂N are the intensive conjugate variables. This equation — expressing the total internal energy in terms of intensive variables times their extensive conjugates — holds for any simple system and is a direct consequence of extensivity. Notice that the intensive variables (T, P, μ) are the partial derivatives of the extensive variable U with respect to the other extensive variables.

In practice, you will often work with **molar quantities** (dividing an extensive property by the number of moles n) or **specific quantities** (dividing by mass m). Molar volume V_m = V/n, molar entropy S_m = S/n, and specific internal energy u = U/m are all intensive — they describe a property per unit of substance rather than of the whole system. This is why equations of state (like the ideal gas law PV = nRT) are often written as Pv = RT, where v = V/n is the molar volume: intensive variables relate to each other in equations that do not depend on how much gas you have. The intensive-versus-extensive classification is how thermodynamics achieves scale independence: the same equations describe a teaspoon of gas and a planet's atmosphere.
