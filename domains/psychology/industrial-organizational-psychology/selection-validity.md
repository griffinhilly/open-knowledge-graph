---
id: selection-validity
title: Selection Validity
domain: psychology
course: industrial-organizational-psychology
prerequisites:
- id: personnel-selection
  type: hard
- id: job-analysis
  type: hard
- id: measurement-scales-psychology
  type: soft
tags:
- validity
- criterion-related-validity
- content-validity
- construct-validity
stage: advanced
status: validated
---

# Selection Validity

## Core Idea
Selection validity refers to the degree to which a selection procedure actually measures or predicts what it is intended to measure or predict. The Uniform Guidelines recognize three validation strategies: criterion-related validity (demonstrating a statistical relationship between test scores and job performance), content validity (showing that the test representatively samples the job domain), and construct validity (establishing that the test measures the psychological construct it claims to measure). Validity is not a property of the test itself but of the inferences drawn from test scores in a specific context — a test valid for one purpose may be invalid for another.

## Questions

```yaml
- question: "A fire department develops a physical fitness test by having subject matter experts identify the physical demands of firefighting and then designing test components that simulate those demands. This best illustrates which validation strategy?"
  type: multiple-choice
  options:
    - "Predictive criterion-related validity"
    - "Concurrent criterion-related validity"
    - "Content validity"
    - "Construct validity"
  answer: 2
  explanation: "Content validity is established by demonstrating that the test content representatively samples the important aspects of the job domain. By having SMEs identify physical demands and then designing test components that directly simulate those demands, the fire department is building a content-valid test. No criterion data (actual job performance scores) are collected — the argument rests on the correspondence between test content and job content."

- question: "A validity coefficient of r = .30 between a selection test and job performance should be considered useless because it explains only 9% of the variance in performance."
  type: true-false
  answer: false
  explanation: "The 'variance explained' interpretation (r² = .09) dramatically understates practical utility. In selection contexts, even modest validity coefficients yield substantial gains when applied across many hiring decisions. Taylor-Russell tables and utility analysis show that a test with r = .30 can produce large improvements in workforce quality, especially when the selection ratio is low (many applicants per opening). Schmidt and Hunter estimated that the dollar-value utility of valid selection is enormous when aggregated across an organization."

- question: "What is restriction of range, and how does it affect observed validity coefficients?"
  type: short-answer
  answer: "Restriction of range occurs when the sample used to assess validity has less variability on the predictor or criterion than the full applicant population — typically because only those who were hired (selected) are included. This attenuates the observed correlation between predictor and criterion, making the test appear less valid than it actually is."
  explanation: "If an organization only hires applicants who scored above 70 on a test, the hired sample will have a compressed range of test scores (70-100 instead of 0-100). With less variance in the predictor, the correlation with the criterion is mathematically reduced. Correction formulas exist to estimate what the validity coefficient would have been in the unrestricted population. This is why predictive validity designs — hiring all applicants regardless of test scores — are methodologically superior, though rarely practical."

- question: "Validity generalization research by Schmidt and Hunter challenged which long-held belief about selection test validity?"
  type: multiple-choice
  options:
    - "That cognitive ability tests have any validity at all for predicting job performance"
    - "That validity is situation-specific — that a test valid in one setting might not be valid in another"
    - "That content validity is a legitimate validation strategy"
    - "That structured interviews are superior to unstructured interviews"
  answer: 1
  explanation: "Before validity generalization (VG) research, the prevailing view was situational specificity — that a test's validity could vary dramatically across settings, requiring local validation for every new context. Schmidt and Hunter used meta-analysis to show that much of the observed variability in validity coefficients across studies was due to statistical artifacts (sampling error, restriction of range, criterion unreliability). After correcting for these artifacts, the true variability was much smaller, suggesting that cognitive ability test validity generalizes broadly across jobs and settings."
```

## Explainer

Validity is the most important concept in personnel selection — and one of the most misunderstood. The common phrasing "this test is valid" is imprecise. Validity is not an inherent property of a test; it is a property of the inferences drawn from test scores for a particular purpose in a particular context. A cognitive ability test might be highly valid for predicting performance in complex jobs but less valid for predicting performance in jobs with minimal cognitive demands. The question is always: valid for what?

The three validation strategies — criterion-related, content, and construct — are not competing alternatives but complementary lines of evidence. Criterion-related validity provides the most direct evidence: you demonstrate empirically that test scores predict job performance. This can be done predictively (test candidates, hire regardless of scores, then correlate with later performance) or concurrently (test current employees and correlate with their current performance). The predictive approach is methodologically stronger because it avoids restriction of range and motivation differences, but it requires patience and the willingness to hire without using the test — a hard sell for most organizations.

Content validity takes a different approach entirely. Instead of demonstrating a statistical relationship between test scores and performance, you argue that the test content faithfully represents the job content. This is most compelling for work sample tests and job knowledge tests where the overlap between test and job is visible and direct. A typing test for a secretary job is content-valid on its face. Content validity is established through expert judgment (SMEs evaluating the correspondence between test and job), not through correlational data. It is the appropriate strategy when criterion data are unavailable or when the test directly samples job tasks.

Construct validity is the broadest framework. It asks whether the test measures the theoretical construct it claims to measure — for example, whether a "conscientiousness" scale actually measures conscientiousness and not something else. Construct validity is established through a web of evidence: factor analyses showing the right internal structure, correlations with other measures of the same construct (convergent validity), low correlations with measures of different constructs (discriminant validity), and theoretically predicted relationships with external variables. In practice, construct validity subsumes the other two strategies as special cases.

The validity generalization movement, led by Schmidt and Hunter from the 1970s onward, transformed the field by challenging the doctrine of situational specificity. Prior to their work, practitioners believed that a test's validity had to be demonstrated locally — in each new organization, for each new job — because validity might not transfer across settings. Using meta-analysis, Schmidt and Hunter showed that much of the apparent variability in validity coefficients was artifactual, caused by sampling error, range restriction, and measurement error in the criterion. Once these artifacts were corrected, the remaining true variability was small. This meant that cognitive ability tests, for instance, could be confidently used in new settings without full local validation, dramatically expanding the practical reach of validated selection tools.
