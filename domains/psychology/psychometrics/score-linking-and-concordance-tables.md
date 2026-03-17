---
id: score-linking-and-concordance-tables
title: Score Linking and Concordance Tables
domain: psychology
course: psychometrics
prerequisites:
- id: test-equating-and-linking
  type: hard
- id: measurement-scales-psychology
  type: soft
tags:
- linking
- concordance
- scale-translation
- equating
- score-conversion
stage: advanced
status: draft
---

# Score Linking and Concordance Tables

## Core Idea
Score linking creates empirical relationships between scales measuring related constructs (e.g., old and new versions of a test, or different tests of similar constructs), enabling researchers to translate scores from one test to another. Concordance tables or regression equations allow comparison of scores and facilitate interpretation when multiple measures exist. Linking assumes the constructs are sufficiently similar and requires sufficient overlap data.

## Explainer

From your study of test equating and linking, you know that **equating** refers to the strict case of creating interchangeable scores across parallel forms of the same test — forms designed to measure the identical construct at the same difficulty level with the same scaling. **Score linking** is the broader family of methods that includes equating but extends to situations where tests are similar but not identical, and where the goal is translation rather than strict interchangeability.

The most common application is the **concordance table** — an empirically derived lookup table that maps scores from one test to scores on another. A familiar example is the SAT-ACT concordance: because millions of students take one or both, researchers can identify the ACT composite score that corresponds to each SAT total score by finding the scores at equivalent percentile ranks in the overlap sample. If 70% of students who score a 28 on the ACT score below a 1300 on the SAT, and 70% of students who score 1300 on the SAT score below a 1300, then 28 ACT ≈ 1300 SAT by **equipercentile linking**. This approach requires no strong parametric assumptions — it simply matches the percentile distributions.

The critical distinction you must hold onto is between **equating** and **concordance**, and the difference lies in what you can claim afterward. Equated scores are interchangeable — a 500 on Form A means the same thing as a 500 on Form B, and admission officers can treat them identically. Concorded scores are merely *comparable* — a concorded ACT score is an estimate of the score range a student would likely achieve on the SAT, but it carries more uncertainty and should not be treated as exact. The reason is **construct overlap**: the SAT and ACT measure overlapping but non-identical constructs (the ACT has a science section; the two differ in timing and format). When construct overlap is imperfect, equipercentile correspondence does not imply score exchangeability.

**Regression-based linking** is an alternative approach, particularly useful in research contexts. If you have a sample that completed both instruments, you can regress scores on one test onto the other and use the regression equation to predict one from the other. This is simpler but inherits a limitation: regression to the mean means predicted scores will be more compressed than actual scores — extreme scorers on one test will be predicted as less extreme on the other. Concordance tables using equipercentile methods avoid this compression. Understanding these trade-offs matters whenever you need to pool data from studies using different instruments, translate clinical cutoffs from one screening tool to another, or interpret scores when a test is revised and the new version cannot be directly equated to the old.
