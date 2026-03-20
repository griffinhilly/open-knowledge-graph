---
id: surface-tension-and-capillarity
title: Surface Tension and Capillarity
domain: physics
course: thermodynamics
prerequisites:
- id: gibbs-free-energy
  type: hard
builds-toward:
- phase-equilibrium-coexistence
tags:
- interfaces
- surface-effects
- intermolecular-forces
stage: advanced
status: draft
---

# Surface Tension and Capillarity

## Core Idea
Surface tension γ arises from unbalanced intermolecular forces at an interface, creating an excess Gibbs free energy per unit area; it has units of N/m or J/m². Capillarity refers to the spontaneous rise or fall of liquids in narrow tubes, driven by surface tension and the balance of adhesive forces between liquid and solid versus cohesive forces within the liquid. The capillary length scale √(γ/ρg) determines when surface tension effects dominate over gravity.

## How It's Best Learned
Measure surface tension using capillary rise or hanging drop methods. Observe contact angles and wetting behavior. Calculate capillary length scales.

## Common Misconceptions
- Thinking surface tension is purely a mechanical effect (it has thermodynamic origins).
- Confusing surface tension with interfacial tension between two liquids.
- Assuming water has the highest surface tension among common liquids (mercury does).

## Explainer

You already understand Gibbs free energy as the thermodynamic potential that governs equilibrium at constant temperature and pressure. Surface tension emerges when you ask: what happens to G when you account for the energy cost of creating an interface between two phases? Molecules in the bulk of a liquid are surrounded by neighbors on all sides and their intermolecular interactions are fully satisfied. Molecules at the surface, however, have neighbors on only one side — the other side faces vapor or vacuum. These surface molecules are in a higher-energy configuration. The **surface tension** γ (also called the **interfacial free energy**) quantifies this excess: it is the Gibbs free energy per unit area required to create new surface, with units J/m² or equivalently N/m.

The mechanical picture and the thermodynamic picture are two views of the same phenomenon. Mechanically, γ appears as a force per unit length pulling along the surface, trying to minimize area (like a stretched elastic membrane). Thermodynamically, γ = (∂G/∂A)_{T,P,n}, the partial derivative of G with respect to surface area. These are consistent: minimizing G at constant T and P drives the system to minimize surface area. This is why liquid droplets are spherical (the shape that minimizes area for a given volume), why bubbles are round, and why small droplets merge when they touch.

**Capillarity** is the manifestation of surface tension in confined geometry. In a narrow tube of radius r, the liquid-solid **adhesion** (liquid molecules attracted to tube wall) competes with liquid-liquid **cohesion** (liquid molecules attracted to each other). If adhesion dominates (contact angle θ < 90°, as with water in glass), the liquid wets the wall, the meniscus curves upward at the edges, and liquid is pulled upward into the tube. The equilibrium capillary rise h is set by balancing the surface tension force 2πrγ cosθ against the weight of the liquid column πr²hρg, giving h = 2γ cosθ/(ρgr). Notice that h ∝ 1/r: narrower tubes draw liquid higher. If cohesion dominates (θ > 90°, as with mercury in glass), the meniscus inverts and the liquid is depressed below the external level.

The natural length scale of capillarity is the **capillary length** λ_c = √(γ/ρg). For water, λ_c ≈ 2.7 mm. Objects smaller than λ_c are dominated by surface effects; objects larger than λ_c are dominated by gravity. This is why small insects can walk on water (their legs are lighter than the upward surface-tension force), why morning dew forms hemispherical beads on leaves (contact angle effects), and why water menisci in xylem vessels allow trees to draw water 100 meters upward against gravity. The **Young-Laplace equation** ΔP = γ(1/R₁ + 1/R₂) — the pressure jump across a curved interface with principal radii of curvature R₁ and R₂ — unifies all these phenomena in a single thermodynamic identity derived directly from the Gibbs free energy of the interface.
