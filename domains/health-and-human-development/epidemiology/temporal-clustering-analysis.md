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
stage: expert
status: validated
---

# Temporal Clustering and Seasonality Analysis

## Core Idea
Temporal clustering refers to non-random disease occurrence patterns in time. Seasonal patterns and epidemic curves indicate temporal clustering. Detection methods identify deviations from baseline expected rates. Clustering suggests common exposure windows or transmission chains.

## Questions

```yaml
- question: "Epidemiologists detect a sharp cluster of gastroenteritis cases over 3 days among attendees of a company picnic, with all cases appearing within one incubation period. A second similar cluster appears 3 weeks later among employees who had no contact with the first group. What does this temporal pattern most suggest?"
  type: multiple-choice
  options:
    - "A propagated outbreak originating from the picnic, with secondary cases appearing after one generation interval"
    - "Two separate point-source exposures — each cluster is narrow and contained within a single incubation period, suggesting two distinct contamination events"
    - "Annual seasonal influenza following its typical bimodal winter pattern"
    - "Person-to-person spread from a single index case at the picnic generating two waves of transmission"
  answer: 1
  explanation: "Each cluster is narrow (cases within a single incubation period) and the two groups had no contact — both features are inconsistent with propagated transmission, which would show successive waves at intervals matching the incubation period with continuous chain-of-contact. Two separate narrow clusters in isolated populations point to two distinct point-source exposures. A propagated epidemic (option D) would show a gradually broadening curve with new cases at each subsequent generation, and would require contact between the two groups."

- question: "Kulldorff's temporal scan statistic is used in disease surveillance rather than simply comparing weekly counts to a historical average. What is the key methodological advantage of the scan statistic?"
  type: multiple-choice
  options:
    - "It is computationally simpler and requires less historical data than baseline comparison methods"
    - "It tests windows of variable width across the time series without requiring prior specification of when or how long an outbreak will last, while correcting for the multiple comparisons introduced by scanning many windows"
    - "It eliminates seasonal variation automatically, making a separate seasonal adjustment model unnecessary"
    - "It can detect clusters from just two data points, making it faster to deploy in early outbreak response"
  answer: 1
  explanation: "The key advantage of scan statistics is that they do not require the analyst to pre-specify the time window of interest. An outbreak of unknown start date and duration can still be detected because the scan statistic tests all possible window locations and widths simultaneously. The multiple-comparison correction (via Monte Carlo simulation of the null distribution) ensures that the overall false positive rate is controlled despite testing many windows. A fixed-window baseline comparison method would miss outbreaks that don't align with the pre-specified interval."

- question: "A significant peak in the autocorrelation function (ACF) at a lag of 52 weeks, computed from weekly disease incidence data, is consistent with annual seasonality in that disease."
  type: true-false
  answer: true
  explanation: "The ACF measures how strongly disease counts at time t are correlated with counts at time t+k (lag k). For a disease with annual seasonality, incidence at week 1 in any given year is correlated with incidence at week 1 the following year — which is a lag of 52 weeks. A significant ACF peak at lag 52 (in weekly data) directly identifies a recurring annual pattern. The ACF would show additional peaks at multiples of 52 (104, 156 weeks, etc.) for a strongly seasonal disease."

- question: "A broad, multi-week epidemic curve with new case waves appearing at intervals approximately equal to one incubation period is most consistent with a point-source food contamination event."
  type: true-false
  answer: false
  explanation: "This pattern is the hallmark of propagated (person-to-person) transmission. In a point-source exposure, all cases share the same exposure event, so onset dates cluster within a single incubation period producing a narrow, peaked curve. When new waves appear at intervals matching the incubation period, it indicates successive generations of transmission: infected people from one generation expose others, who develop illness one incubation period later. Distinguishing these patterns is critical for response: point-source outbreaks require identifying and eliminating the source, while propagated outbreaks require interrupting transmission chains."

- question: "Explain how the temporal shape and width of a disease cluster helps narrow down whether the underlying cause is a point-source exposure versus person-to-person transmission, and why this distinction matters for the public health response."
  type: short-answer
  answer: "A point-source exposure (e.g., contaminated food at a single event) produces a narrow, unimodal cluster: all exposed individuals share the same exposure time, so their onset dates are spread only by variation in incubation period around a single central exposure. The cluster width approximates one incubation period. In contrast, propagated transmission produces a broader, multi-modal pattern: the index cases infect secondary cases who infect tertiary cases, with each generation separated by approximately one incubation period — the curve broadens and shows successive peaks. The distinction matters critically for response: a point-source outbreak requires identifying and removing the contaminated source (a food product, a water supply); a propagated outbreak requires interrupting transmission chains through isolation of cases, contact tracing, or vaccination. Responding to a propagated outbreak as if it were point-source (by searching for a contaminated food) would miss the actual mechanism and allow the chain of transmission to continue."
  explanation: "The epidemic curve shape was recognized as a diagnostic tool long before formal statistical methods existed — John Snow's original investigation of the 1854 Broad Street cholera outbreak used the time distribution of cases (concentrated around a single exposure event at the pump) to identify point-source transmission. Modern scan statistics and autocorrelation methods formalize this intuition into rigorous statistical tests, but the underlying conceptual logic — temporal pattern reveals transmission mechanism — is the same."
```

