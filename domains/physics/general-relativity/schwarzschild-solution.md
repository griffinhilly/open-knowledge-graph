---
id: schwarzschild-solution
title: The Schwarzschild Solution
domain: physics
course: general-relativity
prerequisites:
- id: einstein-field-equations
  type: hard
- id: geodesic-equation
  type: hard
tags:
- schwarzschild
- vacuum-solution
- spherical-symmetry
- static-spacetime
- birkhoff-theorem
stage: expert
status: validated
---

# The Schwarzschild Solution

## Core Idea
The Schwarzschild metric ds² = -(1 - 2GM/rc²)c²dt² + (1 - 2GM/rc²)⁻¹dr² + r²dΩ² is the unique spherically symmetric vacuum solution to Einstein's field equations (Birkhoff's theorem). It describes the spacetime geometry outside any non-rotating, uncharged, spherically symmetric mass M. The metric has a coordinate singularity at the Schwarzschild radius r_s = 2GM/c² (the event horizon for a black hole) and a true curvature singularity at r = 0. In the weak-field limit (r >> r_s), it reduces to Newtonian gravity, but near r_s it predicts qualitatively new phenomena: extreme gravitational time dilation, the bending of light, the precession of orbits, and the existence of event horizons. The Schwarzschild solution is the foundation for understanding black holes, gravitational redshift, and the classic tests of GR.

## Questions

```yaml
- question: "At the Schwarzschild radius r = 2GM/c², the metric component g_{rr} diverges. This means:"
  type: multiple-choice
  options:
    - "There is a physical singularity — spacetime curvature becomes infinite at this radius"
    - "The coordinate system breaks down, but spacetime geometry is perfectly regular — freely falling observers pass through without experiencing infinite tidal forces"
    - "The metric is undefined and must be replaced by a different theory of gravity"
    - "Time stops at this radius, so nothing can ever cross it"
  answer: 1
  explanation: "The divergence at r = 2GM/c² is a coordinate singularity, not a physical one. The curvature invariant R_{μνρσ}R^{μνρσ} is finite and well-behaved at r = r_s, confirming that spacetime is smooth there. Alternative coordinate systems (Eddington-Finkelstein, Kruskal-Szekeres) eliminate the singularity and show that freely falling observers cross the horizon in finite proper time. The apparent 'infinite time' in Schwarzschild coordinates is a coordinate artifact — it is the coordinate time t of a distant observer that diverges, not the proper time of the infalling observer."

- question: "Birkhoff's theorem states that the Schwarzschild solution is the only spherically symmetric vacuum solution, even if the source is not static (e.g., a radially pulsating star)."
  type: true-false
  answer: true
  explanation: "Birkhoff's theorem proves that any spherically symmetric vacuum solution must be static and equal to the Schwarzschild metric. This means the exterior spacetime of a radially pulsating or collapsing spherically symmetric star is still Schwarzschild — the time-dependent internal dynamics do not radiate gravitational waves (spherical symmetry forbids it) and do not affect the external geometry. This is the GR analog of Newton's shell theorem (a spherically symmetric mass distribution creates the same external field as a point mass at the center)."

- question: "Derive the Schwarzschild radius for a mass equal to that of the Sun (M_☉ ≈ 2 × 10³⁰ kg) and explain its physical significance."
  type: short-answer
  answer: "r_s = 2GM/c² = 2(6.67 × 10⁻¹¹)(2 × 10³⁰)/(3 × 10⁸)² ≈ 2.95 km. This is the radius to which the Sun would need to be compressed for its surface to coincide with the event horizon of a black hole. For a normal star like the Sun (radius ~700,000 km), r_s is deep inside the star where the vacuum Schwarzschild solution does not apply. The Schwarzschild radius sets the scale at which general relativistic effects become extreme: gravitational time dilation becomes infinite, escape velocity reaches c, and an event horizon forms."
  explanation: "The remarkable smallness of r_s compared to the Sun's actual radius illustrates why Newtonian gravity is an excellent approximation for most stellar physics. The ratio r_s/R_☉ ≈ 4 × 10⁻⁶ is the dimensionless measure of how relativistic the Sun's gravitational field is at its surface."

- question: "How does the Schwarzschild metric reduce to Newtonian gravity far from the central mass?"
  type: short-answer
  answer: "For r >> 2GM/c², the metric component g_{00} = -(1 - 2GM/rc²) ≈ -(1 + 2Φ/c²), where Φ = -GM/r is the Newtonian gravitational potential. The geodesic equation for a slowly moving particle (v << c) in this weak-field metric reduces to d²r/dt² ≈ -GM/r², which is Newton's inverse-square law. The spatial metric deviation from flatness is also small (g_{rr} ≈ 1 + 2GM/rc²), contributing only post-Newtonian corrections. Thus the Schwarzschild metric smoothly connects to Newtonian gravity in the weak-field limit, as required for any viable theory of gravity."
  explanation: "The weak-field expansion of the Schwarzschild metric is the starting point for computing post-Newtonian corrections: the perihelion precession of Mercury, gravitational time dilation, and the Shapiro time delay are all first-order corrections beyond the Newtonian limit."
```

