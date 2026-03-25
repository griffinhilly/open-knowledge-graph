---
id: surface-tension-and-capillarity
title: Surface Tension and Capillarity
domain: physics
course: thermodynamics
prerequisites:
- id: gibbs-free-energy
  type: hard
- id: virial-equation-and-intermolecular-forces
  type: soft
builds-toward:
- phase-equilibrium-coexistence
tags:
- interfaces
- surface-effects
- intermolecular-forces
stage: advanced
status: validated
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

## Questions

```yaml
- question: "Water (contact angle θ ≈ 20° with glass) rises in a glass capillary tube. Mercury (contact angle θ ≈ 140° with glass) is placed in an identical tube. What happens to the mercury, and why?"
  type: multiple-choice
  options:
    - "Mercury rises like water, but more slowly due to its much greater density"
    - "Mercury stays level — its very high surface tension exactly balances the adhesive and cohesive forces"
    - "Mercury rises even higher than water because its surface tension is larger"
    - "Mercury is depressed below the external liquid level because cohesive forces among mercury atoms dominate over adhesion to glass, causing the meniscus to curve downward and net force to push down"
  answer: 3
  explanation: "The direction of capillary effect depends on the contact angle θ. When θ < 90° (water-glass), adhesion to the wall dominates, the meniscus curves upward, and liquid is pulled up. When θ > 90° (mercury-glass), cohesion dominates, the meniscus curves downward, and the liquid is pushed *down* — depression. The capillary rise formula h = 2γ cosθ/(ρgr) gives negative h when θ > 90° (since cosθ < 0), confirming depression. High surface tension (mercury has γ ≈ 490 mN/m vs. water's 72 mN/m) amplifies the effect in magnitude but doesn't change its direction, which is governed by the contact angle."

- question: "Water rises to height h in a capillary tube of radius r. The tube is replaced with one of radius r/2 (half the original). What is the new capillary rise height?"
  type: multiple-choice
  options:
    - "h/2 — narrower tubes offer less area for adhesion"
    - "h — capillary rise depends on fluid properties and contact angle, not tube radius"
    - "2h — capillary rise is inversely proportional to tube radius (h ∝ 1/r)"
    - "4h — cross-sectional area decreases fourfold, amplifying the rise"
  answer: 2
  explanation: "From h = 2γ cosθ/(ρgr), the rise height is inversely proportional to r. Halving r doubles h. The physical reasoning: with smaller r, the surface tension force (proportional to circumference, 2πrγ cosθ) decreases, but the weight of liquid lifted (proportional to cross-sectional area, πr²hρg) decreases faster (as r²). At equilibrium, h must increase to compensate, and the math gives h ∝ 1/r. This is why plants can draw water 100 meters up through narrow xylem vessels but a bucket cannot."

- question: "Surface tension can be understood both as a force per unit length (N/m) acting along an interface and as the Gibbs free energy cost per unit area (J/m²) of creating new surface — these two descriptions are physically equivalent."
  type: true-false
  answer: true
  explanation: "N/m and J/m² are dimensionally identical (J = N·m, so J/m² = N·m/m² = N/m). The equivalence is not just dimensional — it reflects the same underlying physics viewed in two frames. Mechanically, γ is a force per unit length pulling the surface inward, minimizing area. Thermodynamically, γ = (∂G/∂A)_{T,P,n}, the energy cost of expanding the surface. Both descriptions say the same thing: the system minimizes surface area to minimize free energy. The driving force for droplet sphericity, bubble formation, and capillary rise all follow from either framing."

- question: "Water has the highest surface tension of any common liquid."
  type: true-false
  answer: false
  explanation: "Mercury has a much higher surface tension than water: γ_mercury ≈ 485–490 mN/m, while γ_water ≈ 72 mN/m at room temperature. Mercury's exceptionally strong metallic cohesion (delocalized electron interactions, not just van der Waals forces) makes its surface molecules far more strongly attracted to each other than to almost any interface. This is why mercury forms convex menisci in glass (cohesion >> adhesion to glass) and why liquid mercury beads into nearly spherical droplets. Water has unusually high surface tension *for a molecular liquid* (due to hydrogen bonding), but mercury exceeds it."

- question: "Explain the thermodynamic origin of surface tension. Why are surface molecules in a higher-energy state than bulk molecules, and how does this relate to the tendency of liquids to minimize their surface area?"
  type: short-answer
  answer: "In the bulk of a liquid, each molecule is surrounded by neighbors on all sides, and all intermolecular attractions are satisfied. A molecule at the surface has neighbors on only one side — the other side faces vapor or vacuum — so its intermolecular interactions are only partially satisfied. This incomplete coordination places surface molecules in a higher-energy state than bulk molecules. The excess energy per unit area is the surface tension γ = (∂G/∂A)_{T,P,n}. Since systems minimize Gibbs free energy at constant T and P, a liquid spontaneously minimizes its surface area to reduce the number of energetically unfavorable surface molecules — which is why droplets are spherical, bubbles are round, and liquids climb capillary tubes only as far as the free-energy balance requires."
  explanation: "The thermodynamic framing makes clear why surface tension is not a purely mechanical property but reflects intermolecular physics. Strong cohesive forces (mercury) → high γ; weaker cohesion (organic solvents) → lower γ. Temperature reduces γ because thermal energy partially compensates the energy penalty of surface molecules — the surface becomes less thermodynamically costly as kT becomes comparable to the intermolecular binding energy."
```

