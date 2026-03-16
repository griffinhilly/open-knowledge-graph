---
id: earthquake-location-and-hypocenter
title: Earthquake Location and Hypocenter Determination
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: seismic-body-waves-p-and-s
  type: hard
builds-toward:
- moment-tensor-inversion
tags:
- seismology
- earthquake-location
- hypocenter
- arrival-times
stage: advanced
status: draft
---

# Earthquake Location and Hypocenter Determination

## Core Idea
Earthquake hypocenter (focus) locations are determined by measuring P and S arrival times at multiple seismometer stations and solving an inverse problem to find the source space and time coordinates. The method relies on forward modeling of travel times through a velocity model and iterative least-squares or probabilistic inversion. Hypocenter distribution reveals the geometry of faults, subduction zones, and stress accumulation zones at plate boundaries.

## Explainer

You already know that earthquakes generate P waves (compressional, faster) and S waves (shear, slower) that travel through Earth's interior at different speeds. The difference in their arrival times at a seismometer is the key to locating where an earthquake occurred. The **hypocenter** (or focus) is the point underground where rupture initiates, and the **epicenter** is the point on the surface directly above it. Determining these coordinates — plus the origin time — is one of the most fundamental tasks in seismology.

The basic principle is straightforward: because P waves travel faster than S waves, the time gap between their arrivals at a station grows with distance. If you record the P–S interval at a single station and know the velocities, you can estimate how far away the earthquake occurred — but not in which direction. With three or more stations, each providing a distance estimate, the intersection of the corresponding spheres (in three dimensions) constrains the hypocenter. This is the classic **trilateration** approach, and in its simplest form it requires only a stopwatch and a velocity model.

In practice, the problem is more complex because Earth's velocity structure is not uniform — waves speed up with depth, bend along curved ray paths, and encounter discontinuities. The modern approach treats hypocenter determination as an **inverse problem**. You start with a trial location and origin time, compute predicted arrival times at each station using ray tracing through a velocity model (the **forward problem**), then compare these predictions to the observed arrivals. The differences — called **residuals** — tell you how to adjust the trial location. Iterative algorithms like **Geiger's method** (a linearized least-squares approach) repeat this process until residuals are minimized. More sophisticated methods use probabilistic frameworks that map out the full uncertainty in the solution rather than returning a single best-fit point.

The accuracy of earthquake locations depends critically on the quality of the velocity model and the geometry of the recording network. A dense, well-distributed network of stations surrounding the source region produces tight constraints; sparse or one-sided coverage leads to large uncertainties, especially in depth. Relative relocation techniques like the **double-difference method** achieve sub-kilometer precision by exploiting the fact that closely spaced earthquakes share nearly identical ray paths, so velocity model errors cancel out. The resulting catalogs of precisely located hypocenters reveal the three-dimensional geometry of active faults, illuminate the dipping planes of subduction zones (Wadati-Benioff zones), and identify clusters of seismicity that map stress concentrations — making earthquake location the foundation upon which most seismological interpretation is built.
