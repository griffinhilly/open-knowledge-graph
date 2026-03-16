---
id: compositional-semantics
title: Compositional Semantics
domain: language-and-communication
course: linguistics
prerequisites:
- id: lexical-semantics
  type: hard
- id: syntactic-structure
  type: soft
builds-toward:
- linguistic-pragmatics
tags:
- semantics
- compositionality
- truth conditions
- entailment
- presupposition
- scope
stage: formal-systems
status: validated
---

# Compositional Semantics

## Core Idea
Compositional semantics addresses how the meanings of complex expressions are built from the meanings of their parts combined according to syntactic structure — Frege's principle of compositionality. Truth-conditional semantics analyzes sentence meaning as the conditions under which a sentence would be true. Key phenomena include entailment (if A is true, B must follow necessarily), presupposition (background assumptions that survive negation), and scope ambiguity (when quantifiers or negation interact in multiple ways).

## How It's Best Learned
Practice writing truth conditions for simple sentences. Work through scope ambiguity examples with quantifiers like 'every' and 'some'. Distinguish entailment from presupposition by testing what happens when the sentence is negated.

## Common Misconceptions
- Compositionality does not mean every phrase has a literal, part-by-part meaning — idioms and metaphors are systematic exceptions that require special treatment.
- Truth conditions describe what it would take for a sentence to be true, not whether it is actually true.
- Presuppositions, unlike assertions, survive negation — 'John didn't stop smoking' still presupposes he was smoking.

## Questions

```yaml
- question: "Which pair of sentences best illustrates the entailment relation?"
  type: multiple-choice
  options:
    - "'The cat slept on the mat' and 'The cat was on the mat' — the first entails the second"
    - "'It is raining' and 'The streets are wet' — the first entails the second"
    - "'John stopped smoking' and 'John used to smoke' — neither entails the other"
    - "'Every student passed' and 'Some students passed' — the second entails the first"
  answer: 0
  explanation: "Entailment is a strictly logical relation: A entails B when B must be true in every situation where A is true, purely in virtue of meaning. 'The cat slept on the mat' entails 'The cat was on the mat' because sleeping somewhere guarantees being there. Option B fails because streets being wet has independent causes; option D has the entailment direction reversed — 'Every student passed' entails 'Some students passed', not the other way around."

- question: "Negating a sentence cancels its presuppositions, just as it cancels its ordinary assertions."
  type: true-false
  answer: false
  explanation: "This is the defining property of presuppositions: they survive negation. 'John stopped smoking' asserts he has stopped, but presupposes he was smoking before. The negation 'John didn't stop smoking' cancels the assertion but preserves the presupposition — we still take it for granted that John was smoking. Ordinary entailments and assertions, by contrast, are cancelled by negation."

- question: "What is scope ambiguity, and why does it arise in sentences with quantifiers?"
  type: short-answer
  answer: "Scope ambiguity occurs when a sentence with multiple quantifiers or operators (like 'every', 'some', or negation) can be interpreted in more than one way depending on which expression takes wider scope. For example, 'Every linguist speaks some language' can mean either that there is one particular language all linguists share (wide scope for 'some') or that each linguist speaks at least one language, possibly different ones (narrow scope for 'some'). It arises because syntax does not always uniquely determine the logical relationship between quantifiers."
  explanation: "Compositionality pairs with syntactic structure, but quantifiers can take scope independently of their surface position. Formal semantic frameworks (like lambda calculus or quantifier raising) make these interpretations explicit by assigning each quantifier a logical scope domain. Understanding scope ambiguity is essential for modeling the full range of meanings a sentence can express."
```

## Explainer

If you have studied lexical semantics, you know the meaning of individual words. But knowing that "dog" means dog and "chased" means chased does not tell you what "Every dog chased some cat" means — or why that sentence is ambiguous in a way that "The dog chased the cat" is not. Compositional semantics is the study of how sentential meaning is built from word meanings and grammatical structure. Frege's foundational insight, called the **principle of compositionality**, states that the meaning of a complex expression is a function of the meanings of its parts and the way those parts are combined. Structure matters: "The dog bit the man" and "The man bit the dog" contain the same words but mean different things because the syntactic roles differ.

A key tool in compositional semantics is **truth-conditional meaning**: to know the meaning of a sentence is to know under what conditions it would be true. "Snow is white" is true if and only if snow is white. This may seem trivially obvious, but it gives a precise, testable handle on meaning. We can now ask whether sentence A entails sentence B — does B have to be true in every situation where A is true? "Fido is a dog" entails "Fido is an animal," because there is no possible situation in which the first is true and the second is false. Entailment is strictly logical: it holds necessarily, in virtue of meaning alone, not just in most cases.

**Presuppositions** are a subtler phenomenon. They are background assumptions that a sentence takes for granted rather than asserts. "My sister stopped going to the gym" presupposes that my sister was going to the gym before. The diagnostic is negation: negate the sentence ("My sister didn't stop going to the gym") and the presupposition survives — we still assume she had been going. Regular assertions and entailments, by contrast, are cancelled by negation. This survival under negation is what makes presuppositions unusual and worth studying separately.

**Scope ambiguity** shows how syntactic structure and semantic interpretation can come apart. The sentence "Every professor read some student's paper" has two readings: one where a single paper was read by all professors (existential quantifier takes wide scope), and one where each professor read a (possibly different) paper (existential takes narrow scope under the universal). These are genuine differences in logical content. Formal semantics handles them by explicitly representing which quantifier takes scope over which, using tools like lambda calculus or logical form representations.

The reason compositional semantics feels challenging at first is that natural language is extraordinarily efficient — a small vocabulary and grammar generates an infinite range of meanings. The machinery behind that efficiency is what this field makes explicit. As you move into pragmatics, you will discover that truth conditions are only part of the story: what we communicate goes well beyond what we literally say. But compositional semantics gives you the baseline — the literal meaning relative to which all other communicative enrichments operate.
