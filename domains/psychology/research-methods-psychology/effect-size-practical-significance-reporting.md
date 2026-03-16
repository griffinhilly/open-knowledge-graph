---
id: effect-size-practical-significance-reporting
title: Effect Sizes, Practical Significance, and Results Reporting
domain: psychology
course: research-methods-psychology
prerequisites:
- id: statistical-inference-significance-testing
  type: hard
builds-toward:
- qualitative-analysis-synthesis-meta-ethnography
tags:
- effect-size
- practical-significance
- result-reporting
- interpretation
stage: abstract-reasoning
status: draft
---

# Effect Sizes, Practical Significance, and Results Reporting

## Core Idea
Effect sizes (Cohen's d, r, eta-squared) quantify the magnitude of differences or relationships. They are comparable across studies and samples, making them crucial for meta-analysis and interpretation. Practical significance considers both statistical significance and effect magnitude: a statistically significant but negligible effect may be theoretically uninteresting. Reporting both p-values and effect sizes with confidence intervals enables full understanding.

## How It's Best Learned
Calculate and interpret effect sizes for published studies. Compare studies with identical p-values but different effect sizes. Discuss when small effects are scientifically valuable and when large effects are expected.

## Common Misconceptions
- Larger p-values indicate larger effects; - Effect sizes are only meaningful for 'significant' results; - Standardized effect sizes apply equally to all contexts; - Confidence intervals and effect sizes communicate equivalent information.

## Explainer

From your study of statistical inference and significance testing, you know that a p-value answers a specific and narrow question: given that the null hypothesis is true, how probable is a result at least as extreme as the one observed? A small p-value tells you the result is unlikely under the null—that's evidence something real is happening. What it does not tell you is *how much* is happening. Two studies can both achieve p < 0.001 while one shows a large, clinically meaningful difference and the other shows a difference so small it has no practical consequence whatsoever. This is the gap that **effect sizes** fill.

An **effect size** is a standardized, scale-free measure of the magnitude of a relationship or difference. The most common in psychology is **Cohen's d**, which expresses a mean difference between two groups in standard deviation units: d = (M₁ − M₂) / SD_pooled. A d of 0.2 means the groups differ by two-tenths of a standard deviation—a small effect. A d of 0.8 means they differ by nearly a full standard deviation—a large effect by conventional benchmarks. Cohen's d is interpretable across studies because it removes the original measurement scale: a drug that raises test scores by 3 points on a 100-point scale and a drug that raises them by 6 points on a 200-point scale could have the same d if the SDs scale proportionally. **Pearson's r** (the correlation coefficient) also serves as an effect size for relationships, and **eta-squared (η²)** describes the proportion of variance explained in ANOVA designs—analogous to R² in regression.

The critical conceptual point is that statistical significance and effect size are logically independent. A tiny effect can be highly significant with a large sample (because significance depends on sample size), and a large effect can fail to reach significance with a small sample. In a study of thousands of participants, you might detect a statistically significant difference in IQ between people born in January versus July—but if d = 0.03, this result has essentially no practical meaning. Conversely, a clinical trial with only 20 patients might find a 40% reduction in symptoms (a massive effect) that fails to reach p < 0.05 purely due to low power. The p-value answers "Is this real?" Effect size answers "Does it matter?"

Reporting standards in psychology have shifted toward requiring both, along with **confidence intervals**. A well-reported result looks like: "The intervention group outperformed the control group by 8.4 points (d = 0.61, 95% CI [0.32, 0.90], p = .003)." This tells the reader that the effect is likely real (significant), medium-large in magnitude (d = 0.61), and the plausible range of the true effect excludes zero (the CI doesn't include d = 0). Confidence intervals around effect sizes are particularly valuable because they communicate both the estimate and the precision of that estimate—a very wide CI around a large d signals that the true effect size is uncertain despite the observed result. Together, p-values, effect sizes, and confidence intervals give a complete picture that neither statistic alone provides, and this complete picture is what modern psychological science demands.
