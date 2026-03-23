---
id: reproducibility-preregistration
title: Pre-Registration and Open Science Practices
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: research-integrity-open-science-social
  type: hard
- id: research-design-advanced
  type: soft
builds-toward:
- multi-site-replication-studies
- registered-reports
tags:
- open-science
- reproducibility
- transparency
- preregistration
stage: expert
status: draft
---

# Pre-Registration and Open Science Practices

## Core Idea
Pre-registration documents analysis plans before data collection or analysis, reducing researcher degrees of freedom and distinguishing confirmatory from exploratory analyses. Open science practices—sharing code, data, materials, and preprints—enable reproduction and verification. The credibility crisis in social science stems partly from selective reporting; pre-registration and transparency are institutional solutions. However, openness must be balanced against privacy, proprietary concerns, and equitable access to resources.

## Questions

```yaml
- question: "A researcher runs an experiment, tries several different analytic choices (exclusion criteria, covariates, outcome operationalizations) after seeing the data, and publishes the one analysis where p < .05 without noting the others. Is this scientific fraud?"
  type: multiple-choice
  options:
    - "Yes — selectively reporting analyses is legally and ethically equivalent to data fabrication"
    - "Not necessarily; it exploits researcher degrees of freedom in a way that inflates false positives even without any intent to deceive"
    - "No — running multiple analyses is standard scientific practice that does not alter error rates"
    - "Only if the excluded analyses showed the opposite finding; otherwise the published result is valid"
  answer: 1
  explanation: "This is the core insight about researcher degrees of freedom: honest researchers making individually defensible analytic choices after seeing data can systematically inflate false positive rates without intending to deceive. Running 20 analytic choices at α = .05 is roughly equivalent to running 20 significance tests — the probability of finding a 'significant' result by chance compounds. Pre-registration addresses this structural problem by requiring choices to be locked in before the data are seen, not by assuming researchers are dishonest."

- question: "A critic argues that pre-registration prevents scientific discovery by limiting researchers to their original hypotheses. What is the most accurate response to this critique?"
  type: multiple-choice
  options:
    - "The critic is right — pre-registration eliminates all exploratory analysis and should be used selectively"
    - "Pre-registration constrains confirmatory analyses but explicitly permits exploratory analyses, which must simply be labeled as such"
    - "All research must be confirmatory; exploratory work is inherently unreliable and should not be published"
    - "Pre-registration solves p-hacking but does so at the cost of eliminating hypothesis generation"
  answer: 1
  explanation: "Pre-registration does not prohibit exploration — it requires honesty about which analyses are confirmatory (pre-specified) and which are exploratory (post-hoc). Both types of research are scientifically valuable. Exploratory analyses generate hypotheses for future confirmatory tests; the problem arises when exploratory results are presented as if they were confirmatory. Pre-registration restores the distinction rather than eliminating one type of research."

- question: "Researcher degrees of freedom — the many underdetermined analytic decisions in any study — can inflate false positive rates even when every individual decision seems defensible and no fraud occurs."
  type: true-false
  answer: true
  explanation: "This is the central insight motivating pre-registration. Decisions like which observations to exclude, how to operationalize a construct, whether to add covariates, and when to stop data collection are each individually reasonable, but each creates an additional opportunity to find a significant result by chance. The cumulative effect of these choices, made while looking at the data, produces an actual false positive rate that can far exceed the nominal α = .05. Structural fixes like pre-registration address this without requiring researchers to be dishonest."

- question: "Pre-registration is primarily a response to deliberate fraud and dishonesty among researchers."
  type: true-false
  answer: false
  explanation: "Pre-registration targets inadvertent false positives from analytic flexibility and publication bias, not deliberate fraud. Most researchers are honest. The problem is that the incentive structure — rewarding significant, surprising findings — combines with researcher degrees of freedom to make it easy to find 'significant' results without ever consciously intending to deceive. Fraud is a separate problem addressed by data audits and replication; pre-registration addresses the structural inflation of false positives that occurs even in completely honest research."

- question: "Explain how 'researcher degrees of freedom' can produce false positive findings even when every individual analytic decision is defensible."
  type: short-answer
  answer: "Each underdetermined analytic decision — exclusion criteria, operationalization choices, covariate inclusion, stopping rules — made after seeing the data constitutes an implicit significance test. If a researcher tries different combinations until one yields p < .05, the probability that at least one combination is significant by chance is much higher than α = .05, even though each individual decision was locally reasonable. The cumulative effect is an actual false positive rate far above the nominal level, without any single identifiable dishonest act."
  explanation: "This is sometimes called the 'garden of forking paths': each branching analytic choice is a path through the data, and the researcher implicitly (or explicitly) selects the path that yields a publishable result. Because the alternatives are not reported, readers cannot see how many paths were tried. Pre-registration closes this problem by requiring the path to be chosen before entering the garden — so what looks like a single confirmatory test actually is one."
```

## Explainer

The credibility problem in social science research is not primarily one of fraud. Most researchers are honest. The problem is structural: the incentive system rewards publishing surprising, statistically significant findings, while the publication process lacks mechanisms to detect whether those findings emerged from rigorous analysis or from selective reporting after the fact. **Pre-registration** is a structural fix designed to close this gap — not by making researchers more virtuous, but by making the incentive problem visible and correctable.

The mechanism is simple: before collecting or analyzing data, you deposit a time-stamped document (typically on OSF, AsPredicted, or a trial registry) specifying your hypotheses, your key measures, your sample size, and your planned analyses. Once the study is complete, readers can compare what you said you would do with what you actually did. Any deviations must be acknowledged and justified. This makes the distinction between **confirmatory research** (testing a pre-specified hypothesis) and **exploratory research** (mining data for patterns) legible from the outside. Both types of research are valuable — exploratory work generates hypotheses for future confirmatory tests — but conflating them by presenting exploratory results as if they were confirmatory is a primary driver of irreplicability.

**Researcher degrees of freedom** refers to the many underdetermined decisions in any analysis: which observations to exclude, how to operationalize a construct, which covariates to include, when to stop collecting data. Each decision, made after seeing the data, creates an opportunity to find significance by accident. A researcher exploring 20 analytic choices is roughly equivalent to running 20 significance tests at α = .05 — even if every individual decision seems defensible. Pre-registration constrains these decisions in advance, removing the flexibility to search for a favorable result while preserving the ability to do honest exploratory follow-up.

**Open science practices** extend this transparency logic across the full research stack. Sharing **code** allows others to verify that analysis was performed as described. Sharing **data** (where privacy permits) enables replication and secondary analysis. Sharing **materials** — stimuli, survey instruments, interview protocols — allows other researchers to build on your work without reinventing it. **Preprints** accelerate scientific communication by making findings available before peer review, while the peer review record documents what changes were made. None of these practices guarantees correct findings, but together they shift research from a trust-based to a verification-based system. The key tension to hold: openness is not always possible (sensitive populations, proprietary partners, low-resource settings) and requirements imposed without institutional support can reproduce inequality across research contexts.
