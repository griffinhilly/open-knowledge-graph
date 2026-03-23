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
stage: expert
status: validated
---

# Score Linking and Test Equating Methods

## Core Idea
Test equating adjusts scores on different forms to make them comparable; if Form A is easier, equating maps Form A scores to Form B scale. Equating assumes equal constructs measured with equal precision. When assumptions fail, linking or concordance is more appropriate. Design (equipercentile, linear, IRT) and sample design affect accuracy.

## Questions

```yaml
- question: "A university converts SAT and ACT scores to a common 1600-point scale using a published concordance table. An admissions officer says 'a 1200 on our scale means the same thing whether it came from SAT or ACT.' Is this defensible?"
  type: multiple-choice
  options:
    - "Yes — the concordance was derived from a large sample of students who took both tests, making the scores equivalent"
    - "No — SAT and ACT measure overlapping but non-identical constructs with different reliabilities, so the conversion is a concordance, not an equating; the scores are not fully interchangeable"
    - "Yes — both tests are normed to the same college-bound population, which makes their scales equivalent"
    - "No — common-item equating was not used, so no valid comparison is possible"
  answer: 1
  explanation: "True equating requires that both forms measure the same construct with equal reliability. SAT and ACT overlap substantially but differ in construct coverage (e.g., ACT includes a science reasoning section; the SAT emphasizes evidence-based reading differently). A concordance table translates scores statistically but does not make them fully interchangeable — it documents a predictive relationship, not construct equivalence. Claiming the scores 'mean the same thing' overstates what concordance can support."

- question: "Two forms of a reading test are built to identical blueprints, but Form B turns out slightly harder. Student X scores 68 on the harder Form B; Student Y scores 68 on the easier Form A. Without equating, what is the correct interpretation of their scores?"
  type: multiple-choice
  options:
    - "Both students have equivalent ability — they answered the same number of items correctly"
    - "Student X demonstrated more ability — achieving the same raw score on a harder form indicates higher proficiency"
    - "Student Y demonstrated more ability — Form A's lower difficulty means Y answered easier items correctly"
    - "No comparison is possible without knowing each student's raw score percentile"
  answer: 1
  explanation: "The same raw score on a harder form represents greater demonstrated ability than on an easier form. This is precisely the problem equating solves: it maps raw scores to a common scale so that equivalent scaled scores represent equivalent ability, regardless of which form was taken. Without equating, identical raw scores on forms of different difficulty are not comparable — the student who took the harder form is systematically underrepresented."

- question: "Equipercentile equating maps a score on Form A to the score on Form B that corresponds to the same percentile rank in the equating sample."
  type: true-false
  answer: true
  explanation: "This is the defining logic of equipercentile equating. If the 80th percentile on Form A is a raw score of 64, and the 80th percentile on Form B is a raw score of 61, then Form A raw 64 equates to Form B raw 61. The method requires no assumption about the shape of the score distributions and adjusts for differences in both central tendency and spread, making it more flexible than linear equating when score distributions are asymmetric or differently shaped."

- question: "Any two tests that measure related psychological constructs and are administered to similar populations can be equated to make their scores fully interchangeable."
  type: true-false
  answer: false
  explanation: "Equating requires that both forms measure the same construct with equal reliability and equal construct representation. When this assumption fails — because the tests differ in what they measure — only concordance or linking is appropriate. Concordance establishes a statistical translation between the scales but does not make scores interchangeable. Treating a concordance as an equating implies a level of comparability the data do not support, and can lead to consequential errors in selection and comparison decisions."

- question: "Explain the difference between test equating and concordance, and why conflating the two is a practical problem in educational or clinical settings."
  type: short-answer
  answer: "Equating adjusts scores on different forms of the same test to a common scale, making identical scaled scores truly interchangeable — a student who took Form A and one who took Form B with the same scaled score demonstrated the same ability. Concordance statistically relates scores from different tests measuring overlapping but non-identical constructs; the resulting translations are predictive, not equivalent. Conflating the two is a problem because decision-makers may treat concordanced scores as if they were equated — for example, using an SAT-to-ACT conversion to claim a student meets a cutoff they would not have met if they'd actually taken the other test. This overclaims comparability and can disadvantage test-takers."
  explanation: "The conceptual crux is that equating preserves construct identity across forms, while concordance only preserves statistical prediction. The distinction matters most in high-stakes contexts: admissions cutoffs, clinical diagnostics, and credentialing."
```

## Explainer

From your work on parallel test forms, you know that different forms are built to the same specifications — same content blueprint, same difficulty distribution, same reliability targets — so that no test-taker is advantaged or disadvantaged by which form they receive. But "built to the same specification" is not the same as "identically difficult in practice." Random variation in item selection means Form A will almost always end up slightly easier or harder than Form B, even with excellent blueprinting. **Test equating** is the statistical process that corrects for this, making it possible to report scores from different forms on the same interpretable scale.

The conceptual core is simple: if Form A is easier, then a given raw score on Form A represents less demonstrated ability than the same raw score on Form B. Equating maps raw scores from one form to their equivalent on a common scale so that identical scaled scores represent identical ability levels regardless of which form was administered. Think of it like currency exchange: the exchange rate between two currencies isn't arbitrary — it reflects something real about the underlying economies. Similarly, equating ratios reflect real differences in form difficulty, derived from how actual test-takers performed on the items.

Several **equating designs** exist, each with different data requirements and assumptions. **Random groups equating** assigns Form A to one randomly drawn group and Form B to another; because the groups are equivalent by randomization, raw score differences between the forms can be attributed entirely to form difficulty. **Common-item equating** (anchor equating) embeds a set of identical items across both forms; these **anchor items** link the two forms to a shared scale without requiring the same group of people to take both. **IRT-based equating** places all items on a latent ability scale using item response theory parameters, then derives the equating transformation from those parameters — the most flexible approach and the standard for high-stakes testing programs where multiple forms circulate simultaneously.

The distinction between **equating** and **linking** is the conceptual crux of this topic. True equating requires that both forms measure the same construct with equal reliability and equal construct representation — only then can you claim that a score of 75 on Form A is truly interchangeable with 75 on Form B. When forms diverge in construct coverage (one form emphasizes reasoning items, another emphasizes computation), you can establish a **concordance** — a statistical translation between the two scales — but the scores are not fully interchangeable. A SAT Math score converted to an ACT Math score is a concordance, not an equating: the tests measure overlapping but non-identical constructs. Treating a concordance as an equating implies more score comparability than the data support and is a common error in operational test use.

**Equipercentile equating** is the most intuitive method: it maps the score at the Xth percentile on Form A to whatever score on Form B falls at the same percentile. If the 75th percentile on Form A is a raw score of 62, and the 75th percentile on Form B is 59, then Form A raw 62 equates to Form B raw 59. **Linear equating** assumes the two score distributions have the same shape and adjusts only for mean and standard deviation differences — simpler but more assumption-dependent. When distributions are markedly non-normal or differently shaped, equipercentile methods are preferred. In practice, equating accuracy depends on sample size (equating functions are estimated with error), the quality of the anchor design, and how well the equating assumptions are met — which is why large testing programs invest substantially in equating research before operational score reporting.
