---
id: conjoint-analysis-preferences
title: Conjoint Analysis and Stated Preference Methods
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: survey-design-advanced
  type: hard
- id: logistic-regression-binary-outcomes
  type: soft
- id: combinations
  type: soft
builds-toward:
- discrete-choice-modeling
- experimental-design-survey
tags:
- preferences
- survey
- experimental
- choice-modeling
stage: advanced
status: draft
---

# Conjoint Analysis and Stated Preference Methods

## Core Idea
Conjoint analysis presents respondents with combinations of attributes (e.g., policy options with different costs and benefits) and asks them to rank, rate, or choose. Analysis decomposes choices into attribute importance and part-worth utilities. Conjoint experiments reveal trade-offs respondents make; for example, voters' trade-offs between security, liberty, and cost. Advantages include realism and efficiency; disadvantages include hypothetical bias and cognitive burden. Conjoint analysis is widely used in political science, marketing, and policy research.

## Explainer

The fundamental challenge conjoint analysis solves is this: if you ask someone "how much do you value privacy?" they'll say "a lot." If you ask "how much do you value security?" they'll say "a lot." People consistently over-report their preference for every positive attribute when asked directly. Conjoint analysis sidesteps this by forcing respondents to make **trade-offs** — just as real decisions do. By presenting profiles that bundle attributes together (high privacy but high cost; low privacy but high security), the method reveals preferences through choices rather than stated importance ratings. The result is a much more realistic picture of what people actually value relative to each other.

The mechanics connect directly to your survey design background. In a typical conjoint experiment, you construct a factorial design: you have several attributes (say, cost, privacy protection, and response time for a technology policy), each with several levels. Respondents see pairs of profiles drawn from this design and choose which they prefer, or rate each profile. The key mathematical operation is decomposition — working backward from the pattern of choices to estimate each attribute's contribution to overall preference. These contributions are called **part-worth utilities**, and they tell you how much a one-unit change in each attribute moves the average respondent's evaluation. An attribute with high variance in part-worths matters a lot to respondents; one with low variance barely moves the needle.

The statistical engine behind modern conjoint analysis is often logistic regression or its extensions — exactly the model you've studied. Each choice observation is a binary outcome (chose profile A or profile B), and the attribute levels of each profile are the predictors. The coefficients estimate how much each attribute level increases the log-odds of being chosen. This framing makes it easy to extend: you can include interactions between attributes (does cost matter more at high security than low?), allow heterogeneous preferences across respondent subgroups, or model preference shares for hypothetical product configurations not actually tested.

The main threats to conjoint validity are hypothetical bias and cognitive burden. **Hypothetical bias** means stated choices in a survey context may not match real behavior — respondents might claim to care deeply about environmental impact in a product choice but not act on it when paying with their own money. **Cognitive burden** refers to the fact that realistic conjoint profiles can be complex, and respondents simplify by ignoring some attributes, especially late in a long survey. Both threats call for careful design: keep the number of attributes manageable, randomize attribute order, and when possible, validate against real-world data. When those conditions are met, conjoint analysis is among the most powerful tools for measuring latent preferences at scale.
