---
id: mutual-information
title: Mutual Information
domain: computer-science
course: information-theory
prerequisites:
- id: shannon-entropy
  type: hard
- id: joint-and-conditional-entropy
  type: hard
builds-toward:
- kl-divergence
- channel-capacity
- fanos-inequality
tags:
- mutual information
- dependence
- information
- symmetric
stage: advanced
status: validated
---

# Mutual Information

## Core Idea
Mutual information I(X;Y) = H(X) - H(X|Y) = H(Y) - H(Y|X) = H(X) + H(Y) - H(X,Y) measures the amount of information that one random variable provides about another. Unlike correlation, which only captures linear relationships, mutual information detects any statistical dependence. It is symmetric: X tells you as much about Y as Y tells you about X. I(X;Y) = 0 if and only if X and Y are independent. It is always non-negative and is bounded above by min(H(X), H(Y)). Mutual information is the central quantity in channel capacity, feature selection, and information-theoretic analysis of learning.

## Questions

```yaml
- question: "A machine learning engineer uses mutual information to select features for a classifier. Why might mutual information be preferred over Pearson correlation for feature selection?"
  type: multiple-choice
  options:
    - "Mutual information is faster to compute than correlation"
    - "Mutual information detects any statistical dependence (including nonlinear), while Pearson correlation only measures linear association"
    - "Mutual information accounts for the causal direction between features and the target"
    - "Pearson correlation is undefined for discrete variables"
  answer: 1
  explanation: "Pearson correlation measures only linear association — if Y = X^2 and X is symmetric around zero, the correlation is zero despite perfect functional dependence. Mutual information captures ALL dependence: linear, nonlinear, categorical, or otherwise. I(X;Y) = 0 if and only if X and Y are truly independent. This makes it a more general measure for feature selection, though it requires density estimation for continuous variables, which adds computational cost."

- question: "I(X;Y) = H(X) + H(Y) - H(X,Y). If X and Y are independent, I(X;Y) = 0. If Y is a deterministic function of X, what is I(X;Y)?"
  type: multiple-choice
  options:
    - "I(X;Y) = 0 because deterministic relationships contain no randomness"
    - "I(X;Y) = H(X) + H(Y)"
    - "I(X;Y) = H(Y), because knowing X completely determines Y, so H(Y|X) = 0"
    - "I(X;Y) = infinity because the dependence is perfect"
  answer: 2
  explanation: "If Y = f(X) for some deterministic function f, then H(Y|X) = 0 — there is no residual uncertainty about Y once X is known. So I(X;Y) = H(Y) - H(Y|X) = H(Y) - 0 = H(Y). Equivalently, I(X;Y) = H(X) - H(X|Y), and if f is invertible, then H(X|Y) = 0 as well, giving I(X;Y) = H(X) = H(Y). If f is not invertible (many-to-one), then H(X|Y) > 0 and I(X;Y) = H(Y) < H(X)."

- question: "Mutual information is symmetric: I(X;Y) = I(Y;X). This means that if knowing X reduces your uncertainty about Y by 2 bits, then knowing Y also reduces your uncertainty about X by 2 bits."
  type: true-false
  answer: true
  explanation: "Symmetry is a fundamental property: I(X;Y) = H(X) - H(X|Y) = H(Y) - H(Y|X) = I(Y;X). The total information shared between X and Y is the same regardless of which direction you look. This is true even though H(X|Y) != H(Y|X) in general — the asymmetry in conditional entropies cancels exactly. Intuitively, mutual information measures the overlap in information content between the two variables, and overlap is inherently symmetric."

- question: "Explain the Venn diagram interpretation of mutual information and how it relates H(X), H(Y), H(X,Y), H(X|Y), and H(Y|X)."
  type: short-answer
  answer: "Imagine two overlapping circles, one for H(X) and one for H(Y). The union is H(X,Y). The overlap (intersection) is I(X;Y) — the shared information. The left crescent (H(X) minus the overlap) is H(X|Y) — the information in X that Y does not capture. The right crescent is H(Y|X). The chain rule gives H(X,Y) = H(X|Y) + I(X;Y) + H(Y|X) = H(X) + H(Y|X) = H(Y) + H(X|Y). For independent variables the circles don't overlap (I=0, H(X,Y)=H(X)+H(Y)). For perfectly dependent variables the circles coincide (I=H(X)=H(Y), H(X|Y)=H(Y|X)=0)."
  explanation: "This Venn diagram is one of the most useful mental models in information theory. It breaks down perfectly for two variables but becomes tricky for three or more, where interaction information (the analog of the intersection of three sets) can be negative — meaning three-way redundancy can be negative, unlike set intersections."
```

## Explainer

You know that conditional entropy H(Y|X) measures the uncertainty remaining in Y after learning X, and that this is always at most H(Y). The gap — the amount by which knowing X reduces uncertainty about Y — is **mutual information**: I(X;Y) = H(Y) - H(Y|X). It measures how much information X and Y share.

Mutual information has several equivalent expressions, each offering a different perspective. I(X;Y) = H(X) - H(X|Y) shows how much Y tells you about X. I(X;Y) = H(X) + H(Y) - H(X,Y) shows the "redundancy" between X and Y — how much the sum of individual uncertainties exceeds the joint uncertainty. And I(X;Y) = sum over (x,y) of p(x,y) log(p(x,y) / (p(x)p(y))), which is the KL divergence between the joint distribution and the product of marginals. This last form makes the connection to KL divergence explicit and shows that mutual information measures how far X and Y are from independence.

The key properties make mutual information exceptionally useful. It is non-negative (I(X;Y) >= 0), symmetric (I(X;Y) = I(Y;X)), and zero if and only if X and Y are independent. Unlike correlation, it captures any form of dependence — if there is ANY statistical relationship between X and Y, mutual information will detect it. This generality makes it the gold standard for measuring associations in information theory, machine learning (feature selection, information bottleneck), neuroscience (neural coding), and statistics.

In the context of communication, mutual information plays a starring role. Shannon's channel coding theorem states that the capacity of a noisy channel — the maximum rate at which information can be reliably transmitted — equals the maximum mutual information between the input and output: C = max I(X;Y) over all input distributions. This gives mutual information its operational meaning: it is the amount of useful information that survives the noise. The Venn diagram picture (H(X) and H(Y) as overlapping circles, with I(X;Y) as the overlap) provides a powerful visual intuition that extends to understanding conditional mutual information and the data processing inequality.
