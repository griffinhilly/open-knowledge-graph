---
id: semantic-linking-to-syntax
title: Semantic Role Linking to Syntax
domain: language-and-communication
course: linguistics
prerequisites:
- id: argument-structure-thematic-roles
  type: hard
- id: lexical-semantics
  type: hard
builds-toward:
- selectional-restrictions
- argument-alternations
tags:
- semantics
- syntax-semantics
- thematic-roles
- linking
stage: formal-systems
status: draft
---

# Semantic Role Linking to Syntax

## Core Idea
Linking rules map thematic roles (agent, patient, goal, location) to syntactic positions. Languages consistently place agents in subject position and patients in object position, though many permit alternations (passives, middles, causatives). Formal linking theory predicts which semantic structures map to which syntactic frames, explaining why some argument alternations exist and others are impossible.

## How It's Best Learned
Compare alternating predicates across languages and note which thematic roles shift positions. Predict ungrammatical alternations using proposed linking rules.

## Explainer

You already know that verbs have **argument structures** — they specify how many participants they require and what thematic roles those participants play. "Give" requires three arguments: a giver (agent), a gift (theme), and a recipient (goal). You also know from lexical semantics that word meanings can be analyzed into structured components. **Linking theory** is where these two strands meet: it asks how a verb's semantic structure determines which syntactic positions its arguments occupy, and why that mapping is so consistent across languages.

The basic **linking generalizations** hold remarkably cross-linguistically. Agents — volitional, causal participants — surface as grammatical subjects. Patients and themes — entities undergoing change — surface as direct objects. Goals and recipients surface as indirect objects or in prepositional phrases. "Maria gave the book to Elena": Maria is agent/subject, the book is theme/object, Elena is goal/oblique. This is not arbitrary convention. It reflects deep regularities in how languages encode causal structure: the initiator of an event occupies the most prominent syntactic position. Knowing the thematic roles lets you predict the syntactic frame before you've seen the sentence.

What makes linking theory explanatory rather than merely descriptive is that it must also account for **argument alternations** — cases where the same verb appears in multiple syntactic frames. Consider "John broke the window" (transitive, agent+patient) versus "The window broke" (intransitive/middle, patient only). The patient surfaces as object in one frame and as subject in the other; the agent is suppressed entirely. Linking rules must predict which alternations are licensed and which aren't. English has a **locative alternation**: "spray paint on the wall" and "spray the wall with paint" are both grammatical. But you cannot say *"pour the glass with water" in the same way. The explanation is in the verb's meaning: "spray" encodes a manner that distributes substance over a surface holistically, which licenses the surface-as-object reading; "pour" does not encode this distribution, so the alternation is blocked.

The deeper principle is that **lexical semantic structure constrains linking**. Verbs that encode causation can suppress their agent (passives, middles). Verbs of motion encode a path, and the path role links to specific positions depending on whether manner or result is foregrounded in the verb's meaning. Once you understand that syntactic frames follow from verb semantics — not from arbitrary memorization — you gain a powerful diagnostic: when a sentence sounds ungrammatical, you can ask which linking principle has been violated, and why the verb's semantic structure doesn't permit the configuration you're trying to build.
