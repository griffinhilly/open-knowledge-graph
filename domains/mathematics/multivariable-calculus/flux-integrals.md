---
id: flux-integrals
title: Flux Integrals of Vector Fields
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: surface-integrals-scalar
  type: hard
builds-toward:
- stokes-theorem
- divergence-theorem
tags:
- flux
- surface-integral
stage: formal-systems
status: draft
---

# Flux Integrals of Vector Fields

## Core Idea
The flux of F through surface S: ∬_S F · dS = ∬_S F · n dS, where n is the unit normal. If S is parametrized, ∬_S F · dS = ∬_D F · (r_u × r_v) du dv. Flux measures flow rate through the surface.

## Questions

```yaml
- question: "A vector field F is everywhere tangent to a flat surface — every flow vector lies parallel to the surface at every point. What is the flux of F through this surface?"
  type: multiple-choice
  options:
    - "Maximum — the field is fully interacting with the surface at every point"
    - "Zero — only the component of F perpendicular to the surface contributes to flux"
    - "Positive or negative depending on the orientation chosen for the surface"
    - "Cannot be determined without explicitly computing the integral"
  answer: 1
  explanation: "Flux measures flow *through* a surface, not along it. Flow parallel to the surface skims past without crossing — like wind blowing horizontally past a vertical net, passing no air through the net. The flux integral computes F · n̂, the dot product of F with the surface normal. When F is tangent to the surface, it is perpendicular to n̂, so F · n̂ = 0 at every point. The integral of zero is zero. This is the physical content of the dot product in the flux formula."

- question: "When computing ∬_D F · (r_u × r_v) du dv, what does the cross product r_u × r_v provide?"
  type: multiple-choice
  options:
    - "The unit tangent vector to the boundary curve of the surface"
    - "A vector perpendicular to the surface whose magnitude encodes the local area scaling factor"
    - "The gradient of the flux function integrated over the domain D"
    - "The curl of the vector field F evaluated on the surface"
  answer: 1
  explanation: "The partial derivatives r_u and r_v span the tangent plane at each point of the surface. Their cross product r_u × r_v is therefore perpendicular to the surface (a normal vector), and its magnitude ‖r_u × r_v‖ is the area scaling factor — exactly the quantity that appeared as the denominator in scalar surface integrals. For flux, we use the full *vector* cross product (not normalized) as the area element dS = (r_u × r_v) du dv. This bundles the perpendicular direction and the area scale into one object, letting the dot product F · (r_u × r_v) extract the perpendicular component and weight it by area in a single step."

- question: "Reversing the orientation of a surface — swapping which side is 'positive' — changes the sign of the flux integral through that surface."
  type: true-false
  answer: true
  explanation: "Flux is a signed quantity: it is positive when flow is in the direction of the chosen normal, negative when flow opposes it. If you swap the orientation (equivalently, negate the normal vector n̂, or swap u and v in the parametrization so that r_u × r_v points the other way), then F · n̂ changes sign everywhere, and the integral changes sign. This is why orientation must be specified explicitly — for a closed surface like a sphere, the convention is outward normals; for open surfaces, the orientation is stated as part of the problem."

- question: "The flux integral measures the total strength (magnitude) of the vector field across a surface, summing how large F is at each point regardless of the field's direction."
  type: true-false
  answer: false
  explanation: "Flux is directional, not just a measure of magnitude. The flux integral computes ∬ F · n̂ dS — the dot product extracts only the component of F in the direction of the surface normal. A strong field flowing parallel to the surface contributes zero flux; a weaker field flowing straight through contributes fully. If flux measured total magnitude, ∬ ‖F‖ dS, a field circulating in the plane of the surface would produce nonzero flux — but physically, no flow passes through, so flux should be zero. The dot product is essential to the physical meaning."

- question: "Explain in physical terms why flux through a surface is computed using the dot product F · n̂, rather than simply integrating the magnitude of F over the surface."
  type: short-answer
  answer: "Flux measures how much of the field passes *through* the surface, not how strong the field is near it. Think of F as a fluid velocity field and the surface as a permeable membrane. Only the component of flow perpendicular to the membrane actually crosses it — flow parallel to the membrane slides along without passing through. The dot product F · n̂ isolates exactly this perpendicular component: it equals |F| cos θ, where θ is the angle between F and the surface normal. When F is parallel to the surface, θ = 90° and cos θ = 0, so no flow crosses. When F is perpendicular, θ = 0° and cos θ = 1, so all the flow crosses. Integrating ‖F‖ alone would count parallel flow as contributing to flux, which has no physical meaning."
  explanation: "The dot product is the mathematical tool that encodes directionality. Its role in the flux integral is not a formality — it is what makes the integral measure a physically meaningful quantity (flow rate through a surface) rather than an arbitrary field integral."
```

## Explainer

From scalar surface integrals, you know how to integrate a real-valued function over a surface — you weigh each area element dS by the function's value and sum. A **flux integral** extends this to vector fields: instead of a scalar function, you have a vector field F assigning a flow vector to every point in space, and you want to measure how much of that flow passes through the surface. Think of F as the velocity field of a fluid. Flux answers the question: how many liters per second pass through this membrane?

The physical insight is that only the component of F *perpendicular* to the surface contributes to flow through it. Flow parallel to the surface skims along without crossing. To isolate the perpendicular component, you take the dot product of F with the **unit normal** n̂ to the surface at each point. The scalar F · n̂ tells you the flow rate per unit area at that point (positive if flowing "outward," negative if flowing "inward"). The flux integral ∬_S F · n̂ dS then sums this rate over the entire surface. Choosing an orientation — which side of the surface is "positive" — amounts to choosing a consistent direction for n̂, and flux changes sign if you reverse the orientation.

To compute this in practice, you parametrize the surface as r(u, v) over a domain D in the uv-plane. The partial derivatives r_u and r_v span the tangent plane at each point, so their cross product r_u × r_v is perpendicular to the surface and its magnitude equals the area scaling factor — exactly the role played by the area element ‖r_u × r_v‖ du dv in scalar surface integrals. For flux, you take the *vector* area element **dS** = (r_u × r_v) du dv (without normalizing), so the integral becomes ∬_D F(r(u,v)) · (r_u × r_v) du dv. This bundles the dot product with the normal and the area scaling into a single expression, making computation direct.

Orientation choices matter carefully here. The cross product r_u × r_v points to one side of the surface; if you swap u and v, it points to the other side. For a closed surface like a sphere, the convention is outward-pointing normals; for an open surface like an upper hemisphere, you specify the orientation explicitly. Getting orientation wrong flips the sign of the answer — the flux of an outward-flowing field is positive for outward normals, negative if you accidentally use inward normals.

Flux integrals are the key ingredient in the two great theorems that follow: **Stokes' theorem** relates the flux of a curl through a surface to a line integral around its boundary, and the **Divergence theorem** relates the flux of a vector field through a closed surface to the triple integral of its divergence over the enclosed volume. Both theorems generalize the Fundamental Theorem of Calculus to higher dimensions, and both reduce abstract spatial relationships to computable integrals. Flux is the quantity that makes these connections precise.
