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
status: draft
---

# Presupposition in Formal Semantics

## Core Idea
Formal accounts distinguish presupposition (background assumptions required for a sentence to have a truth value) from assertion (the main claim). Presuppositions project—they are preserved in negation and under quantifiers—a key property formalized in theories like Partial Function Logic.

## Explainer

From semantic types and composition, you know that sentences denote functions from possible worlds to truth values — in any world, the sentence is either true or false. But some sentences fail to have a truth value in certain contexts, not because they are false, but because something their meaning assumes to be true is not. "The king of France is bald" is neither true nor false (on the standard analysis) in the actual world, because there is no king of France. The sentence **presupposes** that a king of France exists; when that presupposition fails, the assertion is left without a truth value. This is different from falsehood — "The king of France is bald" is false only if there is a king of France who is not bald.

The formal signature that distinguishes presupposition from ordinary assertion is **projection behavior** under operators. Ordinary asserted content disappears under negation: "It is raining" is false when negated to "It is not raining." But presuppositions survive: "The king of France is not bald" still carries the presupposition that France has a king. They also project out of questions ("Is the king of France bald?" — still assumes France has a king) and out of conditional antecedents ("If the king of France is bald..." — same assumption). The diagnostic test for presupposition is this survival: content that is **asserted** is canceled by negation; content that is **presupposed** projects through negation, questioning, and embedding. If a piece of content is preserved when you negate the sentence, it was presupposed, not asserted.

The **partial functions** formalization captures this directly. Rather than assigning every sentence a defined truth value in every world, a sentence with a presupposition denotes a **partial function**: it is defined (returns T or F) only in worlds where the presupposition holds, and undefined in worlds where it fails. Negation under this account only applies to defined values — undefined stays undefined. This gives the projection behavior automatically: in worlds where France has no king, neither the sentence nor its negation has a truth value. Three-valued logics generalize this by adding a third value (undefined, ⊥, or indeterminate) alongside true and false, with designated truth tables that keep ⊥ stable under most operations.

A complementary treatment uses **dynamic semantics**, where sentences update a **context set** (the set of possible worlds consistent with what is mutually assumed by the discourse participants). Presuppositions are then requirements on the input context: a sentence with a presupposition is only well-formed if the context already entails the presupposed content. When a sentence is uttered in a context where the presupposition is not already entailed, listeners typically perform **presupposition accommodation** — silently adding the presupposed content to the common ground before processing the assertion. "My sister is coming to dinner tonight" presupposes the speaker has a sister; an interlocutor who didn't know this accommodates it rather than objecting. The distinction between what must already be in context (presupposition) and what the sentence contributes to context (assertion) formalizes the intuition that presuppositions convey background information while assertions convey news.
