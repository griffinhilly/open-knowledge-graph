---
id: item-difficulty-discrimination
title: Item Difficulty and Item Discrimination Analysis
domain: psychology
course: psychometrics
prerequisites:
- id: item-response-functions
  type: hard
- id: classical-test-theory
  type: hard
builds-toward:
- differential-item-functioning
tags:
- item-analysis
- p-value
- point-biserial
- item-revision
stage: advanced
status: draft
---

# Item Difficulty and Item Discrimination Analysis

## Core Idea
Item difficulty is the proportion of test-takers answering an item correctly; item discrimination is the correlation between item response and total score (point-biserial correlation). These indices identify problematic items that fail to contribute effectively to score precision and test reliability.

## How It's Best Learned
Calculate p-values and discrimination indices for classroom or standardized test data. Create item analysis reports identifying items for revision or removal based on statistical evidence.

## Common Misconceptions
Very high difficulty (p-value near 1.0) is always undesirable. Easy items can be valuable for confidence and accessibility. Similarly, low discrimination doesn't automatically warrant item removal; consider construct relevance and test purpose.

## Explainer

Classical test theory and item response functions, which you've studied as prerequisites, both treat individual test items as the unit of analysis for understanding test quality. Item difficulty and discrimination are the two most basic numerical summaries of how a single item is performing — together they are the workhorses of practical test development, review, and revision.

**Item difficulty** in classical test theory is expressed as the **p-value** — not the statistical significance p-value, but the proportion of test-takers answering the item correctly. A p-value of 0.80 means 80% answered correctly; 0.30 means 30% did. The scale is counterintuitive: higher p-value means an easier item. For a test designed to discriminate across a wide range of ability, items near p = 0.50 contribute the most information because they split the group. Very easy items (p near 1.0) and very hard items (p near 0.0) tell you little about individual differences — almost everyone gets them right or wrong regardless of ability. But p-value targets must match test purpose: a mastery certification test may legitimately include many easy items if the threshold skill is expected of nearly all competent performers.

**Item discrimination** measures whether the item distinguishes between high and low scorers on the test overall. The most common index is the **point-biserial correlation** — the correlation between item response (0 = wrong, 1 = right) and total score. A high point-biserial (typically 0.30+ is considered good) means high scorers mostly got this item right and low scorers mostly got it wrong — the item is pulling in the same direction as the test. A near-zero discrimination means the item is essentially noise, contributing no information about the underlying construct. A *negative* discrimination is a red flag: high-scoring students are getting the item wrong more often than low scorers, which usually signals a miskeyed item (the wrong answer recorded as correct) or a genuinely ambiguous question.

The connection to item response theory (IRT) from your prerequisite is direct: IRT's difficulty parameter (*b*) is a more principled version of the p-value, estimated from the full item characteristic curve rather than a simple proportion. IRT's discrimination parameter (*a*) corresponds to the slope of the curve at the difficulty point — which is what the point-biserial is approximating in simpler form. Classical indices are computationally transparent and sufficient for most routine test review; IRT provides more information at the cost of greater complexity and larger sample requirements. In practice, item analysis combines both indices alongside expert review: statistics diagnose problems, but content knowledge determines the remedy.
