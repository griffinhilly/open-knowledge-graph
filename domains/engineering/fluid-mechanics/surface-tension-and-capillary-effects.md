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
stage: formal-systems
status: validated
---

# Surface Tension and Capillary Phenomena

## Core Idea
Surface tension σ (energy per unit area) arises from molecular cohesion at fluid-gas or fluid-fluid interfaces, acting as a membrane under tension. Capillary rise in narrow tubes follows h = (2σ cosθ)/(ρgr), where θ is the contact angle and r is the tube radius. These effects dominate in small-scale flows (high surface-area-to-volume ratio) and can significantly alter transport in microfluidics, porous media, and thin films.

## How It's Best Learned
Measure capillary rise in tubes of different diameters and materials (wettable glass versus non-wettable plastic). Calculate the rise height theoretically and compare to measurements. Observe the shape of interfaces (menisci) and relate them to contact angles and pressure discontinuity (Young-Laplace equation).

## Questions

```yaml
- question: "Two glass tubes are dipped vertically into water — one with radius 0.5 mm and one with radius 2 mm. Compared to the wider tube, the narrower tube will show:"
  type: multiple-choice
  options:
    - "Lower capillary rise, because less water fits in the narrower tube"
    - "The same capillary rise, because surface tension is a property of the liquid, not the tube"
    - "Higher capillary rise, because h ∝ 1/r and smaller radius means greater rise"
    - "Higher capillary rise only if the tube material has a smaller contact angle"
  answer: 2
  explanation: "The capillary rise formula h = 2σ cosθ / (ρgr) shows rise height is inversely proportional to tube radius r. The narrower tube (r = 0.5 mm) rises four times higher than the 2 mm tube. The physical reason: surface tension force acts around the tube perimeter (2πr) while the weight of liquid resisting it scales with the cross-sectional area (πr²). As r shrinks, perimeter shrinks linearly but area shrinks quadratically, so the surface tension force wins more and more — smaller tubes pull liquid higher."

- question: "Mercury is poured into a narrow glass tube. What happens, and why?"
  type: multiple-choice
  options:
    - "Mercury rises above the external level, just like water, because surface tension acts the same way in all liquids"
    - "Mercury stays level with the external surface because its high density cancels the surface tension effect"
    - "Mercury depresses below the external level, forming a convex meniscus, because its contact angle with glass exceeds 90°"
    - "Mercury rises slightly then falls back to equilibrium after the gas dissolved in mercury escapes"
  answer: 2
  explanation: "Mercury is a non-wetting liquid on glass: its contact angle θ ≈ 140°, making cosθ negative. The capillary formula h = 2σ cosθ / (ρgr) gives a negative h — depression rather than rise. Physically, mercury's cohesive forces (liquid-to-liquid) greatly exceed its adhesive forces to glass (liquid-to-solid), so the liquid curves away from the wall, forming a convex meniscus. The Young-Laplace pressure jump pushes mercury down inside the tube rather than pulling it up."

- question: "Surface tension is a bulk property of a liquid — it depends on the total volume of liquid present, so a larger body of liquid has higher surface tension than a small droplet."
  type: true-false
  answer: false
  explanation: "Surface tension σ is an intensive property — it is a property of the interface itself, characterizing the energy per unit area (J/m²) required to create new surface. Its value depends on the molecular identity of the two phases in contact and temperature, not on the total volume of liquid. A large tank of water and a tiny droplet have the same σ ≈ 0.072 N/m at room temperature. What changes with size is the total surface energy (σ × area), not the surface tension itself."

- question: "Capillary rise height is inversely proportional to tube radius — halving the radius doubles the rise height."
  type: true-false
  answer: true
  explanation: "This follows directly from h = 2σ cosθ / (ρgr): h ∝ 1/r, so halving r doubles h. This relationship is why capillary action is so significant in fine-pored materials (soil, paper, plant xylem) and negligible in large pipes. It also explains why engineers designing microfluidic devices must account for capillary effects that would be completely irrelevant at larger scales — the physics is the same, but the relative importance shifts dramatically with scale."

- question: "Explain why the contact angle θ determines whether a liquid rises or falls in a capillary tube, and what physical property of the system it encodes."
  type: short-answer
  answer: "The contact angle encodes the balance between adhesive forces (liquid-to-solid) and cohesive forces (liquid-to-liquid). When adhesion dominates (θ < 90°, e.g., water on glass), the liquid spreads along the wall and curves concave upward at the meniscus. The Young-Laplace pressure discontinuity across this curved interface creates lower pressure inside the liquid than in the gas above, pulling the column upward. When cohesion dominates (θ > 90°, e.g., mercury on glass), the liquid resists contact with the wall, curves convex downward, and the pressure inside the liquid exceeds atmospheric, pushing the column down. At θ = 90°, cosθ = 0 and there is no net capillary effect."
  explanation: "The contact angle is the observable signature of the surface energy balance at the three-phase contact line (solid-liquid-gas). The capillary rise formula makes this explicit: h = 2σ cosθ / (ρgr). For θ < 90°, cosθ > 0 and h > 0 (rise); for θ > 90°, cosθ < 0 and h < 0 (depression). The cos factor precisely quantifies how much of the surface tension force is directed vertically — at θ = 0° (perfect wetting), the full surface tension acts upward; at θ = 180° (perfect non-wetting), it acts fully downward."
```

