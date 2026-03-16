---
id: context-update-semantics
title: Context-Update Semantics
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: discourse-representation-theory
  type: hard
- id: formal-pragmatics-context
  type: hard
tags:
- pragmatics
- semantics
- context
stage: advanced
status: draft
---

# Context-Update Semantics

## Core Idea
Context-update semantics views utterance meaning as how utterances change conversational context. Rather than assigning truth values relative to fixed context, it asks: what is the update effect of this utterance? This framework elegantly handles assertions, questions, and imperatives as different context-update types, explaining why presupposition is fundamentally about context change rather than truth-conditional semantics.

## Explainer

From your work in discourse representation theory you know that meaning extends beyond individual sentences — how we interpret an utterance depends on what has been established in the discourse so far. Context-update semantics sharpens this insight into a formal framework. Instead of asking "what proposition does this sentence express?" — the standard truth-conditional move — it asks "what does this sentence *do* to the state of the conversation?" Meaning becomes an operation on context, not an assignment of content to a fixed context.

The key technical notion is the **common ground** — the information mutually accepted by all participants in a conversation. Think of it as a shared whiteboard. When I assert "It's raining," I am not merely expressing a proposition; I am proposing to add that proposition to the whiteboard. If you accept the assertion, the common ground updates. If you reject it, the whiteboard stays the same. This move — treating assertion as a *proposal to update* rather than a *statement of fact* — solves a problem that classical truth-conditional semantics struggles with: it explains why assertion is a speech act, not just a display of information.

**Presupposition** is where context-update semantics becomes particularly powerful. Your prerequisite work in formal pragmatics introduced presupposition as information the speaker takes for granted. In the context-update framework, a presupposition is a *precondition on successful update*: an assertion can only update the common ground if its presuppositions are already part of the common ground. "The King of France is bald" presupposes there is a King of France; if that information isn't on the whiteboard, the update operation fails — not because the proposition is false, but because it cannot even be processed. This explains **presupposition projection** (why presuppositions survive embedding under negation and questions) without any special stipulation.

Questions and imperatives fit naturally into the framework as distinct update types. A question does not add a proposition; it transforms the common ground into an *issue* — an open set of possibilities that the discourse is now tasked with resolving. An imperative updates a different dimension of context: the set of obligations on the addressee. This **multidimensional** view of context — tracking facts, issues, and commitments simultaneously — unifies speech act theory with formal semantics, explaining diverse utterance types through a single principle: every utterance is a context-change instruction, differing in *which* dimension of context it targets and *how* it transforms it.