## Explainer

Karl Schwarzschild found the first exact solution to Einstein's field equations in 1916, just weeks after Einstein published the final form of general relativity. The solution describes the spacetime outside a spherically symmetric, non-rotating mass — a star, a planet, or a black hole. In Schwarzschild coordinates (t, r, θ, φ), the line element is ds² = -(1 - r_s/r)c²dt² + (1 - r_s/r)⁻¹dr² + r²(dθ² + sin²θ dφ²), where r_s = 2GM/c² is the Schwarzschild radius. The angular part r²dΩ² is the metric of a standard 2-sphere, reflecting the assumed spherical symmetry. The two metric functions (1 - r_s/r) in g_{tt} and g_{rr} encode all the gravitational physics.

Birkhoff's theorem guarantees that this solution is unique: any spherically symmetric vacuum solution must be the Schwarzschild metric. This is a remarkably strong result. It means the exterior spacetime of a spherically symmetric star is Schwarzschild regardless of the star's internal dynamics — even during radial pulsation or spherically symmetric collapse. No gravitational radiation escapes, and distant observers see a static gravitational field. This is the general-relativistic generalization of Newton's shell theorem. For a non-black-hole object (r_s well inside the body), the Schwarzschild solution applies only to the vacuum exterior; the interior is described by a different solution matched at the surface.

Far from the mass (r >> r_s), the Schwarzschild metric approaches the flat Minkowski metric, with small corrections of order r_s/r. The leading correction in g_{00} is exactly 2Φ/c², where Φ = -GM/r is the Newtonian potential. This is the regime in which Newtonian gravity is an excellent approximation. The geodesic equation for slow-moving particles reproduces Newton's inverse-square law. The corrections to Newtonian gravity — perihelion precession, gravitational time dilation, light deflection — are of order r_s/r compared to the Newtonian terms, which for the Sun at the Earth's orbit is about 10⁻⁸. These effects are small but measurable, and their observation constitutes the classic tests of general relativity.

At r = r_s, the metric components have apparent singularities: g_{tt} → 0 and g_{rr} → ∞. For decades, this was confused with a physical singularity, but it is actually a failure of the coordinate system — like the coordinate singularity at the North Pole in latitude-longitude coordinates. The curvature invariant K = R_{μνρσ}R^{μνρσ} = 48G²M²/(c⁴r⁶) is finite and well-behaved at r = r_s. Coordinate systems that are regular at the horizon — Eddington-Finkelstein coordinates, Kruskal-Szekeres coordinates — show that spacetime is smooth there and that freely falling observers cross the horizon in finite proper time, experiencing finite (though potentially large) tidal forces. The true singularity is at r = 0, where K → ∞ and the curvature is genuinely infinite. The physics of this singularity and the event horizon at r = r_s are explored in the black hole topic.
