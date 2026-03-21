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

## Questions

```yaml
- question: "A math test item is answered correctly by 72% of male examinees and 54% of female examinees. A researcher concludes the item shows DIF. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "DIF can only be detected using IRT, not raw score comparisons, so the method is invalid"
    - "DIF requires showing that the group performance difference persists after conditioning on ability — the score gap alone could reflect genuine group differences in the construct, not item-specific bias"
    - "The score gap is too small to constitute DIF; a gap of at least 25 percentage points is needed"
    - "DIF analysis requires the two groups to be matched in sample size before comparison"
  answer: 1
  explanation: "This is the central conceptual error in DIF analysis. A raw score gap between groups tells you nothing about DIF because it could simply reflect real differences in the underlying construct (math ability). DIF requires showing that, at *matched* ability levels, the item still behaves differently across groups. Without conditioning on ability, you cannot separate legitimate construct differences from item-specific bias. The conditioning step is what defines DIF."

- question: "A test of English language proficiency includes an item that shows DIF against non-native speakers. Content reviewers find that the item uses a grammatical construction that is genuinely difficult for non-native speakers at any given proficiency level because it targets a specific feature of advanced English grammar. How should this DIF be classified?"
  type: multiple-choice
  options:
    - "As bias requiring immediate removal — any DIF against a minority group is by definition biased"
    - "Potentially as legitimate DIF — the differential functioning may reflect the target construct itself rather than irrelevant content"
    - "As negligible — DIF only matters when it affects groups by more than one standard deviation"
    - "As an IRT calibration error requiring the item to be recalibrated using the non-native speaker subsample"
  answer: 1
  explanation: "DIF is a statistical finding, not automatic evidence of bias. The DIF here could be legitimate if the grammatical feature being tested is genuinely part of English language proficiency — in which case non-native speakers at the same overall proficiency level might genuinely differ on this specific aspect of the construct. Bias requires DIF due to *construct-irrelevant* content. Content expert review is the essential next step: DIF identifies items for investigation; it does not determine by itself whether the differential functioning is appropriate or problematic."

- question: "A group scoring significantly lower on an overall test than another group provides sufficient statistical evidence that specific items in the test show DIF against the lower-scoring group."
  type: true-false
  answer: false
  explanation: "Overall group score differences and DIF are logically independent. A lower-scoring group might simply have lower levels of the construct being measured — which is not DIF. DIF requires showing that specific items perform differently for different groups at the *same* ability level. You can have large overall group differences with no DIF on any individual item (if the group difference reflects the construct uniformly), or you can have items with DIF even when overall group means are identical."

- question: "The Mantel-Haenszel method detects DIF by stratifying examinees into ability-matched subgroups and testing whether each item's difficulty is consistent across demographic groups within each stratum."
  type: true-false
  answer: true
  explanation: "This is an accurate description of the Mantel-Haenszel approach. By creating subgroups of examinees matched on overall performance (as a proxy for ability), the method controls for ability before comparing item performance across demographic groups. This non-parametric approach does not require fitting an IRT model and remains widely used because it is computationally straightforward and interpretable. It directly implements the 'conditioning on ability' logic that defines DIF detection."

- question: "Why is 'conditioning on ability' the essential step in DIF detection, and what does the analysis fail to show without it?"
  type: short-answer
  answer: "DIF is defined as differential item functioning at matched ability levels — the same item behaving differently for examinees who are otherwise equivalent on the target construct. Without conditioning on ability, a group performance difference on an item cannot be distinguished from a genuine group difference in the trait being measured. If you simply compare raw scores without matching on ability, you cannot tell whether the item is biased or whether the groups simply differ in the construct. Conditioning on ability isolates the item-specific effect from the construct-level effect."
  explanation: "The intuition is that DIF asks a counterfactual: 'If I could compare two examinees with identical ability but from different demographic groups, would this item treat them identically?' That counterfactual requires ability-matching. Without it, you cannot answer the DIF question at all — you can only observe that groups differ, which is a different (and much less interesting) finding."
```

## Explainer

From your work with item response theory and the Rasch model, you already know that each item has an **item characteristic curve (ICC)** — a function mapping the latent trait level (θ) to the probability of a correct response. In a perfectly fair test, this curve is the same for every group of examinees: a man and a woman with identical math ability (θ) have identical probabilities of getting any given item correct. **Differential item functioning** occurs when this assumption breaks down — when the ICC differs across groups even after controlling for the underlying construct. In other words, group membership is doing explanatory work beyond what the target trait does.

The intuition is clearest with a concrete example. Imagine a word-problem on a math test involving baseball statistics. Suppose that for any given level of mathematical ability (θ), boys answer this item correctly more often than girls. The item is not measuring only math — it is also drawing on cultural familiarity with baseball that has nothing to do with the construct being assessed. Girls at the same math ability level are at a systematic disadvantage on this item due to **construct-irrelevant variance**. That is DIF: the item functions differently across groups, not because those groups differ in the target construct, but because the item is inadvertently tapping something else.

Detecting DIF requires comparing ICC parameters across groups while **conditioning on ability**. This conditioning step is what distinguishes DIF from simple group score differences. If girls score lower on average, that alone tells us nothing about DIF — it could simply mean there is a genuine group difference in the construct. DIF requires showing that, at *matched* ability levels, item performance still differs. The **Mantel-Haenszel method** does this non-parametrically: it stratifies examinees into ability-matched subgroups and tests whether the item's difficulty is consistent across groups within each stratum. IRT-based approaches compare estimated ICC parameters (difficulty, discrimination) across the groups directly and use likelihood-ratio tests or area-between-curves metrics to quantify how different the functions are.

The critical interpretive step is that **DIF is not automatic evidence of bias**. DIF is a statistical anomaly — an item that behaves differently for different groups at the same ability level. But the reason for that difference might be entirely legitimate. If a test of English language proficiency has an item that disadvantages non-native speakers *because* non-native speakers at the same overall proficiency genuinely struggle with a particular grammatical form, the DIF might be measuring something real. If a math item disadvantages girls not because of math ability but because of culturally specific content, that is bias. DIF detection identifies candidates for investigation; the judgment about whether the differential functioning reflects bias requires substantive review by content experts.

## How It's Best Learned
Conduct DIF analysis using real assessment data and interpret practical significance of detected differences. Compare detection methods (Mantel-Haenszel vs. IRT-based) and understand how DIF affects different demographic groups.

## Common Misconceptions
DIF automatically indicates an item is biased and should be removed. DIF is evidence of potential bias warranting investigation, not definitive proof. Group differences in overall test scores do not necessarily indicate DIF in individual items.
