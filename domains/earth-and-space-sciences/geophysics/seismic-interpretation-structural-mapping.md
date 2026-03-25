---
id: seismic-interpretation-structural-mapping
title: Seismic Interpretation and Structural Mapping
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: seismic-migration-techniques
  type: hard
- id: geologic-structures-folds-faults
  type: soft
- id: crustal-velocity-structure
  type: soft
tags:
- seismic
- interpretation
- structure
- faults
stage: expert
status: validated
---
# Seismic Interpretation and Structural Mapping

## Core Idea
Seismic interpretation converts migrated seismic images into geological models by identifying reflectors with subsurface interfaces, tracing faults and stratigraphic units, and estimating depths using velocity models. Interpreters map subsurface geology, identify structural traps for hydrocarbon accumulation, assess resource potential, and guide drilling decisions.

## Questions

```yaml
- question: "Two seismic reflectors in different parts of a survey area appear at the same two-way travel time of 2.0 seconds. Can you conclude they are at the same depth?"
  type: multiple-choice
  options:
    - "Yes — two-way travel time is directly proportional to depth, so equal time means equal depth"
    - "No — equal travel time does not imply equal depth because the seismic velocity of the overlying rock can vary laterally, converting the same time to different depths in different areas"
    - "No — but only because processing errors in migration may have shifted reflectors slightly"
    - "Yes — as long as both reflectors are in the same formation, they must be at the same depth"
  answer: 1
  explanation: "Seismic data is recorded as two-way travel time (the time for a wave to travel from surface to reflector and back), not depth. Converting time to depth requires multiplying by velocity, and seismic velocity varies both vertically (generally increasing with depth as rocks compact) and laterally (different lithologies, fluid fills, and structural settings have different velocities). Two reflectors at 2.0 seconds in a high-velocity carbonate province vs. a low-velocity shale basin could be separated by hundreds of meters in true depth. Time-to-depth conversion using a calibrated velocity model is an essential — and error-prone — step in interpretation."

- question: "An interpreter traces a bright, continuous reflector across a seismic section. What does this reflector represent physically, and what additional data is needed to identify the specific rock type?"
  type: multiple-choice
  options:
    - "A single rock formation of uniform composition; no additional data is needed because rock type determines reflectivity"
    - "An acoustic impedance contrast — a boundary where seismic velocity or density changes; a well log from a nearby borehole is needed to tie the reflector to specific rock types and depths"
    - "A fault plane cutting across the section; the continuity of the reflection proves no displacement has occurred"
    - "The water table; bright continuous reflectors always mark the transition from unsaturated to saturated rock"
  answer: 1
  explanation: "Seismic reflectors mark acoustic impedance contrasts — boundaries where the product of rock density and seismic velocity changes abruptly. A strong, bright reflector does not identify the rock type directly; a limestone-shale boundary and a gas-sand–shale boundary might produce similar-looking reflections. Identifying what a reflector corresponds to geologically requires well control: drilling a borehole, measuring the actual rock properties (lithology, porosity, fluid) at depth, and tying those measurements to the seismic waveform. This process — 'seismic-to-well tie' — is the first step in any serious horizon interpretation."

- question: "A strong, continuous seismic reflector uniquely identifies the rock type at that subsurface interface without needing additional data from boreholes."
  type: true-false
  answer: false
  explanation: "Seismic reflectivity depends on acoustic impedance contrast, not on the absolute rock type. The same reflection amplitude could result from a limestone-shale boundary, a tight sandstone-porous sandstone boundary, or a water-saturated versus gas-saturated reservoir rock. Interpreters use well logs (gamma ray, sonic, density, resistivity) to measure actual rock properties at known depths and then calibrate the seismic reflections to those measurements. Without well control, reflector identity is ambiguous and geological interpretation is speculative."

- question: "In seismic interpretation, wells drilled in the survey area are essential for correlating seismic reflectors to specific geological formations and calibrating the depth conversion."
  type: true-false
  answer: true
  explanation: "Wells provide 'ground truth' that seismic data alone cannot supply. Well logs measure physical properties (velocity, density, lithology, fluid type) at known depths, allowing interpreters to identify which reflections correspond to which geological boundaries. Synthetic seismograms — constructed from sonic and density logs — are compared to actual seismic traces to establish the seismic-to-well tie. Velocity measurements from wells also constrain the velocity model used for time-to-depth conversion. In frontier exploration without any wells, interpretation is far more uncertain and drilling risk is correspondingly higher."

- question: "Why is converting seismic two-way travel time to true depth non-trivial, and what additional information is required to perform this conversion accurately?"
  type: short-answer
  answer: "Seismic reflection data measures the time for a sound wave to travel from the surface to a reflector and return — two-way travel time (TWT). Converting TWT to depth requires knowing the seismic velocity of every rock unit above the reflector (depth = velocity × TWT / 2). This is non-trivial because velocity varies both vertically (rocks compact and velocities increase with depth) and laterally (different lithologies, structural positions, and pore fluids have different velocities). A velocity model is built using check-shot surveys or vertical seismic profiles (VSP) from wells, seismic interval velocity analysis, and geological constraints. Errors in the velocity model directly translate into depth errors — a 5% velocity error produces a 5% depth error, which could be tens to hundreds of meters for deep targets."
  explanation: "In areas with complex velocity structure — salt basins, heavily faulted terrains, or areas with significant lateral facies changes — time-to-depth conversion is one of the most challenging and consequential steps in seismic interpretation. Drilling a well 200 meters shallower than the predicted trap crest because of a poor velocity model can mean the difference between a commercial discovery and a dry hole."
```

## Explainer

From your study of seismic migration, you know how raw seismic reflection data is processed to produce an image where reflectors appear at their true subsurface positions. **Seismic interpretation** is the next step: translating that processed image into a geological model — identifying what each reflector represents, where faults cut through the section, and what the three-dimensional structure of the subsurface looks like.

A migrated seismic section displays reflections as a series of light and dark bands. Each band corresponds to an **acoustic impedance contrast** — a boundary where rock density or seismic velocity changes abruptly. The interpreter's first task is to correlate these reflections with known geology, typically by tying the seismic data to well logs from boreholes where the actual rock types and depths are known. A strong, continuous reflector at a certain depth might correspond to the top of a limestone formation; a weaker, discontinuous one might mark a sandstone-shale interface. This process of **horizon picking** — tracing a specific reflector across the seismic volume — builds a map of each geological surface.

**Fault identification** requires recognizing characteristic patterns: abrupt termination or offset of reflectors, changes in dip, and zones of chaotic or diminished reflections where the rock has been fractured. Normal faults show hanging-wall reflectors dropped down relative to the footwall. Reverse and thrust faults show repeated or stacked reflector packages. Strike-slip faults may appear as subtle lateral discontinuities that are easier to see on horizontal time slices through 3D seismic volumes. The interpreter traces each fault surface through the data, building a structural framework that divides the subsurface into discrete fault blocks.

With horizons and faults mapped, the interpreter constructs **structural maps** — contour maps of each geological surface showing its depth (or time) across the survey area. These maps reveal anticlines, synclines, fault-bounded closures, and unconformities. In hydrocarbon exploration, the primary goal is identifying **structural traps**: configurations where an impermeable seal rock overlies a porous reservoir rock in a geometry (such as a four-way dip closure or a fault-sealed compartment) that could trap migrating oil or gas. The interpreter must also convert from seismic two-way travel time to true depth using velocity models, since the same time interval can represent different thicknesses depending on the velocity of the intervening rock. The final product — an integrated structural and stratigraphic model — guides decisions about where to drill, what to expect at depth, and how much resource a prospect might contain.
