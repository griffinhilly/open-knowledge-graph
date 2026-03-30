---
id: fanos-inequality
title: "Fano's Inequality"
domain: computer-science
course: information-theory
prerequisites:
- id: joint-and-conditional-entropy
  type: hard
- id: mutual-information
  type: hard
builds-toward:
- channel-coding-theorem
tags:
- "Fano's inequality"
- error probability
- converse
- lower bound
stage: expert
status: validated
---

# Fano's Inequality

## Core Idea
Fano's inequality relates the probability of error in estimating a random variable X from an observation Y to the conditional entropy H(X|Y). Specifically, if X-hat = g(Y) is any estimator of X from Y with error probability P_e = Pr(X-hat != X), then H(X|Y) <= H(P_e) + P_e * log(|X| - 1), where H(P_e) is the binary entropy. Equivalently, low error probability implies low conditional entropy: if you can estimate X well from Y, then Y must carry a lot of information about X. Fano's inequality is the primary tool for proving converse (impossibility) results in information theory, including the converse of the channel coding theorem.

## Questions

```yaml
- question: "An estimator guesses a random variable X (which takes 8 values) from observation Y with error probability P_e = 0.01. What does Fano's inequality tell us about H(X|Y)?"
  type: multiple-choice
  options:
    - "H(X|Y) = 0, because the estimator is nearly perfect"
    - "H(X|Y) <= H(0.01) + 0.01 * log2(7) ≈ 0.081 + 0.028 = 0.109 bits — the conditional entropy must be small because the estimation is accurate"
    - "H(X|Y) <= 3 bits (the full entropy of a uniform 8-valued variable)"
    - "Fano's inequality cannot be applied when the error probability is below 0.5"
  answer: 1
  explanation: "Fano's inequality gives H(X|Y) <= H(P_e) + P_e * log2(|X|-1) = H(0.01) + 0.01 * log2(7) ≈ 0.081 + 0.028 = 0.109 bits. The small error probability forces H(X|Y) to be small — Y carries almost all the information about X. This is the inequality's power: low estimation error implies high information content, which constrains what communication rates are possible."

- question: "Fano's inequality provides a LOWER bound on the conditional entropy H(X|Y)."
  type: true-false
  answer: false
  explanation: "Fano's inequality provides an UPPER bound on H(X|Y): it says H(X|Y) is at most H(P_e) + P_e * log(|X|-1). However, its typical use is to derive a LOWER bound on error probability: rearranging, P_e >= (H(X|Y) - 1) / log(|X|-1). If H(X|Y) is large (Y carries little information about X), then P_e must be large. This makes it a tool for proving impossibility: high conditional entropy implies high error probability."

- question: "Explain how Fano's inequality is used to prove the converse of the channel coding theorem — that reliable communication above channel capacity is impossible."
  type: short-answer
  answer: "Consider transmitting one of 2^(nR) messages over n uses of a channel with capacity C. The message M is estimated as M-hat from the channel output Y^n. Fano's inequality gives H(M|Y^n) <= 1 + P_e * nR. Meanwhile, the data processing inequality and the capacity definition give I(M; Y^n) <= nC. Since I(M; Y^n) = H(M) - H(M|Y^n) = nR - H(M|Y^n), combining yields nR - 1 - P_e * nR <= nC. If R > C, then for large n, P_e must be bounded away from zero — the error probability cannot vanish. Therefore, reliable communication at rate R > C is impossible."
  explanation: "The converse proof chains together Fano's inequality (connecting error probability to conditional entropy), the definition of mutual information (connecting conditional entropy to information rate), and the channel capacity bound (capping mutual information per channel use). Each link is individually simple; their composition yields the profound result that capacity is a hard ceiling."
```

## Explainer

Fano's inequality connects two seemingly different quantities: the probability of making an error when estimating X from Y, and the conditional entropy H(X|Y). The intuition is straightforward: if Y contains a lot of information about X (H(X|Y) is small), then a good estimator should rarely be wrong (P_e is small). Fano's inequality makes this intuition precise and quantitative.

The inequality states: H(X|Y) <= H(P_e) + P_e * log(|X| - 1). The first term, H(P_e) = -P_e log P_e - (1-P_e) log(1-P_e), is the entropy of the error event itself — it is at most 1 bit and decreases as P_e approaches 0 or 1. The second term, P_e * log(|X|-1), accounts for the uncertainty about which of the |X|-1 wrong values X takes when an error occurs. Together, they bound how much residual uncertainty H(X|Y) can exist given error probability P_e.

The inequality is most powerful when inverted: rearranging, P_e >= (H(X|Y) - 1) / log(|X|-1). If Y carries little information about X — meaning H(X|Y) is close to its maximum H(X) — then the error probability must be large. This is a converse tool: it proves that accurate estimation is impossible when the mutual information I(X;Y) = H(X) - H(X|Y) is small relative to H(X).

The central application is proving that rates above channel capacity are unachievable. In this context, X = M (the message) and Y = Y^n (the channel output). Fano's inequality converts the assumption of low error probability into a constraint on H(M|Y^n), which in turn constrains the rate R through the mutual information chain. The resulting proof is clean and powerful: any attempt to communicate faster than capacity is mathematically guaranteed to produce non-vanishing errors. Fano's inequality appears throughout information theory wherever converse proofs are needed — in source coding, multi-user information theory, hypothesis testing, and statistical estimation.
