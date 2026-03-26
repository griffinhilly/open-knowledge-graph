---
id: event-ontology
title: Event Ontology
domain: philosophy
course: metaphysics
prerequisites:
- id: ontological-categories
  type: hard
- id: causation-and-causal-relations
  type: soft
- id: first-order-logic-syntax
  type: soft
tags:
- events
- ontology
- individuation
- Davidson
- Kim
stage: formal-systems
status: validated
---

# Event Ontology

## Core Idea
Events — births, explosions, decisions — seem to be genuine items in our ontology, not reducible to objects or properties alone. The central questions are what events are and when two event-descriptions pick out the same event. Davidson argued that events are individuated by their causes and effects: if two descriptions share all the same causal relations, they name one event. Kim proposed a finer-grained view: events are property exemplifications by objects at times, so the same action can constitute distinct events if it exemplifies distinct properties. The debate matters because causation, action theory, and philosophy of mind all presuppose answers about what events are and how to count them.

## How It's Best Learned
Read Davidson's 'The Individuation of Events' alongside Kim's 'Events as Property Exemplifications.' For each account, test it against a case like the assassination of Caesar: how many events occurred — a stabbing, a killing, a political upheaval?

## Common Misconceptions
- Events are not just changes; some philosophers treat static states (a ball resting on a table) as events too.
- The coarse-grained vs. fine-grained debate is not merely verbal — it has consequences for how many causes an effect has and whether mental events are identical to physical events.

## Explainer

From your study of ontological categories, you know that metaphysics asks what kinds of things exist and how they relate to one another. Objects — tables, electrons, persons — are the most familiar ontological category. But the world also seems to contain **events**: births, explosions, decisions, collisions, performances. Events are not objects — an explosion is not a thing in the way a table is — yet we refer to them, quantify over them ("three events occurred"), and cite them as causes and effects. Event ontology asks whether events are genuine items in our ontology and, if so, what they are and how to individuate them — that is, when two event-descriptions pick out the same event versus distinct events.

**Donald Davidson** proposed a **coarse-grained** theory of event individuation. On his view, events are concrete particulars — like objects, but extended in time rather than (or in addition to) space. The criterion of identity is causal: two event-descriptions pick out the same event if and only if they have exactly the same causes and exactly the same effects. Consider Brutus stabbing Caesar. "The stabbing," "the killing," and "the assassination" all share the same causal history (Brutus's intentions, the political circumstances, the physical motion of the knife) and the same causal consequences (Caesar's death, the political upheaval). By Davidson's criterion, these are three descriptions of one event. The event is individuated by its causal position in history, not by the properties under which it is described. This makes event identity extensional — a matter of causal profile — rather than intensional — a matter of descriptive content.

**Jaegwon Kim** proposed a **fine-grained** alternative. On his view, events are **property exemplifications**: structured triples of an object, a property, and a time — (object, property, time). "Caesar's being stabbed by Brutus" and "Caesar's being killed by Brutus" involve the same object and the same time, but different properties (being stabbed, being killed). Since the property component differs, they are distinct events. Kim's approach multiplies events dramatically: a single physical occurrence can constitute as many distinct events as there are properties exemplified. Where Davidson sees one event under multiple descriptions, Kim sees multiple events sharing a spatio-temporal location.

This is not a merely verbal dispute — the choice between coarse-grained and fine-grained individuation has real consequences for other areas of philosophy. In **philosophy of mind**, Davidson's view supports the identity theory: if a mental event (a desire for water) and a physical event (a particular pattern of neural firing) share all the same causes and effects, they are the same event described in two vocabularies. Kim's view makes this identity harder to sustain, since "being a desire for water" and "being neural pattern P" are different properties, yielding distinct events. This opens the **causal exclusion problem**: if the mental event and the physical event are distinct, which one actually causes behavior? The debate over event individuation thus ramifies into foundational questions about the relationship between mind and body, the nature of causation, and how many causes an effect can have.

## Questions

