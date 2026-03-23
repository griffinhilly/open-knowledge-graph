---
id: earths-magnetic-dipole-field-basics
title: Earth's Magnetic Dipole Field Basics
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: earth-interior-structure
  type: soft
builds-toward:
- paleomagnetism-and-reversals
- geomagnetic-dynamo-theory
- magnetotelluric-methods-em-induction
tags:
- geomagnetism
- dipole-field
- magnetic-field
- core
stage: expert
status: validated
---

# Earth's Magnetic Dipole Field Basics

## Core Idea
Earth's magnetic field is generated primarily by convection of liquid iron in the outer core (geodynamo) and approximated as a dipole field tilted about 11° from the rotation axis. The field strength at the surface is ~25–65 microteslas and varies spatially and temporally. Secular variation (long-period changes) occurs on timescales of years to centuries; paleomagnetic reversals occur on timescales of thousands to millions of years.

## Questions

```yaml
- question: "A geologist measures the inclination (dip angle) of Earth's magnetic field at a surface location and finds it is nearly horizontal — approximately 5°. Where is she most likely located?"
  type: multiple-choice
  options:
    - "Near a magnetic pole, where field lines are nearly vertical"
    - "Near the magnetic equator, where field lines are parallel to the surface"
    - "In the northern hemisphere at mid-latitudes, where inclination is typically 45–70°"
    - "At an anomalous location where non-dipole components dominate"
  answer: 1
  explanation: "The dipole model predicts that field line inclination varies systematically with magnetic latitude: at the magnetic poles, inclination is ±90° (field lines point straight down or up); at the magnetic equator, inclination is 0° (field lines are horizontal). A nearly horizontal field (inclination ≈ 5°) indicates a location near the magnetic equator. This relationship is captured by the equation tan(I) = 2 tan(λ), where I is inclination and λ is magnetic latitude — the same relationship used in paleomagnetism to reconstruct ancient plate positions."

- question: "Earth's magnetic dipole model accounts for roughly 90% of the observed surface field. What does the remaining ~10% represent, and what does it tell us?"
  type: multiple-choice
  options:
    - "The angular offset between the geographic and magnetic poles, which accounts for the declination at every surface location"
    - "Higher-order terms — quadrupole, octupole, and further — that describe regional departures from the simple dipole and change over time through secular variation"
    - "The contribution of crustal rocks to the total field, which is fixed and does not vary temporally"
    - "Interference from the solar wind, which distorts the perfect dipole pattern near the surface"
  answer: 1
  explanation: "The real field is more complex than a pure dipole. Spherical harmonic analysis decomposes the field into its components: the dipole (degree 1) dominates, but quadrupole, octupole, and higher-degree terms account for regional anomalies. These non-dipole features drift and change over decades to centuries — a phenomenon called secular variation — reflecting shifting convection patterns in the outer core. Navigators have tracked declination changes for centuries because these regional non-dipole features cause magnetic north to wander noticeably over human timescales."

- question: "Because Earth's magnetic dipole axis is tilted about 11° from the geographic rotation axis, magnetic declination (the angle between true north and magnetic north) varies depending on where you are on Earth's surface."
  type: true-false
  answer: true
  explanation: "The tilt of the magnetic dipole means that magnetic north and geographic north only coincide along a line (the agonic line) where both poles happen to be on the same meridian. At all other locations, a compass needle points toward magnetic north, which is offset from true north by the declination angle. Declination ranges from near zero in some regions to 20° or more in others, and it changes slowly over time due to secular variation. Accurate navigation requires knowing and correcting for the local declination."

- question: "Earth's magnetic field polarity has been stable throughout geologic history, with the north magnetic pole always located near the geographic north pole."
  type: true-false
  answer: false
  explanation: "Paleomagnetic evidence shows that Earth's field has reversed polarity hundreds of times throughout geologic history — the north and south magnetic poles swap. These reversals happen at irregular intervals averaging roughly every 200,000–300,000 years, though some stable polarity intervals (chrons) have lasted tens of millions of years. The record of reversals is preserved in magnetized rocks and is the basis for magnetostratigraphy. We are currently in the Brunhes Normal Chron (polarity like today), which began about 780,000 years ago."

- question: "Earth's interior is too hot for a permanent bar magnet to maintain Earth's magnetic field. Explain what actually generates the field and why a solid permanent magnet deep in the Earth is impossible."
  type: short-answer
  answer: "Earth's field is generated by the geodynamo: convecting electrically conducting liquid iron in the outer core produces electric currents, which generate a magnetic field that in turn organizes the fluid flow — a self-sustaining feedback loop. A permanent bar magnet is impossible because Earth's deep interior temperature far exceeds the Curie temperature of iron (~770°C for iron, but the outer core is ~3,000–5,000°C). Above the Curie temperature, thermal agitation destroys the magnetic ordering of atomic magnetic moments, making permanent magnetism impossible regardless of the material."
  explanation: "This is a fundamental misconception worth correcting. The geodynamo requires the outer core to be liquid (for convection) and electrically conducting (to carry currents). The inner core is solid iron but does not maintain permanent magnetism for the same reason — it is also above the Curie temperature. The field is dynamic and self-generated, which is why it can undergo secular variation and polarity reversals that a permanent magnet could never produce."
```

