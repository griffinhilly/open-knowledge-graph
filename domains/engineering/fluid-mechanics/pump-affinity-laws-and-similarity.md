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
stage: expert
status: validated
---

# Pump Affinity Laws and Geometric Similarity Scaling

## Core Idea
Affinity laws relate performance of geometrically similar pumps at different speeds and sizes: Q₂/Q₁ = (N₂/N₁)(D₂/D₁)³, H₂/H₁ = (N₂/N₁)²(D₂/D₁)², P₂/P₁ = (N₂/N₁)³(D₂/D₁)⁵. These scaling laws enable prediction of behavior without redesign, facilitating pump selection and speed-variation control (via variable-speed drives) for changing operating conditions. Efficiency is approximately preserved under affinity scaling.

## Questions

```yaml
- question: "A centrifugal pump running at 1200 RPM consumes 100 kW. The operator installs a variable-speed drive and reduces speed to 900 RPM to lower flow. What is the new power consumption?"
  type: multiple-choice
  options:
    - "75 kW — power scales linearly with speed"
    - "56.25 kW — power scales as the square of the speed ratio"
    - "42.2 kW — power scales as the cube of the speed ratio"
    - "30 kW — power scales as the fourth power due to combined head and flow effects"
  answer: 2
  explanation: "Power follows the cubic affinity law: P₂/P₁ = (N₂/N₁)³. The speed ratio is 900/1200 = 0.75, so P₂ = 100 × 0.75³ = 100 × 0.422 = 42.2 kW. This is the famous result that makes variable-speed drives so energy-effective: a 25% speed reduction cuts power nearly in half. The linear and square-law options represent common misconceptions — mistaking power for flow or head scaling respectively. The cubic relationship arises because power equals ρgQH, and both Q (∝ N) and H (∝ N²) scale with speed, giving P ∝ N × N² = N³."

- question: "When a pump's speed is varied while its diameter stays constant, the operating points at different speeds in the Q-H diagram:"
  type: multiple-choice
  options:
    - "Fall on a horizontal line, since head depends only on speed and not flow"
    - "Fall on a parabola through the origin — the affinity parabola — because H ∝ Q² at each speed ratio"
    - "Fall on a straight line through the origin with slope proportional to the speed ratio"
    - "Are unpredictable without knowing the system curve, since it shifts with speed"
  answer: 1
  explanation: "Since Q ∝ N and H ∝ N², eliminating N gives H ∝ Q² — the relationship between head and flow at corresponding operating points is parabolic. As speed changes, the operating point traces this parabola, called the affinity parabola, through the Q-H diagram. This geometric insight is practically useful: you can predict where the pump will operate at any speed by finding the intersection of the affinity parabola with the pump curve at the new speed. The system curve does not shift when speed changes — it is a property of the piping, not the pump."

- question: "Reducing pump speed by 20% reduces power consumption by approximately 49%, because power scales as the cube of the speed ratio."
  type: true-false
  answer: true
  explanation: "With N₂/N₁ = 0.8, P₂/P₁ = 0.8³ = 0.512 — power drops to about 51% of its original value, a savings of ~49%. This is the core engineering argument for variable-speed drives in systems that frequently operate at partial flow: the energy savings are disproportionately large compared to the speed reduction. A pump that runs at 80% speed for half its operating hours saves nearly half the energy during those hours."

- question: "The affinity laws apply equally to any two pumps regardless of their shape, size, or specific speed, as long as they are both centrifugal pumps."
  type: true-false
  answer: false
  explanation: "The affinity laws require geometric similarity — the pumps must be the same shape (scaled versions of each other) and must operate at the same specific speed (the same dimensionless point on their performance curves). They do not hold between geometrically dissimilar pumps, nor between a pump operating near its best-efficiency point and one operating at the extremes of its range. When significant impeller trimming is applied, viscous scaling effects also cause the efficiency to shift, further limiting the laws' accuracy."

- question: "Why does power scale as the cube of rotational speed rather than linearly, and what practical implication does this have for systems that frequently operate at partial flow?"
  type: short-answer
  answer: "Power equals ρgQH. Under affinity scaling with constant diameter, Q scales as N (first law) and H scales as N² (second law), so P ∝ ρg × N × N² = ρgN³ — the cubic relationship. Because both flow and head decrease together as speed falls, the power reduction is multiplicative. Practically, this means variable-speed drives are highly effective for systems that frequently operate below design flow: reducing speed by just 20% cuts power nearly in half. Systems with seasonally variable demand — HVAC chilled water loops, building pressure-boosting, irrigation — capture enormous energy savings by matching pump speed to actual demand rather than throttling with control valves (which waste energy by dissipating excess head across the valve)."
  explanation: "The contrast with throttle control is instructive: a throttle valve reduces flow by increasing system resistance, forcing the pump to work against higher head. The pump still runs at full speed and consumes most of its rated power, but most of that energy is wasted as heat across the valve. Variable-speed control instead reduces the speed, shifting the entire pump curve downward. The operating point moves along the system curve at lower Q and lower H, with dramatically lower power — the affinity laws ensure all three quantities decrease together."
```

## Explainer

Pump affinity laws are the direct application of geometric similarity — which you studied in similitude and scale model testing — to rotating turbomachinery. If two pumps are geometrically similar (same shape, just different sizes or operating speeds) and operate at the same **specific speed** (the same dimensionless operating point), then dimensional analysis guarantees that their performance parameters scale in fixed ratios. The affinity laws make those ratios explicit.

The dimensional reasoning behind each law is straightforward. Flow rate Q has units of volume per time; for a pump, the relevant velocity is the impeller tip velocity, which scales as ND (where N is rotational speed and D is impeller diameter). The relevant area scales as D². So Q ∝ ND × D² = ND³ — this is the first affinity law. **Head** H (pressure rise per unit weight) has units of velocity squared divided by g, and the velocity scale is again ND, giving H ∝ (ND)² = N²D². **Power** P equals ρgQH, which scales as ρ × ND³ × N²D² = ρN³D⁵ — the third law.

The most common engineering application is speed variation on a fixed pump (D₁ = D₂, so the diameter terms cancel). You know from pump-system curves that the operating point is where the pump curve intersects the system resistance curve. When speed decreases from N₁ to N₂, the entire pump curve shifts: every flow point scales by N₂/N₁ and every head point scales by (N₂/N₁)². The shift traces a parabolic locus through the operating points at different speeds — called the **affinity parabola**. Power scales as (N₂/N₁)³, which is the famous cubic law. Reducing speed by 20% (N₂/N₁ = 0.8) cuts power to 0.8³ = 0.51 of the original — a 49% energy savings. This is why variable-speed drives are so valuable for systems that frequently run at partial flow.

The efficiency-preservation assumption — that geometrically similar pumps operating at similar specific speeds have similar efficiencies — enables scaling from catalog data. If a manufacturer tested a pump at one speed and you need performance at another, affinity scaling gives the predicted curve. The assumption breaks down at very different scales (viscous losses scale differently from pressure forces), near the ends of the operating range, or when impeller trim (cutting the impeller diameter) is used heavily. For catalog-based pump selection, the procedure is: identify a candidate pump at its tested speed, use affinity scaling to find the speed or impeller size that hits your required (Q, H) operating point, then verify the efficiency at that scaled point against the manufacturer's curve.
