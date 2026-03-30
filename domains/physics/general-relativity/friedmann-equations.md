---
id: friedmann-equations
title: Friedmann Equations (Cosmology)
domain: physics
course: general-relativity
prerequisites:
- id: einstein-field-equations
  type: hard
- id: robertson-walker-metric
  type: hard
- id: stress-energy-tensor
  type: hard
tags:
- friedmann-equations
- cosmology
- expansion
- hubble-parameter
- critical-density
stage: expert
status: validated
---

# Friedmann Equations (Cosmology)

## Core Idea
The Friedmann equations are the Einstein field equations applied to a homogeneous, isotropic universe described by the Robertson-Walker metric. The first Friedmann equation (ȧ/a)² = (8πG/3)ρ - kc²/a² + Λ/3 relates the expansion rate H = ȧ/a (Hubble parameter) to the total energy density ρ, the spatial curvature parameter k, and the cosmological constant Λ. The second (acceleration) equation ä/a = -(4πG/3)(ρ + 3p/c²) + Λ/3 determines whether the expansion is accelerating or decelerating. Together with an equation of state relating pressure to density, they form a complete dynamical system for the scale factor a(t). These equations are the foundation of the standard ΛCDM cosmological model and describe the expansion history of the universe from the Big Bang to the present accelerating expansion.

## Questions

```yaml
- question: "The first Friedmann equation can be rewritten as Ω_total - 1 = kc²/(a²H²), where Ω_total = ρ/ρ_crit. What is the critical density ρ_crit, and what does it determine?"
  type: multiple-choice
  options:
    - "ρ_crit = 3H²/(8πG) — it determines whether the universe is spatially flat (k=0), positively curved (k=+1), or negatively curved (k=-1)"
    - "ρ_crit = c²/(8πG) — it determines the age of the universe"
    - "ρ_crit = H²/(4πG) — it determines whether the universe will expand forever"
    - "ρ_crit = 3H/(8πG) — it determines the deceleration parameter"
  answer: 0
  explanation: "The critical density ρ_crit = 3H²/(8πG) is the density at which the universe is spatially flat (k = 0). If ρ > ρ_crit, the universe is positively curved (k = +1, closed); if ρ < ρ_crit, it is negatively curved (k = -1, open). The density parameter Ω = ρ/ρ_crit is the central observable in cosmology. Current observations give Ω_total ≈ 1.000 ± 0.002, indicating the universe is very close to spatially flat. The present critical density is about 9.5 × 10⁻²⁷ kg/m³ — roughly 6 hydrogen atoms per cubic meter."

- question: "In a universe containing only matter (p = 0, Λ = 0, k = 0), the scale factor grows as a(t) ∝ t^{2/3}."
  type: true-false
  answer: true
  explanation: "For a flat, matter-dominated universe with Λ = 0, the first Friedmann equation gives (ȧ/a)² = (8πG/3)ρ. Since matter density dilutes as ρ ∝ a⁻³ (volume expansion), this becomes ȧ² ∝ a⁻¹, which integrates to a(t) ∝ t^{2/3}. The expansion decelerates (ä < 0) because gravity slows it down. For comparison, a radiation-dominated universe (p = ρc²/3) gives a(t) ∝ t^{1/2}, and a cosmological-constant-dominated universe gives a(t) ∝ exp(Ht), exponential expansion."

- question: "Explain why the second Friedmann equation shows that ordinary matter and radiation always decelerate the expansion, while a cosmological constant accelerates it."
  type: short-answer
  answer: "The acceleration equation ä/a = -(4πG/3)(ρ + 3p/c²) + Λ/3 shows that the contribution of matter/radiation to ä is proportional to -(ρ + 3p/c²). For ordinary matter (p ≥ 0), ρ + 3p/c² > 0, so the matter contribution is negative — the expansion decelerates. For radiation (p = ρc²/3), the deceleration is even stronger. The cosmological constant Λ contributes +Λ/3, which is positive (for Λ > 0) and drives acceleration. Equivalently, a cosmological constant acts like a fluid with equation of state p = -ρc², giving ρ + 3p/c² = ρ - 3ρ = -2ρ < 0, which means its 'gravitational' effect is repulsive. The observed acceleration of cosmic expansion (discovered 1998) requires Λ > 0 or an equivalent dark energy component."
  explanation: "The key insight is that in GR, pressure gravitates — and negative pressure (tension) produces gravitational repulsion. A cosmological constant has maximally negative pressure (p = -ρc²), making it the most efficient driver of accelerating expansion. This is why the universe's expansion is accelerating despite the decelerating effect of matter."

- question: "Derive how the energy density of radiation scales with the scale factor a(t), starting from the continuity equation dρ/dt + 3(ȧ/a)(ρ + p/c²) = 0."
  type: short-answer
  answer: "For radiation, p = ρc²/3. Substituting into the continuity equation: dρ/dt + 3(ȧ/a)(ρ + ρ/3) = dρ/dt + 4(ȧ/a)ρ = 0. This gives dρ/ρ = -4 da/a, which integrates to ρ ∝ a⁻⁴. The a⁻³ factor comes from the dilution of photon number density as the volume expands, and the additional a⁻¹ factor comes from the cosmological redshift — each photon loses energy as its wavelength stretches with the expansion: E = hν ∝ a⁻¹. For comparison, matter (p = 0) gives ρ ∝ a⁻³ (volume dilution only), and a cosmological constant (p = -ρc²) gives ρ = const (energy density of vacuum does not dilute)."
  explanation: "The different scaling laws — ρ_matter ∝ a⁻³, ρ_radiation ∝ a⁻⁴, ρ_Λ = const — explain why the universe passes through radiation-dominated, matter-dominated, and dark-energy-dominated eras as it expands. Each era has a different expansion law a(t) determined by the Friedmann equations."
```

