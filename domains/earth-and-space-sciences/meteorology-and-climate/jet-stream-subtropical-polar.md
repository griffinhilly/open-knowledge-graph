---
id: jet-stream-subtropical-polar
title: Subtropical and Polar Jet Streams
domain: earth-and-space-sciences
course: meteorology-and-climate
prerequisites:
- id: thermal-wind-shear-geostrophic
  type: hard
- id: planetary-wind-circulation-cells
  type: soft
builds-toward:
- atmospheric-waves-and-instability
- storm-track-dynamics-climate
tags:
- jet-stream
- wind-maximum
- subtropical
- polar
stage: formal-systems
status: validated
---

# Subtropical and Polar Jet Streams

## Core Idea
Jet streams are narrow bands of strong westerly winds (~100+ m/s) at upper levels, located where the thermal wind is strongest. The subtropical jet marks the poleward edge of the Hadley cell and subtropical anticyclones (~30° lat), while the polar jet forms at the baroclinic zone between mid and polar latitudes (~60° lat). Polar jet variability drives mid-latitude weather patterns and storm tracks.

## Questions

```yaml
- question: "The subtropical jet stream is strongest in winter and weakest in summer. What is the best explanation for this seasonal variation?"
  type: multiple-choice
  options:
    - "Jet streams only form during winter because the atmosphere is colder overall"
    - "The equator-to-pole temperature gradient steepens in winter, increasing thermal wind shear and concentrating the jet"
    - "Winter storms generate stronger surface winds that merge to form the upper-level jet"
    - "The Hadley cell expands in summer, pushing the jet to higher latitudes where it weakens and disperses"
  answer: 1
  explanation: "Jet streams are driven by the thermal wind mechanism: horizontal temperature gradients cause vertical wind shear, and concentrated shear produces a jet maximum. In winter, the poles cool dramatically while the tropics remain relatively warm, steepening the equator-to-pole temperature gradient. The stronger gradient drives stronger thermal wind shear and produces a more intense, narrower jet. In summer, polar temperatures moderate and the gradient weakens, resulting in a weaker, more diffuse jet. The seasonal cycle in jet strength traces directly to the thermal wind relationship."

- question: "The polar jet stream becomes highly meridional — making large northward ridges and southward troughs — over a continental region. What weather pattern is most likely to result?"
  type: multiple-choice
  options:
    - "Rapid succession of different weather systems, as storms move quickly across the region under the fast-moving jet"
    - "Persistent weather patterns lasting weeks, such as prolonged heat waves, cold outbreaks, or drought"
    - "No significant surface weather impact, because the jet stream only affects aviation, not surface conditions"
    - "Increased precipitation everywhere, since meridional flow always draws moisture from the tropics"
  answer: 1
  explanation: "A zonal (west-to-east) polar jet steers weather systems briskly — no single pattern dominates for long. A highly meridional jet meanders in large Rossby waves that move slowly or become stationary (blocking). When a ridge of high pressure parks over a region, it can produce weeks of warm, dry conditions (heat waves, drought). An adjacent trough delivers persistent cold and precipitation. This blocking pattern is associated with some of the most extreme weather events on record — the 2003 European heat wave and 2010 Russian heat wave both involved blocking ridges maintained by a meridional polar jet."

- question: "The polar jet stream is considerably more variable in position and strength than the subtropical jet stream."
  type: true-false
  answer: true
  explanation: "True. The subtropical jet forms at the poleward edge of the Hadley cell, which is a thermally direct, persistent circulation driven by equatorial heating. The Hadley cell's position and strength change relatively little day-to-day, keeping the subtropical jet relatively steady near 30° latitude. The polar jet forms along the baroclinic zone between polar and midlatitude air masses, which is inherently unstable to growing Rossby waves and extratropical cyclones. The polar front shifts with individual weather systems, making the polar jet highly variable in location and intensity on daily to weekly timescales."

- question: "Jet streams are easterly winds — they blow from east to west at upper levels of the atmosphere."
  type: true-false
  answer: false
  explanation: "False. Jet streams are strongly *westerly* winds — they blow from west to east. This is a common geographic misconception. In the midlatitudes, the combination of Earth's rotation (Coriolis force) and the equator-to-pole temperature gradient drives upper-level winds from west to east. Easterly winds (blowing from east to west) are found in the tropics (trade winds near the surface) and at the poles, but midlatitude jet streams are definitively westerly. This is why transatlantic flights from North America to Europe are significantly faster than the return trip."

- question: "Explain why the polar jet stream meanders in large Rossby waves rather than flowing in a smooth, uniform band around the globe."
  type: short-answer
  answer: "The polar jet is baroclinically unstable — small perturbations grow rather than decay. Rossby waves arise from conservation of potential vorticity on a rotating sphere: when air parcels are displaced meridionally, the latitude-dependent Coriolis parameter (β-effect) provides a restoring force that generates planetary-scale wave oscillations. These waves are also excited by orographic forcing (the Rocky Mountains and Himalayas deflect the flow) and by land-ocean heating contrasts. The jet responds to these perturbations by developing a quasi-stationary wavy structure of ridges and troughs superimposed on the mean westerly flow."
  explanation: "Rossby waves are the fundamental large-scale wave mode of rotating atmospheres and oceans. They propagate because conservation of potential vorticity (the sum of planetary and relative vorticity divided by layer thickness) requires air displaced poleward to develop anticyclonic relative vorticity (ridges) and air displaced equatorward to develop cyclonic vorticity (troughs). The amplitude and phase speed of these waves determine midlatitude weather patterns: low-amplitude, fast-moving waves produce active, changeable weather; high-amplitude, stationary (blocking) waves produce extreme persistent conditions."
```

