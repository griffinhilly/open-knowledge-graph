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
stage: advanced
status: draft
---

# Thermal Time Constants and Lithospheric Cooling

## Core Idea
The thermal time constant τ = d²/κ (where d is thickness and κ is thermal diffusivity ~10⁻⁶ m²/s) describes how quickly thermal perturbations diffuse through rock. Lithospheric cooling occurs over tens to hundreds of millions of years. Understanding thermal timescales is essential for interpreting geothermal data, predicting basin subsidence, and linking geophysical observations to geological processes.

## Explainer

From crustal age and cooling curves, you know that oceanic lithosphere cools and subsides predictably as it moves away from mid-ocean ridges, and that heat flow decreases with the square root of age. The thermal time constant provides the physical framework for understanding *why* these cooling processes operate on the timescales they do — and it comes down to a single, powerful relationship between length scale and diffusion time.

The formula **τ = d²/κ** says that the time required for a thermal disturbance to diffuse through a layer of thickness d is proportional to the *square* of that thickness. The thermal diffusivity κ (about 10⁻⁶ m²/s for most rocks, or roughly 32 m²/yr) describes how efficiently a material conducts heat relative to its ability to store it. The quadratic dependence on d is the critical insight: doubling the thickness quadruples the equilibration time. A 1-meter-thick lava flow cools in about a day. A 1 km slab of rock takes roughly 30,000 years. The 100 km-thick oceanic lithosphere has a thermal time constant on the order of 100 million years — which is why plate-scale thermal processes unfold over geological time.

This scaling relationship explains many first-order observations in geophysics. The **half-space cooling model** for oceanic lithosphere assumes that newly formed lithosphere at a ridge starts hot and cools by conduction from the surface. The thermal boundary layer (the depth to which cooling has penetrated) grows as √(κt), so the lithosphere thickens proportionally to the square root of its age. This is why ocean depth increases as √(age) — the plate gets denser as it cools, and it subsides isostatically. Heat flow decreases as 1/√(age) for the same reason: as the thermal boundary layer thickens, the temperature gradient at the surface decreases. The model works remarkably well for lithosphere younger than about 80 million years.

The thermal time constant also governs how geological processes interact across scales. A volcanic intrusion (a dike or sill) a few meters thick heats its surrounding rock for days to weeks — fast enough to be irrelevant to regional tectonics but critical for contact metamorphism. A sedimentary basin that subsides and fills over tens of millions of years cools slowly enough that its thermal history controls petroleum maturation — source rocks must spend sufficient time in the "oil window" temperature range. Continental collision zones, where crust is thickened to 60–70 km, require over 100 million years to reach a new thermal equilibrium, which is why elevated heat flow and metamorphism persist long after active shortening ceases. In each case, the thermal time constant tells you whether a given thermal perturbation has had time to equilibrate, is still evolving, or has barely begun — connecting the timescale of geological processes to the physics of heat diffusion.
