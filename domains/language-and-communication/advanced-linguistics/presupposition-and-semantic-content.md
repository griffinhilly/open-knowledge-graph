---
id: presupposition-and-semantic-content
title: Presupposition and Assertion
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: montague-semantics
  type: hard
builds-toward:
- formal-pragmatics-context
tags:
- semantics
- pragmatics
- presupposition
stage: advanced
status: draft
---

# Presupposition and Assertion

## Core Idea
Presuppositions are background assumptions that must be true for a sentence to have a truth value. 'The king of France is bald' presupposes a unique king of France exists; if false, the statement is neither true nor false. Presuppositions survive under negation, conditionals, and questions—a key test distinguishing them from assertions, revealing a fundamental division in linguistic content.

## Explainer

From your study of Montague semantics, you know that sentences are evaluated for truth conditions relative to possible worlds — a sentence is true if the world is as the sentence describes it. Montague semantics handles two-valued logic cleanly: every proposition is either true or false. **Presupposition** introduces a complication: some sentences carry background assumptions that, if false, make the sentence neither true nor false — they fail to express a complete proposition at all. This is called **presupposition failure**, and it forces us to distinguish between what a sentence *asserts* and what it *takes for granted*.

Bertrand Russell's famous example remains the clearest entry point. *The king of France is bald* — said today — **presupposes** that there is a unique king of France. The *assertion* is that this king is bald. If France has no king, the sentence is not false; it is semantically defective. There is nothing to be true or false about. This is in sharp contrast to an ordinary assertion like *France is a monarchy* — that sentence is simply false if France is not a monarchy. The presupposition is different in kind: it is a precondition for the sentence to enter the true/false game at all.

The diagnostic test for presuppositions — and the core of what makes them theoretically interesting — is **projection under embedding**. An ordinary assertion that P is true gets negated when you negate the sentence: *France is a monarchy* is true; *France is not a monarchy* says the opposite. But presuppositions **survive** negation, conditionals, and questions. Consider: *John stopped smoking* presupposes that John used to smoke. Now embed it: *John didn't stop smoking* still carries the presupposition that he used to smoke. *Did John stop smoking?* still presupposes prior smoking. *If John stopped smoking, he'll feel better* still presupposes prior smoking. The presupposition "projects" out of these **presupposition holes** even when the sentence is negated, questioned, or conditionalized. This projection behavior is what distinguishes presuppositions from ordinary **entailments** (which do not survive negation) and from **implicatures** (which are defeasible and pragmatic rather than semantic).

Different **presupposition triggers** — the lexical items that introduce presuppositions — produce slightly different projection behaviors. Definite descriptions (the king) trigger existence and uniqueness presuppositions. Factive verbs like *know*, *realize*, *regret* presuppose the truth of their complement (*John knows it's raining* presupposes it is raining). Change-of-state verbs like *stop*, *begin*, *continue* presuppose a prior state. Cleft constructions (*It was Mary who won*) presuppose that someone won. The challenge for formal semantics — going beyond Montague's two-valued framework — is to model how these presuppositions interact with context, how they can be **accommodated** (silently accepted by the listener even when not previously established), and when they **cancel** rather than project. This is the bridge from Montague semantics into formal pragmatics and dynamic semantics, where the meaning of an utterance is understood as an update to a context state rather than a static truth condition.

