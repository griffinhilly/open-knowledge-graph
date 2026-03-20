---
id: seismic-hazard-assessment
title: 'Seismic Hazard Assessment: Earthquake Probability and Risk'
domain: earth-and-space-sciences
course: geology
prerequisites:
- id: fault-mechanics-rupture
  type: hard
- id: earthquakes-and-seismology
  type: soft
tags:
- seismic-hazard
- earthquakes
- probability
- risk
stage: advanced
status: draft
---

# Seismic Hazard Assessment: Earthquake Probability and Risk

## Core Idea
Earthquake hazard combines fault geometry, slip rate, recurrence interval, and ground motion predictions. Paleoseismic records (offset features, trenched deposits) reveal previous earthquakes and magnitudes over millennia. Hazard maps show probabilistic earthquake occurrence and expected ground shaking intensity for earthquake planning and building design.

## How It's Best Learned
Analyze paleoseismic data to construct magnitude-frequency relationships. Calculate hazard curves for a specific site.

## Common Misconceptions
- Large earthquakes are unpredictable in time and space.
- Seismic hazard is uniform across a region.
- Historical earthquakes always repeat at regular intervals.

## Explainer

From your study of fault mechanics and rupture, you know that earthquakes occur when accumulated stress on a fault exceeds the frictional strength holding it locked, causing sudden slip. **Seismic hazard assessment** takes this physical understanding and asks the practical question: for a given location, what is the probability of experiencing a certain level of ground shaking over a specified time period? The answer combines geology, seismology, and probability theory into a framework that directly informs building codes, land-use planning, and insurance.

The assessment begins with identifying and characterizing the **seismic sources** — the faults capable of producing damaging earthquakes near the site of interest. For each fault, geologists need to know its geometry (length, dip, depth extent), its **slip rate** (how fast the two sides are moving relative to each other, typically millimeters to centimeters per year), and its **recurrence interval** (how often it produces large earthquakes). Slip rate comes from geodetic measurements, offset geological features, and paleoseismic investigations. Recurrence interval is estimated from **paleoseismology**: trenching across faults to expose and date layers disrupted by past earthquakes. By identifying the stratigraphic horizons offset by each event and dating the sediments above and below, geologists can reconstruct earthquake histories spanning thousands of years — far longer than the instrumental record, which only extends back about a century.

With source characterization complete, the next step is **ground motion prediction**. A magnitude 7 earthquake on a fault 10 km away will shake your site very differently from a magnitude 6 earthquake on a fault 100 km away. **Ground motion prediction equations** (GMPEs) — empirical relationships derived from thousands of recorded earthquakes — estimate the expected shaking intensity (usually expressed as peak ground acceleration or spectral acceleration) as a function of earthquake magnitude, distance, fault type, and local site conditions. Soft sediments amplify shaking relative to bedrock, which is why Mexico City (built on an ancient lakebed) experienced catastrophic damage in 1985 from an earthquake whose epicenter was 350 km away.

The final product is a **probabilistic seismic hazard analysis (PSHA)**, which integrates over all possible earthquake scenarios — every fault that could rupture, at every possible magnitude, with every possible distance — weighted by their probability of occurrence. The output is a hazard curve or hazard map showing, for example, the ground acceleration that has a 2% probability of being exceeded in 50 years. This is the number that building codes use: structures are designed to withstand that level of shaking without collapse. The maps are not static predictions — they are continually updated as new faults are discovered, paleoseismic records are extended, and ground motion models are refined. Regions once considered low-hazard (like parts of the central United States near the New Madrid seismic zone) have been reclassified as new paleoseismic evidence revealed large prehistoric earthquakes.
