---
id: random-sampling-techniques
title: Random Sampling Techniques
domain: computer-science
course: advanced-algorithms
prerequisites:
- id: randomized-algorithms
  type: hard
- id: expected-value-and-variance
  type: hard
- id: probability-density-functions
  type: soft
tags:
- random-sampling
- reservoir-sampling
- importance-sampling
- randomized-algorithms
stage: expert
status: validated
---

# Random Sampling Techniques

## Core Idea
Random sampling is a foundational technique in algorithm design where selecting elements randomly from a dataset enables efficient estimation, selection, and optimization. Reservoir sampling solves the problem of uniformly sampling k items from a stream of unknown length in O(k) space. Importance sampling reweights samples to reduce variance when estimating expectations, enabling efficient simulation of rare events. Random sampling underpins randomized selection (expected O(n) median finding), random projections (Johnson-Lindenstrauss dimensionality reduction), and the design of sublinear-time algorithms that make decisions by examining only a small fraction of the input.

## Questions

```yaml
- question: "Reservoir sampling maintains a sample of size k from a stream. When the i-th element arrives (i > k), it replaces a random element in the reservoir with probability k/i. After n elements, each element is in the reservoir with probability exactly k/n. What makes this non-obvious?"
  type: multiple-choice
  options:
    - "The algorithm requires knowing n in advance to set the replacement probability"
    - "The probability that an element stays involves a telescoping product: it must survive all subsequent replacement attempts, and this product must equal k/n despite the algorithm never knowing n"
    - "The algorithm requires O(n) random bits to achieve uniform sampling"
    - "Each element's inclusion probability depends on the other elements in the stream"
  answer: 1
  explanation: "Element j (j <= k) starts in the reservoir and survives round i > k with probability 1 - (k/i)(1/k) = (i-1)/i. The probability it remains through all rounds is (k/(k+1)) * ((k+1)/(k+2)) * ... * ((n-1)/n) = k/n — a telescoping product. Element j (j > k) enters with probability k/j and then survives with the same telescoping product (j-1)/j * ... * (n-1)/n = (j-1)/(n-1) — wait, more carefully: enters with k/j, then survives each subsequent round i with (i-1)/i, giving k/j * j/(j+1) * ... * (n-1)/n = k/n. The algorithm achieves perfect uniformity without knowing n, which is the key insight."

- question: "In importance sampling, you draw samples from a proposal distribution q(x) instead of the target distribution p(x), and reweight by p(x)/q(x). This reweighting always produces an unbiased estimator of E_p[f(x)]."
  type: true-false
  answer: true
  explanation: "E_q[f(x) * p(x)/q(x)] = integral of f(x) * p(x)/q(x) * q(x) dx = integral of f(x) * p(x) dx = E_p[f(x)]. The reweighting exactly cancels the proposal distribution and recovers the target expectation. Unbiasedness holds for any proposal q that has support wherever p * f is nonzero. However, unbiasedness says nothing about variance — a poorly chosen q can produce astronomical variance. The optimal proposal distribution (minimizing variance) is q*(x) proportional to |f(x)| * p(x), which concentrates samples where the integrand is large."

- question: "Explain why random sampling enables sublinear-time algorithms and what fundamental tradeoff is involved."
  type: short-answer
  answer: "If a property holds for a large fraction of the input, a small random sample will contain evidence of that property with high probability. Specifically, to distinguish 'property holds everywhere' from 'property fails on epsilon-fraction of elements' with confidence 1-delta, you need only O(1/epsilon * log(1/delta)) samples — independent of input size n. This enables algorithms that run in time sublinear in n. The fundamental tradeoff is precision vs. speed: you can only make approximate statements (within epsilon of the truth) because you haven't seen most of the input. The sample size depends on the desired accuracy and confidence, not on n, which is why these algorithms achieve sublinear time."
  explanation: "This tradeoff is formalized in property testing: you are guaranteed either that the input has a property or is epsilon-far from having it, and must distinguish these cases using few samples. The connection between sampling and approximation is the theoretical foundation for all sublinear algorithms."

- question: "Reservoir sampling requires knowing the total stream length n in advance to set correct replacement probabilities."
  type: true-false
  answer: false
  explanation: "This is precisely the problem reservoir sampling solves. The replacement probability at step i is k/i — it depends only on the current position i, not the total length n. The algorithm processes elements one at a time and maintains uniform sampling at every prefix of the stream. When the stream ends at any point n, the reservoir contains a uniform random sample of size k from all n elements seen. This is what makes reservoir sampling suitable for streaming settings where n is unknown or effectively infinite."
```

## Explainer

Random sampling is one of the most versatile tools in the algorithm designer's toolkit. At its simplest, drawing a random subset of an input lets you estimate global properties without examining every element. But the techniques range from the elegant (reservoir sampling for streams) to the sophisticated (importance sampling for variance reduction), and the theoretical foundations connect to concentration inequalities, approximation theory, and information-theoretic limits.

Reservoir sampling addresses a clean problem: maintain a uniform random sample of k elements from a data stream whose length is unknown. The algorithm initializes the reservoir with the first k elements, then for each subsequent element i, includes it with probability k/i (replacing a random existing element). The proof of correctness is a beautiful telescoping argument: each element's survival probability across all future replacement rounds collapses to exactly k/n. The algorithm uses O(k) memory regardless of stream length, making it practical for massive data streams where you cannot store or revisit the data.

Importance sampling solves a different problem: efficiently estimating E_p[f(x)] when sampling from p is difficult or when naive sampling has high variance. Instead of drawing from p, you sample from a proposal distribution q and reweight each sample by p(x)/q(x). The estimator is unbiased for any q with adequate support, but the variance depends critically on how well q matches the shape of |f(x)| * p(x). The optimal proposal concentrates samples where the integrand is large, dramatically reducing the number of samples needed. This is essential in computational physics (rare event simulation), Bayesian inference (sampling from complex posteriors), and Monte Carlo integration.

The deeper significance of random sampling is that it enables sublinear-time computation. If you want to determine whether a property holds for most elements of a massive dataset, you do not need to examine every element — a random sample of size O(1/epsilon) suffices to distinguish "property holds everywhere" from "property fails on epsilon-fraction of elements," independent of the dataset size. This insight underlies property testing, streaming algorithms, and the entire field of sublinear algorithms. The price is approximation: you sacrifice exact answers for massive speed gains. But in an era of terabyte-scale data, an approximate answer in seconds often dominates an exact answer in hours.
