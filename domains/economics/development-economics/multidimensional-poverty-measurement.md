---
id: multidimensional-poverty-measurement
title: Multidimensional Poverty Indices
domain: economics
course: development-economics
prerequisites:
- id: development-measurement-fundamentals
  type: hard
builds-toward:
- poverty-traps-and-development-thresholds
tags:
- poverty
- measurement
- multidimensional
stage: expert
status: validated
---

# Multidimensional Poverty Indices

## Core Idea
Poverty is not one-dimensional. The Alkire-Foster index captures multiple deprivations—malnutrition, lack of education, no electricity, insecure housing—simultaneously. A person is poor if deprived in enough dimensions, even if income is above a line. This reveals different policy priorities than income-based measures.

## Questions

```yaml
- question: "A household earns $3.50 per person per day (above the World Bank's $2.15/day income line) but lacks clean water, uses solid cooking fuel, and has no household member who has completed six years of schooling. Under the Alkire-Foster MPI with a one-third breadth cutoff, how is this household classified?"
  type: multiple-choice
  options:
    - "Not poor — income above the poverty line is the primary criterion and overrides other deprivations"
    - "Marginally poor — the method averages income and non-income deprivations to produce a composite score"
    - "Multidimensionally poor — deprived in enough indicators simultaneously to meet the breadth cutoff, regardless of income"
    - "Cannot be determined without knowing whether these deprivations are in the same or different dimensions"
  answer: 2
  explanation: "The Alkire-Foster method is explicitly designed to identify poverty that income measures miss. The dual cutoff applies two tests: first, whether the household falls below the threshold on each indicator (deprivation cutoff); second, whether the household is deprived in enough indicators simultaneously to meet the breadth cutoff (typically one-third of weighted indicators). This household's deprivations in water, cooking fuel, and education likely clear the breadth threshold. Income is not part of the MPI at all — the method measures well-being directly."

- question: "Two countries each have income poverty rates of 25%. Country A's multidimensional poverty is concentrated in malnutrition and sanitation; Country B's is concentrated in school non-attendance and lack of electricity. What does this reveal?"
  type: multiple-choice
  options:
    - "Nothing useful — if income poverty is the same, policy responses should be identical"
    - "Country A has worse poverty because malnutrition and sanitation are more severe deprivations than education and electricity"
    - "Different policy priorities: Country A needs nutritional and sanitation programs; Country B needs school construction and electrification — priorities invisible to income data alone"
    - "The MPI is unreliable because two countries with the same income poverty rate produce different profiles"
  answer: 2
  explanation: "This is the central argument for multidimensional measurement: identical income poverty rates can mask radically different patterns of deprivation requiring different interventions. A government using only income data would prescribe the same cash transfer program in both countries. The MPI reveals that Country A needs public health and WASH (water, sanitation, hygiene) investment while Country B needs education and infrastructure investment. The decomposability of the MPI — by region, group, and dimension — is what makes it a policy tool, not just a statistic."

- question: "Under the Alkire-Foster method, a person is classified as multidimensionally poor if they fall below the threshold on any single indicator — for example, lacking electricity alone qualifies them as poor."
  type: true-false
  answer: false
  explanation: "This describes a union approach, not the Alkire-Foster dual cutoff. The method applies a BREADTH cutoff: a person must be deprived in enough indicators simultaneously — in the global MPI, at least one-third of the weighted indicators. Being deprived in a single indicator while meeting all others would not qualify someone as poor. This dual cutoff is what distinguishes the Alkire-Foster method from simply counting any single deprivation and is what makes it measure overlapping, simultaneous deprivations rather than isolated hardships."

- question: "The Alkire-Foster method involves normative choices about which dimensions to include, how to weight them, and where to set cutoffs — meaning that different reasonable methodological choices can produce different poverty headcounts for the same population."
  type: true-false
  answer: true
  explanation: "This is a genuine and acknowledged limitation of multidimensional measurement. Why weight health and education equally? Why set the poverty cutoff at one-third rather than one-quarter of indicators? These are value-laden choices, not purely empirical ones. The Alkire-Foster method is transparent about these choices (unlike many composite indices), but users must recognize that the resulting numbers embed normative judgments. This is why the method should be used with explicit documentation of all choices, sensitivity analysis across alternative specifications, and awareness that the index measures a particular operationalization of poverty — not poverty itself."

- question: "Why might multidimensional poverty measurement lead to different policy recommendations than income-based measurement alone, even for the same population?"
  type: short-answer
  answer: "Income is a means to well-being, not well-being itself. In settings with dysfunctional markets, poor public services, or gender-based exclusion, income may not translate into clean water, education, or adequate nutrition. The MPI measures the actual conditions of people's lives across multiple dimensions simultaneously. Two populations with identical income poverty rates may have completely different deprivation profiles — one concentrated in health and sanitation, another in education and housing. These different profiles imply different interventions: cash transfers improve income but may not reach people deprived of public goods. The MPI can also be decomposed to reveal which subgroups bear the heaviest burden of overlapping deprivations, enabling targeted policy that income data cannot support."
  explanation: "The underlying argument is Sen's capability approach: what matters is what people are able to do and be, not just their monetary resources. Multidimensional measurement operationalizes this by asking directly about capabilities (nutrition, education, shelter, sanitation) rather than inferring them from income. The policy implication is that eliminating poverty requires addressing each deprivation type, not just raising incomes."
```

## Explainer

From your study of development measurement fundamentals, you understand that measuring well-being is not straightforward and that income-based poverty lines — like the World Bank's $2.15/day threshold — provide only a partial picture. **Multidimensional poverty measurement** starts from a direct observation: a person can earn above the income poverty line and still lack clean water, live in a house with a dirt floor, have children out of school, and suffer chronic malnutrition. Income is a means to well-being, not well-being itself, and in settings with dysfunctional markets, poor public services, or gender-based exclusion, income may not translate into the capabilities that actually constitute a decent life.

The most widely used framework is the **Alkire-Foster method**, which underlies the UN's Multidimensional Poverty Index (MPI). It works in two steps. First, you define a set of **dimensions** and **indicators** — the global MPI uses three dimensions (health, education, living standards) with ten indicators such as nutrition, years of schooling, cooking fuel, sanitation, and electricity. For each indicator, you set a deprivation threshold: a child is deprived in schooling if no household member has completed six years of education; a household is deprived in sanitation if it lacks an improved toilet facility. Second, you apply a **dual cutoff**: a person is identified as multidimensionally poor if they are deprived in at least one-third of the weighted indicators simultaneously. This dual cutoff — deprivation within indicators *and* breadth across indicators — distinguishes the approach from simply counting deprivations one at a time.

The power of this approach is that it reveals patterns invisible to income measures. India and the Democratic Republic of Congo may have similar income poverty rates, but their MPI profiles look entirely different: India's deprivations concentrate in nutrition and sanitation, while the DRC's concentrate in education and electricity. This directly informs policy — a government looking only at income poverty would not see that its most urgent need is school construction rather than cash transfers. The MPI can also be decomposed by region, ethnic group, or gender, revealing which subpopulations bear the heaviest burden of overlapping deprivations.

Critics raise legitimate concerns. The choice of dimensions, indicators, weights, and cutoffs involves normative judgments — why weight education and health equally? Why set the poverty cutoff at one-third rather than one-quarter of indicators? Different choices produce different poverty counts. The Alkire-Foster method is transparent about these choices, but users must understand that the resulting numbers reflect both empirical reality and the values embedded in the index design. Despite these limitations, multidimensional measurement has become central to development policy because it forces attention to the actual conditions of people's lives rather than the abstraction of a single dollar figure.
