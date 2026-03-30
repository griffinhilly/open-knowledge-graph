---
id: algorithmic-information-theory
title: Algorithmic Information Theory
domain: computer-science
course: information-theory
prerequisites:
- id: kolmogorov-complexity
  type: hard
- id: shannon-entropy
  type: hard
tags:
- algorithmic information
- randomness
- incompressibility
- computability
- Chaitin
- Solomonoff
stage: expert
status: validated
---

# Algorithmic Information Theory

## Core Idea
Algorithmic information theory (AIT) studies information content through the lens of computation, building on Kolmogorov complexity to develop a complete theory of individual-sequence randomness, algorithmic probability, and the limits of mathematical reasoning. A string is algorithmically random if it is incompressible — no program significantly shorter than the string itself can produce it. Chaitin's constant Omega (the halting probability of a universal prefix-free Turing machine) is a real number that is algorithmically random, well-defined, but uncomputable. AIT provides the foundations for Solomonoff induction (a universal theory of prediction), the minimum description length principle in statistics, and connects to Godel's incompleteness theorems.

## Questions

```yaml
- question: "A string x of length n is called 'c-incompressible' if K(x) >= n - c. What fraction of n-bit strings are c-incompressible?"
  type: multiple-choice
  options:
    - "A negligible fraction — most strings have short descriptions"
    - "At least (1 - 2^(-c)) of all n-bit strings — by counting, there are fewer than 2^(n-c) programs shorter than n-c bits, so at most a fraction 2^(-c) of n-bit strings can be compressed by c or more bits"
    - "Exactly half of all strings"
    - "It depends on the choice of universal Turing machine"
  answer: 1
  explanation: "There are 2^n strings of length n but at most 2^0 + 2^1 + ... + 2^(n-c-1) < 2^(n-c) programs of length less than n-c. So at most 2^(n-c) strings can have K(x) < n-c, meaning at most a fraction 2^(-c) are compressible by c bits. The remaining fraction 1 - 2^(-c) are c-incompressible. For c = 10, over 99.9% of strings are incompressible. This is the counting argument: randomness (incompressibility) is the norm, not the exception."

- question: "Chaitin's halting probability Omega is a well-defined real number that can be approximated from below but never computed exactly."
  type: true-false
  answer: true
  explanation: "Omega = sum over halting programs p of 2^(-|p|) is perfectly well-defined — it is the probability that a prefix-free universal Turing machine halts on a random input. It can be approximated from below by running more programs and adding the contributions of those that halt. But it cannot be computed to arbitrary precision, because knowing the first n bits of Omega would solve the halting problem for all programs of length n. Omega is an example of a 'computably enumerable but not computable' real number — you can get closer from below but never know when you've converged."

- question: "Explain how Solomonoff induction uses Kolmogorov complexity to define a universal theory of prediction, and why it is uncomputable but theoretically important."
  type: short-answer
  answer: "Solomonoff induction assigns prior probability to a hypothesis (program) p proportional to 2^(-|p|) — shorter programs get higher prior weight. The predictive distribution for the next observation given past data is the mixture over all programs consistent with the data, weighted by this prior. This is 'universal' because it converges to the true distribution regardless of what the true data-generating process is (as long as it is computable). It is uncomputable because it requires summing over all programs and determining which ones are consistent with the data (equivalent to solving the halting problem). Despite uncomputability, Solomonoff induction provides the theoretical gold standard for prediction: any computable predictor can be shown to be at most a constant factor worse."
  explanation: "Solomonoff induction bridges Kolmogorov complexity and Bayesian inference. The 'universal prior' 2^(-K(x)) is the shortest-description analog of Occam's razor: simpler hypotheses get more weight. This directly inspires the practical minimum description length (MDL) principle in statistics, where model selection favors models that compress the data most effectively."
```

## Explainer

Shannon's information theory is fundamentally probabilistic: entropy, mutual information, and capacity all require a probability distribution. Algorithmic information theory takes a different approach: it measures information content through the lens of computability, asking how much computational work is needed to produce a given object. The central object is Kolmogorov complexity K(x), and AIT builds an entire theory around it.

The first major result is a **rigorous definition of randomness**. In Shannon's framework, "random" means "drawn from a distribution." But what makes an individual string random? AIT answers: x is algorithmically random if K(x) >= |x| - c, meaning no program significantly shorter than x can produce it. This captures the intuition that random strings have no patterns, no shortcuts, no compressibility. The counting argument shows that most strings are random in this sense — structure and compressibility are the exception.

The second major result is **algorithmic probability and Solomonoff induction**. The algorithmic probability of x is m(x) = sum over {p : U(p) = x} 2^(-|p|), the probability that a random program produces x. This is dominated by the shortest program, so m(x) ≈ 2^(-K(x)). Solomonoff showed that using m as a prior for prediction yields a universal prediction scheme that converges to the truth for any computable data source. This is the deepest formalization of Occam's razor: prefer the simplest (shortest-description) explanation, weighted by its complexity.

The third pillar connects AIT to the **foundations of mathematics**. Chaitin showed that for any formal system (like ZFC set theory), there exists a constant c such that the system cannot prove "K(x) > c" for any specific string x, even though most strings have K above any finite threshold. This is an information-theoretic version of Godel's incompleteness: a formal system with finite information content (its axioms) cannot establish facts about strings with more information content than the system itself. The halting probability Omega encodes the solution to every finite mathematical problem in its digits, yet no algorithm can compute those digits — it is a single real number containing infinite compressed information that is provably inaccessible.
