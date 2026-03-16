---
id: radiative-forcing-greenhouse-gases
title: Radiative Forcing by Greenhouse Gases
domain: earth-and-space-sciences
course: climate-science
prerequisites:
- id: radiative-transfer-atmospheric
  type: hard
- id: greenhouse-effect
  type: hard
- id: radiative-forcing-definition
  type: hard
- id: ir-spectroscopy-basics
  type: soft
builds-toward:
- climate-sensitivity-radiative-feedbacks
- anthropogenic-climate-forcing
tags:
- radiative-forcing
- greenhouse-gases
- climate-change
- forcing-metrics
stage: advanced
status: draft
---

# Radiative Forcing by Greenhouse Gases

## Core Idea
Radiative forcing by greenhouse gases quantifies the change in net radiative flux at the tropopause due to concentration changes, typically expressed in W/m². CO₂ has a logarithmic forcing relationship with concentration, while forcing from other gases depends on their spectral overlap and atmospheric abundance. The combined forcing from all anthropogenic greenhouse gases exceeds 3 W/m² and is the primary driver of recent climate warming.

## Explainer

You already know that the greenhouse effect works because certain gases absorb and re-emit infrared radiation, trapping energy that would otherwise escape to space. Radiative forcing puts a precise number on that trapping. Specifically, **radiative forcing** measures the change in net energy flux at the tropopause — the boundary between the troposphere and stratosphere — when the concentration of a greenhouse gas changes, after the stratosphere has had time to adjust to the new conditions. The result is expressed in watts per square meter (W/m²), and a positive forcing means the Earth system is gaining energy, which drives warming.

The relationship between CO₂ concentration and its forcing is **logarithmic**, not linear. This means that doubling CO₂ from 280 to 560 ppm produces roughly the same forcing (~3.7 W/m²) as doubling it again from 560 to 1120 ppm. The physical reason traces back to your radiative transfer background: at current concentrations, the central absorption band of CO₂ near 15 μm is already nearly saturated — almost all radiation at those wavelengths is already absorbed. Additional CO₂ mainly broadens the wings of the absorption band, where absorption is weaker. Each successive increment of CO₂ captures a smaller additional slice of the infrared spectrum, producing diminishing returns in forcing per unit of added gas.

Other greenhouse gases do not share this logarithmic relationship because they are present at much lower concentrations and their absorption bands are far from saturated. Methane (CH₄), nitrous oxide (N₂O), and halocarbons absorb in **atmospheric windows** — spectral regions where the atmosphere is otherwise relatively transparent. This makes them disproportionately effective per molecule: one molecule of methane produces roughly 80 times the forcing of one molecule of CO₂ over a 20-year period. However, because CO₂ is so much more abundant and because human emissions of it are so large, CO₂ still dominates the total anthropogenic forcing budget.

A crucial complication is **spectral overlap**. If two gases absorb at the same wavelengths, adding more of one has less effect because the other is already capturing that radiation. The overlap between methane and nitrous oxide absorption bands, for example, means their combined forcing is less than the sum of their individual forcings calculated in isolation. Radiative transfer models handle this by computing absorption line-by-line across the full infrared spectrum, accounting for all gases simultaneously. The total anthropogenic greenhouse gas forcing now exceeds 3 W/m², equivalent to trapping roughly 1% more energy than the pre-industrial atmosphere. That seemingly small imbalance, sustained over decades, is sufficient to warm the planet by several degrees — the forcing-to-temperature translation is the subject of climate sensitivity, which this topic builds toward.
