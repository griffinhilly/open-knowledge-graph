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
stage: expert
status: draft
---

# Decision Curve Analysis

## Core Idea
Decision curve analysis (DCA) evaluates the net clinical benefit of using a prediction model or diagnostic test across a range of decision thresholds. DCA overcomes ROC curve limitations by directly incorporating clinically relevant costs and benefits of false positives and false negatives. It plots net benefit (true positives - false positives × cost ratio) against probability threshold, showing whether a test is actually worth using and at which thresholds it provides value. Comparing DCA curves reveals when one test outperforms another.

## How It's Best Learned
Calculate and plot DCA curves for competing diagnostic tests or prediction models; demonstrate how optimal test choice changes with threshold.

## Common Misconceptions
Tests with high area-under-the-ROC-curve are always clinically useful (utility depends on decision threshold and costs). ROC curves fully capture the clinical utility of tests.

## Questions

```yaml
- question: "A new prediction model for sepsis has an AUC of 0.82, substantially better than the existing clinical score (AUC = 0.74). A decision curve analysis is run. At the threshold range used in clinical practice (5%–15%), the new model's DCA curve lies below the 'treat all' reference line. What should you conclude?"
  type: multiple-choice
  options:
    - "The new model should be adopted because its AUC is meaningfully higher"
    - "The new model provides no clinical benefit over simply treating all high-risk patients at this threshold range"
    - "The AUC comparison is more reliable than DCA for evaluating clinical utility"
    - "The DCA result is invalid because the threshold range is too narrow"
  answer: 1
  explanation: "When a model's DCA curve falls below the 'treat all' line at the clinically relevant threshold range, using the model provides less net benefit than simply treating everyone — making it clinically useless despite its higher AUC. AUC summarizes discrimination across all thresholds simultaneously, ignoring the relative costs of false positives and false negatives. DCA evaluates whether the model improves on the simplest possible strategies (treat all, treat none) at the threshold a clinician would actually use. High AUC is not sufficient for clinical utility."

- question: "What does the decision threshold (p_t) in decision curve analysis represent?"
  type: multiple-choice
  options:
    - "The probability cutoff at which the model's sensitivity equals its specificity"
    - "The minimum AUC required for the model to be considered valid"
    - "The disease probability at which a clinician is indifferent between treating and not treating"
    - "The prevalence of disease in the study population"
  answer: 2
  explanation: "The decision threshold encodes the clinician's implicit judgment about the relative harm of a false positive versus a false negative. At p_t = 10%, a clinician is willing to treat 9 disease-free patients to avoid missing one case — the expected harm of unnecessary treatment equals the expected harm of missing disease. This threshold is determined by clinical context (disease severity, treatment side-effects), not by statistical properties of the test. It is what makes DCA clinically grounded rather than purely statistical."

- question: "A diagnostic model can have a high AUC and still provide no clinical benefit over treating everyone, depending on the decision threshold."
  type: true-false
  answer: true
  explanation: "True. AUC averages performance across all possible thresholds, weighting them equally. But if a model's net benefit at clinically relevant thresholds falls below the 'treat all' line, it offers no practical advantage despite strong overall discrimination. The 'treat all' strategy — giving the intervention to every patient — performs well at low thresholds because it catches every case; a model only adds value if it reduces unnecessary treatments without missing too many cases. High AUC guarantees good discrimination on average, not clinical utility at the specific threshold that matters."

- question: "Decision curve analysis plots sensitivity on the y-axis against 1 − specificity on the x-axis across decision thresholds."
  type: true-false
  answer: false
  explanation: "False. That is the ROC curve. DCA plots net benefit on the y-axis against decision threshold (probability) on the x-axis. Net benefit = (true positives / N) − (false positives / N) × (p_t / (1 − p_t)), incorporating the clinical cost ratio of false positives relative to false negatives. This distinction is fundamental: ROC curves summarize discrimination without reference to clinical context, while DCA directly addresses whether using the test is better than not using it, given how much harm a false positive costs relative to a false negative."

- question: "Why does decision curve analysis include 'treat all' and 'treat none' as reference lines, and what happens to the 'treat all' line as the threshold increases?"
  type: short-answer
  answer: "The reference lines represent the simplest possible strategies: intervene for every patient regardless of test result, or intervene for none. A test is only clinically valuable if it outperforms both — if it can't beat treating everyone or treating no one, there is no reason to use it. The 'treat all' line decreases as threshold rises because at a high threshold you are implying that false positives are very costly; treating everyone incurs those costs on every disease-free patient, producing large negative net benefit."
  explanation: "This framing is what separates DCA from purely statistical metrics. A test that looks good on AUC might still be worse than 'treat all' at low thresholds (where the condition is dangerous and treatment is safe) or worse than 'treat none' at high thresholds (where treatment is harmful and the condition is mild). By plotting both reference lines, DCA forces a direct answer to the clinical question: does this model improve on trivial strategies at the threshold that actually governs practice?"
```

## Explainer

You already know from ROC curves that a diagnostic test's performance can be summarized as a tradeoff between sensitivity and specificity at every possible threshold. But ROC curves have a blind spot: they treat false positives and false negatives as equally costly, summarize performance over all thresholds simultaneously, and tell you nothing about whether using the test is actually better than treating everyone or treating no one. Decision curve analysis fills this gap by asking a practical question: **at the threshold a clinician would actually use, does this test produce more benefit than harm?**

The key concept is the **decision threshold** (sometimes called the threshold probability, p_t). This is the probability of disease at which a clinician is indifferent between treating and not treating—the point where the expected benefit of treating equals the expected harm. If you would treat a patient whenever their estimated disease probability exceeds 10%, your threshold is 0.10. This threshold encodes the relative cost of a false positive (unnecessary treatment) versus a false negative (missed disease). At a low threshold (e.g., 5%), you are willing to treat many patients without disease to avoid missing cases—appropriate for a lethal disease with a safe treatment. At a high threshold (e.g., 50%), you require strong evidence before exposing patients to an invasive intervention.

**Net benefit** is defined as: (true positives / N) − (false positives / N) × (p_t / (1 − p_t)). The second term discounts false positives by the odds of the threshold—how much you care about treating unnecessarily. Net benefit is plotted on the y-axis against threshold on the x-axis, producing a curve for your model, and two reference lines: "treat all" (everybody gets the intervention regardless of test result) and "treat none" (nobody does). The "treat all" line decreases as the threshold rises—at a low threshold, treating everyone gives high benefit, but at a high threshold, you are overtreating massively. "Treat none" is a flat line at net benefit = 0. A test is **clinically useful** only when its DCA curve lies above both reference lines across the relevant threshold range. A test with a high AUC can still lie below the "treat all" line if it fails to improve on indiscriminate treatment.

The practical power of DCA is comparison. When evaluating two competing prediction models—say, a simple clinical score versus a complex machine learning model—you plot both on the same DCA graph and identify the threshold range where one outperforms the other. A model that is modestly better on AUC might show no meaningful DCA advantage within clinically plausible thresholds, making the complexity unjustifiable. Conversely, a model that is slightly worse on AUC overall might be dramatically better at the specific threshold where clinical decisions are actually made. DCA thus translates statistical model performance into clinical decision quality, making it the preferred tool for evaluating whether a prediction model should change practice.
