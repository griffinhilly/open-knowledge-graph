---
id: multiple-choice-distractor-analysis
title: Distractor Analysis and Multiple-Choice Item Evaluation
domain: psychology
course: psychometrics
prerequisites:
- id: classical-vs-irt-item-analysis
  type: hard
tags:
- multiple-choice
- distractor-analysis
- item-evaluation
stage: advanced
status: draft
---

# Distractor Analysis and Multiple-Choice Item Evaluation

## Core Idea
Effective distractors are plausible but clearly wrong; weak distractors fail to attract low-ability examinees. When high-ability examinees select distractors, correct answers may be ambiguous; unselected distractors waste space. Iterative item review and empirical analysis improve distractor quality, particularly examining option frequencies across ability groups.

## How It's Best Learned
Analyze actual test data by examining frequency of each option choice stratified by total test score groups. Identify patterns and revise weak distractors.

## Explainer

From your study of classical and IRT item analysis, you know how to evaluate a multiple-choice item's difficulty (p-value) and discrimination (point-biserial correlation with total score). Distractor analysis extends this framework from the item level down to the **option level**: instead of just asking "did examinees get it right?", you ask "which wrong answer did they pick, and who picked it?" This more granular view reveals whether each distractor is doing its intended job.

The purpose of a **distractor** — a wrong answer option — is not merely to pad out the format. A well-constructed distractor attracts examinees who have a specific, predictable misconception. For example, a distractor that represents a common algebraic sign error will attract examinees who know the procedure but make that error; a distractor that reflects a conceptual confusion will attract those who lack conceptual understanding. Good distractors reveal diagnostic information about what examinees know and don't know. Weak distractors — those selected by almost nobody — contribute nothing; they waste space that could be filled with a more informative alternative.

The diagnostic signature of a **functioning distractor** is a negative correlation with total test score: low-scoring examinees should choose it more often than high-scoring examinees. This mirrors the logic of item discrimination — if a wrong answer attracts high-scorers as much as low-scorers, something is wrong. Either the distractor is ambiguous (the high-scorers who chose it may have a valid interpretation), or the intended correct answer is unclear, or the distractor captures a nuanced but defensible answer. The **option-level point-biserial** — the correlation between selecting a specific option (coded 1/0) and the total score — should be negative for each distractor and positive for the correct answer. A distractor with a near-zero or positive option-biserial is a red flag.

The practical workflow for distractor analysis is to stratify your sample into score groups (low, middle, high — or deciles for large samples) and tally option frequencies within each group. A well-functioning item shows: most high-scorers selecting the correct answer, most low-scorers distributed across the distractors in a pattern that reflects known misconceptions, and very few examinees at any level selecting any single distractor that dominates. When a distractor attracts nobody, revise it to represent a more plausible error. When a distractor attracts too many high-scorers, investigate whether it is actually wrong — sometimes item review reveals that the distractor is correct or defensible, requiring a scoring correction. Iterative distractor revision is one of the highest-leverage activities in applied test development.
