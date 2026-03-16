---
id: capacitor-geometry
title: 'Capacitors: Geometry and Capacitance'
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: dielectric-polarization
  type: soft
- id: electric-potential-field
  type: hard
builds-toward:
- energy-stored-capacitors
tags:
- capacitor
- geometry
- capacitance
stage: formal-systems
status: draft
---

# Capacitors: Geometry and Capacitance

## Core Idea
A capacitor stores charge by maintaining a potential difference between conductors. Capacitance is C = Q/V. For a parallel-plate capacitor: C = ε₀κᵣA/d. For spherical and cylindrical geometries: C_sphere = 4πε₀κᵣab/(b−a) and C_cylinder = 2πε₀κᵣℓ/ln(b/a). Capacitance depends only on geometry and material properties, independent of Q and V.

## Explainer

You already know that the **electric potential** V at a point describes the energy per unit charge needed to bring a test charge there. A capacitor exploits this idea deliberately: it consists of two conductors held apart, and when charge Q is deposited on them (equal and opposite), a potential difference V develops between them. The ratio C = Q/V is the **capacitance** — a geometric quantity that tells you how efficiently the device stores charge per volt of potential difference. A large capacitance means you can store a lot of charge with only a modest voltage; a small capacitance means even a little charge drives a large voltage.

To see where the geometry enters, consider the simplest case: two large parallel conducting plates, each with area A, separated by a small distance d. From your study of electric potential and Gauss's law, the electric field between ideal parallel plates is uniform: E = σ/ε₀ = Q/(ε₀A). The potential difference is just that field integrated over the gap: V = Ed = Qd/(ε₀A). Plugging into C = Q/V, the charge cancels entirely — giving C = ε₀A/d. This is the key insight: the Q and V dependence disappears, leaving only the geometric factors. A larger plate area stores more charge at the same voltage; a larger gap reduces capacitance because the same charge spreads its influence over more distance.

For other geometries you use the same approach: find the field (via Gauss's law exploiting symmetry), integrate to get the potential difference, and divide Q by V. For a **spherical capacitor** with inner radius a and outer radius b, the field is radial and falls off as Q/(4πε₀r²), so integrating from a to b gives V = Q(b−a)/(4πε₀ab), and C = 4πε₀ab/(b−a). Notice that as b → ∞ this becomes C = 4πε₀a — the capacitance of a single isolated sphere of radius a relative to infinity. For a **cylindrical capacitor** of length ℓ, the field is Q/(2πε₀ℓr), integrating from r = a to r = b yields V = Q·ln(b/a)/(2πε₀ℓ), so C = 2πε₀ℓ/ln(b/a). The logarithm reflects how the radial field distributes over a growing circumference.

Inserting a **dielectric material** (relative permittivity κᵣ) between the conductors multiplies capacitance by κᵣ in all three formulas. Physically, the dielectric polarizes: its molecules align with the applied field, creating bound surface charges that partially cancel the free charges on the plates, reducing the net field and the potential difference. Lower V for the same Q means higher C. All three geometry formulas therefore carry the factor ε₀κᵣ: C = ε₀κᵣA/d, C_sphere = 4πε₀κᵣab/(b−a), and C_cylinder = 2πε₀κᵣℓ/ln(b/a). The central lesson is that capacitance is a property of space and material, not of the charge itself — you can change Q and V dramatically while C remains fixed, as long as their ratio stays constant.
