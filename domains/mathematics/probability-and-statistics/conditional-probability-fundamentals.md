---
id: conditional-probability-fundamentals
title: Conditional Probability Fundamentals
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: probability-axioms-and-rules
  type: hard
builds-toward:
- bayes-theorem
- independence-of-events
tags:
- conditional
- probability
stage: formal-systems
status: draft
---

# Conditional Probability Fundamentals

## Core Idea
Conditional probability P(A|B)=P(A∩B)/P(B) measures the probability of A given that B has occurred. The law of total probability states P(A)=∑P(A|B_i)P(B_i) over a partition {B_i}. Conditional probability formalizes how information updates our beliefs.

## Questions

```yaml
- question: "A box contains 4 red and 6 blue marbles. You draw one marble. Given that it is not blue, what is P(red | not blue)?"
  type: multiple-choice
  options:
    - "4/10 — there are 4 red marbles out of 10 total"
    - "4/6 — you divide by the probability of blue"
    - "1 — conditioning on 'not blue' restricts the sample space entirely to red marbles"
    - "1/2 — there are two colors, so equal probability once blue is ruled out"
  answer: 2
  explanation: "P(red | not blue) = P(red ∩ not blue) / P(not blue). Since the only non-blue marbles are red, P(red ∩ not blue) = P(red) = 4/10, and P(not blue) = 4/10. The ratio is 1. Conditioning on 'not blue' restricts the sample space to the 4 red marbles — within that restricted space, all outcomes are red, so the probability is 1. This illustrates how conditioning redefines 'all possible outcomes.'"

- question: "A factory has two machines. Machine A produces 70% of items with a 3% defect rate. Machine B produces 30% with an 8% defect rate. What is the overall probability that a randomly selected item is defective?"
  type: multiple-choice
  options:
    - "5.5% — the simple average of 3% and 8%"
    - "4.5% — the law of total probability: (0.03)(0.70) + (0.08)(0.30)"
    - "11% — the sum of the two defect rates"
    - "3% — since machine A produces most items, only its rate matters"
  answer: 1
  explanation: "The law of total probability: P(defect) = P(defect|A)·P(A) + P(defect|B)·P(B) = (0.03)(0.70) + (0.08)(0.30) = 0.021 + 0.024 = 0.045 = 4.5%. The partition is {A, B} — every item comes from exactly one machine. You weight each conditional defect rate by how much production that machine accounts for. The simple average would only be correct if both machines produced equal volumes."

- question: "P(A|B) and P(B|A) are always equal."
  type: true-false
  answer: false
  explanation: "P(A|B) = P(A∩B)/P(B) and P(B|A) = P(A∩B)/P(A). These are equal only when P(A) = P(B). In general they differ substantially. For example, P(cancer | positive test) is very different from P(positive test | cancer). Confusing these two is the basis of many statistical fallacies, including the 'prosecutor's fallacy.' Bayes' theorem is precisely the tool for correctly relating P(A|B) to P(B|A)."

- question: "If P(B) = 0, then P(A|B) is defined to be 0."
  type: true-false
  answer: false
  explanation: "P(A|B) = P(A∩B)/P(B) is undefined when P(B) = 0 — you cannot divide by zero. Conditioning on an impossible event is mathematically undefined in the standard framework. This is not a technicality: conditioning on B means restricting to a non-empty part of the sample space. If B never occurs, there is no meaningful way to ask 'given that B occurred, what is P(A)?'"

- question: "Explain in your own words why the denominator P(B) appears in the formula P(A|B) = P(A∩B)/P(B). What role does it play?"
  type: short-answer
  answer: "When you condition on B, you restrict your sample space to outcomes where B occurred. The numerator P(A∩B) picks out the portion of that restricted space where A also occurs. But P(A∩B) is measured relative to the original full sample space, where all probabilities sum to 1. Dividing by P(B) rescales the restricted space so that probabilities within it also sum to 1 — it renormalizes the B-world to be its own complete probability space."
  explanation: "Think of it as zooming in on B: you are proportionally rescaling all probabilities within B so they add up to 100% of the new, smaller world. Without the denominator, the probabilities of all events given B would sum to P(B), not 1. The denominator P(B) is the normalizing constant that makes this zoom well-defined."
```

## Explainer

You've learned the **probability axioms**: probabilities are non-negative, the full sample space has probability 1, and disjoint events have additive probabilities. Conditional probability is the tool that lets you update probabilities when you learn new information. The key idea: if you know event B has occurred, you're no longer working with the full sample space — you've restricted your attention to the outcomes where B is true. Conditional probability renormalizes your probabilities to fit this smaller space.

Formally, **P(A|B) = P(A ∩ B) / P(B)**: the probability of A given B is the fraction of B's probability that also lies in A. Picture a Venn diagram: B is a region of the sample space; within B, the region also in A is A ∩ B. Conditioning on B means zooming in on B and asking what fraction of it is A. The denominator P(B) rescales so that probabilities within the conditioned space still sum to 1. If A and B have no overlap, P(A|B) = 0 — knowing B makes A impossible. If A contains all of B, P(A|B) = 1 — knowing B guarantees A.

The **law of total probability** is conditional probability used in reverse. If {B₁, B₂, ..., Bₙ} partition the sample space (they're mutually exclusive and cover everything), then P(A) = Σ P(A|Bᵢ) · P(Bᵢ). The intuition: every way that A can happen passes through exactly one Bᵢ, so you sum up the contributions from each scenario, weighted by how likely each scenario is. For example, a factory has two machines: Machine 1 makes 60% of items with a 2% defect rate; Machine 2 makes 40% with a 5% defect rate. P(defect) = (0.02)(0.60) + (0.05)(0.40) = 0.012 + 0.020 = 0.032 — a weighted average over the partition of machines.

Conditional probability is the gateway to **Bayes' theorem**, which you'll encounter next. Bayes' theorem is nothing more than applying the definition twice: P(B|A) = P(A|B) P(B) / P(A). Everything in Bayesian reasoning — updating a prior belief with new evidence, reversing the direction of conditioning — builds on P(A|B) = P(A ∩ B)/P(B). The algebra is simple; the skill is reading a problem, identifying which event is being conditioned on, and correctly translating sentences like "given that we drew a red ball" into a conditioning statement. Practice setting up these problems carefully: define the sample space, identify A and B, and apply the formula.
