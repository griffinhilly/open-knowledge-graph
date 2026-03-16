---
id: temporal-clustering-analysis
title: Temporal Clustering and Seasonality Analysis
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: epidemic-curve-analysis
  type: hard
- id: infectious-disease-surveillance
  type: soft
builds-toward:
- outbreak-transmission-models
tags:
- temporal-analysis
- seasonality
- clustering
- trend-analysis
stage: advanced
status: draft
---

# Temporal Clustering and Seasonality Analysis

## Core Idea
Temporal clustering refers to non-random disease occurrence patterns in time. Seasonal patterns and epidemic curves indicate temporal clustering. Detection methods identify deviations from baseline expected rates. Clustering suggests common exposure windows or transmission chains.

## Explainer

From your study of epidemic curves, you know how to plot disease onset dates as a histogram to visualize the time course of an outbreak — the characteristic shape of a point-source curve versus a propagated curve tells you about exposure patterns and transmission chains. **Temporal clustering analysis** formalizes and extends this visual intuition into statistical methods that detect whether disease cases occur closer together in time than would be expected by chance, and at what scales and with what periodicity.

The baseline idea is straightforward: if disease incidence were purely random — cases drawn from a uniform distribution over time — they would be spread evenly. Any real disease deviates from this baseline, and the question is whether deviation is systematic. The most basic detection approach compares observed case counts in each time interval to an **expected count** derived from a baseline model — typically a historical average rate, a Poisson-distributed count, or a model adjusting for population growth and secular trends. When observed counts exceed the upper confidence limit of the baseline, an alert is triggered, signaling a potential outbreak or seasonal peak.

**Seasonality** is the most regular and expected form of temporal clustering: diseases that recur predictably with calendar season. Influenza peaks in winter in temperate climates; enteric infections spike in summer; vector-borne diseases track arthropod season. Detecting seasonality requires methods that identify periodic signals in count data. **Fourier analysis** decomposes time series into sinusoidal components, identifying dominant frequencies — a peak at frequency 1/year identifies annual seasonality. **Autocorrelation functions (ACF)** measure how correlated case counts at time t are with counts at time t+k (the lag), showing significant peaks at lags corresponding to recurring intervals. These methods separate the seasonal signal from noise, enabling routine seasonal variation to be distinguished from epidemic superimposed on that background.

Beyond seasonality, **scan statistics** — particularly Kulldorff's temporal scan statistic — offer a rigorous approach to detecting clusters without prespecifying their timing or duration. The method moves a window of variable width across the time series, and at each position tests whether the rate inside the window is significantly elevated above the rate outside it, accounting for the multiple-testing problem introduced by scanning many windows. This data-driven approach is valuable in surveillance, where you do not know in advance when an outbreak will start or how long it will last.

Temporal clustering patterns contain etiologic information. A **sharp, narrow cluster** — cases appearing within a single incubation period over a few days — suggests a **point-source exposure**: contaminated food, a water supply failure, a single infectious event. A **broader, spreading cluster** where new cases appear at intervals matching an incubation period suggests **propagated transmission**: person-to-person spread generating successive waves. **Recurrent annual clusters** point to seasonal exposures, seasonal changes in host susceptibility, or seasonal vector activity. The shape and width of detected clusters narrows the hypothesis space for the underlying cause, connecting temporal statistics back to the mechanistic questions of transmission that drive outbreak investigation.
