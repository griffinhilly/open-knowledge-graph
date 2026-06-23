---
id: chi-square-test
title: Chi-Square Test
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: hypothesis-testing-fundamentals
  type: hard
- id: chi-square-distribution-theory
  type: hard
- id: frequency-distributions-and-tables
  type: soft
- id: hypothesis-testing-framework-theory
  type: hard
tags:
- chi-square
- goodness-of-fit
- independence
stage: formal-systems
status: validated
---

# Chi-Square Test

## Core Idea
The chi-square test assesses whether observed frequencies in categories differ significantly from expected frequencies under a null hypothesis. For a goodness-of-fit test, it compares observed category frequencies to theoretical (expected) frequencies. For a test of independence, it tests whether two categorical variables are independent in a contingency table. The test statistic is χ² = Σ(Observed - Expected)²/Expected, which follows a chi-square distribution when the null hypothesis is true and expected frequencies are sufficiently large (typically ≥ 5).

## How It's Best Learned
Set up null hypotheses for goodness-of-fit scenarios (coin fairness, six-sided die). Create contingency tables and test independence. Verify that expected frequencies meet assumptions.

## Common Misconceptions
Using chi-square with expected frequencies < 5. Confusing goodness-of-fit with independence tests. Forgetting that small p-values indicate deviation from the null, not confirmation of hypotheses. Thinking chi-square tests directionality (they don't).

## Questions

```yaml
- question: "A researcher rolls a fair die 120 times and gets counts {18, 22, 19, 21, 20, 20}. She computes χ² = 0.7 and p = 0.98. Her classmate says: 'A p-value that high means the test confirmed the die is fair — it proved H₀.' What is wrong with this interpretation?"
  type: multiple-choice
  options:
    - "Nothing — a p-value near 1.0 is the standard way to confirm a null hypothesis in chi-square testing"
    - "A high p-value means the data are consistent with H₀, but this is not the same as proving H₀ is true — chi-square tests can only provide evidence against a null, not confirm it"
    - "The sample size of 120 is too large for chi-square — smaller samples are required"
    - "Chi-square cannot test whether a die is fair; it can only test independence"
  answer: 1
  explanation: "Hypothesis testing logic is asymmetric: a small p-value provides evidence against H₀, but a large p-value only means the data are not inconsistent with H₀ — it does not confirm H₀. A p = 0.98 means the observed counts are very close to what a fair die would produce; but many other dice (slightly biased ones) could produce the same data. Failing to reject H₀ is not the same as accepting it. This is one of the most important and persistent misconceptions in applied statistics."

- question: "A chi-square test of independence returns p = 0.008 for the relationship between neighborhood income level and access to fresh produce (three categories: high/moderate/low). What can you correctly conclude from this result alone?"
  type: multiple-choice
  options:
    - "Higher income causes better produce access — the causal direction is confirmed"
    - "There is a statistically significant association between income level and produce access, but the test does not identify which income categories drive the pattern or in what direction"
    - "8% of survey respondents reported limited produce access regardless of income"
    - "Produce access is at least 8% lower in low-income neighborhoods than high-income ones"
  answer: 1
  explanation: "Chi-square tests of independence detect whether an association exists — not its direction, magnitude, or cause. A p = 0.008 tells you the cell frequencies deviate significantly from what independent variables would produce, but not which cells are driving the deviation. To understand direction and pattern, you examine the individual (O−E)²/E contributions per cell after rejecting H₀. Causal inference requires study design beyond the test statistic."

- question: "A chi-square test always rejects H₀ for very large values of the test statistic, and the test statistic is always non-negative."
  type: true-false
  answer: true
  explanation: "Both parts are correct. The test statistic χ² = Σ(O−E)²/E is a sum of squared terms divided by positive denominators — it cannot be negative. It equals zero only when every observed count exactly matches the expected count, indicating perfect agreement with H₀. The test is one-tailed: we only reject H₀ when χ² is large (data far from H₀ predictions). There is no 'too low' rejection region, because a very small χ² just means the data fit H₀ well."

- question: "When some expected cell counts in a chi-square test are below 5, the test statistic becomes larger, making the test more conservative and less likely to produce false positives."
  type: true-false
  answer: false
  explanation: "The problem with small expected counts is not conservatism — it is that the chi-square distribution is no longer a reliable approximation to the true null distribution of the test statistic. With sparse cells, p-values become unreliable in unpredictable directions (they can be too small or too large). The conventional remedy is to use Fisher's exact test (for 2×2 tables) or to combine sparse categories. The minimum expected count of 5 is a rule of thumb for when the chi-square approximation holds."

- question: "Explain why the chi-square test statistic χ² = Σ(O−E)²/E is always non-negative and what it means conceptually when χ² is close to zero."
  type: short-answer
  answer: "Each term (O−E)²/E squares the discrepancy between observed and expected counts, making every term non-negative, and sums them — so the total cannot be negative. When χ² is close to zero, every category's observed count is very close to its expected count under H₀, meaning the data look almost exactly like what H₀ predicts. This provides no evidence against H₀ — the data fit the null model well. χ² grows as any category's observed count deviates from expected, accumulating evidence across all categories that the data are inconsistent with H₀."
  explanation: "The squaring serves two purposes: it makes all terms non-negative (so deviations in opposite directions don't cancel out) and it penalizes large deviations more than small ones. Dividing by E normalizes each term — a deviation of 10 from an expected count of 20 is more striking than a deviation of 10 from an expected count of 1,000."
```

## Explainer

From hypothesis testing, you know the general structure: state H₀, compute a test statistic designed to be large when H₀ is wrong, compare to a null distribution, and reject if the result is unlikely under H₀. The chi-square test applies this structure to **categorical data** — outcomes that fall into labeled buckets rather than on a numerical scale. The test statistic χ² = Σ(O − E)²/E accumulates evidence by comparing observed counts O to expected counts E in each category. Each term (O−E)²/E is zero when observations match expectations perfectly and grows as the discrepancy increases. The total χ² measures the overall gap between what you saw and what H₀ predicts.

The **goodness-of-fit** test asks whether your data came from a specific distribution. Example: you roll a six-sided die 120 times. Under H₀ (fair die), you expect E = 20 for each face. If your observed counts are 15, 22, 18, 25, 17, 23, compute χ² = (15−20)²/20 + (22−20)²/20 + ... for all six faces. The degrees of freedom are k−1 = 5 (you lose one degree of freedom because the counts must sum to 120). Compare χ² to a chi-square distribution with 5 degrees of freedom. A large value means the die is likely unfair; a small value means the data is consistent with fairness.

The **test of independence** asks whether two categorical variables are related. Suppose you survey 200 people and record gender (M/F) and preference (Product A/B/C). You arrange data in a 2×3 contingency table. Under H₀ (independence), the expected count in each cell is (row total × column total)/grand total — the count you would expect if gender and preference had nothing to do with each other. Compute χ² summing (O−E)²/E over all 6 cells, with degrees of freedom (r−1)(c−1) = (2−1)(3−1) = 2. The same test statistic, different null hypothesis and degrees of freedom.

One critical assumption underlies both tests: expected counts in every cell must be at least 5. When expected counts are small, the chi-square approximation to the null distribution breaks down, p-values become unreliable, and you need alternatives such as Fisher's exact test. Also note that chi-square tests are always one-tailed (you only reject for large χ²) and do not indicate *direction* of association — they detect that a difference exists, but not which categories deviate most. For that, examine the individual (O−E)²/E terms after rejecting H₀.
