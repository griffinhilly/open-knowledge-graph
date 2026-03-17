---
id: intelligence-test-construction
title: Intelligence Test Construction and Score Interpretation
domain: psychology
course: psychometrics
prerequisites:
- id: classical-test-theory
  type: hard
- id: confirmatory-factor-analysis
  type: soft
- id: construct-validity-multitrait
  type: soft
tags:
- intelligence-testing
- wais
- stanford-binet
- g-factor
stage: advanced
status: draft
---

# Intelligence Test Construction and Score Interpretation

## Core Idea
Intelligence tests (WAIS, Stanford-Binet) are complex batteries measuring multiple cognitive abilities within a hierarchical structure. Construction involves theoretical grounding in intelligence models, extensive norming on representative samples, comprehensive validation across diverse populations, and careful standardization of administration and scoring.

## Explainer

Building on classical test theory, you already understand that every observed score is a signal-plus-noise combination: true score contaminated by measurement error. Intelligence test construction scales this challenge enormously — the goal is to measure a latent construct (or set of constructs) that is both theoretically contested and practically consequential. The **Wechsler Adult Intelligence Scale (WAIS)** and the **Stanford-Binet** are the most widely used individually administered intelligence batteries, and their construction reflects decades of iterative refinement at each step of the test development process.

The theoretical foundation comes first. Modern intelligence tests are grounded in hierarchical factor models — most influentially the **Cattell-Horn-Carroll (CHC) model**, which organizes cognitive abilities in tiers: a general factor (*g*) at the apex, broad abilities (fluid reasoning, crystallized intelligence, processing speed, working memory, and others) at the second stratum, and narrow task-specific abilities at the bottom. The WAIS operationalizes this by grouping subtests into composite indices — Verbal Comprehension, Perceptual Reasoning, Working Memory, Processing Speed — each corresponding to a broad CHC ability. Confirmatory factor analysis (your soft prerequisite) is used to verify that the hypothesized factor structure fits the actual response data, linking theory to measurement.

Once items are developed and factor structure confirmed, **norming** is the critical next step. Raw scores on intelligence tests are meaningless without a reference distribution. The norming process involves administering the battery to a large, carefully stratified sample (matched to census demographics by age, sex, education, ethnicity, and region) and converting raw scores to **standardized scores** with a mean of 100 and standard deviation of 15 — the familiar IQ metric. These are **deviation IQ scores**: not a ratio of mental age to chronological age, but a statement about where an individual falls in the contemporary age-matched distribution. A score of 115 means one standard deviation above the mean for one's age group, not that one has the mental abilities of a 15-year-old.

Score interpretation requires construct validity — your soft prerequisite. A valid intelligence battery must demonstrate convergent validity (correlating with other measures of intellectual ability), discriminant validity (not collapsing into a measure of personality or motivation), and predictive validity (correlating with real-world outcomes like academic achievement and occupational success). The **Flynn effect** — the secular rise in raw IQ scores of about 3 points per decade over the 20th century — illustrates why test renorming is periodic and important: a test normed in 1980 and used in 2010 would systematically overestimate intelligence relative to current norms. Each revision of the WAIS or Stanford-Binet re-establishes the normative baseline, updates item content, and revisits the factor structure in light of new theoretical and empirical advances.
