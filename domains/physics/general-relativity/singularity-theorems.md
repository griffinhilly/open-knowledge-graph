---
id: singularity-theorems
title: Singularity Theorems
domain: physics
course: general-relativity
prerequisites:
- id: einstein-field-equations
  type: hard
- id: geodesic-equation
  type: hard
- id: penrose-diagrams
  type: soft
tags:
- singularity
- penrose-theorem
- hawking-theorem
- trapped-surface
- geodesic-incompleteness
stage: expert
status: validated
---

# Singularity Theorems

## Core Idea
The Penrose (1965) and Hawking-Penrose (1970) singularity theorems prove that singularities — defined as geodesic incompleteness (the existence of geodesics that cannot be extended to arbitrary parameter values) — are generic features of general relativity under physically reasonable conditions, not artifacts of special symmetry. Penrose's theorem requires: (1) the existence of a trapped surface (a closed surface from which all outgoing light rays converge), (2) a reasonable energy condition (null energy condition: T_μν k^μ k^ν ≥ 0 for all null vectors k^μ), and (3) global hyperbolicity. Under these conditions, at least one geodesic must be incomplete — a singularity exists. Hawking extended this to cosmological singularities, proving that an expanding universe satisfying the strong energy condition must have begun from a singularity (the Big Bang). These theorems do not describe the nature of the singularity — they only prove its existence.

## Questions

```yaml
- question: "The singularity theorems prove that spacetime curvature becomes infinite at singularities."
  type: true-false
  answer: false
  explanation: "The singularity theorems prove geodesic incompleteness — the existence of geodesics (worldlines of freely falling particles or light rays) that terminate after a finite affine parameter. They do not prove that curvature diverges, that matter density becomes infinite, or any specific physical behavior at the singularity. In practice, known singular solutions (Schwarzschild, Kerr) do have divergent curvature, but the theorems are more general and more modest: they prove something goes wrong (geodesics end) without specifying exactly what."

- question: "What is a trapped surface, and why is its existence the key condition in Penrose's singularity theorem?"
  type: multiple-choice
  options:
    - "A surface where the gravitational potential exceeds c², trapping all matter"
    - "A closed 2-surface where both the ingoing and outgoing families of null geodesics orthogonal to the surface have negative expansion — all light rays converge regardless of direction"
    - "The event horizon of a black hole"
    - "A surface where the metric signature changes from Lorentzian to Euclidean"
  answer: 1
  explanation: "A trapped surface is a closed spacelike 2-surface where the expansion of both families of orthogonal null geodesics is negative — light emitted from the surface converges in both the inward and outward directions. In flat spacetime, outgoing light from a sphere always diverges; a trapped surface means gravity is so strong that even outgoing light is being focused inward. Penrose showed that the existence of such a surface, combined with an energy condition, implies that geodesics must terminate — a singularity is inevitable. A trapped surface is a more general concept than an event horizon: you can determine locally whether a surface is trapped, while an event horizon is a global property."

- question: "Explain why the singularity theorems imply that general relativity predicts its own breakdown."
  type: short-answer
  answer: "The singularity theorems prove that under generic, physically reasonable conditions, spacetime contains incomplete geodesics — worldlines of particles or light that simply end after finite proper time or affine parameter. This means the theory cannot predict what happens beyond the singularity: the initial-value problem breaks down and determinism fails. Since general relativity is a classical theory and singularities are points where quantities like curvature likely diverge, the theorems strongly suggest that GR is incomplete as a theory of gravity at extreme scales. A quantum theory of gravity is expected to resolve singularities by modifying physics at the Planck scale (l_P ~ 10⁻³⁵ m), just as quantum mechanics resolved the classical singularity of the Coulomb potential."
  explanation: "The singularity theorems were revolutionary because they showed that singularities are not artifacts of idealized solutions (perfect spherical symmetry, etc.) but unavoidable features of the theory. This transformed the search for a quantum theory of gravity from a theoretical nicety into a physical necessity."

- question: "Hawking's cosmological singularity theorem shows that an expanding universe satisfying the strong energy condition must have a past singularity (Big Bang). What assumption does the strong energy condition make, and what type of matter violates it?"
  type: short-answer
  answer: "The strong energy condition requires (T_μν - (1/2)g_μν T)u^μ u^ν ≥ 0 for all timelike vectors u^μ, which for a perfect fluid reduces to ρ + 3p/c² ≥ 0. This is satisfied by ordinary matter and radiation but is violated by a cosmological constant or dark energy with p < -ρc²/3. The accelerating expansion of the universe (discovered in 1998) is driven by dark energy that violates the strong energy condition, which means the Hawking singularity theorem does not straightforwardly apply to our actual universe. However, the Big Bang singularity is still expected on other grounds (the initial singularity can be established under weaker conditions in inflationary models)."
  explanation: "The energy conditions are the physical inputs to the singularity theorems, and their validity is an empirical question. The strong energy condition is violated by inflation and dark energy, the null energy condition is violated by quantum effects (Casimir energy, Hawking radiation). Understanding which energy conditions hold in quantum gravity is crucial for resolving the singularity question."
```

