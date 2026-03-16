---
id: chi-square-test
title: Chi-Square Test
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: hypothesis-testing-fundamentals
  type: hard
tags:
- chi-square
- goodness-of-fit
- independence
stage: formal-systems
status: draft
---

# Chi-Square Test

## Core Idea
The chi-square test assesses whether observed frequencies in categories differ significantly from expected frequencies under a null hypothesis. For a goodness-of-fit test, it compares observed category frequencies to theoretical (expected) frequencies. For a test of independence, it tests whether two categorical variables are independent in a contingency table. The test statistic is χ² = Σ(Observed - Expected)²/Expected, which follows a chi-square distribution when the null hypothesis is true and expected frequencies are sufficiently large (typically ≥ 5).

## How It's Best Learned
Set up null hypotheses for goodness-of-fit scenarios (coin fairness, six-sided die). Create contingency tables and test independence. Verify that expected frequencies meet assumptions.

## Common Misconceptions
Using chi-square with expected frequencies < 5. Confusing goodness-of-fit with independence tests. Forgetting that small p-values indicate deviation from the null, not confirmation of hypotheses. Thinking chi-square tests directionality (they don't).

## Explainer

From hypothesis testing, you know the general structure: state H₀, compute a test statistic designed to be large when H₀ is wrong, compare to a null distribution, and reject if the result is unlikely under H₀. The chi-square test applies this structure to **categorical data** — outcomes that fall into labeled buckets rather than on a numerical scale. The test statistic χ² = Σ(O − E)²/E accumulates evidence by comparing observed counts O to expected counts E in each category. Each term (O−E)²/E is zero when observations match expectations perfectly and grows as the discrepancy increases. The total χ² measures the overall gap between what you saw and what H₀ predicts.

The **goodness-of-fit** test asks whether your data came from a specific distribution. Example: you roll a six-sided die 120 times. Under H₀ (fair die), you expect E = 20 for each face. If your observed counts are 15, 22, 18, 25, 17, 23, compute χ² = (15−20)²/20 + (22−20)²/20 + ... for all six faces. The degrees of freedom are k−1 = 5 (you lose one degree of freedom because the counts must sum to 120). Compare χ² to a chi-square distribution with 5 degrees of freedom. A large value means the die is likely unfair; a small value means the data is consistent with fairness.

The **test of independence** asks whether two categorical variables are related. Suppose you survey 200 people and record gender (M/F) and preference (Product A/B/C). You arrange data in a 2×3 contingency table. Under H₀ (independence), the expected count in each cell is (row total × column total)/grand total — the count you would expect if gender and preference had nothing to do with each other. Compute χ² summing (O−E)²/E over all 6 cells, with degrees of freedom (r−1)(c−1) = (2−1)(3−1) = 2. The same test statistic, different null hypothesis and degrees of freedom.

One critical assumption underlies both tests: expected counts in every cell must be at least 5. When expected counts are small, the chi-square approximation to the null distribution breaks down, p-values become unreliable, and you need alternatives such as Fisher's exact test. Also note that chi-square tests are always one-tailed (you only reject for large χ²) and do not indicate *direction* of association — they detect that a difference exists, but not which categories deviate most. For that, examine the individual (O−E)²/E terms after rejecting H₀.
