---
id: item-selection-and-pool-development
title: Item Selection and Item Pool Development for Tests
domain: psychology
course: psychometrics
prerequisites:
- id: item-difficulty-discrimination
  type: hard
- id: classical-test-theory
  type: hard
builds-toward:
- distractor-analysis-and-optimization
- test-development-workflow-and-project-management
tags:
- item-analysis
- item-pool
- test-construction
- item-selection
- optimal-testing
stage: expert
status: draft
---

# Item Selection and Item Pool Development for Tests

## Core Idea
Effective test development requires curating items from a larger pool based on difficulty, discrimination, reliability, and content coverage. Item selection algorithms balance competing goals: maximizing reliability, maintaining content representativeness, achieving appropriate difficulty levels, and minimizing test length. The process involves iterative pilot testing and refinement.

## Explainer

From classical test theory (CTT), you know that observed scores contain measurement error, and that reliability is the proportion of score variance attributable to true differences between people rather than random noise. Item selection is the process by which you strategically assemble items into a test that minimizes that error while also covering the construct you care about. The key insight is that you never write a final test from scratch — you write an **item pool** first, roughly two to three times larger than you need, and then select down.

Why oversample? Because items fail in predictable ways that you cannot detect until you try them on real test-takers. Some items turn out to be too easy or too hard for your target population; their **p-values** (proportion answering correctly) approach 0 or 1, meaning they discriminate no one. From your prerequisite on item difficulty and discrimination, you know that items in the .30–.70 difficulty range produce the most information about individual differences. Items outside this range are not wrong — easy items at the start can reduce anxiety, and very hard items can differentiate among the most capable — but if most items are at extremes, reliability suffers. Pilot testing reveals which items fall outside useful difficulty ranges before they contaminate your real assessment.

**Discrimination** is the second filter. A discrimination index (typically the correlation between item score and total score) measures whether getting the item right predicts getting the total test right. An item that high-scorers answer correctly and low-scorers miss is doing its job; an item that high- and low-scorers answer at equal rates is statistically useless regardless of how thoughtfully it was written. In practice, items with discrimination indices below .20 are candidates for revision or elimination. High discrimination items pull more variance into the total score's reliable true-score component, directly boosting reliability.

The tension that makes item selection genuinely hard is **statistical quality versus content coverage**. A purely statistical approach would select the 30 most discriminating items and stop — but if those 30 items all happen to assess the same narrow sub-domain, the test has poor content validity. Good item selection is constrained optimization: maximize reliability *within* the requirement that each specified content area meets its item quota from the blueprint. This is why the process is iterative: you may find that some content areas yield only weak items after pilot testing, requiring a second round of item writing before you have enough strong candidates to fill the table.

## Questions

```yaml
- question: "A test developer selects the 20 items with the highest discrimination indices from a pilot pool of 60 items and declares the test complete. What is the most significant problem with this approach?"
  type: multiple-choice
  options:
    - "Twenty items is too few — reliability requires at least 40 items"
    - "Using only the top discriminating items may produce a test that covers only a narrow slice of the construct, violating content validity"
    - "Discrimination indices are not meaningful until the final test is assembled"
    - "High-discrimination items are typically too difficult for most test-takers"
  answer: 1
  explanation: "Item selection is constrained optimization, not simple maximization. Selecting purely on discrimination ignores the content blueprint: if the top 20 discriminating items all happen to assess the same sub-domain, the test has high internal consistency but poor content validity — it measures some of the construct very reliably and ignores the rest entirely. Good item selection maximizes reliability within the binding constraint that each specified content area is adequately represented. Option A is a common intuition but not a universal rule; test length is a function of reliability goals and content requirements, not a fixed minimum."

- question: "An item on a medical licensing exam has a p-value of 0.97, meaning 97% of test-takers answered it correctly. What does this tell you about its contribution to the test?"
  type: multiple-choice
  options:
    - "It is an excellent item — all examinees answered it correctly, confirming mastery of this content area"
    - "It contributes almost nothing to reliability because it produces virtually no variance — nearly everyone passes it regardless of true ability"
    - "Its discrimination index will be high because most examinees got it right"
    - "It should be removed only if it also has low face validity"
  answer: 1
  explanation: "Reliability is driven by variance in item scores across test-takers. When 97% answer correctly, the item produces almost no variance — it cannot distinguish among test-takers because nearly everyone passes it. A discrimination index measures correlation between item score and total score; with near-zero variance on the item, that correlation will be near zero as well. The item is statistically useless for measuring individual differences. Note: very easy items can serve other purposes (reducing anxiety, serving as warm-up) but should not make up the majority of a test designed to reliably differentiate among candidates."

- question: "An item that every test-taker answers correctly contributes nothing to the reliability of the test."
  type: true-false
  answer: true
  explanation: "True. Reliability — the proportion of score variance attributable to true differences between people — depends on items that produce variance in scores. If every test-taker answers an item correctly (p-value = 1.0), that item has zero variance. Zero-variance items cannot correlate with anything, including the total test score, so their discrimination index is zero. They contribute no information about individual differences and do not improve reliability. They may still serve other purposes (e.g., gauging absolute mastery of a critical safety item), but they are statistically inert for reliability purposes."

- question: "The goal of item selection is to maximize the average discrimination index across all selected items, regardless of other considerations."
  type: true-false
  answer: false
  explanation: "False. Item selection is constrained optimization: the goal is to maximize reliability (which discrimination indices contribute to) *within* the requirement that each content area specified in the test blueprint meets its item quota. A purely statistical approach that ignores the content blueprint would sacrifice content validity — the test might be internally consistent but measure only a narrow part of the intended construct. Additionally, item difficulty distribution matters: an overly narrow difficulty range reduces the test's ability to differentiate across the ability spectrum. Discrimination is one important criterion, not the sole objective."

- question: "Why must test developers write an item pool two to three times larger than the final test, rather than writing exactly the items they intend to use?"
  type: short-answer
  answer: "Because item properties cannot be predicted before pilot testing. Some items will turn out too easy or too hard (p-values near 0 or 1), producing little variance and low discrimination. Others will be ambiguous, poorly worded, or biased against subgroups — problems that only emerge when real test-takers respond. A large pool provides enough candidates in each content area that after eliminating poorly performing items, sufficient high-quality items remain to fill the content blueprint without compromising difficulty distribution or reliability."
  explanation: "The item pool exists to absorb attrition. Pilot testing is the quality control step that reveals which items work as intended. If you start with exactly the items you plan to use and several fail psychometric criteria, you either have to use weak items (harming reliability) or leave content areas undercovered (harming validity). The pool provides redundancy: for each content specification, you want multiple viable candidates so that statistical filtering still leaves adequate coverage."
```

## How It's Best Learned
Start with item statistics (difficulty p-values and discrimination indices) and learn to identify strong vs. weak items. Practice selecting items to achieve target difficulty levels and maximize internal consistency. Understand trade-offs between test length, reliability, and practical constraints.
