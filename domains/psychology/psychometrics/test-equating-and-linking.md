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
stage: expert
status: validated
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

## Questions

```yaml
- question: "A testing program uses equipercentile equating, but the group that took Form B happened to consist of significantly higher-ability students than the group that took Form A. What is the most likely consequence?"
  type: multiple-choice
  options:
    - "The equating will be unaffected, because equipercentile equating is robust to group ability differences by design"
    - "The equating will be biased — scores will be adjusted as if form differences account for all the score differences, when in fact ability differences are also contributing"
    - "The equating will compensate correctly because it matches percentile ranks, which are not affected by the ability level of the group"
    - "The equating will fail entirely and produce no equated scores, since the groups are not equivalent"
  answer: 1
  explanation: "Equipercentile equating — and linear equating — assume that the groups taking the two forms are equivalent in ability, so that any score distribution differences reflect form differences, not ability differences. If Group B is higher-ability, their higher average score on Form B looks like Form B is easier, when actually the group was just better. The equating will overcorrect, penalizing Form B scores by more than is justified. The fundamental assumption violation leads to systematic bias, not equating failure or robustness."

- question: "What is the key advantage of IRT-based equating with anchor items over linear or equipercentile equating?"
  type: multiple-choice
  options:
    - "It requires smaller sample sizes and works better when only a few items overlap between forms"
    - "It explicitly separates person ability from item difficulty on a common scale, so form differences can be detected and corrected even when groups are not equivalent in ability"
    - "It always produces the same equated scores as linear equating, but with less computation"
    - "It eliminates the need for anchor items by using the full item response patterns from both forms simultaneously"
  answer: 1
  explanation: "IRT's scale-invariance property is precisely what makes IRT equating powerful: in a well-fitting model, item parameters and person abilities are on the same underlying metric regardless of who took which items. Anchor items provide reference points that let us put two separate parameter estimates onto one common scale. This means IRT equating can handle non-equivalent groups, because the model separates what the person brought (ability) from what the form presented (difficulty). Linear and equipercentile methods cannot make this separation — they require equivalent groups."

- question: "Equipercentile equating can detect non-linear relationships between test forms that linear equating would miss."
  type: true-false
  answer: true
  explanation: "Linear equating applies a single mean-and-SD transformation, which can only adjust for forms that differ uniformly across the score range. If Form B is harder at the low end but easier at the high end (a non-linear relationship), linear equating applies one average correction that is too small in some regions and too large in others. Equipercentile equating matches each score point separately by its percentile rank, so it can track whatever shape the relationship takes. The tradeoff is that it requires larger samples to estimate the full score distribution reliably."

- question: "If two independent teams apply different equating methods to the same pair of test forms using the same data, they should arrive at essentially identical equated scores — equating has a unique correct answer."
  type: true-false
  answer: false
  explanation: "Different equating methods rest on different assumptions and can yield meaningfully different equated scores, especially when those assumptions are not fully met. Linear equating assumes a linear relationship between forms; equipercentile allows non-linearity; IRT-based equating assumes the IRT model fits well. When the assumptions of one method are violated, its equated scores diverge from methods with different assumptions. There is no method-independent 'correct' equated score to converge on — the choice of method is consequential, not merely computational."

- question: "Why is it insufficient to equate two test forms using samples from groups with very different average ability levels, even if those samples are large?"
  type: short-answer
  answer: "Equating methods assume that score differences between forms reflect form differences (difficulty, item characteristics), not differences between the groups of test-takers. If the groups are not equivalent in ability, score differences on the two forms confound form difficulty with group ability. There is no way to statistically separate how much of the score gap is due to one form being harder versus one group being more skilled. Large samples reduce sampling error but cannot solve this identification problem — you need equivalent groups (or IRT's explicit ability-difficulty separation) to make valid equating inferences."
  explanation: "This is the fundamental equating assumption, and violating it is a design flaw that no amount of data can fix. Equating is an inference: 'this score difference is due to form differences.' That inference requires that the groups taking the forms are similar in ability, so ability is not a confound. When they aren't, the equating assigns form-based corrections for what is actually a group-based difference, producing scores that are systematically non-comparable — the opposite of what equating is supposed to achieve."
```

## Explainer

From **classical test theory** you know that observed scores reflect true score plus error, and that a test's mean and standard deviation depend on both the ability of the test-takers and the difficulty of the items. From **item response theory** you know that item parameters and person ability can be placed on a common scale that is, in principle, independent of the particular sample tested. Test equating is where these ideas meet a practical problem that arises in every large-scale testing program: different test forms cannot be identical (that would allow answer-sharing), but they must produce comparable scores. An examinee who happened to take an easier form should not be advantaged over one who took a harder form — unless the scores are adjusted to account for form differences.

The simplest approach is **linear equating**, which assumes scores on two forms are related by a linear transformation. If Form A has a mean of 50 and SD of 10, and Form B has a mean of 55 and SD of 9, every Form B score is converted to the Form A scale using mean and standard deviation adjustment: the score 55 on Form B (the mean) maps to 50 on Form A (the mean); a score one SD above the mean on Form B maps to one SD above the mean on Form A. This preserves rank order and adjusts for mean and spread differences, but it works well only when the two forms are roughly parallel — when the relationship between forms really is approximately linear across the whole score range.

**Equipercentile equating** relaxes this assumption by matching scores based on their percentile ranks in a common population. A Form B score at the 75th percentile is equated to the Form A score that also falls at the 75th percentile, regardless of whether a linear transformation would produce the same result. This handles non-linear relationships between forms but requires large samples to estimate percentile distributions accurately, and it can produce irregular equating functions that need statistical smoothing. The key assumption is that both groups of test-takers are sampled from equivalent ability distributions — if one group was systematically higher-ability, the equating will be biased.

**IRT-based equating** exploits the scale-invariance property of IRT models: in a well-fitting model, item parameter estimates and person ability estimates are on the same underlying metric regardless of which specific items were administered. When two test forms share **anchor items** — items that appear on both forms and serve as a common reference — IRT equating places both forms on a single ability scale by using the anchor items as reference points. You estimate item parameters for each form separately, then use the anchor items (whose parameters should be the same on both forms) to derive a linear transformation that puts Form B's parameters onto Form A's scale. This approach is more powerful than linear or equipercentile equating because it explicitly separates item difficulty from person ability, but it requires the IRT model to fit well and adequate sample sizes for stable item parameter estimation.

The practical choice among methods depends on design: do you have random equivalent groups or a common-item anchor? How large are your samples? Are the forms roughly parallel in difficulty? A mismatch between equating design and method is a common source of non-comparability. Throughout, the goal is the same: ensure that a score of, say, 68 means the same level of proficiency regardless of which form the examinee took — so that form assignment becomes genuinely irrelevant to the score's interpretation.