```yaml
- question: "Brutus stabs Caesar, and Caesar dies. According to Davidson's coarse-grained theory, how many events occurred?"
  type: multiple-choice
  options:
    - "Three — the stabbing, the killing, and the death have distinct causal profiles"
    - "Two — the stabbing and the dying are separate, but killing just redescribes the stabbing"
    - "One — 'the stabbing,' 'the killing,' and 'Caesar's death' are descriptions of a single event"
    - "It depends on how many properties Caesar exemplified at the moment of death"
  answer: 2
  explanation: "Davidson's coarse-grained theory individuates events by their causal relations: two descriptions pick out the same event if and only if they share all the same causes and effects. 'Brutus stabbed Caesar' and 'Brutus killed Caesar' refer to the same physical occurrence — one spatio-temporal event that caused Caesar's death. The different descriptions simply characterize the same event under different aspects. Option D describes Kim's view, not Davidson's — Kim individuates by property exemplifications at times."

- question: "On Kim's fine-grained view, 'Caesar's being stabbed by Brutus' and 'Caesar's being killed by Brutus' are:"
  type: multiple-choice
  options:
    - "The same event described differently, since they share all causal relations"
    - "Two distinct events, because they involve Caesar exemplifying different properties"
    - "Both reducible to a single physical state — the motion of Brutus's arm"
    - "Identical only if Brutus intended to kill Caesar from the start"
  answer: 1
  explanation: "Kim defines events as property exemplifications by an object at a time: (object, property, time) triples. 'Being stabbed' and 'being killed' are different properties, so they constitute different events even though they occur at the same time with the same object. This fine-grained individuation multiplies events: a single occurrence can constitute many events depending on how many properties are instantiated. Davidson would say all these descriptions name one event; Kim says each distinct property creates a distinct event."

- question: "The debate between Davidson's coarse-grained and Kim's fine-grained event individuation is merely a verbal dispute — both views agree on most substantive metaphysical questions."
  type: true-false
  answer: false
  explanation: "This is a substantive debate with real consequences. One critical consequence is for philosophy of mind: if mental events are identical to physical events, Davidson's view allows 'a pain' and 'C-fiber firing' to be the same event (sharing causal relations), making mental-physical identity more readily defensible. On Kim's fine-grained view, they would be distinct events (different properties exemplified), making identity harder. Another consequence: how many causes an effect has differs — Davidson's one-event view yields one proximate cause; Kim's view can yield multiple distinct event-causes."

- question: "On Davidson's account, two event-descriptions pick out the same event if and only if they have exactly the same causes and effects."
  type: true-false
  answer: true
  explanation: "This is Davidson's criterion of event individuation: events are identical when they stand in exactly the same causal relations. 'The stabbing' and 'the killing' of Caesar are the same event because the same prior conditions caused both, and both caused the same subsequent events. Davidson's criterion makes event identity extensional — determined by causal profile — rather than intensional (determined by description or property). This is why it is called 'coarse-grained': many descriptions can name one event, individuated only by its causal position in history."

- question: "Why does the choice between Davidson's coarse-grained and Kim's fine-grained accounts of events matter for philosophy of mind? Give a concrete example of a consequence."
  type: short-answer
  answer: "One major consequence is for the mind-body identity theory. Davidson's view allows 'a mental event' (a thought) and 'a physical event' (a brain state) to be identical — two descriptions of one event sharing the same causal history. On Kim's view, the mental event (exemplifying 'being a desire for water') and the physical event (exemplifying 'neurons firing in pattern P') would be distinct events because they exemplify different properties, making strict mind-brain identity harder to maintain and raising the causal exclusion problem."
  explanation: "The debate also affects overdetermination: if 'the killing' and 'the stabbing' are one event (Davidson), Caesar's death has one proximate cause. If they are two events (Kim), the death might have two distinct event-causes, raising questions about which one is explanatorily primary. This structure recurs in philosophy of mind: if a mental event and a physical event are distinct (Kim), what does the causal work in producing behavior — the mental or the physical? This is the causal exclusion problem, a central challenge for non-reductive physicalism."
```
