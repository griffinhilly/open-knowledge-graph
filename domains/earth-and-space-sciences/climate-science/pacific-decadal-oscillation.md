---
id: pacific-decadal-oscillation
title: Pacific Decadal Oscillation and Multi-Decadal Variability
domain: earth-and-space-sciences
course: climate-science
prerequisites:
- id: el-nino-southern-oscillation
  type: soft
- id: ocean-atmosphere-interactions
  type: soft
tags:
- pdo
- decadal
- pacific
- ocean-climate
- variability
stage: advanced
status: validated
---

# Pacific Decadal Oscillation and Multi-Decadal Variability

## Core Idea
The Pacific Decadal Oscillation (PDO) is a climate pattern in the North Pacific with a dominant timescale of 20–30 years, characterized by anomalies in sea surface temperature, sea level pressure, and atmospheric circulation. PDO phases influence global weather patterns, precipitation in North America, salmon populations, and the intensity of ENSO events. Unlike ENSO, the PDO mechanisms are not fully understood, but both atmospheric forcing and ocean memory (via ocean gyres and mid-latitude currents) play roles.

## How It's Best Learned
Compute the PDO index from North Pacific SST anomalies. Examine precipitation and temperature anomalies during positive and negative PDO phases and their impacts on regional climate.

## Common Misconceptions
The PDO is not a single mode; principal component analysis of North Pacific SST reveals multiple modes with different timescales. Also, the PDO is not entirely predictable like ENSO; stochastic forcing and chaos limit predictability.

## Questions

```yaml
- question: "During a positive PDO phase, El Niño events tend to have stronger impacts on North American weather than during a negative PDO phase. What is the best explanation?"
  type: multiple-choice
  options:
    - "Positive PDO phases generate stronger El Niño events in the tropical Pacific by enhancing the Bjerknes feedback"
    - "The positive PDO's SST anomaly pattern reinforces the tropical El Niño signal through constructive interference — both patterns favor warm coastal waters and similar atmospheric circulation shifts"
    - "Negative PDO phases suppress El Niño events entirely, so there are no El Niño impacts to measure during negative PDO"
    - "The PDO and ENSO are statistically independent, so apparent modulation reflects sampling coincidence rather than physical interaction"
  answer: 1
  explanation: "The PDO and ENSO are independent oscillations, but their spatial patterns in the Pacific can constructively or destructively interfere. During positive PDO, the coastal North American waters are already anomalously warm and the atmospheric circulation is predisposed toward the teleconnection patterns that El Niño drives. When El Niño then occurs, both signals push in the same direction, amplifying impacts on precipitation and temperature in the Pacific Northwest and beyond. During negative PDO, the background SST pattern counteracts the ENSO signal, weakening downstream impacts."

- question: "A fisheries scientist studying Pacific salmon records that Alaska's salmon yields were consistently high from 1977–1998 but then declined sharply around 1998–1999. Based on PDO dynamics, what is the most plausible climate explanation?"
  type: multiple-choice
  options:
    - "The El Niño of 1997–1998 was so strong that it permanently altered Pacific circulation patterns, reducing salmon habitat"
    - "A phase shift in the PDO from positive to negative around 1998–1999 reorganized North Pacific SST, ocean currents, and marine productivity in ways that reduced salmon productivity in Alaska"
    - "Global warming raised North Pacific temperatures monotonically throughout this period, creating a breakpoint when temperatures exceeded salmon tolerance"
    - "Overfishing peaked in 1998, and the subsequent decline in yields reflects stock collapse rather than any climate signal"
  answer: 1
  explanation: "The 'regime shifts' of 1976–77 (negative→positive PDO) and the late 1990s (positive→negative PDO) are the canonical examples of PDO's biological impact. During the positive PDO phase (1977–1998), North Pacific conditions favored Alaskan salmon. The late-1990s shift to negative PDO reversed these conditions, reorganizing the marine food web and reducing productivity. This multi-decadal variation is distinct from year-to-year ENSO variability and from secular warming trends — it's the slowly oscillating background state of the North Pacific."

- question: "The PDO is defined by a sea surface temperature anomaly pattern in which the central North Pacific is anomalously warm or cool while coastal North American waters show the opposite sign."
  type: true-false
  answer: true
  explanation: "Yes — this horseshoe/dipole pattern is the defining spatial structure of the PDO. During the positive phase, the central North Pacific is cooler than normal while a horseshoe of warm water hugs the coast from the tropics up through the Gulf of Alaska. During the negative phase, the central North Pacific warms while coastal waters cool. The PDO index is defined as the leading principal component of North Pacific SST anomalies poleward of 20°N, which captures this dipole pattern."

- question: "Like ENSO, the PDO is driven by a well-understood tropical ocean-atmosphere feedback mechanism, making multi-decadal climate prediction based on PDO nearly as reliable as seasonal ENSO forecasting."
  type: true-false
  answer: false
  explanation: "This is a key distinction. ENSO has a well-understood mechanistic basis — the Bjerknes feedback, in which wind anomalies and SST anomalies reinforce each other in the tropical Pacific — which enables skillful 6–12 month forecasts. The PDO's mechanisms are actively debated: it may reflect a superposition of ENSO teleconnections to the North Pacific, ocean gyre advection of temperature anomalies (~20-year timescales), and stochastic atmospheric forcing — possibly all three simultaneously. This mechanistic ambiguity makes PDO forecasting far less reliable than ENSO forecasting, and the PDO may not be a single coherent mode at all."

- question: "How does the PDO differ from ENSO in terms of geographic center, dominant timescale, and predictability, and why does knowing the current PDO phase matter for climate outlooks and resource management?"
  type: short-answer
  answer: "The PDO is centered in the extratropical North Pacific (poleward of 20°N), whereas ENSO is a tropical Pacific phenomenon centered near the equator. The PDO operates on 20–30 year timescales per phase; ENSO cycles every 2–7 years. ENSO is significantly more predictable because its mechanism (Bjerknes feedback) is well understood; PDO predictability is limited by mechanistic uncertainty and stochastic forcing. Knowing the PDO phase matters because it modulates ENSO's downstream impacts, shapes multi-decadal precipitation and temperature patterns in North America, and drives reorganizations in marine ecosystems — particularly Pacific salmon. Climate outlooks that account for PDO phase are more accurate than those treating each year identically, and fisheries managers use PDO phase to contextualize stock assessments and harvest decisions."
  explanation: "The PDO exemplifies a broader challenge in climate science: separating natural multi-decadal variability from long-term anthropogenic trends. A region experiencing two decades of below-average rainfall during a negative PDO phase may falsely appear to be undergoing permanent aridification. Recognizing the PDO phase helps disentangle internally-generated variability from forced climate change signals."
```

