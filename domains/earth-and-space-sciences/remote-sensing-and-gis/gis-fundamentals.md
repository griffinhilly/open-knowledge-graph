---
id: gis-fundamentals
title: GIS Fundamentals
domain: earth-and-space-sciences
course: remote-sensing-and-gis
prerequisites:
- id: coordinate-systems-projections
  type: hard
builds-toward:
- spatial-data-models
- spatial-analysis-gis
- network-analysis-gis
- web-gis
tags:
- GIS
- geographic-information-systems
- geospatial
- mapping
stage: advanced
status: validated
---

# GIS Fundamentals

## Core Idea
A Geographic Information System (GIS) is a framework for capturing, storing, analyzing, and visualizing geographically referenced data. Unlike a simple map, a GIS links spatial features (points, lines, polygons, rasters) to attribute databases, enabling queries that combine location and characteristics: "show all parcels within 500 meters of a river that are zoned residential and have slope less than 15%." GIS integrates data from many sources (remote sensing, surveys, GPS, census, administrative records) into a common spatial framework, making it possible to ask spatial questions, detect patterns, and model scenarios that would be impossible with tabular data alone.

## Questions

```yaml
- question: "A city planner needs to identify suitable locations for a new fire station. The site must be within 200 meters of a main road, more than 500 meters from existing stations, on publicly owned land, and on slopes less than 10%. Which GIS operation framework is most appropriate?"
  type: multiple-choice
  options:
    - "Simple visual inspection of a printed map"
    - "Multi-criteria overlay analysis: buffer main roads (200m), buffer existing stations (500m exclusion zone), select public parcels, derive slope from DEM, then intersect all criteria to identify candidate areas"
    - "Geocoding the addresses of all existing fire stations"
    - "Creating a 3D fly-through visualization of the city"
  answer: 1
  explanation: "This is a classic suitability analysis that combines proximity (buffering), attribute selection, and terrain analysis. GIS overlay operations intersect these derived layers to identify areas satisfying ALL criteria simultaneously -- a task that is essentially impossible without spatial data integration."

- question: "GIS is primarily a map-making tool, similar to graphic design software."
  type: true-false
  answer: false
  explanation: "Map production is one output of GIS, but the core capability is spatial analysis -- the ability to query, combine, transform, and model geographic data to answer questions about spatial relationships, patterns, and processes. GIS integrates a database management system (for storing and querying attributes), spatial analysis tools (for proximity, overlay, network, and terrain analysis), and visualization. A map is a communication product; GIS is an analytical framework."

- question: "Explain the difference between a GIS layer showing land parcels and the same information printed on a paper map."
  type: short-answer
  answer: "A GIS layer links each parcel polygon to a database record containing attributes (owner, area, zoning, tax value, date of sale, etc.) that can be queried, filtered, and analyzed programmatically. The geometry has precise coordinates enabling measurement, overlay with other layers, and spatial analysis. A paper map shows only what was printed -- fixed attributes at a fixed scale with no database connection. You cannot query a paper map for all parcels over 5 acres, calculate distances, or overlay flood zones. The GIS layer is dynamic, queryable, and analytically powerful; the paper map is static and visual only."
  explanation: "The fundamental distinction is that GIS data is computable -- it can be queried, transformed, and combined -- while a paper map is a fixed visual representation."
```

## Explainer

GIS emerged in the 1960s from the realization that geographic data stored digitally could be analyzed in ways impossible with paper maps. The core innovation was linking spatial features (where things are) with attributes (what they are), enabling queries that combine spatial and thematic criteria.

A GIS organizes data in layers (or themes), each representing a different type of geographic feature: roads, buildings, land parcels, elevation, land cover, soil types, population density. Each layer shares a common coordinate system, allowing them to be overlaid and combined. Vector layers represent discrete features as points (wells, stations), lines (roads, rivers), or polygons (parcels, lakes) with associated attribute tables. Raster layers represent continuous phenomena (elevation, temperature, satellite imagery) as regular grids of cells.

The analytical power of GIS comes from spatial operations. Buffering creates zones at specified distances from features. Overlay operations (intersection, union, difference) combine layers to identify areas meeting multiple criteria. Network analysis finds shortest paths, service areas, and optimal routes. Terrain analysis derives slope, aspect, and watersheds from elevation data. Spatial statistics identify clusters, hotspots, and spatial autocorrelation. Each operation leverages the explicit spatial relationships that distinguish geographic data from ordinary tabular data.

Modern GIS has evolved from expensive desktop software (ArcGIS, QGIS) into a broad ecosystem including web-based platforms (ArcGIS Online, Google Earth Engine), spatial databases (PostGIS), programming libraries (GeoPandas, sf in R), and cloud-native geospatial formats. The fundamental principles remain: geographic data integration, spatial analysis, and evidence-based spatial decision-making.
