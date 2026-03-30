---
id: robertson-walker-metric
title: Robertson-Walker Metric
domain: physics
course: general-relativity
prerequisites:
- id: curved-spacetime-metric-tensor
  type: hard
- id: smooth-manifolds
  type: soft
tags:
- robertson-walker
- cosmological-metric
- homogeneity
- isotropy
- scale-factor
- comoving-coordinates
stage: expert
status: validated
---

# Robertson-Walker Metric

## Core Idea
The Robertson-Walker (RW) metric ds² = -c²dt² + a(t)²[dr²/(1-kr²) + r²dΩ²] is the most general metric for a spatially homogeneous and isotropic universe. The scale factor a(t) encodes the expansion history of the universe, and the curvature parameter k takes values +1 (closed, spherical spatial geometry), 0 (flat, Euclidean spatial geometry), or -1 (open, hyperbolic spatial geometry). The coordinates are comoving: galaxies at rest in the cosmic expansion have fixed spatial coordinates (r, θ, φ), and the physical distance between them grows as a(t) increases. Cosmic time t is the proper time of comoving observers. The RW metric is the geometric foundation of all standard cosmological models — the Friedmann equations, which govern the evolution of a(t), are derived by inserting this metric into the Einstein field equations.

## Questions

```yaml
- question: "In the Robertson-Walker metric, the spatial coordinates of galaxies participating in the Hubble flow remain constant as the universe expands. What changes to produce the observed recession of distant galaxies?"
  type: multiple-choice
  options:
    - "The galaxies accelerate through space away from us"
    - "The scale factor a(t) increases, stretching the metric distance between fixed comoving coordinates"
    - "The speed of light decreases over time, making distant objects appear to recede"
    - "The curvature parameter k changes with time"
  answer: 1
  explanation: "In comoving coordinates, galaxies at rest in the Hubble flow have fixed coordinate positions. The physical (proper) distance between two comoving galaxies is d(t) = a(t) × Δr, where Δr is the fixed coordinate separation. As a(t) increases, d(t) increases — galaxies recede from each other not because they move through space but because the space between them expands. This distinction is subtle but important: the expansion is a property of the metric (the geometry of space), not a motion of galaxies through a pre-existing space."

- question: "The curvature parameter k in the Robertson-Walker metric determines whether the spatial geometry of the universe is finite or infinite."
  type: true-false
  answer: false
  explanation: "The curvature parameter k determines the local geometry (spherical, flat, or hyperbolic), but not necessarily the global topology. A flat (k = 0) or hyperbolic (k = -1) universe could be infinite (the simplest topology) or finite with a non-trivial topology (e.g., a flat torus or a compact hyperbolic manifold). A positively curved (k = +1) universe is finite in volume in the standard topology (a 3-sphere). The Robertson-Walker metric constrains local geometry, not global topology."

- question: "Explain what cosmological redshift is in terms of the Robertson-Walker metric, and how it differs from Doppler redshift."
  type: short-answer
  answer: "In the RW metric, a photon emitted at time t_e with wavelength λ_e is observed at time t_o with wavelength λ_o = λ_e × a(t_o)/a(t_e). The redshift z = (λ_o - λ_e)/λ_e = a(t_o)/a(t_e) - 1 arises because the photon's wavelength stretches with the expanding space — the metric scale factor a(t) increases during the photon's travel. This differs from a Doppler shift, which is caused by the relative motion of source and observer through space. Cosmological redshift is a property of the expanding metric, not of the relative velocity of galaxies. For small redshifts (z << 1), the two descriptions approximately coincide (v ≈ cz ≈ H₀d), but for large z they diverge — galaxies at z > 1.5 have recession velocities exceeding c, which is allowed because it is the metric expanding, not objects moving through space faster than light."
  explanation: "The distinction between cosmological redshift and Doppler shift is subtle and partly semantic. In GR, there is no unique way to define the 'velocity' of a distant galaxy; the redshift is the observable, and it directly measures the ratio of scale factors at emission and observation."

- question: "Derive the relationship between the Hubble parameter H(t) and the scale factor a(t)."
  type: short-answer
  answer: "The Hubble parameter is defined as H(t) = ȧ(t)/a(t), where ȧ = da/dt. For a nearby comoving galaxy at fixed coordinate distance Δr, the proper distance is d = a(t)Δr. The recession velocity is v = ḋ = ȧ(t)Δr = (ȧ/a)(aΔr) = H(t)d. This is Hubble's law: v = Hd. The present value H₀ ≈ 70 km/s/Mpc is the Hubble constant. Note that H(t) generally changes with time — it is not truly a 'constant' except at the present epoch. In a matter-dominated universe, H decreases; in a dark-energy-dominated universe, H approaches a constant asymptotically."
  explanation: "The Hubble parameter is the most directly measurable cosmological quantity. Its present value H₀, combined with the density parameters Ω_m, Ω_r, Ω_Λ, determines the entire expansion history a(t) through the Friedmann equations."
```

## Explainer

The cosmological principle — the assumption that the universe is homogeneous (the same at every point) and isotropic (the same in every direction) on large scales — constrains the spacetime geometry to a specific form. In 1935-1936, Robertson and Walker independently proved that the most general metric compatible with spatial homogeneity and isotropy is ds² = -c²dt² + a(t)²[dr²/(1-kr²) + r²(dθ² + sin²θ dφ²)], where a(t) is an arbitrary function of time (the scale factor) and k is a constant that can be normalized to +1, 0, or -1 (the curvature parameter). This result is purely geometric — it does not depend on the Einstein equations, only on the symmetry assumptions.

The coordinates have a direct physical interpretation. The time coordinate t is cosmic time — the proper time measured by clocks at rest in the cosmic expansion (comoving observers). The spatial coordinates (r, θ, φ) are comoving coordinates: a galaxy participating in the uniform Hubble expansion has fixed (r, θ, φ) for all time. The physical distance between two comoving galaxies separated by coordinate distance Δr is d(t) = a(t) × Δr, which changes with time as a(t) changes. The scale factor is conventionally normalized so that a(t₀) = 1 at the present time t₀. The redshift of a distant galaxy is directly related to the scale factor at the time of emission: 1 + z = a(t₀)/a(t_e) = 1/a(t_e).

The curvature parameter k determines the geometry of spatial slices (constant-t hypersurfaces). For k = +1, the spatial geometry is that of a 3-sphere — positively curved, finite in volume, with parallel lines eventually converging. For k = 0, space is flat Euclidean — the familiar geometry of everyday experience extended to cosmological scales. For k = -1, space is hyperbolic — negatively curved, with parallel lines diverging and the volume of a sphere growing faster than r³. Current observations constrain the universe to be very close to spatially flat: |Ω_k| = |k|/(aH)² < 0.002, consistent with k = 0. This near-flatness is one of the motivations for cosmic inflation, which dynamically drives the universe toward k = 0.

The Robertson-Walker metric is the input to the Einstein field equations. The matter content of the universe is modeled as a perfect fluid with energy density ρ(t) and pressure p(t) (both spatially uniform, by homogeneity). Inserting the RW metric and the perfect-fluid stress-energy tensor into the Einstein equations yields the Friedmann equations, which are ordinary differential equations for a(t). The metric itself does not determine the expansion history — that requires specifying the matter content (through the equation of state p = wρc²) and the cosmological constant Λ. But the RW metric provides the geometric framework within which all of homogeneous cosmology operates, from the Big Bang to the present accelerating expansion.
