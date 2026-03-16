---
id: categorical-vs-quantitative-data
title: Categorical vs. Quantitative Data
domain: mathematics
course: probability-and-statistics
prerequisites: []
builds-toward:
- frequency-distributions-and-tables
- frequency-tables-histograms
tags:
- data-types
- descriptive-statistics
stage: formal-systems
status: draft
---

# Categorical vs. Quantitative Data

## Core Idea
Categorical (qualitative) data represents categories or groups like colors or regions. Quantitative (numerical) data represents measured or counted quantities. The distinction determines which statistical methods and visualizations are appropriate.

## How It's Best Learned
Classify variables from real datasets. Create frequency tables for categorical data and histograms for quantitative data. Note that ordinal data (like ratings) falls in between.

## Common Misconceptions
Thinking all numerical data is quantitative (zip codes are categorical). Treating categorical data as numerical (averaging color codes). Not recognizing that the same attribute can be measured as either categorical or quantitative.

## Explainer

Every dataset is made up of variables, and before you can analyze any variable you need to know what kind of data it is. The most fundamental split is between **categorical data** — which places each observation into a named group — and **quantitative data** — which records a number that represents a measured or counted amount. This distinction is not cosmetic; it determines which graphs are appropriate, which summary statistics are meaningful, and which statistical tests apply.

Categorical data describes membership in groups. Eye color (brown, blue, green), country of residence, political affiliation, type of car — these are categories. You can count how many observations fall in each category, but arithmetic on the labels themselves is meaningless. You cannot compute the "average eye color" or say that blue is twice as much as brown. The natural display is a **bar chart** or **pie chart**, and the natural summaries are counts and proportions. A useful sub-distinction: **nominal** categorical data has no natural ordering (like colors or country names), while **ordinal** categorical data has a ranking (like pain level: mild/moderate/severe, or letter grades A/B/C/D/F) — but even ordinal data doesn't support arithmetic.

Quantitative data records a number that means something numerically. Height in centimeters, temperature in Kelvin, test scores out of 100, number of siblings — these are quantities. You can add them, subtract them, average them, and measure how spread out they are. The natural display is a **histogram** or **dot plot**, and the natural summaries are measures of center (mean, median) and spread (standard deviation, range). A further sub-distinction: **discrete** quantitative data can only take specific values (whole number of children: 0, 1, 2, ...), while **continuous** quantitative data can take any value in a range (height, weight, time).

The most common trap is that numbers don't automatically mean quantitative. A zip code is a number, but averaging zip codes produces a meaningless result — 10001 and 90210 are labels for geographic areas, not amounts of something. Similarly, jersey numbers, phone area codes, and survey responses coded as 1/2/3 are all categorical despite being numbers. The test is simple: does arithmetic on these numbers produce a meaningful result? If yes, it's quantitative. If no — if the "difference" between a zip code of 10001 and 90210 means nothing — it's categorical. Getting this distinction right is the first step in every data analysis.
