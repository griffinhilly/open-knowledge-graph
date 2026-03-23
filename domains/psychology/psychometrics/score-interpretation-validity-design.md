---
id: score-interpretation-validity-design
title: Score Interpretation and Validity Evidence Design
domain: psychology
course: psychometrics
prerequisites:
- id: validity-evidence-frameworks
  type: hard
builds-toward:
- consequential-validity-and-fairness
- norm-referenced-criterion-referenced-interpretation
tags:
- validity
- score-interpretation
- evidence
stage: expert
status: draft
---

# Score Interpretation and Validity Evidence Design

## Core Idea
Validity is not a test property but a quality of inferences drawn from scores in a specific context. Validity evidence comes from five sources: content, response processes, internal structure, relations to external variables, and consequences. Effective interpretation requires designing validation studies that gather evidence relevant to intended uses and interpretations.

## Questions

```yaml
- question: "A reading comprehension test has been extensively validated for selecting employees in roles requiring heavy reading. A company now wants to use the same test to screen candidates for a physical security role with no reading requirements. Which statement best describes the validity situation?"
  type: multiple-choice
  options:
    - "The test remains valid because validity is established once and transfers across uses"
    - "The test may have been valid for the original purpose, but the new use requires new validity evidence — validity attaches to specific inferences in specific contexts, not to tests themselves"
    - "The test is now invalid because validity is a fixed property that is destroyed when you change the context"
    - "Validity only applies to psychological constructs, not to employment screening instruments"
  answer: 1
  explanation: "The conceptual pivot in modern validity theory is that validity is not a property of a test but of inferences drawn from scores for specific purposes in specific contexts. A test that supports valid inferences about reading ability does not automatically support valid inferences about physical security performance — those are different claims about different relationships. The test did not change; the inference changed. New evidence is required for the new use."

- question: "A researcher develops a test of mathematical reasoning. Response process studies reveal that low-scoring students consistently struggle with the verbal complexity of the word problems, not with the underlying mathematics. What validity threat is this?"
  type: multiple-choice
  options:
    - "Content validity threat — the items do not adequately represent the domain of mathematics"
    - "Consequential validity threat — the test is producing harmful outcomes for students"
    - "Response process threat — examinees are engaging with a different construct (reading/verbal comprehension) than the test intends to measure (mathematical reasoning)"
    - "Internal structure threat — the test items do not form a unidimensional factor"
  answer: 2
  explanation: "Response process evidence asks whether examinees are doing what the test intends. If low scores reflect reading difficulty rather than mathematical reasoning, the test is not measuring what it claims to measure — this is a construct validity failure revealed through response process data. Think-aloud protocols, cognitive interviews, and eye-tracking are the methods for gathering this evidence. The finding doesn't merely suggest the test is 'too hard'; it suggests the scores mean something different from what the test claims."

- question: "Validity is a property of a test itself — a well-constructed test is valid regardless of how its scores are interpreted or for what purpose it is used."
  type: true-false
  answer: false
  explanation: "This is the key misconception the modern validity framework was designed to correct. Validity is always about a specific inference: 'these scores support the conclusion that...' The same test can yield valid inferences for one purpose (reading comprehension scores predict reading performance) and invalid inferences for another (those scores predict physical security performance). Calling a test 'valid' without specifying the inference and context is incomplete."

- question: "Response process evidence for validity can reveal whether examinees are actually engaging with the construct a test intends to measure, rather than solving items through unintended strategies."
  type: true-false
  answer: true
  explanation: "Response process evidence is gathered through methods like think-aloud protocols, cognitive interviewing, and eye-tracking. It answers: 'When test-takers respond to these items, are they actually doing the cognitive or behavioral process we're trying to assess?' If students are skipping steps and guessing based on keyword matching, or using test-taking tricks rather than applying knowledge, the scores may not reflect the construct — even if the content looks right on paper."

- question: "Why is it a problem to gather validity evidence after a test has already been deployed widely, rather than designing validation studies before operational use?"
  type: short-answer
  answer: "Once a test is widely deployed, negative validity findings become very costly to act on: withdrawing or revising the test requires revisiting decisions already made for large numbers of people (hiring, admission, licensure), and institutional and political pressures make it difficult to respond appropriately. Pre-deployment validation lets problems be caught and corrected when the stakes are low and changes are feasible. The interpretive argument framework (Kane, 2006) supports this by requiring the validation plan to be designed alongside the test, not appended after the fact."
  explanation: "This is why the Standards recommend that validation is an ongoing process beginning before operational deployment. The goal is for validation evidence to be in place when the test is first used consequentially — not accumulated retroactively in response to criticism. The five sources of validity evidence are most useful as a design framework for the validation program, not as a post-hoc checklist."
```

## Explainer

From your work on validity evidence frameworks, you know the conceptual pivot that the *Standards for Educational and Psychological Testing* (1999/2014) introduced: validity is not a fixed property of a test, but a judgment about the **appropriateness of specific inferences** drawn from test scores in specific contexts for specific purposes. A test of reading comprehension may yield valid inferences about reading ability while yielding invalid inferences when used to make employment decisions in a job that does not require reading. The test did not change; the inference changed. This reframing dissolves the older tripartite distinction (content validity, criterion validity, construct validity) and replaces it with a unified concept: an **argument** that evidence supports, or fails to support, a score interpretation.

The five sources of validity evidence define the terrain of that argument. **Content evidence** asks whether the test items adequately represent the domain of interest — established through expert review, content mapping, and alignment studies. **Response process evidence** asks whether examinees are actually doing what the test intends — established through think-aloud protocols, eye-tracking, or cognitive interviewing. A math test may be measuring reading ability instead of mathematical reasoning if the items are verbally dense; response process data can reveal this. **Internal structure evidence** asks whether the item relationships within the test match the hypothesized structure of the construct — established through factor analysis and IRT model fit. **Relations to external variables evidence** asks whether scores correlate with other measures as theory predicts — convergent correlations with measures of the same construct, discriminant correlations with measures of different constructs. **Consequential evidence** asks whether the use of test scores produces intended outcomes and whether unintended consequences exist.

Designing a validation study means deciding which sources of evidence are most relevant to the intended interpretation and then building a research program to gather them. Not all five sources need equal attention for every test: a straightforward knowledge assessment for a licensure exam may require principally content evidence and criterion evidence (can licensed practitioners actually do the job?), while a novel measure of an abstract psychological construct like "grit" requires heavy investment in internal structure and discriminant validity research. The **interpretive argument** framework (Kane, 2006) makes this structure explicit: the test developer states the chain of inferences from observed score to ultimate decision, then identifies each inference as a link, and specifies what evidence would strengthen or break each link.

The most common failure mode in test development is gathering validity evidence *after* widespread deployment, when negative findings are costly to act on. Best practice is to design the validation program before the test is used operationally: pilot data should inform both item refinement and the evidentiary argument simultaneously. If the intended interpretation is that high scorers are more qualified for a clinical position, then criterion-related studies should be designed with the hiring outcome in mind — not added retroactively when someone questions the test's use. Validity is an ongoing process of accumulation, not a one-time certification, and each new population, context, or decision changes the evidentiary requirements.
