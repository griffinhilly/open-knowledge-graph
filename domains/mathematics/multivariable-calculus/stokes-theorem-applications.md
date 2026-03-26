---
id: stokes-theorem-applications
title: 'Stokes'' Theorem: Circulation and Curl'
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: curl-and-divergence-operators
  type: hard
- id: surface-integrals-flux-vector
  type: hard
- id: stokes-and-divergence-theorems
  type: soft
- id: work-circulation
  type: soft
- id: greens-theorem-applications
  type: soft
tags:
- stokes-theorem
- curl
- circulation
stage: formal-systems
status: validated
---
# Stokes' Theorem: Circulation and Curl

## Core Idea
Stokes' theorem states ∮_C F · dr = ∬_S (∇ × F) · n dS, where S is a surface bounded by closed curve C. It generalizes Green's theorem to 3D: circulation around C equals flux of curl through S. Boundary orientation uses right-hand rule.

## Questions

```yaml
- question: "You need to compute ∮_C F·dr where C is a complicated 3D curve. Applying Stokes' theorem, you may:"
  type: multiple-choice
  options:
    - "Replace C with any simpler closed curve in the same plane"
    - "Choose any surface spanning C and compute the flux of curl(F) through it"
    - "Only use the planar surface bounded directly by C"
    - "Replace the line integral with a volume integral over the region enclosed by C"
  answer: 1
  explanation: "Stokes' theorem guarantees ∮_C F·dr = ∬_S (∇×F)·n dS for ANY surface S bounded by C — flat disk, hemisphere, saddle, anything. The freedom to choose S is the theorem's strategic power: pick whichever surface makes the flux integral tractable. Option C (using only the flat surface) is a special case, not a requirement."

- question: "A vector field F satisfies ∇×F = 0 everywhere. What does Stokes' theorem immediately imply about line integrals of F around closed curves?"
  type: multiple-choice
  options:
    - "∮_C F·dr = 1 for all closed curves (unit circulation)"
    - "∮_C F·dr = 0 for any closed curve in the domain"
    - "The field has no flux through any surface"
    - "The curl equals the divergence everywhere"
  answer: 1
  explanation: "If ∇×F = 0, Stokes gives ∮_C F·dr = ∬_S 0·n dS = 0. An irrotational field has zero circulation around every closed curve, which on simply connected domains is equivalent to the field being conservative and path-independent."

- question: "Stokes' theorem gives the same value for ∬_S (∇×F)·n dS regardless of which spanning surface S you choose, as long as S is bounded by the same closed curve C."
  type: true-false
  answer: true
  explanation: "Surface-independence is the theorem's deep content. It follows from ∇·(∇×F) = 0 always. Any two surfaces spanning C together form a closed surface; by the divergence theorem, the net flux of ∇×F through a closed surface equals the volume integral of ∇·(∇×F) — which is zero. So the flux through any two spanning surfaces is equal."

- question: "Stokes' theorem is a mostly separate result from Green's theorem, with no mathematical relationship between them."
  type: true-false
  answer: false
  explanation: "Green's theorem is a special case of Stokes' theorem applied to a flat region in ℝ². When the surface S is a planar region D and the boundary curve C lies in the plane, Stokes reduces exactly to Green's theorem. Both are instances of the same master result: ∫_∂Ω ω = ∫_Ω dω."

- question: "Explain why Stokes' theorem gives the same answer regardless of which spanning surface S you choose for a given boundary curve C."
  type: short-answer
  answer: "Because the curl is always divergence-free (∇·(∇×F) = 0). Any two different spanning surfaces S₁ and S₂ with the same boundary C together form a closed surface. By the divergence theorem, the net flux of ∇×F through a closed surface equals the volume integral of ∇·(∇×F) over the enclosed region — which is zero. So the flux through S₁ equals the flux through S₂."
  explanation: "The algebraic identity div(curl) = 0 is what makes the theorem strategically useful: you can freely choose whichever spanning surface simplifies the computation, guaranteed that the answer is independent of that choice."
```

## Explainer

You know Green's theorem: for a flat region D in ℝ² bounded by a closed curve C, the circulation of a 2D vector field around C equals the double integral of the 2D curl over D. **Stokes' theorem** generalizes this to three dimensions: the circulation of a 3D vector field around a closed curve C equals the flux of the **curl** ∇ × F through any surface S bounded by C. The formula ∮_C F · dr = ∬_S (∇ × F) · **n** dS encodes the same fundamental idea — boundary information equals interior information — but now the boundary is a curve in 3D and the interior is a surface.

The leap from Green's theorem to Stokes is replacing the flat region D with a curved surface S in ℝ³. The boundary of S is the closed curve C, and the surface can be any shape you like — a flat disk, a hemisphere, a saddle — as long as it spans C. The integrand on the right is the **flux of the curl**: you compute ∇ × F at each point on the surface (a vector measuring local rotation of the field), take its component perpendicular to the surface (dot with the unit normal **n**), and integrate against the surface area element dS. The remarkable non-obvious fact is that the result is the same regardless of which spanning surface you choose — this follows because the curl is divergence-free (∇ · (∇ × F) = 0), so switching surfaces changes the double integral by zero.

**Orientation** is the essential bookkeeping issue. The direction of traversal around C and the direction of the surface normal **n** must be consistent via the **right-hand rule**: curl the fingers of your right hand in the direction you traverse C, and your thumb points in the direction of **n**. Getting orientation wrong introduces a sign error, flipping the sign of the entire answer. In practice: fix the orientation of C, then choose **n** consistently; or fix **n** first, then traverse C in the direction given by the right-hand rule.

The strategic use of Stokes' theorem mirrors Green's theorem — trade a hard integral for an easier one. A complicated line integral in 3D can become a flux integral of the curl if the curl is simple (or zero). A complicated flux integral of a curl can become a line integral if the boundary curve is manageable. A powerful special case: when ∇ × F = **0** everywhere (the field is irrotational and hence conservative on simply connected domains), Stokes' theorem gives ∮_C F · dr = 0 for any closed curve — recovering path-independence. Green's theorem, Stokes' theorem, and the divergence theorem are all instances of one master result from differential geometry: the integral of a differential form over a boundary equals the integral of its exterior derivative over the interior.
