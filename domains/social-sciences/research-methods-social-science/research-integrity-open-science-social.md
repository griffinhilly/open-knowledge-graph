---
id: research-integrity-open-science-social
title: 'Research Integrity and Open Science: Transparency and Reproducibility'
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: research-ethics-human-subjects
  type: soft
tags:
- research-integrity
- open-science
- reproducibility
- preregistration
stage: expert
status: validated
---

# Research Integrity and Open Science: Transparency and Reproducibility

## Core Idea
Research integrity requires transparency about methods, data, and decisions. Open science practices—preregistration, data sharing, code availability—reduce researcher degrees of freedom and enable replication. Social science faces a reproducibility challenge; transparency improves reliability.

## Questions

```yaml
- question: "A researcher collects data and finds p = .06. They remove two participants flagged as potential outliers, find p = .049, and publish with no mention of the original analysis. This practice is best described as:"
  type: multiple-choice
  options:
    - "Appropriate data cleaning — outliers distort results and must be removed"
    - "P-hacking — using post-hoc, result-contingent decisions to push p below the significance threshold, exploiting researcher degrees of freedom"
    - "Acceptable because p = .049 technically falls below .05"
    - "Standard practice in social science because all outliers must be removed"
  answer: 1
  explanation: "This is a textbook example of exploiting researcher degrees of freedom. Decisions about outlier exclusion made after seeing results — and contingent on whether they produce significance — are not legitimate data cleaning. They inflate the false-positive rate because the researcher is effectively running multiple analyses and reporting only the one that worked. Preregistration would have required the exclusion criteria to be specified before data collection, preventing this."

- question: "A researcher preregisters the hypothesis that 'nature exposure reduces anxiety,' with a specific anxiety scale as the outcome. After running the study, they notice a second anxiety measure also shows a trend and report it prominently. How should this second finding be classified?"
  type: multiple-choice
  options:
    - "As strong confirmation of the preregistered hypothesis, since both measures reflect the same construct"
    - "As exploratory — a pattern not pre-specified that requires independent replication before being treated as confirmed"
    - "As more important than the preregistered result, since it was an unexpected discovery"
    - "As disconfirmatory, since it was not the primary outcome"
  answer: 1
  explanation: "Preregistration creates a clean distinction between confirmatory analysis (testing a pre-specified hypothesis with full inferential weight) and exploratory analysis (discovering post-hoc patterns that require replication). Both types of analysis are legitimate and valuable, but they differ in inferential status. Calling an exploratory finding 'confirmation' conflates hypothesis-testing with hypothesis-generation and is one of the mechanisms driving false positives in the literature."

- question: "The replication crisis in social science was primarily caused by deliberate fraud by individual researchers who fabricated or falsified their data."
  type: true-false
  answer: false
  explanation: "While fraud exists, it is not the primary cause of the replication crisis. The crisis arises from structural features: researcher degrees of freedom (many legitimate-seeming analytical choices that can be steered toward significance, even unconsciously) combined with publication bias (journals preferentially publish significant results, making null results invisible). These mechanisms produce inflated false-positive rates even when every researcher is acting in complete good faith. The crisis would persist even with zero fraud."

- question: "Preregistration prevents researchers from conducting any analyses beyond those specified in advance, eliminating all researcher flexibility in data analysis."
  type: true-false
  answer: false
  explanation: "Preregistration does not prohibit additional analysis — it creates transparency by distinguishing pre-specified (confirmatory) analyses from post-hoc (exploratory) ones. Researchers remain free to explore their data fully; they must simply label exploratory findings as such. The value of preregistration is accountability and clarity about inferential status, not restriction of scientific creativity. A preregistered study can have a rich exploratory section, as long as it is clearly labeled."

- question: "Explain why a publication bias problem could mislead the scientific literature even if every individual researcher is acting in complete good faith and reporting their results accurately."
  type: short-answer
  answer: "Even honest researchers preferentially write up and submit significant results. Journals preferentially publish significant results. Non-significant results — even from well-designed studies — go unreported or are rejected. Over time, the published literature becomes a biased sample that overrepresents positive findings, many of which are false positives or inflated effect sizes, because the filtering mechanism systematically excludes the null results that would correct the picture."
  explanation: "This is why the replication crisis is a structural problem, not primarily an ethics problem. Individual virtue cannot fix a selection process that filters the literature. Remedies must be structural too: preregistered reports (where journals commit to publish before seeing results), registered replication reports, data sharing requirements, and meta-analytic correction techniques like trim-and-fill. The problem is architectural — and so must be the solution."
```

## Explainer

Your prerequisite introduced research ethics in the context of human subjects — the rules that protect participants from harm. This topic addresses a different dimension of integrity: not participant harm but the reliability of scientific knowledge itself. The social sciences experienced what is now called the **replication crisis**: a series of high-profile failures when influential findings could not be reproduced by independent researchers. A 2015 project attempted to replicate 100 psychology studies and found that only about 36–39% produced significant results in the same direction. This is not primarily a story about fraud — it is a story about structural features of the research process that systematically inflate false-positive findings.

The key concept is **researcher degrees of freedom** — the many legitimate-seeming choices a researcher makes during data collection, processing, and analysis that can, consciously or not, be steered toward significant results. When to stop collecting data, which participants to exclude, which covariates to include, which of several plausible dependent variable operationalizations to use — each choice creates a fork. With enough forks, a researcher can almost always find a path to p < .05 even in the absence of a real effect. This is sometimes called **p-hacking** when intentional, but the same outcome arises from unconscious motivated reasoning. The research literature accumulates false positives because journals preferentially publish significant results (**publication bias**), so the non-significant replications that never get submitted are invisible.

**Preregistration** is the primary structural solution. Before collecting data, a researcher publicly registers their hypotheses, sample size, exclusion criteria, and analysis plan in a time-stamped repository (such as AsPredicted or OSF). This creates a clean separation between confirmatory analysis (testing the pre-specified hypothesis) and exploratory analysis (discovering patterns not anticipated in advance). Both are legitimate, but they have different inferential status: an exploratory finding requires replication before it is treated as confirmed. Preregistration does not eliminate researcher flexibility — it makes it transparent, allowing readers to evaluate which choices were made in advance versus post-hoc.

**Open data and open code** address the complementary problem of reproducibility. When data and analysis scripts are published alongside findings, other researchers can reproduce the exact results, catch errors, and run alternative analyses. This standard — increasingly required by journals and funders — represents a shift from "trust the author" to "verify the analysis." The infrastructure for this (GitHub, OSF, Zenodo) now makes sharing cheap; the main barriers are cultural and incentive-based. A researcher who shares imperfect data faces scrutiny they might avoid by not sharing; changing these incentives requires field-level norm change, not just individual virtue. Understanding these structural dynamics is what distinguishes integrity as a systems problem from integrity as a personal ethics problem.
