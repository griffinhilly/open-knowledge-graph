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
stage: formal-systems
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

## Questions

```yaml
- question: "Two cities sit at the same distance from the same fault. City A is built on thick soft sediments; City B is on bedrock. For the same earthquake, which city is likely to experience more intense shaking?"
  type: multiple-choice
  options:
    - "City B on bedrock, because bedrock transmits seismic waves more efficiently with less energy loss"
    - "Both cities experience identical shaking — ground acceleration depends only on earthquake magnitude and distance"
    - "City A on soft sediments, because soft sediments amplify seismic waves, increasing shaking intensity and duration"
    - "It depends entirely on whether the earthquake rupture propagates toward or away from each city"
  answer: 2
  explanation: "Soft sediments amplify seismic waves significantly — this is called site amplification. When seismic waves travel from hard bedrock into soft, water-saturated sediments, they slow down, and their amplitude increases to conserve energy. The 1985 Mexico City earthquake demonstrated this dramatically: the city, built on ancient lake sediments, experienced catastrophic damage from an earthquake 350 km away whose epicenter was in bedrock terrain. Site conditions are a critical component of seismic hazard assessment and are incorporated into ground motion prediction equations."

- question: "A seismic hazard map shows a 2% probability of exceeding a given ground acceleration in 50 years at a location. What does this mean?"
  type: multiple-choice
  options:
    - "There will be exactly two earthquakes in the next 50 years, and each has a 1% chance of producing that acceleration"
    - "There is a 98% chance no earthquake will occur in the region over the next 50 years"
    - "The specified acceleration level has a 2% probability of being exceeded at some point within a 50-year period — the standard design threshold for buildings"
    - "Scientists are 98% confident the fault will not rupture in the next 50 years"
  answer: 2
  explanation: "Probabilistic seismic hazard analysis (PSHA) produces exceedance probabilities — the chance that shaking will exceed a specified level within a time window. A 2% probability of exceedance in 50 years corresponds to a return period of approximately 2,475 years and is the standard threshold used in building codes for Life Safety design. It does not mean 'two earthquakes' or 'the fault won't rupture'; multiple faults contribute to the hazard, and even a 2% probability means the event is expected to occur roughly once every ~2,475 years on average."

- question: "Because large earthquakes are fundamentally random and unpredictable, seismic hazard assessment cannot assign meaningful probabilities to ground shaking at a specific location."
  type: true-false
  answer: false
  explanation: "While the exact timing of individual earthquakes cannot be predicted, the long-term rates and magnitudes of earthquakes on specific faults can be estimated from fault slip rates, recurrence intervals, and paleoseismic data. PSHA integrates these probabilistic estimates with ground motion models to produce hazard curves — quantitative probabilities of exceeding specified shaking levels. This probabilistic approach is precisely how building codes and land-use planning are informed by seismic science. Unpredictability of specific events does not preclude meaningful probabilistic risk assessment."

- question: "Paleoseismology — trenching fault zones and dating disrupted sediment layers — can reveal earthquake histories spanning thousands of years, far beyond the ~100-year instrumental seismograph record."
  type: true-false
  answer: true
  explanation: "Instrumental seismographs have existed only since the late 19th century, giving us roughly 100–150 years of earthquake records. Many faults have recurrence intervals of hundreds to thousands of years, meaning the instrumental record may contain only a handful — or zero — large ruptures on any given fault. Paleoseismology extends this record by identifying and dating sediment layers that were disrupted, offset, or folded by prehistoric earthquakes. Radiocarbon dating of organic material above and below event horizons can place earthquake ages to within decades to centuries, providing recurrence interval estimates essential for PSHA."

- question: "Why is probabilistic seismic hazard analysis (PSHA) more useful for engineering design than simply identifying which active faults exist near a site?"
  type: short-answer
  answer: "Identifying faults tells you earthquakes are possible, but not how often they occur, how large they might be, or what shaking intensity would result at a specific site. PSHA integrates all of this quantitatively: it accounts for every nearby fault, the rate at which each produces earthquakes of various magnitudes (from slip rates and recurrence intervals), the attenuation of shaking with distance (using ground motion prediction equations), and local site amplification effects. The result is a probabilistic hazard curve giving a specific ground acceleration with a specified exceedance probability over a given time period — a single number that engineers can use directly for structural design. This integrated, probabilistic output is what building codes require."
  explanation: "A pure fault inventory would only tell an engineer 'this region has active faults nearby' — useless for specifying how strong to build a structure. PSHA converts that qualitative awareness into quantitative design loads, accounting for the fact that some faults are closer, faster-slipping, and capable of larger earthquakes than others, and that ground shaking depends heavily on local geology at the specific site."
```

## Explainer

From your study of fault mechanics and rupture, you know that earthquakes occur when accumulated stress on a fault exceeds the frictional strength holding it locked, causing sudden slip. **Seismic hazard assessment** takes this physical understanding and asks the practical question: for a given location, what is the probability of experiencing a certain level of ground shaking over a specified time period? The answer combines geology, seismology, and probability theory into a framework that directly informs building codes, land-use planning, and insurance.

The assessment begins with identifying and characterizing the **seismic sources** — the faults capable of producing damaging earthquakes near the site of interest. For each fault, geologists need to know its geometry (length, dip, depth extent), its **slip rate** (how fast the two sides are moving relative to each other, typically millimeters to centimeters per year), and its **recurrence interval** (how often it produces large earthquakes). Slip rate comes from geodetic measurements, offset geological features, and paleoseismic investigations. Recurrence interval is estimated from **paleoseismology**: trenching across faults to expose and date layers disrupted by past earthquakes. By identifying the stratigraphic horizons offset by each event and dating the sediments above and below, geologists can reconstruct earthquake histories spanning thousands of years — far longer than the instrumental record, which only extends back about a century.

With source characterization complete, the next step is **ground motion prediction**. A magnitude 7 earthquake on a fault 10 km away will shake your site very differently from a magnitude 6 earthquake on a fault 100 km away. **Ground motion prediction equations** (GMPEs) — empirical relationships derived from thousands of recorded earthquakes — estimate the expected shaking intensity (usually expressed as peak ground acceleration or spectral acceleration) as a function of earthquake magnitude, distance, fault type, and local site conditions. Soft sediments amplify shaking relative to bedrock, which is why Mexico City (built on an ancient lakebed) experienced catastrophic damage in 1985 from an earthquake whose epicenter was 350 km away.

The final product is a **probabilistic seismic hazard analysis (PSHA)**, which integrates over all possible earthquake scenarios — every fault that could rupture, at every possible magnitude, with every possible distance — weighted by their probability of occurrence. The output is a hazard curve or hazard map showing, for example, the ground acceleration that has a 2% probability of being exceeded in 50 years. This is the number that building codes use: structures are designed to withstand that level of shaking without collapse. The maps are not static predictions — they are continually updated as new faults are discovered, paleoseismic records are extended, and ground motion models are refined. Regions once considered low-hazard (like parts of the central United States near the New Madrid seismic zone) have been reclassified as new paleoseismic evidence revealed large prehistoric earthquakes.
