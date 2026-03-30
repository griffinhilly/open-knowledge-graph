---
id: streaming-algorithms
title: Streaming Algorithms
domain: computer-science
course: advanced-algorithms
prerequisites:
- id: universal-and-perfect-hashing
  type: hard
- id: randomized-algorithms
  type: hard
- id: bloom-filters
  type: soft
- id: expected-value-and-variance
  type: soft
tags:
- streaming
- count-min-sketch
- hyperloglog
- space-complexity
stage: expert
status: validated
---

# Streaming Algorithms

## Core Idea
Streaming algorithms process massive data sequences in a single pass (or few passes) using memory sublinear in the input size — typically O(polylog n) or O(1/epsilon^2) space. The count-min sketch estimates item frequencies using a 2D array of counters with d hash functions, providing frequency estimates with additive error epsilon * ||f||_1 using O((1/epsilon) * log(1/delta)) counters. HyperLogLog estimates the number of distinct elements (cardinality) using O(log log n) bits per register across O(1/epsilon^2) registers, achieving epsilon-relative error. The AMS (Alon-Matias-Szegedy) sketch estimates frequency moments F_k = sum(f_i^k). These algorithms share a common structure: hash-based projections compress the stream into a compact summary, and probabilistic analysis guarantees approximation quality.

## Questions

```yaml
- question: "A count-min sketch uses d = log(1/delta) hash functions and w = ceil(e/epsilon) counters per row. When querying frequency of item x, it returns the MINIMUM of d counter values. Why the minimum, not the average?"
  type: multiple-choice
  options:
    - "The minimum is faster to compute than the average"
    - "All d counters are unbiased estimators that can only OVERCOUNT (due to hash collisions adding to the count), so the minimum is closest to the true frequency — averaging would preserve the positive bias from collisions"
    - "The minimum provides a lower bound while the average provides an upper bound"
    - "The minimum uses less memory than storing all d values for averaging"
  answer: 1
  explanation: "Each counter tracks the true frequency of x PLUS the frequencies of all other items that hash to the same position — it can only overestimate, never underestimate. Each counter independently has expected overcount at most epsilon * ||f||_1. Taking the minimum of d independent overcounts reduces the probability that ALL d counters have large overcount. By the union bound, the probability that the minimum exceeds the true frequency by more than epsilon * ||f||_1 is at most (1 - 1/e)^d ≈ delta for d = log(1/delta). The minimum exploits the one-sided error structure; averaging would retain the bias."

- question: "HyperLogLog estimates the number of distinct elements in a stream. It works by hashing each element and tracking the maximum number of leading zeros observed. Explain why this works and why multiple registers are needed."
  type: short-answer
  answer: "If elements are hashed to uniformly random binary strings, the probability of seeing k leading zeros is 2^(-k-1). Among n distinct elements, the expected maximum number of leading zeros is approximately log_2(n). So the maximum leading-zero count is a rough estimator of log_2(n), giving a cardinality estimate of 2^(max_zeros). However, a single register has high variance — the estimate can be off by a constant factor. HyperLogLog uses m = 2^p registers, partitioning elements by their first p hash bits and tracking the max leading zeros in each partition. The harmonic mean of the per-register estimates reduces variance by a factor of sqrt(m), achieving standard error approximately 1.04/sqrt(m). With m = 1024 registers (~5 bits each ≈ 640 bytes), the standard error is about 3.25%."
  explanation: "The key insight is that a single max-leading-zeros register is an exponential-scale estimator with multiplicative noise. Averaging many independent such estimators (via stochastic averaging / partitioning) reduces the noise. The harmonic mean is used instead of the arithmetic mean because it handles the heavy-tailed distribution of 2^(max_zeros) better."

- question: "The Alon-Matias-Szegedy result showed that computing the second frequency moment F_2 exactly requires Omega(n) space in the streaming model, but it can be (1+epsilon)-approximated in O(1/epsilon^2 * log n) space."
  type: true-false
  answer: true
  explanation: "F_2 = sum(f_i^2) measures the 'skewness' of the frequency distribution. The AMS sketch maintains a counter that, for each stream element, adds or subtracts 1 based on a random 4-wise independent hash function. The square of this counter is an unbiased estimator of F_2. The variance is controlled by the 4-wise independence, and median-of-means reduces the failure probability. The O(1/epsilon^2 * log n) space bound is essentially optimal (up to log factors) by communication complexity lower bounds. This result launched the streaming algorithms field and won the Gödel Prize."

- question: "Count-min sketches are mergeable: the sketch of a combined stream equals the entry-wise sum of the individual sketches. This makes them suitable for distributed and parallel settings."
  type: true-false
  answer: true
  explanation: "If two streams S1 and S2 are summarized by count-min sketches CMS1 and CMS2 using the same hash functions, then CMS1 + CMS2 (entry-wise addition) is exactly the count-min sketch of the concatenated stream S1 || S2. This mergeability property means you can sketch data at distributed nodes, transmit the compact sketches to a central coordinator, sum them, and get the same result as if you had streamed all data through a single sketch. This property holds because the sketch is a linear function of the frequency vector — and linearity is what makes merging exact."
```

## Explainer

The streaming model captures a fundamental constraint of modern data processing: the data is too large to store, arrives too fast to revisit, and you have severely limited memory. A streaming algorithm sees each element once (or a small constant number of times) and must maintain a compact summary — a sketch — that supports approximate queries about the entire stream. The theoretical question is: which statistics can be approximated in sublinear space, and how much space is necessary and sufficient?

The count-min sketch is perhaps the most practical streaming data structure. It maintains a d-by-w array of counters, where each of d rows uses a different hash function mapping items to w = O(1/epsilon) positions. When item x arrives, increment the counter at position h_i(x) in each row. To estimate the frequency of x, return the minimum counter value across all d rows. Each counter overestimates (collisions only add), so the minimum is the tightest estimate. With d = O(log(1/delta)) rows, the estimate exceeds the true frequency by at most epsilon * N (total stream length) with probability at least 1 - delta. Total space: O((1/epsilon) * log(1/delta)) counters.

HyperLogLog solves the distinct-count problem: how many unique elements have appeared in the stream? It exploits a probabilistic observation: if you hash elements to uniform random binary strings, the maximum number of leading zeros among n distinct hashes is approximately log_2(n). A single register tracking this maximum gives a rough cardinality estimate, but with high variance. HyperLogLog partitions elements into m = 2^p buckets (by the first p bits of the hash) and maintains a separate max-leading-zeros register per bucket. The stochastic averaging across buckets reduces variance, and the harmonic mean provides a better estimator than the arithmetic mean. With m = 1024 registers of 5 bits each (about 640 bytes total), HyperLogLog achieves ~3% standard error — estimating cardinalities up to billions with sub-kilobyte memory.

The theoretical foundations of streaming connect to communication complexity. The space lower bound for exact F_2 computation follows from a reduction to the communication complexity of set disjointness. More broadly, streaming lower bounds typically reduce to two-party communication problems: if Alice holds the first half of the stream and Bob the second, the sketch that Alice passes to Bob is a message in a communication protocol, and known communication lower bounds translate to streaming space lower bounds. This connection provides tight lower bounds showing that the sketching algorithms above are essentially optimal.