## Explainer

Before the singularity theorems, the singularity in the Schwarzschild and Friedmann solutions was widely regarded as an artifact of their perfect symmetry. Perhaps a slightly asymmetric collapse would produce a "bounce" rather than a singularity, and perhaps the Big Bang singularity would be avoided in a slightly inhomogeneous universe. The Penrose singularity theorem of 1965 demolished this hope. Using global geometric methods rather than explicit solutions, Penrose proved that once a trapped surface forms — a surface from which even outgoing light converges — a singularity is inevitable, regardless of any symmetry assumptions.

The key concept is geodesic incompleteness. A spacetime is called geodesically incomplete if there exists at least one geodesic (timelike or null) that cannot be extended to all values of its affine parameter. Physically, this means a freely falling particle or light ray reaches the "edge" of spacetime in finite proper time or affine parameter — its worldline simply ends. This is the mathematically precise definition of a singularity used in the theorems. The theorems do not say what happens at the singularity (infinite curvature, infinite density, etc.) — they only prove that geodesics terminate. In all known exact solutions, the termination is accompanied by divergent curvature, but this is not guaranteed in general.

Penrose's theorem requires three ingredients: (1) a trapped surface exists, (2) the null energy condition holds (T_μν k^μ k^ν ≥ 0 for all null vectors k — roughly, energy density is non-negative as seen by any light ray), and (3) the spacetime is globally hyperbolic (well-posed initial-value problem). The proof uses the Raychaudhuri equation, which governs the expansion of a congruence of geodesics: the energy condition ensures that the expansion of null geodesics from the trapped surface cannot stop decreasing, and the trapped-surface condition means the expansion starts negative. The geodesics must therefore reach zero expansion (a caustic or focal point) in finite affine parameter, and global hyperbolicity prevents them from simply exiting the spacetime. The conclusion: at least one geodesic is incomplete.

Hawking adapted Penrose's methods to cosmology. His theorem (and the later Hawking-Penrose theorem of 1970) proved that an expanding universe satisfying the strong energy condition — (ρ + 3p/c²) ≥ 0 for a perfect fluid — must have a past singularity: the Big Bang. The expanding universe plays the role of the trapped surface (run time backward and the expansion becomes convergence). The discovery of accelerating cosmic expansion (1998) means the strong energy condition is violated by dark energy, which technically invalidates the theorem's applicability to the far future. However, the past singularity (Big Bang) remains robust under weaker conditions. The profound lesson of the singularity theorems is that general relativity, under generic conditions, predicts its own breakdown — signaling the need for a quantum theory of gravity to describe the physics of extreme curvature. Penrose received the 2020 Nobel Prize in Physics for this work.