## Explainer

From your understanding of ENSO, you know that the tropical Pacific undergoes irregular oscillations between El Niño (warm eastern Pacific) and La Niña (cool eastern Pacific) on timescales of 2–7 years, with global consequences for weather and climate. The **Pacific Decadal Oscillation** (PDO) is a related but distinct pattern that operates on much longer timescales — roughly 20–30 years per phase — and is centered in the *North* Pacific rather than the tropics. Think of it as the slow background rhythm over which ENSO's faster oscillations play out.

The PDO is defined by the leading pattern (first principal component) of monthly **sea surface temperature anomalies** in the North Pacific, poleward of 20°N. During a **positive (warm) phase**, the central North Pacific is cooler than normal while a horseshoe of warm water hugs the west coast of North America and the tropical Pacific. During a **negative (cool) phase**, the pattern reverses: the central North Pacific warms while coastal waters cool. These SST anomalies are accompanied by shifts in the Aleutian Low pressure system, the jet stream position, and storm tracks. The PDO was first identified in the 1990s by fisheries scientist Steven Hare, who noticed that Pacific salmon productivity in Alaska and the Pacific Northwest alternated in multi-decadal cycles that correlated with these SST patterns.

The impacts of PDO phase are wide-ranging. During positive PDO phases, the Pacific Northwest and Alaska tend to be warmer and drier, while the southwestern United States receives more precipitation. Negative PDO phases reverse these tendencies. The PDO also modulates ENSO's effects: El Niño events during a positive PDO phase tend to produce stronger impacts on North American weather than those occurring during a negative PDO phase, because the background SST pattern reinforces the tropical signal. Marine ecosystems respond dramatically — the "regime shifts" of 1976–77 (negative to positive) and the late 1990s (positive to negative) coincided with major reorganizations of fish populations, including the collapse of some salmon stocks and the boom of others.

Unlike ENSO, which has a well-understood mechanism rooted in tropical ocean-atmosphere coupling (the Bjerknes feedback), the PDO's driving mechanisms remain debated. It may not be a single dynamical mode at all, but rather the superposition of several processes operating on different timescales: tropical ENSO variability imprinting on the North Pacific through atmospheric teleconnections, **ocean gyre circulation** slowly advecting temperature anomalies around the North Pacific (the "ocean memory" component with ~20-year timescales matching gyre transit times), and stochastic atmospheric forcing exciting the ocean's natural response timescales. This mechanistic ambiguity means the PDO is harder to predict than ENSO. Nonetheless, recognizing which PDO phase the Pacific is in provides valuable context for seasonal and decadal climate outlooks, fisheries management, and interpreting whether observed temperature trends reflect long-term climate change or natural multi-decadal variability.
