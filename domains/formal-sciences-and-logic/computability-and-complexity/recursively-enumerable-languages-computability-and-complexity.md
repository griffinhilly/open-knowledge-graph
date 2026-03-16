---
id: recursively-enumerable-languages-computability-and-complexity
title: 'Recursively Enumerable Languages: Semi-Decidability'
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: recursive-languages
  type: hard
builds-toward:
- turing-degrees-equivalence
- undecidable-problems-examples
tags:
- semi-decidable
- recursively-enumerable
- halting
- verification
stage: advanced
status: draft
---

# Recursively Enumerable Languages: Semi-Decidability

## Core Idea
A language is recursively enumerable (RE) if there exists a Turing machine that accepts exactly those strings in the language but may not halt on strings outside the language. RE languages represent problems where 'yes' answers are verifiable but 'no' answers may require infinite computation. Every recursive language is RE, but not vice versa.

## How It's Best Learned
Use the Halting Problem as motivating example: it's RE (simulate and accept if halts) but not recursive. Contrast with problems that are RE and recursive.

## Common Misconceptions
- Confusing 'enumerates' with 'lists in order.' RE means we can verify membership by simulation, not necessarily list in canonical order.
- Thinking RE languages are rarer than recursive. In fact, the complement of an undecidable problem is often not RE.

## Explainer

You already know what a **recursive (decidable) language** is: a Turing machine that always halts and always gives the correct yes/no answer. Now weaken that requirement in one direction only: the machine must halt and accept when the answer is yes, but it is allowed to run forever when the answer is no. This is **semi-decidability**, and languages with this property are called **recursively enumerable (RE)**. The name comes from an equivalent characterization: a language is RE if and only if some Turing machine can enumerate (print out, one by one) all its members — not necessarily in any particular order, but eventually producing each member.

The relationship to recursive languages is a strict containment. Every recursive language is RE — just ignore the "run forever on no" permission. But there are RE languages that are not recursive. The canonical example is the **Halting Problem**: the set of (M, w) pairs where Turing machine M halts on input w. To verify a "yes" answer, just simulate M on w; if M halts, accept. But to answer "no," you would need to confirm that M runs forever — and no algorithm can do that in general. The Halting Problem is RE but not recursive.

This asymmetry between yes and no has a striking consequence for complements. A language L is recursive if and only if both L and its complement L̄ are RE. This is because if you have a semi-decider for L and a semi-decider for L̄, you can run them in parallel: whichever halts first tells you the answer, guaranteeing termination. If a language is RE but not recursive, its complement cannot be RE at all — otherwise we could combine the two semi-deciders to get a full decider, contradicting undecidability. The complement of the Halting Problem is the prototypical example of a language that is **not** RE.

RE languages form the top of the Chomsky hierarchy: they are exactly what unrestricted Turing machines can recognize. Understanding them sharpens your mental model of what computation can and cannot do. The recursive languages are the "safe" territory — problems we can fully decide. The RE languages are the "one-sided" territory — problems where we can confirm yes answers but may loop on no. And beyond RE lies the truly unrecognizable: problems where no Turing machine gives even a one-sided answer. The boundary between recursive and RE, marked by the Halting Problem, is the deepest fault line in computability theory.