## Explainer

From the thermal wind relationship, you know that when a horizontal temperature gradient exists in the atmosphere, the geostrophic wind must change with height — the wind shear is proportional to the temperature contrast. From planetary circulation cells, you know that Earth's atmosphere organizes into distinct latitudinal bands: the Hadley cell in the tropics, the Ferrel cell in the midlatitudes, and the Polar cell at high latitudes. **Jet streams** are the dramatic consequence of combining these two ideas — they form where the strongest temperature gradients meet the deepest atmosphere, concentrating kinetic energy into remarkably narrow ribbons of fast-moving air.

The **subtropical jet stream** sits near 30° latitude at roughly 10–12 km altitude, right at the poleward boundary of the Hadley cell. Here, air that rose at the equator and flowed poleward in the upper troposphere has been steadily deflected eastward by the Coriolis force. By the time it reaches the subtropics, it has accumulated so much eastward momentum that it forms a concentrated wind maximum — often reaching 50–70 m/s. The subtropical jet is relatively steady in position and strength because the Hadley cell itself is thermally direct and persistent. It is strongest in winter, when the equator-to-pole temperature gradient steepens.

The **polar jet stream** forms near 50–60° latitude where cold polar air masses collide with warmer midlatitude air — the **polar front**. This is where the temperature gradient is sharpest in the lower and middle troposphere, and the thermal wind equation dictates that the strongest wind shear and therefore the strongest upper-level winds will concentrate here. Unlike the relatively stable subtropical jet, the polar jet is wild and variable. It meanders in great sinuous waves called **Rossby waves**, dipping south to bring Arctic air into temperate regions (troughs) and bulging north to carry warm air poleward (ridges). These undulations are the steering mechanism for midlatitude weather — extratropical cyclones form and travel along the jet, and the position of the jet determines whether a given region experiences warmth or cold, drought or rain.

The polar jet's behavior has enormous practical consequences. When the jet is strong and relatively zonal (flowing mostly west to east), weather systems move briskly across the midlatitudes, and no single pattern persists for long. When the jet weakens and becomes highly meridional (large north-south undulations), weather patterns stall — a blocking ridge can park over a region for weeks, producing heat waves and drought, while an adjacent deep trough delivers persistent cold and flooding. The jet stream's position also matters for aviation: flying with a strong jet stream tail wind can cut hours off a transatlantic flight, while flying against it extends travel time significantly. Understanding where the jets are and how they are behaving is the starting point for nearly all midlatitude weather forecasting.
