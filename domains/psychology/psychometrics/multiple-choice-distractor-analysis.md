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
stage: expert
status: draft
---

# Distractor Analysis and Multiple-Choice Item Evaluation

## Core Idea
Effective distractors are plausible but clearly wrong; weak distractors fail to attract low-ability examinees. When high-ability examinees select distractors, correct answers may be ambiguous; unselected distractors waste space. Iterative item review and empirical analysis improve distractor quality, particularly examining option frequencies across ability groups.

## How It's Best Learned
Analyze actual test data by examining frequency of each option choice stratified by total test score groups. Identify patterns and revise weak distractors.

## Questions

```yaml
- question: "An item analysis shows that distractor option B is selected by 38% of high-scoring examinees and only 12% of low-scoring examinees. What does this pattern most likely indicate?"
  type: multiple-choice
  options:
    - "Option B is a highly effective distractor because many examinees selected it"
    - "Option B may be defensible or ambiguous, and the scoring key should be reviewed"
    - "The item is too difficult and should be removed from the test"
    - "Low-scoring examinees are not reading carefully enough"
  answer: 1
  explanation: "A functioning distractor should have a negative correlation with test score — low scorers choose it more, high scorers avoid it. When high-scorers choose a distractor more than low-scorers, the option-biserial correlation is positive, which is a red flag. High-scorers are presumably more knowledgeable, so if they are selecting a 'wrong' answer, it may not actually be wrong — the option may be ambiguous, technically defensible, or reveal a scoring key error. This is precisely when item review is needed."

- question: "What property must a distractor have to be considered 'functioning' in a well-designed multiple-choice item?"
  type: multiple-choice
  options:
    - "It must be selected by at least 5% of examinees at all ability levels"
    - "It must be selected more frequently by lower-scoring examinees than by higher-scoring examinees"
    - "It must closely resemble the correct answer in surface form to maximize difficulty"
    - "It must be selected by high-scoring examinees to confirm they carefully considered it"
  answer: 1
  explanation: "The diagnostic signature of a functioning distractor is a negative option-level point-biserial correlation — low-scorers select it more often than high-scorers. This mirrors item discrimination logic: the distractor successfully attracts examinees who hold a specific misconception or gap, while well-prepared examinees correctly reject it. A distractor that is equally likely to attract high and low scorers provides no diagnostic information and may signal item flaws."

- question: "An unselected distractor — one chosen by almost no examinees — is a problem in multiple-choice item development because it wastes an option slot that could carry diagnostic information."
  type: true-false
  answer: true
  explanation: "Distractors serve a purpose: they should attract examinees who hold a specific, predictable misconception and thereby reveal diagnostic information about what examinees do and don't understand. A distractor that nobody selects contributes nothing — it is not attracting the misconception it was presumably written to target. That option slot could instead represent a more commonly held error, making the item more informative and the test more valid."

- question: "A distractor is functioning well if high-scoring examinees avoid it, even if low-scoring examinees also rarely select it."
  type: true-false
  answer: false
  explanation: "A distractor requires two things to be functioning: high scorers should avoid it AND low scorers should select it. If both groups avoid it, the distractor is simply unselected — it represents no real misconception in the test population. The negative correlation between option selection and test score is the defining characteristic of a functioning distractor. High scorers avoiding it alone does not make it functional; the distractor must also attract the less-prepared examinees."

- question: "What does it mean for a distractor to be 'diagnostic,' and why is this property important in test development?"
  type: short-answer
  answer: "A diagnostic distractor represents a specific, predictable misconception or error pattern — when an examinee chooses it, this reveals something meaningful about their knowledge gap. A distractor is diagnostic when examinees who select it share a common error: a procedural mistake, a conceptual confusion, or a misremembered fact. This matters because it transforms the multiple-choice item from a simple right/wrong indicator into a tool that reveals the nature of examinee understanding, enabling targeted instructional follow-up."
  explanation: "Non-diagnostic distractors — those that attract responses at random or that attract nobody — provide only noise. The goal of distractor construction is to represent the actual error space of the examinee population, so that wrong answers carry as much information as right answers. In formative assessment settings, this diagnostic function is especially valuable."
```

## Explainer

From your study of classical and IRT item analysis, you know how to evaluate a multiple-choice item's difficulty (p-value) and discrimination (point-biserial correlation with total score). Distractor analysis extends this framework from the item level down to the **option level**: instead of just asking "did examinees get it right?", you ask "which wrong answer did they pick, and who picked it?" This more granular view reveals whether each distractor is doing its intended job.

The purpose of a **distractor** — a wrong answer option — is not merely to pad out the format. A well-constructed distractor attracts examinees who have a specific, predictable misconception. For example, a distractor that represents a common algebraic sign error will attract examinees who know the procedure but make that error; a distractor that reflects a conceptual confusion will attract those who lack conceptual understanding. Good distractors reveal diagnostic information about what examinees know and don't know. Weak distractors — those selected by almost nobody — contribute nothing; they waste space that could be filled with a more informative alternative.

The diagnostic signature of a **functioning distractor** is a negative correlation with total test score: low-scoring examinees should choose it more often than high-scoring examinees. This mirrors the logic of item discrimination — if a wrong answer attracts high-scorers as much as low-scorers, something is wrong. Either the distractor is ambiguous (the high-scorers who chose it may have a valid interpretation), or the intended correct answer is unclear, or the distractor captures a nuanced but defensible answer. The **option-level point-biserial** — the correlation between selecting a specific option (coded 1/0) and the total score — should be negative for each distractor and positive for the correct answer. A distractor with a near-zero or positive option-biserial is a red flag.

The practical workflow for distractor analysis is to stratify your sample into score groups (low, middle, high — or deciles for large samples) and tally option frequencies within each group. A well-functioning item shows: most high-scorers selecting the correct answer, most low-scorers distributed across the distractors in a pattern that reflects known misconceptions, and very few examinees at any level selecting any single distractor that dominates. When a distractor attracts nobody, revise it to represent a more plausible error. When a distractor attracts too many high-scorers, investigate whether it is actually wrong — sometimes item review reveals that the distractor is correct or defensible, requiring a scoring correction. Iterative distractor revision is one of the highest-leverage activities in applied test development.
