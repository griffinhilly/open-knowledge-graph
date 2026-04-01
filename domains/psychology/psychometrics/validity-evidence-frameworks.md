---
id: validity-evidence-frameworks
title: Modern Validity Frameworks and Integrated Evidence
domain: psychology
course: psychometrics
prerequisites:
- id: construct-validity-multitrait
  type: hard
- id: criterion-validity-prediction
  type: hard
- id: content-validity-judgment
  type: soft
- id: hypothesis-test-framework
  type: soft
- id: confidence-intervals-framework
  type: soft
builds-toward:
- structural-equation-modeling-measurement
tags:
- validity
- evidence-integration
- standards
- test-use
stage: expert
status: validated
---

# Modern Validity Frameworks and Integrated Evidence

## Core Idea
Contemporary validity frameworks (APA/AERA/NCME Standards) organize evidence into five sources: test content, response processes, internal structure, relations to other variables, and consequences of testing. This unified view synthesizes validity as an integrated evaluation of whether test scores support their intended interpretations and uses.

## Questions

```yaml
- question: "A cognitive ability test shows strong criterion-related validity and good internal consistency. However, researchers discover that many test-takers solve the 'reasoning' items using a pattern-matching shortcut rather than the analytical reasoning the test is meant to measure. Which source of validity evidence is most directly threatened?"
  type: multiple-choice
  options:
    - "Evidence from test content — the items do not adequately cover the reasoning domain"
    - "Evidence from internal structure — factor analysis would reveal that items load on a single shortcut factor"
    - "Evidence from response processes — examinees are not using the cognitive processes the test intends to invoke"
    - "Evidence from relations to other variables — criterion correlations are inflated by the shortcut strategy"
  answer: 2
  explanation: "Evidence from response processes directly addresses whether examinees are engaging with test items the way the test designers intended. If a 'reasoning' test is being solved through pattern recognition rather than analytical reasoning, then the score does not measure what it claims to measure — regardless of criterion correlations or internal consistency. Think-aloud protocols and cognitive interviews are the primary methods for gathering this evidence. A test can look valid by other criteria while being fundamentally invalid at the process level."

- question: "A personnel selection test has been thoroughly validated for predicting performance in entry-level software engineering roles. A new HR director decides to use the same test to identify candidates for promotion to senior engineer positions. According to the modern validity framework, what is the key concern?"
  type: multiple-choice
  options:
    - "The test needs to be re-normed for the senior engineer population before use"
    - "Validity is specific to interpretations and uses; using the test for promotion requires building a new validity argument for that purpose"
    - "The test is invalid for this purpose because it was never designed for promotion decisions"
    - "Re-validation is only needed if the test content or scoring has changed"
  answer: 1
  explanation: "The central shift in the modern framework is from asking 'Is this a valid test?' to asking 'Is this a valid use of this test with these people for this purpose?' A test thoroughly validated for predicting entry-level performance has not been validated for predicting senior-level performance — those are different constructs requiring different evidence. Validity evidence is built for a specific interpretation and use; borrowing it wholesale for a different context is a logical error, not just a technical shortcoming."

- question: "Under the modern validity framework, a test that accurately predicts job performance but systematically underestimates performance for one demographic group provides validity evidence against its use in that application."
  type: true-false
  answer: true
  explanation: "Evidence from consequences — the fifth source in the modern framework — asks whether the actual use of the test produces intended outcomes and avoids harmful unintended ones. Systematic underprediction for a demographic group is a consequence that bears on whether the score interpretation is valid for that group. The modern framework treats this as validity evidence, not merely a social or legal concern. A test that 'works on average' while producing systematically biased decisions for a subgroup is not fully valid for that use."

- question: "Once a test demonstrates good criterion-related validity and strong internal consistency, no further validity evidence is needed to support its use."
  type: true-false
  answer: false
  explanation: "The modern framework treats validity as an integrated argument built from multiple convergent sources. Criterion validity and internal structure are two of five sources; evidence from test content, response processes, and consequences can each reveal problems that the other two sources miss. A test might predict job performance well (criterion validity) while examinees bypass the intended cognitive processes (response process problem), or while producing harmful disparate impacts (consequences problem). No single source is sufficient — validity is always a cumulative case."

- question: "What is the fundamental shift in how validity is understood in the modern APA/AERA/NCME framework compared to the older 'types of validity' approach, and why does this distinction matter for test use?"
  type: short-answer
  answer: "The older approach treated content validity, criterion validity, and construct validity as separate, independent properties a test could possess. The modern framework reconceives validity as a single unified property: the degree to which evidence supports a specific interpretation and use of test scores. The five sources of evidence are not separate 'types' — they are converging lines of evidence in a validity argument. This matters because validity is now tied to a specific use, not the test itself. A test can be valid for one purpose and invalid for another, and the burden of building the validity argument falls on whoever is using the test."
  explanation: "The practical consequence is significant: organizations can no longer simply point to a published validation study and assume their use of the test is justified. They must ask whether the evidence supports their specific interpretation, with their specific population, for their specific purpose. This is a more demanding and contextual standard — which is exactly the point. Tests are powerful tools; the modern framework requires those using them to actively justify that power."
```

## Explainer

Your earlier work on construct validity, criterion validity, and content validity gave you three historically separate concepts that were once treated as distinct *types* of validity — as if a test could be "criterion valid" independently of whether it was "content valid." The modern framework, codified in the *Standards for Educational and Psychological Testing* (APA/AERA/NCME), rejects this fragmentation. Validity is now understood as a single, unified property: the degree to which evidence supports the interpretation and use of test scores for a specific purpose. The five sources of evidence are not separate validity types — they are different evidentiary lines that collectively build or undermine the validity argument for a particular use.

**Evidence from test content** examines whether the items adequately represent the domain the test claims to measure. This is the conceptual heir to content validity — subject matter experts judge whether the test covers the right content in the right proportions. But content coverage alone cannot establish validity; a history exam might perfectly represent the curriculum and still produce scores that are uninterpretable because of poor item wording. **Evidence from response processes** addresses this gap: it examines whether examinees are actually using the cognitive or behavioral processes the test intends to invoke. Think-aloud protocols, eye-tracking, and cognitive interviews reveal whether a "math reasoning" item is solved through reasoning or through test-taking tricks. If examinees bypass the intended process, the score does not mean what you think it means.

**Evidence from internal structure** uses factor analysis and related methods (building on your measurement prerequisites) to evaluate whether the relationships among items and subscales match the theoretical model. If a test claims to measure three distinct abilities but all items load on a single factor, the three-score interpretation lacks structural support. **Evidence from relations to other variables** encompasses the convergent, discriminant, and criterion-related evidence you have studied separately — correlations with theoretically related and unrelated constructs, and with outcomes the test is supposed to predict. These external relationships are the most direct test of whether the score captures the intended construct.

**Evidence from consequences** is the most controversial source. It asks whether the actual use of the test produces the intended outcomes and does not produce harmful unintended ones. From your hypothesis testing background, you know that a statistical result is only meaningful relative to a purpose — the same is true for test validity. A test that validly predicts job performance but systematically underestimates performance for one demographic group is not simply "valid" in the abstract; the consequences of its use constitute validity evidence against its current application. This fifth source reflects validity theory's shift from asking "is this a valid test?" to asking "is this a valid use of this test with these people for this purpose?" — a fundamentally more demanding and contextual standard.
