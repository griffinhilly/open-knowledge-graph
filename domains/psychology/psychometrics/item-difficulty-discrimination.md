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

## Questions

```yaml
- question: "After scoring an exam, you find that Item 14 has a point-biserial correlation of -0.22. What does this most likely indicate?"
  type: multiple-choice
  options:
    - "The item is too easy — nearly everyone got it right, compressing variance"
    - "The item is too difficult — very few correct responses inflated the correlation"
    - "The item may be miskeyed or genuinely ambiguous — high scorers got it wrong more than low scorers"
    - "The item is fine — negative correlations are common for true-false items"
  answer: 2
  explanation: "A negative point-biserial is a red flag: it means students who scored higher on the test overall were *less* likely to get this item correct. This is the opposite of what a good item does. The most common cause is a miskeyed item — the answer key records the wrong option as correct, so knowledgeable students who know the right answer are penalized. It can also signal a genuinely ambiguous question that confused the best students. A negative discrimination almost always warrants immediate review of the key and item wording before the scores are used."

- question: "An item has a p-value of 0.95 on a licensure examination for nurses. A test developer proposes removing it for being 'too easy.' What is the best response?"
  type: multiple-choice
  options:
    - "Agree — items near p = 0.50 are always preferable because they maximize variance"
    - "Agree — a p-value of 0.95 means the item contributes almost no information to score differentiation"
    - "Disagree — the p-value should be evaluated in context; for a safety-critical competency, near-universal mastery is expected and appropriate"
    - "Disagree — p-values above 0.90 are outliers caused by measurement error and should be retained"
  answer: 2
  explanation: "Easy items (high p-value) do minimize variance and contribute little to differentiating ability across the full range, which makes them poor choices for norm-referenced tests designed to spread examinees out. But test purpose matters: a licensure exam certifies minimum competency, and certain safety-critical tasks (e.g., identifying a medication overdose) should be known by virtually every competent nurse. A p-value of 0.95 on such an item reflects appropriate domain mastery, not a flawed item. The statistical argument for removing easy items applies most forcefully to aptitude tests, not mastery assessments."

- question: "In classical test theory, a higher p-value for an item means the item is harder."
  type: true-false
  answer: false
  explanation: "This is the most counterintuitive convention in classical test theory. The p-value (proportion correct) runs from 0 to 1, and a higher p-value means *more* people got the item right — meaning the item is *easier*, not harder. An item with p = 0.90 is very easy (90% correct); an item with p = 0.20 is very difficult (only 20% correct). The naming is confusing because 'p-value' in statistics usually refers to hypothesis testing, but in item analysis it simply means the proportion passing. Students who reason by analogy from statistical p-values often get this backwards."

- question: "An item with near-zero point-biserial discrimination is contributing meaningful information about the underlying construct being measured."
  type: true-false
  answer: false
  explanation: "Discrimination measures whether the item distinguishes high from low scorers. A point-biserial near zero means the item response is essentially uncorrelated with total score — whether a student answers correctly is unrelated to their overall ability on the test. Such items contribute statistical noise rather than signal. They inflate test length without improving reliability or validity. Items with near-zero discrimination should be reviewed for construct relevance (does this item actually measure what the test is measuring?), clarity (is the wording confusing to all ability levels equally?), and keying accuracy."

- question: "Why is a negative item discrimination index a more serious problem than simply low discrimination, and what should a test developer do when encountering it?"
  type: short-answer
  answer: "Negative discrimination means high scorers got the item wrong more often than low scorers — the item is pulling in the opposite direction from the test. This actively *harms* measurement validity: it penalizes the most knowledgeable students. Low discrimination is a neutral problem (the item is inert), but negative discrimination is an active problem. The immediate step is to check the answer key for miskeying, then review the item for ambiguity. The item should be flagged and either rescored or removed before final score reporting."
  explanation: "Low discrimination items waste test time but don't distort rankings; negative discrimination items distort them in the wrong direction. In high-stakes testing (admissions, licensure), leaving a negatively discriminating item in the scored set can change who passes and fails. The standard practice is to audit all items with point-biserials below 0.15 and treat negative values as emergencies requiring pre-score-reporting resolution."
```

## Explainer

Classical test theory and item response functions, which you've studied as prerequisites, both treat individual test items as the unit of analysis for understanding test quality. Item difficulty and discrimination are the two most basic numerical summaries of how a single item is performing — together they are the workhorses of practical test development, review, and revision.

**Item difficulty** in classical test theory is expressed as the **p-value** — not the statistical significance p-value, but the proportion of test-takers answering the item correctly. A p-value of 0.80 means 80% answered correctly; 0.30 means 30% did. The scale is counterintuitive: higher p-value means an easier item. For a test designed to discriminate across a wide range of ability, items near p = 0.50 contribute the most information because they split the group. Very easy items (p near 1.0) and very hard items (p near 0.0) tell you little about individual differences — almost everyone gets them right or wrong regardless of ability. But p-value targets must match test purpose: a mastery certification test may legitimately include many easy items if the threshold skill is expected of nearly all competent performers.

**Item discrimination** measures whether the item distinguishes between high and low scorers on the test overall. The most common index is the **point-biserial correlation** — the correlation between item response (0 = wrong, 1 = right) and total score. A high point-biserial (typically 0.30+ is considered good) means high scorers mostly got this item right and low scorers mostly got it wrong — the item is pulling in the same direction as the test. A near-zero discrimination means the item is essentially noise, contributing no information about the underlying construct. A *negative* discrimination is a red flag: high-scoring students are getting the item wrong more often than low scorers, which usually signals a miskeyed item (the wrong answer recorded as correct) or a genuinely ambiguous question.

The connection to item response theory (IRT) from your prerequisite is direct: IRT's difficulty parameter (*b*) is a more principled version of the p-value, estimated from the full item characteristic curve rather than a simple proportion. IRT's discrimination parameter (*a*) corresponds to the slope of the curve at the difficulty point — which is what the point-biserial is approximating in simpler form. Classical indices are computationally transparent and sufficient for most routine test review; IRT provides more information at the cost of greater complexity and larger sample requirements. In practice, item analysis combines both indices alongside expert review: statistics diagnose problems, but content knowledge determines the remedy.
