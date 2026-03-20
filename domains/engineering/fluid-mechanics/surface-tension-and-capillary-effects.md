---
id: surface-tension-and-capillary-effects
title: Surface Tension and Capillary Phenomena
domain: engineering
course: fluid-mechanics
prerequisites:
- id: fluid-properties-and-continuum
  type: hard
tags:
- surface-tension
- interfacial
- capillary
stage: advanced
status: draft
---

# Surface Tension and Capillary Phenomena

## Core Idea
Surface tension σ (energy per unit area) arises from molecular cohesion at fluid-gas or fluid-fluid interfaces, acting as a membrane under tension. Capillary rise in narrow tubes follows h = (2σ cosθ)/(ρgr), where θ is the contact angle and r is the tube radius. These effects dominate in small-scale flows (high surface-area-to-volume ratio) and can significantly alter transport in microfluidics, porous media, and thin films.

## How It's Best Learned
Measure capillary rise in tubes of different diameters and materials (wettable glass versus non-wettable plastic). Calculate the rise height theoretically and compare to measurements. Observe the shape of interfaces (menisci) and relate them to contact angles and pressure discontinuity (Young-Laplace equation).

## Explainer

From your study of fluid properties, you know that molecules in a liquid are attracted to each other by **cohesive forces** — the intermolecular attractions that hold the liquid together. In the bulk of the liquid, these forces act equally in all directions and cancel out. But a molecule sitting at the interface between the liquid and air has neighbors below and beside it, but not above. The missing cohesive force on one side creates a net inward pull on surface molecules, which manifests macroscopically as **surface tension σ** — a force per unit length (N/m) acting along the interface, or equivalently, an energy per unit area (J/m²) representing the cost of creating new surface. Think of it as the liquid trying to minimize its surface area, much like a stretched elastic membrane.

The **contact angle θ** encodes the competition between cohesive forces (liquid-to-liquid) and **adhesive forces** (liquid-to-solid). When water sits on clean glass, adhesion to the glass surface is strong — water wets the glass, the contact angle is small (< 90°), and the liquid surface curves upward at the wall (concave meniscus). On a waxed or hydrophobic surface, cohesion dominates, the contact angle is large (> 90°), and the meniscus curves downward (convex). Mercury on glass is the classic non-wetting case: θ ≈ 140°, so mercury forms a convex meniscus and depresses inside narrow tubes rather than rising.

Capillary rise and depression are consequences of these curved menisci. A curved liquid-gas interface has a pressure discontinuity across it — the **Young-Laplace equation** quantifies this: ΔP = σ(1/R₁ + 1/R₂), where R₁ and R₂ are the principal radii of curvature. For a spherical meniscus in a tube of radius r, this gives ΔP = 2σ/r directed inward (for a concave meniscus, the liquid is under lower pressure than the gas above it). This pressure deficit pulls the liquid column upward until the hydrostatic weight of the raised column, ρgh·πr², exactly balances the upward surface tension force pulling around the perimeter, 2πr·σ·cosθ. Setting these equal yields the **capillary rise formula** h = (2σ cosθ)/(ρgr). Two key insights from this formula: rise height scales inversely with tube radius (tiny capillaries pull liquid much higher), and cosθ explains why hydrophobic surfaces cause depression instead of rise.

These effects are negligible in large-diameter pipes but dominate at the millimeter scale and below. In microfluidic chips, capillary forces drive fluid flow without pumps — engineers deliberately engineer channel surface chemistry to control wettability. In porous media like soil or paper, capillary pressure allows water to wick against gravity. In inkjet printing, surface tension controls droplet formation and wetting on the substrate. Whenever you encounter a problem involving thin films, droplets, bubbles, or flow through fine passages, surface tension is likely the dominant physics — the Bond number (gravitational to surface tension forces) and Weber number (inertial to surface tension forces) quantify whether you can safely ignore it.

