---
id: formal-semantics-of-tense
title: Formal Semantics of Tense and Time
domain: language-and-communication
course: linguistics
prerequisites:
- id: semantic-types-and-composition
  type: hard
- id: tense-aspect-formal-semantics
  type: soft
- id: viewpoint-aspect-perfective-imperfective
  type: soft
- id: event-semantics-formal
  type: soft
- id: syntax-semantics-interface-formal
  type: soft
- id: scope-and-binding-formally
  type: soft
tags:
- semantics
- tense
- logic
stage: advanced
status: validated
---
# Formal Semantics of Tense and Time

## Core Idea
Temporal logic formalizes the semantics of tense by quantifying over time intervals and assigning truth values relative to moments. Past, present, and future tenses are formalized as assertions about when events hold relative to the speech time.

## Questions

```yaml
- question: "In Reichenbach's framework, which ordering of Speech time (S), Event time (E), and Reference time (R) correctly describes the past perfect in 'She had left before I arrived'?"
  type: multiple-choice
  options:
    - "S before R, R before E — the event is ahead of the reference point, which is in turn ahead of speech"
    - "E before R, R before S — the leaving event preceded the arriving event (the reference), and both are before the speech moment"
    - "R equals S, with E before both — the reference point is identical to the speech time, placing only the event in the past"
    - "E equals R, both before S — the event and reference time coincide at a single past moment"
  answer: 1
  explanation: "In 'She had left before I arrived': E = the leaving event, R = the arriving event (the reference point from which the leaving is viewed), S = the moment of utterance. The leaving (E) preceded the arriving (R), which in turn preceded the speech moment (S): E < R < S. This is what makes the past perfect different from simple past — simple past is just E, R before S with R≈E, while past perfect requires a distinct earlier event anchored to an intermediate reference point. The R point is what Reichenbach added to Prior's simpler framework to distinguish these tenses."

- question: "A researcher proposes evaluating all tensed sentences at a single world-speech-time pair — using only the speech time S, with no separate reference time R. Which pair of tenses would this framework fail to distinguish?"
  type: multiple-choice
  options:
    - "Simple present from habitual present — both are evaluated at speech time regardless"
    - "Simple past from past progressive — both describe past events and would map to the same operator"
    - "Past perfect ('she had left') from simple past ('she left') — both are 'before S' without a separate reference point to mark the earlier-past perspective of the past perfect"
    - "Simple future from future progressive — both describe future events and collapse to the same future operator"
  answer: 2
  explanation: "With only P and F operators relative to S: simple past P(φ) = 'there exists t < S where φ holds'; past perfect PP(φ) = 'there exists t < S where P(φ) holds at t'. But the English past perfect specifically requires an anchoring reference point R (like 'before I arrived') that differs from S. Without R, 'she had left' and 'she left' both reduce to 'E before S' — the difference between 'she left yesterday' and 'she had left by yesterday' collapses. Reichenbach's three-point system (S, R, E) was introduced precisely to make this distinction formally explicit."

- question: "In Prior's tense logic, the operators P and F (past and future) are fundamentally structurally different from modal operators in possible-worlds semantics, because they quantify over times instead of worlds."
  type: true-false
  answer: false
  explanation: "The explainer states explicitly that 'the formal machinery is identical in structure to modal logic over possible worlds, with time replacing worlds and temporal precedence replacing the accessibility relation.' P and F quantify over times just as modal operators □ and ◇ quantify over possible worlds; temporal ordering (t' < t) plays the same structural role as the accessibility relation in modal logic. This parallel is not accidental — it means that the full toolkit of modal logic (possible-worlds semantics, frame conditions, soundness and completeness results) transfers directly to tense logic."

- question: "The distinction between simple past ('she ran') and past progressive ('she was running') requires an interval-based model of time rather than a point-based one, because the progressive views an event as ongoing at a reference time rather than completed."
  type: true-false
  answer: true
  explanation: "Simple past treats the running event as completed — true at a point (or across an interval but viewed as a whole unit). Past progressive 'she was running at noon' requires a reference time R (noon) that falls within the running interval, meaning the event is true throughout a duration and has not concluded at R. Point-based models where events are simply true or false at instants cannot represent this: you need the event to be true throughout an interval [t₁, t₂] with R falling strictly inside it. This is why the formal treatment of aspect requires interval-based temporal models."

- question: "What is the difference between Speech time (S), Event time (E), and Reference time (R) in Reichenbach's framework, and why is the Reference time needed to distinguish the past perfect from the simple past?"
  type: short-answer
  answer: "S is when the utterance occurs; E is when the described event actually happens; R is a temporal vantage point from which the event is viewed. Simple past: E and R both precede S, with R approximately at E — the event is viewed from the same past vantage where it occurred ('she left'). Past perfect: E precedes R, which precedes S — the event is viewed from a later past vantage point, before that reference point ('she had left by the time I arrived'). Without R, both tenses would be indistinguishable — both just have E before S. R provides the intermediate anchor that captures the 'doubly past' quality of the past perfect."
  explanation: "The need for three reference points becomes vivid in narrative embedding: 'She realized she had made a mistake.' Here S = narrating moment, R = the moment of realization, E = the mistake itself (earlier). Simple past would lose the hierarchical relationship between the moment of realization and the earlier mistake. Reichenbach's framework is thus richer than Prior's P/F operators precisely because it can represent this kind of temporal anchoring — events viewed from past vantage points that are themselves in the past."
```

## Explainer

From your work with semantic types and composition, you know that sentences are evaluated relative to a model — they denote functions from possible worlds to truth values. But the same sentence, "It is raining," is true at some times and false at others. A model that ignores time is underdetermined. The formal solution is to extend the evaluation index: instead of evaluating a sentence at a world w alone, we evaluate it at a **world-time pair ⟨w, t⟩**, where t is a point or interval on a timeline. The present tense is the default: the formula is evaluated at the **speech time** S, the moment of utterance.

The simplest formal treatment, following Prior's **tense logic**, introduces two sentential operators analogous to modal operators. The **past operator P** and **future operator F** quantify over times: P(φ) is true at time t if there exists some time t' < t at which φ is true; F(φ) is true at t if there exists some t' > t at which φ is true. These operators compose: PP(φ) — "it was the case that it had been the case that φ" — describes a doubly past event, as in the pluperfect. The formal machinery is identical in structure to modal logic over possible worlds, with time replacing worlds and temporal precedence replacing the accessibility relation.

A more fine-grained account, following **Reichenbach**, distinguishes three independent reference points: the **speech time** S (when the utterance occurs), the **event time** E (when the described event actually occurs), and the **reference time** R (a temporal perspective point from which the event is viewed). Each tense can be characterized by the ordering of these three points. Simple past: E and R before S — the event occurred, and we view it from the same past vantage. **Past perfect**: E before R, R before S — the event occurred before a past reference point, as in "She had left before I arrived" (E=leaving, R=arriving, both before S). Simple future: S before R and E — the event is ahead of now. These orderings predict the felicity conditions for each tense in discourse.

The formal treatment of **aspect** — the distinction between simple past "she ran" (event viewed as completed) and past progressive "she was running" (event viewed as ongoing at a reference time) — requires moving from point-based to **interval-based** models. Events with duration are true throughout an interval; culminating events are true only at a point. In compositional semantics, this connects directly to the type system you know: predicates can take **event variables** (of type *e* over eventualities), and tense operators bind those variables to positions on the timeline relative to S and R. The semantics of tense is thus the semantics of quantification, applied to a temporal domain rather than an individual-level one.
