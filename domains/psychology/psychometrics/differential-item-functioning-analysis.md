---
id: differential-item-functioning-analysis
title: 'Differential Item Functioning: Detection and Interpretation'
domain: psychology
course: psychometrics
prerequisites:
- id: differential-item-functioning
  type: hard
- id: item-information-function-test-precision
  type: soft
- id: chi-square-test
  type: soft
- id: chi-square-distribution-theory
  type: soft
- id: chi-square-test-independence-theory
  type: soft
builds-toward:
- measurement-invariance-equivalence
tags:
- dif
- measurement-bias
- fairness
- item-analysis
stage: advanced
status: draft
---

# Differential Item Functioning: Detection and Interpretation

## Core Idea
Differential item functioning occurs when groups have different item response probabilities after matching on ability. Detected via logistic regression, Mantel-Haenszel, or IRT methods; uniform DIF shows constant differences, nonuniform DIF shows ability-level interactions. DIF is statistical evidence; deciding whether flagged items are biased requires qualitative judgment about content and context.

## Explainer

Your prerequisite on differential item functioning introduced the core definition: an item exhibits DIF when examinees from different groups who have the same underlying ability nevertheless differ in their probability of answering correctly. This topic deepens that definition into a methodology — how do you actually detect DIF, how do you distinguish its forms, and what do you do when you find it?

The fundamental challenge in DIF detection is matching on ability without already knowing the ability you're trying to measure. You can't simply compare group pass rates, because those rates might differ due to genuine ability differences rather than item bias. The solution is **conditional comparison**: group examinees by their total test score (a proxy for ability) and then compare item pass rates within each score level. An item showing DIF will have systematically different pass rates between groups at the same score level. The **Mantel-Haenszel procedure** formalizes this: it computes a weighted odds ratio comparing group performance across score strata, producing a single effect size index. **Logistic regression** extends this by modeling the probability of a correct response as a function of group membership, total score, and their interaction. **IRT-based methods** go further, comparing the estimated item characteristic curves directly between groups to see if the item's parameters differ.

The distinction between **uniform DIF** and **nonuniform DIF** matters both statistically and substantively. Uniform DIF means one group consistently outperforms the other at every ability level — the item characteristic curves run parallel but offset. Nonuniform DIF means the advantage reverses or changes across ability levels — the curves cross. A vocabulary item that uses formal academic language might show uniform DIF against students from lower socioeconomic backgrounds at all ability levels. A timed arithmetic item might show nonuniform DIF if test-taking speed strategies differ between groups only at high ability levels. Logistic regression detects both types via main effect and interaction terms; Mantel-Haenszel only detects uniform DIF.

The most important conceptual point is the **DIF-bias distinction**. DIF is a statistical finding; bias is a normative judgment. Not all DIF indicates bias. An item about physics equipment on a science test might show DIF favoring students from well-resourced schools — but if the curriculum standards require knowledge of physics equipment, the DIF may reflect real differences in opportunity to learn, not an unfairly constructed item. Conversely, some items without detected DIF may still be conceptually problematic. DIF analysis is therefore best understood as a **flagging tool**: it identifies items that warrant careful qualitative review by content experts, test developers, and fairness specialists. The statistical flag opens an investigation; it doesn't close it.
