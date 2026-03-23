---
id: atlantic-multidecadal-oscillation
title: Atlantic Multidecadal Oscillation
domain: earth-and-space-sciences
course: climate-science
prerequisites:
- id: ocean-atmosphere-interactions
  type: hard
- id: el-nino-southern-oscillation
  type: soft
- id: atlantic-meridional-overturning-circulation
  type: soft
builds-toward:
- enso-mechanisms-teleconnections
- climate-models-and-projections
tags:
- ocean-oscillation
- atlantic-ocean
- decadal-variability
- climate-modes
stage: expert
status: draft
---

# Atlantic Multidecadal Oscillation

## Core Idea
The Atlantic Multidecadal Oscillation is a pattern of coherent sea surface temperature variability in the North Atlantic with a timescale of 60–80 years, related to fluctuations in the Atlantic Meridional Overturning Circulation. Warm (positive) phases are linked to increased Atlantic hurricane activity and drought in the Sahel, while cool phases enhance precipitation in North America. Its interactions with anthropogenic forcing remain uncertain.

## Questions

```yaml
- question: "North Atlantic sea surface temperatures have been above their long-term average for the past 25 years. A researcher attributes this entirely to greenhouse gas forcing. What is the most important complication for this attribution claim?"
  type: multiple-choice
  options:
    - "The North Atlantic warms faster than other oceans due to greater industrial emissions nearby"
    - "The current AMO warm phase coincides with this period, and with only ~170 years of instrumental records (~2 AMO cycles), separating internal variability from forced trends is statistically very difficult"
    - "ENSO warm phases in the Pacific systematically warm the North Atlantic on decadal timescales"
    - "Satellite SST measurements are unreliable before the 1980s, making trend analysis impossible"
  answer: 1
  explanation: "The AMO operates on 60–80 year timescales, meaning the instrumental record covers only about 2–3 complete cycles. Both the AMO and anthropogenic warming produce multi-decadal warming trends in the North Atlantic, and statistical methods cannot cleanly separate them with so few cycles. This is the central unresolved scientific debate around the AMO: how much of recent North Atlantic warming is forced (greenhouse gases, aerosols) versus internal (AMOC variability)? It matters enormously for projections — an AMO warm phase that partially reverses could temporarily offset anthropogenic warming in the region."

- question: "The leading hypothesis for what drives AMO variability is fluctuations in:"
  type: multiple-choice
  options:
    - "Solar output on multi-decadal timescales, which preferentially heats the North Atlantic basin"
    - "ENSO cycle frequency, which modulates heat transport from the tropical Pacific to the Atlantic"
    - "The Atlantic Meridional Overturning Circulation, which controls how much warm surface water is transported northward"
    - "Arctic sea ice extent, which reflects or absorbs solar radiation and cools or warms the sub-polar North Atlantic"
  answer: 2
  explanation: "The AMOC acts as a heat conveyor: stronger AMOC moves more warm surface water northward, raising North Atlantic SSTs (AMO warm phase); weaker AMOC reduces this transport, cooling SSTs (cool phase). This AMOC-AMO linkage is supported by coupled climate model experiments and paleoclimate evidence. Options A and B describe other climate phenomena on wrong timescales. Option D reverses the causal direction — sea ice extent responds to AMO phase rather than driving it."

- question: "During an AMO warm phase, Atlantic hurricane activity decreases because the warmer ocean surface creates unstable atmospheric conditions that disrupt storm formation."
  type: true-false
  answer: false
  explanation: "The opposite is true. Warm-phase AMO increases Atlantic hurricane frequency and intensity: warmer SSTs provide more energy and moisture to developing tropical storms, lowering the energy threshold for hurricane formation and intensification. AMO warm phases (e.g., mid-1990s onward) have historically coincided with active hurricane seasons. The confusion may arise from conflating the warming itself with some secondary effect — but for SSTs directly beneath storm tracks, warmer = more energetic storms."

- question: "The roughly 170-year instrumental SST record makes it difficult to definitively separate the AMO's internal variability from externally forced multi-decadal trends in North Atlantic temperatures."
  type: true-false
  answer: true
  explanation: "With an AMO period of 60–80 years, 170 years of data provides only about 2 complete cycles — far too few for robust statistical decomposition, especially when the forced trend (from greenhouse gases and time-varying aerosol emissions) also produces multi-decadal variability. This is why researchers turn to paleoclimate proxies (tree rings, corals, ice cores) extending the record back several centuries, and why the AMO's amplitude and forcing mechanism remain active research questions rather than settled science."

- question: "Explain why separating the AMO's contribution to recent North Atlantic warming from anthropogenic forcing is scientifically challenging, and what evidence supports the existence of an internal AMO oscillation independent of external forcing."
  type: short-answer
  answer: "The challenge is statistical: both the AMO and greenhouse forcing produce warming trends on similar (multi-decadal) timescales, and the instrumental record is only ~170 years — about 2 AMO cycles. This is too short to reliably separate internal variability from a forced trend using observational data alone. Supporting evidence for an internal oscillation includes: (1) paleoclimate proxies (corals, tree rings, ice cores) showing quasi-periodic Atlantic SST variability over centuries before industrial forcing; (2) climate model 'control runs' (no external forcing) that still produce AMO-like variability driven by AMOC fluctuations; (3) the physical mechanism linking AMOC strength to North Atlantic heat transport."
  explanation: "The policy stakes are high. If recent North Atlantic warming is partly a natural AMO warm phase, models project some reversal in coming decades — partially offsetting greenhouse warming in the region, affecting hurricane predictions, European summer temperatures, and Sahel rainfall. If the AMO is instead mainly a response to aerosol forcing that has diminished, no such reversal would occur. Current consensus leans toward a real internal oscillation but disagrees on its amplitude relative to forced variability."
```

