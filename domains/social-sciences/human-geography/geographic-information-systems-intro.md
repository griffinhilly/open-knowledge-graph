---
id: geographic-information-systems-intro
title: Geographic Information Systems and Spatial Analysis
domain: social-sciences
course: human-geography
prerequisites:
- id: human-geography-overview
  type: soft
- id: place-and-space-concepts
  type: soft
- id: scale-drawings-and-maps
  type: soft
- id: coordinate-plane-intro
  type: soft
- id: ratios
  type: soft
- id: 3d-coordinate-systems
  type: hard
- id: matrix-operations
  type: soft
- id: coordinate-geometry-proofs
  type: soft
builds-toward:
- population-distribution-density
- spatial-interaction-theory
tags:
- GIS
- spatial data
- cartography
- remote sensing
- map projections
- choropleth
- spatial analysis
stage: formal-systems
status: validated
---

# Geographic Information Systems and Spatial Analysis

## Core Idea
Geographic Information Systems (GIS) are computational systems that capture, store, analyze, and visualize spatial data, enabling geographers to overlay multiple data layers and detect spatial patterns invisible in tabular data. GIS represents the world as layers of vector (points, lines, polygons) or raster (grid) data, each carrying associated attribute information. Map projections are mathematical transformations of the spherical Earth onto flat surfaces; all projections introduce distortions of area, shape, distance, or direction, and the choice of projection is never a neutral technical decision. Remote sensing — data acquisition from satellites and aircraft — provides much of the raw imagery underlying GIS layers. The proliferation of GPS, open spatial datasets, and web mapping platforms has democratized spatial analysis but also raised concerns about surveillance and data privacy.

## How It's Best Learned
Use free GIS tools (QGIS, Google Earth Engine) to overlay demographic and environmental data layers and identify spatial correlations. Compare the Mercator, Robinson, and Peters projections and analyze what each distorts and preserves — and what political implications each carries. Practice reading choropleth, dot density, and proportional symbol maps to understand how design choices shape viewer interpretation.

## Common Misconceptions
- Maps are not neutral representations of reality; every map embeds choices about projection, scale, classification, and symbolization that shape what viewers see and conclude.
- GIS is a tool, not a method; the analytical questions and interpretive frameworks driving its use remain the responsibility of the human geographer.
- Spatial correlation on a map does not imply causation; apparent associations must be explained by theoretical mechanisms, not merely visual pattern matching.

## Questions

```yaml
- question: "A GIS analyst overlays a layer of childhood asthma rates with a layer showing proximity to highways and observes a strong spatial correlation. What is the most appropriate next step?"
  type: multiple-choice
  options: ["Publish the finding as evidence that highways cause asthma", "Dismiss the correlation because GIS cannot prove causation", "Develop a theoretical mechanism linking vehicle emissions to respiratory health and seek additional supporting evidence", "Reclassify the asthma data into fewer categories to reduce the visual correlation"]
  answer: 2
  explanation: "Spatial correlation in GIS is a hypothesis generator, not a causal proof. The correct next step is to articulate a plausible causal mechanism (vehicle emissions → particulate matter → airway inflammation) and test it with additional data — for instance, air quality measurements, longitudinal health records, or natural experiments. Dismissing the correlation ignores real signal; publishing it as causal proof commits the ecological fallacy."

- question: "Choosing the Mercator projection for a world map is a neutral technical decision with no political implications."
  type: true-false
  answer: false
  explanation: "The Mercator projection severely distorts area at high latitudes, making Greenland appear as large as Africa (in reality, Africa is about 14 times larger). This distortion systematically exaggerates the visual size of Europe and North America relative to equatorial regions. The Peters projection — which preserves area — was explicitly developed as a political counter to the Mercator. Every projection choice privileges some properties over others; those choices have implications for how viewers perceive the relative importance of different parts of the world."

- question: "What is the difference between vector and raster data formats in GIS, and give an example of when each would be appropriate?"
  type: short-answer
  answer: "Vector data represents features as discrete points, lines, or polygons with associated attributes; raster data represents the world as a grid of cells, each with a value. Vector suits discrete features like roads or country borders; raster suits continuous phenomena like elevation or land surface temperature."
  explanation: "Vector format is efficient for discrete, bounded features — a city boundary is a polygon, a river is a line, a weather station is a point. Raster format is natural for phenomena that vary continuously across space — elevation models, satellite imagery, and temperature surfaces are all grids where each pixel carries a measurement. GIS analyses often require converting between formats or overlaying both types, which is why understanding the distinction matters for choosing the right tool and interpreting outputs correctly."
```

## Explainer

A Geographic Information System is, at its core, a way of layering questions onto space. When you look at a traditional map, you see one representation of the world frozen at a moment in time. GIS replaces that single map with dozens of data layers — roads, population, rainfall, land use, pollution readings — that can be combined, queried, and analyzed computationally. The power of GIS is not just display; it is the ability to ask spatial questions: Where do high poverty rates and low supermarket access overlap? Which neighborhoods are within 500 meters of a toxic facility? How has the urban footprint of a city expanded over decades?

Data in GIS comes in two fundamental formats. Vector data represents the world as discrete geometric features — points (a hospital, a well), lines (a road, a river), or polygons (a country boundary, a census tract) — each carrying a table of attributes. Raster data divides space into a grid of equally sized cells, with each cell holding a value: a satellite image is a raster where each pixel records spectral reflectance; an elevation model is a raster where each cell records height above sea level. Neither format is inherently superior — you choose based on what you are modeling. Discrete, bounded objects are vector territory; continuous phenomena that vary across space are raster territory.

Map projections are the unavoidable compromise underlying all GIS work. The Earth is a sphere; a map is flat. Converting one to the other always distorts at least one of four properties: area, shape, distance, or direction. The Mercator projection — developed in 1569 for navigation — preserves direction perfectly (straight lines are true compass bearings) but catastrophically inflates area at high latitudes. Greenland appears roughly the same size as Africa, though Africa is nearly 14 times larger. The choice of projection is a design decision with real consequences for how viewers perceive the relative importance of different regions. There is no neutral choice.

The most critical thinking skill in GIS is resisting the visual persuasiveness of maps. When two spatial patterns overlap on a map, the temptation to infer causation is powerful — the patterns look like they "go together." But spatial correlation is not causation. Two variables can co-vary across space because they share a common cause, because they are both products of the same historical process, or even by chance at the scale you are examining (the modifiable areal unit problem: your results change depending on how you draw the boundaries). GIS surfaces patterns worth investigating; it does not supply explanations. The theoretical work remains yours.
