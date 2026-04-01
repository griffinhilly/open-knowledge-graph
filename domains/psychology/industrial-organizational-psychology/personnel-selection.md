---
id: personnel-selection
title: Personnel Selection
domain: psychology
course: industrial-organizational-psychology
prerequisites:
- id: job-analysis
  type: hard
- id: measurement-scales-psychology
  type: soft
tags:
- selection
- hiring
- predictors
- criteria
stage: advanced
status: validated
---

# Personnel Selection

## Core Idea
Personnel selection is the process of choosing individuals for employment based on their predicted job performance. It involves identifying relevant predictors (tests, interviews, work samples), measuring candidates on those predictors, and making hiring decisions using some combination rule. Effective selection requires that predictors are both valid (actually related to job performance) and legally defensible (based on job-relevant criteria established through job analysis). The core challenge is prediction under uncertainty: using limited information gathered before hiring to forecast performance that will unfold over months and years.

## Questions

```yaml
- question: "A company uses a cognitive ability test, a structured interview, and a work sample test to select software engineers. These are all examples of..."
  type: multiple-choice
  options:
    - "Criteria — the outcomes the company wants to predict"
    - "Predictors — measures used to forecast future job performance"
    - "Job analysis methods — tools for understanding job requirements"
    - "Performance appraisal instruments — tools for evaluating current employees"
  answer: 1
  explanation: "In the predictor-criterion framework, predictors are measures collected before or during hiring that are used to forecast criteria (job performance outcomes). The cognitive ability test, interview, and work sample are all predictors — they generate scores used to predict how well candidates will perform on the job. The criterion is the actual job performance the company hopes to forecast."

- question: "Using multiple predictors in a selection system always improves prediction over using a single predictor."
  type: true-false
  answer: false
  explanation: "Adding predictors improves prediction only when the new predictor captures variance in job performance that is not already captured by existing predictors — that is, when it has incremental validity. If a new predictor is highly correlated with existing predictors, it adds redundancy rather than new information. For example, adding a second cognitive ability test to a battery that already includes one may add little incremental validity because both tests measure largely the same construct."

- question: "What is the predictor-criterion framework, and why is it central to personnel selection?"
  type: short-answer
  answer: "The predictor-criterion framework distinguishes between the measures used to evaluate candidates (predictors) and the outcomes those measures are supposed to forecast (criteria, typically job performance). It is central because it structures the entire validation process: a selection system is valid to the extent that predictor scores actually predict criterion scores."
  explanation: "This framework forces practitioners to be explicit about what they are measuring (predictors) and what they are trying to predict (criteria). Without this distinction, organizations may select on characteristics that feel relevant but have no demonstrated relationship to actual job performance. The framework also clarifies what validation means: empirically demonstrating a statistical relationship between predictor and criterion."

- question: "An organization hires all applicants regardless of their test scores, then correlates test scores with subsequent job performance. This describes which validation strategy?"
  type: multiple-choice
  options:
    - "Content validity"
    - "Predictive criterion-related validity"
    - "Concurrent criterion-related validity"
    - "Construct validity"
  answer: 1
  explanation: "Predictive validity involves collecting predictor data first, then waiting to collect criterion data later (after the person is on the job). By hiring all applicants regardless of test scores, the organization avoids restriction of range — a key methodological advantage. Concurrent validity, by contrast, collects predictor and criterion data from current employees at the same time. Content validity evaluates whether the test content representatively samples the job domain."
```

## Explainer

Personnel selection sits at the intersection of measurement science and practical decision-making. The foundational idea is simple: organizations want to hire people who will perform well, and they use various assessment tools to predict who those people will be. But the execution is anything but simple, because prediction of human behavior is inherently uncertain and the consequences of poor prediction — bad hires, legal liability, wasted training resources — are substantial.

The predictor-criterion framework organizes all of selection psychology. Predictors are the assessments administered to candidates: cognitive ability tests, personality inventories, structured interviews, work samples, assessment centers, biographical data, and more. Criteria are the outcomes the organization cares about: job performance ratings, sales figures, tenure, counterproductive behavior, and other indicators of success. The validation question is whether predictor scores actually predict criterion scores — and how well.

Different predictors have different validity profiles. Meta-analyses by Schmidt and Hunter (1998) and subsequent updates have established a rough hierarchy: general cognitive ability (GCA) is the single strongest predictor of job performance across nearly all jobs, with validity coefficients around .50-.65 for complex jobs. Structured interviews, work sample tests, and integrity tests also show strong validity. Unstructured interviews, years of experience, and graphology perform much worse. But validity is only one consideration — organizations also care about applicant reactions, adverse impact (differential selection rates across demographic groups), cost, and legal defensibility.

A critical concept is incremental validity: the extent to which a new predictor improves prediction beyond what existing predictors already provide. Because many predictors are correlated with each other (cognitive ability correlates with work sample performance, for instance), adding a second predictor does not simply add its validity to the first. The gain depends on how much unique variance it captures. This is why optimal selection batteries typically combine predictors that tap different constructs — for example, cognitive ability plus conscientiousness plus a structured interview — rather than stacking similar measures.

Selection decisions also require a combination rule for integrating information across multiple predictors. Compensatory models (like multiple regression) allow high scores on one predictor to compensate for low scores on another. Non-compensatory models (like multiple hurdles) set minimum cutoffs on each predictor — failing any one is disqualifying regardless of other scores. The choice between these approaches depends on the job: a firefighter must meet minimum physical requirements regardless of cognitive ability, suggesting a multiple-hurdle approach, while many office jobs allow compensation across dimensions.
