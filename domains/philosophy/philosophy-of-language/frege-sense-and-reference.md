---
id: frege-sense-and-reference
title: Frege's Sense and Reference
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: meaning-and-reference-basics
  type: hard
builds-toward:
- russell-definite-descriptions
- kripke-causal-theory-naming
- wittgenstein-tractatus-picture-theory
tags:
- sense
- reference
- Frege
- Bedeutung
stage: abstract-reasoning
status: draft
---

# Frege's Sense and Reference

## Core Idea
Frege argued that linguistic expressions have both a sense (Sinn) and a reference (Bedeutung). The sense is the mode of presentation—the conceptual content that determines which object is referred to—while the reference is the object itself. Two expressions can have the same reference but different senses, explaining how 'morning star' and 'evening star' differ in meaning despite referring to the same planet.

## How It's Best Learned
Work through the morning star / evening star example and other identity puzzles to see why simple reference theories fail. Then study how Frege's distinction solves them.

## Common Misconceptions
Sense is just what the speaker means—sense is the objective, language-determined mode of presentation, not individual psychology. Reference requires a complete description—Frege allowed incomplete descriptions to have sense.

## Questions

```yaml
- question: "Which scenario best illustrates Frege's distinction between sense and reference?"
  type: multiple-choice
  options:
    - "Two different speakers have different mental images when they hear 'Venus' — showing that meaning varies by individual psychology"
    - "'The morning star' and 'the evening star' refer to the same planet but present it via different modes — explaining why learning they pick out the same object is genuinely informative"
    - "'Venus' and 'planet' have different references, showing that different words pick out different objects"
    - "The word 'Venus' has both a sound (Sinn) and a planet it refers to (Bedeutung)"
  answer: 1
  explanation: "Option B captures the core of Frege's theory: two expressions share the same reference (Venus) but have different senses (modes of presentation), which explains why the identity 'Hesperus is Phosphorus' is informative rather than trivially true. Option A is the view Frege explicitly rejected — sense is objective and public, not individual psychology. Option D confuses sound/form with sense."

- question: "According to Frege, what is the reference of a declarative sentence?"
  type: multiple-choice
  options:
    - "The thought or proposition the sentence expresses"
    - "The objects named by the nouns in the sentence"
    - "Its truth value — True or False"
    - "The speaker's communicative intention in uttering it"
  answer: 2
  explanation: "Frege extended the sense/reference distinction to whole sentences: the sense of a sentence is the thought (proposition) it expresses, while the reference is its truth value. Two sentences can express different thoughts but have the same reference (both true, or both false). This architecture — sense determines reference at every level — is foundational to formal semantic theory."

- question: "On Frege's view, 'Hesperus is Phosphorus' is informative in a way that 'Hesperus is Hesperus' is not, even though both sentences are true."
  type: true-false
  answer: true
  explanation: "This is Frege's central motivating puzzle. Both names refer to Venus, yet the first sentence ('Hesperus is Hesperus') is a trivial logical truth knowable without any empirical investigation, while 'Hesperus is Phosphorus' was a genuine astronomical discovery. Frege explains this by appeal to sense: the two names have different modes of presentation, so the identity statement makes a non-trivial claim about the world."

- question: "For Frege, the sense of a term is the set of beliefs or mental images that an individual speaker associates with it when using the word."
  type: true-false
  answer: false
  explanation: "Frege explicitly held that sense is objective and public — it belongs to the language, not to individual psychology. Two competent speakers using the same expression share the same sense even if their private mental associations differ. This objectivity is essential to Frege's project: if sense were merely psychological, there would be no basis for saying speakers communicate the same thought."

- question: "Explain why a pure reference theory of meaning — where the meaning of a name just is its referent — cannot account for the informativeness of 'Hesperus is Phosphorus.' How does Frege's sense/reference distinction solve this problem?"
  type: short-answer
  answer: "On a pure reference theory, 'Hesperus' and 'Phosphorus' both refer to Venus, so the sentence expresses the same thing as 'Venus is Venus' — a trivial logical truth. But that misses the cognitive significance: the identity was a genuine discovery. Frege solves this by introducing sense as the mode of presentation. The two names have different senses (one presents Venus as the evening star, the other as the morning star), so the identity claims that two distinct modes of presentation lead to the same object — a non-trivial, empirically discoverable fact."
  explanation: "The key move is that identity statements are not just about objects but about how those objects are presented. Informative identity statements connect two different conceptual routes to the same destination. This is why sense must be distinguished from reference: reference alone cannot explain cognitive significance."
```

## Explainer

From your study of meaning and reference basics, you understand that words and phrases point to things in the world — a name like "Mount Everest" picks out the mountain, and a predicate like "is tall" picks out a property. A simple **reference theory** of meaning says that the meaning of a name just is its referent — the object it picks out. This theory is attractive in its economy, but Frege identified a problem that forces a more complex picture: identity statements can be informative, and a pure reference theory cannot explain why.

Consider: "Hesperus is Hesperus" versus "Hesperus is Phosphorus." Both statements are true, and both names — Hesperus (the evening star) and Phosphorus (the morning star) — turn out to refer to the same object: the planet Venus. On a pure reference theory, both sentences express the same thing — the identity of Venus with itself — and therefore should have the same cognitive value. But they do not. "Hesperus is Hesperus" is trivially true, knowable by logic alone. "Hesperus is Phosphorus" was a genuine astronomical discovery. Learning it tells you something about the world. How can two sentences with the same reference have different cognitive significance?

Frege's solution is to distinguish **sense (Sinn)** from **reference (Bedeutung)**. The reference of a term is the object it picks out. The sense is the **mode of presentation** — the conceptual route by which the reference is determined. "Hesperus" and "Phosphorus" have the same reference (Venus) but different senses: one presents Venus as the bright object visible in the evening sky, the other as the bright object visible in the morning sky. The identity statement "Hesperus is Phosphorus" is informative precisely because it tells you that two different modes of presentation lead to the same object. This is a fact about the world that could not be known from the senses alone.

Frege extended the distinction beyond names to whole sentences. The **reference of a sentence** is its truth value (True or False). The **sense of a sentence** is the thought or proposition it expresses — the condition the world must satisfy for the sentence to be true. Two sentences can express the same thought with different wording, or two sentences can share a truth value without expressing the same thought. This architecture — sense determines reference, reference is what sense presents — becomes the backbone of formal semantic theory.

An important clarification: sense is not the same as what a particular speaker happens to have in mind when they use a word. Frege insisted that sense is **objective and public** — it belongs to the language, not to individual psychology. This is why the theory is not simply about speakers' intentions but about the semantic structure of language itself. The distinction between sense and reference sets up the central questions that Russell, Kripke, and later philosophers of language will contest: Are senses descriptive? Can names have sense without description? Could reference be fixed by causal chains rather than by sense? You will engage these questions directly as you build toward Kripke's causal theory of naming.
