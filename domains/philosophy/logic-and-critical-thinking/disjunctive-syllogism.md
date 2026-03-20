---
id: disjunctive-syllogism
title: Disjunctive Syllogism
domain: philosophy
course: logic-and-critical-thinking
prerequisites:
- id: inference-patterns-and-validity
  type: hard
- id: propositional-logic-introduction
  type: soft
builds-toward:
- argument-evaluation-holistic
tags:
- disjunction
- or
- deductive-reasoning
stage: formal-systems
status: draft
---

# Disjunctive Syllogism

## Core Idea
Disjunctive syllogism uses 'or' statements: either A or B (or both); one of them is false; therefore the other is true. This pattern applies when we must choose among alternatives or eliminate possibilities. Understanding disjunctive reasoning helps us reason through situations where multiple options exist but some are ruled out.

## Explainer

**Disjunctive syllogism** is one of the most useful inference patterns in everyday reasoning. Its formal structure is: (1) P or Q; (2) not-P; (3) therefore, Q. In plain language: if you know that at least one of two options is true, and you can rule out one of them, the other must hold. The detective who reasons "The suspect was either in London or Paris that night — we've confirmed he was not in London — therefore he was in Paris" is using disjunctive syllogism. The validity of this pattern follows directly from the meaning of "or" in logic.

You've already encountered **validity** and **argument forms** as a prerequisite. Disjunctive syllogism is formally valid: there is no possible world in which both premises are true and the conclusion is false. If "P or Q" is true (meaning at least one is true) and "not-P" is true (P is definitely false), then Q is the only remaining way to satisfy the first premise. The inference is airtight. This distinguishes it from invalid elimination patterns — for instance, "P or Q; P is true; therefore Q is false" commits the fallacy of affirming a disjunct, because inclusive or allows both to be true simultaneously.

The most important subtlety is the distinction between **inclusive or** and **exclusive or**. Standard logical "or" is inclusive: "P or Q" means at least one is true, possibly both. Disjunctive syllogism works the same either way — if we know not-P, we conclude Q whether or not both could have been true. But in natural language, "or" is sometimes exclusive: "You can have cake or pie" often implies not both. Recognizing which sense is intended matters for constructing valid disjunctive arguments. When analyzing arguments in ordinary language, you may need to check whether the disjunction is meant inclusively or exclusively before applying this pattern.

In practice, disjunctive syllogism is the engine behind **process of elimination**. Whenever you have an exhaustive set of possibilities and start ruling them out, you are implicitly chaining disjunctive syllogisms. Doctors diagnosing by exclusion, detectives eliminating suspects, engineers testing components one by one — all rely on this pattern. The key requirement is that the initial disjunction genuinely covers all possibilities. If you set up "either A or B" but there's actually a third option C you've overlooked, eliminating A doesn't establish B. The fallacy of false dilemma exploits precisely this: artificially narrowing a disjunction to force a predetermined conclusion. Disjunctive syllogism is valid; setting up a false disjunction is not.

