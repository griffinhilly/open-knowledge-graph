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

## Questions

```yaml
- question: "Consider the sentence 'John ran quickly in the park.' In a purely propositional semantics without event variables, what specific logical problem arises when trying to prove that this sentence entails 'John ran'?"
  type: multiple-choice
  options:
    - "The quantifier over John creates a scope ambiguity that blocks the entailment derivation"
    - "'Ran-quickly-in-the-park' and 'ran' are treated as completely separate, unrelated predicates with no logical connection, so the entailment from the longer sentence to the shorter one cannot be formally derived"
    - "Propositional semantics cannot represent manner adverbs like 'quickly' at all — they are syntactically uninterpretable"
    - "The tense of the verb creates a temporal reference problem that prevents cross-sentence entailment"
  answer: 1
  explanation: "In propositional semantics, 'John ran quickly in the park' would be formalized as something like ran-quickly-in-the-park(john). This is a single atomic predicate completely distinct from ran(john). There is no logical mechanism to derive 'John ran' from it — you would need a stipulated axiom for every combination of adverbs. Event semantics solves this by making adverbs separate conjuncts over a shared event variable: ∃e[run(e) ∧ agent(e,j) ∧ quick(e) ∧ in(e,park)]. Dropping any conjunct (including both adverbs) yields ∃e[run(e) ∧ agent(e,j)], which is 'John ran.'"

- question: "In a neo-Davidsonian analysis, how is the passive sentence 'Mary was seen' derived semantically, without positing a separate passive lexical entry for 'be seen'?"
  type: multiple-choice
  options:
    - "The agent and patient arguments are swapped in the verb's argument structure, reversing the thematic roles"
    - "The agent conjunct is suppressed or existentially closed while the event predicate and patient role conjunct remain intact — passivization is a syntactic operation on the event representation, not a lexical change to the verb"
    - "The event variable is bound to a different temporal index in passive constructions, creating the interpretation of a past-directed state"
    - "A separate passive morpheme introduces a new lambda abstraction over the agent argument, effectively canceling the agent role"
  answer: 1
  explanation: "In neo-Davidsonian event semantics, the active 'X saw Mary' is ∃e[see(e) ∧ agent(e,X) ∧ patient(e,mary)]. The passive 'Mary was seen' simply suppresses the agent conjunct (or binds it existentially), leaving ∃e[see(e) ∧ patient(e,mary)]. Since agent and patient are separate conjuncts — not embedded in the verb — this operation is straightforward and requires no new lexical item. This is one of neo-Davidsonian event semantics' major explanatory wins: a uniform account of the active-passive alternation without lexical redundancy."

- question: "In Davidsonian event semantics, adverbs such as 'quickly' and 'in the park' are predicates over the event variable — they add information about the event itself rather than modifying the verb predicate or operating on the proposition."
  type: true-false
  answer: true
  explanation: "This is the central move of the Davidsonian analysis. Instead of treating 'quickly' as an operator on the predicate (ran → ran-quickly) or on the proposition (P → quickly-P), Davidson treats it as a conjunct predicate over the same event variable: ∃e[run(e) ∧ agent(e,j) ∧ quick(e)]. This makes all adverbs logically uniform — they are all predications over events — and immediately explains why stripping any adverb yields a valid entailment: you simply drop a conjunct from a conjunction."

- question: "The primary motivation for introducing event variables into semantic representations is to handle quantification over individuals — standard predicate logic lacks the expressive power to represent who performed an action without an event argument."
  type: true-false
  answer: false
  explanation: "Standard predicate logic handles individual quantification perfectly well — 'John ran' is simply run(john), and 'someone ran' is ∃x[run(x)]. The motivation for event variables is entirely different: it is the problem of adverbial modification and the entailment patterns that come with it. Without event variables, there is no way to formally derive that 'John ran quickly' entails 'John ran,' or to give a unified account of passivization and nominalization. The event variable is introduced to give adverbs a logical argument position, not to help with individual quantification."

- question: "Explain why the introduction of an event variable solves the problem of adverbial entailment. What can be derived with event variables that cannot be derived from a purely propositional (no-event) representation?"
  type: short-answer
  answer: "Without event variables, 'ran-quickly-in-the-park(john)' and 'ran(john)' are unrelated atomic predicates — there is no logical operation that derives the second from the first. With event variables, 'John ran quickly in the park' is ∃e[run(e) ∧ agent(e,j) ∧ quick(e) ∧ in(e,park)], a conjunction of predications over a shared event e. Each conjunct is independent, so dropping any subset yields a valid entailment: ∃e[run(e) ∧ agent(e,j)] follows by existential instantiation plus simplification of a conjunction. The event variable is the shared argument that links all the adverbial modifiers to the same event — it gives 'quickly' and 'in the park' a logical home without requiring them to be fused into the verb predicate."
  explanation: "The key mechanism is existential generalization over conjunctions: if P ∧ Q is true, P is true. By making adverbs conjuncts rather than predicate modifiers, event semantics turns adverbial entailment into a trivial theorem of propositional logic. This same structure then extends to passivization (drop the agent conjunct) and nominalization (the nominal refers to the same event variable as the corresponding verb)."
```

## Explainer

From your work on semantic types and composition, you know how to build the meaning of a sentence by combining types: a transitive verb is a function from individuals to properties, and applying it to arguments yields a proposition. That approach works cleanly for simple subject-predicate sentences. But it encounters problems as soon as you add adverbs. In the Davidsonian tradition, "John ran quickly in the park" should entail "John ran" — if you strip away the adverbs, the core event persists. In a purely propositional semantics, "ran(john)" and "ran-quickly-in-the-park(john)" are completely separate predicates with no logical relationship. You cannot derive one from the other. **Event semantics** solves this by introducing a new argument slot — the **event variable** — into the logical representation of verbs.

The **Davidsonian analysis** reanalyzes verbs as relations that include an event participant. Instead of "ran(john)" as a two-place predicate, the logical form becomes ∃e[run(e) ∧ agent(e, john)]: there exists an event *e* such that *e* is a running event and John is the agent of *e*. Adverbs become predicates over the same event variable, conjoined to the main predication: "John ran quickly" → ∃e[run(e) ∧ agent(e, john) ∧ quick(e)]. Now the entailment falls out automatically: if ∃e[run(e) ∧ agent(e, john) ∧ quick(e)] is true, then ∃e[run(e) ∧ agent(e, john)] is also true, because you simply drop the conjunct. Adverbs are existential statements about the same event, not modifications of the predicate itself.

The **neo-Davidsonian extension** separates thematic roles entirely from the verb's argument structure. In the original Davidson, "John saw Mary" might still embed the agent and patient directly. In the neo-Davidsonian version, even subject and object are introduced as separate conjuncts: ∃e[see(e) ∧ agent(e, john) ∧ patient(e, mary)]. This modularity pays off for **passivization**: "Mary was seen" simply drops the agent conjunct and promotes the patient — the event predicate and the patient role remain, and the agent is existentially closed or suppressed. The semantics of passives no longer requires a separate lexical entry; it follows from the structure of the event representation.

The same logic extends to **nominalization** — turning verbs into nouns ("the destruction," "the running"). Nominalizations denote the same events as their verbal counterparts, allowing sentences like "The destruction was sudden" to be semantically related to "It was destroyed suddenly" via shared event variables. This also accounts for why "John's destruction of the city" and "the city's destruction" both make reference to the same underlying event with the same participants, even though the surface syntax differs. Event semantics provides a unified account of these relationships that predicate-only semantics cannot. As you proceed to more formal analyses of aspect, aktionsart, and causal structure, the event variable will appear at the center of each analysis.
