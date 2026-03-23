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
stage: expert
status: draft
---

# Event Semantics and Thematic Structure

## Core Idea
Event semantics treats verbs as predicates over events rather than relations between individuals: 'give' is GIVE(e, x, y, z), where e is an event variable. This approach elegantly explains argument alternations (agent-theme reordering, causative-inchoative pairs) and adverbial modification.

## How It's Best Learned
Analyze argument alternations using event-semantic templates; test how manner, duration, and frequency adverbs interact with event structure.

## Common Misconceptions
Events are not sentences or propositions; they are abstract semantic objects that serve as arguments to predicates and can be quantified over.

## Questions

```yaml
- question: "In standard Montague semantics without event variables, the sentence 'John sang beautifully in the park' creates a problem. Which of the following best describes that problem?"
  type: multiple-choice
  options:
    - "The verb 'sang' cannot take an adverb as a type-theoretic argument in intensional logic"
    - "To capture all the entailments (that John sang, that he sang beautifully, that he sang in the park), one must stipulate an unlimited family of distinct predicates with no principled connection between them"
    - "Adverbs like 'beautifully' lack truth conditions because they express subjective evaluation"
    - "Prepositional phrases are adjuncts and adjuncts carry no semantic content in Montague grammar"
  answer: 1
  explanation: "Without event variables, 'sang beautifully in the park' becomes a single complex predicate SANG-BEAUTIFULLY-IN-THE-PARK(John), which has no principled relationship to SANG(John) or SANG-BEAUTIFULLY(John). To capture all the entailments, you would need an infinite inventory of related predicates with stipulated implication relations between them — and no principled account of why they entail each other. Davidson's event variable solution collapses this: SANG(e) ∧ Agent(e, John) ∧ BEAUTIFULLY(e) ∧ IN-THE-PARK(e), and each entailment follows by conjunction elimination. The adverb problem becomes a straightforward consequence of predicate logic."

- question: "In the neo-Davidsonian framework, the sentences 'The chef melted the butter' and 'The butter melted' share an underlying event structure, differing only in:"
  type: multiple-choice
  options:
    - "The Patient/Theme argument — different objects undergo melting in each sentence"
    - "The presence or absence of a Causer argument — the causative form adds Causer(e, the chef) to the same underlying melting event"
    - "The tense and aspectual structure — the transitive implies completion, the intransitive implies process"
    - "The thematic role assigned to 'butter' — it is a Theme in the intransitive but a Patient in the causative"
  answer: 1
  explanation: "This is the causative-inchoative alternation. Both sentences describe a melting event MELT(e) with Theme(e, the butter). The causative form adds Causer(e, the chef) to an event structure that is otherwise shared. In the neo-Davidsonian representation — where thematic roles are separate predicates rather than fixed argument positions — this addition or removal of a role is a systematic operation, not a stipulated lexical alternation. The insight is that what appears to be two different verbs is actually one event type with a variable argument structure, predicting the alternation rather than listing it."

- question: "In event semantics, adverbs like 'slowly' and 'in the park' are predicates over event variables rather than modifiers of the main verb predicate, which allows adverbial entailments to follow as logical consequences rather than stipulations."
  type: true-false
  answer: true
  explanation: "This is Davidson's core insight. 'John ran slowly in the park' becomes RAN(e) ∧ Agent(e, John) ∧ SLOWLY(e) ∧ IN-THE-PARK(e). The entailment 'John ran slowly' follows by conjunction elimination — drop the IN-THE-PARK(e) conjunct. Without event variables, you have a single complex predicate RAN-SLOWLY-IN-THE-PARK(John) with no sub-parts to eliminate and no principled account of why it implies RAN-SLOWLY(John). The event variable is what transforms an intuition about entailment into a formal consequence."

- question: "Event variables in event semantics are simply a notational shorthand — they do not add semantic content beyond what was expressible in standard Montague semantics without events."
  type: true-false
  answer: false
  explanation: "Event variables are genuine semantic objects with their own expressive power that goes beyond notation. They can be quantified over ('John kissed Mary twice' quantifies over kissing events), referred to by demonstratives ('That surprised me' picks up a previously mentioned event), and located by temporal expressions ('before noon' locates an event in time). None of these constructions are tractable in standard Montague semantics without events. The framework is not a notational variant of what came before — it extends the descriptive range of semantic theory to cover quantification over events, event reference, and temporal modification in a principled way."

- question: "Why does the neo-Davidsonian decomposition of thematic roles into separate predicate positions provide a better account of argument alternations than the original Davidsonian representation?"
  type: short-answer
  answer: "In the original Davidsonian representation, GIVE(e, x, y, z) bundles Agent, Theme, and Goal into fixed argument positions. To handle alternations like passivization or ditransitive variants, separate lexical entries with stipulated relationships would be needed. In the neo-Davidsonian version — GIVE(e) ∧ Agent(e, x) ∧ Theme(e, y) ∧ Goal(e, z) — each thematic role is an independent predicate that can be suppressed, demoted, or rearranged. Passivization suppresses the Agent predicate from surface syntax while leaving the event structure intact. The causative adds a Causer predicate to an otherwise unchanged event. These become systematic operations rather than language-specific stipulations."
  explanation: "The separability of thematic roles is not just a formal nicety — it makes testable predictions. If roles are truly independent, we expect the same role to behave similarly across different verbs and alternations, and we expect the suppression or addition of a role to have consistent syntactic effects across the lexicon. This transforms what was a collection of observed alternations into derived predictions of a principled theory, which is the mark of genuine theoretical progress in semantics."
```

