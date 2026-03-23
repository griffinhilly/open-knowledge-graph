---
id: score-linking-and-concordance-tables
title: Score Linking and Concordance Tables
domain: psychology
course: psychometrics
prerequisites:
- id: test-equating-and-linking
  type: hard
- id: measurement-scales-psychology
  type: soft
tags:
- linking
- concordance
- scale-translation
- equating
- score-conversion
stage: expert
status: draft
---

# Score Linking and Concordance Tables

## Core Idea
Score linking creates empirical relationships between scales measuring related constructs (e.g., old and new versions of a test, or different tests of similar constructs), enabling researchers to translate scores from one test to another. Concordance tables or regression equations allow comparison of scores and facilitate interpretation when multiple measures exist. Linking assumes the constructs are sufficiently similar and requires sufficient overlap data.

## Questions

```yaml
- question: "A university uses a concordance table to treat concorded ACT and SAT scores as fully interchangeable for admissions — accepting a 28 ACT as identical to a 1300 SAT. A psychometrician objects. What is the most defensible reason for the objection?"
  type: multiple-choice
  options:
    - "The concordance table was likely built from an unrepresentative sample, making percentile matching unreliable"
    - "Concorded scores reflect equivalent percentile ranks but not interchangeable constructs — the tests differ enough that treating them as identical overstates precision"
    - "Equipercentile linking systematically underestimates ACT scores relative to SAT scores at the high end"
    - "Regression-based linking would have produced a more accurate concordance than equipercentile methods"
  answer: 1
  explanation: "The key distinction is equating versus concordance. Equated scores (parallel forms of the same test) are interchangeable. Concorded scores are comparable estimates — the SAT and ACT measure overlapping but non-identical constructs (the ACT includes a science section; formats and timing differ). Matching percentile distributions says nothing about construct identity. The admission office is treating a concordance as if it were an equating, ignoring the additional uncertainty that imperfect construct overlap introduces."

- question: "A researcher pools data from two studies that used different depression screening instruments by regressing Instrument B scores onto Instrument A scores. What limitation should she specifically flag in her methods section?"
  type: multiple-choice
  options:
    - "Regression-based linking will exaggerate extreme scores on Instrument B, inflating apparent severity"
    - "Regression-based linking will compress predicted scores — extreme Instrument A scorers will have less extreme predicted Instrument B scores than their actual scores would be"
    - "Regression-based linking cannot be applied unless both instruments use identical response formats"
    - "Regression-based linking assumes the instruments measure completely unrelated constructs"
  answer: 1
  explanation: "Regression to the mean is the critical limitation. Predicted values from a regression are always more compressed (closer to the mean) than the observed distribution. Someone in the extreme 95th percentile on Instrument A will be predicted at a less extreme percentile on Instrument B. Concordance tables using equipercentile methods avoid this compression by directly matching observed score distributions rather than predicting through a regression line — making them preferable when preserving the full score range matters."

- question: "A concorded score is an estimate of the score range a test-taker would likely achieve on the other instrument — not a precise equivalent that can be treated as interchangeable with the original score."
  type: true-false
  answer: true
  explanation: "This is the defining distinction between equating and concordance. Equated scores from parallel test forms are interchangeable — admission officers can treat them identically. Concorded scores carry inherent uncertainty due to imperfect construct overlap between the instruments. They are useful for rough comparisons and population-level interpretations, but should not be used to make high-stakes individual decisions that hinge on precise cutpoints."

- question: "Because equipercentile linking matches the full score distributions of two tests, it guarantees that scores mapped to the same percentile rank are measuring the same underlying construct."
  type: true-false
  answer: false
  explanation: "Equipercentile linking is a distributional alignment procedure — it identifies scores where equal proportions of test-takers fall below. This says nothing about what the tests measure. Two tests with completely different content would produce a concordance table just the same. Construct validity — whether two scores reflect the same underlying trait — requires separate evidence from the statistical linking procedure. Matching percentile ranks establishes comparability in rank, not equivalence in meaning."

- question: "Explain the key difference between equating and concordance, and give a concrete example of when treating a concorded score as equated would lead to a problematic decision."
  type: short-answer
  answer: "Equated scores come from parallel forms of the same test measuring the identical construct at equivalent difficulty — they are interchangeable. Concorded scores link different instruments measuring related but non-identical constructs — they are comparable estimates carrying additional uncertainty from imperfect construct overlap. Example of a problematic decision: using an SAT-ACT concordance to deny admission to a student whose concorded score falls exactly at the cutoff, when the uncertainty in the concordance could easily span several points in either direction. Or translating a clinical depression cutoff from one screening instrument to another via concordance and treating the translated cutoff as precise, when construct differences mean the threshold may not carry over."
```

## Explainer

From your study of test equating and linking, you know that **equating** refers to the strict case of creating interchangeable scores across parallel forms of the same test — forms designed to measure the identical construct at the same difficulty level with the same scaling. **Score linking** is the broader family of methods that includes equating but extends to situations where tests are similar but not identical, and where the goal is translation rather than strict interchangeability.

The most common application is the **concordance table** — an empirically derived lookup table that maps scores from one test to scores on another. A familiar example is the SAT-ACT concordance: because millions of students take one or both, researchers can identify the ACT composite score that corresponds to each SAT total score by finding the scores at equivalent percentile ranks in the overlap sample. If 70% of students who score a 28 on the ACT score below a 1300 on the SAT, and 70% of students who score 1300 on the SAT score below a 1300, then 28 ACT ≈ 1300 SAT by **equipercentile linking**. This approach requires no strong parametric assumptions — it simply matches the percentile distributions.

The critical distinction you must hold onto is between **equating** and **concordance**, and the difference lies in what you can claim afterward. Equated scores are interchangeable — a 500 on Form A means the same thing as a 500 on Form B, and admission officers can treat them identically. Concorded scores are merely *comparable* — a concorded ACT score is an estimate of the score range a student would likely achieve on the SAT, but it carries more uncertainty and should not be treated as exact. The reason is **construct overlap**: the SAT and ACT measure overlapping but non-identical constructs (the ACT has a science section; the two differ in timing and format). When construct overlap is imperfect, equipercentile correspondence does not imply score exchangeability.

**Regression-based linking** is an alternative approach, particularly useful in research contexts. If you have a sample that completed both instruments, you can regress scores on one test onto the other and use the regression equation to predict one from the other. This is simpler but inherits a limitation: regression to the mean means predicted scores will be more compressed than actual scores — extreme scorers on one test will be predicted as less extreme on the other. Concordance tables using equipercentile methods avoid this compression. Understanding these trade-offs matters whenever you need to pool data from studies using different instruments, translate clinical cutoffs from one screening tool to another, or interpret scores when a test is revised and the new version cannot be directly equated to the old.
