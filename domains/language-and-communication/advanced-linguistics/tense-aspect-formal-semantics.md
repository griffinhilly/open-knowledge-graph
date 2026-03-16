---
id: tense-aspect-formal-semantics
title: Tense and Aspect in Formal Semantics
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: montague-semantics
  type: hard
- id: progressive-and-perfect-aspects
  type: hard
tags:
- semantics
- tense
- aspect
stage: advanced
status: draft
---

# Tense and Aspect in Formal Semantics

## Core Idea
Tense locates events relative to the utterance time (past, present, future); aspect specifies internal temporal structure (perfective/imperfective, habitual, progressive). Formal theories model these using event times, reference times, and intervals to derive compositional truth conditions.

## How It's Best Learned
Compare event-based and interval-based semantics for tense and aspect; test languages with different aspect systems (Slavic perfective/imperfective) to see how aspectual meaning varies cross-linguistically.

## Common Misconceptions
Tense and aspect are not purely temporal but interact with grammatical aspect marking and viewpoint; the same absolute event time can be described via different aspects.

## Explainer

From Montague semantics, you know how to build compositional truth conditions for sentences using typed functions — extensions of words combined by function application. From your study of progressive and perfect aspects, you have intuitions about what these forms mean: the progressive describes an ongoing event, the perfect relates a past event to a present state. Formal semantics for tense and aspect is the project of making those intuitions precise enough to compute truth conditions compositionally. The central challenge is that temporal meaning involves *multiple* time coordinates, not just the moment of speaking.

**Reichenbach's three-time analysis** remains the foundational framework. He distinguished the **Speech Time (S)** — when the utterance is produced; the **Event Time (E)** — when the described event occurs; and the **Reference Time (R)** — a contextually salient temporal perspective point from which the event is viewed. Simple past: E precedes S, R coincides with E ("She left"). Past perfect: E precedes R, R precedes S ("She had left before he arrived" — R is anchored to his arrival, E is before that). Future perfect: S precedes R, E precedes R ("By noon, she will have left" — R is noon, E is before noon, both after S). This three-way distinction elegantly captures why sentences about the same event can differ in meaning depending on the perspective point from which the event is viewed.

**Aspect** — the contribution your progressive and perfect study prepared you for — adds internal temporal structure to events. Neo-Davidsonian event semantics treats verbs as predicates over events, with tense operators locating those events temporally. The **progressive** "She was running" introduces an event interval I containing the reference time — R is within the running interval, even though the running may not be completed. This captures the **imperfective paradox**: "She was crossing the street" does not entail "She crossed the street" (she might have been hit by a car partway), because the progressive only requires R to be inside the event interval, not that the interval reaches its culmination. **Perfective** aspect presents events as completed wholes, with no internal structure — "She crossed the street" asserts the full event.

**Aktionsart** (lexical aspect) interacts crucially with grammatical aspect. Verbs lexically encode their temporal structure: **states** have no inherent endpoint (*know*, *love*); **activities** are processes without culmination (*run*, *swim*); **accomplishments** are processes with a telos (*walk to the store*); **achievements** are punctual (*notice*, *arrive*). The interaction produces systematic patterns: only telic predicates (accomplishments, achievements) produce inferences about completion in the simple past — "She walked to the store" implies she arrived; "She walked" does not. Progressive aspect suppresses the telos of accomplishments: "She was walking to the store" no longer implies arrival. These interactions are not quirks but follow from how aspect operators compose with the event structures provided by lexical aspect — which is why the formal apparatus, tedious as it can seem, does real explanatory work that informal description cannot achieve.
