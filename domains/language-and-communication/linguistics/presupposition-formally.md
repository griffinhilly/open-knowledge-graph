---
id: presupposition-formally
title: Presupposition in Formal Semantics
domain: language-and-communication
course: linguistics
prerequisites:
- id: semantic-types-and-composition
  type: hard
- id: presupposition-and-semantic-content
  type: soft
tags:
- semantics
- presupposition
- logic
stage: advanced
status: validated
---

# Presupposition in Formal Semantics

## Core Idea
Formal accounts distinguish presupposition (background assumptions required for a sentence to have a truth value) from assertion (the main claim). Presuppositions project—they are preserved in negation and under quantifiers—a key property formalized in theories like Partial Function Logic.

## Questions

```yaml
- question: "Consider the sentence: 'John stopped smoking.' You negate it to get: 'John didn't stop smoking.' Both the original and the negation carry the implication that John used to smoke. What does this behavior tell you about the proposition 'John used to smoke' relative to the original sentence?"
  type: multiple-choice
  options:
    - "It is asserted by the original sentence, since it is clearly communicated"
    - "It is presupposed — it is background content that projects through negation rather than being canceled by it"
    - "It is a conversational implicature that can be canceled in the right context"
    - "It is a logical entailment, since 'stopping' logically requires a prior state"
  answer: 1
  explanation: "The diagnostic test for presupposition is exactly this: content that *survives negation* is presupposed, not asserted. Asserted content is canceled by negation — 'It is raining' becomes false when negated. But 'John used to smoke' is carried by both 'John stopped smoking' and 'John didn't stop smoking,' so it is presupposed background content, not the main claim. Option D (logical entailment) is partially correct in that there is a logical dependency, but presupposition is distinguished as the specific content that projects not just through negation but also through questions ('Did John stop smoking?') and conditional embeddings."

- question: "Under the partial functions formalization of presupposition, what is the truth value of 'The king of France is bald' in the actual world, given that France has no king?"
  type: multiple-choice
  options:
    - "False — the sentence makes a claim about a king of France, and since no such person exists, the claim is false"
    - "True — the sentence's presupposition being unfulfilled doesn't make it false, so it defaults to true"
    - "Undefined — the sentence's presupposition fails, so the sentence falls outside the domain of true and false"
    - "Meaningless — sentences with failed presuppositions have no semantic content"
  answer: 2
  explanation: "The partial functions formalization says that a sentence with a presupposition denotes a function that is only *defined* (returns T or F) in worlds where the presupposition holds. In worlds where the presupposition fails, the function is undefined — neither true nor false. This is importantly different from falsehood. 'The king of France is bald' is *false* only if there is a king of France who is not bald. Without a king of France, the sentence is like asking whether a number you haven't chosen is odd — the question doesn't have a truth value. This three-valued logic (true / false / undefined) directly formalizes the intuition that presupposition failure is different from falsehood."

- question: "A sentence that presupposes content P and a sentence that asserts content P differ formally in that presupposed content survives embedding under negation, questions, and conditionals, while asserted content does not."
  type: true-false
  answer: true
  explanation: "This projection behavior is the formal signature of presupposition and the key diagnostic test. If you negate a sentence and a piece of content disappears (the sentence no longer implies it), that content was asserted. If the content survives — appears in both the sentence and its negation — it was presupposed. The same test applies to questions: 'Is the king of France bald?' still presupposes France has a king, even though the assertion (baldness) is being questioned. And to conditionals: 'If the king of France is bald...' still assumes France has a king. Projection is the operational criterion that distinguishes presupposition from assertion."

- question: "The sentence 'The king of France is not bald' is false in the actual world, because there is no king of France and the sentence makes a claim about him."
  type: true-false
  answer: false
  explanation: "This is the classic confusion between presupposition failure and falsehood. The sentence is *undefined* (lacks a truth value) in the actual world, not false. It is false only in worlds where France has a king who has hair. When the presupposition fails (no king exists), the sentence cannot be evaluated as true or false — it is like asking whether the current king of France is bald: the question doesn't have an answer, it has a defective presupposition. Under the partial functions formalization, the sentence's truth value function is simply not defined for the actual world. Three-valued logic captures this with a third value (⊥, or 'undefined') that is distinct from false."

- question: "What is the formal diagnostic test for distinguishing whether a piece of content is presupposed or asserted, and why does it work?"
  type: short-answer
  answer: "The diagnostic test is projection under negation (and other operators like questions and conditionals): negate the sentence and check whether the content survives. Asserted content is canceled by negation — it appears in the positive but not the negative version. Presupposed content projects through negation — it appears in both. The test works because negation targets the *asserted* claim of a sentence, flipping its truth value, while leaving background presuppositions intact. A sentence and its negation share the same presuppositions but have opposite assertions."
  explanation: "This projection test is what makes presupposition a formal, testable category rather than just an informal intuition about 'background knowledge.' It allows linguists to distinguish presupposed content from entailments (which don't project through all operators the same way), conversational implicatures (which are cancelable), and direct assertions (which are negation-reversible). The test can be extended to other operators — questions, conditionals, attitude verbs — to refine the analysis further."
```

## Explainer

From semantic types and composition, you know that sentences denote functions from possible worlds to truth values — in any world, the sentence is either true or false. But some sentences fail to have a truth value in certain contexts, not because they are false, but because something their meaning assumes to be true is not. "The king of France is bald" is neither true nor false (on the standard analysis) in the actual world, because there is no king of France. The sentence **presupposes** that a king of France exists; when that presupposition fails, the assertion is left without a truth value. This is different from falsehood — "The king of France is bald" is false only if there is a king of France who is not bald.

The formal signature that distinguishes presupposition from ordinary assertion is **projection behavior** under operators. Ordinary asserted content disappears under negation: "It is raining" is false when negated to "It is not raining." But presuppositions survive: "The king of France is not bald" still carries the presupposition that France has a king. They also project out of questions ("Is the king of France bald?" — still assumes France has a king) and out of conditional antecedents ("If the king of France is bald..." — same assumption). The diagnostic test for presupposition is this survival: content that is **asserted** is canceled by negation; content that is **presupposed** projects through negation, questioning, and embedding. If a piece of content is preserved when you negate the sentence, it was presupposed, not asserted.

The **partial functions** formalization captures this directly. Rather than assigning every sentence a defined truth value in every world, a sentence with a presupposition denotes a **partial function**: it is defined (returns T or F) only in worlds where the presupposition holds, and undefined in worlds where it fails. Negation under this account only applies to defined values — undefined stays undefined. This gives the projection behavior automatically: in worlds where France has no king, neither the sentence nor its negation has a truth value. Three-valued logics generalize this by adding a third value (undefined, ⊥, or indeterminate) alongside true and false, with designated truth tables that keep ⊥ stable under most operations.

A complementary treatment uses **dynamic semantics**, where sentences update a **context set** (the set of possible worlds consistent with what is mutually assumed by the discourse participants). Presuppositions are then requirements on the input context: a sentence with a presupposition is only well-formed if the context already entails the presupposed content. When a sentence is uttered in a context where the presupposition is not already entailed, listeners typically perform **presupposition accommodation** — silently adding the presupposed content to the common ground before processing the assertion. "My sister is coming to dinner tonight" presupposes the speaker has a sister; an interlocutor who didn't know this accommodates it rather than objecting. The distinction between what must already be in context (presupposition) and what the sentence contributes to context (assertion) formalizes the intuition that presuppositions convey background information while assertions convey news.