## Explainer

You already understand Gibbs free energy as the thermodynamic potential that governs equilibrium at constant temperature and pressure. Surface tension emerges when you ask: what happens to G when you account for the energy cost of creating an interface between two phases? Molecules in the bulk of a liquid are surrounded by neighbors on all sides and their intermolecular interactions are fully satisfied. Molecules at the surface, however, have neighbors on only one side — the other side faces vapor or vacuum. These surface molecules are in a higher-energy configuration. The **surface tension** γ (also called the **interfacial free energy**) quantifies this excess: it is the Gibbs free energy per unit area required to create new surface, with units J/m² or equivalently N/m.

The mechanical picture and the thermodynamic picture are two views of the same phenomenon. Mechanically, γ appears as a force per unit length pulling along the surface, trying to minimize area (like a stretched elastic membrane). Thermodynamically, γ = (∂G/∂A)_{T,P,n}, the partial derivative of G with respect to surface area. These are consistent: minimizing G at constant T and P drives the system to minimize surface area. This is why liquid droplets are spherical (the shape that minimizes area for a given volume), why bubbles are round, and why small droplets merge when they touch.

**Capillarity** is the manifestation of surface tension in confined geometry. In a narrow tube of radius r, the liquid-solid **adhesion** (liquid molecules attracted to tube wall) competes with liquid-liquid **cohesion** (liquid molecules attracted to each other). If adhesion dominates (contact angle θ < 90°, as with water in glass), the liquid wets the wall, the meniscus curves upward at the edges, and liquid is pulled upward into the tube. The equilibrium capillary rise h is set by balancing the surface tension force 2πrγ cosθ against the weight of the liquid column πr²hρg, giving h = 2γ cosθ/(ρgr). Notice that h ∝ 1/r: narrower tubes draw liquid higher. If cohesion dominates (θ > 90°, as with mercury in glass), the meniscus inverts and the liquid is depressed below the external level.

The natural length scale of capillarity is the **capillary length** λ_c = √(γ/ρg). For water, λ_c ≈ 2.7 mm. Objects smaller than λ_c are dominated by surface effects; objects larger than λ_c are dominated by gravity. This is why small insects can walk on water (their legs are lighter than the upward surface-tension force), why morning dew forms hemispherical beads on leaves (contact angle effects), and why water menisci in xylem vessels allow trees to draw water 100 meters upward against gravity. The **Young-Laplace equation** ΔP = γ(1/R₁ + 1/R₂) — the pressure jump across a curved interface with principal radii of curvature R₁ and R₂ — unifies all these phenomena in a single thermodynamic identity derived directly from the Gibbs free energy of the interface.
