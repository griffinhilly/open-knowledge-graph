---
id: presupposition-and-assertion
title: Presupposition and Assertion
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: pragmatics-semantics-boundary
  type: hard
- id: speech-acts-and-communication
  type: soft
builds-toward:
- what-is-said-grice
tags:
- presupposition
- assertion
- truth-conditions
- semantics
stage: abstract-reasoning
status: validated
---

# Presupposition and Assertion

## Core Idea
Presuppositions are semantic contents that must be true for an utterance to have a truth value, distinct from what is asserted. "The king of France is bald" presupposes there is a king of France; if false, the whole utterance fails to be true or false (or context must repair it). Understanding presupposition projection and how it interacts with assertion explains semantic phenomena and communication success.

## Questions

```yaml
- question: "Someone says 'The present king of France is bald,' but France has no king. Which best describes the status of this statement?"
  type: multiple-choice
  options:
    - "It is straightforwardly false, because the presupposed king does not exist"
    - "It fails to have a truth value — it commits presupposition failure and cannot be evaluated as true or false"
    - "It is meaningless because it uses an empty definite description"
    - "It is true, because a non-existent king cannot be bald"
  answer: 1
  explanation: "The sentence presupposes that France has a king. When that presupposition fails, the sentence doesn't simply come out false — it fails to make a determinate truth-apt claim at all. This is presupposition failure: the utterance misfires rather than merely being wrong. Option A represents Russell's original view (the sentence is false); option B reflects Strawson's insight that the sentence fails to get off the ground as a truth-apt assertion when the presupposition is absent."

- question: "Someone asks: 'Have you stopped cheating on tests?' You have never cheated. Which response correctly targets the presupposition rather than the assertion?"
  type: multiple-choice
  options:
    - "'No, I haven't stopped' — denying the assertion while accepting the presupposition"
    - "'Yes, I have stopped' — accepting both the presupposition and the assertion"
    - "'I never cheated on tests in the first place' — denying the presupposition itself"
    - "'That's an unfair question' — refusing to engage with the structure"
  answer: 2
  explanation: "The question presupposes that you have cheated in the past (that's what 'stopped' requires). Answering 'no' accepts the presupposition and merely denies the assertion — it implies you're still cheating. The only correct response is to deny the presupposition: 'I never cheated.' This is a presupposition denial — it pulls the prop from under the entire question rather than engaging with the assertion on the question's own terms."

- question: "Negating a sentence eliminates its presuppositions — 'The king of France is not bald' carries no presupposition about France having a king."
  type: true-false
  answer: false
  explanation: "Presuppositions survive negation — this is the definitive diagnostic test distinguishing presupposed from asserted content. Both 'The king of France is bald' and 'The king of France is not bald' presuppose that France has a king. Assertions flip under negation (committing to the positive vs. denying it); presuppositions remain stable through negation, embedding, and questioning. This survival-under-negation test is what separates presupposition from implicature."

- question: "Factive verbs like 'know,' 'realize,' and 'discover' trigger presuppositions because they assume the truth of their complement clauses."
  type: true-false
  answer: true
  explanation: "'Sam knows that it is raining' presupposes that it is raining — the verb 'knows' builds in the truth of its complement. Even 'Sam doesn't know that it is raining' presupposes rain: negating the factive verb doesn't cancel the embedded clause's presupposition. Factive verbs are among the most important presupposition triggers, alongside definite descriptions, change-of-state verbs ('stopped,' 'started'), and iteratives ('again,' 'still')."

- question: "What is the practical difference between asserting something and presupposing it? Use an example to show why the distinction matters for communication."
  type: short-answer
  answer: "An assertion is what the speaker explicitly commits to as true — the main claim, which can be accepted or denied directly. A presupposition is background content the speaker takes for granted without asserting it. Example: 'My sister just graduated' — assertion: a graduation just occurred; presupposition: the speaker has a sister. Denying the assertion ('No, she didn't') accepts the sister exists. Denying the presupposition requires a different move: 'Wait — you have a sister?'"
  explanation: "The distinction matters because false presuppositions can smuggle unverified content past a listener focused on the main assertion. Political and legal language routinely exploits this: 'When did you stop embezzling funds?' forces the respondent to either accept the presupposition of past embezzlement or explicitly challenge it — and explicitly challenging a presupposition is a more disruptive conversational move than simply denying an assertion. Tracking presuppositional structure reveals how much implicit content shapes communication."
```

## Explainer

When you make a statement, you are not just asserting one thing — you are simultaneously taking a background of other things for granted. **Presuppositions** are the background assumptions that a sentence requires to be in place for the main claim to even get off the ground as a truth-apt assertion. The classic example is Bertrand Russell's: "The present king of France is bald." This sentence presupposes that France currently has a king. If it doesn't, the sentence doesn't just come out false — it fails to make a determinate claim at all. Philosophers call this **presupposition failure**: the utterance misfires rather than merely being wrong.

This is distinct from what the sentence **asserts**, which is the main claim the speaker is committing themselves to as true. Assertion and presupposition carry different semantic weight. If I assert "John has stopped smoking," I presuppose that John was smoking (if he never smoked, the assertion is neither true nor false in a well-defined way), and I assert that he no longer is. You can reject a presupposition with a **presupposition denial**: "John hasn't stopped smoking — he never started." This is different from just saying "that's false." You're not denying the assertion; you're pulling out the presuppositional prop from under it.

One of the most diagnostically useful tests for presuppositions is that they **survive negation**. Both "The king of France is bald" and "The king of France is not bald" presuppose that there is a king of France. If negation killed the presupposition, we'd say the negative form lacks it — but it doesn't. Assertions, by contrast, flip under negation: asserting the positive commits you to something the negative denies. This survival-under-negation test distinguishes presupposed content from what is merely conversationally implied (which you may have studied as implicature).

**Presupposition projection** is the phenomenon where presuppositions of embedded clauses bubble up to the whole sentence. "Sam knows that there's life on Mars" presupposes that there is life on Mars — the presupposition of the embedded clause "there's life on Mars" projects through the factive verb "knows." Factive verbs (know, realize, discover) are major presupposition triggers. So are definite descriptions, iteratives ("again," "still"), and change-of-state verbs ("stop," "start"). Knowing which constructions trigger presuppositions helps you see how much context-setting is happening implicitly in ordinary conversation, and why removing a false presupposition can feel more disruptive than simply contradicting an assertion.

You've already studied the pragmatics-semantics boundary from your prerequisites, and presupposition sits right on that boundary. Some presuppositions are semantic — built into the meaning of the words themselves, regardless of context. Others are **pragmatic presuppositions**: things the speaker takes for granted in the context of utterance, which listeners are expected to accommodate. When context can supply what's missing (a friend has clearly been telling you about a new relationship and then says "he told me he loves me"), listeners automatically **accommodate** the presupposition without even noticing. Presupposition accommodation is ubiquitous, invisible when it succeeds, and disruptive when it fails — which is why tracking presuppositional structure is essential to understanding how communication works and breaks down.

