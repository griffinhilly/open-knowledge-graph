---
id: event-semantics-formal
title: 'Event Semantics: Formal Representation of Eventualities'
domain: language-and-communication
course: linguistics
prerequisites:
- id: semantic-types-and-composition
  type: hard
- id: event-semantics
  type: soft
tags:
- semantics
- events
- formalism
stage: advanced
status: draft
---

# Event Semantics: Formal Representation of Eventualities

## Core Idea
Event semantics treats verbs as predicates over events, not just propositions. Formalized by quantifying over event variables: 'John ran' is ∃e[run(e) ∧ agent(e, john)]. This naturally captures adverbial modification and explains patterns in passivization and nominalization.

## Explainer

From your work on semantic types and composition, you know how to build the meaning of a sentence by combining types: a transitive verb is a function from individuals to properties, and applying it to arguments yields a proposition. That approach works cleanly for simple subject-predicate sentences. But it encounters problems as soon as you add adverbs. In the Davidsonian tradition, "John ran quickly in the park" should entail "John ran" — if you strip away the adverbs, the core event persists. In a purely propositional semantics, "ran(john)" and "ran-quickly-in-the-park(john)" are completely separate predicates with no logical relationship. You cannot derive one from the other. **Event semantics** solves this by introducing a new argument slot — the **event variable** — into the logical representation of verbs.

The **Davidsonian analysis** reanalyzes verbs as relations that include an event participant. Instead of "ran(john)" as a two-place predicate, the logical form becomes ∃e[run(e) ∧ agent(e, john)]: there exists an event *e* such that *e* is a running event and John is the agent of *e*. Adverbs become predicates over the same event variable, conjoined to the main predication: "John ran quickly" → ∃e[run(e) ∧ agent(e, john) ∧ quick(e)]. Now the entailment falls out automatically: if ∃e[run(e) ∧ agent(e, john) ∧ quick(e)] is true, then ∃e[run(e) ∧ agent(e, john)] is also true, because you simply drop the conjunct. Adverbs are existential statements about the same event, not modifications of the predicate itself.

The **neo-Davidsonian extension** separates thematic roles entirely from the verb's argument structure. In the original Davidson, "John saw Mary" might still embed the agent and patient directly. In the neo-Davidsonian version, even subject and object are introduced as separate conjuncts: ∃e[see(e) ∧ agent(e, john) ∧ patient(e, mary)]. This modularity pays off for **passivization**: "Mary was seen" simply drops the agent conjunct and promotes the patient — the event predicate and the patient role remain, and the agent is existentially closed or suppressed. The semantics of passives no longer requires a separate lexical entry; it follows from the structure of the event representation.

The same logic extends to **nominalization** — turning verbs into nouns ("the destruction," "the running"). Nominalizations denote the same events as their verbal counterparts, allowing sentences like "The destruction was sudden" to be semantically related to "It was destroyed suddenly" via shared event variables. This also accounts for why "John's destruction of the city" and "the city's destruction" both make reference to the same underlying event with the same participants, even though the surface syntax differs. Event semantics provides a unified account of these relationships that predicate-only semantics cannot. As you proceed to more formal analyses of aspect, aktionsart, and causal structure, the event variable will appear at the center of each analysis.
