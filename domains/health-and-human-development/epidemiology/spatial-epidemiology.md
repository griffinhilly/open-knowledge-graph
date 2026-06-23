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
- id: hierarchical-models-epidemiology
  type: soft
tags:
- spatial-analysis
- geographic-variation
- mapping
- spatial-autocorrelation
stage: expert
status: validated
---

# Spatial Epidemiology and Geographic Analysis

## Core Idea
Spatial epidemiology examines geographic disease variation and identifies clusters and hotspots. Spatial data exhibit autocorrelation (nearby locations more similar than distant ones), violating independence assumptions. Spatial regression and cluster detection algorithms identify areas of unusually high or low risk.

## Questions

```yaml
- question: "A researcher uses ordinary least squares (OLS) regression to model county-level diabetes rates as a function of poverty and food access. The primary methodological concern with this analysis is:"
  type: multiple-choice
  options:
    - "OLS cannot accept area-level data as inputs"
    - "Neighboring counties likely have similar diabetes rates due to shared unmeasured environmental factors, violating OLS's independence assumption"
    - "Diabetes rates cannot be mapped to county boundaries"
    - "The number of counties in the U.S. is too small for regression analysis"
  answer: 1
  explanation: "OLS assumes that observations are independent. In spatial data, neighboring areas tend to be more similar than distant ones (spatial autocorrelation) because they share unobserved environmental, socioeconomic, and demographic factors. This produces spatially correlated residuals, violating the independence assumption and biasing standard errors. Spatial regression models — which explicitly model the dependence structure — are the correct solution."

- question: "A spatial scan statistic identifies a significant cluster of elevated lung cancer rates near an industrial facility. A critic invokes the ecological fallacy. This means:"
  type: multiple-choice
  options:
    - "The cluster is likely a statistical artifact requiring more data to confirm"
    - "The geographic boundary of the cluster was drawn arbitrarily, invalidating the result"
    - "The area-level association between proximity to the facility and lung cancer does not prove that individuals living near the facility have elevated personal risk"
    - "The Monte Carlo simulation used to assess significance was underpowered"
  answer: 2
  explanation: "The ecological fallacy is the error of inferring individual-level relationships from area-level data. Even if areas near the facility have higher lung cancer rates on average, this could reflect confounding by socioeconomic status, age distribution, or smoking rates that differ between areas — not necessarily individual exposure to the facility. The area-level association is a hypothesis-generating finding, not individual-level causal evidence. Supplementing with individual-level exposure data is the methodological remedy."

- question: "A Moran's I value of +1 indicates that geographically adjacent areas have randomly distributed disease rates with no spatial clustering."
  type: true-false
  answer: false
  explanation: "Moran's I ranges from −1 to +1. A value near 0 indicates spatial randomness (no autocorrelation). A value near +1 indicates perfect positive spatial autocorrelation — adjacent areas are maximally similar (strong clustering). A value near −1 indicates perfect spatial dispersion — adjacent areas are maximally different (a checkerboard pattern). The claim in the question reverses the interpretation."

- question: "The modifiable areal unit problem (MAUP) means that spatial analysis results can change depending on how geographic boundaries are drawn, even when the underlying case data are identical."
  type: true-false
  answer: true
  explanation: "MAUP is a fundamental limitation of area-based spatial analysis. Whether you aggregate data to counties, ZIP codes, or Census tracts — different choices of areal unit — can produce different and sometimes contradictory patterns from the same point-level data. This is because different aggregation schemes create different mixes of cases and populations within each unit. Reporting scale-sensitivity is a standard requirement in careful spatial epidemiology."

- question: "Why do standard regression models often produce misleading results when applied to geographic disease rate data, and what does spatial regression do differently?"
  type: short-answer
  answer: "Standard OLS assumes observations are independent, but neighboring areas share environmental, socioeconomic, and unmeasured factors that make their disease rates more similar than chance would predict. This spatial autocorrelation shows up as correlated residuals, violating OLS assumptions and biasing standard errors. Spatial regression models — spatial lag models (neighboring outcomes predict the current outcome) or spatial error models (residuals are spatially correlated) — explicitly model this dependence structure, producing valid inference."
  explanation: "Tobler's first law of geography — 'near things are more related than distant things' — is the underlying principle. OLS treats a Census tract in downtown Boston as statistically no more similar to adjacent tracts than to a tract in rural Montana. Spatial models encode the geographic neighborhood structure, allowing the analysis to distinguish the effect of measured covariates from the unmeasured spatial background that makes neighbors resemble each other."
```

## Explainer

From your study of environmental epidemiology, you know that exposures are often place-based: air pollution concentrations, contaminated water sources, proximity to industrial facilities. The distribution of disease is therefore also place-based. **Spatial epidemiology** formalizes the methods for analyzing that geographic structure — moving beyond saying "there seems to be more cancer near this plant" to rigorously testing whether observed clustering exceeds what would be expected by chance, and estimating the magnitude of geographic risk variation.

The foundational concept is **spatial autocorrelation**, sometimes called Tobler's first law of geography: "everything is related to everything else, but near things are more related than distant things." Neighborhoods close to each other tend to have similar air quality, similar socioeconomic composition, similar access to healthcare, and similar disease rates. This violates the independence assumption of standard regression models: if neighboring Census tracts have similar disease rates not because of measured covariates but because of unmeasured shared environmental factors, the residuals from an OLS model will be spatially correlated. **Spatial regression** models — including spatial lag models (the outcome in a location is partly predicted by neighboring outcomes) and spatial error models (residuals are spatially autocorrelated) — correct for this by explicitly modeling the spatial dependence structure. The degree of autocorrelation is measured by **Moran's I**, which ranges from −1 (perfect spatial dispersion) through 0 (random) to +1 (perfect clustering).

**Cluster detection** is the spatial analog of outbreak investigation. The most widely used method is the **SaTScan spatial scan statistic**, which works by imposing circular windows of varying radius across the study area, counting observed versus expected cases inside each window, and identifying the window with the highest likelihood ratio. Statistical significance is assessed by Monte Carlo simulation — generating thousands of random spatial distributions of cases and comparing the observed maximum to the null distribution. This approach controls for the multiple-testing problem that arises from scanning many possible clusters simultaneously. The output is a map showing statistically significant clusters with elevated (or reduced) risk, which can guide public health investigation into underlying causes.

Two key pitfalls must always be considered. The **ecological fallacy** is the error of inferring individual-level associations from area-level data. If areas with high poverty rates also have high diabetes rates, this tells you about the area-level association, not necessarily that poor *individuals* have higher diabetes risk within those areas — a wealthier resident of a poor area might still be at high personal risk due to unmeasured individual factors. The **modifiable areal unit problem (MAUP)** is the observation that results depend on how geographic units are drawn: county-level analysis often shows different patterns than ZIP-code or Census tract level analysis of the same underlying case data. Both problems require interpretive caution and, when possible, supplementation with individual-level data. When used carefully, spatial epidemiology is invaluable for identifying environmental justice disparities, targeting interventions, and generating hypotheses about exposure sources that observational studies can then test more rigorously.
