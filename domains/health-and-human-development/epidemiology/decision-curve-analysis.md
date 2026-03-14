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