## Explainer

From your study of fluid properties, you know that molecules in a liquid are attracted to each other by **cohesive forces** — the intermolecular attractions that hold the liquid together. In the bulk of the liquid, these forces act equally in all directions and cancel out. But a molecule sitting at the interface between the liquid and air has neighbors below and beside it, but not above. The missing cohesive force on one side creates a net inward pull on surface molecules, which manifests macroscopically as **surface tension σ** — a force per unit length (N/m) acting along the interface, or equivalently, an energy per unit area (J/m²) representing the cost of creating new surface. Think of it as the liquid trying to minimize its surface area, much like a stretched elastic membrane.

The **contact angle θ** encodes the competition between cohesive forces (liquid-to-liquid) and **adhesive forces** (liquid-to-solid). When water sits on clean glass, adhesion to the glass surface is strong — water wets the glass, the contact angle is small (< 90°), and the liquid surface curves upward at the wall (concave meniscus). On a waxed or hydrophobic surface, cohesion dominates, the contact angle is large (> 90°), and the meniscus curves downward (convex). Mercury on glass is the classic non-wetting case: θ ≈ 140°, so mercury forms a convex meniscus and depresses inside narrow tubes rather than rising.

Capillary rise and depression are consequences of these curved menisci. A curved liquid-gas interface has a pressure discontinuity across it — the **Young-Laplace equation** quantifies this: ΔP = σ(1/R₁ + 1/R₂), where R₁ and R₂ are the principal radii of curvature. For a spherical meniscus in a tube of radius r, this gives ΔP = 2σ/r directed inward (for a concave meniscus, the liquid is under lower pressure than the gas above it). This pressure deficit pulls the liquid column upward until the hydrostatic weight of the raised column, ρgh·πr², exactly balances the upward surface tension force pulling around the perimeter, 2πr·σ·cosθ. Setting these equal yields the **capillary rise formula** h = (2σ cosθ)/(ρgr). Two key insights from this formula: rise height scales inversely with tube radius (tiny capillaries pull liquid much higher), and cosθ explains why hydrophobic surfaces cause depression instead of rise.

These effects are negligible in large-diameter pipes but dominate at the millimeter scale and below. In microfluidic chips, capillary forces drive fluid flow without pumps — engineers deliberately engineer channel surface chemistry to control wettability. In porous media like soil or paper, capillary pressure allows water to wick against gravity. In inkjet printing, surface tension controls droplet formation and wetting on the substrate. Whenever you encounter a problem involving thin films, droplets, bubbles, or flow through fine passages, surface tension is likely the dominant physics — the Bond number (gravitational to surface tension forces) and Weber number (inertial to surface tension forces) quantify whether you can safely ignore it.

