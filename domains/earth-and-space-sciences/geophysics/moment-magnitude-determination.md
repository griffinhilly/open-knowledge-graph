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
stage: expert
status: draft
---

# Seismic Moment and Moment Magnitude

## Core Idea
Seismic moment (M₀) quantifies the rigidity, area of fault that slipped, and amount of slip during an earthquake: M₀ = μAu (rigidity × area × average slip). Moment magnitude Mw = (2/3) log₁₀(M₀) − 10.7 is defined directly from earthquake physics and does not saturate at large magnitudes, making it the standard magnitude scale for modern seismology.

## Questions

```yaml
- question: "Why does the Richter magnitude scale saturate for very large earthquakes, assigning similar values to events that differ enormously in energy?"
  type: multiple-choice
  options:
    - "The Richter scale uses a linear rather than logarithmic relationship, so it compresses large values"
    - "Large earthquakes radiate most of their energy at long periods, which short-period seismometers cannot capture — so peak amplitudes plateau even as true energy grows"
    - "The Richter scale was designed only for California and its formula breaks down outside that region"
    - "Large earthquakes produce lower amplitude waves because the fault moves more slowly"
  answer: 1
  explanation: "The Richter scale measures peak amplitudes on specific short-period instruments. Large ruptures release most energy as long-period seismic waves that these instruments simply miss — their response falls off at long periods. So an M 9 earthquake can produce peak amplitudes on such instruments similar to an M 7, even though the M 9 releases roughly 1,000 times more energy. Moment magnitude avoids this by measuring the physics of the source (fault area, slip, rigidity) rather than instrument response."

- question: "Two earthquakes both rupture a 200 km² fault with 2 m average slip. Earthquake A occurs in rigid crystalline crust (high μ); Earthquake B occurs in soft sediment (low μ). Which has larger seismic moment, and why?"
  type: multiple-choice
  options:
    - "Earthquake B, because soft sediment deforms more easily and releases stored energy faster"
    - "They are equal — seismic moment depends only on fault area and slip, not rock type"
    - "Earthquake A, because M₀ = μAu and higher rigidity (μ) directly increases seismic moment for the same area and slip"
    - "Earthquake A, because rigid rock produces higher-frequency waves that seismometers record more efficiently"
  answer: 2
  explanation: "Seismic moment M₀ = μAu, so all three factors matter. With identical A and u, the earthquake in higher-rigidity (higher μ) rock has larger seismic moment. This makes physical sense: stiffer rock stores more elastic strain per unit deformation, so releasing the same amount of slip releases more energy. Option B is wrong because it ignores μ; option D confuses moment with recorded amplitude."

- question: "An earthquake with a larger fault rupture area always has a higher moment magnitude than one with a smaller rupture area."
  type: true-false
  answer: false
  explanation: "Moment magnitude derives from seismic moment M₀ = μAu. A smaller fault with very high slip (u) and high rigidity (μ) can produce greater M₀ — and thus higher Mw — than a larger fault with small slip in soft rock. All three factors multiply together. Rupture area is one component, not the sole determinant. Mw is a summary of the combined product, not any single physical parameter."

- question: "The constants in the Mw formula are chosen so that moment magnitude agrees with the Richter scale for moderate earthquakes where both scales are valid."
  type: true-false
  answer: true
  explanation: "The formula Mw = (2/3)log₁₀(M₀) − 10.7 was calibrated so that for moderate earthquakes (roughly M 4–7), Mw gives values consistent with the Richter magnitude that seismologists had been using for decades. This ensures backward compatibility — historical catalogs using ML can be compared with modern Mw values. The advantage is that for large earthquakes where ML saturates, Mw continues to scale correctly with actual source energy."

- question: "Why is seismic moment considered a more physically meaningful measure of earthquake size than peak seismic wave amplitude recorded on a seismometer?"
  type: short-answer
  answer: "Seismic moment M₀ = μAu is calculated directly from the physical properties of the fault rupture — the stiffness of the rock, the area that broke, and how far it slipped. These quantities describe what actually happened in the Earth regardless of which instruments happened to be nearby or what frequencies they recorded. Peak amplitude, by contrast, depends on the instrument's frequency response, the distance to the earthquake, and the local site conditions — none of which reflect the source's true size. For large earthquakes that radiate energy at long periods, short-period instruments underestimate the amplitude and thus the scale's value saturates. Moment magnitude, derived from M₀, has no such saturation because it measures the source, not the instrument response."
  explanation: "This is the core reason seismology adopted Mw as the standard: it is anchored to physics, not to the characteristics of a particular instrument design."
```

## Explainer

From your study of seismic moment and focal mechanisms, you know that an earthquake is fundamentally a slip event on a fault surface, and that the radiation pattern of seismic waves encodes the geometry of that slip. **Seismic moment** (M₀) takes these concepts and distills the total "size" of an earthquake into a single physical quantity: M₀ = μAu, where **μ** is the rigidity (shear modulus) of the rock surrounding the fault, **A** is the area of the fault that ruptured, and **u** is the average displacement across that area. The units are Newton-meters (N·m), the same as torque — hence the name "moment."

Each factor in the formula captures a different aspect of the earthquake. Rigidity tells you how stiff the rock is — faults in rigid crustal rock release more energy per unit slip than faults in soft sediment. Rupture area tells you how much of the fault broke — a magnitude 9 earthquake ruptures hundreds of kilometers of fault, while a magnitude 4 might rupture just a few hundred meters. Average slip tells you how far the two sides moved — centimeters for small earthquakes, tens of meters for the largest. The product of all three gives you a number that scales directly with the total energy released, without any of the measurement artifacts that plagued earlier magnitude scales.

The older **Richter magnitude** (ML) was defined from the amplitude of seismic waves on a specific instrument at a specific distance. It works well for moderate, local earthquakes, but it **saturates** for large events — an M 7 and an M 9 earthquake can produce similar peak amplitudes on short-period instruments, even though the M 9 releases roughly 1,000 times more energy. This happens because large earthquakes radiate most of their energy at long periods that short-period seismometers miss. Moment magnitude avoids this problem entirely because it is derived from the physics of the source, not the characteristics of the recording instrument.

The formula **Mw = (2/3) log₁₀(M₀) − 10.7** converts seismic moment into the familiar magnitude scale. The logarithmic relationship (inherited from Richter's original definition) means that each unit increase in Mw corresponds to a roughly 32-fold increase in energy and a 10-fold increase in wave amplitude. The constants are chosen so that Mw agrees with ML for moderate earthquakes where both scales are valid, ensuring backward compatibility. In practice, seismologists determine M₀ from long-period waveform modeling or centroid moment tensor inversion, then compute Mw from the formula. Because it is grounded in measurable fault parameters rather than instrument response, moment magnitude is now the universal standard for comparing earthquakes of all sizes.
