---
id: las-vegas-vs-monte-carlo
title: Las Vegas vs Monte Carlo Algorithms
domain: computer-science
course: advanced-algorithms
prerequisites:
- id: randomized-algorithms
  type: hard
- id: expected-value-and-variance
  type: hard
- id: bpp-complexity-class
  type: soft
tags:
- las-vegas
- monte-carlo
- randomized-algorithms
- error-probability
stage: expert
status: validated
---

# Las Vegas vs Monte Carlo Algorithms

## Core Idea
Randomized algorithms split into two fundamental classes based on where the randomness manifests. Las Vegas algorithms always produce the correct answer but have random running time — randomized quicksort always sorts correctly, but the number of comparisons varies. Monte Carlo algorithms run in deterministic (or bounded) time but may produce incorrect results with bounded probability — the Miller-Rabin primality test runs in fixed polynomial time but has a small false-positive probability. The distinction matters for complexity theory (ZPP vs BPP/RP) and for practice: Las Vegas algorithms compose trivially (correctness is guaranteed) while Monte Carlo algorithms require careful error management when chained together.

## Questions

```yaml
- question: "A Monte Carlo algorithm for a decision problem has one-sided error: it never says 'yes' incorrectly but says 'no' incorrectly with probability at most 1/3. After running the algorithm k independent times on the same input, what is the best strategy and resulting error probability?"
  type: multiple-choice
  options:
    - "Take a majority vote; error drops to (1/3)^k"
    - "If ANY run says 'yes,' output 'yes'; otherwise output 'no' — error drops to (1/3)^k for true-yes instances"
    - "Average the outputs; error drops to 1/(3k)"
    - "Run once — repetition cannot help with one-sided error"
  answer: 1
  explanation: "With one-sided error on the 'no' side, a 'yes' output is always correct. For a true-yes instance, each run independently has probability at most 1/3 of incorrectly saying 'no.' If we output 'yes' whenever any run says 'yes,' the only way we err is if ALL k runs say 'no' on a true-yes instance, which happens with probability at most (1/3)^k. This is exponential amplification with k trials. Majority vote works for two-sided error (BPP), but for one-sided error (RP), the 'accept if any run accepts' strategy is optimal."

- question: "Every Las Vegas algorithm can be converted to a Monte Carlo algorithm, but the reverse is not always true."
  type: true-false
  answer: true
  explanation: "Las Vegas to Monte Carlo is straightforward: run for a time budget, output 'don't know' or a wrong answer if it doesn't finish. Monte Carlo to Las Vegas requires being able to VERIFY the answer efficiently. For decision problems in RP (one-sided Monte Carlo), you can verify 'yes' answers are correct but not 'no' answers, so conversion to Las Vegas is possible only if you can also verify 'no' (which puts you in ZPP = RP ∩ coRP). In general, without efficient verification, Monte Carlo algorithms cannot be made Las Vegas."

- question: "The complexity class ZPP (Zero-error Probabilistic Polynomial time) equals RP ∩ coRP. This means ZPP algorithms are exactly Las Vegas polynomial-time algorithms."
  type: true-false
  answer: true
  explanation: "ZPP is defined as the class of problems solvable by Las Vegas algorithms with expected polynomial running time. The equivalence ZPP = RP ∩ coRP follows from a clean construction: if a problem is in both RP and coRP, you have a Monte Carlo algorithm with one-sided error for 'yes' (RP) and another with one-sided error for 'no' (coRP). Run both alternately; at least one gives a definitive answer each round. The expected number of rounds to get a definitive answer is constant, yielding a Las Vegas algorithm. Conversely, any ZPP algorithm can be truncated to give RP and coRP algorithms."

- question: "Explain the practical implications of the Las Vegas vs Monte Carlo distinction when composing randomized subroutines inside larger algorithms."
  type: short-answer
  answer: "Las Vegas subroutines compose trivially because each call produces a guaranteed-correct result regardless of running time variability. Monte Carlo subroutines are more delicate: if an algorithm makes m calls to a Monte Carlo subroutine with error probability epsilon each, the overall error probability can be as high as m*epsilon by a union bound. To keep overall error below delta, each subroutine call needs error at most delta/m, which requires O(log(m/delta)) repetitions per call. This amplification cost multiplies with the number of calls, making Monte Carlo composition more expensive. In practice, this means algorithms that call randomized subroutines many times (e.g., in loops) strongly prefer Las Vegas subroutines when available."
  explanation: "The union bound composition cost is why BPP (two-sided Monte Carlo) algorithms can still be composed polynomially — logarithmic amplification is cheap. But it explains why Las Vegas algorithms are preferred when available: zero error composes without any overhead."
```

## Explainer

From your study of randomized algorithms, you understand that coin flips can improve algorithmic performance. The Las Vegas / Monte Carlo classification sharpens this into a precise tradeoff between two desirable properties: guaranteed correctness and guaranteed running time. Every randomized algorithm sacrifices one of these — you cannot have both with nontrivial randomization (or you would have a deterministic algorithm).

Las Vegas algorithms sacrifice predictable running time for guaranteed correctness. Randomized quicksort always produces a correctly sorted array, but the number of comparisons is a random variable with expectation O(n log n). The worst-case time is still O(n^2) — it is just exponentially unlikely. Randomized algorithms for finding medians, hashing, and computational geometry often fall in this class. The complexity class ZPP captures Las Vegas polynomial-time computation: problems solvable with zero error and expected polynomial running time.

Monte Carlo algorithms sacrifice guaranteed correctness for predictable running time. The Miller-Rabin primality test runs in fixed polynomial time but may declare a composite number prime with probability at most 1/4 per trial. Repeating k times drives the error to (1/4)^k — for k = 40, the error probability is below 2^(-80), far smaller than hardware failure rates. The complexity classes RP (one-sided error) and BPP (two-sided error) capture different flavors of Monte Carlo computation. A crucial subtlety: one-sided error is more powerful for amplification because you know which direction might be wrong.

The distinction becomes operationally important when randomized subroutines are composed. A Las Vegas call inside a loop contributes variable running time but no error accumulation — you can call it a million times and the output is still correct. A Monte Carlo call inside a loop accumulates error: m calls each with error epsilon give overall error up to m * epsilon by the union bound. Managing this requires amplifying each call's success probability, which costs O(log(m)) factor per call. This compositional difference is why Las Vegas algorithms are preferred when available, and why the question of whether RP = ZPP (can every one-sided Monte Carlo algorithm be made Las Vegas?) remains a fundamental open question in complexity theory.
