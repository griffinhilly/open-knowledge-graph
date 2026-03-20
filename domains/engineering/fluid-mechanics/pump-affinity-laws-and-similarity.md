---
id: pump-affinity-laws-and-similarity
title: Pump Affinity Laws and Geometric Similarity Scaling
domain: engineering
course: fluid-mechanics
prerequisites:
- id: similitude-and-scale-model-testing
  type: hard
- id: pump-system-curves
  type: hard
tags:
- affinity-laws
- scaling
- similarity
stage: advanced
status: draft
---

# Pump Affinity Laws and Geometric Similarity Scaling

## Core Idea
Affinity laws relate performance of geometrically similar pumps at different speeds and sizes: Q₂/Q₁ = (N₂/N₁)(D₂/D₁)³, H₂/H₁ = (N₂/N₁)²(D₂/D₁)², P₂/P₁ = (N₂/N₁)³(D₂/D₁)⁵. These scaling laws enable prediction of behavior without redesign, facilitating pump selection and speed-variation control (via variable-speed drives) for changing operating conditions. Efficiency is approximately preserved under affinity scaling.

## Explainer

Pump affinity laws are the direct application of geometric similarity — which you studied in similitude and scale model testing — to rotating turbomachinery. If two pumps are geometrically similar (same shape, just different sizes or operating speeds) and operate at the same **specific speed** (the same dimensionless operating point), then dimensional analysis guarantees that their performance parameters scale in fixed ratios. The affinity laws make those ratios explicit.

The dimensional reasoning behind each law is straightforward. Flow rate Q has units of volume per time; for a pump, the relevant velocity is the impeller tip velocity, which scales as ND (where N is rotational speed and D is impeller diameter). The relevant area scales as D². So Q ∝ ND × D² = ND³ — this is the first affinity law. **Head** H (pressure rise per unit weight) has units of velocity squared divided by g, and the velocity scale is again ND, giving H ∝ (ND)² = N²D². **Power** P equals ρgQH, which scales as ρ × ND³ × N²D² = ρN³D⁵ — the third law.

The most common engineering application is speed variation on a fixed pump (D₁ = D₂, so the diameter terms cancel). You know from pump-system curves that the operating point is where the pump curve intersects the system resistance curve. When speed decreases from N₁ to N₂, the entire pump curve shifts: every flow point scales by N₂/N₁ and every head point scales by (N₂/N₁)². The shift traces a parabolic locus through the operating points at different speeds — called the **affinity parabola**. Power scales as (N₂/N₁)³, which is the famous cubic law. Reducing speed by 20% (N₂/N₁ = 0.8) cuts power to 0.8³ = 0.51 of the original — a 49% energy savings. This is why variable-speed drives are so valuable for systems that frequently run at partial flow.

The efficiency-preservation assumption — that geometrically similar pumps operating at similar specific speeds have similar efficiencies — enables scaling from catalog data. If a manufacturer tested a pump at one speed and you need performance at another, affinity scaling gives the predicted curve. The assumption breaks down at very different scales (viscous losses scale differently from pressure forces), near the ends of the operating range, or when impeller trim (cutting the impeller diameter) is used heavily. For catalog-based pump selection, the procedure is: identify a candidate pump at its tested speed, use affinity scaling to find the speed or impeller size that hits your required (Q, H) operating point, then verify the efficiency at that scaled point against the manufacturer's curve.
