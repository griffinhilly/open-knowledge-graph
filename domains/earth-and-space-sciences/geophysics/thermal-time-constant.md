---
id: thermal-time-constant
title: Thermal Time Constants and Lithospheric Cooling
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: crustal-age-and-cooling-curves
  type: hard
tags:
- geothermics
- thermal-modeling
- cooling-time
stage: expert
status: draft
---

# Thermal Time Constants and Lithospheric Cooling

## Core Idea
The thermal time constant τ = d²/κ (where d is thickness and κ is thermal diffusivity ~10⁻⁶ m²/s) describes how quickly thermal perturbations diffuse through rock. Lithospheric cooling occurs over tens to hundreds of millions of years. Understanding thermal timescales is essential for interpreting geothermal data, predicting basin subsidence, and linking geophysical observations to geological processes.

## Questions

```yaml
- question: "Oceanic lithosphere is ~100 km thick with κ ≈ 10⁻⁶ m²/s, giving a thermal time constant of roughly 100 million years. If the lithosphere were only 50 km thick, what would the thermal time constant be?"
  type: multiple-choice
  options:
    - "~50 million years — halving the thickness halves the time constant"
    - "~25 million years — the time constant scales with the square of thickness, so halving d reduces τ by a factor of four"
    - "~100 million years — thermal diffusivity, not thickness, controls the cooling rate"
    - "~200 million years — thinner lithosphere retains heat longer because there is less surface area to radiate"
  answer: 1
  explanation: "τ = d²/κ — the time constant scales with the *square* of thickness. Halving d reduces d² by a factor of 4. The most tempting wrong answer (option A) assumes a linear relationship, which would be true if heat simply 'flowed through' the slab at a constant velocity. But diffusion slows as it progresses: the thermal front penetrates a distance proportional to √(κt), so the time to diffuse through a given thickness d is proportional to d²/κ. This quadratic dependence is the key conceptual insight."

- question: "Why does heat flow at the ocean surface decrease as 1/√(age) rather than decreasing linearly as the plate cools?"
  type: multiple-choice
  options:
    - "Volcanic activity at the ridge decreases exponentially as the plate moves away"
    - "The thermal boundary layer thickens as √(κt), deepening the hot interior; as the temperature gradient at the surface decreases proportionally, so does heat flow"
    - "Older oceanic crust develops higher thermal conductivity through metamorphism, letting heat escape more efficiently"
    - "The mantle beneath older plates cools faster because it is further from the ridge heat source"
  answer: 1
  explanation: "Heat flow at the surface is proportional to the temperature gradient there (Fourier's law: q = −k dT/dz). As the oceanic plate ages, the cooled thermal boundary layer grows as √(κt) — the hot mantle is progressively deeper below the surface. The shallower temperature gradient means less heat is conducted to the surface per unit time. Since boundary layer depth ∝ √t, the surface gradient ∝ 1/√t, and heat flow follows the same relationship. This is a direct consequence of the diffusion equation, not a material property of the crust."

- question: "The thermal time constant of a rock layer depends linearly on its thickness — doubling the thickness doubles the time required for a thermal perturbation to diffuse through it."
  type: true-false
  answer: false
  explanation: "The thermal time constant is τ = d²/κ — it scales with the *square* of thickness. Doubling the thickness quadruples the time constant, not doubles it. This counterintuitive result follows from the diffusion equation: the distance a thermal front penetrates grows as √(κt), so the time to reach depth d is t = d²/κ. Diffusion slows as it progresses — it cannot be described by a constant propagation velocity, which would give linear scaling. The quadratic dependence is why a 10,000× increase in linear scale produces a 10⁸× increase in thermal equilibration time."

- question: "The enormous difference in cooling timescale between a 5-meter lava flow (days) and 100-km-thick lithosphere (100 Myr) is primarily due to differences in the thermal diffusivity of different rock types."
  type: true-false
  answer: false
  explanation: "Rocks of similar composition have similar thermal diffusivity — κ ≈ 10⁻⁶ m²/s is a reasonable value for most crustal rocks. The extraordinary difference in cooling timescale is almost entirely due to the difference in thickness. The 100 km lithosphere is 2 × 10⁷× thicker than a 5-meter flow, and because τ = d²/κ, this translates to a time constant roughly (2 × 10⁷)² = 4 × 10¹⁴ times longer. Physical scale — not material properties — is the dominant control on geological thermal timescales. This is what makes τ = d²/κ such a powerful conceptual tool."

- question: "Explain why continental collision zones remain thermally elevated and produce metamorphism and granitic melts for tens of millions of years after active shortening has ceased."
  type: short-answer
  answer: "Continental collision thickens the crust from ~35 km to ~65–70 km by stacking one crustal slab onto another. Because τ = d²/κ, doubling the thickness quadruples the thermal time constant — the thickened crust requires roughly 100–160 million years to reach a new thermal equilibrium, far longer than the shortening event itself. When shortening stops, the deep crust contains material that was rapidly buried to depths where ambient temperatures are hundreds of degrees higher than before collision. This hot, deeply buried rock takes a geological epoch to cool, and during that time elevated temperatures drive prograde metamorphism and can cause crustal melting, generating granitic magmas that intrude upward. The thermal time constant explains why the thermal and magmatic consequences of a collision outlast the collision itself by tens to hundreds of millions of years."
  explanation: "The same logic applies in sedimentary basins: source rocks for petroleum must spend sufficient time in the 'oil window' (~60–120°C). The thermal time constant of the basin determines whether burial history has been long enough for organic matter to mature. The τ = d²/κ formula connects the timescale of heat diffusion to the thickness of the system, providing a simple order-of-magnitude test for whether thermal equilibration has had time to occur in any geological setting."
```

