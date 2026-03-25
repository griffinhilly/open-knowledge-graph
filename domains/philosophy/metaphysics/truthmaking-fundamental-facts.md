---
id: truthmaking-fundamental-facts
title: Truthmakers and Fundamental Facts
domain: philosophy
course: metaphysics
prerequisites:
- id: grounding-and-fundamentality
  type: hard
- id: facts-and-truthmakers
  type: hard
- id: grounding-fundamentality-hierarchy
  type: soft
- id: truthmakers-and-grounding
  type: soft
builds-toward:
- grounding-fundamentality-hierarchy
- reduction-metaphysical-relations
tags:
- truthmakers
- fundamentality
- grounding
stage: formal-systems
status: validated
---
# Truthmakers and Fundamental Facts

## Core Idea
Truthmakers are entities in virtue of which propositions are true; fundamental truthmakers explain truths without relying on further truths. This framework connects semantic truth to metaphysical structure, raising the question of which facts are truly fundamental and what makes complex truths true given only fundamental truths.

## How It's Best Learned
Work through examples of composite truths (conjunctions, conditionals, negations) and determine what minimal truthmakers would need to exist for each to be true.

## Common Misconceptions
Assuming every true proposition must have a truthmaker in some domain (truthmaker maximalism). Confusing truthmakers with causes or explanations of why propositions are true.

## Questions

```yaml
- question: "What makes the proposition 'Either it is raining or it is sunny' true, according to truthmaker theory?"
  type: multiple-choice
  options:
    - "Both the fact that it is raining AND the fact that it is sunny must exist as truthmakers"
    - "A special 'disjunction fact' — the fact of there being a disjunction — must exist as a distinct entity"
    - "The proposition is self-certifying and needs no external truthmaker"
    - "The fact that it is raining (or the fact that it is sunny) is sufficient — a truthmaker for either disjunct makes the whole disjunction true"
  answer: 3
  explanation: "A disjunction is made true by a truthmaker for either disjunct — you only need one of them. This illustrates a key insight: truthmakers need not mirror the logical complexity of the propositions they make true. You don't need a 'disjunction fact'; the existence of rain (or the existence of sunshine) is sufficient. Truthmaker theory maps the structure of reality onto the structure of propositions, but this mapping need not be one-to-one."

- question: "A philosopher argues: 'The proposition There are no unicorns is made true by all the actual animals in existence — each of which is not a unicorn.' A truthmaker maximalist would most likely respond:"
  type: multiple-choice
  options:
    - "This is correct — the collection of non-unicorn animals constitutes a sufficient positive truthmaker"
    - "No collection of positive facts about what exists can rule out the existence of additional things, like unicorns, without a totality fact"
    - "Negative truths do not require truthmakers, so the question is irrelevant"
    - "The proposition is not meaningful because it refers to non-existent objects"
  answer: 1
  explanation: "The maximalist problem with negative truths is that no collection of positive facts about what exists rules out the existence of unicorns — you could always add unicorns to the world alongside all the actual animals. A totality fact — the fact that the existing things are all the existing things — is needed to close off this possibility. Without it, the positive facts about actual animals are compatible with unicorns also existing. This is why negative truths are the hardest case for truthmaker theory."

- question: "Truthmakers are the causes or explanations of why a proposition is true — to know the truthmaker is to understand why the proposition came to be true."
  type: true-false
  answer: false
  explanation: "Truthmakers are entities in virtue of which a proposition is true — a metaphysical grounding relation, not a causal one. The ball's redness is what makes 'this ball is red' true; the redness is not the cause of the truth in any temporal sense. Causes involve time and processes; truthmaking is a synchronic relation of ontological dependence. Confusing truthmakers with causes or explanations is a listed misconception — the two notions are logically distinct."

- question: "A universal proposition like 'All emeralds are green' might require, as truthmakers, individual facts about each emerald being green — rather than a single unified truthmaker that mirrors the universal logical form."
  type: true-false
  answer: true
  explanation: "Truthmakers need not mirror the logical form of the propositions they make true, and the search for minimal adequate truthmakers is part of the project. For a universal claim, one view is that it is made true by all the relevant individual facts (each emerald's greenness) plus a totality fact (these are all the emeralds). Another view posits a general fact or law as a truthmaker for the universal. The point is that the logical structure of the proposition does not dictate the ontological structure of its truthmakers."

- question: "Why are negative truths the hardest case for truthmaker theory, and what are two competing strategies philosophers use to handle them?"
  type: short-answer
  answer: "Negative truths like 'There are no unicorns' cannot be made true by any positive entity — a unicorn is precisely what's absent, and any collection of actual things is compatible with unicorns also existing. Two strategies: (1) Truthmaker maximalism posits totality facts — the fact that the existing things are all the existing things — as a positive entity that rules out absences. But totality facts are metaphysically suspicious because they seem to quantify over everything that doesn't exist. (2) An alternative denies that negative truths require positive truthmakers, holding they hold in virtue of the absence of false-makers rather than the presence of truth-makers."
  explanation: "This debate reveals a deep tension in truthmaker theory between the intuition that all truths should be grounded in positive reality and the difficulty of providing positive grounds for facts about what doesn't exist. The maximalist position generates controversial ontological commitments (totality facts, perhaps absences as entities); the minimalist position must explain what grounds negative truths if not positive entities. Neither solution is fully satisfying, which is why negative truths remain a live research problem in analytic metaphysics."
```

## Explainer

From your prerequisites on grounding and fundamentality, you know that the world has a hierarchical structure: some facts are fundamental and others hold in virtue of the fundamental facts. From your work on facts and truthmakers, you know the truthmaking relation: a truthmaker for a proposition is something in the world in virtue of which that proposition is true—not merely evidence for it, but the very entity or fact that makes it true. Putting these together, the central question becomes: what are the truthmakers for all true propositions, and can they all ultimately be traced back to fundamental facts?

A key insight is that **truthmakers need not mirror the complexity of the truths they make true**. For the proposition "This ball is red," the truthmaker might simply be the ball with its property of redness. But consider "Either it is raining or it is sunny"—a disjunction is made true by a truthmaker for either disjunct, so the existence of rain suffices. Consider "There are seven planets"—this seems to require the existence of seven distinct objects. The project of truthmaker theory is to systematically map the logical structure of propositions onto the structure of reality, determining which kinds of entities—objects, properties, relations, states of affairs, tropes—are needed as truthmakers for the full range of true statements.

The hardest cases are **negative truths**. What makes "There are no unicorns" true? It cannot be any positive entity—unicorns are precisely what is absent. One response is **truthmaker maximalism**: insisting that every true proposition must have a positive truthmaker, leading to positing "totality facts"—the fact that the things that exist are all the things that exist—as truthmakers for negative truths. But many philosophers find totality facts metaphysically suspicious. Alternative views deny that negative truths require truthmakers at all, holding instead that they hold in virtue of the absence of false-making entities, not the presence of true-making ones.

The connection to **fundamentality** transforms this into a full research program. If grounding has a bottom level, then fundamental truthmakers are those at the base of the hierarchy: they make truths true without themselves holding in virtue of anything more basic. Every derivative truth should be traceable upward through the grounding structure to the fundamental level. This gives metaphysics a precise task: identify which facts are genuinely fundamental—candidates include fundamental physical facts, facts about properties or laws of nature—and show how all other truths are grounded in them without remainder.
