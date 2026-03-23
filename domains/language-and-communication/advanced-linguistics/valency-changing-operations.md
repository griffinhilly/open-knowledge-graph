---
id: valency-changing-operations
title: Valency-Changing Operations
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: argument-structure-thematic-roles
  type: hard
- id: derivational-morphology
  type: hard
tags:
- morphology
- argument-structure
stage: expert
status: draft
---

# Valency-Changing Operations

## Core Idea
Valency-changing operations like passivization, causativization, and applicatives alter predicate argument structure. Passivization demotes agents and promotes objects; causativization adds external causers; applicatives add beneficiaries. These operations are often expressed morphologically and illuminate the lexical-syntactic structure of predicates, showing that argument structure is not fixed but systematically transformable through dedicated operations.

## Questions

```yaml
- question: "In Turkish, an intransitive verb meaning 'the ice melted' becomes 'she melted the ice' by adding a causativization suffix. What has changed about the verb's argument structure?"
  type: multiple-choice
  options:
    - "The Theme argument (ice) was replaced by an Agent (she), leaving the total valency unchanged"
    - "An external Causer (she) was added while the original Theme (ice) was preserved, increasing valency by one"
    - "The event changed from spontaneous melting to a different event of controlled heating"
    - "The verb acquired passive morphology, which demoted the original subject to an oblique"
  answer: 1
  explanation: "Causativization adds a Causer without replacing any existing argument. The original Theme (ice) remains a participant; a new Causer (she) is added as the external instigator of the event. Valency increases by one. The event described is still melting — the same physical process — now with an added external cause. This is the signature of causativization: valency increase by adding specifically a Causer, not just any participant."

- question: "Passivizing 'The thief broke the window' yields 'The window was broken by the thief.' What happens to the Agent argument?"
  type: multiple-choice
  options:
    - "The Agent is eliminated from the sentence's meaning — in the passive, there is no agent"
    - "The Agent is promoted to an additional grammatical object alongside the Theme"
    - "The Agent is demoted from obligatory subject to an optional oblique (the by-phrase), which can be suppressed entirely"
    - "The Agent and Theme swap positions with no change in their semantic or grammatical prominence"
  answer: 2
  explanation: "Passivization demotes — it does not eliminate — the Agent. The Agent moves from obligatory subject position to an optional by-phrase ('by the thief') that can be omitted: 'The window was broken.' The event and its participants remain the same; only the mapping from semantic roles to grammatical positions has changed. The Theme is promoted to subject. This is why passivization reduces apparent valency: the Agent becomes optional, no longer an obligatory argument."

- question: "A valency-changing operation can produce a sentence describing the same event as the base sentence but with a different number of grammatical arguments."
  type: true-false
  answer: true
  explanation: "This is the defining property of valency-changing operations. Passivization produces the same event with the Agent demoted/optional (apparent decrease in valency). Causativization produces the same type of event with an added Causer (valency increase). The event type — breaking, melting, giving — is not changed; what changes is the grammatical projection of participants. Same semantic event, different argument structure configurations."

- question: "When a sentence is passivized, the event being described changes — the passive describes an event in which no agent caused the action."
  type: true-false
  answer: false
  explanation: "'The window was broken by the thief' describes the exact same event as 'The thief broke the window' — the same thief, the same window, the same breaking. Passivization is a structural operation that reorganizes the grammatical projection of participants (who is subject, who is oblique) without changing the underlying semantic event. Even when the by-phrase is omitted ('The window was broken'), there is still an implied agent; the passive merely renders it optional rather than eliminating it from the meaning."

- question: "Explain the two-layer architecture of argument structure and how valency-changing operations work within it."
  type: short-answer
  answer: "Argument structure has two layers: (1) the underlying semantic structure — who does what to whom, which participants the event requires — and (2) the grammatically projected structure — which participants are encoded as subject, object, or oblique in the syntax. Valency-changing operations manipulate the mapping between these layers, not the semantic layer itself. Passivization keeps the same participants but reassigns their grammatical roles (Theme → subject, Agent → optional oblique). Causativization adds a new semantic participant (Causer) and maps it to subject. The event stays constant; the grammatical packaging changes."
  explanation: "This two-layer view predicts that valency-changing operations should be compositional: you can passivize a causative ('The ice was melted by her') because the same architecture applies at each step. It also explains why languages encode these operations morphologically — the verb's morphology signals which valency operation has applied, helping listeners recover which semantic participant maps to each grammatical position. The cross-linguistic prevalence of these operations (passives, causatives, and applicatives appear in unrelated language families) suggests they reflect something deep about how humans conceptualize and grammatically encode events."
```

## Explainer

From argument structure and thematic roles, you know that verbs come with a fixed set of participants they require — the verb *give* demands a Giver, a Recipient, and a Given-thing; *break* needs an Agent (optionally) and a Theme. This argument structure is stored in the lexicon as part of the verb's meaning. Valency-changing operations are the grammatical machinery that alters this stored structure in principled ways, either adding, removing, or reorganizing participants without changing the core event being described.

**Passivization** is the most familiar example and the clearest illustration of the logic. Take *The thief broke the window*: Agent (*thief*) and Theme (*window*), with Agent as grammatical subject. Passivize it: *The window was broken (by the thief)*. The event is the same; the arguments are the same; but the Theme has been promoted to subject position and the Agent has been either demoted to an optional *by*-phrase or suppressed entirely. The **valency** — the number of obligatory arguments — effectively decreases: in the passive, the Agent can be omitted, whereas in the active it typically cannot be. Passive morphology is the surface signal that this structural reorganization has occurred. Languages vary enormously in how they encode this: English uses an auxiliary (*was*) plus a participial form; Latin uses morphological endings on the verb; many languages use a reflexive clitic.

**Causativization** works in the opposite direction — it adds a participant rather than demoting one. The verb *melt* is intransitive in *The ice melted* (just one argument, the Theme). Causativize it: *She melted the ice*. Now there's an Agent (*she*) who caused the melting, plus the original Theme. The **valency increases** by one. Many languages encode this morphologically: in Japanese, adding the suffix *-sase* to a verb causativizes it, and in Turkish, *-dır/-tır* serves a similar function. What makes this theoretically important is that causativization doesn't simply add any participant — it adds specifically a **causer** who stands outside the original event and brings it about. The morphology tracks a semantic relationship, not just an extra noun.

**Applicatives** add yet another type of participant: a beneficiary, instrument, location, or goal that would otherwise be expressed as an oblique or adjunct. In English, *She baked him a cake* is a dative alternation — *him* is semantically a Recipient but syntactically an object. In languages with applicative morphology (many Bantu languages, Quechua, some Mesoamerican languages), a dedicated affix on the verb promotes an oblique participant into the core argument structure, giving it direct object properties like agreement and case. This matters because it shows that what counts as a "core argument" is not just a semantic question — it's a language-specific grammatical choice that morphology can modulate.

The unifying insight across all three operations is that argument structure is **two-layered**: there is the underlying semantic structure (who did what to whom), and there is the grammatically projected structure (which participants are subjects, objects, or obliques). Valency-changing operations manipulate the mapping between these layers. This view predicts that you can have a single semantic event — breaking, melting, giving — realized with different grammatical argument configurations depending on which morphological operations have applied. It also predicts that these operations should interact systematically: you can passivize a causative (*The ice was melted by her*) because the same layered architecture applies at each step. Recognizing these operations is essential for analyzing any language with rich verbal morphology.
