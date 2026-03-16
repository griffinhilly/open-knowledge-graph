---
id: test-equating-and-linking
title: Test Equating and Score Linking Methods
domain: psychology
course: psychometrics
prerequisites:
- id: classical-test-theory
  type: hard
- id: item-response-functions
  type: hard
builds-toward:
- anchor-items-and-scale-linking
- score-linking-and-concordance-tables
tags:
- equating
- linking
- scale-transformation
- test-forms
- irt
stage: advanced
status: draft
---

# Test Equating and Score Linking Methods

## Core Idea
Test equating ensures that scores on different test forms are directly comparable by adjusting for form differences in difficulty and other characteristics. Methods include linear equating, equipercentile equating, and IRT-based equating; each makes different assumptions about the relationship between forms and when to use each depends on test design and prerequisite conditions.

## How It's Best Learned
Start with conceptual understanding of why equating is necessary (form differences lead to non-comparable scores). Work through classical linear equating using mean and standard deviation adjustments, then explore equipercentile methods. Finally examine IRT-based equating to understand how ability scales can be linked through anchor items.

## Common Misconceptions
- Assuming all equating methods are interchangeable; they can yield different results when assumptions are violated.
- Equating samples that are not equivalent in ability, which violates the equating assumption.
- Confusing equating (comparable scores) with scaling (transforming to a standard metric).

## Explainer

From **classical test theory** you know that observed scores reflect true score plus error, and that a test's mean and standard deviation depend on both the ability of the test-takers and the difficulty of the items. From **item response theory** you know that item parameters and person ability can be placed on a common scale that is, in principle, independent of the particular sample tested. Test equating is where these ideas meet a practical problem that arises in every large-scale testing program: different test forms cannot be identical (that would allow answer-sharing), but they must produce comparable scores. An examinee who happened to take an easier form should not be advantaged over one who took a harder form — unless the scores are adjusted to account for form differences.

The simplest approach is **linear equating**, which assumes scores on two forms are related by a linear transformation. If Form A has a mean of 50 and SD of 10, and Form B has a mean of 55 and SD of 9, every Form B score is converted to the Form A scale using mean and standard deviation adjustment: the score 55 on Form B (the mean) maps to 50 on Form A (the mean); a score one SD above the mean on Form B maps to one SD above the mean on Form A. This preserves rank order and adjusts for mean and spread differences, but it works well only when the two forms are roughly parallel — when the relationship between forms really is approximately linear across the whole score range.

**Equipercentile equating** relaxes this assumption by matching scores based on their percentile ranks in a common population. A Form B score at the 75th percentile is equated to the Form A score that also falls at the 75th percentile, regardless of whether a linear transformation would produce the same result. This handles non-linear relationships between forms but requires large samples to estimate percentile distributions accurately, and it can produce irregular equating functions that need statistical smoothing. The key assumption is that both groups of test-takers are sampled from equivalent ability distributions — if one group was systematically higher-ability, the equating will be biased.

**IRT-based equating** exploits the scale-invariance property of IRT models: in a well-fitting model, item parameter estimates and person ability estimates are on the same underlying metric regardless of which specific items were administered. When two test forms share **anchor items** — items that appear on both forms and serve as a common reference — IRT equating places both forms on a single ability scale by using the anchor items as reference points. You estimate item parameters for each form separately, then use the anchor items (whose parameters should be the same on both forms) to derive a linear transformation that puts Form B's parameters onto Form A's scale. This approach is more powerful than linear or equipercentile equating because it explicitly separates item difficulty from person ability, but it requires the IRT model to fit well and adequate sample sizes for stable item parameter estimation.

The practical choice among methods depends on design: do you have random equivalent groups or a common-item anchor? How large are your samples? Are the forms roughly parallel in difficulty? A mismatch between equating design and method is a common source of non-comparability. Throughout, the goal is the same: ensure that a score of, say, 68 means the same level of proficiency regardless of which form the examinee took — so that form assignment becomes genuinely irrelevant to the score's interpretation.
