---
id: indexicals-context-sensitivity
title: Indexicals and Context-Sensitive Expressions
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: meaning-and-reference-basics
  type: hard
builds-toward:
- pragmatics-semantics-boundary
- compositionality-principle
tags:
- indexicals
- context-sensitivity
- reference
- semantics
stage: abstract-reasoning
status: validated
---

# Indexicals and Context-Sensitive Expressions

## Core Idea
Indexical expressions like 'I,' 'now,' 'here,' 'that,' and tense change their reference depending on context—who is speaking, when, where, etc. The semantic content of 'I am hungry' depends on who is speaking. Context-sensitive expressions pose a challenge to truth-conditional semantics: the truth-condition of an indexical utterance cannot be specified without reference to context. Yet indexicals are central to natural language.

## How It's Best Learned
Analyze indexicals systematically: what do they refer to? How is reference determined? How do they interact with tense, modality, and other operators? Distinguish character (context-invariant rule) from content (reference fixed by context).

## Common Misconceptions
Indexicals are special or marginal—they are pervasive (all utterances involve a context of utterance). Context is merely psychological—context is partly objective (facts about speakers, times, places) and partly determined by the conversation.

## Explainer

From your work on **meaning and reference**, you know that the meaning of an expression is connected to what it picks out in the world. But some expressions work differently: their reference is not fixed by a stable descriptive content but shifts systematically with who uses them, when, and where. These are **indexical** expressions — "I," "you," "here," "now," "today," "this," and grammatical tense — and understanding them requires distinguishing two layers of meaning that a single expression carries simultaneously.

David Kaplan introduced the crucial distinction between **character** and **content**. The **character** of an indexical is its context-invariant rule for determining reference: the rule for "I" is always "the agent of the context" — whoever is speaking. This rule is the same no matter who uses "I." The **content** (or **semantic value**) is what the expression contributes to the proposition expressed on a particular occasion: when I say "I am hungry," the content is me specifically, not the general rule about speakers. Character is like a function; content is the output of that function applied to a particular context.

This two-level structure solves what would otherwise be a puzzle. "I am here now" is trivially true whenever uttered — but it expresses different propositions in different contexts (different speakers, places, and times). The sentence is not analytically true in virtue of meaning alone; rather, its character guarantees that any utterance of it will be true. Kaplan calls such sentences **logically true** in a special sense: true at every context of utterance, though the proposition expressed varies. Contrast this with "The president is at the White House," which has stable content but is not true at every context.

Context-sensitivity goes well beyond the classic indexicals. Many expressions — gradable adjectives like "tall" or "expensive," knowledge attributions, predicates of personal taste — have been argued to be context-sensitive in similar ways, with the context-invariant linguistic meaning underdetermining what proposition is expressed. This makes indexicality not a quirky side phenomenon but a window into the systematic relationship between linguistic meaning, context, and propositional content. The **pragmatics/semantics boundary** — your builds-toward topic — is partly defined by the question of which apparent context-sensitivity is built into linguistic meaning (semantics) and which is a matter of pragmatic enrichment after the fact.

## Questions

```yaml
- question: "Kaplan distinguishes 'character' from 'content' for indexicals. What is the character of the word 'now'?"
  type: short-answer
  answer: "The character of 'now' is the context-invariant rule: 'the time of the context of utterance.' This rule is the same regardless of when 'now' is used. The content, by contrast, is the particular time the utterance occurs — which varies with each use. When I say 'It is raining now' at 3pm on Tuesday, the content contributed by 'now' is 3pm Tuesday; when you say it at 9am on Wednesday, the content is 9am Wednesday. The character is the constant function; the content is the output of that function applied to the specific context."
  explanation: "This two-level analysis is Kaplan's key contribution. It explains how the same word can be fully understood by all competent speakers (they all know the character) while contributing different semantic content to different propositions on different occasions. Character is a property of the linguistic expression type; content is a property of the expression-in-a-particular-context (the token)."

- question: "'I am here now' is true in every context of utterance because its meaning is trivially self-confirming."
  type: true-false
  answer: true
  explanation: "Yes — Kaplan calls such sentences 'logically true' in his technical sense: their character guarantees they will be true at every context of utterance, regardless of what world the context is in. The 'I' always refers to the speaker, 'here' to the speaker's location, and 'now' to the time of utterance — so the proposition expressed (a specific individual is at a specific place at a specific time) will always be true when uttered. However, this is not the same as analytic truth in the traditional sense, since the proposition expressed changes from context to context."
```
