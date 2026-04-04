---
id: inform-language-fiction-authoring
title: 'Inform: Language Design for Interactive Fiction'
domain: literature
course: digital-and-experimental-literature
prerequisites:
- id: interactive-fiction-text-adventures
  type: hard
builds-toward:
- procedural-narrative-system-generation
tags:
- inform
- interactive-fiction
- authoring-language
- literary-form
stage: advanced
status: draft
---

# Inform: Language Design for Interactive Fiction

## Core Idea
Inform is a specialized language for interactive fiction that abstracts computational complexity into syntax closer to narrative logic. Its design embodies specific assumptions about how stories work (objects, properties, states, actions), shaping what kinds of narratives can be created. Understanding Inform reveals how technical implementation directly constrains literary possibility.

## Questions

```yaml
- type: multiple-choice
  question: How does Inform's language design shape what kinds of interactive narratives can be created?"
  options:
    - 0: "Inform abstracts programming into narrative-friendly syntax and enforces a model of stories as object-property-state systems, enabling certain narrative possibilities while constraining others"
    - 1: "Inform allows any narrative structure regardless of technical constraints"
    - 2: "Inform is purely a programming language unrelated to narrative structure"
    - 3: "Inform proves that interactive fiction cannot have complex narratives"
  correct_answer: 0
  explanation: "Inform's design embodies assumptions about story structure: objects with properties, state changes through actions, rule systems governing interaction. This model works well for exploration-based or puzzle-based narratives but may constrain psychologically complex or non-spatial narratives. The language's affordances and constraints directly shape what stories are easy or difficult to create."

- type: multiple-choice
  question: What does Inform reveal about the relationship between technical implementation and literary form?"
  options:
    - 0: "Technical design decisions (language syntax, data structures, system architecture) fundamentally shape what literary forms are possible and easy to create"
    - 1: "Technical implementation has no relationship to literary form"
    - 2: "All programming languages produce identical narrative possibilities"
    - 3: "Literature is completely independent of its technical substrate"
  correct_answer: 0
  explanation: "Inform's object-property-state model makes interactive exploration natural but might complicate non-spatial narrative or emotional complexity. A different technical architecture might enable different narrative possibilities. This reveals something important: form is not separable from technical implementation. The tools available constrain and enable different literary possibilities."

- type: true-false
  statement: "Inform's design assumes that interactive fiction works through player interaction with objects in spaces, which shapes the kinds of stories that are most naturally created in the language"
  correct_answer: true
  explanation: "Inform is optimized for object-based, location-based, puzzle-based interactive narratives. Stories structured around other principles (pure dialogue, internal monologue, non-spatial narrative) require more effort in Inform. This is not a failing but a feature—every tool has affordances and constraints."

- type: true-false
  statement: "Understanding Inform is unnecessary for literary criticism since it is purely a technical tool unrelated to aesthetic or narrative analysis"
  correct_answer: false
  explanation: "Understanding Inform is essential for understanding interactive fiction as literary form. The language embodies assumptions about narrative structure that shape what's possible. A literary critic ignoring technical implementation would miss crucial dimensions of how the work functions."

- type: short-answer
  question: "Explain how Inform's object-property-action model of narrative embodies particular assumptions about how stories work, and discuss what narrative possibilities this enables or constrains."
  explanation: "Inform's model assumes: (1) Narrative world consists of objects (items, locations, characters); (2) Objects have properties (descriptions, states, relationships); (3) Narrative progresses through player actions affecting object states. This model enables: Exploration-based narratives (discovering objects and properties), puzzle-based narratives (actions to change states), spatial narratives (moving through locations). This model constrains: Internal monologue/consciousness narratives (difficult to represent objects/states), purely dialogic narratives (dialogue is secondary to object interaction), non-spatial narratives (everything relates to location/object model), narratives about abstract concepts or emotions (Inform naturalizes physical/spatial thinking). Other languages might enable different possibilities. Example: A language modeling narrative as dialogue rather than object-interaction might create different possibilities for conversation-based or non-spatial stories. This reveals: (1) Technical choices are aesthetic choices—they shape what's easy and natural to create; (2) Form emerges from technical affordances as much as from authorial intention; (3) Understanding interactive fiction requires understanding the technical substrate—what tools make possible and constrain."
```

## Explainer

Inform is a programming language specifically designed for interactive fiction, but it is far more than a neutral technical tool. Its design embodies particular assumptions about how stories work—assumptions that shape what kinds of narratives are easy to create and what kinds are difficult.

Inform models narrative through objects, properties, and state changes. A story world consists of objects (rooms, items, characters) with properties (descriptions, conditions, relationships). Narrative progresses through actions that change these properties: taking an object changes its location; solving a puzzle changes a state flag; moving between rooms changes the player's location property. This model is elegant and powerful for certain kinds of narratives, particularly those involving exploration, puzzle-solving, and spatial navigation.

However, this object-property-action model shapes what narrative is natural in Inform. Stories structured around discovery and interaction with objects are straightforward. Internal monologue or psychological depth—states that are primarily conceptual rather than object-based—are more difficult to represent elegantly. Dialogue-centered or non-spatial narratives require more elaborate workarounds. A story about emotional transformation or social negotiation, while possible in Inform, may require fighting the language's affordances.

This reveals something important about the relationship between technical design and literary form. Inform is not a neutral implement; it is a tool shaped by particular assumptions. These assumptions enable certain aesthetic possibilities while constraining others. Understanding interactive fiction literature requires understanding the technical substrate—what the tool makes easy, natural, and elegant, and what it makes difficult or awkward.

Different authoring languages shape different narrative possibilities. Twine, another interactive fiction language, models story as nodes and links rather than objects and properties, enabling branching narrative in a way Inform does not. A language designed around dialogue as the primary unit would enable different narrative possibilities than Inform's object-focus. This suggests that literary form is not independent of technical implementation but emerges from it.

The broader lesson is that technical choices are aesthetic choices. Programming language design, data structure selection, and system architecture are not merely implementation details; they shape what stories can be told and how naturally they can be told. Interactive fiction authors work within the affordances and constraints of their chosen language. Understanding the works thus requires understanding the technical choices that made them possible.
