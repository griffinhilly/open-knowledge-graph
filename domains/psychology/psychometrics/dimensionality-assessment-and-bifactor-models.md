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
stage: expert
status: validated
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

## Questions

```yaml
- question: "A psychologist administers a depression questionnaire with 20 items and obtains Cronbach's alpha = .91. She concludes the test is unidimensional and that only a total score should be reported. What is the critical problem with this reasoning?"
  type: multiple-choice
  options:
    - "Cronbach's alpha must reach .95 or higher before a total score is justified"
    - "Subscale scores should always be reported regardless of the underlying factor structure"
    - "High alpha reflects internal consistency, not unidimensionality — strong group factors can produce high alpha even in a clearly multidimensional test"
    - "She should have used omega-total instead, which would definitively confirm unidimensionality"
  answer: 2
  explanation: "Alpha is sensitive to the average inter-item correlation and scale length, not to whether items measure one latent trait or several. A test with two or three strong correlated subfactors will yield high alpha while being clearly multidimensional — bifactor analysis might reveal that affective, somatic, and cognitive symptom clusters all carry substantial specific variance beyond a general depression factor. The correct tool for assessing unidimensionality is exploratory or confirmatory factor analysis, not alpha."

- question: "A bifactor model fitted to an intelligence battery yields omega-hierarchical = .83 and omega-subscale for verbal ability = .61. What does this pattern most clearly support?"
  type: multiple-choice
  options:
    - "The verbal subscale is unreliable and subscale scores should not be reported"
    - "Both a total score and verbal subscale scores carry meaningful information and can both be legitimately reported"
    - "The general factor explains all meaningful variance; the verbal subscale adds nothing beyond the total score"
    - "The bifactor model is misspecified because omega-subscale should always exceed omega-hierarchical"
  answer: 1
  explanation: "Omega-hierarchical of .83 indicates the general factor accounts for substantial reliable variance in the total score, justifying a full-scale score. Omega-subscale of .61 for verbal ability indicates the verbal subscale has meaningful reliable variance *beyond* the general factor — not captured by the total score. Both numbers being substantial is exactly the pattern that justifies reporting both levels. Reporting only the total score in this situation discards clinically relevant information."

- question: "A bifactor model simultaneously models a general factor (which all items load on) and group-specific factors (which subsets of items load on), allowing the two levels of structure to be estimated at once."
  type: true-false
  answer: true
  explanation: "This is the defining feature of bifactor models. Every item receives two loadings: one on the general factor and one on its group factor. This is what makes bifactor models more informative than either a pure unidimensional model (which ignores the group structure) or a standard correlated-factors model (which doesn't cleanly separate general from specific variance). The simultaneous estimation allows omega coefficients to be computed that attribute variance to each level."

- question: "A Cronbach's alpha of .90 provides strong evidence that a psychological test measures a single latent trait."
  type: true-false
  answer: false
  explanation: "Alpha measures internal consistency — the degree to which items correlate with each other — not dimensionality. A test can achieve high alpha through several correlated subfactors without being unidimensional. For example, an anxiety measure with distinct cognitive, somatic, and behavioral facets that all correlate with each other could easily yield alpha = .90 while a bifactor model shows significant specific variance in each facet. Unidimensionality requires factor analysis, not alpha."

- question: "What is the key advantage of omega-hierarchical over Cronbach's alpha when deciding whether to justify reporting a single total score from a multidimensional psychological test?"
  type: short-answer
  answer: "Omega-hierarchical specifically estimates what proportion of total score variance is attributable to the general factor alone, after accounting for group factors. If it is high, the general factor dominates the total score and reporting a single score is defensible. Cronbach's alpha inflates when items form correlated clusters, so it can be high even when group factors carry substantial specific variance — it cannot distinguish between 'one strong general factor' and 'several correlated specific factors.' Omega-hierarchical makes that distinction directly."
  explanation: "The practical decision about what scores to report turns on whether the general factor or the group factors are doing more work. Omega-hierarchical answers that question. A low omega-hierarchical (say .50) alongside high alpha (.90) would signal that alpha is being inflated by group structure, and that subscale scores would be more interpretable than a total. A high omega-hierarchical means the total score reflects mostly the general factor — the variance that subscales share — which is what makes a single total score scientifically defensible."
```

## Explainer

From confirmatory factor analysis (CFA), you know how to specify a model where items load onto latent factors and test whether that structure fits the data. From item response theory (IRT), you know how item response functions describe the relationship between a latent trait and item performance. Dimensionality assessment is the question that comes before either of those: *how many* latent traits does this test actually measure? The answer determines which model is appropriate and what scores you can legitimately report.

The simplest case is **unidimensionality**: all items measure a single latent trait, and IRT's core assumption is satisfied. In practice, most psychological tests measure something that is mostly one thing but also has subcomponents. An intelligence test measures general cognitive ability but also verbal, spatial, and processing-speed abilities. A depression questionnaire measures overall depression but also affective, somatic, and cognitive symptom clusters. The question is whether these subcomponents are strong enough to matter, or whether treating the test as essentially unidimensional is close enough.

**Bifactor models** offer a powerful solution to this problem. Instead of forcing a choice between "one factor" and "multiple factors," bifactor models specify a **general factor** that all items load on plus **group factors** that capture the residual clustering. Every item has two loadings: one on the general factor and one on its specific group factor. This structure lets you ask: "How much variance does the general factor explain versus the group factors?" The answer guides what scores to report. If the general factor dominates, a total score makes sense. If group factors are strong, subscale scores carry interpretable variance that would be lost in a total score.

The practical output of bifactor modeling is a set of **omega coefficients** that are far more informative than Cronbach's alpha. **Omega-total** estimates the reliability of the total score, capturing all sources of common variance. **Omega-hierarchical** (sometimes called omega-general) estimates how much of the total score variance is attributable to the general factor alone — this is the key index for justifying a single total score. **Omega-subscale** estimates the reliability of subscale scores after removing the general factor. If omega-hierarchical is high (say, 0.85) but omega-subscale for verbal ability is also substantial (0.65), you have evidence that both a total score and verbal subscale scores carry meaningful signal. The clinical implication is direct: a psychologist administering an intelligence test should report not just a full-scale IQ, but also the subscale scores when the bifactor model shows those scales have interpretable specific variance.
