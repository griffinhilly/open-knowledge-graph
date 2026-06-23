---
id: bayesian-inference-intro
title: Introduction to Bayesian Inference
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: bayes-theorem
  type: hard
- id: probability-spaces-measure-theoretic
  type: soft
- id: bayesian-statistics-fundamentals
  type: soft
- id: maximum-likelihood-estimation-theory-probability-and-statistics
  type: soft
builds-toward:
- bayesian-point-estimation
tags:
- bayesian
- inference
- probability
stage: formal-systems
status: validated
---
# Introduction to Bayesian Inference

## Core Idea
Bayesian inference uses Bayes' rule to update prior beliefs about parameters given data: P(θ|data) ∝ P(data|θ)P(θ). The posterior distribution combines information from the prior and likelihood. Bayesian methods naturally incorporate prior knowledge and quantify uncertainty.

## How It's Best Learned
Apply Bayes' rule to simple problems with discrete parameters. Compare frequentist and Bayesian confidence/credible intervals. Choose sensible priors for familiar distributions. Recognize sensitivity of conclusions to prior specification.

## Questions

```yaml
- question: "A Bayesian analyst computes a 95% credible interval for a parameter θ. What does this interval correctly claim?"
  type: multiple-choice
  options:
    - "If we repeated the experiment many times, 95% of the computed intervals would contain the true θ"
    - "Given the observed data and the prior, there is a 95% probability that θ lies within this interval"
    - "θ is guaranteed to lie in this interval with 95% certainty regardless of the prior used"
    - "The interval contains 95% of the observed data values"
  answer: 1
  explanation: "Option B is the correct Bayesian interpretation: the credible interval is a statement about the posterior distribution — given this data and prior, P(θ ∈ interval | data) = 0.95. Option A is the frequentist confidence interval interpretation, which is subtly different and is often what people mistakenly attribute to both. The frequentist interval makes no probability claim about the specific interval computed; it describes a procedure that works 95% of the time in repeated sampling. The Bayesian interval directly answers the question practitioners typically want answered."

- question: "Two analysts apply Bayesian inference to the same dataset of 1,000 observations where evidence strongly suggests θ ≈ 0.8. Analyst A uses an informative prior strongly concentrated near θ = 0. Analyst B uses a flat (uniform) prior. What happens to their posteriors?"
  type: multiple-choice
  options:
    - "They remain dramatically different because the prior always determines the posterior"
    - "They converge to approximately the same posterior because the large likelihood from 1,000 data points overwhelms both priors"
    - "Analyst A's posterior peaks near 0, Analyst B's peaks near 0.8"
    - "Only Analyst B's analysis is valid; informative priors are not permitted in Bayesian inference"
  answer: 1
  explanation: "With 1,000 data points, the likelihood P(data|θ) is extremely concentrated and dominates both priors. Even Analyst A's prior, which favors θ = 0, is overwhelmed by the cumulative evidence from so many observations. Both posteriors will peak near 0.8. This is a key feature of Bayesian inference: when data is plentiful, the prior matters little and analysts with different priors reach similar conclusions. The prior matters most — and sensitivity analysis becomes critical — when data is sparse."

- question: "A frequentist 95% confidence interval and a Bayesian 95% credible interval answer the same question about parameter uncertainty, just using different calculation methods."
  type: true-false
  answer: false
  explanation: "They answer different questions. A 95% confidence interval describes a procedure: if you repeated the experiment and computed intervals each time, 95% of them would contain the true parameter. It makes no probability claim about the specific interval in hand — the true θ either is or is not in it. A 95% credible interval makes a direct posterior probability claim: given the observed data and prior, there is 95% probability that θ lies in the interval. This is the statement practitioners usually want, but it requires a prior and cannot be made under frequentist assumptions."

- question: "In Bayesian inference, treating a parameter as a random variable allows you to make direct probability statements about it, such as 'there is a 72% probability that θ exceeds 0.5 given the data.'"
  type: true-false
  answer: true
  explanation: "This is one of the key practical advantages of the Bayesian framework. Because the posterior P(θ|data) is a full probability distribution over θ, you can compute the probability that θ falls in any region by integrating the posterior over that region. Under frequentist assumptions, θ is a fixed (if unknown) constant, so saying 'there is 72% probability that θ > 0.5' is not a valid statement — θ is either greater than 0.5 or it isn't. Bayesian inference enables exactly this kind of probabilistic statement, which is often what decision-makers need."

- question: "Why is the Bayesian approach philosophically distinct from the frequentist approach in how it treats unknown parameters, and what is the key practical consequence of this difference?"
  type: short-answer
  answer: "Bayesian inference treats parameters as random variables with probability distributions, reflecting uncertainty. Frequentist inference treats parameters as fixed but unknown constants. The key practical consequence is interpretability: Bayesian results in credible intervals that directly state the probability that a parameter lies in a range given the data, while frequentist confidence intervals describe a repeated-sampling procedure that does not make probability claims about specific intervals. Bayesian inference also allows prior knowledge to be incorporated formally."
  explanation: "The philosophical divide traces to the question of what 'probability' means. Frequentists define probability as long-run frequency — a property of repeated experiments. Bayesians define it as degree of belief — a property of an agent's state of knowledge. This difference has real consequences: frequentist methods cannot assign probabilities to one-time events or fixed parameters, while Bayesian methods can but must specify a prior. Neither framework is universally superior; the choice depends on the problem, available prior knowledge, and what question you want to answer."
```

