---
id: validity-construct-internal-external
title: 'Validity: Construct, Internal, External, and Statistical'
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: operationalization-construct-validity
  type: hard
builds-toward:
- regression-diagnostics-assumption-violations
tags:
- validity
- threats
- inference
stage: advanced
status: draft
---

# Validity: Construct, Internal, External, and Statistical

## Core Idea
Validity concerns whether we measure what we claim (construct validity), whether observed associations reflect causal effects (internal validity), and whether findings generalize (external validity). Each type faces distinct threats, and research trade-offs often exist between them.

## Explainer

You already know that operationalization — translating an abstract concept into a measurable indicator — is one of the most consequential choices in research design. Validity is the framework for evaluating whether that translation succeeded and whether the inferences you draw from your measurements are trustworthy. The four types of validity are not interchangeable: each asks a different question, faces different threats, and requires different defenses.

**Construct validity** is the most foundational: does your measure actually capture the concept you claim to be measuring? You want to study "democratic legitimacy," but you measure it with a single survey item asking whether respondents trust the government. Trust and legitimacy are related but distinct constructs — legitimacy involves normative acceptance of authority, while trust is an expectation about behavior. A measure that conflates them has poor construct validity. Threats to construct validity include **mono-operation bias** (relying on a single indicator for a complex construct), **construct underrepresentation** (the measure captures only part of the concept), and **construct-irrelevant variance** (the measure picks up noise unrelated to the concept). The defenses are convergent validity (the measure correlates with other measures of the same construct), discriminant validity (it does not correlate with measures of different constructs), and content validity (expert judgment that the measure covers the construct's full domain).

**Internal validity** asks whether the observed association between your independent and dependent variables reflects a genuine causal effect or whether some confounding explanation is responsible. If you find that countries with higher newspaper readership have lower corruption, you cannot conclude that newspapers cause accountability — wealthier countries may have both more newspapers and better institutions, and wealth is the real cause. Threats to internal validity include **confounding** (omitted variables), **selection bias** (non-random assignment to conditions), **history** (external events during the study period), **maturation** (natural change over time), and **regression to the mean** (extreme cases are sampled because they are extreme, then move toward average). Random assignment to experimental conditions addresses most of these threats simultaneously, which is why randomized experiments are the gold standard for internal validity.

**External validity** asks whether findings generalize beyond the specific sample, context, and time period of the study. A highly controlled lab experiment may have excellent internal validity — you know the effect is causal — but poor external validity if the lab setting is so artificial that the effect disappears in real-world conditions. Survey experiments conducted on online convenience samples may not generalize to the general population. This is not a minor methodological nicety: a finding that is internally valid but externally invalid tells you about a world that does not exist. The tension between internal and external validity is real and irreducible: the controls that maximize internal validity often reduce external validity by creating artificial conditions.

**Statistical conclusion validity** is the fourth type: even if your construct is well-measured and your design is clean, are your statistical inferences about the association correct? Threats include insufficient **statistical power** (your sample is too small to detect a real effect), **violated statistical assumptions** (using a test whose assumptions your data do not meet), and **multiple comparisons** (testing so many hypotheses that some will appear significant by chance). Understanding these four types of validity together is essential because research trade-offs often force choices: randomized field experiments can have high internal and external validity but may require constructs that are operationalizable in the field. Lab experiments can tightly control confounders but sacrifice ecological realism. Good research design is an argument that the validity types most essential to your specific inferential claim are adequately protected.
