---
id: temporal-semantics-and-tense
title: Temporal Semantics and Linguistic Tense
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: first-order-semantics
  type: hard
- id: possible-worlds-semantics
  type: soft
- id: temporal-logic
  type: soft
builds-toward:
  - anaphora-and-discourse-dynamics
tags:
- temporality
- tense
- aspect
- semantics
stage: advanced
status: draft
---
# Temporal Semantics and Linguistic Tense

## Core Idea
Temporal expressions and tense require a semantic framework treating time as an additional dimension. Tense can be analyzed as quantification over times or as context-dependent reference to utterance time, and interacts with aspect and modality in complex ways.

## Explainer

Natural language is saturated with temporal information: verbs are marked for tense, sentences carry aspect, and time adverbials locate events precisely. Temporal semantics asks how this information is encoded in meaning. From your study of first-order semantics, you know that truth conditions for simple sentences relate predicates to objects at a world. Adding temporal dimensions means extending those truth conditions to include **times** as an additional evaluation parameter — sentences are no longer just true or false at a world, but true or false at a world *and a time*.

The simplest approach treats **tense as quantification over times**. "It rained" means roughly: there is a time t such that t is before the utterance time, and it rained at t. The **utterance time** — when the sentence is spoken or written — becomes a context parameter. Past tense existentially quantifies over times before the utterance; future tense quantifies over times after it. This connects naturally to your background in temporal logic, where the operators P (it was the case that) and F (it will be the case that) function as temporal quantifiers, and the compositional semantics unpacks them accordingly.

A richer framework introduces Reichenbach's three-way distinction: **Speech Time** (S), **Reference Time** (R), and **Event Time** (E). Simple past ("she left") places the event before speech: E before S. But the past perfect ("she had left") adds a layer: an event before a reference time, which is itself before speech: E before R, R before S. "She had left when he arrived" makes this concrete — her leaving is E, his arriving is R, both before S. This three-way structure explains the systematic behavior of perfect and pluperfect constructions. **Aspect** adds yet another dimension: simple past presents an event as a completed whole ("she left"), while progressive aspect ("she was leaving") presents it as ongoing — an event viewed from the inside rather than from completion. This aspectual distinction affects how temporal adverbials attach and how tenses interact.

Temporal semantics connects most interestingly to **possible worlds semantics** when we consider the future tense. "It will rain tomorrow" — is this simply true or false based on present facts? If all times are equally real (eternalism/B-theory), future-tensed sentences are true or false based on what happens at future times, just as past-tensed sentences are true based on past events. If only the present is real (presentism/A-theory), future tense becomes semantically fraught — what makes a future-tensed claim true if future events don't yet exist? Some analyze future tense as quantifying over a default "most normal" continuation; others analyze it as expressing a kind of epistemic or metaphysical possibility. The relationship between formal temporal semantics and metaphysical theories of time is thus not merely analogical: the formal framework forces metaphysical commitments into the open, making them precise and subject to linguistic evidence.

