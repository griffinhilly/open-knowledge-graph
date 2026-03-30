---
id: randomized-algorithms
title: Randomized Algorithms
domain: computer-science
course: advanced-algorithms
prerequisites:
- id: big-o-complexity-analysis
  type: hard
- id: expected-value-and-variance
  type: hard
- id: quicksort
  type: soft
- id: complexity-class-p-definition
  type: soft
tags:
- randomized-algorithms
- probabilistic-analysis
- expected-time
- algorithm-design
stage: expert
status: validated
---

# Randomized Algorithms

## Core Idea
A randomized algorithm uses random coin flips as part of its logic, making its behavior (runtime, output, or both) a random variable rather than a deterministic quantity. Randomization often yields simpler, faster, or more elegant algorithms than the best known deterministic alternatives. Randomized quicksort achieves O(n log n) expected time with no adversarial worst case; randomized min-cut (Karger's algorithm) finds minimum cuts with high probability through simple edge contractions. The analysis of randomized algorithms relies on probability tools — linearity of expectation, tail bounds, and the probabilistic method — to provide rigorous guarantees despite the inherent unpredictability.

## Questions

```yaml
- question: "Randomized quicksort picks a pivot uniformly at random. Its expected number of comparisons on any input of size n is O(n log n). What probability technique most directly yields this result?"
  type: multiple-choice
  options:
    - "Union bound over all possible pivot sequences"
    - "Linearity of expectation — define indicator variables for each pair of elements being compared, then sum their expectations"
    - "Markov's inequality applied to the total comparison count"
    - "Chernoff bounds on the depth of the recursion tree"
  answer: 1
  explanation: "For each pair (i, j) of elements in sorted order, define X_ij = 1 if element i is ever compared to element j. The total comparisons = sum of all X_ij. By linearity of expectation, E[total] = sum of E[X_ij] = sum of Pr[i compared to j]. Two elements are compared exactly when one of them is the first pivot chosen from the range [i..j], giving Pr = 2/(j-i+1). Summing this over all pairs yields O(n log n) via the harmonic series. The beauty is that linearity of expectation requires no independence — the indicator variables can be arbitrarily correlated."

- question: "A randomized algorithm always produces the correct answer but its running time is a random variable. This describes a Las Vegas algorithm."
  type: true-false
  answer: true
  explanation: "Las Vegas algorithms guarantee correctness but have random running time. Randomized quicksort is the canonical example: it always sorts correctly, but the number of comparisons depends on the random pivot choices. The complementary class — Monte Carlo algorithms — have deterministic running time but may produce incorrect results with bounded probability. This Las Vegas / Monte Carlo distinction is fundamental to the classification of randomized algorithms."

- question: "Every Las Vegas algorithm can be converted to a Monte Carlo algorithm with the same expected resource usage."
  type: true-false
  answer: true
  explanation: "Run the Las Vegas algorithm for a fixed time budget (e.g., twice its expected running time). If it finishes, output the (guaranteed correct) result. If not, output an arbitrary answer or 'fail.' By Markov's inequality, the probability of not finishing within 2E[T] time is at most 1/2. This gives a Monte Carlo algorithm with deterministic time bound 2E[T] and error probability at most 1/2. The reverse conversion — Monte Carlo to Las Vegas — is not always possible without additional structure (you need a way to verify correctness)."

- question: "Karger's randomized min-cut algorithm contracts a randomly chosen edge at each step until two vertices remain. Why does repeating the algorithm O(n^2 log n) times and taking the minimum cut found yield the true minimum cut with high probability?"
  type: short-answer
  answer: "A single run of Karger's algorithm preserves a specific minimum cut with probability at least 2/n(n-1) = Omega(1/n^2), because at each contraction step the probability of not cutting a min-cut edge is at least (n-i-2)/(n-i), and the product telescopes to 2/n(n-1). The probability that a single run FAILS to find a specific min-cut is therefore at most 1 - 2/n(n-1). Running O(n^2 log n) independent trials, the probability that ALL trials miss the min-cut is at most (1 - 2/n(n-1))^(cn^2 ln n) <= e^(-2c ln n) = n^(-2c), which is polynomially small. Taking the minimum over all trials gives the true min-cut with high probability."
  explanation: "This is a foundational example of probability amplification: a weak success probability (1/n^2) becomes overwhelming certainty through independent repetition. The key insight is that even a crude per-trial success probability, when amplified by O(n^2 log n) repetitions, drives the failure probability below any desired polynomial threshold."
```

## Explainer

You already understand deterministic algorithm analysis — given an input, the algorithm follows a fixed sequence of steps and you analyze the worst case. Randomized algorithms break this model by introducing coin flips into the algorithm's logic. The algorithm's behavior on a fixed input becomes a random variable, and the analysis shifts from worst-case determinism to probabilistic guarantees. This is not the same as average-case analysis over random inputs: the randomness is internal to the algorithm, and the guarantees hold for every input.

The power of randomization is surprising. Randomized quicksort achieves O(n log n) expected time on every input — no adversary can force quadratic behavior because the adversary cannot predict the random pivot choices. The analysis uses linearity of expectation: define indicator random variables X_ij for whether elements i and j are compared, compute Pr[X_ij = 1] = 2/(j-i+1) from the observation that i and j are compared exactly when one of them is the first pivot chosen from the range between them, then sum over all pairs to get the harmonic series. No independence assumptions are needed because linearity of expectation holds unconditionally.

Karger's min-cut algorithm illustrates a different flavor of randomization. The algorithm repeatedly contracts a uniformly random edge until only two vertices remain, and the edges between them form a candidate cut. A single run finds a specific minimum cut with probability at least 2/n(n-1), which seems terrible — but repeating O(n^2 log n) times and keeping the best cut drives the failure probability to inverse polynomial. This technique of probability amplification through independent repetition is a recurring theme: weak probabilistic guarantees become strong ones through repetition, as long as verification is cheap.

The theoretical foundation for analyzing randomized algorithms draws on tools you know from probability — linearity of expectation, Markov's and Chebyshev's inequalities, Chernoff bounds — and applies them in algorithmic contexts. Tail bounds are particularly important: they tell you not just the expected behavior but how tightly concentrated the actual behavior is around the expectation. An algorithm with O(n log n) expected time is less useful if the variance is huge, but Chernoff bounds often show that the running time is sharply concentrated, deviating from the expectation with only exponentially small probability. This combination of simplicity, efficiency, and provable concentration makes randomized algorithms indispensable in modern algorithm design.
