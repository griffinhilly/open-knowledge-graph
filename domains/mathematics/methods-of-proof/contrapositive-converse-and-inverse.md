---
id: contrapositive-converse-and-inverse
title: The Contrapositive, Converse, and Inverse
domain: mathematics
course: methods-of-proof
prerequisites:
- id: proof-by-contrapositive
  type: hard
tags:
- proof
- logical-relationships
- implications
stage: formal-systems
status: validated
---

# The Contrapositive, Converse, and Inverse

## Core Idea
For conditional p → q: the contrapositive ¬q → ¬p is logically equivalent; the converse q → p is NOT equivalent; the inverse ¬p → ¬q is NOT equivalent. Distinguishing these prevents logical errors in proof.

## How It's Best Learned
Test with concrete examples: 'If even, then divisible by 2' versus its converse, contrapositive, and inverse.

## Common Misconceptions
- Treating the converse as equivalent to the original (a very common error).
- Thinking the inverse is equivalent to the original or contrapositive.

## Questions

```yaml
- question: "The statement 'If a function is differentiable at a point, then it is continuous there' is true. Which of the following is logically equivalent to this statement?"
  type: multiple-choice
  options:
    - "If a function is continuous at a point, then it is differentiable there"
    - "If a function is not differentiable at a point, then it is not continuous there"
    - "If a function is not continuous at a point, then it is not differentiable there"
    - "If a function is not continuous at a point, then it is differentiable there"
  answer: 2
  explanation: "The contrapositive of p → q is ¬q → ¬p, and it is the only one of the four forms logically equivalent to the original. Here p = 'differentiable' and q = 'continuous,' so the contrapositive is 'If not continuous, then not differentiable' — option C. Option A is the converse (q → p), which is famously false (|x| is continuous but not differentiable at 0). Option B is the inverse (¬p → ¬q), which is also false. Only the contrapositive preserves the truth value."

- question: "A student argues: 'We know that if it rains, the ground gets wet. Right now the ground is wet — so it must have rained.' What logical error is this?"
  type: multiple-choice
  options:
    - "Denying the antecedent: concluding ¬q from ¬p"
    - "Affirming the consequent: treating the converse as equivalent to the original"
    - "Applying the contrapositive: concluding ¬p from ¬q"
    - "No error — the argument is valid because rain implies wet ground"
  answer: 1
  explanation: "This is affirming the consequent: the student has the conditional 'p → q' (rain → wet) and observes q (wet), then concludes p (rain). This treats the converse 'q → p' as equivalent to the original — a classic logical error. The ground could be wet from a sprinkler, a spilled drink, or any other cause. Wet ground does not entail rain; only the absence of wet ground entails the absence of rain (the valid contrapositive direction)."

- question: "The converse and the inverse of a conditional statement are logically equivalent to each other."
  type: true-false
  answer: true
  explanation: "There are only two distinct logical forms among the four: the original (p → q) and its contrapositive (¬q → ¬p) are equivalent; the converse (q → p) and the inverse (¬p → ¬q) are equivalent to each other. The converse and inverse are not equivalent to the original. So when the original is true, the contrapositive is true, but the converse and inverse may be true or false — and whatever truth value the converse has, the inverse shares it."

- question: "If a conditional p → q is true, its converse q → p is expected to also be true."
  type: true-false
  answer: false
  explanation: "This is the most common error in conditional logic. The converse is not logically equivalent to the original. A conditional and its converse can have different truth values. The example from the topic is conclusive: 'If a function is differentiable, it is continuous' is true; the converse 'If a function is continuous, it is differentiable' is false (|x| at 0 is a counterexample). Only the contrapositive is guaranteed to have the same truth value as the original."

- question: "Why is affirming the converse a logical error? Give a concrete mathematical or everyday example."
  type: short-answer
  answer: "Affirming the converse mistakes q → p for p → q. The converse is not logically equivalent to the original conditional. A concrete example: 'If n is even, then n is divisible by 2' is true. The converse is 'If n is divisible by 2, then n is even' — which happens to also be true in this case, but that's a coincidence. A case where it fails: 'If it rains, the ground is wet' (true), but the converse 'If the ground is wet, it rained' is false — the ground could be wet for other reasons."
  explanation: "The error matters in mathematics because many important theorems are one-directional. 'Differentiable implies continuous' is true; 'continuous implies differentiable' is false. Using the converse of a theorem as if it were proven generates false conclusions. The discipline of asking 'is this the original, the converse, the contrapositive, or the inverse?' before applying a conditional prevents this entire class of proof error."
```

## Explainer

You already know proof by contrapositive: to prove p → q, you instead prove ¬q → ¬p, because these two statements are logically equivalent. Now it is worth mapping all four forms a conditional can take, so you can recognize which transformations preserve truth and which do not. Start with the conditional **p → q**: "If p, then q." There are exactly three related forms: the **contrapositive** (¬q → ¬p), the **converse** (q → p), and the **inverse** (¬p → ¬q).

A concrete example anchors all four. Let p = "it is raining" and q = "the ground is wet." Then: the original says "If it is raining, then the ground is wet." The contrapositive says "If the ground is not wet, then it is not raining." The converse says "If the ground is wet, then it is raining." The inverse says "If it is not raining, then the ground is not wet." The original and contrapositive are both true — if it rains the ground gets wet, and if the ground is dry you know it hasn't rained. But the converse and inverse are false: the ground could be wet from a sprinkler, not rain. This shows that flipping the direction (converse) or negating both parts (inverse) can destroy truth.

The equivalence structure is precise. **p → q is logically equivalent to ¬q → ¬p** (contrapositive). This follows from truth tables: both are false only when p is true and q is false. Meanwhile, **q → p is logically equivalent to ¬p → ¬q** (converse and inverse are equivalent to each other). So there are really only two distinct logical forms among the four: the original/contrapositive pair, and the converse/inverse pair. These pairs are not equivalent to each other.

The practical danger is **affirming the converse**: concluding that because q → p looks similar to p → q, the two can be swapped freely. In mathematics, this mistake generates false theorems. For example, "if a function is differentiable, then it is continuous" is true; the converse "if a function is continuous, then it is differentiable" is famously false (|x| is continuous at 0 but not differentiable there). Training yourself to ask "which of the four forms is this claim?" before using it in a proof prevents this class of error entirely.
