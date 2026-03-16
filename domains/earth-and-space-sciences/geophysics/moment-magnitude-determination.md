---
id: moment-magnitude-determination
title: Seismic Moment and Moment Magnitude
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: seismic-moment-and-magnitude
  type: hard
- id: focal-mechanisms-and-stress-tensors
  type: hard
- id: logarithms-intro
  type: soft
builds-toward:
- earthquake-magnitude-frequency-gutenberg-richter
tags:
- seismic
- moment
- magnitude
- earthquake
stage: advanced
status: draft
---

# Seismic Moment and Moment Magnitude

## Core Idea
Seismic moment (M₀) quantifies the rigidity, area of fault that slipped, and amount of slip during an earthquake: M₀ = μAu (rigidity × area × average slip). Moment magnitude Mw = (2/3) log₁₀(M₀) − 10.7 is defined directly from earthquake physics and does not saturate at large magnitudes, making it the standard magnitude scale for modern seismology.

## Explainer

From your study of seismic moment and focal mechanisms, you know that an earthquake is fundamentally a slip event on a fault surface, and that the radiation pattern of seismic waves encodes the geometry of that slip. **Seismic moment** (M₀) takes these concepts and distills the total "size" of an earthquake into a single physical quantity: M₀ = μAu, where **μ** is the rigidity (shear modulus) of the rock surrounding the fault, **A** is the area of the fault that ruptured, and **u** is the average displacement across that area. The units are Newton-meters (N·m), the same as torque — hence the name "moment."

Each factor in the formula captures a different aspect of the earthquake. Rigidity tells you how stiff the rock is — faults in rigid crustal rock release more energy per unit slip than faults in soft sediment. Rupture area tells you how much of the fault broke — a magnitude 9 earthquake ruptures hundreds of kilometers of fault, while a magnitude 4 might rupture just a few hundred meters. Average slip tells you how far the two sides moved — centimeters for small earthquakes, tens of meters for the largest. The product of all three gives you a number that scales directly with the total energy released, without any of the measurement artifacts that plagued earlier magnitude scales.

The older **Richter magnitude** (ML) was defined from the amplitude of seismic waves on a specific instrument at a specific distance. It works well for moderate, local earthquakes, but it **saturates** for large events — an M 7 and an M 9 earthquake can produce similar peak amplitudes on short-period instruments, even though the M 9 releases roughly 1,000 times more energy. This happens because large earthquakes radiate most of their energy at long periods that short-period seismometers miss. Moment magnitude avoids this problem entirely because it is derived from the physics of the source, not the characteristics of the recording instrument.

The formula **Mw = (2/3) log₁₀(M₀) − 10.7** converts seismic moment into the familiar magnitude scale. The logarithmic relationship (inherited from Richter's original definition) means that each unit increase in Mw corresponds to a roughly 32-fold increase in energy and a 10-fold increase in wave amplitude. The constants are chosen so that Mw agrees with ML for moderate earthquakes where both scales are valid, ensuring backward compatibility. In practice, seismologists determine M₀ from long-period waveform modeling or centroid moment tensor inversion, then compute Mw from the formula. Because it is grounded in measurable fault parameters rather than instrument response, moment magnitude is now the universal standard for comparing earthquakes of all sizes.
