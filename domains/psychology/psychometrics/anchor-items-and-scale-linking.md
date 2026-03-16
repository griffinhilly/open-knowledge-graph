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
stage: advanced
status: draft
---

# Anchor Items and Scale Linking in Test Equating

## Core Idea
Anchor items are common items administered on two test forms that establish an empirical relationship for equating. Using anchor items in IRT-based equating allows test developers to bridge between test forms so that scores from different administrations can be placed on the same scale. Anchor item quality and representativeness directly affect equating accuracy.

## Explainer

From your study of item response functions, you know that IRT places both persons and items on a common latent scale — a person's ability and an item's difficulty are expressed in the same units. This is what makes IRT so powerful for equating: if two test forms share items whose scale locations are known, you can use those shared items as reference points to bring the two forms onto a common metric. These shared items are called **anchor items**, and they are the mechanism by which scores from different test forms or administrations become directly comparable.

The intuition is similar to using a known landmark to calibrate a map. If you're working with two maps drawn at different times, you can align them by identifying features that appear on both. Anchor items serve the same function: they are items administered to both groups, and their IRT parameters on the two forms should be — after linking — identical. Any discrepancy between the two calibrations of the same anchor item reflects scale drift or **parameter non-invariance**, which signals a problem with equating assumptions.

There are two main anchor designs. In an **external anchor** (or common-item nonequivalent groups) design, a subset of items from Form A is embedded in Form B and administered to a different group of test-takers. Since the groups differ in ability, the anchor items are the only basis for estimating how the two forms compare. In an **internal anchor** design, the anchor items contribute to each examinee's total score rather than being separately administered. The internal design is more efficient but requires the anchors to be representative of the full test's content and difficulty range — otherwise, the equating function will distort score distributions in ways that misrepresent true ability differences.

The quality demands on anchor items are stringent. Ideal anchors are **mini-tests**: they should span the difficulty range of the full form, cover the same content blueprint, and show no evidence of differential functioning across the two groups being linked. If anchor items are systematically easier for one group — perhaps because they reference content more familiar to that group — the equating will be contaminated. This is why anchor item selection and monitoring are among the most technically demanding aspects of large-scale assessment programs, and why careful inspection of anchor item behavior (using procedures like the Stocking-Lord or Haebara methods) is a standard step before any IRT-based scale linking is accepted as valid.
