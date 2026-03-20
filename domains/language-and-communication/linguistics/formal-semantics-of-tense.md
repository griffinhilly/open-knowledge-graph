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
tags:
- semantics
- tense
- logic
stage: advanced
status: draft
---

# Formal Semantics of Tense and Time

## Core Idea
Temporal logic formalizes the semantics of tense by quantifying over time intervals and assigning truth values relative to moments. Past, present, and future tenses are formalized as assertions about when events hold relative to the speech time.

## Explainer

From your work with semantic types and composition, you know that sentences are evaluated relative to a model — they denote functions from possible worlds to truth values. But the same sentence, "It is raining," is true at some times and false at others. A model that ignores time is underdetermined. The formal solution is to extend the evaluation index: instead of evaluating a sentence at a world w alone, we evaluate it at a **world-time pair ⟨w, t⟩**, where t is a point or interval on a timeline. The present tense is the default: the formula is evaluated at the **speech time** S, the moment of utterance.

The simplest formal treatment, following Prior's **tense logic**, introduces two sentential operators analogous to modal operators. The **past operator P** and **future operator F** quantify over times: P(φ) is true at time t if there exists some time t' < t at which φ is true; F(φ) is true at t if there exists some t' > t at which φ is true. These operators compose: PP(φ) — "it was the case that it had been the case that φ" — describes a doubly past event, as in the pluperfect. The formal machinery is identical in structure to modal logic over possible worlds, with time replacing worlds and temporal precedence replacing the accessibility relation.

A more fine-grained account, following **Reichenbach**, distinguishes three independent reference points: the **speech time** S (when the utterance occurs), the **event time** E (when the described event actually occurs), and the **reference time** R (a temporal perspective point from which the event is viewed). Each tense can be characterized by the ordering of these three points. Simple past: E and R before S — the event occurred, and we view it from the same past vantage. **Past perfect**: E before R, R before S — the event occurred before a past reference point, as in "She had left before I arrived" (E=leaving, R=arriving, both before S). Simple future: S before R and E — the event is ahead of now. These orderings predict the felicity conditions for each tense in discourse.

The formal treatment of **aspect** — the distinction between simple past "she ran" (event viewed as completed) and past progressive "she was running" (event viewed as ongoing at a reference time) — requires moving from point-based to **interval-based** models. Events with duration are true throughout an interval; culminating events are true only at a point. In compositional semantics, this connects directly to the type system you know: predicates can take **event variables** (of type *e* over eventualities), and tense operators bind those variables to positions on the timeline relative to S and R. The semantics of tense is thus the semantics of quantification, applied to a temporal domain rather than an individual-level one.
