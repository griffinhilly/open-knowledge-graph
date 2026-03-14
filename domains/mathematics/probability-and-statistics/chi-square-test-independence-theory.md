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