## Explainer

From your study of ocean-atmosphere interactions, you know that the ocean and atmosphere are coupled systems — heat, moisture, and momentum transfer between them drives weather patterns and modulates climate on timescales far longer than individual storms. You are also familiar with ENSO as an example of a climate oscillation driven by ocean-atmosphere feedbacks in the tropical Pacific. The **Atlantic Multidecadal Oscillation** (AMO) is an analogous but much slower pattern in the North Atlantic, operating on timescales of 60–80 years rather than ENSO's 2–7 year cycles.

The AMO manifests as basin-wide swings in North Atlantic **sea surface temperatures** (SSTs) that alternate between warm (positive) and cool (negative) phases over several decades. Instrumental records going back to the 1850s show the pattern clearly: warm phases in roughly 1930–1960 and again from the mid-1990s onward, with a cool phase in between (~1960–1990). The temperature anomalies are modest — only about 0.2–0.4°C above or below the long-term mean — but because they persist for decades and span the entire basin, their cumulative effects on climate are substantial. The leading hypothesis for what drives these oscillations is variability in the **Atlantic Meridional Overturning Circulation** (AMOC), the large-scale conveyor of warm surface water northward and cold deep water southward. When the AMOC strengthens, it transports more heat into the North Atlantic, warming SSTs; when it weakens, the North Atlantic cools.

The climate impacts of the AMO extend far beyond the Atlantic itself. During **warm phases**, the warmer ocean surface provides more energy and moisture to the atmosphere, fueling increased Atlantic hurricane activity — both in frequency and intensity. The warm phase also shifts tropical rainfall belts northward, bringing wetter conditions to the Sahel region of Africa (reducing drought risk) while simultaneously suppressing rainfall over parts of the American Midwest and Southwest. During **cool phases**, these patterns reverse: fewer hurricanes, more Sahel drought, and enhanced precipitation over North America. The AMO has also been linked to summer climate variability in Europe and to modulation of Arctic sea ice extent.

One of the most important and unresolved questions in climate science is how to disentangle the AMO from **anthropogenic warming**. Both produce multi-decadal trends in North Atlantic SSTs, and the observational record is only about 170 years long — barely two full AMO cycles. Some researchers argue that what we call the AMO may partly reflect the ocean's response to time-varying aerosol emissions and greenhouse gas forcing rather than a purely internal oscillation. This matters enormously for climate projections: if some portion of recent North Atlantic warming is due to a natural AMO warm phase, it could temporarily reverse, partially offsetting greenhouse warming in the Atlantic for a few decades. If the AMO is instead largely forced by external factors, such a reversal would not occur. Paleoclimate proxies — tree rings, corals, ice cores — extend the record back several centuries and do show quasi-periodic Atlantic variability, supporting the existence of an internal oscillation, but the debate over its relative importance compared to forced trends remains active.
