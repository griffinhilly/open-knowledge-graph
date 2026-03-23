---
id: proposition-and-semantic-content
title: Propositions and Semantic Content
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: first-order-semantics
  type: hard
- id: philosophy-of-language-intro
  type: soft
- id: first-order-logic-syntax
  type: soft
builds-toward:
- truth-conditions-and-meaning
- compositionality-principle
tags:
- semantics
- propositions
- truth-value
stage: formal-systems
status: validated
---

# Propositions and Semantic Content

## Core Idea
A proposition is the semantic content of a sentence—what it expresses independently of whether anyone utters it. Propositions are primary bearers of truth-value and are distinct from sentences, since different sentences in different languages can express the same proposition. This distinction is fundamental to semantic theory.

## Questions

```yaml
- question: "You say 'I am hungry' and your friend also says 'I am hungry.' Which of the following is true?"
  type: multiple-choice
  options:
    - "You both uttered the same sentence and expressed the same proposition"
    - "You uttered different sentences but expressed the same proposition"
    - "You uttered the same sentence type but expressed different propositions"
    - "You expressed different propositions because you used different words"
  answer: 2
  explanation: "This is the canonical case of indexicality. 'I am hungry' is the same sentence type — the same string of words — but 'I' refers to different people depending on who utters it. Once the referent of 'I' is fixed by context, the resulting propositions differ: one is about you being hungry, the other is about your friend being hungry. These are distinct propositions with potentially different truth values. The same sentence type, different propositions — showing that the sentence-proposition distinction is not a theoretical nicety but required to handle ordinary indexical language."

- question: "Why can't sentences alone serve as the primary bearers of truth value, without introducing propositions?"
  type: multiple-choice
  options:
    - "Sentences are too long to evaluate for truth — propositions are more compact"
    - "Indexical sentences like 'I am here now' have no stable truth value independent of context; we need the context-fixed content (proposition) to assign truth"
    - "Sentences are written or spoken, and truth is a property only of abstract objects"
    - "Propositions are needed because different languages have different numbers of sentences"
  answer: 1
  explanation: "The problem with assigning truth directly to sentences is that indexical sentences like 'I am here now' are always trivially true when uttered but would be false if you moved — the sentence type itself has no fixed truth value. We need the proposition — the content with all context-sensitive expressions filled in — to get a stable truth-bearer. 'I am hungry' said by you right now expresses a proposition with a definite truth condition (you, hungry, now), which can be true or false. The sentence type has no such stability."

- question: "The English sentence 'Snow is white' and the French sentence 'La neige est blanche' express the same proposition."
  type: true-false
  answer: true
  explanation: "This is one of the core motivations for positing propositions as abstract entities distinct from sentences. If truth were a property of sentences (linguistic objects), 'snow is white' would be true in English but the French sentence would be a different thing with different truth conditions. Instead, both sentences express the same abstract content — the proposition that snow is white — which is true independently of which language or sentence is used to express it. This is why propositions are said to be language-independent."

- question: "A single sentence type always expresses exactly one proposition, regardless of context or speaker."
  type: true-false
  answer: false
  explanation: "Indexical expressions — 'I,' 'you,' 'here,' 'now,' 'this,' 'today' — mean that the same sentence type can express different propositions in different contexts. 'I am in Paris' expresses a different proposition when Napoleon utters it versus when you utter it. 'Today is Tuesday' expresses a different proposition on different days. The sentence type is fixed; the proposition varies with context. This is precisely why propositions are theoretically necessary: they are the context-determined semantic contents that result once all context-sensitive expressions are resolved."

- question: "What theoretical work do propositions do that sentences cannot do on their own?"
  type: short-answer
  answer: "Propositions provide stable, context-independent truth-bearers. Sentences — especially those with indexical expressions like 'I,' 'here,' and 'now' — can express different things in different contexts, so they don't have fixed truth values. Propositions are the content that results after all context-sensitive elements are fixed; they are true or false simpliciter. They also explain cross-linguistic synonymy (different sentences, same meaning) and serve as the inputs to logical operators like negation and conjunction."
  explanation: "The proposition is the unit of logical evaluation: 'not P' negates the proposition P, not the sentence 'P'. For logical operators to work, they need inputs that have determinate truth values — sentences with indexicals don't provide this. Propositions also explain why translation preserves meaning: what is preserved across linguistic expression is the proposition, the abstract content. Without propositions (or something playing their theoretical role), semantic theory lacks a stable foundation for truth, logic, and cross-linguistic meaning."
```

## Explainer

From first-order semantics, you have worked with a formal language in which formulas are interpreted over models: a formula like "Fa" is true if the object assigned to "a" falls under the extension assigned to "F." But natural language sentences are not formulas — they are strings of words spoken or written by particular people at particular times. What is it that a sentence expresses, and what makes it true or false? **Propositions** are the theoretical entities introduced to answer this question.

A **proposition** is the abstract content that a sentence expresses — the bearer of truth value that is distinct from any particular sentence, speaker, or occasion of utterance. The English sentence "Snow is white," the French "La neige est blanche," and the German "Schnee ist weiß" are three different sentences, but they all express the same proposition: roughly, the claim that snow is white. The proposition is true if snow is white, false otherwise, and this truth condition holds independently of whether anyone utters it, thinks it, or knows about it. This is why propositions are said to be **abstract entities** — they exist independently of language use, like mathematical objects.

The distinction between sentence and proposition matters immediately for logical and semantic analysis. Two distinct sentence tokens — a sentence written on a chalkboard and the same sentence spoken aloud — express the same proposition. But a single sentence type can express different propositions in different contexts: "I am hungry" expresses a different proposition when you say it versus when I say it, because "I" refers to different people. **Indexical** expressions like "I," "here," "now," and "this" mean that the same sentence type can have different semantic content on different occasions of use. Propositions are the context-independent contents that result once the referents of all context-sensitive expressions are fixed.

Propositions serve a second crucial function: they are what logical operators operate on. "Not P" is true if and only if proposition P is false. "P and Q" is true if and only if both P and Q are true. For these connectives to have determinate meaning, there must be something — propositions — that the logical operators take as inputs and transform into outputs. Your first-order logic syntax gave you the formal machinery; propositions are the semantic objects that the machinery is about.

There is deep disagreement about what propositions actually are. **Russellian propositions** are structured entities that contain the actual objects and properties that sentences are about — so the proposition expressed by "Venus is bright" contains Venus itself as a constituent. **Fregean propositions** (Fregean thoughts) are built from senses rather than referents — they represent the world under modes of presentation. **Possible-worlds propositions** identify a proposition with the set of possible worlds in which it is true, abstracting away from internal structure. Each theory has different consequences for how compositionality works, how we handle empty names, and what it means for two propositions to be the same. These debates are where semantics meets metaphysics — the study of truth conditions builds toward both truth-conditional theories of meaning and the compositional principle that the meaning of complex expressions is determined by the meanings of their parts.
