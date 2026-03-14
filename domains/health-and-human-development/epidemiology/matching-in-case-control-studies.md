---
id: matching-in-case-control-studies
title: Matching in Case-Control Studies
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: epidemiologic-study-designs
  type: hard
- id: confounding-epidemiology
  type: hard
builds-toward:
- stratification-and-adjustment
tags:
- study-design
- confounding-control
- case-control
stage: advanced
status: draft
---

# Matching in Case-Control Studies

## Core Idea
Matching is a design strategy that pairs cases with controls on specific confounding variables (age, gender, etc.) to reduce confounding bias without necessarily losing statistical power. Matching can be 1:1, k:1, or frequency matching depending on study goals and resource constraints. Matched analyses require special statistical techniques such as conditional logistic regression to properly account for the matching structure and preserve bias reduction.

## How It's Best Learned
Compare unmatched and matched datasets for the same exposures and outcomes; visualize how matching reduces residual confounding.

## Common Misconceptions
Matching on a variable automatically controls for confounding without further adjustment. Overmatching on intermediate variables or strong correlates of exposure can unnecessarily decrease statistical efficiency and precision.
