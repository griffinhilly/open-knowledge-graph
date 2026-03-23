---
id: geomagnetic-field-secular-variation
title: Geomagnetic Secular Variation and Long-Term Changes
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: geomagnetic-dynamo-theory
  type: hard
- id: earths-magnetic-dipole-field-basics
  type: hard
tags:
- geomagnetic
- secular-variation
- long-term
stage: expert
status: draft
---

# Geomagnetic Secular Variation and Long-Term Changes

## Core Idea
Earth's magnetic field changes over years to centuries (secular variation) due to core fluid dynamics. The dipole tilts and moves, non-dipole anomalies grow and decay, and westward drift persists—all tracked by global observatory networks and satellite missions.

## Questions

```yaml
- question: "Earth's magnetic dipole has weakened by about 10% over the last 150 years. What can geophysicists most accurately conclude from this observation?"
  type: multiple-choice
  options:
    - "A geomagnetic polarity reversal is likely within the next few centuries, based on the current rate of weakening"
    - "The geomagnetic dynamo is failing; the outer core is cooling and convection is slowing"
    - "The current weakening is within the range of natural fluctuations seen in the paleomagnetic record and does not reliably indicate an imminent reversal"
    - "Solar activity is interfering with the outer core's convection and weakening the field"
  answer: 2
  explanation: "The paleomagnetic record — preserved in volcanic rocks and sediments — shows that the dipole field has fluctuated significantly in intensity many times without reversing. The current dipole strength is still above the long-term average, and similar periods of weakening have occurred and recovered repeatedly. Reversals are associated with prolonged excursions to very low dipole intensity, not brief 10% changes. Attributing the weakening to solar activity or outer-core cooling conflates the driving physics (turbulent fluid dynamics) with external processes. The correct interpretation is: monitor carefully, but don't conclude a reversal is imminent from 150 years of data."

- question: "What is the physical cause of the westward drift of non-dipole geomagnetic features?"
  type: multiple-choice
  options:
    - "The solid inner core rotates faster than the mantle, dragging field lines westward relative to the surface"
    - "The outer core fluid near the core-mantle boundary rotates slightly slower than the overlying mantle, so field features rooted in the core appear to drift westward relative to surface observers"
    - "The solar wind applies a steady westward torque to Earth's magnetic field lines"
    - "Thermal convection plumes in the outer core preferentially rise on the east side, pushing features westward"
  answer: 1
  explanation: "Westward drift reflects a differential rotation between the core and the mantle. The outer core fluid near the core-mantle boundary rotates at a slightly lower angular velocity than the overlying mantle. Since magnetic field structures are anchored in the core fluid, they appear to move westward when observed from the surface (which rotates with the mantle). This was one of the earliest recognized regularities in secular variation — documented by comparing compass declination measurements across centuries of maritime navigation — and remains an important constraint on models of outer-core flow."

- question: "The migration of the north magnetic pole toward Siberia reflects changes in large-scale flow patterns in the outer core beneath the polar regions."
  type: true-false
  answer: true
  explanation: "The magnetic poles are not fixed geographic points — they are the surface locations where field lines are vertical (inclination = 90°), and they move as the dominant flow structures in the outer core shift. The north magnetic pole's acceleration from ~10 km/year to ~50 km/year over the past few decades corresponds to changes in a patch of intense magnetic flux beneath the Arctic — likely related to a jet-like flow structure in the outer core. Geophysicists use pole migration patterns as a window into the large-scale fluid dynamics 2,900 km below the surface."

- question: "Earth's magnetic poles remain essentially fixed over human timescales; the apparent westward drift of field features is an artifact of measurement errors in global observatory networks."
  type: true-false
  answer: false
  explanation: "Secular variation — including pole migration and westward drift — is real, well-documented, and physically significant. The International Geomagnetic Reference Field (IGRF) is updated every five years specifically because the field changes enough to require correction for navigators, surveyors, and geophysicists. Historical shipping records going back centuries document changing compass declination at fixed locations, long before modern observatory networks existed. The north magnetic pole has moved from the Canadian Arctic toward Siberia by hundreds of kilometers over the 20th century alone."

- question: "What is westward drift, what physical mechanism causes it, and why is it significant evidence about outer core dynamics?"
  type: short-answer
  answer: "Westward drift is the systematic westward migration of non-dipole magnetic field features at roughly 0.2° per year, observed over centuries of declination measurements. It is caused by the outer core fluid near the core-mantle boundary rotating slightly slower than the mantle, so field structures anchored in the core appear to drift westward relative to the surface. It is significant because it constrains the differential rotation between the core and mantle — one of the few direct observational handles on fluid motion deep in the Earth."
  explanation: "The fact that westward drift is systematic (not random) implies large-scale coherent flow in the outer core, not purely turbulent chaos. Its rate and spatial pattern are used to test and constrain numerical dynamo models. The persistence of westward drift across centuries also shows that core-mantle coupling (the mechanical and electromagnetic interaction between the core and mantle) is not strong enough to synchronize their rotation rates — the core is partially decoupled from the mantle above it."
```

## Explainer

From your study of the geomagnetic dynamo, you know that Earth's magnetic field is generated by convective motion of liquid iron in the outer core — a self-sustaining electromagnetic process driven by heat loss and compositional buoyancy. From Earth's magnetic dipole basics, you know the field is roughly dipolar, with field lines emerging near the south geographic pole and re-entering near the north. **Secular variation** is what happens when you watch this field over human timescales: it does not sit still. The dipole wobbles, non-dipole features drift, and the total field strength fluctuates — all because the fluid flow in the core is turbulent and constantly evolving.

The most obvious secular change is the movement of the **magnetic poles**. The north magnetic pole has migrated from the Canadian Arctic toward Siberia over the past century, recently accelerating to roughly 50 km per year. This drift reflects changes in the large-scale flow pattern in the outer core beneath the polar regions. The dipole itself is also weakening: its strength has declined about 10% over the last 150 years. While this has prompted speculation about an impending polarity reversal, the current intensity is still well above the long-term average, and similar fluctuations appear routinely in the paleomagnetic record without leading to reversals.

Beyond the dipole, the field contains **non-dipole anomalies** — regional features where the field departs significantly from what a simple bar magnet would produce. These anomalies have their own secular variation: some grow, others decay, and many drift systematically westward at about 0.2° per year. This **westward drift** was one of the earliest recognized features of secular variation, documented by comparing declination measurements across centuries of maritime navigation. The physical explanation is that the outer core fluid near the core-mantle boundary rotates slightly slower than the mantle above it, so field features rooted in the core appear to migrate westward relative to surface observers.

Monitoring secular variation requires continuous, high-precision measurements from **geomagnetic observatories** (ground stations measuring declination, inclination, and intensity) and satellite missions like the European Space Agency's Swarm constellation. These data are compiled into global field models — the International Geomagnetic Reference Field (IGRF) is updated every five years and includes predictive secular variation coefficients that allow navigators, surveyors, and geophysicists to correct for field changes between updates. For geophysicists, secular variation is a window into core dynamics: the pattern and rate of field changes constrain models of core flow, providing one of the only direct observational handles on processes occurring 2,900 km beneath our feet.
