---
id: gnss-satellite-positioning
title: GNSS Satellite Positioning (GPS and Related Systems)
domain: earth-and-space-sciences
course: remote-sensing-and-gis
prerequisites:
- id: coordinate-systems-projections
  type: hard
- id: satellite-orbits-remote-sensing
  type: soft
- id: gis-fundamentals
  type: soft
builds-toward: []
tags:
- gnss
- gps
- positioning
- trilateration
- differential-correction
- rtk
stage: advanced
status: validated
---

# GNSS Satellite Positioning (GPS and Related Systems)

## Core Idea
A Global Navigation Satellite System (GNSS) finds a receiver's position by measuring how long radio signals take to arrive from several satellites whose positions are known. Each travel time gives a distance, and the receiver's position is the point that fits all the distances. Because the receiver's clock is much less accurate than the satellites' atomic clocks, at least four satellites are needed to solve for three position coordinates plus the clock error. GPS (United States), GLONASS (Russia), Galileo (European Union), and BeiDou (China) all work this way and supply much of the location data used in GIS.

## How It's Best Learned
Begin in two dimensions: give students distances from three known points on a map and have them draw circles to find the one point that fits. Then add the clock problem, showing how a common timing error makes all circles too large or too small and why one more satellite fixes it. Finally, compare positions logged by a phone with a survey benchmark to see real error sizes, and discuss how corrections improve them.

## Common Misconceptions
- GPS satellites track your phone. (The satellites only broadcast signals; the receiver calculates its own position and sends nothing back to them.)
- Satellite positioning uses triangulation by angles. (It uses distances from timed signals, a method called trilateration.)
- Three satellites are always enough for a 3D fix. (A fourth is needed because the receiver's clock error is an extra unknown.)
- A GNSS position is exact. (Basic positions from consumer receivers are typically good to a few meters; correction methods are needed for centimeter-level work.)

## Questions

```yaml
- question: "Why does a GNSS receiver need signals from at least four satellites to find a 3D position?"
  type: multiple-choice
  options:
    - "One satellite is needed for each of the four cardinal directions"
    - "There are four unknowns: three position coordinates and the error in the receiver's clock"
    - "Each satellite can see only one quarter of Earth"
    - "Four signals are needed to cancel out the effect of the ionosphere"
  answer: 1
  explanation: "Distances come from signal travel times, so a clock error of even a millionth of a second shifts every distance by about 300 m. The receiver's cheap clock adds a fourth unknown, which requires a fourth measurement."

- question: "Signal travel time is used to compute distance. If a timing error of 1 microsecond (10⁻⁶ s) went uncorrected, about how large would the distance error be?"
  type: short-answer
  answer: "About 300 m, because radio signals travel at about 3 × 10⁸ m/s, and 3 × 10⁸ m/s × 10⁻⁶ s = 300 m."
  explanation: "This calculation shows why GNSS satellites carry atomic clocks and why receivers must solve for their own clock error."

- question: "Differential GNSS improves accuracy by using a base station at a precisely known location to measure current errors and send corrections to nearby receivers."
  type: true-false
  answer: true
  explanation: "Many error sources, such as signal delays in the ionosphere and small orbit and clock errors, are nearly the same for receivers close to each other. A base station that knows its true position can measure these errors and broadcast corrections. Real-time kinematic (RTK) methods that also track the carrier wave can reach centimeter-level accuracy."

- question: "A surveyor's GNSS position in a narrow city street between tall buildings is much worse than in an open field. What is the most likely cause?"
  type: multiple-choice
  options:
    - "The satellites move more slowly over cities"
    - "Buildings block some satellites and reflect signals (multipath), and the remaining satellites are bunched in a poor geometry"
    - "City air is too dense for radio waves"
    - "GNSS does not work below 100 m elevation"
  answer: 1
  explanation: "Blocked signals reduce the number of usable satellites, and reflections make some signals travel a longer path. When the visible satellites are close together in the sky, small distance errors cause larger position errors; this effect is measured by dilution of precision (DOP)."
```

## Explainer
You know how coordinate systems and datums describe locations on Earth. GNSS is the main way modern devices find those coordinates in the field.

The key idea is that **time gives distance**. Each satellite carries very precise atomic clocks and broadcasts a signal that says, in effect, "I am here, and this is the time." The receiver notes when the signal arrives. Radio waves travel at about 300,000 km per second, so travel time multiplied by that speed gives the distance to the satellite. Because this distance includes the receiver's own clock error, it is called a **pseudorange**.

Picture the geometry. One distance puts you somewhere on a sphere around the satellite. A second distance narrows you to the circle where two spheres meet. A third leaves two points, and usually only one is near Earth's surface. This method is **trilateration**. There is one more problem: a phone's clock is not an atomic clock. An error of one microsecond would put every distance off by about 300 meters. So the receiver treats its clock error as a fourth unknown and solves for it using a fourth satellite. More satellites give a better solution.

The American GPS has a core constellation of at least 24 satellites in six orbital planes about 20,200 km up, each circling Earth about twice a day. GLONASS, Galileo, and BeiDou use similar designs. Modern receivers combine signals from several systems, so many satellites are usually in view. GPS positions are referenced to the WGS 84 datum. The satellite clocks must also be adjusted for the effects of relativity, or errors would build up quickly.

Several things limit accuracy. Signals slow down as they pass through the ionosphere and the lower atmosphere. They can bounce off buildings or cliffs before reaching the antenna, an effect called **multipath**. Satellites that are bunched together in the sky give poor geometry, measured by **dilution of precision**. A typical consumer receiver under open sky is accurate to a few meters.

Better accuracy comes from corrections. In **differential GNSS**, a base station at a known point measures the current errors and sends corrections to nearby receivers. **Real-time kinematic** (RTK) positioning also tracks the phase of the carrier wave and can reach centimeter accuracy. These methods make GNSS useful for surveying, mapping, precision farming, and measuring the slow motion of tectonic plates.
