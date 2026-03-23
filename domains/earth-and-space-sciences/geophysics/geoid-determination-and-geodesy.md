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
stage: expert
status: draft
---

# Geoid Determination and Geodesy

## Core Idea
The geoid is the equipotential surface of Earth's gravity field coinciding with mean sea level; it deviates from an ideal ellipsoid by up to ±100 m due to density variations in crust and mantle. Geoid undulations reflect the response to isostatic and dynamic processes: positive undulations occur over dense subducting slabs, and negative undulations over hot buoyant mantle plumes. Satellite missions like GRACE measure the geoid with high precision, constraining subsurface mass anomalies and time-varying mass transport.

## Questions

```yaml
- question: "A GPS receiver reports an ellipsoidal height of 80 meters at a location where the geoid undulation (geoid height above the ellipsoid) is +25 meters. What is the orthometric height — the true elevation above sea level — at that location?"
  type: multiple-choice
  options:
    - "105 meters — add the geoid undulation to the ellipsoidal height"
    - "55 meters — subtract the geoid undulation from the ellipsoidal height"
    - "80 meters — GPS directly measures elevation above sea level"
    - "25 meters — the geoid undulation is the actual elevation"
  answer: 1
  explanation: "Orthometric height H = ellipsoidal height h − geoid undulation N. Here: H = 80 − 25 = 55 m. The geoid undulation N is the height of the geoid *above* the ellipsoid; a positive N means the geoid surface is higher than the ellipsoid at that point. GPS measures height above the ellipsoid (a mathematical surface), but sea level and drainage follow the geoid (a physical equipotential surface). Subtracting N converts GPS ellipsoidal height to the meaningful engineering quantity. Adding them (option A) gets the sign wrong."

- question: "A positive geoid undulation — where the geoid surface rises above the reference ellipsoid — occurs over what type of subsurface feature, and why?"
  type: multiple-choice
  options:
    - "Over a low-density mantle plume, because the lighter material pushes the crust upward, creating a surface bulge"
    - "Over a dense subducting slab, because the extra mass increases gravitational attraction, pulling the equipotential surface upward toward the denser material"
    - "Over oceanic trenches, because water is denser than continental crust and raises the gravity field"
    - "Over regions of recent glacial retreat, because removing ice reduces pressure and allows the geoid to rise"
  answer: 1
  explanation: "A positive geoid undulation (geoid above the ellipsoid) indicates excess mass below. Dense material — like a cold, subducting slab — exerts stronger gravitational attraction, pulling the equipotential surface upward toward it. Conversely, a hot, buoyant, low-density mantle plume creates a mass deficit, and the geoid dips below the ellipsoid (negative undulation). The geoid is a direct map of subsurface mass distribution, not surface topography."

- question: "GPS receivers directly measure elevation above sea level, making geoid models unnecessary for surveying and engineering applications."
  type: true-false
  answer: false
  explanation: "GPS receivers measure height above the *reference ellipsoid* — a smooth mathematical surface that approximates Earth's shape. Sea level (and the direction water flows) follows the *geoid*, which is a physical equipotential surface that can deviate from the ellipsoid by up to ±100 meters. Without applying a geoid undulation correction, GPS heights cannot be used for drainage engineering, flood mapping, or any application where gravity-driven flow matters. National geoid models exist precisely to bridge this gap."

- question: "The geoid is an equipotential surface of Earth's gravity field, which means water on a perfectly still geoid surface would not flow in any direction."
  type: true-false
  answer: true
  explanation: "An equipotential surface is one where the gravitational potential is constant everywhere — no potential energy gradient exists along the surface, so no gravitational force acts to move an object along it. A ball or water droplet placed on a perfect equipotential would experience no net force parallel to the surface. This is precisely why the geoid is the natural reference for elevation: 'above sea level' means above this surface, and water at rest always lies on it. Any deviation from the geoid creates a slope in the potential, which drives water flow."

- question: "Why does the geoid deviate from the reference ellipsoid by up to ±100 meters, and what does this tell us about Earth's interior?"
  type: short-answer
  answer: "The reference ellipsoid assumes Earth has a smoothly varying, rotationally symmetric internal density. In reality, Earth's interior is heterogeneous: dense subducting slabs, light mantle plumes, thick continental roots, and ocean sediment basins all create lateral density variations. These mass anomalies warp the gravitational potential field, pulling equipotential surfaces toward dense regions and pushing them away from low-density regions. The geoid undulations — where the geoid diverges from the ellipsoid — are therefore a direct map of subsurface mass distribution, revealing structures we cannot directly observe."
  explanation: "This connection between surface gravity measurements and subsurface structure is the foundation of geodesy and satellite gravity missions like GRACE. The GRACE mission exploited this by measuring geoid changes over time, revealing ice sheet loss, groundwater depletion, and post-glacial rebound — all of which represent mass redistribution that shifts the geoid. The geoid is thus not just a static reference surface but a dynamic window into Earth's interior and its ongoing mass transport."
```

## Explainer

From your study of gravity potential theory, you know that Earth's gravitational field can be described by a potential function whose value decreases with distance from mass concentrations. An **equipotential surface** is one where the gravity potential is constant everywhere — no work is done moving along it, so a ball placed on it would not roll in any direction. The **geoid** is a particular equipotential surface: the one that coincides with mean sea level in the oceans. If the continents were sliced through at sea level and connected by canals, the water surface in those canals would trace the geoid across the land masses. It is the natural reference surface for elevation — "height above sea level" really means height above the geoid.

If Earth were a perfectly uniform rotating body, the geoid would be a simple **reference ellipsoid** — a slightly flattened sphere bulging at the equator due to centrifugal force. But Earth's interior is not uniform. Dense subducting slabs, buoyant mantle plumes, thick continental roots, and sedimentary basins create lateral density variations that warp the gravity field. The geoid therefore undulates above and below the reference ellipsoid by as much as ±100 meters. These **geoid undulations** are a direct map of subsurface mass distribution: a positive undulation (geoid above the ellipsoid) indicates excess mass below, such as a cold, dense subducting slab, while a negative undulation signals a mass deficit, perhaps from a hot, buoyant mantle upwelling.

Measuring the geoid precisely requires separating its signal from the much larger ellipsoidal shape. Ground-based gravimeters provide pointwise measurements, but global coverage comes from satellite missions. The **GRACE** (Gravity Recovery and Climate Experiment) mission measures the geoid by tracking the distance between two co-orbiting satellites with micrometer precision: when the lead satellite passes over a mass concentration, it accelerates slightly, increasing the inter-satellite distance. These perturbations are inverted into a global gravity field model expressed as a spherical harmonic expansion. Successive monthly solutions reveal **time-varying** mass changes — ice sheet loss in Greenland, groundwater depletion in aquifers, post-glacial rebound of Scandinavia — making the geoid not just a static reference surface but a dynamic monitor of mass transport across the Earth system.

In practical geodesy, the distinction between the geoid and the ellipsoid matters for everything from surveying to GPS. GPS receivers measure heights relative to the ellipsoid (a mathematical surface), but engineers and mapmakers need heights relative to the geoid (a physical surface tied to water flow). The difference — the **geoid undulation** at a given location — must be added or subtracted to convert between the two. National survey agencies maintain detailed geoid models for their territories precisely because getting this conversion wrong by even a few centimeters can cause drainage systems to flow the wrong way or tunnel bores to miss their targets.
