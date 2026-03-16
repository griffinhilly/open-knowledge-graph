---
id: event-semantics
title: Event Semantics
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: montague-semantics
  type: hard
- id: argument-structure-thematic-roles
  type: hard
tags:
- events
- argument-structure
- semantics
stage: advanced
status: draft
---

# Event Semantics

## Core Idea
Event semantics treats sentences as describing events, with participants (agents, patients, etc.) as arguments of event predicates. Rather than verbs directly taking noun phrases as arguments, they take both event variables and nominal arguments. This approach explains verbal modifiers (adverbs), event quantification, and relationships between argument structure and thematic roles—a clean separation between what the verb describes and how participants fill roles.

## How It's Best Learned
Rewrite sentences using explicit event variables (e.g., 'John ate pizza' becomes 'There is an event e such that John eats e and the object of e is pizza'). Compare predictions for adverbial modification and negative quantification.

## Common Misconceptions
- Events are not solely about actions; they include states and processes (sleeping, existing).
- Event semantics does not require events to be accessible to consciousness; all aspectual distinctions invoke events, even imperceptible ones.

## Explainer

From your study of Montague semantics, you know how formal semantics represents sentence meaning using logical formulas. A simple sentence like "John runs" is handled by treating *runs* as a predicate and *John* as its argument: *run(john)*. This is elegant, but it faces a serious problem with adverbial modification. Consider: "John ran quickly in the park." This should entail that "John ran quickly" is true, that "John ran in the park" is true, and that "John ran" is true — each follows logically from the original. But in the standard predicate-logic treatment, you'd need separate predicates (*ran*, *ran-quickly*, *ran-in-the-park*, *ran-quickly-in-the-park*) and axioms connecting them. This proliferates predicates indefinitely and misses the obvious pattern. The entailments should fall out from the logical structure automatically.

**Event semantics**, developed principally by Donald Davidson in 1967, solves this by treating verbs as introducing an implicit **event variable** *e*. Instead of *run(john)*, we get *∃e[run(e) ∧ agent(e, john)]*: "there exists an event *e* such that *e* is a running and John is the agent of *e*." Adverbs then modify the event directly: "quickly" becomes a predicate on the event (*quick(e)*), and "in the park" becomes a locative predicate (*in-park(e)*). The full sentence "John ran quickly in the park" becomes *∃e[run(e) ∧ agent(e, john) ∧ quick(e) ∧ in-park(e)]*. Now the entailments fall out automatically from the conjunction: remove any conjunct and you get a logically weaker but still true statement. No extra axioms needed — logic handles it.

The connection to argument structure and thematic roles — your other prerequisite — is direct. In your study of thematic roles, you learned that verbs assign roles like *agent*, *patient*, *theme*, *goal* to their arguments. Event semantics gives thematic roles their formal home: they become predicates relating participants to the event variable. *agent(e, john)* says John is the agent of event *e*; *patient(e, mary)* says Mary is the patient. This allows a clean separation between the event's basic description (what kind of event it is) and the participants' roles within it. It also explains why the same thematic role (*patient*) appears across different verbs — kicking, hitting, breaking all assign a patient role — because the patient is defined by its relationship to the event variable, not by verb-specific stipulation.

The scope of event semantics extends well beyond action sentences. States (*John is tall*), processes (*John is running*), and achievements (*John won*) all involve events in the technical sense, and **aspectual** distinctions — the difference between *John ran* (completed) and *John was running* (ongoing) — are formally captured through how the event variable is bounded. This is why the misconception that events are only actions matters: if you restrict event variables to actions, you lose the tools needed to handle the full range of verbal meaning. Event semantics is the formal framework that connects the logical structure of sentences to the aspectual and thematic dimensions of meaning that make natural language so expressively rich.