## Explainer

From crustal age and cooling curves, you know that oceanic lithosphere cools and subsides predictably as it moves away from mid-ocean ridges, and that heat flow decreases with the square root of age. The thermal time constant provides the physical framework for understanding *why* these cooling processes operate on the timescales they do — and it comes down to a single, powerful relationship between length scale and diffusion time.

The formula **τ = d²/κ** says that the time required for a thermal disturbance to diffuse through a layer of thickness d is proportional to the *square* of that thickness. The thermal diffusivity κ (about 10⁻⁶ m²/s for most rocks, or roughly 32 m²/yr) describes how efficiently a material conducts heat relative to its ability to store it. The quadratic dependence on d is the critical insight: doubling the thickness quadruples the equilibration time. A 1-meter-thick lava flow cools in about a day. A 1 km slab of rock takes roughly 30,000 years. The 100 km-thick oceanic lithosphere has a thermal time constant on the order of 100 million years — which is why plate-scale thermal processes unfold over geological time.

This scaling relationship explains many first-order observations in geophysics. The **half-space cooling model** for oceanic lithosphere assumes that newly formed lithosphere at a ridge starts hot and cools by conduction from the surface. The thermal boundary layer (the depth to which cooling has penetrated) grows as √(κt), so the lithosphere thickens proportionally to the square root of its age. This is why ocean depth increases as √(age) — the plate gets denser as it cools, and it subsides isostatically. Heat flow decreases as 1/√(age) for the same reason: as the thermal boundary layer thickens, the temperature gradient at the surface decreases. The model works remarkably well for lithosphere younger than about 80 million years.

The thermal time constant also governs how geological processes interact across scales. A volcanic intrusion (a dike or sill) a few meters thick heats its surrounding rock for days to weeks — fast enough to be irrelevant to regional tectonics but critical for contact metamorphism. A sedimentary basin that subsides and fills over tens of millions of years cools slowly enough that its thermal history controls petroleum maturation — source rocks must spend sufficient time in the "oil window" temperature range. Continental collision zones, where crust is thickened to 60–70 km, require over 100 million years to reach a new thermal equilibrium, which is why elevated heat flow and metamorphism persist long after active shortening ceases. In each case, the thermal time constant tells you whether a given thermal perturbation has had time to equilibrate, is still evolving, or has barely begun — connecting the timescale of geological processes to the physics of heat diffusion.
