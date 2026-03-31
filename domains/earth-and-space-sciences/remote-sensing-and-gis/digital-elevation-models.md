---
id: digital-elevation-models
title: Digital Elevation Models
domain: earth-and-space-sciences
course: remote-sensing-and-gis
prerequisites:
- id: radar-remote-sensing-sar
  type: soft
- id: lidar-principles
  type: soft
- id: gis-fundamentals
  type: hard
builds-toward:
- spatial-analysis-gis
- photogrammetry
tags:
- DEM
- DTM
- DSM
- terrain-analysis
- elevation
stage: advanced
status: validated
---

# Digital Elevation Models

## Core Idea
A Digital Elevation Model (DEM) is a gridded representation of terrain elevation where each cell stores a height value. DEMs come in two main variants: Digital Terrain Models (DTM) represent the bare-earth surface with vegetation and buildings removed, while Digital Surface Models (DSM) include the tops of all features. DEMs are derived from multiple sources -- stereo photogrammetry, InSAR, LiDAR, and GPS surveys -- each with different accuracy, resolution, and coverage characteristics. DEMs underpin slope analysis, watershed delineation, viewshed computation, flood modeling, orthorectification of imagery, and countless other spatial analyses.

## Questions

```yaml
- question: "A flood modeler needs to determine which areas would be inundated if a river rises 3 meters. Why is a LiDAR-derived DTM preferred over an SRTM DEM for this analysis?"
  type: multiple-choice
  options:
    - "SRTM has global coverage while LiDAR is only available locally"
    - "LiDAR DTM has centimeter-level vertical accuracy and represents bare earth, while SRTM (~30m resolution, ~10m vertical accuracy) is a DSM that includes canopy and buildings, overestimating surface elevation in vegetated and urban areas"
    - "SRTM data is classified and unavailable for civilian flood modeling"
    - "LiDAR produces colored elevation maps while SRTM produces grayscale"
  answer: 1
  explanation: "Flood models require accurate bare-earth elevation to determine flow paths and inundation extent. SRTM's C-band radar reflects off vegetation canopy and building roofs, producing a DSM that overestimates ground elevation -- potentially hiding low-lying areas from the flood model. SRTM's ~10m vertical uncertainty also exceeds the 3m flood scenario. LiDAR penetrates vegetation (via last returns) to map bare earth with ~10 cm accuracy, revealing the true terrain that water would follow."

- question: "The terms DEM, DTM, and DSM all refer to the same type of elevation data."
  type: true-false
  answer: false
  explanation: "DEM is a general term for any gridded elevation representation. DTM specifically represents the bare-earth terrain surface (no vegetation or buildings). DSM represents the elevation of the highest surface including tree canopy, buildings, and other structures. The distinction matters enormously: a DTM is needed for flood modeling (water flows on the ground), while a DSM is needed for viewshed analysis (visibility is blocked by trees and buildings) or urban planning."

- question: "Explain how InSAR generates a DEM from two SAR images acquired from slightly different orbital positions."
  type: short-answer
  answer: "Two SAR antennas (or one antenna in two orbital passes) view the same terrain from slightly different positions, creating a baseline. The phase difference between the two radar returns for each pixel is related to the path length difference, which depends on the viewing geometry and the terrain height. By knowing the precise baseline geometry and unwrapping the phase (which repeats every 2-pi radians), the height of each pixel can be calculated trigonometrically. This is how SRTM generated near-global elevation data in 11 days using a fixed 60-meter baseline on the Space Shuttle."
  explanation: "InSAR elevation measurement is essentially parallax (like stereo vision) measured through phase differences rather than pixel offsets, achieving high precision from the sub-wavelength sensitivity of phase measurements."
```

## Explainer

Elevation data is the third dimension that transforms 2D mapping into 3D understanding of the landscape. A DEM encodes the shape of the terrain -- ridgelines, valleys, slopes, flat plains -- in a regular grid that computers can analyze systematically.

The source technology determines DEM characteristics. LiDAR produces the highest-accuracy DEMs (5-15 cm vertical accuracy) with the ability to separate bare earth from vegetation and buildings, but coverage is limited and acquisition is expensive. InSAR provides moderate-accuracy global DEMs -- SRTM (30 m, ~10 m vertical accuracy) and TanDEM-X (12 m, ~2 m vertical accuracy) cover most of Earth's land surface, but these are DSMs that include canopy. Stereo photogrammetry from optical satellites generates DEMs from parallax between images, with accuracy depending on the baseline and image resolution.

Terrain derivatives computed from DEMs include slope (the rate of elevation change), aspect (the compass direction a slope faces), curvature (how slope changes across the surface), hillshade (simulated illumination for visualization), and hydrological products like flow direction, flow accumulation, and watershed boundaries. These derivatives are often more useful than raw elevation for analysis -- slope determines erosion potential and construction suitability; aspect controls solar exposure and microclimate; watershed boundaries define the fundamental units of hydrological management.

DEM quality assessment requires understanding the error characteristics of the source. LiDAR accuracy degrades in dense vegetation (fewer ground returns), steep slopes (larger footprints), and areas with low point density. InSAR DEMs have systematic biases in vegetation (canopy elevation, not ground), urban areas (layover effects), and steep terrain (shadow and layover). Knowing these error patterns is essential for choosing the right DEM for each application and interpreting results appropriately.
