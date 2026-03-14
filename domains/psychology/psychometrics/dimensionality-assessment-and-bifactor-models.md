---
id: dimensionality-assessment-and-bifactor-models
title: Dimensionality Assessment and Bifactor Models
domain: psychology
course: psychometrics
prerequisites:
- id: item-response-functions
  type: hard
- id: confirmatory-factor-analysis
  type: hard
builds-toward:
- multidimensional-item-response-theory
tags:
- dimensionality
- factor-analysis
- bifactor
- test-structure
- omega
stage: advanced
status: draft
---

# Dimensionality Assessment and Bifactor Models

## Core Idea
Dimensionality assessment determines whether a test measures one latent trait or multiple latent traits, using exploratory/confirmatory factor analysis and IRT fit indices. Bifactor models represent a general factor (e.g., overall intelligence) and specific group factors (e.g., verbal and spatial abilities), allowing computation of scores at multiple levels. Omega coefficients based on bifactor models provide more nuanced reliability estimates than traditional Cronbach's alpha.

## How It's Best Learned
Conduct factor analyses on multi-subtest data from intelligence or achievement tests. Fit unidimensional models, standard factor models, and bifactor models, then compare fit. Interpret omega_total (reliability of general factor), omega_group (reliability of group factors), and omega_subscale (reliability of subscale scores).

## Common Misconceptions
- Assuming a test is unidimensional if Cronbach's alpha is high; alpha is sensitive to internal consistency but not true unidimensionality.
- Treating group factors in bifactor models as independent; they are orthogonal by design but may correlate conceptually.
- Reporting only general factor scores when group factors are meaningfully interpretable and clinically relevant.
