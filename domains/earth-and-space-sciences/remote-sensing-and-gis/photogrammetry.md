---
id: photogrammetry
title: Photogrammetry
domain: earth-and-space-sciences
course: remote-sensing-and-gis
prerequisites:
- id: optical-remote-sensing
  type: hard
- id: digital-elevation-models
  type: soft
builds-toward:
- land-use-land-cover-mapping
tags:
- photogrammetry
- stereo-imagery
- structure-from-motion
- 3d-reconstruction
stage: advanced
status: validated
---

# Photogrammetry

## Core Idea
Photogrammetry extracts three-dimensional measurements from two-dimensional photographs by exploiting parallax -- the apparent shift of objects when viewed from different positions. When the same scene is captured from two or more viewpoints with known geometry, corresponding points in the overlapping images can be matched and their 3D coordinates computed through triangulation. Traditional photogrammetry uses precisely calibrated aerial cameras with controlled flight geometry, while modern Structure-from-Motion (SfM) photogrammetry works with unordered photographs from consumer cameras or drones, automatically solving for camera positions and scene geometry simultaneously.

## Questions

```yaml
- question: "A drone survey captures 200 overlapping photographs of a construction site. Structure-from-Motion (SfM) processing produces a 3D point cloud, orthomosaic, and DEM. What is the minimum geometric requirement for SfM to work?"
  type: multiple-choice
  options:
    - "All photographs must be taken from exactly the same altitude"
    - "Each point in the scene must be visible in at least two photographs taken from different positions, providing parallax for triangulation"
    - "The drone must fly in a perfectly straight line"
    - "At least one photograph must include a GPS antenna for georeferencing"
  answer: 1
  explanation: "SfM requires overlapping photographs from different viewpoints so that feature matching algorithms can identify common points across images and compute their 3D positions through triangulation. The parallax (apparent shift of points between views) encodes depth information. In practice, 60-80% forward overlap and 30-60% side overlap between flight lines ensures every ground point appears in multiple images."

- question: "Photogrammetric DEMs derived from optical imagery can see through forest canopy to map the bare-earth surface, just like LiDAR."
  type: true-false
  answer: false
  explanation: "Photogrammetry matches visible surface features between images, so it maps what is visible from above -- the tops of trees, not the ground beneath them. In forested areas, photogrammetric DEMs are Digital Surface Models (DSMs), not bare-earth DTMs. LiDAR pulses physically penetrate canopy gaps to reach the ground. This is a fundamental limitation of passive optical 3D reconstruction compared to active laser-based measurement."

- question: "Explain what ground control points (GCPs) contribute to a photogrammetric survey and when they might be unnecessary."
  type: short-answer
  answer: "GCPs are points with precisely known coordinates (typically surveyed with GPS) that are visible in the photographs. They anchor the photogrammetric model to real-world coordinates, correcting for systematic errors in camera position and orientation. They also enable accuracy assessment by comparing photogrammetric coordinates against known values. GCPs may be unnecessary when high-accuracy RTK/PPK GPS is integrated with the drone, providing centimeter-level camera positions directly, or when absolute georeferencing is not required (e.g., relative measurements within a scene)."
  explanation: "GCPs transform an internally consistent but arbitrarily oriented 3D model into a georeferenced product with known accuracy in a real-world coordinate system."
```

## Explainer

Photogrammetry is one of the oldest remote sensing techniques -- aerial photographs have been used for mapping since World War I. The fundamental principle is stereoscopic measurement: viewing the same scene from two different positions provides depth perception through parallax, just as human binocular vision does.

Traditional aerial photogrammetry uses precisely calibrated metric cameras mounted on aircraft flying systematic parallel flight lines with 60% forward overlap and 30% side overlap. Stereo pairs of photographs are processed in stereoplotters (originally optical instruments, now digital software) that allow operators to view the terrain in 3D and trace contours, buildings, and features. This remains the standard production method for topographic mapping and orthophoto production at national mapping agencies.

Structure-from-Motion (SfM) photogrammetry has democratized 3D measurement. SfM algorithms automatically detect and match distinctive features (keypoints) across large sets of unordered photographs, then simultaneously solve for all camera positions and a sparse 3D point cloud through bundle adjustment -- a least-squares optimization that minimizes reprojection errors across all images and points. Multi-view stereo (MVS) algorithms then densify the sparse cloud to produce millions of 3D points. The result -- a dense point cloud, mesh, orthomosaic, and DEM -- is similar to LiDAR output but derived entirely from photographs.

The combination of consumer drones and SfM software has made centimeter-resolution 3D mapping accessible for applications that previously required expensive LiDAR or aerial photography campaigns: construction monitoring, precision agriculture, archaeological documentation, mine volume calculation, and disaster damage assessment. The trade-off is that photogrammetry maps only visible surfaces and requires good lighting and texture, while LiDAR works through vegetation and in darkness.
