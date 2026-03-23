---
id: causative-voice-constructions
title: Causative Voice Constructions
domain: language-and-communication
course: linguistics
prerequisites:
- id: valency-changing-operations
  type: hard
- id: argument-structure-thematic-roles
  type: hard
- id: control-and-raising-constructions
  type: soft
tags:
- syntax
- voice
- valency
- morphology
stage: advanced
status: validated
---

# Causative Voice Constructions

## Core Idea
Causative voice adds a causer argument to a predicate, increasing valency: 'break' (intransitive) → 'cause to break' (transitive). Causatives are expressed as morphemes (suffixes, prefixes), periphrastic constructions (verbs like make, have), or special embedded structures, and interact with argument structure and transitivity across languages.

## Questions

```yaml
- question: "Consider the sentences: (A) 'The window broke.' (B) 'The child broke the window.' What has happened to argument structure between A and B?"
  type: multiple-choice
  options:
    - "The subject in A has been promoted to object in B, and the child has been added as a new object"
    - "A new causer argument (the child) has been added as subject; the original subject (the window) has been demoted to object position"
    - "The valency has decreased by one because the causative removes the intransitive reading"
    - "Both sentences have the same valency; only the thematic role of 'window' has changed"
  answer: 1
  explanation: "This is the causative alternation: applying a causative adds one argument (the causer) at the subject position, and demotes the original intransitive subject (the Patient/Theme — the window) to object position. Valency increases from 1 to 2. The window's thematic role as Patient is preserved; what changes is its grammatical position. Option A reverses the direction: promotion/demotion describes what happens in passives, not causatives."

- question: "A linguist describes the Turkish form getir- ('bring,' derived from gel- 'come' via the suffix -t) as a morphological causative. What distinguishes this from the English periphrastic causative 'I made him come'?"
  type: multiple-choice
  options:
    - "The morphological causative increases valency by two; the periphrastic causative increases it by one"
    - "The morphological causative expresses direct causation encoded in the verb itself; the periphrastic uses a separate causative verb and typically implies indirect causation"
    - "They are functionally identical; the distinction is purely a matter of historical development"
    - "Periphrastic causatives are only available in English; morphological causatives are the universal cross-linguistic default"
  answer: 1
  explanation: "The key cross-linguistic distinction is not just structural but semantic: morphological causatives (affixes on the verb) tend to imply direct causation — the causer acts immediately on the event. Periphrastic causatives (make/have/let + infinitive) typically imply indirect causation — the causer acts on the causee, who then performs the action. 'She made him clean the room' implies pressure or instruction; a morphological equivalent would suggest she directed the cleaning more immediately. Option C ignores the semantic distinction; Option D is empirically false."

- question: "A morphological causative typically implies more direct causation than a periphrastic (analytic) causative expressing the same event."
  type: true-false
  answer: true
  explanation: "This is a robust cross-linguistic generalization: periphrastic causatives introduce a full 'causal chain' between causer and event, implying mediation through the causee's action. Morphological causatives, by encoding causation directly in the verb, express a more tight, immediate causal connection. This gradient of directness is also reflected within English periphrastic causatives: 'make' (coercive), 'have' (arranged), and 'let' (permissive) form a scale of decreasing causer control."

- question: "When a causative construction is applied to an intransitive verb, the original subject of that verb remains in the subject position, and the causer is added as a new object."
  type: true-false
  answer: false
  explanation: "The opposite is true: the causer is introduced at the subject position (it is the new, higher-ranked argument), and the original intransitive subject is demoted to object position. For example: 'The ice melted' (intransitive; ice = subject) → 'The heat melted the ice' (causative; heat = causer/subject, ice = object). The causer always occupies the highest argument position because it is the external initiator of the event."

- question: "What happens to argument structure when a causative construction is applied to a transitive verb? Use an example to illustrate."
  type: short-answer
  answer: "Applying a causative to a transitive verb increases valency by one, creating a ditransitive structure. The new causer is added as subject; the original subject is demoted to an indirect object or oblique position; the original object remains as direct object. For example: 'She ate the cake' (transitive; she = subject/Agent, cake = object) → 'I made her eat the cake' (causative; I = causer/subject, her = causee/indirect object, cake = direct object). The original subject (she) is demoted but retains its agency as the entity performing the action."
  explanation: "This demotion pattern follows from the general logic of causatives as valency-increasing operations: each application of a causative adds one argument at the top of the argument hierarchy, shifting all other arguments down one position. This is why repeated causativization (making a causative of a causative) is constrained in most languages — the argument structure would otherwise become unmanageably complex."
```

## Explainer

You already understand **valency** — the number of arguments a predicate requires — and **thematic roles** like Agent, Patient, and Experiencer. Causative constructions are one of the clearest demonstrations of valency change in action: they systematically add one argument (the **causer**) to an existing predicate, shifting everything else down. An intransitive verb with one argument becomes transitive; a transitive verb with two arguments becomes ditransitive. The causer role is new — it is the entity responsible for bringing about the event described by the base predicate.

Consider the English verb "melt." By itself it is intransitive: "The ice melted." One participant, a Patient/Theme. Add a causative and you need a causer: "The heat melted the ice." Now two arguments. The original subject (ice) has been demoted to object, and a new Agent-causer (heat) has been introduced at the subject position. This is the causative alternation at work — a structural transformation that reorganizes argument positions while preserving the core event meaning. English handles this largely through lexical alternation (the same verb can appear in both frames), but other languages grammaticalize causation more explicitly.

Languages express causatives through three main strategies. **Morphological causatives** use affixes directly on the verb: in Turkish, the suffix -t or -dir creates causatives (gel "come" → getir "bring," i.e., cause to come). In Japanese, the suffix -(s)ase does the same. **Periphrastic causatives** use a dedicated causative verb plus an infinitive or complement clause: English "make," "have," and "let" work this way ("She made him apologize," "I had the mechanic fix it"). The distinction between make, have, and let captures degrees of causation — coercive, arranged, and permissive respectively. **Lexical causatives** are unrelated words that encode causation by convention ("kill" = cause to die, "show" = cause to see).

A key cross-linguistic generalization is that periphrastic causatives (analytic) tend to express **indirect causation** — the causer acts on the causee, who then performs the action — while morphological causatives express **direct causation** where the causer acts more immediately. "She made him clean the room" suggests she pressured or ordered him; a morphological causative in a language that has one would imply she physically directed the cleaning. Control and raising constructions, which you have seen, interact with causatives: in "I let her leave," she retains full control; in "I made her leave," she does not. Understanding causatives builds your ability to analyze how languages grammatically encode the relationship between agency, causation, and event structure.
