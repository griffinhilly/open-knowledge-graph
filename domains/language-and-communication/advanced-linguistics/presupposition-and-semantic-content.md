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
stage: expert
status: draft
---

# Presupposition and Assertion

## Core Idea
Presuppositions are background assumptions that must be true for a sentence to have a truth value. 'The king of France is bald' presupposes a unique king of France exists; if false, the statement is neither true nor false. Presuppositions survive under negation, conditionals, and questions—a key test distinguishing them from assertions, revealing a fundamental division in linguistic content.

## Questions

```yaml
- question: "Consider the sentence: 'My brother stopped lying.' Which of the following demonstrates that 'My brother used to lie' is a *presupposition* rather than an ordinary entailment?"
  type: multiple-choice
  options:
    - "It follows logically from the meaning of 'stopped'"
    - "It is strongly implied in ordinary conversation"
    - "It survives under negation: 'My brother didn't stop lying' still implies he used to lie"
    - "It can be cancelled without contradiction by adding context"
  answer: 2
  explanation: "The diagnostic test for presupposition is projection — survival under embedding operators like negation, questions, and conditionals. An ordinary entailment is cancelled by negation: if P entails Q, then not-P does not entail Q. But presuppositions survive: 'My brother stopped lying' and 'My brother didn't stop lying' both carry the background assumption that he used to lie. The negation targets the assertion ('stopped') while leaving the presupposition ('used to lie') intact. This projection behavior is what distinguishes presuppositions from entailments and from implicatures (which can be cancelled without contradiction)."

- question: "Russell's example: 'The present king of France is bald.' Assuming France is a republic with no king, what is the semantic status of this sentence?"
  type: multiple-choice
  options:
    - "False — there is no king, so a bald king of France does not exist, making the sentence false"
    - "True — the sentence makes a vacuous claim about a non-existent entity, which is trivially satisfied"
    - "Neither true nor false — the existence presupposition fails, and the sentence cannot be assigned a truth value"
    - "Indeterminate only because we lack empirical information about whether the king is bald"
  answer: 2
  explanation: "This is the classic case of presupposition failure. The sentence 'The present king of France is bald' presupposes (via the definite description 'the present king of France') that there is a unique current king of France. If this presupposition fails, the sentence does not get to enter the true/false game — there is nothing to predicate baldness of. It is not merely false (as Russell originally argued in his theory of descriptions); it is semantically defective. This is the key contrast with ordinary false assertions: 'France is a monarchy' is simply false if France is a republic, but 'The king of France is bald' fails differently — it suffers presupposition failure."

- question: "If 'John knows it is raining' presupposes that it is raining, then 'John does not know it is raining' also presupposes that it is raining."
  type: true-false
  answer: true
  explanation: "This illustrates the projection property that defines presuppositions. 'Know' is a factive verb — it presupposes the truth of its complement. When you negate the sentence, the assertion changes (now claiming John lacks knowledge), but the presupposition (that it is in fact raining) is preserved. The same holds for questions ('Does John know it's raining?' still presupposes rain) and conditionals ('If John knows it's raining, he'll bring an umbrella' still presupposes rain). Projection through negation and other operators is the defining signature of presupposition, distinguishing it from both entailment and implicature."

- question: "Presuppositions and conversational implicatures are both types of content that go beyond the literal semantic content of a sentence, so they behave similarly — both survive negation and are difficult to cancel."
  type: true-false
  answer: false
  explanation: "Presuppositions and implicatures differ in a crucial way: implicatures are *defeasible* — they can be cancelled without contradiction. If I say 'Some students passed' and you ask if all did, I can add 'In fact, all of them did' without contradiction, cancelling the implicature that not all passed. But presuppositions resist cancellation: you cannot say 'John stopped smoking, but he never smoked' without contradiction (or at least radical pragmatic incoherence). This defeasibility test cleanly separates implicatures (pragmatic, cancellable) from presuppositions (semantic background, not cancellable)."

- question: "What is 'presupposition projection,' and why does it serve as the key diagnostic test distinguishing presuppositions from ordinary entailments?"
  type: short-answer
  answer: "Presupposition projection is the phenomenon whereby a presupposition introduced in an embedded clause survives and becomes a presupposition of the entire sentence, even when the sentence is negated, questioned, or placed in a conditional. For example, if S presupposes P, then 'not S,' 'Is S?,' and 'If S, then Q' all also presuppose P. This behavior contrasts sharply with ordinary entailments: if S entails Q, then 'not S' does not entail Q (negation cancels entailments). Because negation cancels assertions but not presuppositions, negation provides the clearest diagnostic: embed the sentence under negation and ask whether the background assumption survives. If it does, the content is a presupposition; if it is cancelled, it is an entailment."
  explanation: "The name 'projection' describes how the presupposition 'projects out' of an embedded environment to become a presupposition of the whole. Understanding projection is essential for formal semantics because it shows that truth-conditional content and presuppositional content respond differently to logical operators — requiring either a three-valued semantics or a dynamic framework where utterances update context states rather than simply being evaluated against a static world."
```

## Explainer

From your study of Montague semantics, you know that sentences are evaluated for truth conditions relative to possible worlds — a sentence is true if the world is as the sentence describes it. Montague semantics handles two-valued logic cleanly: every proposition is either true or false. **Presupposition** introduces a complication: some sentences carry background assumptions that, if false, make the sentence neither true nor false — they fail to express a complete proposition at all. This is called **presupposition failure**, and it forces us to distinguish between what a sentence *asserts* and what it *takes for granted*.

Bertrand Russell's famous example remains the clearest entry point. *The king of France is bald* — said today — **presupposes** that there is a unique king of France. The *assertion* is that this king is bald. If France has no king, the sentence is not false; it is semantically defective. There is nothing to be true or false about. This is in sharp contrast to an ordinary assertion like *France is a monarchy* — that sentence is simply false if France is not a monarchy. The presupposition is different in kind: it is a precondition for the sentence to enter the true/false game at all.

The diagnostic test for presuppositions — and the core of what makes them theoretically interesting — is **projection under embedding**. An ordinary assertion that P is true gets negated when you negate the sentence: *France is a monarchy* is true; *France is not a monarchy* says the opposite. But presuppositions **survive** negation, conditionals, and questions. Consider: *John stopped smoking* presupposes that John used to smoke. Now embed it: *John didn't stop smoking* still carries the presupposition that he used to smoke. *Did John stop smoking?* still presupposes prior smoking. *If John stopped smoking, he'll feel better* still presupposes prior smoking. The presupposition "projects" out of these **presupposition holes** even when the sentence is negated, questioned, or conditionalized. This projection behavior is what distinguishes presuppositions from ordinary **entailments** (which do not survive negation) and from **implicatures** (which are defeasible and pragmatic rather than semantic).

Different **presupposition triggers** — the lexical items that introduce presuppositions — produce slightly different projection behaviors. Definite descriptions (the king) trigger existence and uniqueness presuppositions. Factive verbs like *know*, *realize*, *regret* presuppose the truth of their complement (*John knows it's raining* presupposes it is raining). Change-of-state verbs like *stop*, *begin*, *continue* presuppose a prior state. Cleft constructions (*It was Mary who won*) presuppose that someone won. The challenge for formal semantics — going beyond Montague's two-valued framework — is to model how these presuppositions interact with context, how they can be **accommodated** (silently accepted by the listener even when not previously established), and when they **cancel** rather than project. This is the bridge from Montague semantics into formal pragmatics and dynamic semantics, where the meaning of an utterance is understood as an update to a context state rather than a static truth condition.

