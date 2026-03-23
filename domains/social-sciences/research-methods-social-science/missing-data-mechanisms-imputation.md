---
id: missing-data-mechanisms-imputation
title: 'Missing Data: Mechanisms, Diagnostics, and Multiple Imputation'
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: regression-diagnostics-assumption-violations
  type: hard
- id: probability-mass-functions
  type: soft
- id: conditional-probability
  type: soft
- id: probability-axioms
  type: hard
tags:
- missing-data
- imputation
- mcar-mar
- multiple-imputation
stage: expert
status: validated
---

# Missing Data: Mechanisms, Diagnostics, and Multiple Imputation

## Core Idea
Missing data is ubiquitous in social research. Data can be missing completely at random (MCAR), at random given observed data (MAR), or not at random (MNAR). Each mechanism requires different handling. Multiple imputation under MAR preserves uncertainty and produces valid inference.

## Questions

```yaml
- question: "A study finds that older respondents systematically skip the income question, but among respondents of the same age, whether income is reported is unrelated to the respondent's actual income level. Which missing data mechanism applies?"
  type: multiple-choice
  options:
    - "MCAR — missingness is random since it is unrelated to actual income values"
    - "MAR — missingness depends on an observed variable (age) but not on the missing values themselves"
    - "MNAR — missingness depends on the unobserved income values"
    - "Cannot be classified without knowing the percentage of missing cases"
  answer: 1
  explanation: "MAR (Missing at Random) means missingness depends on observed variables but not on the unobserved values themselves. Here, age (observed) predicts missingness, but conditional on age, actual income does not predict its own missingness. MCAR would require missingness to be unrelated to any variable — which it isn't (age predicts it). MNAR would require that high (or low) earners skip the question because of their income level — but the problem states that conditional on age, this doesn't happen. Correctly diagnosing the mechanism determines which analysis strategy is valid."

- question: "A researcher uses single imputation — replacing each missing value with its predicted mean from a regression model — to handle MAR data before running the main analysis. What is the primary statistical problem with this approach?"
  type: multiple-choice
  options:
    - "Single imputation produces biased point estimates because it assumes MCAR"
    - "It artificially inflates precision by treating imputed values as if they were known observations, producing standard errors that are too narrow"
    - "It can only handle MNAR data and is inappropriate for MAR"
    - "The regression model used for imputation must match the analysis model exactly, which is rarely achievable"
  answer: 1
  explanation: "Single imputation's core flaw is not bias in point estimates — a well-specified imputation model can produce unbiased estimates — but the treatment of imputed values as known observations. After imputation, analysis proceeds as if all n values were observed. But the imputed values are uncertain guesses, not measurements. This artificial certainty produces standard errors that are too small, confidence intervals too narrow, and p-values too significant. Multiple imputation corrects this by generating m plausible complete datasets and using Rubin's rules to pool results in a way that reflects the extra uncertainty introduced by missingness itself."

- question: "Whether data is MCAR or MAR can be definitively determined by statistical tests comparing cases with and without missing values on observed variables."
  type: true-false
  answer: false
  explanation: "Statistical tests can detect departures from MCAR — if cases with missing values differ systematically from cases without on observed variables, MCAR is violated. But distinguishing MAR from MNAR is fundamentally unidentifiable from the observed data alone, because the relevant information (how missingness relates to the missing values themselves) is by definition absent. To know whether high earners skip the income question because they earn a lot (MNAR), you'd need their income — which is missing. Distinguishing MAR from MNAR requires subject-matter knowledge about why data goes missing, not statistical tests."

- question: "Under MCAR, listwise deletion (dropping all cases with any missing values) produces unbiased parameter estimates, though with reduced statistical power."
  type: true-false
  answer: true
  explanation: "MCAR means the probability of missingness is unrelated to any variable in the dataset, observed or unobserved. Under MCAR, complete cases are a random subset of the full sample — so they represent the population without systematic distortion, and estimates are unbiased. Power is reduced because sample size is smaller. Under MAR or MNAR, however, the complete cases are not a random subset — they differ systematically from incomplete cases in ways that bias the estimates. This is why the mechanism, not the amount of missing data, determines whether listwise deletion is acceptable."

- question: "Explain why the mechanism of missingness (MCAR, MAR, MNAR) matters more than the percentage of missing data for choosing an appropriate analysis strategy."
  type: short-answer
  answer: "The mechanism determines whether missingness is informative. Under MCAR, missing cases are a random subset, so analysis on complete cases is unbiased — even 30% missingness is manageable. Under MNAR, even 5% missing data can severely bias estimates because the missingness carries information about the very values being analyzed (e.g., high earners skipping the income question means observed incomes systematically underrepresent high earners). No amount of data or sophisticated analysis fully corrects for MNAR. The appropriate method — listwise deletion, multiple imputation, sensitivity analysis — follows from the mechanism, not from the count of missing cells."
  explanation: "This is the central conceptual shift in modern missing data methodology: from treating missingness as a data quantity problem (how much is missing?) to a causal process problem (why is it missing?). A small percentage of MNAR data can invalidate an entire study; a large percentage of MCAR data is merely inconvenient. Understanding the missing data mechanism requires thinking about the data-generating process — a substantive, theoretical question, not a statistical one. This is why subject-matter expertise about survey design, participant attrition, and measurement processes is essential to missing data analysis."
```

