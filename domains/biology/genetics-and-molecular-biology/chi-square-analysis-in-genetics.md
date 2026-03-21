---
id: chi-square-analysis-in-genetics
title: Chi-Square Analysis in Genetic Data
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: mendelian-genetics
  type: hard
- id: genetic-recombination-and-linkage-mapping
  type: soft
- id: chi-square-test
  type: hard
- id: statistical-methods-analytical
  type: soft
builds-toward:
- quantitative-genetics-and-polygenic-traits
tags:
- chi-square-test
- goodness-of-fit
- expected-ratio
- degrees-of-freedom
stage: advanced
status: draft
---

# Chi-Square Analysis in Genetic Data

## Core Idea
Chi-square (χ²) tests determine whether observed genetic ratios significantly differ from predicted Mendelian expectations. The test compares observed versus expected frequencies for each class, computing χ² = Σ((observed - expected)²/expected). The χ² statistic is compared against a critical value for the degrees of freedom (number of classes minus 1); a χ² value above the critical value indicates statistically significant deviation from the hypothesis. Chi-square analysis is essential for validating genetic models, detecting non-Mendelian patterns, identifying hidden genetic interactions, and confirming linkage hypotheses. Large deviations may reveal unequal viability of genotypic classes, incomplete penetrance, or linked genes.

## Questions

```yaml
- question: "A student performs a monohybrid cross and counts 240 round and 60 wrinkled peas (n = 300). A 3:1 ratio predicts 225 round and 75 wrinkled. χ² = (240−225)²/225 + (60−75)²/75 = 1.00 + 3.00 = 4.00. With 1 degree of freedom, the critical value at p = 0.05 is 3.84. What should the student conclude?"
  type: multiple-choice
  options:
    - "The data fit the 3:1 ratio because the observed counts are visually close to expected"
    - "The data statistically deviate from the 3:1 ratio, suggesting the simple Mendelian model may be insufficient"
    - "A χ² of 4.00 is too small to be meaningful; far more data are needed before any conclusion"
    - "The hypothesis is disproven because expected values differ from observed values"
  answer: 1
  explanation: "The χ² value (4.00) exceeds the critical value (3.84) at p = 0.05 with 1 df, so we reject the null hypothesis that the data fit a 3:1 ratio. Option A is the classic intuitive error: 'close enough by eye' is not a statistical standard. Option D is too strong — a significant chi-square doesn't disprove the hypothesis, it means the deviations exceed what random sampling variation explains at this significance level, warranting further investigation. Option C misunderstands how chi-square works — the value is always evaluated against the critical value, not in absolute terms."

- question: "After failing to reject a 9:3:3:1 ratio in a chi-square test, a student writes: 'The chi-square test proves that these two genes assort independently.' What is wrong with this conclusion?"
  type: multiple-choice
  options:
    - "The student should have used a t-test for genetic ratio data"
    - "Failing to reject the null only shows the data are consistent with the model — it does not prove the model is correct"
    - "Chi-square cannot be applied to dihybrid crosses with four phenotypic classes"
    - "The conclusion is correct — a non-significant result means the hypothesis is confirmed"
  answer: 1
  explanation: "A non-significant chi-square means the observed deviations are within the range expected from random sampling variation if the model were true. Many alternative models might also fit the same data — this is especially true with small samples where statistical power is low. The correct phrasing is: 'The data are consistent with independent assortment' or 'We failed to find evidence against the hypothesis of independent assortment.' Failing to falsify ≠ proving. This is the distinction between failing to reject H₀ and confirming H₀."

- question: "In a chi-square goodness-of-fit test for a dihybrid cross producing four phenotypic classes, the correct degrees of freedom is 3."
  type: true-false
  answer: true
  explanation: "Degrees of freedom = number of phenotypic classes − 1 = 4 − 1 = 3. The subtraction of 1 accounts for the constraint that expected frequencies must sum to the observed total N (one degree of freedom is 'used up' fixing the total). With 3 df, the critical value at p = 0.05 is 7.82 — substantially higher than the 3.84 for a monohybrid (1 df) test. More phenotypic classes allow more ways for data to deviate from expectations, so a higher threshold is needed to distinguish real deviations from chance variation across more categories."

- question: "A statistically significant chi-square result in a genetics experiment identifies which specific alternative mechanism — epistasis, linkage, or differential viability — is responsible for the deviation from expected ratios."
  type: true-false
  answer: false
  explanation: "Chi-square is a goodness-of-fit test: it tells you only whether observed and expected frequencies differ more than sampling chance explains. It does not identify *why* they differ. A significant deviation from 9:3:3:1 could reflect epistasis (giving modified ratios like 12:3:1 or 9:7), linkage reducing recombinant class frequencies, differential viability of certain genotypes, or even systematic data collection errors. The chi-square flags the problem and tells you your simple model is wrong; identifying the correct alternative requires additional crosses, different experimental designs, and biological reasoning."

- question: "Why does increasing sample size generally improve the usefulness of chi-square analysis in genetics? What statistical property does a larger sample improve?"
  type: short-answer
  answer: "Larger sample sizes increase statistical power — the probability of detecting a real deviation from the expected ratio when one actually exists. With small samples, random sampling variation is large relative to expected counts, so even substantial proportional deviations may not produce a χ² value above the critical threshold. The same proportional deviation produces a larger χ² with a larger sample because the expected values (and therefore the denominators in each (O−E)²/E term) scale with sample size while the proportional deviations remain constant, causing the total χ² to increase. Equivalently: small samples can both fail to detect genuine non-Mendelian patterns (false negatives) and fail to exclude chance deviations (low precision). This is also why Mendel's published data — which fit expected ratios almost perfectly with few apparent sampling deviations — have been questioned statistically: with his sample sizes, some random deviation was expected, and suspiciously good fits may indicate selective reporting."
```

