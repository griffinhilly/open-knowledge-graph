---
id: geostatistics
title: Geostatistics
domain: earth-and-space-sciences
course: remote-sensing-and-gis
prerequisites:
- id: spatial-analysis-gis
  type: hard
builds-toward: []
tags:
- geostatistics
- kriging
- variogram
- spatial-interpolation
stage: advanced
status: validated
---

# Geostatistics

## Core Idea
Geostatistics provides a framework for analyzing and predicting spatially distributed phenomena based on the principle that nearby measurements are more similar than distant ones. The variogram (or semivariogram) quantifies this spatial dependence by measuring how the variance between paired observations increases with separation distance. Kriging uses the variogram model to produce optimal, unbiased spatial predictions at unsampled locations, along with prediction uncertainty estimates. Unlike simple interpolation methods (inverse distance weighting, splines), kriging is grounded in the theory of regionalized variables and produces not just predicted values but confidence intervals -- telling you both what the estimate is and how reliable it is.

## Questions

```yaml
- question: "A soil scientist measures lead contamination at 50 sample points and needs to produce a continuous contamination map. Why might kriging be preferred over inverse distance weighting (IDW)?"
  type: multiple-choice
  options:
    - "Kriging is computationally faster than IDW"
    - "Kriging uses the variogram to model the actual spatial structure of the data and provides prediction uncertainty estimates, while IDW uses an arbitrary distance-weighting function and gives no uncertainty information"
    - "IDW cannot handle irregularly spaced sample points"
    - "Kriging produces smoother maps that look better in reports"
  answer: 1
  explanation: "Kriging models the specific spatial correlation structure of the data (via the variogram), weights nearby samples optimally, and produces a standard error map showing where predictions are reliable and where they are uncertain. IDW applies a generic distance-decay function regardless of the data's actual spatial behavior and gives no uncertainty quantification. For environmental contamination assessment, knowing the uncertainty is as important as the prediction itself."

- question: "A variogram that reaches a constant value (the sill) at a certain distance (the range) indicates that observations separated by more than the range are no longer spatially correlated."
  type: true-false
  answer: true
  explanation: "The range is the distance at which the variogram reaches its sill (plateau). Beyond this distance, pairs of observations are no more similar than random pairs -- spatial autocorrelation has decayed to zero. The sill represents the total variance of the data. The nugget (variogram value at distance zero) represents very short-range variability plus measurement error. These three parameters -- nugget, sill, range -- characterize the spatial structure."

- question: "Explain what the nugget effect in a variogram represents physically."
  type: short-answer
  answer: "The nugget is the variogram value extrapolated to zero separation distance. Theoretically, two observations at the same location should be identical (zero variance), but the nugget captures two real-world effects: (1) measurement error -- repeat measurements at the same point will differ due to instrument precision and sampling variability; (2) micro-scale spatial variation at distances smaller than the sampling interval that the survey cannot resolve. A large nugget relative to the sill indicates that much of the total variance is either noise or occurs at scales finer than the sampling design can capture."
  explanation: "The nugget represents the irreducible uncertainty in the data -- the variance that cannot be explained by spatial structure at the scale of observation."
```

## Explainer

Most environmental, geological, and resource variables are not randomly distributed -- they exhibit spatial structure. Soil properties, ore grades, groundwater levels, and pollutant concentrations all show patterns where nearby locations tend to have similar values. Geostatistics provides the mathematical framework to describe, model, and exploit this spatial structure for prediction.

The variogram is the central diagnostic tool. It plots the average squared difference between paired observations against their separation distance. A typical variogram rises from a nugget (near-zero distance variance) to a sill (maximum variance) over a characteristic range (the distance at which spatial correlation disappears). The shape of this rise (linear, exponential, spherical, Gaussian) describes how quickly spatial similarity decays with distance -- steep rises indicate rapid decorrelation (patchy phenomena), while gradual rises indicate broad spatial continuity (smooth phenomena).

Kriging is the prediction engine. Given a variogram model and a set of sample data, ordinary kriging computes the optimal linear prediction at any unsampled location by weighting nearby samples according to their spatial configuration and the variogram. Samples closer to the prediction point and in less-redundant configurations receive higher weights. The result is the Best Linear Unbiased Predictor (BLUP) -- it minimizes prediction variance while remaining unbiased. Crucially, kriging also produces a prediction variance at each location, enabling probabilistic statements ("there is a 95% probability that contamination exceeds the threshold here").

Variants include simple kriging (known mean), universal kriging (models spatial trends), indicator kriging (predicts probabilities of exceeding thresholds), and co-kriging (uses correlated secondary variables). Geostatistics underpins mineral resource estimation, environmental site assessment, precision agriculture, and any application where spatial prediction with quantified uncertainty is needed.
