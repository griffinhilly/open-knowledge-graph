---
id: score-linking-and-test-equating
title: Score Linking and Test Equating Methods
domain: psychology
course: psychometrics
prerequisites:
- id: parallel-and-equivalent-test-forms
  type: hard
- id: test-development-specifications-blueprints
  type: hard
tags:
- equating
- score-linking
- test-forms
- comparability
stage: advanced
status: draft
---

# Score Linking and Test Equating Methods

## Core Idea
Test equating adjusts scores on different forms to make them comparable; if Form A is easier, equating maps Form A scores to Form B scale. Equating assumes equal constructs measured with equal precision. When assumptions fail, linking or concordance is more appropriate. Design (equipercentile, linear, IRT) and sample design affect accuracy.

## Explainer

From your work on parallel test forms, you know that different forms are built to the same specifications — same content blueprint, same difficulty distribution, same reliability targets — so that no test-taker is advantaged or disadvantaged by which form they receive. But "built to the same specification" is not the same as "identically difficult in practice." Random variation in item selection means Form A will almost always end up slightly easier or harder than Form B, even with excellent blueprinting. **Test equating** is the statistical process that corrects for this, making it possible to report scores from different forms on the same interpretable scale.

The conceptual core is simple: if Form A is easier, then a given raw score on Form A represents less demonstrated ability than the same raw score on Form B. Equating maps raw scores from one form to their equivalent on a common scale so that identical scaled scores represent identical ability levels regardless of which form was administered. Think of it like currency exchange: the exchange rate between two currencies isn't arbitrary — it reflects something real about the underlying economies. Similarly, equating ratios reflect real differences in form difficulty, derived from how actual test-takers performed on the items.

Several **equating designs** exist, each with different data requirements and assumptions. **Random groups equating** assigns Form A to one randomly drawn group and Form B to another; because the groups are equivalent by randomization, raw score differences between the forms can be attributed entirely to form difficulty. **Common-item equating** (anchor equating) embeds a set of identical items across both forms; these **anchor items** link the two forms to a shared scale without requiring the same group of people to take both. **IRT-based equating** places all items on a latent ability scale using item response theory parameters, then derives the equating transformation from those parameters — the most flexible approach and the standard for high-stakes testing programs where multiple forms circulate simultaneously.

The distinction between **equating** and **linking** is the conceptual crux of this topic. True equating requires that both forms measure the same construct with equal reliability and equal construct representation — only then can you claim that a score of 75 on Form A is truly interchangeable with 75 on Form B. When forms diverge in construct coverage (one form emphasizes reasoning items, another emphasizes computation), you can establish a **concordance** — a statistical translation between the two scales — but the scores are not fully interchangeable. A SAT Math score converted to an ACT Math score is a concordance, not an equating: the tests measure overlapping but non-identical constructs. Treating a concordance as an equating implies more score comparability than the data support and is a common error in operational test use.

**Equipercentile equating** is the most intuitive method: it maps the score at the Xth percentile on Form A to whatever score on Form B falls at the same percentile. If the 75th percentile on Form A is a raw score of 62, and the 75th percentile on Form B is 59, then Form A raw 62 equates to Form B raw 59. **Linear equating** assumes the two score distributions have the same shape and adjusts only for mean and standard deviation differences — simpler but more assumption-dependent. When distributions are markedly non-normal or differently shaped, equipercentile methods are preferred. In practice, equating accuracy depends on sample size (equating functions are estimated with error), the quality of the anchor design, and how well the equating assumptions are met — which is why large testing programs invest substantially in equating research before operational score reporting.