## Explainer

Your prerequisite on regression diagnostics introduced the idea that real data often violates the clean assumptions of standard models. Missing data is one of the most common and consequential violations: when observations are incomplete, naive analysis can produce severely biased results. The key insight is that *how* data goes missing matters as much as *how much* is missing. The three mechanisms form a hierarchy of severity, and each implies a different treatment strategy.

**Missing Completely at Random (MCAR)** is the most benign: whether a value is missing is entirely unrelated to any variable in the dataset, observed or unobserved. A random lab malfunction destroying 5% of samples is MCAR. Listwise deletion — dropping all rows with any missing value — produces unbiased estimates under MCAR, though it reduces statistical power. **Missing at Random (MAR)** is more realistic and more insidious: missingness depends on observed variables but not on the missing values themselves. Older survey respondents might be less likely to report income, but their missingness depends on age (observed), not their actual income. Here, listwise deletion produces biased estimates because it drops a systematically non-random subset of observations. Your conditional probability prerequisite explains why: the dropped observations don't represent a random draw from the population, so the remaining sample is distorted. **Missing Not at Random (MNAR)** is the worst case: missingness depends on the unobserved value itself. High earners skip the income question *because* they earn a lot — the missingness carries information about the very thing you're trying to measure. No standard imputation method can fully correct for MNAR.

**Multiple imputation** is the principled solution for MAR data. Rather than substituting a single "best guess" for each missing value — a strategy called single imputation that understates uncertainty — multiple imputation generates several complete datasets, each with plausible imputed values drawn from a probability model that conditions on all observed data. This is where your probability foundations are essential: each imputed value is a draw from the conditional distribution of the missing variable given everything observed. The analysis model is run on each imputed dataset separately, and results are combined using **Rubin's rules**, which pool point estimates and inflate standard errors to reflect the uncertainty introduced by missingness itself. The final confidence intervals are appropriately wider than they would be with complete data — which is honest, because information was genuinely lost.

Diagnosing the missing data mechanism is crucial before choosing a method, but it is partly untestable. You can detect departures from MCAR by comparing cases with and without missing values on observed variables — if the two groups differ systematically, MCAR is violated. But distinguishing MAR from MNAR is fundamentally unidentifiable from the observed data alone, because the relevant information is by definition missing. Subject-matter knowledge about why data might be missing — survey design, participant attrition, measurement error patterns — is the primary resource here. Sensitivity analyses that model different MNAR scenarios and check how much conclusions change are the best available defense against overconfident inference when the missing data mechanism is uncertain.
