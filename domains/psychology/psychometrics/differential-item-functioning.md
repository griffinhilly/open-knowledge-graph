---
id: differential-item-functioning
title: Differential Item Functioning and Test Bias Detection
domain: psychology
course: psychometrics
prerequisites:
- id: item-response-functions
  type: hard
- id: rasch-model
  type: hard
tags:
- dif
- test-bias
- fairness
- equitable-assessment
stage: advanced
status: draft
---

# Differential Item Functioning and Test Bias Detection

## Core Idea
Differential item functioning occurs when an item functions differently across demographic groups (e.g., gender, ethnicity) even at matched ability levels. IRT-based DIF detection and Mantel-Haenszel methods identify potentially biased items. DIF detection is critical for ensuring fairness and preventing construct-irrelevant variance from influencing scores.

## Explainer

From your work with item response theory and the Rasch model, you already know that each item has an **item characteristic curve (ICC)** — a function mapping the latent trait level (θ) to the probability of a correct response. In a perfectly fair test, this curve is the same for every group of examinees: a man and a woman with identical math ability (θ) have identical probabilities of getting any given item correct. **Differential item functioning** occurs when this assumption breaks down — when the ICC differs across groups even after controlling for the underlying construct. In other words, group membership is doing explanatory work beyond what the target trait does.

The intuition is clearest with a concrete example. Imagine a word-problem on a math test involving baseball statistics. Suppose that for any given level of mathematical ability (θ), boys answer this item correctly more often than girls. The item is not measuring only math — it is also drawing on cultural familiarity with baseball that has nothing to do with the construct being assessed. Girls at the same math ability level are at a systematic disadvantage on this item due to **construct-irrelevant variance**. That is DIF: the item functions differently across groups, not because those groups differ in the target construct, but because the item is inadvertently tapping something else.

Detecting DIF requires comparing ICC parameters across groups while **conditioning on ability**. This conditioning step is what distinguishes DIF from simple group score differences. If girls score lower on average, that alone tells us nothing about DIF — it could simply mean there is a genuine group difference in the construct. DIF requires showing that, at *matched* ability levels, item performance still differs. The **Mantel-Haenszel method** does this non-parametrically: it stratifies examinees into ability-matched subgroups and tests whether the item's difficulty is consistent across groups within each stratum. IRT-based approaches compare estimated ICC parameters (difficulty, discrimination) across the groups directly and use likelihood-ratio tests or area-between-curves metrics to quantify how different the functions are.

The critical interpretive step is that **DIF is not automatic evidence of bias**. DIF is a statistical anomaly — an item that behaves differently for different groups at the same ability level. But the reason for that difference might be entirely legitimate. If a test of English language proficiency has an item that disadvantages non-native speakers *because* non-native speakers at the same overall proficiency genuinely struggle with a particular grammatical form, the DIF might be measuring something real. If a math item disadvantages girls not because of math ability but because of culturally specific content, that is bias. DIF detection identifies candidates for investigation; the judgment about whether the differential functioning reflects bias requires substantive review by content experts.

## How It's Best Learned
Conduct DIF analysis using real assessment data and interpret practical significance of detected differences. Compare detection methods (Mantel-Haenszel vs. IRT-based) and understand how DIF affects different demographic groups.

## Common Misconceptions
DIF automatically indicates an item is biased and should be removed. DIF is evidence of potential bias warranting investigation, not definitive proof. Group differences in overall test scores do not necessarily indicate DIF in individual items.
