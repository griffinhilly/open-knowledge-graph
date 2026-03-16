---
id: spatial-epidemiology
title: Spatial Epidemiology and Geographic Analysis
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: environmental-epidemiology-assessment
  type: hard
- id: disease-frequency-measures
  type: soft
tags:
- spatial-analysis
- geographic-variation
- mapping
- spatial-autocorrelation
stage: advanced
status: draft
---

# Spatial Epidemiology and Geographic Analysis

## Core Idea
Spatial epidemiology examines geographic disease variation and identifies clusters and hotspots. Spatial data exhibit autocorrelation (nearby locations more similar than distant ones), violating independence assumptions. Spatial regression and cluster detection algorithms identify areas of unusually high or low risk.

## Explainer

From your study of environmental epidemiology, you know that exposures are often place-based: air pollution concentrations, contaminated water sources, proximity to industrial facilities. The distribution of disease is therefore also place-based. **Spatial epidemiology** formalizes the methods for analyzing that geographic structure — moving beyond saying "there seems to be more cancer near this plant" to rigorously testing whether observed clustering exceeds what would be expected by chance, and estimating the magnitude of geographic risk variation.

The foundational concept is **spatial autocorrelation**, sometimes called Tobler's first law of geography: "everything is related to everything else, but near things are more related than distant things." Neighborhoods close to each other tend to have similar air quality, similar socioeconomic composition, similar access to healthcare, and similar disease rates. This violates the independence assumption of standard regression models: if neighboring Census tracts have similar disease rates not because of measured covariates but because of unmeasured shared environmental factors, the residuals from an OLS model will be spatially correlated. **Spatial regression** models — including spatial lag models (the outcome in a location is partly predicted by neighboring outcomes) and spatial error models (residuals are spatially autocorrelated) — correct for this by explicitly modeling the spatial dependence structure. The degree of autocorrelation is measured by **Moran's I**, which ranges from −1 (perfect spatial dispersion) through 0 (random) to +1 (perfect clustering).

**Cluster detection** is the spatial analog of outbreak investigation. The most widely used method is the **SaTScan spatial scan statistic**, which works by imposing circular windows of varying radius across the study area, counting observed versus expected cases inside each window, and identifying the window with the highest likelihood ratio. Statistical significance is assessed by Monte Carlo simulation — generating thousands of random spatial distributions of cases and comparing the observed maximum to the null distribution. This approach controls for the multiple-testing problem that arises from scanning many possible clusters simultaneously. The output is a map showing statistically significant clusters with elevated (or reduced) risk, which can guide public health investigation into underlying causes.

Two key pitfalls must always be considered. The **ecological fallacy** is the error of inferring individual-level associations from area-level data. If areas with high poverty rates also have high diabetes rates, this tells you about the area-level association, not necessarily that poor *individuals* have higher diabetes risk within those areas — a wealthier resident of a poor area might still be at high personal risk due to unmeasured individual factors. The **modifiable areal unit problem (MAUP)** is the observation that results depend on how geographic units are drawn: county-level analysis often shows different patterns than ZIP-code or Census tract level analysis of the same underlying case data. Both problems require interpretive caution and, when possible, supplementation with individual-level data. When used carefully, spatial epidemiology is invaluable for identifying environmental justice disparities, targeting interventions, and generating hypotheses about exposure sources that observational studies can then test more rigorously.
