---
id: applications-double-integrals
title: 'Applications of Double Integrals: Area, Volume, and Mass'
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: double-integrals-polar
  type: hard
builds-toward:
- triple-integrals
tags:
- applications
- area
- volume
- mass
stage: formal-systems
status: draft
---

# Applications of Double Integrals: Area, Volume, and Mass

## Core Idea
Double integrals compute area (∬_R 1 dA), volume under a surface (∬_R f dA for f ≥ 0), and mass of a lamina with density ρ (∬_R ρ(x,y) dA). These applications anchor multivariable integration to geometry and physics.

## Explainer

You can already set up and evaluate double integrals in Cartesian and polar coordinates, iterating as ∫∫ f(x,y) dy dx over appropriate limits. Now the question is: what does that number actually mean? The three core interpretations — area, volume, and mass — all follow from the same fundamental idea: a double integral sums infinitesimal contributions of the integrand f(x,y) over a region R.

**Area** is the simplest case. Set f(x,y) = 1 everywhere. Then ∬_R 1 dA adds up area elements dA over the region — the result is just the area of R. This seems almost too trivial, but it is useful: if the region R is described in polar coordinates or as the intersection of two complicated curves, computing ∬ 1 dA is often the cleanest way to find its area, especially if you already have the integration limits set up.

**Volume** extends the single-variable interpretation. In one dimension, ∫_a^b f(x) dx gives the area under the curve y = f(x). In two dimensions, ∬_R f(x,y) dA gives the volume under the surface z = f(x,y) and above the region R in the xy-plane (provided f ≥ 0). Each infinitesimal area element dA supports a thin column of height f(x,y), contributing f(x,y) dA to the total volume. Polar coordinates are particularly useful here when the region R is a disk or sector and the surface has rotational symmetry, such as z = √(1 − x² − y²) over the unit disk.

**Mass** of a **lamina** (a thin flat plate) applies when the plate has variable density ρ(x,y). If the plate occupies region R and has mass per unit area ρ(x,y), then the total mass is ∬_R ρ(x,y) dA. Each infinitesimal patch of area dA contributes mass ρ(x,y) dA. This is directly analogous to single-variable mass: ∫ρ(x) dx for a rod with density ρ(x). Uniform density ρ = constant gives mass = ρ · Area(R), which checks out. The same framework extends to **moments** (∬ x ρ dA and ∬ y ρ dA) for locating the center of mass, which connects to the triple integrals and moment-of-inertia calculations you will encounter next.