## Explainer

From Montague semantics, you know how to build truth conditions compositionally: verbs denote functions from individuals to truth values, and sentences like "John runs" are analyzed as RUN(j). From your study of argument structure, you know that thematic roles — **Agent**, **Patient**, **Theme**, **Goal**, etc. — describe the semantic relationship between a verb and its arguments. Event semantics builds directly on both, solving a problem neither framework handles cleanly on its own: how do adverbs and adjuncts modify verb meanings?

The problem, as Donald Davidson posed it in 1967, is this: "John ran slowly in the park" seems to entail "John ran" and "John ran slowly" and "John ran in the park." In standard Montague semantics, where "ran slowly in the park" is a complex predicate, these entailments require an infinite family of related predicates with no principled connection. Davidson's solution was to introduce an **event variable** *e* as an implicit argument of every verb: RAN(e, John), SLOWLY(e), IN-THE-PARK(e). Adverbs become predicates over events, and the entailments follow by existential instantiation — if all three hold of *e*, then there exists an *e* satisfying each individually. The adverb problem dissolves because "slowly" and "in the park" are not modifying the predicate but predicating something of the same event.

The **neo-Davidsonian** extension, associated with Parsons and Kratzer, separates thematic roles into their own predicate positions: instead of GIVE(e, x, y, z), you get GIVE(e) ∧ Agent(e, x) ∧ Theme(e, y) ∧ Goal(e, z). This decomposition, which your knowledge of thematic roles from argument structure makes immediately interpretable, is not just notational — it provides an elegant account of **argument alternations**. The causative-inchoative alternation ("The chef melted the butter" / "The butter melted") can be analyzed as the causative form adding a Causer argument to an event that is present in both. The passive transformation drops the Agent position from the surface syntax while keeping the underlying event structure intact. Argument structure alternations, which previously required language-specific stipulations, become systematic predictions of the event-semantic framework.

What makes this framework powerful is that **events are first-class semantic objects** — they can be quantified over, referred to by pronouns, and modified by temporal expressions. "John kissed Mary twice" quantifies over kissing events. "That surprised me" refers back to a previously mentioned event. "Before noon" locates an event in time. All of this becomes tractable once you have event variables in your semantic representations. The key skill is learning to read natural language sentences and identify the implicit event structure: every dynamic verb introduces an event variable, and every adjunct is a predicate over that variable. Once you see sentences this way, the compositional structure becomes transparent — and the intuitive entailments fall out as logical consequences rather than stipulations.
