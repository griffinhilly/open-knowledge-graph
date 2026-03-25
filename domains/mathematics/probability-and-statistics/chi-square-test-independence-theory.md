---
id: chi-square-test-independence-theory
title: Chi-Square Test for Independence
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: chi-square-distribution-theory
  type: hard
- id: hypothesis-testing-framework-theory
  type: hard
- id: independence-and-mutually-exclusive-events
  type: soft
builds-toward:
- goodness-of-fit-test
tags:
- chi-square
- independence
stage: formal-systems
status: validated
---
# Chi-Square Test for Independence

## Core Idea
Tests independence of categorical variables. χ²=Σ(Observed−Expected)²/Expected with (rows−1)(cols−1) df. Expected counts computed under independence. Requires all expected counts≥5. Large χ² indicates association.

## Questions

```yaml
- question: "A chi-square test of independence on a 2×2 table yields χ² = 12.4, p = .0004. A researcher concludes: 'Smoking strongly causes lung disease.' What is wrong with this conclusion?"
  type: multiple-choice
  options:
    - "Nothing — a significant chi-square result proves a strong causal relationship"
    - "The chi-square test only detects statistical association; it says nothing about direction, magnitude, or causation"
    - "The degrees of freedom for a 2×2 table should be 4, making the test invalid"
    - "A p-value below .001 is too small for chi-square; the test requires p > .01 to be interpretable"
  answer: 1
  explanation: "The chi-square test answers one question: is the pattern of observed counts unlikely under independence? A significant result means association is present — it does not indicate how strong it is (use Cramér's V for effect size), which variable influences which (observational data cannot establish causation), or the practical significance of the relationship. All three claims in the researcher's conclusion — 'strongly,' 'causes,' 'lung disease specifically' — require evidence beyond the chi-square p-value alone."

- question: "A 2×2 contingency table has row totals of 40 and 60, column totals of 50 and 50, and a grand total of 100. What is the expected count for the top-left cell (row 1, column 1) under the null hypothesis of independence?"
  type: multiple-choice
  options:
    - "25 — dividing the grand total equally among all four cells"
    - "20 — multiplying the two column totals and dividing by the grand total"
    - "20 — computed as (row 1 total × column 1 total) / grand total = (40 × 50) / 100"
    - "45 — summing the row 1 and column 1 totals and subtracting the grand total"
  answer: 2
  explanation: "Under independence, P(row 1 AND col 1) = P(row 1) × P(col 1) = (40/100) × (50/100). The expected count is this probability times the grand total: (40/100) × (50/100) × 100 = 40 × 50 / 100 = 20. Options A and B confuse the formula; option D is algebraically unmotivated. The expected count formula E = (row total × column total) / grand total follows directly from the definition of statistical independence."

- question: "In a chi-square test for independence, expected cell counts are computed assuming the two variables are independent."
  type: true-false
  answer: true
  explanation: "Expected counts represent what the data should look like if the null hypothesis (independence) is exactly true. The formula E = (row total × column total) / grand total is derived from the multiplication rule for independent events: P(A and B) = P(A) × P(B). The chi-square statistic then measures how far the observed counts deviate from these independence-predicted expected counts. Large deviations produce large χ² values, which are unlikely under the null hypothesis."

- question: "A statistically significant chi-square test result demonstrates that the association between two categorical variables is practically important and large."
  type: true-false
  answer: false
  explanation: "Statistical significance and practical importance are distinct. With a large enough sample, even a trivially small association will produce a significant chi-square result, because the denominator (expected count) grows with n while tiny systematic deviations accumulate. A highly significant p-value from a study of 10,000 participants might correspond to a Cramér's V of 0.04 — a negligible association by most standards. Always pair the chi-square p-value with an effect size measure like Cramér's V to assess practical magnitude."

- question: "Why must all expected cell counts be at least 5 for the chi-square test to be valid, and what is the recommended alternative when this condition fails?"
  type: short-answer
  answer: "The chi-square test statistic follows the chi-square distribution only approximately — the approximation is derived from the normal approximation to the binomial, which works well when counts are large but breaks down for small expected counts. When expected counts fall below 5, the discrete cell counts do not approximate the continuous chi-square distribution well, making the p-value unreliable (typically anti-conservative — the test appears more significant than it truly is). Fisher's exact test is the recommended alternative: it computes the exact probability of the observed or more extreme table using the hypergeometric distribution, without relying on any large-sample approximation."
  explanation: "The expected count condition is a sample-size adequacy criterion specifically for the chi-square approximation. It is most commonly violated in tables with many cells (large r × c tables) or with very unequal marginal distributions, where some cells receive very few observations under independence."
```

## Explainer

The chi-square test for independence asks a specific question about a **contingency table**: are two categorical variables statistically independent, or does knowing one variable's category tell you something about the other? For example, does a person's smoking status (yes/no) relate to their disease outcome (sick/well)? Independence — your null hypothesis — has a precise probabilistic meaning from your **hypothesis testing framework**: P(A and B) = P(A) · P(B) for all categories A and B. The test constructs a statistic that measures how far the observed data deviates from what independence would predict.

The expected counts under independence are computed using a key formula: for a cell in row i and column j of an r × c table, the **expected count** is E_{ij} = (row i total) × (column j total) / (grand total). This formula follows directly from the independence definition. If smoking and disease are independent, the probability of being a smoking non-sick person should be P(smoking) × P(non-sick) — and multiplying by n gives the expected count. Compare this to the observed count O_{ij} (what you actually see) for every cell. If the two variables are truly independent, observed and expected counts should be close.

The test statistic aggregates these cell-by-cell discrepancies: χ² = Σ (O_{ij} − E_{ij})² / E_{ij}. The denominator E_{ij} standardizes the squared difference — a discrepancy of 5 in a cell with expected count 10 is very different from a discrepancy of 5 in a cell with expected count 1000. Large values of χ² signal systematic association between the variables. Under the null hypothesis of independence, this statistic follows approximately a **chi-square distribution** (your prerequisite) with (r − 1)(c − 1) degrees of freedom. The degrees of freedom count how many cells are free to vary: once the marginal totals are fixed, specifying (r−1)(c−1) cells determines the entire table.

Two practical requirements matter. First, all expected counts should be at least 5 — below this, the chi-square approximation deteriorates and Fisher's exact test is preferred. Second, the chi-square test detects association but says nothing about its direction or magnitude. A statistically significant result means the pattern of association is unlikely under independence; a large table can have significant chi-square with a very weak practical association. For effect size, pair the test with Cramér's V: V = √(χ² / (n · min(r−1, c−1))), which ranges from 0 (no association) to 1 (perfect association). The test gives the p-value; Cramér's V gives the strength.
