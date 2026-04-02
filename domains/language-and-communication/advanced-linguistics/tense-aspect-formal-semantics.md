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
stage: expert
status: validated
---

# Tense and Aspect in Formal Semantics

## Core Idea
Tense locates events relative to the utterance time (past, present, future); aspect specifies internal temporal structure (perfective/imperfective, habitual, progressive). Formal theories model these using event times, reference times, and intervals to derive compositional truth conditions.

## How It's Best Learned
Compare event-based and interval-based semantics for tense and aspect; test languages with different aspect systems (Slavic perfective/imperfective) to see how aspectual meaning varies cross-linguistically.

## Common Misconceptions
Tense and aspect are not purely temporal but interact with grammatical aspect marking and viewpoint; the same absolute event time can be described via different aspects.

## Questions

```yaml
- question: "\"She was crossing the street\" does not entail \"She crossed the street.\" What feature of formal aspect semantics explains this inference gap?"
  type: multiple-choice
  options:
    - "The progressive is in past tense while the simple past is in present perfect, creating a temporal mismatch"
    - "The progressive operator requires only that reference time R fall within the event interval, not that the interval reaches its culmination — so the event may have been interrupted"
    - "Progressive aspect in English marks events as hypothetical or counterfactual rather than actual"
    - "The sentence lacks the perfect structure that would assert event completion"
  answer: 1
  explanation: "This is the imperfective paradox. The progressive 'was crossing' asserts that R (reference time) falls inside the event interval — the crossing is in progress at that moment — but does NOT require the interval to run to its culmination. The woman may have been hit by a car partway through, making 'was crossing' true but 'crossed' false. By contrast, perfective 'crossed' presents the event as a completed whole. This difference is about internal temporal structure (aspect), not tense, and it is why formal semantics needs both dimensions."

- question: "In Reichenbach's three-time analysis, how are S (speech time), E (event time), and R (reference time) ordered in the sentence \"She had left before he arrived\"?"
  type: multiple-choice
  options:
    - "E = R = S — all three coincide at the utterance moment"
    - "S precedes E, E precedes R — speech is before the leaving, which is before the arrival"
    - "E precedes R, R precedes S — the leaving is before the arrival, and the arrival is before speech time"
    - "R precedes E, E precedes S — the reference point is before the event, which is before speech time"
  answer: 2
  explanation: "The past perfect signals E < R < S. The event (leaving) is prior to R, the reference time anchored to 'when he arrived,' which is itself prior to S (speech time). This three-way ordering explains why the past perfect feels 'doubly past' — it marks distance from a past perspective point, not just from the present. Reichenbach's framework captures this elegantly: different perfect and past constructions reflect different orderings of E, R, and S, not just different distances from speech time."

- question: "The same event can be described using either perfective or progressive aspect, and the choice of aspect changes how the event's temporal structure is presented without changing which event occurred."
  type: true-false
  answer: true
  explanation: "Aspect is about viewpoint, not about changing the world. The same crossing event can be described as 'she crossed the street' (perfective: the event is presented as a completed whole, viewed from outside) or 'she was crossing the street' (progressive/imperfective: R is inside the event interval, viewed from within). The event itself is the same; what differs is the temporal perspective. This viewpoint distinction — not a difference in which event happened — is what grammatical aspect formally captures."

- question: "In formal semantics, tense and aspect are equivalent — both locate an event in time relative to the utterance moment, just with different names."
  type: true-false
  answer: false
  explanation: "Tense and aspect are distinct dimensions. Tense locates events relative to speech time S (E before S = past; E = S = present; E after S = future). Aspect characterizes the internal temporal structure of events — whether they are presented as completed wholes (perfective) or as processes viewed from within (imperfective/progressive), and whether lexical endpoints are relevant. The same tense can combine with different aspects ('she crossed' vs. 'she was crossing'), and the same aspect appears in different tenses ('she was crossing' vs. 'she is crossing'). Neither subsumes the other; formal semantics requires both."

- question: "Explain how Aktionsart (lexical aspect) interacts with grammatical aspect, and give an example showing why this interaction matters for truth conditions."
  type: short-answer
  answer: "Aktionsart is the inherent temporal structure encoded in verb meaning: states (no endpoint), activities (no culmination), accomplishments (process + telos), achievements (punctual). Grammatical aspect overlays a viewpoint on this structure. The interaction produces different truth conditions: 'She walked to the store' (accomplishment + perfective) entails arrival because the telos is included in the completed event; 'She was walking to the store' (accomplishment + progressive) does not entail arrival because the progressive places R inside the event without requiring culmination — the telos is suspended. 'She walked' (activity + perfective) entails no specific endpoint because the activity verb encodes none."
  explanation: "These differences in entailment are systematic consequences of how aspect operators compose with lexical event structures, not arbitrary quirks of English idiom. This is why formal semantics needs both Aktionsart and grammatical aspect as separate compositional components — and why cross-linguistic data (e.g., Slavic perfective/imperfective distinctions) reveals the same underlying structure in typologically diverse languages."
```

## Explainer

From Montague semantics, you know how to build compositional truth conditions for sentences using typed functions — extensions of words combined by function application. From your study of progressive and perfect aspects, you have intuitions about what these forms mean: the progressive describes an ongoing event, the perfect relates a past event to a present state. Formal semantics for tense and aspect is the project of making those intuitions precise enough to compute truth conditions compositionally. The central challenge is that temporal meaning involves *multiple* time coordinates, not just the moment of speaking.

**Reichenbach's three-time analysis** remains the foundational framework. He distinguished the **Speech Time (S)** — when the utterance is produced; the **Event Time (E)** — when the described event occurs; and the **Reference Time (R)** — a contextually salient temporal perspective point from which the event is viewed. Simple past: E precedes S, R coincides with E ("She left"). Past perfect: E precedes R, R precedes S ("She had left before he arrived" — R is anchored to his arrival, E is before that). Future perfect: S precedes R, E precedes R ("By noon, she will have left" — R is noon, E is before noon, both after S). This three-way distinction elegantly captures why sentences about the same event can differ in meaning depending on the perspective point from which the event is viewed.

**Aspect** — the contribution your progressive and perfect study prepared you for — adds internal temporal structure to events. Neo-Davidsonian event semantics treats verbs as predicates over events, with tense operators locating those events temporally. The **progressive** "She was running" introduces an event interval I containing the reference time — R is within the running interval, even though the running may not be completed. This captures the **imperfective paradox**: "She was crossing the street" does not entail "She crossed the street" (she might have been hit by a car partway), because the progressive only requires R to be inside the event interval, not that the interval reaches its culmination. **Perfective** aspect presents events as completed wholes, with no internal structure — "She crossed the street" asserts the full event.

**Aktionsart** (lexical aspect) interacts crucially with grammatical aspect. Verbs lexically encode their temporal structure: **states** have no inherent endpoint (*know*, *love*); **activities** are processes without culmination (*run*, *swim*); **accomplishments** are processes with a telos (*walk to the store*); **achievements** are punctual (*notice*, *arrive*). The interaction produces systematic patterns: only telic predicates (accomplishments, achievements) produce inferences about completion in the simple past — "She walked to the store" implies she arrived; "She walked" does not. Progressive aspect suppresses the telos of accomplishments: "She was walking to the store" no longer implies arrival. These interactions are not quirks but follow from how aspect operators compose with the event structures provided by lexical aspect — which is why the formal apparatus, tedious as it can seem, does real explanatory work that informal description cannot achieve.
