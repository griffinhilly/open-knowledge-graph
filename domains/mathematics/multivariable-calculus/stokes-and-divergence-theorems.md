---
id: stokes-and-divergence-theorems
title: Stokes' Theorem and the Divergence Theorem
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: surface-integrals-flux
  type: hard
tags:
- stokes-theorem
- divergence-theorem
- gauss-theorem
stage: formal-systems
status: draft
---

# Stokes' Theorem and the Divergence Theorem

## Core Idea
Stokes' theorem: ∮_C F · dr = ∬_S (∇ × F) · dS (line integral of F around a closed curve equals flux of curl through the surface). Divergence theorem: ∬_S F · dS = ∭_V ∇ · F dV (flux through a closed surface equals integral of divergence over the volume). These unify single, double, and triple integrals.

## Questions

```yaml
- question: "Computing ∬_S F · dS directly over a complicated closed surface S is very difficult. However, the enclosed volume V has a simple shape, and ∇ · F = 4 everywhere inside V (volume of V = 6). Which theorem applies, and what is the flux?"
  type: multiple-choice
  options:
    - "Stokes' theorem; compute the curl of F and integrate over a bounding curve instead."
    - "The Divergence theorem; flux = ∭_V ∇ · F dV = 4 × 6 = 24."
    - "The Divergence theorem; flux = ∬_S 4 dS, still requiring the surface integral."
    - "The Fundamental Theorem of Calculus, since F has constant divergence."
  answer: 1
  explanation: "The Divergence theorem converts the surface integral of F · dS over a closed surface into the volume integral of ∇ · F over the enclosed region: ∬_S F · dS = ∭_V ∇ · F dV. With ∇ · F = 4 everywhere and volume = 6, the answer is 24. Option C is the error of knowing the theorem's name but not applying it — the whole point is to *replace* the surface integral with the volume integral."

- question: "According to Stokes' theorem, two different oriented surfaces S₁ and S₂ both have the same closed curve C as their boundary. Which statement is correct?"
  type: multiple-choice
  options:
    - "∬_{S₁} (∇ × F) · dS and ∬_{S₂} (∇ × F) · dS may differ if the surfaces have different areas."
    - "∬_{S₁} (∇ × F) · dS = ∬_{S₂} (∇ × F) · dS, because both equal the same line integral ∮_C F · dr."
    - "∬_{S₁} (∇ × F) · dS = ∬_{S₂} (∇ × F) · dS only if F is conservative."
    - "You must use the flat surface to apply Stokes' theorem; curved surfaces give different results."
  answer: 1
  explanation: "Stokes' theorem equates the line integral ∮_C F · dr with the surface integral of the curl over any surface bounded by C. Since both S₁ and S₂ share the same boundary curve C, both surface integrals equal the same line integral — they must be equal. This surface-independence is one of Stokes' most powerful features: you can choose whichever surface makes the computation easiest."

- question: "The Divergence theorem, Stokes' theorem, and the Fundamental Theorem of Calculus are all instances of the same pattern: an integral over a region's interior equals an integral over its boundary."
  type: true-false
  answer: true
  explanation: "Yes. The Fundamental Theorem says ∫_a^b f′ dx = f(b) − f(a): integral of derivative over an interval equals function evaluated on the boundary (two points). Green's theorem, Stokes' theorem, and the Divergence theorem are the 2D and 3D versions of this pattern. In each case, an integral involving a differential operator (curl, divergence) over the interior equals an integral over the boundary (curve, surface)."

- question: "The Divergence theorem converts a surface integral into a line integral by integrating the divergence of F along the boundary curve of the surface."
  type: true-false
  answer: false
  explanation: "The Divergence theorem converts a *surface* integral (flux through a closed surface) into a *volume* integral (of divergence over the enclosed 3D region). It has nothing to do with line integrals. That confusion conflates it with Stokes' theorem, which connects a line integral to a surface integral of the curl. These are different theorems: Stokes relates line ↔ surface; Divergence relates surface ↔ volume."

- question: "If ∇ · F = 0 everywhere in a region, what does the Divergence theorem tell you about the flux through any closed surface in that region? Why does this make physical sense?"
  type: short-answer
  answer: "The Divergence theorem gives ∬_S F · dS = ∭_V ∇ · F dV = 0. Physically, zero divergence means there are no sources or sinks — the field neither originates nor terminates at any interior point. So every field line that enters a closed surface must also exit it: the net outward flux is zero. This is exactly Gauss's law for electric fields in a charge-free region, or the incompressibility condition for a fluid with no sources."
  explanation: "The physical interpretation of divergence as 'source density' is key. When ∇ · F = 0, the vector field is source-free, and by conservation, the total flow through any closed surface must balance — what goes in must come out."
```

## Explainer

From your work with surface integrals and flux, you know how to compute ∬_S F · dS — the rate at which a vector field F flows through a surface S. Both Stokes' theorem and the Divergence theorem belong to a single grand pattern: an integral over the interior of a region equals an integral over the boundary of that region. The fundamental theorem of calculus is the simplest instance — ∫_a^b f′(x) dx = f(b) − f(a) says the integral of f′ over an interval equals f evaluated on the boundary (just two points). Green's theorem, Stokes' theorem, and the Divergence theorem are higher-dimensional versions of this same idea.

**Stokes' theorem** connects a line integral around a closed curve C to a surface integral over any surface S bounded by C. The integrand on the surface side is the **curl** ∇ × F, which measures the infinitesimal rotation of F — how much F "circulates" locally. Stokes says the total circulation around the boundary C equals the total accumulated local rotation through the surface. Physically: if F is a velocity field of a fluid, the work done going around C equals the sum of all the little whirlpools threading through the surface. Crucially, any surface with boundary C gives the same answer — the choice of surface doesn't matter, only its boundary does.

The **Divergence theorem** (also called Gauss's theorem) connects a surface integral over a closed surface S to a volume integral over the region V enclosed by S. The integrand inside is the **divergence** ∇ · F, which measures how much F is "spreading out" or "converging" at each point — positive where field lines originate, negative where they terminate. The theorem says total outward flux through the surface equals the total source strength inside the volume. In electrostatics, this is exactly Gauss's law: the flux of the electric field through a closed surface equals the total charge enclosed, divided by ε₀.

These theorems are powerful computational tools as much as conceptual unifications. If ∬_S F · dS is hard to compute directly on a complex surface, and V is simple, compute ∭_V ∇ · F dV instead — often much easier when the divergence is constant or simple. Similarly, if ∮_C F · dr is cumbersome, choose a convenient surface bounded by C and integrate the curl. The freedom to choose the surface (in Stokes) or convert between surface and volume integrals (in the Divergence theorem) is the key flexibility that makes these theorems indispensable in physics and engineering, from Maxwell's equations to fluid dynamics.