## Explainer

You already know Bayes' theorem: P(A|B) = P(B|A)P(A)/P(B). Bayesian inference is the application of this rule to statistical learning — using it to update beliefs about unknown parameters as data arrives. The key conceptual shift is that in the Bayesian framework, unknown parameters are treated as **random variables** with probability distributions, not as fixed but unknown constants. This makes it possible to make direct probability statements about parameters, which frequentist inference cannot do.

The structure of Bayesian inference has three components. The **prior distribution** P(θ) encodes your beliefs about the parameter θ before seeing any data. It might be broad and uninformative if you know little, or informative if domain knowledge constrains the plausible values. The **likelihood** P(data|θ) tells you how probable the observed data would be if the parameter were θ — this is the same likelihood function you encounter in maximum likelihood estimation. Multiplying them and normalizing gives the **posterior distribution** P(θ|data) ∝ P(data|θ)P(θ), which encodes updated beliefs about θ after observing the data. The posterior is the complete answer to a Bayesian inference problem.

A concrete example makes this tangible. Suppose you want to estimate a coin's probability of heads, θ. Your prior might be a Beta(2, 2) distribution — slightly favoring θ near 0.5 but not strongly. You flip the coin 10 times and see 7 heads. The likelihood is Binomial: P(7 heads | θ) ∝ θ⁷(1−θ)³. The posterior is Beta(2+7, 2+3) = Beta(9, 5) — a distribution centered near 9/14 ≈ 0.64, updated from 0.5 toward the observed proportion but not entirely swamped by the data. You can read off a **credible interval**: the central 95% of the Beta(9,5) distribution gives an interval within which θ falls with 95% probability, given the data and prior.

The contrast with frequentist inference is philosophically significant. A frequentist 95% confidence interval means: if you repeated this procedure many times, 95% of the resulting intervals would contain the true θ. It says nothing about the probability that *this* interval contains θ. A Bayesian 95% **credible interval** directly says: given this data and prior, P(θ ∈ interval | data) = 0.95. This is typically what practitioners intuitively want to say. The cost is that Bayesian inference depends on the prior, and different priors lead to different posteriors. When data is plentiful, the likelihood dominates and the prior matters little. When data is sparse, prior specification is critical — which is why sensitivity analysis (checking whether conclusions change under different reasonable priors) is a standard part of applied Bayesian work.
