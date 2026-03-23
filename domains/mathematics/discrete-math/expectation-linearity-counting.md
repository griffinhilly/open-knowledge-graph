---
id: expectation-linearity-counting
title: Linearity of Expectation in Counting
domain: mathematics
course: discrete-math
prerequisites:
- id: expected-value
  type: hard
- id: counting-principles
  type: soft
builds-toward:
- probabilistic-method-counting
tags:
- probability
- counting
- expectation
stage: formal-systems
status: validated
---

# Linearity of Expectation in Counting

## Core Idea
Linearity of expectation states that E[X₁ + X₂ + ... + Xₙ] = E[X₁] + E[X₂] + ... + E[Xₙ], even when variables are dependent. This powerful tool in combinatorics simplifies counting problems by breaking them into indicator random variables and computing expected values.

## Questions

```yaml
- question: "A student wants to find the expected number of students in a class of 30 who share a birthday with at least one classmate. She reasons: 'I can't use linearity of expectation because whether any two students share a birthday depends on all the other birthdays — the indicator variables are not independent.' Is she correct?"
  type: multiple-choice
  options:
    - "Yes — linearity of expectation requires independence, so this approach would give incorrect results"
    - "No — linearity of expectation holds even when the random variables being summed are dependent"
    - "Partially — you can use linearity only after conditioning on the most likely birthday"
    - "Yes — you must first compute the full joint distribution before applying linearity"
  answer: 1
  explanation: "The student's reasoning applies to variance (where Var(X+Y) = Var(X)+Var(Y) only when X and Y are independent), not to expectation. Linearity of expectation is unconditional: E[X₁+X₂+...+Xₙ] = E[X₁]+E[X₂]+...+E[Xₙ] always holds, regardless of dependence. This is the key distinction — and the source of linearity's power in combinatorics."

- question: "You want to find the expected number of edges in a random subgraph where each of m edges is independently included with probability p. Which approach correctly uses linearity of expectation?"
  type: multiple-choice
  options:
    - "Sum p^k · (1-p)^(m-k) · C(m,k) · k over all k from 0 to m"
    - "Define Xₑ = 1 if edge e is included, then E[total edges] = Σₑ E[Xₑ] = m·p"
    - "Use linearity only after verifying that the edge indicators are independent of each other"
    - "Compute the variance first to check whether dependence is small enough to ignore"
  answer: 1
  explanation: "Option A is the direct computation via the binomial distribution — valid but unnecessarily complex. Option B applies linearity correctly: define one indicator variable per edge, note each has expectation p, sum by linearity to get m·p immediately. Crucially, option C is wrong — linearity does not require independence. In this particular problem the edges are independent, but that fact is irrelevant to whether linearity applies; it applies either way."

- question: "For any random variable X that can be written as a sum of indicator random variables, E[X] equals the sum of the probabilities of each indicator event, regardless of whether those events are independent."
  type: true-false
  answer: true
  explanation: "This is the direct application of linearity of expectation: E[Xᵢ] = P(event i occurs) = pᵢ for an indicator variable, so E[ΣXᵢ] = Σpᵢ by linearity. No independence assumption is needed anywhere in this chain. This is exactly why the technique is so powerful — you reduce a hard counting problem to summing easy individual probabilities, even when those events are correlated."

- question: "Because variance has the property Var(X+Y) = Var(X) + Var(Y) only when X and Y are independent, the same independence restriction applies to the linearity of expectation."
  type: true-false
  answer: false
  explanation: "This is the critical distinction. Variance's additivity requires independence; expectation's additivity does not. Linearity of expectation follows from the definition of expectation as a weighted sum (or integral), which is linear as a mathematical operation — unconditionally. Confusing these two properties is the most common misconception about linearity of expectation. Remembering that 'expectation is linear, variance is not (without independence)' is essential."

- question: "Explain why linearity of expectation is more powerful than it initially seems. Specifically: what makes it different from the corresponding property of variance, and why does this difference matter for counting problems?"
  type: short-answer
  answer: "Linearity of expectation holds even for dependent random variables — E[X+Y] = E[X]+E[Y] always. The analogous property for variance (Var(X+Y) = Var(X)+Var(Y)) requires independence. This matters for counting because indicator variables in combinatorial problems are almost always dependent (e.g., whether element i is a fixed point depends on where all other elements map). If linearity required independence, we could rarely use it. Because it doesn't, we can always decompose a complex count into many simple indicator probabilities and sum them — even when those indicators are tangled together in complicated ways."
  explanation: "The fixed-point example illustrates this perfectly: in a random permutation of n elements, the expected number of fixed points is 1 for all n. The indicator variables Xᵢ (is element i a fixed point?) are dependent — knowing that element 1 is fixed tells you something about whether element 2 is fixed. But E[total fixed points] = n·(1/n) = 1 via linearity regardless. Trying to compute this by summing over all n! permutations would be far more work."
```

## Explainer

You already know from your prerequisite that **expected value** is the probability-weighted average of a random variable's possible outcomes. Linearity of expectation says something deceptively simple: the expected value of a sum is always the sum of the expected values — even when the summands are *not* independent. This "even when dependent" clause is what makes it a power tool rather than just a tautology.

The key technique is **indicator random variables**. For any event A, define the indicator Iₐ as 1 if A occurs and 0 otherwise. Then E[Iₐ] = P(A), which is often straightforward to compute. Now suppose you want the expected number of times some thing happens in a complex random process — say, the expected number of fixed points in a random permutation (elements that map to themselves). Direct computation via the full probability distribution is painful. Instead: let Xᵢ = 1 if element i is a fixed point. Then the total number of fixed points is X = X₁ + X₂ + ⋯ + Xₙ, and by linearity E[X] = E[X₁] + ⋯ + E[Xₙ]. Each E[Xᵢ] = P(element i is fixed) = 1/n. So E[X] = n · (1/n) = 1 — regardless of n, a random permutation has on average exactly one fixed point.

The reason linearity holds even for dependent variables comes down to the definition of expectation as an integral (or sum) — linearity of integration is unconditional. This is the key contrast with variance: Var(X + Y) = Var(X) + Var(Y) only when X and Y are independent. Expectation's linearity is genuinely unconditional.

A counting application: you want to know the expected number of edges in a random subgraph where each edge is included independently with probability p. Without linearity, you'd need to sum over all possible subgraphs — combinatorially intractable. With linearity, let Xₑ be the indicator for each edge e. Then E[total edges] = Σₑ E[Xₑ] = Σₑ p = p·|E|. The answer is immediate. The general pattern is always: identify the quantity as a sum of indicators, compute each indicator's expectation separately, then add them up. This technique, combined with your knowledge of counting principles for enumerating the indicators, converts hard combinatorial problems into collections of easy probability calculations.
