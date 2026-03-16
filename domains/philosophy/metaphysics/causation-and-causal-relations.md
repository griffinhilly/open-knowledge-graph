---
id: causation-and-causal-relations
title: Causation and Causal Relations
domain: philosophy
course: metaphysics
prerequisites:
- id: what-is-metaphysics
  type: hard
- id: thought-experiments
  type: soft
builds-toward:
- regularity-theory-of-causation
- counterfactual-causation
- free-will-and-determinism
tags:
- causation
- causal relata
- events
- mechanism
- metaphysics
stage: formal-systems
status: validated
---

# Causation and Causal Relations

## Core Idea
Causation is among the most fundamental relations in nature — understanding it matters for science, law, morality, and the philosophy of mind. The philosophical project asks: what are the relata of causal relations (events? facts? objects?), what kind of relation is causation (necessary connection? regularity? counterfactual dependence?), and is causation discovered or projected? Hume famously argued we never perceive necessitation, only constant conjunction, which launched centuries of attempts to analyze causation in less metaphysically loaded terms. Modern accounts include regularity theories, counterfactual theories, mechanistic theories, and interventionist theories.

## How It's Best Learned
Read Hume's Enquiry Section VII and Lewis's 'Causation' (1973) back to back. For each, identify: what are the relata, what is the key relation, and what counterexamples threaten the view?

## Common Misconceptions
- Temporal precedence alone is not causation (post hoc ergo propter hoc fallacy).
- Causation is not the same as correlation; but the philosophical question is what the difference consists in, which is non-trivial.

## Questions

```yaml
- question: "Which of the following best illustrates the post hoc ergo propter hoc fallacy?"
  type: multiple-choice
  options:
    - "Concluding smoking causes cancer because smokers get cancer at higher rates in large controlled studies"
    - "Concluding a rooster's crowing causes the sun to rise because crowing reliably precedes sunrise"
    - "Concluding exercise improves mood because a randomized controlled trial found the effect"
    - "Concluding atmospheric pressure causes storms because the two co-vary across many observations"
  answer: 1
  explanation: "Post hoc ergo propter hoc ('after this, therefore because of this') mistakes temporal sequence for causation. The rooster reliably crows before sunrise but does not cause it. Option A uses controlled studies that rule out confounders; option C uses an RCT designed precisely to establish causation; option D describes a correlation that does reflect a real causal mechanism."

- question: "According to Hume, repeated observation of one event following another gives us direct perception of the necessary connection between them."
  type: true-false
  answer: false
  explanation: "This is Hume's central negative claim: we never perceive necessary connection. We observe constant conjunction (A is always followed by B) and temporal priority (A comes before B), but no 'power' or 'necessitation' is observed in the events themselves. Our idea of necessary connection arises from a 'determination of the mind' — a habit of expectation — not from observation. This is the core of Hume's skeptical analysis of causation."

- question: "Why is it philosophically difficult to distinguish causation from mere correlation?"
  type: short-answer
  answer: "Correlation is a statistical regularity between two variables, but causation seems to require a real dependence or mechanism that explains why A brings about B. It is difficult to specify what that 'something more' is without using causal concepts, and the observable data alone underdetermines which causal structure produced it."
  explanation: "A correlation between A and B is compatible with A causing B, B causing A, a third variable C causing both, or pure coincidence. Identifying which is operating requires more than statistical data — it requires causal assumptions about what would happen under interventions, or knowledge of the underlying mechanism. This is why causal inference in both philosophy and statistics is technically and conceptually demanding."
```

## Explainer

Causation is so basic to how we think about the world that we rarely stop to question it. We say fires cause smoke, viruses cause illness, intentions cause actions — as if the causal relation were simply given. But philosophers since Hume have argued that causation is deeply puzzling, and that getting it right has practical stakes in science, law, and moral responsibility.

Start with **Hume's challenge**. When you watch one billiard ball strike another and the second rolls away, you observe two things: the collision, and then the motion. You do not observe any "power" or "necessity" binding them together — you see one event followed by another. Hume argued that if you examine any causal claim carefully, you find exactly the same structure: **constant conjunction** (A is always followed by B), **temporal priority** (A comes before B), and **spatial contiguity** (they are connected in space). The idea that there is something more — some metaphysical glue — is, Hume claimed, a projection of our own mental habits onto the world, not a feature we perceive in the events themselves.

Hume's analysis generated immediate counterexamples. Day constantly follows night, but night does not cause day. A falling barometer reliably precedes a storm, but the drop does not cause the storm — both are effects of atmospheric pressure. These cases show that constant conjunction is not sufficient for causation; there must be something more that distinguishes genuine causal relations from mere regularities. Modern theories try to identify that "something more": David Lewis's **counterfactual theory** says A causes B if, had A not occurred, B would not have occurred either; **mechanistic theories** require a continuous physical process connecting A to B; **interventionist theories** ground causation in what would happen if you experimentally manipulated A.

An equally important question is what kinds of things stand in causal relations — the question of **causal relata**. Do events cause events (the match caused the fire)? Do facts cause facts (that the match was struck caused it to be the case that the fire started)? Or do objects with properties cause things (the struck dry match caused the fire by being combustible)? Different answers have different implications, especially in philosophy of mind, where we need to explain how mental states — which are not obviously physical events — can cause bodily actions.

The practical upshot is that recognizing the post hoc fallacy is only the beginning of causal reasoning. Temporal precedence is necessary but not sufficient for causation. Correlation is evidence for causation but does not establish it. And even a well-controlled experiment only establishes causation given background assumptions about the experimental setup. These are the conceptual foundations you will need as you move into the specific theories — regularity theory, counterfactual causation — and their application to free will and determinism.
