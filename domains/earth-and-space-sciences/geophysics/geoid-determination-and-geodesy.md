---
id: geoid-determination-and-geodesy
title: Geoid Determination and Geodesy
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: gravity-potential-theory-earths-field
  type: hard
builds-toward:
- gps-geodesy-and-crustal-deformation
tags:
- geodesy
- geoid
- ellipsoid
- gravity-field
stage: advanced
status: draft
---

# Geoid Determination and Geodesy

## Core Idea
The geoid is the equipotential surface of Earth's gravity field coinciding with mean sea level; it deviates from an ideal ellipsoid by up to ±100 m due to density variations in crust and mantle. Geoid undulations reflect the response to isostatic and dynamic processes: positive undulations occur over dense subducting slabs, and negative undulations over hot buoyant mantle plumes. Satellite missions like GRACE measure the geoid with high precision, constraining subsurface mass anomalies and time-varying mass transport.

## Explainer

From your study of gravity potential theory, you know that Earth's gravitational field can be described by a potential function whose value decreases with distance from mass concentrations. An **equipotential surface** is one where the gravity potential is constant everywhere — no work is done moving along it, so a ball placed on it would not roll in any direction. The **geoid** is a particular equipotential surface: the one that coincides with mean sea level in the oceans. If the continents were sliced through at sea level and connected by canals, the water surface in those canals would trace the geoid across the land masses. It is the natural reference surface for elevation — "height above sea level" really means height above the geoid.

If Earth were a perfectly uniform rotating body, the geoid would be a simple **reference ellipsoid** — a slightly flattened sphere bulging at the equator due to centrifugal force. But Earth's interior is not uniform. Dense subducting slabs, buoyant mantle plumes, thick continental roots, and sedimentary basins create lateral density variations that warp the gravity field. The geoid therefore undulates above and below the reference ellipsoid by as much as ±100 meters. These **geoid undulations** are a direct map of subsurface mass distribution: a positive undulation (geoid above the ellipsoid) indicates excess mass below, such as a cold, dense subducting slab, while a negative undulation signals a mass deficit, perhaps from a hot, buoyant mantle upwelling.

Measuring the geoid precisely requires separating its signal from the much larger ellipsoidal shape. Ground-based gravimeters provide pointwise measurements, but global coverage comes from satellite missions. The **GRACE** (Gravity Recovery and Climate Experiment) mission measures the geoid by tracking the distance between two co-orbiting satellites with micrometer precision: when the lead satellite passes over a mass concentration, it accelerates slightly, increasing the inter-satellite distance. These perturbations are inverted into a global gravity field model expressed as a spherical harmonic expansion. Successive monthly solutions reveal **time-varying** mass changes — ice sheet loss in Greenland, groundwater depletion in aquifers, post-glacial rebound of Scandinavia — making the geoid not just a static reference surface but a dynamic monitor of mass transport across the Earth system.

In practical geodesy, the distinction between the geoid and the ellipsoid matters for everything from surveying to GPS. GPS receivers measure heights relative to the ellipsoid (a mathematical surface), but engineers and mapmakers need heights relative to the geoid (a physical surface tied to water flow). The difference — the **geoid undulation** at a given location — must be added or subtracted to convert between the two. National survey agencies maintain detailed geoid models for their territories precisely because getting this conversion wrong by even a few centimeters can cause drainage systems to flow the wrong way or tunnel bores to miss their targets.
