---
id: frequency-distributions-and-tables
title: Frequency Distributions and Contingency Tables
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: categorical-vs-quantitative-data
  type: hard
builds-toward:
- frequency-tables-histograms
- chi-square-test
tags:
- descriptive-statistics
- frequency
- tables
stage: formal-systems
status: draft
---

# Frequency Distributions and Contingency Tables

## Core Idea
A frequency distribution tabulates how often each value or category occurs. For categorical data, a contingency table shows frequencies for combinations of two variables. These tables reveal patterns in data and form the basis for many statistical tests.

## How It's Best Learned
Create frequency tables from real survey data. Construct contingency tables and calculate marginal and conditional frequencies. Use software to generate these tables efficiently.

## Common Misconceptions
Confusing frequency with relative frequency. Not distinguishing between univariate and bivariate frequency tables. Thinking frequency tables only apply to categorical data (they work for discrete quantitative too).

## Explainer

A **frequency distribution** is simply a systematic count: for each possible value or category in your dataset, how many times does it appear? You already know from your prerequisite work the distinction between categorical variables (like eye color or political party) and quantitative variables (like test scores or height). Frequency tables work for both, though the setup differs slightly — for categorical data you list the categories directly, while for continuous quantitative data you first group values into class intervals (bins) before counting. Either way, the table transforms a raw list of observations into an organized summary of what values occurred and how often.

**Relative frequency** is the count divided by the total number of observations, expressing each category's share as a proportion or percentage. If 30 out of 120 survey respondents prefer option A, the relative frequency is 30/120 = 0.25, or 25%. Relative frequencies are more informative than raw counts when comparing datasets of different sizes, and they sum to exactly 1 (or 100%). **Cumulative frequency** adds frequencies sequentially: what fraction of observations fall below a given value? This cumulative view connects directly to the empirical CDF (cumulative distribution function) you'll encounter in more advanced statistics.

**Contingency tables** (also called two-way or cross-tabulation tables) extend the idea to two categorical variables simultaneously. Each cell shows the frequency (or relative frequency) for one combination of categories — for example, the number of survey respondents who are both female and prefer option A. The row totals and column totals are called **marginal frequencies**, because they sit at the margins of the table and show the distribution of each variable on its own. The individual cells give the **joint frequencies**, showing how the variables relate to each other.

The most important derived quantity is **conditional frequency**: out of all female respondents, what proportion prefer option A? You compute this by dividing the joint frequency (female + option A) by the marginal frequency for that row (all females). Comparing conditional frequencies across rows (or columns) reveals whether two variables are associated — if the conditional distribution of preference looks the same for males and females, the variables are independent; if it differs, there's an association. This comparison is exactly what the **chi-square test** (which this topic builds toward) formalizes statistically. Mastering how to read and construct contingency tables, and how to move fluidly between joint and conditional frequencies, is the foundation for all categorical data analysis.
