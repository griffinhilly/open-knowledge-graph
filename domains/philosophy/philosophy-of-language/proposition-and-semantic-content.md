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
stage: advanced
status: draft
---

# Propositions and Semantic Content

## Core Idea
A proposition is the semantic content of a sentence—what it expresses independently of whether anyone utters it. Propositions are primary bearers of truth-value and are distinct from sentences, since different sentences in different languages can express the same proposition. This distinction is fundamental to semantic theory.

## Explainer

From first-order semantics, you have worked with a formal language in which formulas are interpreted over models: a formula like "Fa" is true if the object assigned to "a" falls under the extension assigned to "F." But natural language sentences are not formulas — they are strings of words spoken or written by particular people at particular times. What is it that a sentence expresses, and what makes it true or false? **Propositions** are the theoretical entities introduced to answer this question.

A **proposition** is the abstract content that a sentence expresses — the bearer of truth value that is distinct from any particular sentence, speaker, or occasion of utterance. The English sentence "Snow is white," the French "La neige est blanche," and the German "Schnee ist weiß" are three different sentences, but they all express the same proposition: roughly, the claim that snow is white. The proposition is true if snow is white, false otherwise, and this truth condition holds independently of whether anyone utters it, thinks it, or knows about it. This is why propositions are said to be **abstract entities** — they exist independently of language use, like mathematical objects.

The distinction between sentence and proposition matters immediately for logical and semantic analysis. Two distinct sentence tokens — a sentence written on a chalkboard and the same sentence spoken aloud — express the same proposition. But a single sentence type can express different propositions in different contexts: "I am hungry" expresses a different proposition when you say it versus when I say it, because "I" refers to different people. **Indexical** expressions like "I," "here," "now," and "this" mean that the same sentence type can have different semantic content on different occasions of use. Propositions are the context-independent contents that result once the referents of all context-sensitive expressions are fixed.

Propositions serve a second crucial function: they are what logical operators operate on. "Not P" is true if and only if proposition P is false. "P and Q" is true if and only if both P and Q are true. For these connectives to have determinate meaning, there must be something — propositions — that the logical operators take as inputs and transform into outputs. Your first-order logic syntax gave you the formal machinery; propositions are the semantic objects that the machinery is about.

There is deep disagreement about what propositions actually are. **Russellian propositions** are structured entities that contain the actual objects and properties that sentences are about — so the proposition expressed by "Venus is bright" contains Venus itself as a constituent. **Fregean propositions** (Fregean thoughts) are built from senses rather than referents — they represent the world under modes of presentation. **Possible-worlds propositions** identify a proposition with the set of possible worlds in which it is true, abstracting away from internal structure. Each theory has different consequences for how compositionality works, how we handle empty names, and what it means for two propositions to be the same. These debates are where semantics meets metaphysics — the study of truth conditions builds toward both truth-conditional theories of meaning and the compositional principle that the meaning of complex expressions is determined by the meanings of their parts.
