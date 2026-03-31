---
id: spatial-data-models
title: Spatial Data Models
domain: earth-and-space-sciences
course: remote-sensing-and-gis
prerequisites:
- id: gis-fundamentals
  type: hard
builds-toward:
- spatial-analysis-gis
- web-gis
tags:
- vector-data
- raster-data
- spatial-data
- data-models
stage: advanced
status: validated
---

# Spatial Data Models

## Core Idea
Spatial data represents geographic features using two fundamental models. The vector model represents discrete features as points, lines, and polygons defined by coordinate pairs, with associated attribute tables -- ideal for boundaries, networks, and discrete objects (buildings, roads, parcels). The raster model represents continuous phenomena as regular grids of cells (pixels), each storing a value -- ideal for elevation, temperature, satellite imagery, and any field that varies continuously across space. Choosing between vector and raster (or combining both) depends on the nature of the phenomenon, the analysis to be performed, and the required precision of boundary representation.

## Questions

```yaml
- question: "A hydrologist needs to model water flow across a landscape. Should the elevation data be stored as vector contour lines or a raster DEM?"
  type: multiple-choice
  options:
    - "Vector contour lines, because they show elevation more precisely"
    - "A raster DEM, because flow algorithms require a continuous grid where each cell has a defined elevation, slope, and flow direction to its neighbors"
    - "Either format works equally well for flow modeling"
    - "Vector points at surveyed locations, interpolated on the fly during analysis"
  answer: 1
  explanation: "Hydrological flow modeling algorithms (D8, D-infinity) operate on raster grids, calculating flow direction from each cell to its lowest neighbor. This requires every location to have a defined elevation. Vector contours only represent elevation at specific intervals, leaving gaps between contours where elevation is undefined. The raster DEM provides the continuous elevation surface that flow algorithms require."

- question: "Vector data is always more accurate than raster data for representing geographic features."
  type: true-false
  answer: false
  explanation: "Accuracy depends on the data source and the phenomenon being represented, not the data model. A high-resolution raster (1 m cells) may represent boundaries more accurately than a generalized vector dataset digitized from a 1:100,000 map. For continuous phenomena like elevation or temperature, raster is the natural representation; forcing these into vector format (contours) actually loses information. Each model suits different phenomena and analyses."

- question: "Explain the concept of topology in vector GIS data and why it matters for spatial analysis."
  type: short-answer
  answer: "Topology defines the spatial relationships between features: which polygons share boundaries, which lines connect at nodes, which polygons are adjacent. Without topology, polygons might overlap or have gaps at shared boundaries, lines might fail to connect at intersections, and adjacent features might have inconsistent boundaries. Topology rules enforce data integrity (no gaps, no overlaps, shared boundaries stored once) and enable spatial queries that depend on connectivity and adjacency -- like finding all parcels adjacent to a given parcel, or tracing connected river segments from source to mouth."
  explanation: "Topology transforms a collection of independent geometric shapes into a structured spatial network where relationships between features are explicitly defined and maintained."
```

## Explainer

The choice of spatial data model is the first and most consequential decision in any GIS project, because it determines what analyses are possible, how storage and processing scale, and how accurately the real world is represented.

The vector model excels at representing discrete features with well-defined boundaries. A land parcel is naturally a polygon with precise coordinates; a road is naturally a line; a fire hydrant is naturally a point. Each feature links to a row in an attribute table, making vector data ideal for database-style queries ("select all parcels zoned commercial with area over 1 hectare"). Common vector formats include Shapefile, GeoJSON, GeoPackage, and features stored in spatial databases (PostGIS, SpatiaLite).

The raster model excels at representing continuous phenomena -- elevation, temperature, precipitation, satellite imagery, land cover probability. Each cell in the grid stores a single value, and the grid's resolution (cell size) determines the spatial detail. Raster data is computationally efficient for map algebra -- cell-by-cell mathematical operations like adding two layers, computing slope from elevation, or creating NDVI from red and NIR bands. Common raster formats include GeoTIFF, NetCDF, and cloud-optimized GeoTIFF (COG).

Many analyses combine both models. A flood analysis might use a raster DEM for hydrological modeling, then convert the inundation boundary to a vector polygon for overlay with vector parcel data to identify affected properties. Remote sensing classification produces raster land cover maps that are often vectorized for integration with administrative boundaries. Understanding the strengths, limitations, and conversion pathways between vector and raster is essential for effective GIS work.
