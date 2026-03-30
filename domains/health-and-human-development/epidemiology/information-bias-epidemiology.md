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
status: validated
---

# Information Bias and Misclassification Error

## Core Idea
Information bias occurs when exposure or outcome data are inaccurate, leading to misclassification. Non-differential misclassification (random error) typically biases RR toward the null; differential misclassification (systematic error, e.g., recall bias) can bias in either direction. Understanding the type and magnitude of misclassification is critical for interpreting study results.

## Questions

```yaml
- question: "In a case-control study of breast cancer, cases (women with breast cancer) are asked about past hormone replacement therapy use, as are matched controls. Cases report substantially higher rates of past HRT use. A critic suggests this may reflect recall bias. If the critic is correct, what type of misclassification is this, and in which direction does it bias the odds ratio?"
  type: multiple-choice
  options:
    - "Non-differential misclassification; biases the odds ratio toward the null"
    - "Differential misclassification; biases the odds ratio toward the null"
    - "Differential misclassification; biases the odds ratio away from the null (inflates the apparent association)"
    - "Non-differential misclassification; biases the odds ratio away from the null"
  answer: 2
  explanation: "Recall bias is a classic form of differential misclassification: cases are more motivated to recall past exposures (searching their memory for an explanation for their illness), so they over-report HRT use compared to controls. The misclassification rate differs between cases and controls — that's what makes it differential. Because cases over-report exposure, the apparent odds ratio is inflated above the true value — bias away from the null. Non-differential misclassification (same error rate in both groups) would instead bias toward the null."

- question: "A cohort study of lung cancer measures smoking status at baseline with a questionnaire that has a 10% misclassification rate applied equally to exposed (smokers) and unexposed (non-smokers) participants. What is the expected effect on the observed risk ratio?"
  type: multiple-choice
  options:
    - "The risk ratio is inflated — random errors amplify apparent associations"
    - "The risk ratio is biased toward the null — the two groups are blurred together"
    - "There is no systematic effect — random errors cancel out across the sample"
    - "The direction of bias depends on the baseline prevalence of smoking in the cohort"
  answer: 1
  explanation: "Equal misclassification rates in both groups (non-differential) blur the two groups toward each other. Some true smokers are classified as non-smokers and vice versa, making the 'exposed' group less purely exposed and the 'unexposed' group less purely unexposed. The observed risk ratio moves toward 1.0 — the null — because the contrast between groups is diluted. This is attenuated, not amplified, association. The 'random errors cancel out' reasoning (Option C) is wrong for bias — it applies to random variation around an estimate, not to systematic misclassification."

- question: "Non-differential misclassification of a binary exposure always biases the observed risk ratio or odds ratio toward the null value of 1.0."
  type: true-false
  answer: true
  explanation: "Under non-differential misclassification of a binary exposure (same error rate in both outcome groups), the mathematical consequence is systematic attenuation of the apparent association toward 1.0 — 'bias toward the null.' This makes studies conservative: they underestimate true effect sizes. This is why studies showing associations despite likely non-differential misclassification are particularly compelling evidence — the true effect would be even larger. Note that with polytomous (more than two category) exposure, non-differential misclassification can occasionally bias away from the null, but for binary exposure the direction is consistent."

- question: "Because non-differential misclassification involves random measurement error applied equally to both groups, it does not introduce systematic bias into study results."
  type: true-false
  answer: false
  explanation: "This is the key misconception. 'Random' here means the errors are applied equally across groups — it does NOT mean the errors have no systematic effect on the estimate. Non-differential misclassification produces a highly predictable, systematic bias: attenuation toward the null. The risk ratio is consistently underestimated. Random individual errors can produce a systematic direction of bias at the aggregate level. The term 'random error' in this context refers to the mechanism of error generation, not its effect on the effect measure."

- question: "Why is differential misclassification considered a more serious validity threat than non-differential misclassification?"
  type: short-answer
  answer: "Non-differential misclassification has a predictable direction of bias (toward the null), so researchers can reason about its effect: the true association is at least as large as observed, and often larger. Differential misclassification can bias in either direction — toward or away from the null — depending on the specific mechanism. Because the direction is unpredictable without knowing the mechanism in detail, differential misclassification can both underestimate and overestimate associations, making it harder to reason about what the 'true' result might be."
  explanation: "Recall bias (a common form of differential misclassification in case-control studies) inflates associations and can create apparent effects where none exist. An unknown direction of bias is fundamentally harder to account for than a known one. This is why study designs that reduce differential misclassification — blinded outcome assessment, objective biomarker measurement — are considered methodologically stronger than those relying on self-report."
```

## Explainer

Every epidemiologic study ultimately rests on two classifications: who was exposed, and who developed the outcome. **Information bias** occurs when errors in making either of these classifications introduce systematic distortions into the data. Because you've studied study designs — cohort, case-control, cross-sectional, RCT — you know that each design collects exposure and outcome data differently, and that difference determines what kinds of information bias are most likely.

**Misclassification** is the specific mechanism: a truly exposed person is recorded as unexposed, or a true case is recorded as a non-case (or vice versa). The critical distinction is whether the misclassification error is **non-differential** or **differential**. **Non-differential misclassification** means the error rate is the same in both groups being compared — exposed and unexposed, or cases and controls. If 15% of truly exposed people are incorrectly recorded as unexposed, and the same 15% misclassification rate applies to truly unexposed people recorded as exposed, the two groups get "blurred" toward each other. The mathematical consequence is that the observed risk ratio or odds ratio is pulled toward 1.0 — the **null value** — making true associations appear weaker than they are. This is called **bias toward the null** and tends to make studies conservative (underestimating effects).

**Differential misclassification** occurs when the error rate differs between groups, and its consequences are more dangerous because it can bias in *either* direction — toward or away from the null. The classic example is **recall bias** in case-control studies: people diagnosed with a disease (cases) are more motivated to recall and report past exposures than healthy controls are, so cases systematically over-report exposures compared to controls. This inflates the apparent association between exposure and disease. Conversely, a disease might cause subjects to underreport certain behaviors, deflating the observed association. The direction of differential misclassification is unpredictable without knowing the specific mechanism, making it the more serious threat to validity.

Several structural features of study designs create characteristic information biases. **Recall bias** is endemic to case-control studies because exposure is measured retrospectively after disease status is known. **Interviewer bias** occurs when the person collecting data knows the exposure or disease status of the subject and (consciously or unconsciously) probes more deeply in one group. **Surveillance bias** (also called **detection bias**) appears when exposed individuals receive more intensive medical monitoring than unexposed ones, making their outcomes more likely to be detected even if true incidence is equal. Recognizing which biases are plausible for a given study design, assessing whether the error is likely differential or non-differential, and reasoning about the expected direction of bias are the core skills for critically interpreting epidemiologic literature.
