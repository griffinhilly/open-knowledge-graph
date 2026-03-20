---
id: reductio-ad-absurdum-method
title: 'Reductio ad Absurdum: Proof by Contradiction'
domain: philosophy
course: logic-and-critical-thinking
prerequisites:
- id: logical-operators-and-truth-functions
  type: hard
- id: conditional-statements-and-material-conditional
  type: soft
- id: propositional-logic-introduction
  type: soft
builds-toward:
- thought-experiment-construction
tags:
- proof-method
- contradiction
- indirect-proof
stage: formal-systems
status: draft
---

# Reductio ad Absurdum: Proof by Contradiction

## Core Idea
In reductio ad absurdum, you assume the negation of what you want to prove, then derive a contradiction or absurdity. The contradiction reveals that your assumption must be false, so your original statement is true. This indirect method is especially powerful when direct proof is difficult.

## How It's Best Learned
Start with simple mathematical examples (proving √2 is irrational). Move to logical arguments. Show the structure: assume negation → derive contradiction → conclude original is true.

## Common Misconceptions
Thinking any contradiction works (it must be a genuine contradiction to established fact or premises). Failing to clearly state what is being assumed. Confusing reductio with other proof techniques.

## Explainer

From your study of propositional logic and logical operators, you know that a contradiction is a statement of the form P ∧ ¬P — something and its negation asserted simultaneously. You also know that any system that contains a contradiction becomes trivially explosive: from a contradiction, any statement whatsoever can be derived. This makes contradictions the logical equivalent of a structural failure. **Reductio ad absurdum** — literally "reduction to absurdity" — harnesses this property as a proof strategy: if assuming something leads inevitably to a contradiction, the assumption must be false.

The structure of the method is always the same. You want to prove proposition P. Instead of finding a direct path to P, you temporarily assume ¬P (the negation of what you want to prove). You then reason forward from ¬P using valid inference steps. If that chain of reasoning terminates in a contradiction — a statement that is known to be false, or a statement that contradicts one of your established premises — you have shown that ¬P cannot hold. Since ¬P leads to absurdity, P must be true.

The classical example that makes this concrete is the proof that √2 is irrational. Assume the negation: that √2 *is* rational, meaning it can be expressed as a fraction a/b in lowest terms. Working through the algebra, you find that a² must be even, so a must be even. If a is even, write a = 2k. Substituting back, b² = 2k², which means b² is even, so b must be even too. But if both a and b are even, the fraction a/b was not in lowest terms — contradicting our initial assumption. The assumption that √2 is rational has generated an internal contradiction. Therefore √2 is irrational.

The method is powerful precisely because it sidesteps the need to construct a direct proof. Sometimes we don't know how to get to the conclusion from first principles, but we can clearly see what would go wrong if the conclusion were false. The move of *testing the negation* turns impossibility into a proof tool. Philosophy deploys this constantly: thought experiments that show a position leads to absurd consequences are informal versions of reductio. If accepting a premise entails something clearly false — say, that everyone should always lie, or that there is no knowledge at all — the original premise is indicted. The method is at home in mathematics, logic, and philosophical argument alike.
