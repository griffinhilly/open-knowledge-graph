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
status: validated
---

# Frequency Distributions and Contingency Tables

## Core Idea
A frequency distribution tabulates how often each value or category occurs. For categorical data, a contingency table shows frequencies for combinations of two variables. These tables reveal patterns in data and form the basis for many statistical tests.

## How It's Best Learned
Create frequency tables from real survey data. Construct contingency tables and calculate marginal and conditional frequencies. Use software to generate these tables efficiently.

## Common Misconceptions
Confusing frequency with relative frequency. Not distinguishing between univariate and bivariate frequency tables. Thinking frequency tables only apply to categorical data (they work for discrete quantitative too).

## Questions

```yaml
- question: "In a survey, 40 out of 200 total respondents are women who prefer Brand A. There are 80 women total. What is the conditional frequency of preferring Brand A, given the respondent is a woman?"
  type: multiple-choice
  options:
    - "0.20 (40 out of 200 total respondents)"
    - "0.50 (40 out of 80 women)"
    - "0.40 (80 out of 200 total respondents)"
    - "0.33 (40 out of 120 non-women)"
  answer: 1
  explanation: "Conditional frequency restricts the denominator to the group you're conditioning on. Given the respondent is a woman, the relevant pool is the 80 women — not all 200 respondents. So the conditional frequency is 40/80 = 0.50. Option A (0.20) is the joint frequency: the proportion of the entire sample that is both female AND prefers Brand A. Option C (0.40) is the marginal frequency of women. Mixing up joint and conditional frequencies is the most common error in contingency table analysis."

- question: "School A reports 60 students prefer online learning; School B reports 90 students prefer online learning. A student concludes School B has stronger preference for online learning. What critical information is missing?"
  type: multiple-choice
  options:
    - "The specific online platforms used at each school"
    - "The total number of students surveyed at each school, needed to compute relative frequencies"
    - "Whether both surveys were conducted during the same semester"
    - "The grade levels of the students surveyed"
  answer: 1
  explanation: "Raw frequency counts are uninterpretable without the total sample size. If School A surveyed 80 students (75% prefer online) and School B surveyed 900 (10% prefer online), School A actually has the stronger preference. Relative frequency — count divided by total — is the correct metric for comparison across samples of different sizes. This is one of the core lessons of frequency distributions: always normalize before comparing."

- question: "In a contingency table, the marginal frequencies are the individual cell counts for each combination of categories."
  type: true-false
  answer: false
  explanation: "Marginal frequencies are the row totals and column totals that appear at the 'margins' of the table. They show the distribution of each variable on its own, ignoring the other. The individual cell counts are called joint frequencies — they show how often each specific combination of both variables occurs. Marginal frequencies are obtained by summing across rows or columns; joint frequencies are the raw cells."

- question: "A frequency distribution can be constructed for discrete quantitative data as well as categorical data."
  type: true-false
  answer: true
  explanation: "Frequency distributions work for any type of data where you can enumerate values and count occurrences. For discrete quantitative data (like the number of siblings, or a 1-10 rating scale), you list each possible value and count how often it appears — exactly as with categorical data. Continuous quantitative data requires grouping into bins (class intervals) first, but the resulting grouped frequency distribution is equally valid."

- question: "What is the difference between a joint frequency and a conditional frequency in a contingency table, and why does this distinction matter for detecting association between variables?"
  type: short-answer
  answer: "A joint frequency is the count (or proportion) for a specific combination of both variables — e.g., the proportion of all respondents who are female AND prefer Brand A. A conditional frequency restricts the denominator to one category — e.g., among women only, the proportion who prefer Brand A. The distinction matters because association is detected by comparing conditional frequencies across groups: if the conditional distribution of Brand preference looks the same for men and women, the variables are independent. If it differs, there is an association. Joint frequencies alone can't reveal this because they're confounded by the marginal distributions."
  explanation: "The chi-square test formalizes exactly this comparison of conditional frequencies. If you only report joint frequencies, you cannot tell whether an observed pattern reflects a real association or merely the fact that one group is larger. Conditional frequencies control for group size and expose the genuine relationship (or lack thereof) between the two variables."
```

## Explainer

A **frequency distribution** is simply a systematic count: for each possible value or category in your dataset, how many times does it appear? You already know from your prerequisite work the distinction between categorical variables (like eye color or political party) and quantitative variables (like test scores or height). Frequency tables work for both, though the setup differs slightly — for categorical data you list the categories directly, while for continuous quantitative data you first group values into class intervals (bins) before counting. Either way, the table transforms a raw list of observations into an organized summary of what values occurred and how often.

**Relative frequency** is the count divided by the total number of observations, expressing each category's share as a proportion or percentage. If 30 out of 120 survey respondents prefer option A, the relative frequency is 30/120 = 0.25, or 25%. Relative frequencies are more informative than raw counts when comparing datasets of different sizes, and they sum to exactly 1 (or 100%). **Cumulative frequency** adds frequencies sequentially: what fraction of observations fall below a given value? This cumulative view connects directly to the empirical CDF (cumulative distribution function) you'll encounter in more advanced statistics.

**Contingency tables** (also called two-way or cross-tabulation tables) extend the idea to two categorical variables simultaneously. Each cell shows the frequency (or relative frequency) for one combination of categories — for example, the number of survey respondents who are both female and prefer option A. The row totals and column totals are called **marginal frequencies**, because they sit at the margins of the table and show the distribution of each variable on its own. The individual cells give the **joint frequencies**, showing how the variables relate to each other.

The most important derived quantity is **conditional frequency**: out of all female respondents, what proportion prefer option A? You compute this by dividing the joint frequency (female + option A) by the marginal frequency for that row (all females). Comparing conditional frequencies across rows (or columns) reveals whether two variables are associated — if the conditional distribution of preference looks the same for males and females, the variables are independent; if it differs, there's an association. This comparison is exactly what the **chi-square test** (which this topic builds toward) formalizes statistically. Mastering how to read and construct contingency tables, and how to move fluidly between joint and conditional frequencies, is the foundation for all categorical data analysis.
