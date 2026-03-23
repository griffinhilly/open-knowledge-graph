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
stage: expert
status: draft
---

# Earthquake Location and Hypocenter Determination

## Core Idea
Earthquake hypocenter (focus) locations are determined by measuring P and S arrival times at multiple seismometer stations and solving an inverse problem to find the source space and time coordinates. The method relies on forward modeling of travel times through a velocity model and iterative least-squares or probabilistic inversion. Hypocenter distribution reveals the geometry of faults, subduction zones, and stress accumulation zones at plate boundaries.

## Questions

```yaml
- question: "A seismologist records P and S wave arrivals at a single station following an earthquake, with a P–S arrival time gap of 25 seconds. What can be determined from this measurement alone?"
  type: multiple-choice
  options:
    - "The exact latitude and longitude of the epicenter"
    - "The depth of the hypocenter below the surface"
    - "The approximate distance from the station to the earthquake source"
    - "The magnitude and seismic moment of the earthquake"
  answer: 2
  explanation: "Because P and S waves travel at known speeds, the time gap between their arrivals is proportional to the distance traveled. A single station gives a distance estimate — placing the source somewhere on a sphere of that radius — but provides no directional information. At least three stations are needed to triangulate a 3D location. Magnitude requires wave amplitude, not just arrival timing."

- question: "The double-difference relocation method achieves sub-kilometer precision for earthquake clusters primarily because:"
  type: multiple-choice
  options:
    - "It uses a much denser network of seismometer stations than conventional methods"
    - "It applies a probabilistic Bayesian framework instead of least-squares inversion"
    - "Nearby earthquakes share nearly identical ray paths, so velocity model errors cancel in the difference"
    - "It measures absolute rather than differential arrival times, reducing timing uncertainty"
  answer: 2
  explanation: "The core insight is that two earthquakes occurring close together send waves along nearly the same ray paths to any given station. Velocity model errors affect both wave trains almost identically, so when you difference the arrival times of the two events, those errors cancel out. The remaining signal reflects only the small spatial separation between the two hypocenters, enabling very precise relative locations even with an imperfect velocity model."

- question: "The epicenter of an earthquake is the underground point where fault rupture initiates."
  type: true-false
  answer: false
  explanation: "The hypocenter (or focus) is the point underground where rupture initiates. The epicenter is the point on Earth's surface directly above the hypocenter. This distinction matters in hazard assessment: the epicenter may be far from the actual rupture zone if the fault is deep or has significant along-strike extent."

- question: "Recording P and S wave arrivals at only two seismometer stations is insufficient to uniquely determine the three-dimensional location of an earthquake hypocenter."
  type: true-false
  answer: true
  explanation: "Locating a hypocenter requires solving for four unknowns: three spatial coordinates (x, y, z) plus origin time. Each P–S pair from a station constrains distance but not direction. Two stations provide two distance spheres that intersect in a circle, not a point — the location remains ambiguous. In practice, at least three stations (providing multiple distance spheres whose intersection narrows to one or two points) are needed, and four or more are required to solve the full four-unknown system reliably."

- question: "Why does Geiger's method use an iterative algorithm to locate earthquake hypocenters rather than solving directly for the source coordinates in a single calculation?"
  type: short-answer
  answer: "The relationship between hypocenter coordinates and observed arrival times is nonlinear — it depends on ray tracing through a velocity model with curved ray paths. Geiger's method linearizes this relationship around a trial solution, solves the linear system for a correction, applies the correction, and repeats. Direct solution would require inverting a nonlinear system, which has no general closed-form solution."
  explanation: "This is a general feature of inverse problems in geophysics: the forward model (computing predicted arrivals from a given location) is straightforward, but inverting it to find location from arrivals requires iterative refinement. The quality of convergence depends on how good the initial guess is and how well-conditioned the problem is — which is why network geometry and velocity model accuracy matter so much."
```

## Explainer

You already know that earthquakes generate P waves (compressional, faster) and S waves (shear, slower) that travel through Earth's interior at different speeds. The difference in their arrival times at a seismometer is the key to locating where an earthquake occurred. The **hypocenter** (or focus) is the point underground where rupture initiates, and the **epicenter** is the point on the surface directly above it. Determining these coordinates — plus the origin time — is one of the most fundamental tasks in seismology.

The basic principle is straightforward: because P waves travel faster than S waves, the time gap between their arrivals at a station grows with distance. If you record the P–S interval at a single station and know the velocities, you can estimate how far away the earthquake occurred — but not in which direction. With three or more stations, each providing a distance estimate, the intersection of the corresponding spheres (in three dimensions) constrains the hypocenter. This is the classic **trilateration** approach, and in its simplest form it requires only a stopwatch and a velocity model.

In practice, the problem is more complex because Earth's velocity structure is not uniform — waves speed up with depth, bend along curved ray paths, and encounter discontinuities. The modern approach treats hypocenter determination as an **inverse problem**. You start with a trial location and origin time, compute predicted arrival times at each station using ray tracing through a velocity model (the **forward problem**), then compare these predictions to the observed arrivals. The differences — called **residuals** — tell you how to adjust the trial location. Iterative algorithms like **Geiger's method** (a linearized least-squares approach) repeat this process until residuals are minimized. More sophisticated methods use probabilistic frameworks that map out the full uncertainty in the solution rather than returning a single best-fit point.

The accuracy of earthquake locations depends critically on the quality of the velocity model and the geometry of the recording network. A dense, well-distributed network of stations surrounding the source region produces tight constraints; sparse or one-sided coverage leads to large uncertainties, especially in depth. Relative relocation techniques like the **double-difference method** achieve sub-kilometer precision by exploiting the fact that closely spaced earthquakes share nearly identical ray paths, so velocity model errors cancel out. The resulting catalogs of precisely located hypocenters reveal the three-dimensional geometry of active faults, illuminate the dipping planes of subduction zones (Wadati-Benioff zones), and identify clusters of seismicity that map stress concentrations — making earthquake location the foundation upon which most seismological interpretation is built.
