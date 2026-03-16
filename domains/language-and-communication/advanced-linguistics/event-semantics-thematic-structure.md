---
id: event-semantics-thematic-structure
title: Event Semantics and Thematic Structure
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: montague-semantics
  type: hard
- id: argument-structure-thematic-roles
  type: hard
tags:
- semantics
- events
- argument-structure
stage: advanced
status: draft
---

# Event Semantics and Thematic Structure

## Core Idea
Event semantics treats verbs as predicates over events rather than relations between individuals: 'give' is GIVE(e, x, y, z), where e is an event variable. This approach elegantly explains argument alternations (agent-theme reordering, causative-inchoative pairs) and adverbial modification.

## How It's Best Learned
Analyze argument alternations using event-semantic templates; test how manner, duration, and frequency adverbs interact with event structure.

## Common Misconceptions
Events are not sentences or propositions; they are abstract semantic objects that serve as arguments to predicates and can be quantified over.

## Explainer

From Montague semantics, you know how to build truth conditions compositionally: verbs denote functions from individuals to truth values, and sentences like "John runs" are analyzed as RUN(j). From your study of argument structure, you know that thematic roles — **Agent**, **Patient**, **Theme**, **Goal**, etc. — describe the semantic relationship between a verb and its arguments. Event semantics builds directly on both, solving a problem neither framework handles cleanly on its own: how do adverbs and adjuncts modify verb meanings?

The problem, as Donald Davidson posed it in 1967, is this: "John ran slowly in the park" seems to entail "John ran" and "John ran slowly" and "John ran in the park." In standard Montague semantics, where "ran slowly in the park" is a complex predicate, these entailments require an infinite family of related predicates with no principled connection. Davidson's solution was to introduce an **event variable** *e* as an implicit argument of every verb: RAN(e, John), SLOWLY(e), IN-THE-PARK(e). Adverbs become predicates over events, and the entailments follow by existential instantiation — if all three hold of *e*, then there exists an *e* satisfying each individually. The adverb problem dissolves because "slowly" and "in the park" are not modifying the predicate but predicating something of the same event.

The **neo-Davidsonian** extension, associated with Parsons and Kratzer, separates thematic roles into their own predicate positions: instead of GIVE(e, x, y, z), you get GIVE(e) ∧ Agent(e, x) ∧ Theme(e, y) ∧ Goal(e, z). This decomposition, which your knowledge of thematic roles from argument structure makes immediately interpretable, is not just notational — it provides an elegant account of **argument alternations**. The causative-inchoative alternation ("The chef melted the butter" / "The butter melted") can be analyzed as the causative form adding a Causer argument to an event that is present in both. The passive transformation drops the Agent position from the surface syntax while keeping the underlying event structure intact. Argument structure alternations, which previously required language-specific stipulations, become systematic predictions of the event-semantic framework.

What makes this framework powerful is that **events are first-class semantic objects** — they can be quantified over, referred to by pronouns, and modified by temporal expressions. "John kissed Mary twice" quantifies over kissing events. "That surprised me" refers back to a previously mentioned event. "Before noon" locates an event in time. All of this becomes tractable once you have event variables in your semantic representations. The key skill is learning to read natural language sentences and identify the implicit event structure: every dynamic verb introduces an event variable, and every adjunct is a predicate over that variable. Once you see sentences this way, the compositional structure becomes transparent — and the intuitive entailments fall out as logical consequences rather than stipulations.
