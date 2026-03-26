---
id: applications-double-integrals
title: 'Applications of Double Integrals: Area, Volume, and Mass'
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: double-integrals-polar
  type: hard
- id: area-volume-integrals
  type: soft
builds-toward:
- triple-integrals
tags:
- applications
- area
- volume
- mass
stage: formal-systems
status: validated
---
# Applications of Double Integrals: Area, Volume, and Mass

## Core Idea
Double integrals compute area (∬_R 1 dA), volume under a surface (∬_R f dA for f ≥ 0), and mass of a lamina with density ρ (∬_R ρ(x,y) dA). These applications anchor multivariable integration to geometry and physics.

## Questions

```yaml
- question: "A thin plate (lamina) occupies the region R with area 6 m² and has uniform density ρ = 4 kg/m². What is its mass, and which double integral computes it?"
  type: multiple-choice
  options:
    - "Mass = 1.5 kg, computed by ∬_R (1/ρ) dA"
    - "Mass = 10 kg, computed by ∬_R (ρ + 1) dA"
    - "Mass = 24 kg, computed by ∬_R ρ dA = ρ · Area(R)"
    - "Mass = 6 kg, computed by ∬_R 1 dA regardless of density"
  answer: 2
  explanation: "Mass equals ∬_R ρ(x,y) dA. When density is uniform (constant ρ), the integral factors: ρ∬_R 1 dA = ρ · Area(R) = 4 · 6 = 24 kg. Each infinitesimal area element dA has mass ρ · dA, and summing over the plate gives total mass. Option D correctly notes that ∬_R 1 dA = Area(R) = 6, but ignores the density factor. The formula ∬_R ρ dA reduces to ρ · Area only for uniform density — for variable density you must integrate ρ(x,y) directly."

- question: "You want the volume under the paraboloid z = x² + y² above the unit disk R: x² + y² ≤ 1. Which setup is correct?"
  type: multiple-choice
  options:
    - "∬_R 1 dA — the unit disk has area π, giving volume π"
    - "∬_R (x² + y²) dA — integrate the surface height over the region"
    - "∫₀¹ ∫₀¹ (x² + y²) dy dx — integrate over the unit square"
    - "∫₀¹ (x² + y²)² dx — square the integrand to account for the 2D region"
  answer: 1
  explanation: "Volume under z = f(x,y) above region R is ∬_R f(x,y) dA, where each infinitesimal area element dA supports a column of height f(x,y). Here f = x² + y², so the setup is ∬_R (x² + y²) dA over the unit disk. Option A gives the area of R (= π), not the volume. Option C integrates over the wrong region (a square, not a disk). This integral is most naturally evaluated in polar coordinates: ∫₀²π ∫₀¹ r² · r dr dθ."

- question: "The integral ∬_R 1 dA generally equals 1, regardless of the shape or size of the region R."
  type: true-false
  answer: false
  explanation: "∬_R 1 dA gives the area of R. When f(x,y) = 1, each infinitesimal area element dA contributes exactly dA to the integral — summing these up gives the total area of the region. A unit square gives 1, a circle of radius 2 gives 4π, and so on. The result is 1 only if R happens to have area 1."

- question: "For a non-uniform lamina with density ρ(x,y), the formula ∬_R ρ(x,y) dA reduces to ρ · Area(R) only when the density is constant."
  type: true-false
  answer: true
  explanation: "When ρ is constant, it factors out of the integral: ∬_R ρ dA = ρ ∬_R 1 dA = ρ · Area(R). When ρ varies with position, different patches of the lamina contribute different amounts of mass per unit area, and you must integrate ρ(x,y) weighted by dA across the whole region. The constant-density formula is a special case, not the general rule."

- question: "Explain why the formulas for volume under a surface and mass of a lamina have identical mathematical structure, even though they describe physically different quantities."
  type: short-answer
  answer: "Both are double integrals of the form ∬_R f(x,y) dA. In both cases, the integrand assigns a 'weight' to each infinitesimal area element dA: for volume, f(x,y) is the height of the surface above that patch, so f·dA is the volume of a thin column; for mass, ρ(x,y) is the mass per unit area at that patch, so ρ·dA is the mass of a tiny piece of the lamina. In both cases the double integral sums infinitely many infinitesimal contributions over the region. The physics differs (geometry vs. mass), but the mathematical operation — integrating a function over a 2D region — is identical."
  explanation: "This structural unity is the payoff of the integral interpretation: once you understand that ∬ f dA sums f-weighted area contributions, you can apply it to any quantity expressible as a density — mass density, probability density, charge density, and more. The application changes; the setup procedure does not."
```

## Explainer

You can already set up and evaluate double integrals in Cartesian and polar coordinates, iterating as ∫∫ f(x,y) dy dx over appropriate limits. Now the question is: what does that number actually mean? The three core interpretations — area, volume, and mass — all follow from the same fundamental idea: a double integral sums infinitesimal contributions of the integrand f(x,y) over a region R.

**Area** is the simplest case. Set f(x,y) = 1 everywhere. Then ∬_R 1 dA adds up area elements dA over the region — the result is just the area of R. This seems almost too trivial, but it is useful: if the region R is described in polar coordinates or as the intersection of two complicated curves, computing ∬ 1 dA is often the cleanest way to find its area, especially if you already have the integration limits set up.

**Volume** extends the single-variable interpretation. In one dimension, ∫_a^b f(x) dx gives the area under the curve y = f(x). In two dimensions, ∬_R f(x,y) dA gives the volume under the surface z = f(x,y) and above the region R in the xy-plane (provided f ≥ 0). Each infinitesimal area element dA supports a thin column of height f(x,y), contributing f(x,y) dA to the total volume. Polar coordinates are particularly useful here when the region R is a disk or sector and the surface has rotational symmetry, such as z = √(1 − x² − y²) over the unit disk.

**Mass** of a **lamina** (a thin flat plate) applies when the plate has variable density ρ(x,y). If the plate occupies region R and has mass per unit area ρ(x,y), then the total mass is ∬_R ρ(x,y) dA. Each infinitesimal patch of area dA contributes mass ρ(x,y) dA. This is directly analogous to single-variable mass: ∫ρ(x) dx for a rod with density ρ(x). Uniform density ρ = constant gives mass = ρ · Area(R), which checks out. The same framework extends to **moments** (∬ x ρ dA and ∬ y ρ dA) for locating the center of mass, which connects to the triple integrals and moment-of-inertia calculations you will encounter next.
