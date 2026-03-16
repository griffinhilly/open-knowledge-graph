---
id: domain-sampling-theory-reliability-generalization
title: Domain Sampling Theory and Generalization of Reliability
domain: psychology
course: psychometrics
prerequisites:
- id: true-score-theory-and-measurement-error
  type: hard
builds-toward:
- alpha-reliability-internal-consistency
- parallel-and-equivalent-test-forms
tags:
- reliability
- sampling
- item-universe
stage: advanced
status: draft
---

# Domain Sampling Theory and Generalization of Reliability

## Core Idea
Domain sampling theory conceptualizes a test as a sample from an infinite universe of possible items measuring the same construct. Reliability reflects how well items generalize to the entire domain; larger and more homogeneous samples yield higher reliability. This framework explains why internal consistency can estimate test-retest stability and justifies using item-level statistics to predict full-test behavior.

## How It's Best Learned
Work through numerical examples showing how adding items and increasing inter-item correlation improve reliability estimates. Simulate sampling from hypothetical item universes to visualize the sampling distribution of reliability coefficients.

## Common Misconceptions
- Assuming reliability equals validity (they are independent properties)
- Thinking item homogeneity (similarity) is always desirable (too-high alpha suggests redundancy)

## Explainer

From true score theory, you already know that any observed score is a combination of a true score and measurement error: X = T + E. Domain sampling theory asks a more ambitious question: what, exactly, is the true score a true score *of*? The answer is the mean score a person would receive if they answered every possible item in the entire **item universe** — the hypothetically infinite pool of questions that could legitimately test the same construct. The test you actually give is a random sample from that universe, just as a survey polls a sample of voters to estimate the whole electorate's opinion. Reliability, reframed this way, is the expected correlation between your sample of items and any other independent sample from the same universe. A highly reliable test is one that would generalize — score almost the same — regardless of which particular items happened to be drawn.

This sampling metaphor makes several otherwise mysterious facts about reliability suddenly intuitive. First, why does adding more items increase reliability? Because a larger sample is a better estimate of the population mean. If you ask five questions about someone's extraversion, you get a noisier estimate than if you ask twenty. The **Spearman-Brown prophecy formula** formalizes this: double the number of parallel items and the reliability gain follows a predictable curve (with diminishing returns). Second, why does higher inter-item correlation raise reliability? Because items that correlate more strongly are drawing from a tighter, more homogeneous region of the item universe — each item is covering roughly the same ground, so each is a good proxy for every other.

But the third insight is the most important for test design: there is a ceiling on how similar items should be. If all twenty items are near-paraphrases of each other, **alpha** will approach 1.0, but you have not measured more of the construct — you have measured the same narrow slice twenty times. This is the paradox of internal consistency as a sole reliability criterion: maximizing alpha can shrink the breadth of what you measure even as it inflates the coefficient. Domain sampling theory clarifies the trade-off: you want items that are representative of the full item universe (broad coverage), not merely redundant with each other. The correct target is a test that samples *widely and consistently* from the domain, not one that obsessively asks the same question in different words.

Practically, domain sampling theory licenses the use of internal consistency (coefficient alpha or omega) as a substitute for test-retest reliability under reasonable assumptions. If items are truly drawn from the same universe, the pattern of inter-item covariances captures the signal-to-noise ratio that would be observed across repeated testings — without actually running the test twice. This is theoretically powerful but assumption-laden: the item universe must be homogeneous (single construct), items must be locally independent (no item depends on another), and the sample must be administered consistently. When these assumptions are met, alpha is a lower bound on reliability; when they are violated, alpha can be deeply misleading in either direction.
