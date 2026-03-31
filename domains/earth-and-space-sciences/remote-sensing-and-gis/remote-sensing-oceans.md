---
id: remote-sensing-oceans
title: Remote Sensing of Oceans
domain: earth-and-space-sciences
course: remote-sensing-and-gis
prerequisites:
- id: electromagnetic-spectrum-remote-sensing
  type: hard
- id: thermal-remote-sensing
  type: soft
- id: radar-remote-sensing-sar
  type: soft
builds-toward: []
tags:
- ocean-remote-sensing
- ocean-color
- sea-surface-temperature
- altimetry
stage: advanced
status: validated
---

# Remote Sensing of Oceans

## Core Idea
Ocean remote sensing measures sea surface temperature (SST) from thermal infrared and microwave sensors, ocean color (chlorophyll, sediment, dissolved matter) from visible-band spectrometers, sea surface height from radar altimeters, surface winds and waves from scatterometers and SAR, and sea ice extent from passive microwave and SAR. Because oceans cover 71% of Earth's surface and are largely inaccessible to in-situ measurement, satellite remote sensing provides the only practical means of systematic global ocean observation. These measurements drive ocean circulation models, fisheries management, climate research, and maritime operations.

## Questions

```yaml
- question: "Satellite ocean color sensors measure chlorophyll-a concentration in surface waters. Why is this measurement significant for understanding ocean productivity?"
  type: multiple-choice
  options:
    - "Chlorophyll-a is a pollutant that indicates water quality degradation"
    - "Chlorophyll-a is the primary photosynthetic pigment in phytoplankton, so its concentration is a proxy for phytoplankton biomass and primary productivity -- the base of the marine food web"
    - "Chlorophyll-a concentration directly measures fish populations"
    - "Chlorophyll-a indicates water temperature more accurately than thermal sensors"
  answer: 1
  explanation: "Phytoplankton are responsible for roughly half of global photosynthesis. Chlorophyll-a, detected through its absorption of blue and red light and reflectance of green, serves as a quantitative proxy for phytoplankton abundance. Mapping chlorophyll from space reveals bloom dynamics, upwelling zones, nutrient transport, and the ocean's biological response to climate variability."

- question: "Radar altimeters measure sea surface height by timing radar pulses reflected from the ocean surface. This measurement is only useful for studying tides."
  type: true-false
  answer: false
  explanation: "Sea surface height variations encode a wealth of information beyond tides: ocean currents (geostrophic flow is proportional to the surface height gradient), mesoscale eddies, El Nino/La Nina events, global sea level rise (measured at ~3.3 mm/year by satellite altimetry since 1993), and even marine gravity anomalies that reveal seafloor topography. Altimetry has been transformative for physical oceanography."

- question: "Explain why microwave sensors are used for global SST measurement in addition to infrared sensors, given that infrared has better spatial resolution."
  type: short-answer
  answer: "Infrared SST measurements are blocked by clouds, and much of the ocean is persistently cloudy (particularly high latitudes and tropical convergence zones). Passive microwave sensors (like AMSR-E) operate at wavelengths that penetrate clouds, providing all-weather SST coverage, though at coarser spatial resolution (~25 km vs ~1 km for infrared). Blended SST products combine infrared data (high resolution where clear) with microwave data (filling cloud gaps) to produce complete daily global SST maps."
  explanation: "Infrared gives sharp detail where skies are clear; microwave gives continuous coverage through clouds. The complementarity is essential for complete ocean monitoring."
```

## Explainer

The ocean is the most under-observed part of the Earth system. Ship-based measurements sample only a tiny fraction of the ocean at any time, and even the Argo float network (4,000 autonomous profilers) samples just the upper 2,000 meters. Satellite remote sensing fills this gap by observing the entire ocean surface systematically, repeatedly, and at scales from meters to global.

Sea surface temperature is measured by both thermal infrared sensors (MODIS, VIIRS, Sentinel-3 SLSTR) and passive microwave radiometers (AMSR-E/AMSR-2). Infrared measurements achieve ~1 km resolution but are blocked by clouds. Microwave measurements penetrate clouds but at ~25 km resolution. Operational SST products merge both into daily gap-free maps that drive weather forecasting, fisheries management, and coral bleaching alerts.

Ocean color remote sensing targets the visible spectrum, where the absorption and scattering properties of seawater are modified by chlorophyll-a (phytoplankton pigment), colored dissolved organic matter (CDOM), and suspended sediments. Sensors like MODIS Aqua, Sentinel-3 OLCI, and the upcoming PACE mission measure water-leaving radiance at multiple narrow bands, from which bio-optical algorithms retrieve chlorophyll concentration, primary productivity, and water clarity. The challenge is that >90% of the signal reaching the sensor comes from the atmosphere, not the ocean -- atmospheric correction must remove this dominant atmospheric contribution to extract the subtle ocean signal.

Radar altimetry measures sea surface height with centimeter precision by timing radar pulses reflected from the ocean surface. The Jason/Sentinel-6 series of altimeters has produced an unbroken record since 1993, documenting global sea level rise, mapping mesoscale ocean eddies, and enabling operational ocean current forecasting. SAR altimetry (Sentinel-3, SWOT) extends these measurements to coastal zones and inland waters where traditional pulse-limited altimetry struggled.
