---
id: independence-of-sigma-algebras
title: Independence of Sigma-Algebras
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: conditional-expectation
  type: hard
- id: independence-and-multiplication-rule
  type: soft
builds-toward:
- weak-law-of-large-numbers
- strong-law-of-large-numbers
tags:
- independence
- sigma-algebras
- events
stage: advanced
status: validated
---

# Independence of Sigma-Algebras

## Core Idea
Sigma-algebras ℊ and ℋ are independent if P(A ∩ B) = P(A)P(B) for all A ∈ ℊ, B ∈ ℋ. Random variables X and Y are independent if their generated sigma-algebras are independent. This definition applies equally to discrete, continuous, and singular distributions.

## Questions

```yaml
- question: "Random variables X and Y satisfy E[f(X) | σ(Y)] = E[f(X)] for every bounded measurable function f. What can you conclude?"
  type: multiple-choice
  options:
    - "X and Y have the same distribution"
    - "X and Y are uncorrelated but may not be independent"
    - "X and Y are independent"
    - "The sigma-algebras σ(X) and σ(Y) overlap but their events are uncorrelated"
  answer: 2
  explanation: "This is the measure-theoretic characterization of independence: X and Y are independent if and only if conditioning on σ(Y) does not change the expectation of any function of X. This links independence to information: 'σ(Y) gives no information about X.' Option B (uncorrelated) is strictly weaker — uncorrelated variables can still be dependent (e.g., X uniform on [-1,1] and Y = X²)."

- question: "A researcher wants to define independence for a mixed pair (X continuous, Y discrete). Which approach works without case-splitting?"
  type: multiple-choice
  options:
    - "Require the joint CDF to factor: F_{X,Y}(x,y) = F_X(x)F_Y(y)"
    - "Require the joint PDF to factor, treating Y's distribution as a limiting case"
    - "Require P(A ∩ B) = P(A)P(B) for all A ∈ σ(X), B ∈ σ(Y)"
    - "Require E[XY] = E[X]E[Y], which is necessary and sufficient for all distribution types"
  answer: 2
  explanation: "The sigma-algebra definition P(A ∩ B) = P(A)P(B) for all measurable events A ∈ σ(X), B ∈ σ(Y) works universally — for discrete, continuous, singular, and mixed types — because it makes no assumptions about the form of the distribution. Option A covers only CDF-level events, not all sigma-algebra events. Option D (E[XY] = E[X]E[Y]) is merely uncorrelation, which is necessary but not sufficient for independence."

- question: "If σ(X) and σ(Y) are independent sigma-algebras, then knowing any event about Y gives no probabilistic information about any event about X."
  type: true-false
  answer: true
  explanation: "This is the informational meaning of sigma-algebra independence. The formal condition P(A ∩ B) = P(A)P(B) for all A ∈ σ(X), B ∈ σ(Y) means conditional on any event in σ(Y), the probability of any event in σ(X) is unchanged. Equivalently, E[1_A | σ(Y)] = P(A) for all A ∈ σ(X) — no observation about Y updates probabilities of events about X."

- question: "Two random variables X and Y are independent if and mainly if their joint probability distribution factors as the product of their marginals, regardless of distribution type."
  type: true-false
  answer: false
  explanation: "This factoring statement is correct for continuous (joint PDF = product of marginals) and discrete (joint PMF = product of marginals) distributions, but 'joint distribution factors' has no clean formulation for singular or mixed-type distributions without the sigma-algebra framework. The sigma-algebra definition P(A ∩ B) = P(A)P(B) for all A ∈ σ(X), B ∈ σ(Y) is universally correct; the density-factoring approach only works in specific cases."

- question: "Why is the sigma-algebra definition of independence more powerful than simply requiring P(A ∩ B) = P(A)P(B) for two specific events A and B?"
  type: short-answer
  answer: "The elementary definition covers only two specific events, while sigma-algebra independence requires the product rule to hold for *all* pairs of events drawn from both sigma-algebras. A sigma-algebra σ(X) contains every observable event about X — {X > 3}, {X ∈ [1,2]}, any Borel event. Independence of σ(X) and σ(Y) means no question about Y helps predict any question about X. Two variables can have some independent event pairs while being statistically dependent overall."
  explanation: "Pairwise independence of specific events is strictly weaker than sigma-algebra independence. The sigma-algebra definition also works across all distribution types and connects directly to conditional expectation: independence is equivalent to E[f(X)|σ(Y)] = E[f(X)], which is the right framing for the law of large numbers and martingale theory."
```

## Explainer

You learned in an earlier course that two events A and B are independent when knowing one occurs gives no information about the other — formally, P(A ∩ B) = P(A)P(B). From your study of conditional expectation, you now have a richer language: E[X | ℱ] is the best prediction of X given all information in the sigma-algebra ℱ. Independence of sigma-algebras is the natural generalization that lets you say "the information in ℊ gives no information about events in ℋ."

A **sigma-algebra** generated by a random variable X, written σ(X), is the collection of all events of the form {X ∈ B} for Borel sets B. It captures everything you could observe about X: any question you can ask about X (is X > 3? is X in [1, 2]? is X rational?) corresponds to some event in σ(X). Two random variables X and Y are independent when σ(X) and σ(Y) are independent sigma-algebras — meaning P({X ∈ A} ∩ {Y ∈ B}) = P(X ∈ A) · P(Y ∈ B) for all Borel sets A and B. This is a single definition that unifies independence for discrete, continuous, and mixed distributions without needing separate cases.

Why does the measure-theoretic definition matter? Consider the alternative — defining independence by joint PMFs or joint PDFs. For discrete random variables you write P(X = x, Y = y) = P(X = x)P(Y = y); for continuous ones you require f_{X,Y}(x,y) = f_X(x)f_Y(y). These case-by-case definitions work in their domains but break down for singular distributions or mixed types. The sigma-algebra definition is universal: it requires the product rule P(A ∩ B) = P(A)P(B) to hold for all observable events in both sigma-algebras, regardless of whether those events are described by mass functions, density functions, or neither.

The connection to conditional expectation is particularly clean: X and Y are independent if and only if E[f(X) | σ(Y)] = E[f(X)] for all measurable f — that is, knowing Y does not change your expectation of any function of X. This equivalence links independence to information, which is the right conceptual framing for probability theory. It also sets up the law of large numbers: when X₁, X₂, … are independent, their sigma-algebras carry no mutual information, and this is what allows the sample average to converge to the true mean with probability 1.
