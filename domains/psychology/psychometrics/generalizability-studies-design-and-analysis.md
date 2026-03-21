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

## Questions

```yaml
- question: "A G-study of a clinical skills exam reveals that rater variance accounts for 38% of total score variance, item variance accounts for 6%, and person variance accounts for 42%. You have a limited budget to improve reliability. What does a D-study direct you to do?"
  type: multiple-choice
  options:
    - "Add more items, because more items always reduce the largest source of error"
    - "Add more raters, because rater variance is the dominant error source and adding raters averages it out"
    - "Add more occasions, because occasion effects are always the largest source of error in performance assessments"
    - "Reduce the number of items to shorten the test and reduce candidate fatigue"
  answer: 1
  explanation: "The D-study uses G-study variance component estimates to project how changing facet levels affects the generalizability coefficient. When rater variance dominates, adding more raters reduces that error source most efficiently — each additional rater averages out idiosyncratic leniency or stringency. Adding items would only help if item variance were large. The point of the two-step G/D workflow is precisely to move from guesswork to principled resource allocation based on empirical variance component estimates."

- question: "A licensing board uses an oral exam to certify whether candidates meet a minimum competency standard of 75 points. Should they compute an absolute or relative generalizability coefficient, and why?"
  type: multiple-choice
  options:
    - "Relative, because they are ultimately comparing candidates against each other to award licenses"
    - "Absolute, because the decision is about meeting a fixed standard — a lenient rater who inflates everyone's scores changes who passes, even without changing rankings"
    - "Either coefficient, since both are mathematically equivalent when the decision threshold is fixed"
    - "Relative, because it is always more conservative and therefore safer for high-stakes decisions"
  answer: 1
  explanation: "The absolute/relative distinction maps directly onto the decision structure. For relative decisions (ranking, selecting the top N%), systematic facet effects like overall rater leniency cancel out — if one rater gives everyone 10 points more, ranks are unchanged. But for absolute decisions (meeting a fixed threshold), those systematic effects matter enormously: a lenient rater pushes borderline candidates over the cut score. The absolute coefficient includes all error variance in the denominator; the relative coefficient excludes facet main effects. Using the wrong coefficient for a licensing exam can systematically misrepresent the measurement's accuracy."

- question: "In G-theory, a lenient rater who gives every candidate a 10-point score inflation affects absolute decisions (pass/fail against a fixed standard) but not relative decisions (ranking candidates against each other)."
  type: true-false
  answer: true
  explanation: "This is the core intuition behind the absolute/relative distinction. For relative decisions, what matters is whether candidates' rank ordering is preserved — uniform inflation shifts everyone equally, leaving ranks intact. For absolute decisions, a 10-point inflation systematically changes who clears the fixed cut score. G-theory formalizes this by including or excluding facet main effects in the error variance term depending on which type of decision is being made. Classical reliability coefficients conflate the two cases."

- question: "Internal consistency coefficients like Cronbach's alpha are sufficient for evaluating the reliability of performance assessments involving multiple raters, tasks, and occasions, making G-study analyses unnecessary."
  type: true-false
  answer: false
  explanation: "Internal consistency coefficients only capture item-level variance within a single administration — they cannot separate rater disagreement, occasion fluctuation, or task-specific variance as distinct error sources. For a performance assessment with three raters and five tasks, Cronbach's alpha can tell you whether items co-vary, but it cannot tell you whether your reliability problem is rater disagreement (fix: add raters) versus task inconsistency (fix: add tasks). G-theory provides the richer diagnostic lens that classical reliability entirely lacks."

- question: "What is the practical difference between a G-study and a D-study, and why do you need both?"
  type: short-answer
  answer: "A G-study is a data collection designed to estimate the variance components for each facet of the measurement situation — it answers 'how much of the score variance comes from persons, raters, items, occasions, and their interactions?' A D-study uses those variance component estimates to project how the generalizability coefficient would change under different test designs — it answers 'if I use two raters instead of three, or eight items instead of five, what reliability would I achieve?' You need the G-study to produce the empirical estimates that make the D-study projections accurate. Without the G-study, test design is guesswork; without the D-study, the variance components are just descriptive statistics with no actionable implications."
  explanation: "The two-step workflow transforms G-theory from an interesting measurement framework into a practical design tool. The G-study produces the raw inputs (variance components); the D-study converts them into engineering specifications (how many raters/items/occasions do I need to reach a G-coefficient of 0.85?). Neither step alone answers the test designer's practical question."
```

## Explainer

From your study of Generalizability Theory, you know that G-theory decomposes measurement error into distinct sources using a variance-components framework — rather than treating error as a single undifferentiated lump (as classical test theory does), it asks: *which facets of the measurement situation contribute variance, and how much?* The G-study and D-study are the two-step workflow that makes this framework practically useful for test design.

A **G-study** (generalizability study) is a carefully designed data collection whose purpose is to estimate the variance components associated with each facet of interest. Suppose you're assessing clinical interview skill using three raters who each evaluate ten candidates on five occasions. Your facets are raters, items (assessment criteria), and occasions. A fully crossed G-study design would have every rater evaluate every candidate on every item on every occasion — generating data from which you can estimate the variance due to persons, due to raters, due to items, due to occasions, and due to every interaction among them. The key output is a set of variance component estimates that answer: how much score variability is attributable to genuine person differences versus rater disagreement versus item difficulty versus occasion fluctuation? These variance components are the raw material for everything that follows.

The **D-study** (decision study) takes G-study variance components and answers a design question: *if we change the number of raters, items, or occasions, how does reliability change?* The core metric is the **generalizability coefficient** (analogous to a reliability coefficient), which equals person variance divided by person variance plus relevant error variance. By plugging in different numbers of facet levels — say, two raters instead of three, or eight items instead of five — the D-study projects what the generalizability coefficient would be under each configuration. This transforms test design from guesswork into principled engineering: you can calculate exactly how many raters you need to reach a G-coefficient of 0.85, or whether adding more items buys more reliability than adding more raters.

The distinction between **absolute** and **relative** decisions shapes which error variance you include in the denominator. For relative decisions (ranking candidates, selecting the top 20%), only variance components that affect the rank ordering matter; facet main effects (e.g., all raters being systematically lenient) cancel out and don't affect the coefficient. For absolute decisions (certifying competence against a fixed standard), systematic facet effects do matter — a lenient rater inflates everyone's scores in a way that changes pass/fail decisions. G-theory formalizes this distinction, whereas classical reliability coefficients conflate the two.

Where G-study and D-study are most powerful is for **performance assessments** — clinical skill ratings, writing portfolios, oral exams, work sample tests — where multiple raters, tasks, and occasions are involved and it is far from obvious which facets are the dominant sources of error. In these contexts, internal consistency coefficients (from your prerequisites) are essentially useless: they only capture item-level variance within a single administration. G-theory provides the richer lens, letting designers see not just "how reliable is this test?" but "reliable for what decision, across which generalization, and what would it cost to improve it?"