## Explainer

You already know that Earth's interior is layered, with a solid inner core surrounded by a liquid outer core of iron-nickel alloy. It is this liquid outer core that generates Earth's magnetic field through a process called the **geodynamo**. Convective motions of electrically conducting liquid iron, driven by heat loss from the core and the crystallization of the inner core, create electric currents. Those currents, in turn, produce a magnetic field — and the field feeds back to organize the fluid flow, sustaining itself in a self-reinforcing loop. The result is a planetary-scale magnetic field that extends far into space and shields the surface from solar wind particles.

To a first approximation, Earth's magnetic field resembles the field of a **magnetic dipole** — essentially a giant bar magnet — positioned at the planet's center and tilted about 11° from the geographic rotation axis. This tilt is why magnetic north and geographic north do not coincide, producing a **declination** (the angle between true north and magnetic north) that varies by location. The dipole model also predicts how the field varies with latitude: at the magnetic poles, field lines are vertical and the field strength is strongest (~60–65 microteslas); at the magnetic equator, field lines are horizontal and the field is weakest (~25–30 microteslas). The angle that the field makes with the horizontal surface is called the **inclination**, and it varies systematically from 0° at the equator to ±90° at the poles. This latitude dependence is captured by the dipole equation tan(I) = 2 tan(λ), where I is inclination and λ is magnetic latitude — a relationship that becomes critical in paleomagnetism.

The dipole model captures about 90% of the observed field, but the real field is more complex. **Non-dipole components** — quadrupole, octupole, and higher-order terms described by spherical harmonic analysis — account for regional departures from the simple dipole pattern. These non-dipole features change over time in a phenomenon called **secular variation**: the field strength at any location drifts, declination angles wander, and patches of anomalous field migrate across the core-mantle boundary. Secular variation occurs on timescales of years to centuries and reflects changes in the pattern of convection in the outer core. Navigators have tracked declination changes for centuries, and repeat surveys of magnetic observatories document how the field evolves.

On much longer timescales — thousands to millions of years — the field undergoes **polarity reversals**, episodes during which the north and south magnetic poles swap. During a reversal, the dipole field weakens, the non-dipole components temporarily dominate, and the field eventually re-establishes with opposite polarity. Reversals happen at irregular intervals averaging roughly every 200,000 to 300,000 years, though some stable polarity intervals (called chrons) have lasted tens of millions of years. The record of these reversals, preserved in volcanic rocks and seafloor sediments, provides the foundation for magnetostratigraphy and was one of the key pieces of evidence confirming seafloor spreading and plate tectonics.
