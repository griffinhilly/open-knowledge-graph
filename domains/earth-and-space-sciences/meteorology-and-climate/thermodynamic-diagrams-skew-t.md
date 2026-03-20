---
id: thermodynamic-diagrams-skew-t
title: Thermodynamic Diagrams and Skew-T Analysis
domain: earth-and-space-sciences
course: meteorology-and-climate
prerequisites:
- id: potential-temperature-and-dry-thermodynamics
  type: hard
- id: equivalent-potential-temperature-conserved
  type: hard
builds-toward:
- cape-convective-available-potential
- weather-map-analysis
tags:
- diagnosis
- soundings
- visualization
stage: advanced
status: draft
---

# Thermodynamic Diagrams and Skew-T Analysis

## Core Idea
Skew-T log-P diagrams display atmospheric soundings with temperature on the skewed x-axis and pressure on the logarithmic y-axis. This coordinate system allows adiabatic and saturated adiabatic processes to be plotted as approximately straight lines, enabling quick visual assessment of stability, cloud base height, CAPE, and wind shear. They are fundamental tools for weather analysis and forecasting.

## How It's Best Learned
Construct a Skew-T from a radiosonde observation; identify stable and unstable layers; calculate CAPE, CIN, LCL, and EL; compare soundings from different environments.

## Common Misconceptions
- Confusing the dry adiabat with environmental lapse rate (environmental lapse rate is data from observations; adiabats are reference lines).
- Thinking clouds always form where environmental lapse rate intersects the lifting curve (requires both saturation and lifting).

## Explainer

From your study of potential temperature and equivalent potential temperature, you know that these conserved quantities let you track air parcel properties as the parcel moves through the atmosphere. The **Skew-T log-P diagram** is the tool that makes these abstract thermodynamic concepts visually operational. It takes a vertical profile of temperature and dew point measured by a weather balloon (a **sounding**) and plots it on a specially designed coordinate system where the powerful relationships between temperature, moisture, pressure, and stability can be read at a glance.

The diagram's axes are chosen for physical reasons. Pressure is plotted on the y-axis using a logarithmic scale, which means equal vertical distances correspond to roughly equal altitude intervals (because pressure decreases approximately exponentially with height). Temperature is plotted on the x-axis but tilted 45° to the right — this is the "skew" in Skew-T. The skewing is not cosmetic; it separates the temperature and dry adiabat lines so they intersect at large angles, making it far easier to distinguish between the environmental temperature profile and the paths that lifted parcels follow. On an unskewed diagram, these lines would run nearly parallel and differences would be hard to see.

Five families of reference lines are printed on every Skew-T diagram: **isotherms** (skewed vertical lines of constant temperature), **isobars** (horizontal lines of constant pressure), **dry adiabats** (curved lines showing how an unsaturated parcel's temperature changes as it rises), **saturated adiabats** (steeper curved lines showing the slower cooling rate of a saturated parcel releasing latent heat), and **mixing ratio lines** (showing how much water vapor the air can hold at each pressure and temperature). To analyze a sounding, you plot the observed temperature and dew point profiles, then trace a surface parcel upward: follow the dry adiabat from the surface temperature until it intersects the mixing ratio line drawn from the surface dew point. This intersection is the **Lifting Condensation Level (LCL)** — the altitude where the parcel reaches saturation and clouds begin to form.

Above the LCL, the parcel follows the saturated adiabat. If the saturated adiabat carries the parcel to temperatures warmer than the observed environmental temperature, the parcel is buoyant and rises freely — the atmosphere is unstable. The area on the diagram between the parcel's path and the environmental temperature, where the parcel is warmer, represents **Convective Available Potential Energy (CAPE)** — essentially the fuel available for thunderstorm development. The area where the parcel is cooler than the environment represents **Convective Inhibition (CIN)** — the energy barrier that must be overcome before free convection begins. A sounding with large CAPE but modest CIN is the classic setup for explosive afternoon thunderstorms: the atmosphere is loaded with potential energy but capped by a stable layer that, once broken by surface heating or a frontal trigger, unleashes violent updrafts. Learning to read these features on a Skew-T diagram is the single most important diagnostic skill in convective forecasting.
