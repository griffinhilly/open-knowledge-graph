---
id: anchor-items-and-scale-linking
title: Anchor Items and Scale Linking in Test Equating
domain: psychology
course: psychometrics
prerequisites:
- id: item-response-functions
  type: hard
- id: test-equating-and-linking
  type: soft
builds-toward:
- score-linking-and-concordance-tables
tags:
- equating
- anchor-items
- scale-linking
- irt
- item-banking
stage: expert
status: draft
---

# Anchor Items and Scale Linking in Test Equating

## Core Idea
Anchor items are common items administered on two test forms that establish an empirical relationship for equating. Using anchor items in IRT-based equating allows test developers to bridge between test forms so that scores from different administrations can be placed on the same scale. Anchor item quality and representativeness directly affect equating accuracy.

## Questions

```yaml
- question: "An anchor set for a mathematics certification exam consists entirely of arithmetic computation items, while the full exam also covers algebra and geometry. What is the most likely consequence for equating?"
  type: multiple-choice
  options:
    - "The equating will be more accurate because arithmetic is foundational to the other content areas"
    - "The anchor items will show more parameter drift than a representative anchor set"
    - "Score comparisons may be distorted for examinees who differ specifically in algebra and geometry ability, since those dimensions are unrepresented in the anchor"
    - "Equating will fail entirely because IRT requires anchors to span all content areas equally"
  answer: 2
  explanation: "Anchor items must function as mini-tests — representative of the full form's content and difficulty range. If anchors only capture arithmetic, the equating function is calibrated only on that slice of the construct. Groups that differ in algebra or geometry ability will have those differences misrepresented when scores are placed on the common scale. This is a concrete example of why anchor representativeness is treated as a stringent technical requirement, not just a best practice."

- question: "Two test forms are being equated using an external anchor design. What makes scores from the two forms comparable after IRT-based linking?"
  type: multiple-choice
  options:
    - "Both forms are administered to groups that have been matched on demographic characteristics"
    - "The anchor items provide a common reference set whose IRT parameters should be identical across calibrations after the linking transformation is applied"
    - "Both forms are constructed to have identical average difficulty before administration"
    - "A raw-score conversion table replaces the need for IRT scaling by mapping scores directly between forms"
  answer: 1
  explanation: "IRT places persons and items on a common latent scale, but each form is calibrated independently — so two calibrations of the same item may produce slightly different parameter estimates due to the different groups tested. Linking uses the anchor items as landmarks: after the transformation, the same anchor item should have identical parameters in both calibrations. The discrepancy between pre- and post-linking anchor parameters is how analysts diagnose whether the linking is working — persistent discrepancies signal parameter non-invariance."

- question: "If anchor items show differential item functioning (DIF) — performing systematically differently across the two groups being linked — the resulting scale linking will be biased even when IRT calibration is otherwise technically correct."
  type: true-false
  answer: true
  explanation: "DIF in anchor items is one of the most serious threats to equating validity. Anchor items work as reference points precisely because they should function the same way across groups. If an anchor item is systematically easier for one group (perhaps because it references culturally familiar content), it provides a biased reference point, and the linking transformation will shift scores in a way that misrepresents true ability differences. This is why anchor item monitoring using procedures like Stocking-Lord or Haebara methods is a standard step before accepting any scale linking."

- question: "In an external anchor design, anchor items must contribute to each examinee's total score in order to provide a valid basis for scale linking."
  type: true-false
  answer: false
  explanation: "This describes the internal anchor design, not the external one. In an external anchor design, the anchor items are administered separately and do not count toward examinees' total scores — they exist solely to bridge the two calibrations. In an internal anchor design, anchor items do contribute to total scores, which has efficiency advantages but requires more careful attention to representativeness. Conflating the two designs is a common confusion in equating discussions."

- question: "Why must anchor items be representative of the full test's content and difficulty range, rather than just any items shared across forms?"
  type: short-answer
  answer: "Anchor items function as a mini-test used to estimate how the two forms compare in difficulty and content. If anchors only sample one difficulty level or content area, the equating function is calibrated on that narrow slice, and it may misrepresent how the forms compare for examinees whose abilities lie in the unrepresented range. A representative anchor set ensures the linking transformation is valid across the full score range and content domain, not just for the specific subset the anchors happen to measure."
  explanation: "The analogy is calibrating a map using only landmarks from one neighborhood — the alignment may be accurate for that area but distort distances everywhere else. Anchor representativeness is the condition that makes the linking transformation generalizable rather than locally valid, which is why large-scale testing programs invest heavily in anchor item construction and monitoring."
```

## Explainer

From your study of item response functions, you know that IRT places both persons and items on a common latent scale — a person's ability and an item's difficulty are expressed in the same units. This is what makes IRT so powerful for equating: if two test forms share items whose scale locations are known, you can use those shared items as reference points to bring the two forms onto a common metric. These shared items are called **anchor items**, and they are the mechanism by which scores from different test forms or administrations become directly comparable.

The intuition is similar to using a known landmark to calibrate a map. If you're working with two maps drawn at different times, you can align them by identifying features that appear on both. Anchor items serve the same function: they are items administered to both groups, and their IRT parameters on the two forms should be — after linking — identical. Any discrepancy between the two calibrations of the same anchor item reflects scale drift or **parameter non-invariance**, which signals a problem with equating assumptions.

There are two main anchor designs. In an **external anchor** (or common-item nonequivalent groups) design, a subset of items from Form A is embedded in Form B and administered to a different group of test-takers. Since the groups differ in ability, the anchor items are the only basis for estimating how the two forms compare. In an **internal anchor** design, the anchor items contribute to each examinee's total score rather than being separately administered. The internal design is more efficient but requires the anchors to be representative of the full test's content and difficulty range — otherwise, the equating function will distort score distributions in ways that misrepresent true ability differences.

The quality demands on anchor items are stringent. Ideal anchors are **mini-tests**: they should span the difficulty range of the full form, cover the same content blueprint, and show no evidence of differential functioning across the two groups being linked. If anchor items are systematically easier for one group — perhaps because they reference content more familiar to that group — the equating will be contaminated. This is why anchor item selection and monitoring are among the most technically demanding aspects of large-scale assessment programs, and why careful inspection of anchor item behavior (using procedures like the Stocking-Lord or Haebara methods) is a standard step before any IRT-based scale linking is accepted as valid.
