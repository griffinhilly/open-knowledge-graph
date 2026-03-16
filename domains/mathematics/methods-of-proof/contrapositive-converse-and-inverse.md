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
status: draft
---

# The Contrapositive, Converse, and Inverse

## Core Idea
For conditional p → q: the contrapositive ¬q → ¬p is logically equivalent; the converse q → p is NOT equivalent; the inverse ¬p → ¬q is NOT equivalent. Distinguishing these prevents logical errors in proof.

## How It's Best Learned
Test with concrete examples: 'If even, then divisible by 2' versus its converse, contrapositive, and inverse.

## Common Misconceptions
- Treating the converse as equivalent to the original (a very common error).
- Thinking the inverse is equivalent to the original or contrapositive.

## Explainer

You already know proof by contrapositive: to prove p → q, you instead prove ¬q → ¬p, because these two statements are logically equivalent. Now it is worth mapping all four forms a conditional can take, so you can recognize which transformations preserve truth and which do not. Start with the conditional **p → q**: "If p, then q." There are exactly three related forms: the **contrapositive** (¬q → ¬p), the **converse** (q → p), and the **inverse** (¬p → ¬q).

A concrete example anchors all four. Let p = "it is raining" and q = "the ground is wet." Then: the original says "If it is raining, then the ground is wet." The contrapositive says "If the ground is not wet, then it is not raining." The converse says "If the ground is wet, then it is raining." The inverse says "If it is not raining, then the ground is not wet." The original and contrapositive are both true — if it rains the ground gets wet, and if the ground is dry you know it hasn't rained. But the converse and inverse are false: the ground could be wet from a sprinkler, not rain. This shows that flipping the direction (converse) or negating both parts (inverse) can destroy truth.

The equivalence structure is precise. **p → q is logically equivalent to ¬q → ¬p** (contrapositive). This follows from truth tables: both are false only when p is true and q is false. Meanwhile, **q → p is logically equivalent to ¬p → ¬q** (converse and inverse are equivalent to each other). So there are really only two distinct logical forms among the four: the original/contrapositive pair, and the converse/inverse pair. These pairs are not equivalent to each other.

The practical danger is **affirming the converse**: concluding that because q → p looks similar to p → q, the two can be swapped freely. In mathematics, this mistake generates false theorems. For example, "if a function is differentiable, then it is continuous" is true; the converse "if a function is continuous, then it is differentiable" is famously false (|x| is continuous at 0 but not differentiable there). Training yourself to ask "which of the four forms is this claim?" before using it in a proof prevents this class of error entirely.
