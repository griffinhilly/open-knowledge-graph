---
id: multidimensional-poverty-index
title: Multidimensional Poverty Index
domain: economics
course: development-economics
prerequisites:
- id: human-development-index
  type: hard
builds-toward:
- poverty-trap-low-equilibrium
tags:
- poverty
- measurement
- multidimensional
stage: expert
status: validated
---

# Multidimensional Poverty Index

## Core Idea
The Multidimensional Poverty Index measures deprivation simultaneously across health, education, and living standards rather than relying solely on income thresholds. Households can experience poverty in multiple dimensions simultaneously; income poverty alone obscures substantial concurrent hardship in health and education.

## Questions

```yaml
- question: "Two households in a developing country each earn $2 per day. Household A has clean water, sends all children to school, and is adequately nourished. Household B lacks sanitation, has no electricity, and has a malnourished child. How does the Multidimensional Poverty Index treat these households differently from an income poverty measure?"
  type: multiple-choice
  options:
    - "It treats them identically, since both fall below the income poverty line and both lack resources"
    - "It classifies Household B as more severely poor, capturing the simultaneous deprivations in health, education, and living standards that income measures miss"
    - "It classifies Household A as more severely poor, since education and clean water are more expensive to provide than cash transfers"
    - "It treats them identically, since the MPI only measures aggregate national poverty, not household-level variation"
  answer: 1
  explanation: "This is the MPI's central insight. Income poverty measures treat both households as identically poor because both fall below the income threshold. The MPI reveals that Household B is deprived in sanitation, electricity, and nutrition simultaneously — a qualitatively different and more severe form of poverty. Two people at the same income level can face radically different lived deprivations that a single monetary measure cannot distinguish."

- question: "A household in a country using the standard MPI is deprived in cooking fuel, sanitation, and child school attendance — but is not deprived in any other indicator. Is this household classified as multidimensionally poor?"
  type: multiple-choice
  options:
    - "Yes, because any deprivation at all classifies a household as poor under the MPI"
    - "No, because the household is deprived in only three indicators out of ten, which is below the one-third threshold"
    - "It depends on the household's income — MPI classifies households only if they are also income-poor"
    - "Yes, because the MPI uses equal weights and three equally-weighted deprivations always exceed the threshold"
  answer: 1
  explanation: "The MPI classifies a household as multidimensionally poor only if its weighted deprivation score exceeds one-third of the maximum possible score. With ten equally-weighted indicators (in the standard MPI each has a weight of 1/10), three deprivations give a score of 3/10 = 0.30, which is below the one-third (0.333) threshold. So this household is NOT classified as multidimensionally poor despite having real deprivations. This threshold prevents minor single-indicator shortfalls from dominating the classification."

- question: "The MPI can be decomposed by dimension, region, and demographic group, allowing policymakers to identify which specific deprivations are driving poverty in different areas."
  type: true-false
  answer: true
  explanation: "Decomposability is one of the MPI's most valuable properties. Because the index is built from weighted sums of specific deprivation indicators, you can mathematically decompose the aggregate MPI score to show what fraction of poverty is attributable to health deprivations, education deprivations, or living standards deprivations — and do this separately for each region or group. This granularity is impossible with a single income threshold, which reveals only 'who is poor,' not 'in what ways are they poor.'"

- question: "A country that successfully reduces income poverty through cash transfer programs will necessarily also reduce its MPI score, since higher income addresses all forms of deprivation."
  type: true-false
  answer: false
  explanation: "This is the key divergence between income and multidimensional poverty. Cash transfers raise income but do not directly provide sanitation infrastructure, build schools, train health workers, or supply electricity. A country can sharply reduce income poverty while leaving households deprived in health services, education access, and basic amenities — the non-monetary dimensions the MPI captures. In practice, some countries have done exactly this: income poverty fell while MPI-measured deprivations in sanitation and education persisted, because those require public investment rather than cash."

- question: "Why might a policymaker prefer the MPI over an income-based poverty measure when designing anti-poverty programs, and what does the MPI reveal that income measures cannot?"
  type: short-answer
  answer: "The MPI reveals the specific dimensions and indicators in which households are deprived simultaneously — health, education, and living standards — rather than just whether they fall below an income threshold. Because the MPI is decomposable, a policymaker can identify that poverty in region A is driven mainly by lack of sanitation while in region B it is driven by school non-attendance, and target investments accordingly. Income measures cannot provide this specificity: two households at the same income level may have entirely different deprivation profiles, and a single cash transfer may address income poverty without touching the underlying deprivations in public services and infrastructure."
  explanation: "The core insight is that poverty is multidimensional and concurrent — deprivations in health, education, and living standards often reinforce each other in ways that income alone cannot capture or address. The MPI operationalizes this by measuring each dimension separately, then asking whether households are simultaneously deprived across enough dimensions to be classified as poor. This turns poverty measurement from a single number into a diagnosis."
```

## Explainer

From your study of the **Human Development Index (HDI)**, you know that development is about more than income — it encompasses health, education, and living standards. The HDI captures this at the country level by averaging national indicators. But the **Multidimensional Poverty Index (MPI)** takes the insight further by asking: at the household level, who is simultaneously deprived across multiple dimensions, and how severely? This shift from country averages to household-level deprivation reveals patterns that income-based poverty measures miss entirely.

The MPI, developed by Sabina Alkire and James Foster, works by defining ten indicators across three equally weighted dimensions. **Health** includes nutrition and child mortality. **Education** includes years of schooling and school attendance. **Living standards** includes cooking fuel, sanitation, drinking water, electricity, housing, and assets. A household is assessed on each indicator, and a **deprivation score** is calculated as the weighted sum of indicators where the household falls below the threshold. A household is classified as **multidimensionally poor** if its deprivation score exceeds one-third of the maximum — meaning it is deprived in at least a third of the weighted indicators simultaneously.

Why does this matter beyond what income measures already tell us? Consider two households, each earning $2 per day. One has clean water, sends children to school, and has adequate nutrition. The other lacks sanitation, has no electricity, and has a malnourished child. Income poverty measures treat them identically; the MPI reveals that the second household faces a qualitatively different and more severe form of deprivation. At the national level, the MPI often produces very different pictures than income poverty. Some countries with moderate income poverty have high multidimensional poverty because public services in health and education are weak. Others have reduced income poverty through cash transfers without addressing the underlying deprivations in sanitation, housing, and nutrition.

The MPI is also a powerful policy tool because it can be **decomposed** — broken down by dimension, indicator, region, or demographic group. A government can identify that poverty in its northern provinces is driven primarily by education deprivation while in southern provinces it is driven by lack of sanitation, and target interventions accordingly. This granularity is impossible with a single income threshold. The MPI makes concrete the principle that poverty is not merely about money but about the intersection of deprivations that together trap households in hardship.