## Explainer

The Friedmann equations are what you get when you apply Einstein's field equations to a universe that is homogeneous (the same everywhere) and isotropic (the same in every direction). The cosmological principle — the assumption that we do not occupy a special place — motivated these symmetry assumptions, and observations of the cosmic microwave background confirm homogeneity and isotropy to better than one part in 10⁵ on large scales. The geometry of such a universe is described by the Robertson-Walker metric, and the Einstein equations reduce to two ordinary differential equations for the scale factor a(t), which measures how the "size" of the universe changes with time.

The first Friedmann equation, H² = (8πG/3)ρ - kc²/a² + Λ/3, is an energy-balance equation. The left side, H² = (ȧ/a)², is the square of the Hubble parameter — the expansion rate. The right side has three terms: the energy density ρ (which drives expansion), the spatial curvature k/a² (which can accelerate or decelerate depending on sign), and the cosmological constant Λ (which drives accelerated expansion). The critical density ρ_crit = 3H²/(8πG) is the density at which the universe is spatially flat (k = 0). The density parameter Ω = ρ/ρ_crit determines the spatial geometry: Ω = 1 means flat, Ω > 1 means positively curved (closed), Ω < 1 means negatively curved (open). Observations from the CMB, baryon acoustic oscillations, and supernovae consistently give Ω ≈ 1, indicating a nearly flat universe.

The second Friedmann equation (acceleration equation) ä/a = -(4πG/3)(ρ + 3p/c²) + Λ/3 determines whether the expansion is accelerating or decelerating. The crucial quantity is ρ + 3p/c²: if it is positive (as for ordinary matter and radiation), gravity decelerates the expansion (ä < 0). If negative (as for a cosmological constant, where p = -ρc² gives ρ + 3p/c² = -2ρ), the expansion accelerates (ä > 0). The 1998 discovery that the expansion is accelerating (Type Ia supernovae observations by the Supernova Cosmology Project and the High-z Supernova Search Team) implies that the dominant energy component of the universe today has negative pressure — dark energy, modeled most simply as a cosmological constant Λ.

The complete cosmological model requires an equation of state p = wρc² for each component. Matter has w = 0 (pressureless), radiation has w = 1/3, and a cosmological constant has w = -1. Each component's density scales differently with the scale factor: ρ_m ∝ a⁻³, ρ_r ∝ a⁻⁴, ρ_Λ = const. This means the universe's expansion history passes through distinct eras: radiation-dominated (early, a ∝ t^{1/2}), matter-dominated (intermediate, a ∝ t^{2/3}), and dark-energy-dominated (late, a ∝ exp(Ht)). The ΛCDM model — cold dark matter plus a cosmological constant — fits all current observations and describes a universe that is 13.8 billion years old, spatially flat, and composed of about 68% dark energy, 27% dark matter, and 5% ordinary (baryonic) matter.
