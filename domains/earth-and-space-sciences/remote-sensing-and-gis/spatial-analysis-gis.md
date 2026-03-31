---
id: spatial-analysis-gis
title: Spatial Analysis in GIS
domain: earth-and-space-sciences
course: remote-sensing-and-gis
prerequisites:
- id: gis-fundamentals
  type: hard
- id: spatial-data-models
  type: hard
builds-toward:
- geostatistics
- network-analysis-gis
tags:
- spatial-analysis
- overlay
- buffering
- proximity
stage: advanced
status: validated
---

# Spatial Analysis in GIS

## Core Idea
Spatial analysis encompasses the quantitative techniques for examining the locations, attributes, and relationships of geographic features. Core operations include overlay (combining layers to find areas meeting multiple criteria), buffering (creating distance zones around features), proximity analysis (measuring distances and identifying nearest neighbors), map algebra (cell-by-cell raster calculations), and spatial statistics (identifying clusters, hotspots, and spatial patterns). These operations exploit the fundamental property of geographic data -- that location matters, and nearby things tend to be more related than distant things (Tobler's First Law of Geography).

## Questions

```yaml
- question: "An environmental agency needs to identify wetlands within 1 km of a highway that also fall within a designated conservation zone. Which sequence of spatial operations accomplishes this?"
  type: multiple-choice
  options:
    - "Geocode the highway, then reclassify the wetland raster"
    - "Buffer the highway by 1 km, then intersect the buffer with both the wetland layer and the conservation zone layer"
    - "Merge all three layers into a single dataset and filter by attribute"
    - "Calculate NDVI for the highway corridor"
  answer: 1
  explanation: "Buffering creates a 1 km zone around the highway. Intersection is the overlay operation that identifies areas where all three conditions overlap: within the buffer, classified as wetland, and within the conservation zone. This is the fundamental GIS workflow for multi-criteria site selection."

- question: "Tobler's First Law of Geography states that everything is related to everything else, but near things are more related than distant things. This principle is irrelevant to modern spatial analysis."
  type: true-false
  answer: false
  explanation: "Tobler's First Law is foundational to spatial analysis. It underlies spatial autocorrelation (why nearby measurements tend to be similar), interpolation (why we can estimate unknown values from nearby known values), and geostatistics (kriging explicitly models the distance-dependence of correlation). Spatial analysis techniques that ignore this principle produce unreliable results."

- question: "Explain the difference between a buffer operation and a Thiessen (Voronoi) polygon operation, and give one application of each."
  type: short-answer
  answer: "A buffer creates a zone of specified distance around features (e.g., 500m buffer around a pollution source to define an impact zone). A Thiessen/Voronoi polygon partitions space so that every location is assigned to its nearest input point, creating polygons where all points inside are closer to that polygon's generator than to any other. Application: buffers define exclusion zones, impact areas, or service areas at fixed distances. Thiessen polygons define service territories (e.g., assigning each address to its nearest school or hospital based on straight-line proximity)."
  explanation: "Buffers are distance-from-feature operations; Thiessen polygons are nearest-neighbor-assignment operations. Both answer proximity questions but in fundamentally different ways."
```

## Explainer

Spatial analysis is what separates a GIS from a digital map. While a map shows where things are, spatial analysis answers questions about why they are there, what is nearby, where conditions overlap, and how patterns vary across space.

Overlay operations are the workhorses of spatial analysis. Vector overlay (intersection, union, identity, erase) combines the geometry and attributes of two or more layers, producing new features where inputs overlap. Raster overlay (map algebra) performs cell-by-cell calculations -- adding, multiplying, or applying conditional logic to grid layers. A classic suitability analysis might weight and combine slope, soil type, proximity to roads, and land cover rasters to produce a composite suitability score for each cell.

Proximity analysis measures spatial relationships. Buffering creates distance zones. Near analysis finds the closest feature. Point-in-polygon determines which polygon contains each point. Distance matrices compute all pairwise distances. These operations answer questions like "how far is each house from the nearest fire station?" or "how many schools are within 2 km of each park?"

Spatial statistics move beyond simple description to inference. Point pattern analysis tests whether features are clustered, dispersed, or random. Hotspot analysis (Getis-Ord Gi*) identifies statistically significant concentrations of high or low values. Spatial autocorrelation (Moran's I) quantifies the degree to which nearby locations have similar values. These tools reveal patterns that visual inspection might miss and provide statistical rigor for spatial decision-making.
