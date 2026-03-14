---
id: measures-of-spread
title: 'Measures of Spread: Range, Variance, and Standard Deviation'
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: mean-median-mode
  type: hard
- id: sigma-notation
  type: soft
- id: histograms-and-frequency-distributions
  type: soft
builds-toward:
- boxplots-and-five-number-summary
- variance-of-random-variables
- standard-normal-and-z-scores
- correlation-coefficient
tags:
- standard-deviation
- variance
- range
- spread
- descriptive-statistics
stage: formal-systems
status: validated
---
# Measures of Spread: Range, Variance, and Standard Deviation

## Core Idea
While measures of center locate a distribution, measures of spread describe how dispersed data values are around that center. The range (max − min) is simple but sensitive to outliers. Variance averages squared deviations from the mean, and standard deviation is its square root — restoring the original units. Population standard deviation uses division by n; sample standard deviation uses n − 1 (Bessel's correction) to produce an unbiased estimate.

## How It's Best Learned
Have students compute standard deviation by hand for small datasets (5–8 values), tracking each step in a table: deviation, squared deviation, average. Then verify with a calculator. Contrast two datasets with the same mean but very different spreads — this makes the purpose of the statistic visceral.

## Common Misconceptions
- Using n instead of n − 1 when estimating population variance from a sample.
- Thinking standard deviation is the average distance from the mean (it is the square root of the average squared distance).
- Treating negative deviations as errors — they must be squared or absolute-valued to avoid cancellation.
