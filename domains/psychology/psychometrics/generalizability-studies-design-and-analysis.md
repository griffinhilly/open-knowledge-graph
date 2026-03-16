---
id: generalizability-studies-design-and-analysis
title: 'Generalizability Studies: Design and Analysis'
domain: psychology
course: psychometrics
prerequisites:
- id: generalizability-theory-g-theory
  type: hard
- id: internal-consistency-reliability
  type: soft
tags:
- generalizability-theory
- g-study
- d-study
- reliability
- variance-components
stage: advanced
status: draft
---

# Generalizability Studies: Design and Analysis

## Core Idea
Generalizability Theory extends classical test theory by allowing researchers to design G-studies (generalizability studies) that quantify how scores generalize across different conditions such as raters, occasions, items, and settings. D-studies (decision studies) use G-study results to optimize test design by showing how to allocate resources to achieve desired reliability. This approach is particularly useful for performance assessments and clinical ratings.

## Explainer

From your study of Generalizability Theory, you know that G-theory decomposes measurement error into distinct sources using a variance-components framework — rather than treating error as a single undifferentiated lump (as classical test theory does), it asks: *which facets of the measurement situation contribute variance, and how much?* The G-study and D-study are the two-step workflow that makes this framework practically useful for test design.

A **G-study** (generalizability study) is a carefully designed data collection whose purpose is to estimate the variance components associated with each facet of interest. Suppose you're assessing clinical interview skill using three raters who each evaluate ten candidates on five occasions. Your facets are raters, items (assessment criteria), and occasions. A fully crossed G-study design would have every rater evaluate every candidate on every item on every occasion — generating data from which you can estimate the variance due to persons, due to raters, due to items, due to occasions, and due to every interaction among them. The key output is a set of variance component estimates that answer: how much score variability is attributable to genuine person differences versus rater disagreement versus item difficulty versus occasion fluctuation? These variance components are the raw material for everything that follows.

The **D-study** (decision study) takes G-study variance components and answers a design question: *if we change the number of raters, items, or occasions, how does reliability change?* The core metric is the **generalizability coefficient** (analogous to a reliability coefficient), which equals person variance divided by person variance plus relevant error variance. By plugging in different numbers of facet levels — say, two raters instead of three, or eight items instead of five — the D-study projects what the generalizability coefficient would be under each configuration. This transforms test design from guesswork into principled engineering: you can calculate exactly how many raters you need to reach a G-coefficient of 0.85, or whether adding more items buys more reliability than adding more raters.

The distinction between **absolute** and **relative** decisions shapes which error variance you include in the denominator. For relative decisions (ranking candidates, selecting the top 20%), only variance components that affect the rank ordering matter; facet main effects (e.g., all raters being systematically lenient) cancel out and don't affect the coefficient. For absolute decisions (certifying competence against a fixed standard), systematic facet effects do matter — a lenient rater inflates everyone's scores in a way that changes pass/fail decisions. G-theory formalizes this distinction, whereas classical reliability coefficients conflate the two.

Where G-study and D-study are most powerful is for **performance assessments** — clinical skill ratings, writing portfolios, oral exams, work sample tests — where multiple raters, tasks, and occasions are involved and it is far from obvious which facets are the dominant sources of error. In these contexts, internal consistency coefficients (from your prerequisites) are essentially useless: they only capture item-level variance within a single administration. G-theory provides the richer lens, letting designers see not just "how reliable is this test?" but "reliable for what decision, across which generalization, and what would it cost to improve it?"

