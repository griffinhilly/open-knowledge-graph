---
id: bayesian-biostatistics
title: Bayesian Methods in Biostatistics
domain: health-and-human-development
course: biostatistics
prerequisites:
- id: probability-axioms
  type: hard
- id: power-and-sample-size
  type: soft
- id: clinical-trial-design-intro
  type: soft
builds-toward:
- adaptive-trial-designs
tags:
- Bayesian
- prior
- posterior
- credible-interval
- MCMC
- Bayes-theorem
stage: expert
status: validated
---

# Bayesian Methods in Biostatistics

## Core Idea
Bayesian biostatistics uses Bayes' theorem to update prior beliefs about parameters with observed data to produce posterior distributions: P(theta|data) proportional to P(data|theta) × P(theta). Unlike frequentist methods, which report what the data tell you about the probability of the data under a fixed parameter, Bayesian methods report the probability of the parameter given the data — the quantity clinicians actually want. The posterior distribution provides a complete summary of uncertainty: point estimates (posterior mean or median), interval estimates (credible intervals that have a direct probabilistic interpretation — "there is a 95% probability that the treatment effect lies in this interval"), and direct probability statements about hypotheses ("the probability that the treatment is effective is 0.93"). The choice of prior distribution is both the method's greatest strength (incorporating existing knowledge) and its primary source of controversy (potential subjectivity).

## Questions

```yaml
- question: "A frequentist 95% confidence interval for a treatment effect is [2, 8]. A Bayesian 95% credible interval with a non-informative prior is [2.1, 7.9]. What is the key interpretive difference?"
  type: multiple-choice
  options:
    - "There is no meaningful difference — both intervals contain the true value with 95% probability"
    - "The confidence interval means: if we repeated the study many times, 95% of computed intervals would contain the true value. The credible interval means: given the observed data and prior, there is a 95% probability the true value lies in this interval"
    - "The credible interval is always narrower than the confidence interval"
    - "The confidence interval is for the data; the credible interval is for the parameter"
  answer: 1
  explanation: "This is the fundamental philosophical distinction. A frequentist confidence interval is a statement about the long-run performance of the procedure — any single interval either contains the true value or does not, with no probability attached. A Bayesian credible interval is a direct probability statement about the parameter: given the data and prior, the probability that the true value falls in the interval is 95%. The credible interval answers the question clinicians are actually asking. With non-informative priors, the two intervals are often numerically similar, but their interpretations differ fundamentally."

- question: "A researcher uses a strong prior centered on a treatment effect of 0 (skeptical prior) in a Bayesian analysis. Critics argue this biases the results. Is this criticism valid?"
  type: multiple-choice
  options:
    - "Yes — any informative prior is biased and should never be used"
    - "Partially — the prior shifts the posterior toward 0, which may be appropriate (incorporating healthy skepticism about treatment claims) or inappropriate (ignoring strong pre-existing evidence), depending on context. The choice of prior should be transparent and sensitivity-analyzed"
    - "No — the prior has no effect on the posterior when the sample size is large"
    - "No — Bayesian methods are immune to bias by construction"
  answer: 1
  explanation: "A skeptical prior is a deliberate choice to require strong data evidence before concluding a treatment works — analogous to the frequentist framework's conservative alpha level. It is appropriate when most treatments fail and prior evidence is weak. It is inappropriate when substantial previous evidence supports the effect. The key to valid Bayesian analysis is transparency (reporting the prior and its justification) and sensitivity analysis (showing how results change under different priors). If the data are overwhelming, the posterior will be dominated by the data regardless of the prior."

- question: "Bayesian methods are particularly advantageous for clinical trial monitoring because they can compute the posterior probability that a treatment is effective at each interim analysis without requiring multiple testing corrections."
  type: true-false
  answer: true
  explanation: "In frequentist interim monitoring, each look at the data inflates the Type I error rate, requiring alpha-spending functions or group sequential boundaries to maintain overall alpha. Bayesian methods do not have this problem because they update the posterior distribution continuously — each analysis simply produces a new posterior given all data so far. The posterior probability that the treatment is effective (e.g., P(treatment effect > 0 | data)) can be computed at any time without adjusting for the number of looks. This makes Bayesian methods natural for adaptive trial designs, where the decision to continue, stop, or modify the trial depends on accumulating evidence."

- question: "Explain why Bayesian analysis is said to answer the question clinicians actually care about, and what makes this different from the frequentist answer."
  type: short-answer
  answer: "Clinicians want to know: given the data from this study, what is the probability that the treatment works? Bayesian analysis answers this directly through the posterior probability. Frequentist analysis answers a different question: if the treatment had no effect, what is the probability of observing data this extreme or more? The p-value is about the probability of the data given a hypothesis (no effect), not the probability of the hypothesis given the data. Clinicians naturally think in Bayesian terms — 'how confident should I be that this treatment helps?' — but frequentist output requires careful translation."
  explanation: "The inversion is subtle but consequential. P(data | H0) ≠ P(H0 | data). A p-value of 0.03 does not mean there is a 3% chance the null is true — it means there is a 3% chance of seeing data this extreme if the null were true. The posterior probability P(H1 | data) that clinicians want requires Bayes' theorem and a prior. This distinction is one of the most frequently misunderstood concepts in applied statistics."
```

## Explainer

Frequentist statistics — the framework underlying p-values, confidence intervals, and hypothesis tests — dominates biostatistics training and practice. But it answers questions in a circuitous way. A p-value of 0.03 tells you: if the null hypothesis were true, there would be only a 3% chance of observing data this extreme. It does not tell you the probability that the null hypothesis is true or that the treatment works. Bayesian statistics, by contrast, directly computes the probability of hypotheses and parameter values given the observed data. This directness comes at a cost: you must specify a **prior distribution** reflecting what was known or believed before the data were collected.

**Bayes' theorem** provides the machinery: posterior ∝ likelihood × prior. The **likelihood** is the same function used in frequentist analysis — it captures what the data say about the parameter. The **prior** encodes pre-existing knowledge: previous studies, biological plausibility, or deliberate skepticism. The **posterior** combines both, representing updated knowledge after seeing the data. With large samples, the data dominate and the posterior is insensitive to the prior. With small samples, the prior matters more — which is either a feature (incorporating legitimate knowledge) or a concern (importing unjustified assumptions), depending on the quality of the prior information.

The practical outputs of Bayesian analysis are more intuitive than their frequentist counterparts. A **credible interval** has a direct probabilistic interpretation: "there is a 95% probability that the treatment effect lies between 3 and 12 units." A **posterior probability** answers clinical questions directly: "the probability that this treatment reduces mortality by at least 5% is 0.87." These statements are what clinicians naturally want but what frequentist inference cannot provide without additional assumptions.

Bayesian methods are increasingly used in clinical trials, particularly **adaptive designs** where the trial is modified based on accumulating data. Because the posterior updates continuously, Bayesian monitoring does not suffer from the multiple testing penalties that plague frequentist interim analyses. The FDA has endorsed Bayesian methods for medical device trials, and Bayesian adaptive platforms are becoming standard in oncology. Computational advances — particularly **Markov Chain Monte Carlo** (MCMC) methods implemented in software like Stan, BUGS, and JAGS — have made complex Bayesian models practical, overcoming the analytical intractability that historically limited Bayesian applications to simple problems.
