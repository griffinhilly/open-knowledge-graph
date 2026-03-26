---
id: split-half-reliability-spearman-brown
title: Split-Half Reliability and the Spearman-Brown Prophecy Formula
domain: psychology
course: psychometrics
prerequisites:
- id: test-retest-reliability
  type: hard
- id: alpha-reliability-internal-consistency
  type: soft
builds-toward:
- reliability-estimation-method-selection
tags:
- split-half
- spearman-brown
- reliability-estimation
stage: expert
status: validated
---

# Split-Half Reliability and the Spearman-Brown Prophecy Formula

## Core Idea
Split-half reliability divides a test into two halves, correlates them, and applies the Spearman-Brown formula to estimate full-length reliability: r_xx = 2r / (1 + r). This method is computationally simple but sensitive to how items are split; odd-even splits are preferable to arbitrary divisions to control for fatigue and item-order effects.

## Questions

```yaml
- question: "A 100-item test is split into odd and even halves. The correlation between the two half-scores is r = .76. What should be reported as the split-half reliability of the full 100-item test?"
  type: multiple-choice
  options:
    - "Apply the Spearman-Brown formula: 2(.76) / (1 + .76) ≈ .86"
    - "The split-half reliability is .76 — the correlation between the two halves is the reliability estimate"
    - "The split-half reliability is .76 / 2 = .38 — the correlation must be halved since each half is half as long"
    - "No reliability can be estimated from a single administration; a second administration is required"
  answer: 0
  explanation: "The raw correlation of .76 is the reliability of a 50-item test — half the actual length. Reporting .76 as the full test's reliability would systematically underestimate it. The Spearman-Brown formula corrects for this: 2(.76) / (1.76) ≈ .864. The formula works because reliability increases predictably with test length — doubling the number of parallel items is equivalent to the correction Spearman-Brown applies. Option B is the classic mistake: treating the half-test correlation as the full-test reliability."

- question: "A researcher splits a 60-item test into items 1–30 versus items 31–60 and reports a correlation of .68. A colleague uses odd-even items instead and reports .74. Why does the split type matter?"
  type: multiple-choice
  options:
    - "Fatigue and strategy drift late in the test systematically depress scores in the second half, deflating the first-half/second-half correlation — not because the test is unreliable, but because the halves were taken under different conditions"
    - "The first-half/second-half split includes harder items in the second half, creating a difficulty imbalance that lowers validity"
    - "The odd-even split artificially inflates reliability by mixing item types across halves"
    - "Both splits should produce the same result; the difference reflects random sampling error"
  answer: 0
  explanation: "The first-half/second-half split confounds reliability with test-taking conditions. If participants tire, lose concentration, or change strategy as the test progresses, the second-half scores are systematically different from what they'd be under fresh conditions — and this systematic difference lowers the correlation, making the test look less reliable than it actually is. Odd-even splitting distributes the effects of fatigue and practice equally across both halves, removing the confound. This is a real measurement artifact, not trivial."

- question: "The raw correlation between the two halves of a split-half reliability analysis underestimates the full test's reliability because it reflects only the consistency of a half-length test."
  type: true-false
  answer: true
  explanation: "This is the core insight behind the Spearman-Brown correction. Reliability increases with test length — more items means more sampling of the construct, more averaging out of random error. The half-test correlation estimates how reliable 50 items are, not 100. Because a 100-item test is inherently more reliable than a 50-item version of the same test, reporting the raw half-test correlation as the full test's reliability is a systematic underestimate. The Spearman-Brown formula predicts how much reliability increases when you effectively double the test."

- question: "The Spearman-Brown prophecy formula can primarily be used to predict the reliability of a test that is exactly twice as long as the test it was calibrated on."
  type: true-false
  answer: false
  explanation: "The Spearman-Brown formula generalizes to any length multiplier, not just doubling. The full formula predicts the reliability of a test k times as long as the original: r_kk = kr / (1 + (k-1)r). The standard split-half application uses k = 2, but the same logic applies if you want to predict the reliability of a test three times as long (k = 3) or half as long (k = 0.5). This makes Spearman-Brown a general tool for test length planning, not just a split-half correction."

- question: "Why is the Spearman-Brown correction necessary when reporting split-half reliability, and what would a researcher be claiming if they skipped it?"
  type: short-answer
  answer: "The Spearman-Brown correction is necessary because the correlation between the two half-tests estimates the reliability of a test that is half as long as the actual test. Skipping it and reporting the raw correlation would implicitly claim that the full test is no more reliable than half of it — a systematic underestimate. The correction predicts the reliability of the full-length test by applying the mathematical relationship between test length and reliability: more items reduce the influence of any single item's measurement error, so the full test is reliably more reliable than either half."
  explanation: "The deeper principle is that reliability is a function of test length, holding all else constant. This is why longer tests are used for high-stakes decisions — a 100-item licensure exam is more reliable than a 10-item quiz measuring the same construct. Spearman-Brown makes this relationship quantitative and precise, allowing researchers to extrapolate from a half-test observation to a full-test prediction. It also works in reverse: if you need a test with reliability .90 and your 40-item version has reliability .80, Spearman-Brown tells you how many items to add."
```

## Explainer

From test-retest reliability — your hard prerequisite — you know that one way to estimate reliability is to administer the same test twice and correlate the scores. The problem is that retesting introduces real complications: participants remember their answers, they learn between sessions, or they simply become different people over time. What if you wanted to estimate reliability from a *single* administration? Split-half reliability is the answer: you give the test once, artificially divide it into two halves, and treat those halves like two separate test administrations.

The logic is straightforward: if the test is measuring a stable construct reliably, then a person's score on the odd-numbered items should correlate highly with their score on the even-numbered items. Both halves are being administered to the same people, at the same time, measuring the same thing — so the only reason the two halves would disagree is measurement error. The correlation between the two half-scores, r, is therefore an estimate of reliability. But there is a catch: it is the reliability of a test that is *half as long* as the actual test.

This is where the **Spearman-Brown prophecy formula** comes in. One of the most robust findings in psychometrics is that longer tests are more reliable than shorter ones — more items means more sampling of the construct and less sensitivity to any single item's quirks. The formula r_xx = 2r / (1 + r) "prophesies" the reliability of the full-length test from the reliability of a half-length test. If the two halves correlate at r = .70, the predicted full-test reliability is 2(.70) / (1 + .70) = 1.40 / 1.70 ≈ .82. The formula works because adding a parallel half to a test is equivalent to doubling its length, and Spearman-Brown generalizes to predict the effect of multiplying test length by any factor k, not just 2.

The connection to your other prerequisite — alpha reliability — is close: coefficient alpha can be understood as the mean of all possible split-half reliabilities for a test. Alpha is preferred when items are not parallel (they vary in difficulty, intercorrelation, or content), because it does not depend on any particular split. Split-half reliability is best understood as the precursor to alpha that is easier to compute by hand and useful for teaching the underlying logic. The practical choice of splitting items by odd-even positions rather than first-half vs. second-half addresses a real confound: if participants tire or change strategy as a test progresses, the first-half / second-half split would artificially deflate the correlation, not because the test is unreliable, but because the two halves were taken under different conditions.


