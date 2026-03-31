---
id: coordinate-systems-projections
title: Coordinate Systems and Map Projections
domain: earth-and-space-sciences
course: remote-sensing-and-gis
prerequisites:
- id: electromagnetic-spectrum-remote-sensing
  type: soft
builds-toward:
- gis-fundamentals
- image-preprocessing-remote-sensing
- spatial-analysis-gis
tags:
- coordinate-systems
- map-projections
- geodesy
- georeference
stage: advanced
status: validated
---

# Coordinate Systems and Map Projections

## Core Idea
Representing Earth's curved surface on flat maps or in digital systems requires two concepts: a geographic coordinate system (GCS) that defines locations on the 3D ellipsoid using latitude and longitude, and a map projection that transforms those 3D coordinates onto a 2D plane. Every projection distorts reality -- it is mathematically impossible to flatten a sphere without distorting area, shape, distance, or direction. Conformal projections (like UTM/Transverse Mercator) preserve local shapes and angles at the cost of area distortion; equal-area projections preserve area at the cost of shape. Choosing the right coordinate system and projection for a given analysis is essential because using the wrong one introduces systematic spatial errors.

## Questions

```yaml
- question: "A GIS analyst calculates the area of forest polygons using geographic coordinates (latitude/longitude in WGS 84) and gets results in square degrees. What is wrong with this approach?"
  type: multiple-choice
  options:
    - "WGS 84 is an outdated coordinate system"
    - "Geographic coordinates are angular units on a curved surface; area calculations require data projected to a planar coordinate system with linear units (meters), ideally using an equal-area projection to avoid systematic area distortion"
    - "The analyst should have used feet instead of degrees"
    - "Forest polygons cannot be represented in geographic coordinates"
  answer: 1
  explanation: "Latitude and longitude are angles, not distances. One degree of longitude covers ~111 km at the equator but ~0 km at the poles. Area in square degrees is physically meaningless and will be systematically wrong -- overestimating area near the equator and underestimating it at high latitudes. Projecting to a local equal-area projection converts angular coordinates to meters and preserves area relationships."

- question: "The Universal Transverse Mercator (UTM) system divides Earth into 60 zones, each 6 degrees of longitude wide, because a single Transverse Mercator projection cannot accurately cover the entire globe."
  type: true-false
  answer: true
  explanation: "The Transverse Mercator projection is accurate near its central meridian but distortion increases with distance. By limiting each zone to 6 degrees of longitude, UTM keeps maximum scale distortion below 0.04% -- adequate for large-scale mapping and engineering. Using a single zone for the entire globe would produce extreme distortion far from the central meridian. This zone system is why UTM coordinates always include a zone number."

- question: "Explain the difference between a datum and a map projection, and why both are needed to define a coordinate reference system."
  type: short-answer
  answer: "A datum defines the size, shape, and orientation of the reference ellipsoid (mathematical model of Earth's shape) and its relationship to Earth's actual surface. WGS 84 and NAD 83 are datums with slightly different ellipsoid parameters and alignment. A map projection is the mathematical transformation that converts 3D ellipsoidal coordinates (latitude/longitude on a specific datum) to 2D planar coordinates (x, y in meters). Both are needed because the projection operates on the ellipsoid defined by the datum -- using the wrong datum shifts features by meters to hundreds of meters, while using the wrong projection distorts shapes, areas, or distances."
  explanation: "Datum = which Earth model; Projection = how to flatten it. Together they form a complete Coordinate Reference System (CRS) like UTM Zone 15N on WGS 84 (EPSG:32615)."
```

## Explainer

Every point on Earth's surface needs an address that digital systems can use. Geographic coordinate systems provide this using latitude (angle north or south of the equator) and longitude (angle east or west of the prime meridian), referenced to a mathematical model of Earth's shape called a datum. The datum specifies the reference ellipsoid -- a slightly flattened sphere that approximates Earth's shape -- and how it aligns with the real surface. Different datums (WGS 84, NAD 83, ED50) have slightly different ellipsoid parameters and positions, so the same physical location has slightly different latitude/longitude values in different datums.

Map projections transform these 3D angular coordinates into 2D planar coordinates suitable for mapping and analysis. The fundamental constraint is Gauss's Theorema Egregium: a curved surface cannot be flattened without distortion. Every projection is a compromise. Mercator projections preserve angles and shapes locally (conformal) but grossly distort area at high latitudes -- Greenland appears the size of Africa when it is actually 14 times smaller. Equal-area projections like Albers preserve area but distort shapes. Equidistant projections preserve distances along certain lines.

For most GIS work, the Universal Transverse Mercator (UTM) system provides a practical solution. It divides Earth into 60 zones, each using a Transverse Mercator projection centered on that zone's central meridian. Within each 6-degree zone, distortion is minimal and coordinates are in meters -- suitable for distance, area, and direction calculations. For analyses spanning multiple zones or entire continents, equal-area projections are preferred for area calculations, while conformal projections are preferred for navigation and shape-preserving mapping.

Understanding coordinate systems prevents a common class of GIS errors: misaligned data, incorrect area calculations, shifted features, and incompatible overlays. When data layers appear offset from each other, the first thing to check is whether they share the same coordinate reference system -- and if not, whether a proper transformation (not just reprojection but datum transformation) has been applied.
