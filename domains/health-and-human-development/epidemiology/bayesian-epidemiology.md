---
id: bayesian-epidemiology
title: Bayesian Methods in Epidemiology
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: missing-data-epidemiology
  type: soft
- id: multivariable-regression-epi
  type: hard
tags:
- bayesian-inference
- prior-specification
- posterior-inference
stage: expert
status: draft
---

# Bayesian Methods in Epidemiology

## Core Idea
Bayesian epidemiology combines prior beliefs about parameters with observed data to produce posterior distributions. Bayesian methods naturally handle complex models, missing data, and indirect evidence, and yield probabilistic statements about parameters and hypotheses.

## Questions

```yaml
- question: "A Bayesian analysis produces a 95% credible interval of [1.2, 3.4] for a relative risk. What can you directly conclude?"
  type: multiple-choice
  options:
    - "There is a 95% chance the true relative risk is between 1.2 and 3.4, given the data and prior"
    - "If the study were repeated 100 times, 95 of the resulting intervals would contain the true value"
    - "The null hypothesis (RR = 1) is rejected at the 5% significance level"
    - "The p-value for the effect is less than 0.05"
  answer: 0
  explanation: "The 95% credible interval has the direct probabilistic interpretation: given the observed data and the prior, there is a 95% posterior probability that the parameter lies in this range. This is the statement practitioners actually want. Options B describes a frequentist confidence interval, which makes no probability statement about the fixed true parameter — it refers to the long-run behavior of the procedure. Options C and D conflate Bayesian credible intervals with null-hypothesis significance testing, which is a frequentist concept."

- question: "A Bayesian epidemiologist runs an analysis with an informative prior derived from three prior studies. A colleague argues the results are invalid because of prior dependence. What is the most accurate response?"
  type: multiple-choice
  options:
    - "The prior makes the analysis invalid; only non-informative priors are scientifically acceptable"
    - "The prior is appropriate as long as it is substantively defensible and sensitivity analyses show robust conclusions across plausible priors"
    - "Informative priors are only valid when the data are sparse; with sufficient data the prior is irrelevant regardless"
    - "The Bayesian analysis should be replaced with a frequentist meta-analysis to avoid subjectivity"
  answer: 1
  explanation: "Informative priors are scientifically legitimate when they reflect genuine prior knowledge from past studies or mechanistic reasoning. The appropriate response to concerns about prior influence is not to abandon the prior but to conduct sensitivity analyses — showing how conclusions change across a range of plausible priors. When results are robust (prior-robust), the evidence is convincing. When results depend heavily on the prior, this honestly reveals that data alone cannot resolve the question. Non-informative priors are not inherently more objective; they make their own implicit choices and can sometimes be poorly suited to constrained parameters like relative risks."

- question: "When prior data are sparse and the observed dataset is small, the posterior distribution in a Bayesian analysis will be heavily influenced by the prior."
  type: true-false
  answer: true
  explanation: "This is a core feature — and a core responsibility — of Bayesian inference. The posterior is proportional to the prior times the likelihood. When data are scarce (the likelihood is flat or weakly informative), the prior carries more weight in determining the posterior. When data are abundant, the likelihood dominates and the prior matters little. This is why prior specification is especially consequential in rare-disease epidemiology or small-sample studies, and why sensitivity analyses over different prior choices are essential in those settings."

- question: "A Bayesian posterior probability directly answers questions like 'What is the probability the true effect exceeds a clinically meaningful threshold?' — something frequentist p-values can answer equally well."
  type: true-false
  answer: false
  explanation: "This is a critical distinction. A frequentist p-value answers: 'What is the probability of observing data this extreme or more, assuming the null hypothesis is true?' It does not answer questions about the probability that the true parameter exceeds a threshold. A Bayesian posterior distribution does answer that question directly: you simply compute the posterior probability that the parameter exceeds the threshold of interest. This is why practitioners often find Bayesian outputs more naturally interpretable — they match the actual clinical or public health question being asked."

- question: "In your own words, explain how a posterior distribution combines prior beliefs and observed data, and describe what it means for a Bayesian result to be 'prior-robust.'"
  type: short-answer
  answer: "The posterior distribution is proportional to the prior distribution times the likelihood: P(θ|D) ∝ P(θ) × P(D|θ). The prior encodes beliefs about the parameter before observing the data; the likelihood reflects how probable the observed data are under each possible parameter value. The posterior combines these, weighting prior beliefs by how well they predict the observed data. A result is prior-robust when the posterior conclusions (e.g., the credible interval, or the posterior probability that the effect exceeds a threshold) remain substantively similar across a range of defensible prior specifications — informative, weakly informative, and non-informative. Prior robustness means the data are sufficiently informative to override prior differences, making the conclusions credible to analysts who hold different prior beliefs."
  explanation: "Prior robustness is the Bayesian analog of sensitivity analysis in frequentist work. It doesn't mean the prior is irrelevant — it means the data are strong enough that reasonable prior disagreements don't change the conclusions. When results are not robust across priors, this is itself a scientifically important finding: it means the study alone cannot resolve the question, and more data or clearer prior knowledge is needed."
```

