---
id: percentile-ranks-and-interpretation
title: Percentile Ranks and Their Interpretation
domain: psychology
course: psychometrics
prerequisites:
- id: norm-referenced-criterion-referenced-interpretation
  type: hard
builds-toward:
- standard-scores-transformations
tags:
- percentiles
- score-conversion
- interpretation
stage: advanced
status: draft
---

# Percentile Ranks and Their Interpretation

## Core Idea
A percentile rank indicates the percentage of a norm group scoring at or below a given raw score. Percentiles are intuitive for non-technical audiences but have unequal intervals, clustering near center and widening at extremes. Percentile of 50 means average performance, not 50% correct; percentiles from different norm groups are incomparable.

## Explainer

From norm-referenced interpretation, you know that a test score's meaning depends entirely on the comparison group. A raw score of 45 is uninformative by itself; "better than 82% of the standardization sample" tells you where someone stands in a reference population. A **percentile rank** is the most intuitive way to communicate that relative standing: it tells you the percentage of the norm group who scored at or below a given raw score. A percentile rank of 75 means the person outperformed 75% of the reference group — not that they answered 75% of items correctly.

This simplicity is the percentile's greatest strength for communicating to non-technical audiences — parents, patients, clients, school administrators. But it comes with a structural trap: **percentile ranks have unequal intervals**. Because most psychological traits are approximately normally distributed, scores cluster near the middle. This means small raw-score differences near the center of the distribution correspond to large percentile differences, while large raw-score differences at the extremes correspond to small percentile differences. Moving from the 45th to the 55th percentile represents a much smaller raw-score gain than moving from the 90th to the 95th, even though both involve a 5-percentile-point shift. If you average percentiles, subtract them, or use them to measure change, you will systematically distort the picture.

This is the practical consequence that matters most for score interpretation: a 10-percentile-point gain at the middle of the distribution is easier to achieve than the same gain near the tails, because the raw score distances are unequal. For this reason, when tracking change over time or computing means, psychometricians prefer **standard scores** — z-scores, T-scores, scaled scores, IQ scores — which are linear transformations that preserve equal intervals. Percentiles are the right tool for communicating position; standard scores are the right tool for arithmetic.

Two persistent misreadings warrant direct attention. First, a percentile rank of 50 does not mean "50% of items correct" — that would be a percent-correct score. A person at the 50th percentile is exactly average relative to the norm group, regardless of raw score. Second, percentiles from different norm groups are not comparable. A 75th percentile on a test normed on a 1990 sample is not the same standing as a 75th percentile on the same test renormed in 2020, if the population's performance has shifted. Always confirm which norm sample a percentile is derived from, and match the norm group to the population the test is being used to evaluate.
