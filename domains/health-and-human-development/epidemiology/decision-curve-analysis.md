---
id: decision-curve-analysis
title: Decision Curve Analysis
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: receiver-operating-characteristic
  type: hard
- id: screening-test-evaluation
  type: hard
- id: diagnostic-sensitivity-specificity
  type: soft
tags:
- diagnostic-testing
- clinical-decision-making
- test-utility
stage: advanced
status: draft
---

# Decision Curve Analysis

## Core Idea
Decision curve analysis (DCA) evaluates the net clinical benefit of using a prediction model or diagnostic test across a range of decision thresholds. DCA overcomes ROC curve limitations by directly incorporating clinically relevant costs and benefits of false positives and false negatives. It plots net benefit (true positives - false positives × cost ratio) against probability threshold, showing whether a test is actually worth using and at which thresholds it provides value. Comparing DCA curves reveals when one test outperforms another.

## How It's Best Learned
Calculate and plot DCA curves for competing diagnostic tests or prediction models; demonstrate how optimal test choice changes with threshold.

## Common Misconceptions
Tests with high area-under-the-ROC-curve are always clinically useful (utility depends on decision threshold and costs). ROC curves fully capture the clinical utility of tests.

## Explainer

You already know from ROC curves that a diagnostic test's performance can be summarized as a tradeoff between sensitivity and specificity at every possible threshold. But ROC curves have a blind spot: they treat false positives and false negatives as equally costly, summarize performance over all thresholds simultaneously, and tell you nothing about whether using the test is actually better than treating everyone or treating no one. Decision curve analysis fills this gap by asking a practical question: **at the threshold a clinician would actually use, does this test produce more benefit than harm?**

The key concept is the **decision threshold** (sometimes called the threshold probability, p_t). This is the probability of disease at which a clinician is indifferent between treating and not treating—the point where the expected benefit of treating equals the expected harm. If you would treat a patient whenever their estimated disease probability exceeds 10%, your threshold is 0.10. This threshold encodes the relative cost of a false positive (unnecessary treatment) versus a false negative (missed disease). At a low threshold (e.g., 5%), you are willing to treat many patients without disease to avoid missing cases—appropriate for a lethal disease with a safe treatment. At a high threshold (e.g., 50%), you require strong evidence before exposing patients to an invasive intervention.

**Net benefit** is defined as: (true positives / N) − (false positives / N) × (p_t / (1 − p_t)). The second term discounts false positives by the odds of the threshold—how much you care about treating unnecessarily. Net benefit is plotted on the y-axis against threshold on the x-axis, producing a curve for your model, and two reference lines: "treat all" (everybody gets the intervention regardless of test result) and "treat none" (nobody does). The "treat all" line decreases as the threshold rises—at a low threshold, treating everyone gives high benefit, but at a high threshold, you are overtreating massively. "Treat none" is a flat line at net benefit = 0. A test is **clinically useful** only when its DCA curve lies above both reference lines across the relevant threshold range. A test with a high AUC can still lie below the "treat all" line if it fails to improve on indiscriminate treatment.

The practical power of DCA is comparison. When evaluating two competing prediction models—say, a simple clinical score versus a complex machine learning model—you plot both on the same DCA graph and identify the threshold range where one outperforms the other. A model that is modestly better on AUC might show no meaningful DCA advantage within clinically plausible thresholds, making the complexity unjustifiable. Conversely, a model that is slightly worse on AUC overall might be dramatically better at the specific threshold where clinical decisions are actually made. DCA thus translates statistical model performance into clinical decision quality, making it the preferred tool for evaluating whether a prediction model should change practice.
