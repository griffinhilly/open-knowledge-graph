---
id: hierarchical-models-epidemiology
title: Hierarchical and Multilevel Models
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: multivariable-regression-epi
  type: hard
- id: biostatistics-in-public-health
  type: soft
builds-toward:
- spatial-epidemiology
tags:
- multilevel-modeling
- mixed-effects
- clustering
stage: advanced
status: draft
---

# Hierarchical and Multilevel Models

## Core Idea
Hierarchical (multilevel/mixed-effects) models handle data with nested structure—individuals within schools, patients within hospitals, repeated measurements within persons—by accounting for within-cluster correlation through random intercepts or slopes at each level. They improve statistical inference and allow investigation of cluster-level effects while borrowing strength across clusters. Partial pooling of cluster-specific estimates provides better small-sample estimates than either complete pooling or no pooling.

## How It's Best Learned
Fit models with and without random effects to clustered data; compare to standard approaches and examine intraclass correlation coefficients.

## Common Misconceptions
Random effects allow one to ignore clustering (ignoring ICC leads to invalid inference). Must check ICC to assess the practical importance of clustering for standard errors.
