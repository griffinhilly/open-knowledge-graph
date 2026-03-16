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

## Explainer

From confirmatory factor analysis (CFA), you know how to specify a model where items load onto latent factors and test whether that structure fits the data. From item response theory (IRT), you know how item response functions describe the relationship between a latent trait and item performance. Dimensionality assessment is the question that comes before either of those: *how many* latent traits does this test actually measure? The answer determines which model is appropriate and what scores you can legitimately report.

The simplest case is **unidimensionality**: all items measure a single latent trait, and IRT's core assumption is satisfied. In practice, most psychological tests measure something that is mostly one thing but also has subcomponents. An intelligence test measures general cognitive ability but also verbal, spatial, and processing-speed abilities. A depression questionnaire measures overall depression but also affective, somatic, and cognitive symptom clusters. The question is whether these subcomponents are strong enough to matter, or whether treating the test as essentially unidimensional is close enough.

**Bifactor models** offer a powerful solution to this problem. Instead of forcing a choice between "one factor" and "multiple factors," bifactor models specify a **general factor** that all items load on plus **group factors** that capture the residual clustering. Every item has two loadings: one on the general factor and one on its specific group factor. This structure lets you ask: "How much variance does the general factor explain versus the group factors?" The answer guides what scores to report. If the general factor dominates, a total score makes sense. If group factors are strong, subscale scores carry interpretable variance that would be lost in a total score.

The practical output of bifactor modeling is a set of **omega coefficients** that are far more informative than Cronbach's alpha. **Omega-total** estimates the reliability of the total score, capturing all sources of common variance. **Omega-hierarchical** (sometimes called omega-general) estimates how much of the total score variance is attributable to the general factor alone — this is the key index for justifying a single total score. **Omega-subscale** estimates the reliability of subscale scores after removing the general factor. If omega-hierarchical is high (say, 0.85) but omega-subscale for verbal ability is also substantial (0.65), you have evidence that both a total score and verbal subscale scores carry meaningful signal. The clinical implication is direct: a psychologist administering an intelligence test should report not just a full-scale IQ, but also the subscale scores when the bifactor model shows those scales have interpretable specific variance.
