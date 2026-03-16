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
builds-toward:
- goodness-of-fit-test
tags:
- chi-square
- independence
stage: formal-systems
status: draft
---

# Chi-Square Test for Independence

## Core Idea
Tests independence of categorical variables. χ²=Σ(Observed−Expected)²/Expected with (rows−1)(cols−1) df. Expected counts computed under independence. Requires all expected counts≥5. Large χ² indicates association.

## Explainer

The chi-square test for independence asks a specific question about a **contingency table**: are two categorical variables statistically independent, or does knowing one variable's category tell you something about the other? For example, does a person's smoking status (yes/no) relate to their disease outcome (sick/well)? Independence — your null hypothesis — has a precise probabilistic meaning from your **hypothesis testing framework**: P(A and B) = P(A) · P(B) for all categories A and B. The test constructs a statistic that measures how far the observed data deviates from what independence would predict.

The expected counts under independence are computed using a key formula: for a cell in row i and column j of an r × c table, the **expected count** is E_{ij} = (row i total) × (column j total) / (grand total). This formula follows directly from the independence definition. If smoking and disease are independent, the probability of being a smoking non-sick person should be P(smoking) × P(non-sick) — and multiplying by n gives the expected count. Compare this to the observed count O_{ij} (what you actually see) for every cell. If the two variables are truly independent, observed and expected counts should be close.

The test statistic aggregates these cell-by-cell discrepancies: χ² = Σ (O_{ij} − E_{ij})² / E_{ij}. The denominator E_{ij} standardizes the squared difference — a discrepancy of 5 in a cell with expected count 10 is very different from a discrepancy of 5 in a cell with expected count 1000. Large values of χ² signal systematic association between the variables. Under the null hypothesis of independence, this statistic follows approximately a **chi-square distribution** (your prerequisite) with (r − 1)(c − 1) degrees of freedom. The degrees of freedom count how many cells are free to vary: once the marginal totals are fixed, specifying (r−1)(c−1) cells determines the entire table.

Two practical requirements matter. First, all expected counts should be at least 5 — below this, the chi-square approximation deteriorates and Fisher's exact test is preferred. Second, the chi-square test detects association but says nothing about its direction or magnitude. A statistically significant result means the pattern of association is unlikely under independence; a large table can have significant chi-square with a very weak practical association. For effect size, pair the test with Cramér's V: V = √(χ² / (n · min(r−1, c−1))), which ranges from 0 (no association) to 1 (perfect association). The test gives the p-value; Cramér's V gives the strength.
