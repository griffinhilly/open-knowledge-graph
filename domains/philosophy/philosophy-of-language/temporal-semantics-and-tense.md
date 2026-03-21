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

## Questions

```yaml
- question: "In the sentence 'She had left when he arrived,' how does Reichenbach's S/R/E framework analyze the temporal structure?"
  type: multiple-choice
  options:
    - "E = her leaving, S = the utterance time, R = absent — the pluperfect only uses two time points"
    - "E = her leaving (before R), R = his arriving (before S), S = utterance time — E before R before S"
    - "R = her leaving, E = his arriving, S = utterance time — R before E before S"
    - "E and R coincide at the time of her leaving, both before S"
  answer: 1
  explanation: "Reichenbach's three-time framework handles the pluperfect by introducing a reference time R distinct from both the event time E and speech time S. 'She had left' places her leaving (E) before a reference point (R); 'when he arrived' establishes that reference point as his arrival; and both precede the speech time (S). The structure is E before R before S. This is what distinguishes the pluperfect from simple past ('she left') which only requires E before S, with R coinciding with E."

- question: "Adding temporal dimensions to first-order semantics means sentences are evaluated at which combination of parameters?"
  type: multiple-choice
  options:
    - "A world and a time — truth is relative to both"
    - "A time only — tense replaces possible-worlds semantics"
    - "A world, a time, and an utterance context — but the utterance context is redundant with the time"
    - "A world only — times are reducible to sets of propositions true at that world"
  answer: 0
  explanation: "Temporal semantics extends standard possible-worlds semantics by adding time as an additional evaluation parameter. A sentence is not simply true or false at a world; it is true or false at a world-time pair (or world-time-context triple when utterance-relative expressions like 'now' or 'yesterday' are involved). This is the core move: treating times as explicit parameters rather than implicit in the description of possible worlds. The utterance context (option C) is not redundant — it provides the anchor point from which tense quantifies forward or backward."

- question: "On a B-theory (eternalist) view of time, future-tensed sentences like 'It will rain tomorrow' can have determinate truth values now."
  type: true-false
  answer: true
  explanation: "B-theory (eternalism) holds that past, present, and future times all equally exist — there is no metaphysically privileged 'now,' only an indexically picked out moment. On this view, future-tensed sentences are made true or false by facts about what happens at future times, just as past-tensed sentences are made true by facts about past times. Truth is relative to a time, but both past and future times are equally real truth-makers. This contrasts with A-theory/presentism, where future times don't yet exist, creating semantic problems for future-tensed claims."

- question: "Past tense in natural language is best analyzed as universally quantifying over all past times — 'it rained' means it rained at every time before the utterance."
  type: true-false
  answer: false
  explanation: "Past tense existentially quantifies over past times, not universally. 'It rained' means there exists some time t before the utterance time such that it rained at t — not that it rained at every past time. Universal quantification ('it always rained') requires explicit marking. This matters because the existential analysis captures the ordinary meaning: 'She left' asserts the existence of a leaving-event at some past time, not that leaving occurred at all past times. The same existential structure applies to future tense: 'It will rain' quantifies over some future time, not all."

- question: "Why does the semantics of the future tense raise metaphysical issues that the past tense does not, and how do B-theory and A-theory respond differently?"
  type: short-answer
  answer: "Past-tensed sentences are uncontroversially about events that have already occurred — past times and events exist (or existed) to serve as truth-makers. Future tense is philosophically fraught because on A-theory (presentism), future events don't yet exist, so there is nothing to make a future-tensed sentence determinately true or false. B-theory avoids this problem by treating future times as equally real as past times, so 'It will rain tomorrow' is made true by what happens at the future time, just as 'It rained yesterday' is made true by the past. A-theorists typically analyze future tense differently — as expressing possibility, probability, or a default continuation — because they lack future truth-makers."
  explanation: "The key insight is that temporal semantics makes metaphysical commitments precise. Once you formalize tense as quantification over times, the question 'what is the domain of that quantification?' forces you to take a position on whether future times exist. The formal framework doesn't resolve the metaphysical debate, but it clarifies exactly what's at stake and makes the competing positions subject to linguistic evidence about how future-tensed sentences actually behave."
```

## Explainer

Natural language is saturated with temporal information: verbs are marked for tense, sentences carry aspect, and time adverbials locate events precisely. Temporal semantics asks how this information is encoded in meaning. From your study of first-order semantics, you know that truth conditions for simple sentences relate predicates to objects at a world. Adding temporal dimensions means extending those truth conditions to include **times** as an additional evaluation parameter — sentences are no longer just true or false at a world, but true or false at a world *and a time*.

The simplest approach treats **tense as quantification over times**. "It rained" means roughly: there is a time t such that t is before the utterance time, and it rained at t. The **utterance time** — when the sentence is spoken or written — becomes a context parameter. Past tense existentially quantifies over times before the utterance; future tense quantifies over times after it. This connects naturally to your background in temporal logic, where the operators P (it was the case that) and F (it will be the case that) function as temporal quantifiers, and the compositional semantics unpacks them accordingly.

A richer framework introduces Reichenbach's three-way distinction: **Speech Time** (S), **Reference Time** (R), and **Event Time** (E). Simple past ("she left") places the event before speech: E before S. But the past perfect ("she had left") adds a layer: an event before a reference time, which is itself before speech: E before R, R before S. "She had left when he arrived" makes this concrete — her leaving is E, his arriving is R, both before S. This three-way structure explains the systematic behavior of perfect and pluperfect constructions. **Aspect** adds yet another dimension: simple past presents an event as a completed whole ("she left"), while progressive aspect ("she was leaving") presents it as ongoing — an event viewed from the inside rather than from completion. This aspectual distinction affects how temporal adverbials attach and how tenses interact.

Temporal semantics connects most interestingly to **possible worlds semantics** when we consider the future tense. "It will rain tomorrow" — is this simply true or false based on present facts? If all times are equally real (eternalism/B-theory), future-tensed sentences are true or false based on what happens at future times, just as past-tensed sentences are true based on past events. If only the present is real (presentism/A-theory), future tense becomes semantically fraught — what makes a future-tensed claim true if future events don't yet exist? Some analyze future tense as quantifying over a default "most normal" continuation; others analyze it as expressing a kind of epistemic or metaphysical possibility. The relationship between formal temporal semantics and metaphysical theories of time is thus not merely analogical: the formal framework forces metaphysical commitments into the open, making them precise and subject to linguistic evidence.