## Explainer

From Mendelian genetics, you know that a monohybrid cross between two heterozygotes (Aa × Aa) should produce a 3:1 phenotypic ratio. But in practice, if you cross two heterozygous pea plants and count 850 round seeds and 150 wrinkled seeds, is that close enough to 3:1 (which predicts 750:250), or is something else going on? Your eyes might say "close enough" or "that's off," but genetics demands a formal, reproducible way to decide. The **chi-square test** provides exactly this — a statistical method to determine whether deviations from expected ratios are within the range of normal sampling variation or too large to be explained by chance alone.

The calculation is straightforward. For each phenotypic class, you compute (observed − expected)² / expected, then sum these values across all classes. In the example above, χ² = (850−750)²/750 + (150−250)²/250 = 13.33 + 40.00 = 53.33. The **degrees of freedom** equal the number of classes minus one — here, 2 classes minus 1 = 1 degree of freedom. You then compare your χ² value to a critical value from a chi-square distribution table. At the conventional p = 0.05 significance level with 1 degree of freedom, the critical value is 3.84. Since 53.33 far exceeds 3.84, you reject the null hypothesis that the data fit a 3:1 ratio. Something beyond simple Mendelian segregation is at work.

What makes this test so powerful in genetics is what a significant result *means* biologically. When observed ratios deviate significantly from Mendelian expectations, it becomes a clue pointing toward deeper genetic phenomena. A dihybrid cross yielding a 9:3:3:1 ratio confirms independent assortment, but a significant deviation from 9:3:3:1 might reveal **epistasis** (one gene masking another), **linkage** (genes on the same chromosome not assorting independently), or **differential viability** (some genotypes dying before being counted). The chi-square test does not tell you *which* alternative explanation is correct — it tells you that your simple model is insufficient and further investigation is needed.

A common pitfall is misinterpreting a non-significant result. Failing to reject the null hypothesis does not prove that your genetic model is correct — it means that your data are *consistent* with the model. With small sample sizes, even substantial deviations from expected ratios may not reach statistical significance because random sampling variation is large. This is why genetics experiments benefit from large sample sizes: they give the chi-square test enough statistical power to detect real deviations. Mendel's own data, famously, fit expected ratios almost *too* well — so well that some statisticians have questioned whether the data were selectively reported. The chi-square test thus cuts both ways: suspiciously good fits deserve scrutiny just as much as poor ones.