## Explainer

From your study of epidemic curves, you know how to plot disease onset dates as a histogram to visualize the time course of an outbreak — the characteristic shape of a point-source curve versus a propagated curve tells you about exposure patterns and transmission chains. **Temporal clustering analysis** formalizes and extends this visual intuition into statistical methods that detect whether disease cases occur closer together in time than would be expected by chance, and at what scales and with what periodicity.

The baseline idea is straightforward: if disease incidence were purely random — cases drawn from a uniform distribution over time — they would be spread evenly. Any real disease deviates from this baseline, and the question is whether deviation is systematic. The most basic detection approach compares observed case counts in each time interval to an **expected count** derived from a baseline model — typically a historical average rate, a Poisson-distributed count, or a model adjusting for population growth and secular trends. When observed counts exceed the upper confidence limit of the baseline, an alert is triggered, signaling a potential outbreak or seasonal peak.

**Seasonality** is the most regular and expected form of temporal clustering: diseases that recur predictably with calendar season. Influenza peaks in winter in temperate climates; enteric infections spike in summer; vector-borne diseases track arthropod season. Detecting seasonality requires methods that identify periodic signals in count data. **Fourier analysis** decomposes time series into sinusoidal components, identifying dominant frequencies — a peak at frequency 1/year identifies annual seasonality. **Autocorrelation functions (ACF)** measure how correlated case counts at time t are with counts at time t+k (the lag), showing significant peaks at lags corresponding to recurring intervals. These methods separate the seasonal signal from noise, enabling routine seasonal variation to be distinguished from epidemic superimposed on that background.

Beyond seasonality, **scan statistics** — particularly Kulldorff's temporal scan statistic — offer a rigorous approach to detecting clusters without prespecifying their timing or duration. The method moves a window of variable width across the time series, and at each position tests whether the rate inside the window is significantly elevated above the rate outside it, accounting for the multiple-testing problem introduced by scanning many windows. This data-driven approach is valuable in surveillance, where you do not know in advance when an outbreak will start or how long it will last.

Temporal clustering patterns contain etiologic information. A **sharp, narrow cluster** — cases appearing within a single incubation period over a few days — suggests a **point-source exposure**: contaminated food, a water supply failure, a single infectious event. A **broader, spreading cluster** where new cases appear at intervals matching an incubation period suggests **propagated transmission**: person-to-person spread generating successive waves. **Recurrent annual clusters** point to seasonal exposures, seasonal changes in host susceptibility, or seasonal vector activity. The shape and width of detected clusters narrows the hypothesis space for the underlying cause, connecting temporal statistics back to the mechanistic questions of transmission that drive outbreak investigation.
