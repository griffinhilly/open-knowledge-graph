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
stage: expert
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

## Questions

```yaml
- question: "A test developer wants to maximize reliability of a 20-item extraversion scale. She replaces 10 diverse items with near-paraphrases of the 10 highest-loading items. Coefficient alpha rises from 0.82 to 0.94. Has the test improved?"
  type: multiple-choice
  options:
    - "Yes — higher alpha means greater reliability and therefore a better test"
    - "Not necessarily — the higher alpha likely reflects item redundancy, narrowing construct coverage without genuinely improving measurement"
    - "Yes — alpha above 0.90 is the accepted threshold for high-quality psychometric instruments"
    - "No — alpha above 0.90 always indicates overfit and requires redesign from scratch"
  answer: 1
  explanation: "Domain sampling theory reveals the paradox: alpha can be inflated by making items redundant rather than by measuring the construct more reliably. If all items ask the same question in slightly different words, alpha approaches 1.0 — but the test is sampling a narrow slice of the domain repeatedly. Higher alpha through redundancy shrinks construct coverage. The correct target is items spread widely across the item universe that still cohere around a single construct."

- question: "Domain sampling theory explains why adding more items increases reliability. Which analogy best captures this logic?"
  type: multiple-choice
  options:
    - "Adding more scales to a weighing room increases the total weight measured"
    - "A larger random sample from a population gives a more accurate estimate of the population mean — more items give a better estimate of the person's true score in the item universe"
    - "More items reduce individual item errors because measurement errors are always independent"
    - "Additional items increase content validity, which causes reliability to rise as a consequence"
  answer: 1
  explanation: "Domain sampling theory treats items as a sample from an infinite item universe, just as a survey samples voters from an electorate. A larger sample estimates the population parameter more accurately — variance of the sample mean decreases as n increases. Similarly, more test items give a better estimate of the person's 'true score' — their mean score across the entire item universe. This is why the Spearman-Brown formula shows predictable reliability gains from lengthening a test."

- question: "Coefficient alpha is a lower bound on reliability — the true reliability of a test is at least as high as its alpha, assuming the test measures a single construct with locally independent items."
  type: true-false
  answer: true
  explanation: "Under the assumptions of essentially tau-equivalent items (items measuring the same construct with equal true score variances) and local independence, alpha equals reliability. When items are congeneric (slightly different factor loadings), alpha underestimates reliability. Thus alpha is a conservative lower bound: the true reliability is at least alpha, often higher. This is why alpha should be viewed as a minimum estimate, not an exact value."

- question: "High internal consistency (alpha ≈ 0.95) guarantees that a test is measuring a broad and representative sample of the construct's item universe."
  type: true-false
  answer: false
  explanation: "High alpha indicates items correlate strongly with each other — but strong inter-item correlation can result from narrow redundancy (all items ask the same thing differently) or from broad coverage of a coherent construct. Alpha cannot distinguish between these two causes. A test can achieve alpha = 0.95 by asking five nearly identical questions about a tiny corner of a construct, which would be a psychometric failure despite the high coefficient."

- question: "Why does the domain sampling framework create a tension between maximizing internal consistency and achieving broad construct coverage?"
  type: short-answer
  answer: "Domain sampling theory treats items as a sample from an infinite item universe. Making items more similar (higher inter-item correlations) raises alpha — but it means sampling a narrower region of the domain more densely rather than covering the full universe. The ideal test samples widely from the item universe (broad coverage) while all items still measure the same construct (coherence). Maximizing alpha through redundancy sacrifices breadth; the correct optimization target is representative sampling, not alpha maximization."
  explanation: "This tension is practically important in scale construction. A test designed purely to maximize alpha will tend to converge on the same few high-loading items asked repeatedly, narrowing what is actually assessed. Domain sampling theory provides the corrective: think of item selection as representative sampling from a conceptual universe, not as alpha optimization. Coefficient alpha is an index of that sampling quality, not the goal itself."
```

## Explainer

From true score theory, you already know that any observed score is a combination of a true score and measurement error: X = T + E. Domain sampling theory asks a more ambitious question: what, exactly, is the true score a true score *of*? The answer is the mean score a person would receive if they answered every possible item in the entire **item universe** — the hypothetically infinite pool of questions that could legitimately test the same construct. The test you actually give is a random sample from that universe, just as a survey polls a sample of voters to estimate the whole electorate's opinion. Reliability, reframed this way, is the expected correlation between your sample of items and any other independent sample from the same universe. A highly reliable test is one that would generalize — score almost the same — regardless of which particular items happened to be drawn.

This sampling metaphor makes several otherwise mysterious facts about reliability suddenly intuitive. First, why does adding more items increase reliability? Because a larger sample is a better estimate of the population mean. If you ask five questions about someone's extraversion, you get a noisier estimate than if you ask twenty. The **Spearman-Brown prophecy formula** formalizes this: double the number of parallel items and the reliability gain follows a predictable curve (with diminishing returns). Second, why does higher inter-item correlation raise reliability? Because items that correlate more strongly are drawing from a tighter, more homogeneous region of the item universe — each item is covering roughly the same ground, so each is a good proxy for every other.

But the third insight is the most important for test design: there is a ceiling on how similar items should be. If all twenty items are near-paraphrases of each other, **alpha** will approach 1.0, but you have not measured more of the construct — you have measured the same narrow slice twenty times. This is the paradox of internal consistency as a sole reliability criterion: maximizing alpha can shrink the breadth of what you measure even as it inflates the coefficient. Domain sampling theory clarifies the trade-off: you want items that are representative of the full item universe (broad coverage), not merely redundant with each other. The correct target is a test that samples *widely and consistently* from the domain, not one that obsessively asks the same question in different words.

Practically, domain sampling theory licenses the use of internal consistency (coefficient alpha or omega) as a substitute for test-retest reliability under reasonable assumptions. If items are truly drawn from the same universe, the pattern of inter-item covariances captures the signal-to-noise ratio that would be observed across repeated testings — without actually running the test twice. This is theoretically powerful but assumption-laden: the item universe must be homogeneous (single construct), items must be locally independent (no item depends on another), and the sample must be administered consistently. When these assumptions are met, alpha is a lower bound on reliability; when they are violated, alpha can be deeply misleading in either direction.
