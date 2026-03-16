---
id: epidemiological-study-design-selection
title: Selecting Appropriate Epidemiologic Study Designs
domain: health-and-human-development
course: public-health
prerequisites:
- id: epidemiologic-study-designs
  type: hard
- id: measures-of-association
  type: hard
builds-toward:
- disease-transmission-dynamics-modeling
- epidemic-investigation-methodology
tags:
- epidemiology
- methodology
- study-design
stage: abstract-reasoning
status: draft
---

# Selecting Appropriate Epidemiologic Study Designs

## Core Idea
Selecting the optimal epidemiologic study design requires matching the research question, available resources, and study population to the design's strengths and limitations. Cross-sectional studies measure prevalence efficiently; case-control studies investigate rare outcomes; cohort studies establish temporal relationships. The choice affects both the validity of causal inference and the practical feasibility of implementation.

## How It's Best Learned
Compare designs side-by-side for the same research question (e.g., whether air pollution causes asthma), noting the different data requirements, cost-benefit tradeoffs, and causal conclusions possible from each.

## Common Misconceptions
- Cohort studies always establish causation better than case-control studies; both face confounding unless carefully designed.
- Observational studies never provide causal evidence; careful design and analysis can strengthen causal inference.

## Explainer

Choosing an epidemiologic study design is an exercise in matching constraints to research goals. You've already learned the catalog of design types — cross-sectional, case-control, cohort, randomized controlled trial — and the measures of association each produces. Now the question becomes: given a specific research question, which design is optimal? The answer depends on four interacting factors: the frequency of the outcome, the frequency of the exposure, the ethical and practical feasibility of manipulation, and the strength of causal inference required.

Start with a concrete example: you want to study whether long-term air pollution exposure causes asthma. A **cross-sectional study** surveys a population at one moment, measuring both asthma prevalence and current pollution exposure. It's cheap and fast, and it will tell you whether asthma is more common in high-pollution areas. But it cannot tell you whether pollution exposure preceded asthma onset — the causal direction is ambiguous. Cross-sectional studies are best for estimating **prevalence** and generating hypotheses, not for establishing causation.

When the outcome is rare, a **case-control study** is almost always the right choice. Recruit 200 asthma cases and 400 matched controls, then ask about their pollution exposure history. This design is efficient: you study a rare outcome without needing to follow thousands of people for years. The tradeoffs are recall bias (cases may remember exposures differently than controls) and the inability to directly calculate incidence — you can only compute **odds ratios**. When you need to follow a defined population over time, a **cohort study** is appropriate. Assemble groups with high versus low pollution exposure and track who develops asthma over 10 years. The key strength is temporality: you know exposure preceded the outcome. The key weakness is cost, time, and loss to follow-up, especially for diseases with long latency.

The practical selection rule is: rare outcome → case-control; rare exposure → cohort; prevalent outcome with simple measurement → cross-sectional; causal hypothesis with ethical feasibility of assignment → RCT. The claim that "observational studies can never establish causation" is too strong. The Bradford Hill criteria — strength of association, consistency across studies, dose-response relationship, biological plausibility, temporality — allow causal inference to be built incrementally. Both cohort and case-control studies face confounding, and neither design alone "proves" causation. But careful design, replication, and triangulation across multiple study types can produce causal conclusions that are scientifically credible even without randomization.
