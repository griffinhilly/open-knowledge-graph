---
id: information-bias-epidemiology
title: Information Bias and Misclassification Error
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: epidemiologic-study-designs
  type: hard
builds-toward:
- stratification-and-adjustment
- sensitivity-analysis-epidemiology
tags:
- information-bias
- misclassification
- measurement-error
- validity
stage: advanced
status: draft
---

# Information Bias and Misclassification Error

## Core Idea
Information bias occurs when exposure or outcome data are inaccurate, leading to misclassification. Non-differential misclassification (random error) typically biases RR toward the null; differential misclassification (systematic error, e.g., recall bias) can bias in either direction. Understanding the type and magnitude of misclassification is critical for interpreting study results.

## Explainer

Every epidemiologic study ultimately rests on two classifications: who was exposed, and who developed the outcome. **Information bias** occurs when errors in making either of these classifications introduce systematic distortions into the data. Because you've studied study designs — cohort, case-control, cross-sectional, RCT — you know that each design collects exposure and outcome data differently, and that difference determines what kinds of information bias are most likely.

**Misclassification** is the specific mechanism: a truly exposed person is recorded as unexposed, or a true case is recorded as a non-case (or vice versa). The critical distinction is whether the misclassification error is **non-differential** or **differential**. **Non-differential misclassification** means the error rate is the same in both groups being compared — exposed and unexposed, or cases and controls. If 15% of truly exposed people are incorrectly recorded as unexposed, and the same 15% misclassification rate applies to truly unexposed people recorded as exposed, the two groups get "blurred" toward each other. The mathematical consequence is that the observed risk ratio or odds ratio is pulled toward 1.0 — the **null value** — making true associations appear weaker than they are. This is called **bias toward the null** and tends to make studies conservative (underestimating effects).

**Differential misclassification** occurs when the error rate differs between groups, and its consequences are more dangerous because it can bias in *either* direction — toward or away from the null. The classic example is **recall bias** in case-control studies: people diagnosed with a disease (cases) are more motivated to recall and report past exposures than healthy controls are, so cases systematically over-report exposures compared to controls. This inflates the apparent association between exposure and disease. Conversely, a disease might cause subjects to underreport certain behaviors, deflating the observed association. The direction of differential misclassification is unpredictable without knowing the specific mechanism, making it the more serious threat to validity.

Several structural features of study designs create characteristic information biases. **Recall bias** is endemic to case-control studies because exposure is measured retrospectively after disease status is known. **Interviewer bias** occurs when the person collecting data knows the exposure or disease status of the subject and (consciously or unconsciously) probes more deeply in one group. **Surveillance bias** (also called **detection bias**) appears when exposed individuals receive more intensive medical monitoring than unexposed ones, making their outcomes more likely to be detected even if true incidence is equal. Recognizing which biases are plausible for a given study design, assessing whether the error is likely differential or non-differential, and reasoning about the expected direction of bias are the core skills for critically interpreting epidemiologic literature.