## Explainer

From your work in multivariable regression, you are accustomed to a particular mode of inference: fit a model to the data, estimate coefficients, compute confidence intervals, and evaluate statistical significance via p-values. This is the **frequentist** framework — parameters are treated as fixed (if unknown) quantities, and probability refers to long-run frequencies over hypothetical repeated samples. Bayesian inference offers a different and complementary framework. In Bayesian thinking, parameters are treated as **random variables** with probability distributions, and "probability" describes your degree of belief given the available information. The payoff is that you can make direct probabilistic statements about the parameters themselves — not just about hypothetical repeated samples.

The mechanics rest on Bayes' theorem. You begin with a **prior distribution** P(θ) that encodes your beliefs about a parameter θ before observing new data. After collecting data D, you update via the likelihood P(D|θ) — the probability of observing those data given each possible value of the parameter. The result is the **posterior distribution**: P(θ|D) ∝ P(θ) × P(D|θ). In words: your posterior belief is your prior belief, updated by the evidence from the data. The posterior combines what you knew before the study with what the data tell you, weighted by how informative the data are. When data are abundant and informative, the posterior will be dominated by the likelihood, and the choice of prior matters little. When data are sparse, the prior carries more weight — which is both a strength and a responsibility, since the choice of prior then substantially influences conclusions.

In epidemiology, Bayesian methods offer several concrete advantages over purely frequentist approaches. First, **prior information from previous studies or mechanistic knowledge** can be formally incorporated. If you are studying the effect of a well-characterized exposure in a new population, a prior derived from meta-analytic estimates of effect sizes in similar populations is a rational and efficient use of scientific knowledge. Second, Bayesian **posterior distributions** directly answer the questions practitioners actually want to ask: "Given these data, what is the probability that the true relative risk exceeds 1.5?" — something a p-value cannot tell you. Third, complex hierarchical models (multilevel, longitudinal, spatial), missing data problems, and models with many parameters are often more tractable in a Bayesian framework, where **Markov Chain Monte Carlo (MCMC)** sampling algorithms can approximate posterior distributions even when analytic solutions are unavailable.

The key practical challenge in Bayesian epidemiology is **prior specification** — choosing prior distributions that are substantively defensible and not inadvertently dominating the analysis. Analysts often report sensitivity analyses using different priors (informative priors versus weakly informative or non-informative priors) to show how conclusions change with prior assumptions. When results are robust across a range of plausible priors, the posterior is said to be **prior-robust**, and the evidence is convincing. When results depend heavily on the prior, the analysis honestly reveals that the data alone are insufficient to resolve the question, which is itself a scientifically important finding.
