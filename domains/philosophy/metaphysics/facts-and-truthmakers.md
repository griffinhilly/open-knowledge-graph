---
id: facts-and-truthmakers
title: Facts and Truthmakers
domain: philosophy
course: metaphysics
prerequisites:
- id: ontological-categories
  type: hard
- id: universals-and-particulars
  type: soft
builds-toward:
- grounding-and-fundamentality
tags:
- facts
- truthmakers
- correspondence
- states of affairs
- Armstrong
stage: formal-systems
status: validated
---

# Facts and Truthmakers

## Core Idea
Truthmaker theory holds that for every truth there must be some entity in the world — a truthmaker — whose existence necessitates that truth. The classic candidate truthmakers are facts or states of affairs: structured entities composed of objects and properties bound together. Armstrong championed the view that facts are irreducible additions to ontology — the world is not just a collection of objects and properties floating free, but objects-having-properties. This grounds the correspondence intuition: the proposition 'the cat is on the mat' is true because there exists a fact (the cat's being on the mat). Critics question whether truthmaker maximalism is sustainable, especially for negative truths ('there are no unicorns') and universal truths.

## How It's Best Learned
Read Armstrong's Truth and Truthmakers chapters 1-3, then study Molnar's and Parsons's objections regarding negative existentials. Try to construct a truthmaker for the claim 'there are no hobbits' — the difficulty is instructive.

## Common Misconceptions
- Facts in the truthmaker sense are not just true propositions restated; they are worldly entities that make propositions true.
- Truthmaker theory does not require that every truth has a unique dedicated truthmaker — one entity can make many truths true.

## Questions

```yaml
- question: "Armstrong argues that the world cannot be adequately described as merely a collection of objects and properties. What motivates this claim?"
  type: multiple-choice
  options:
    - "Objects and properties are not distinct — one reduces to the other — so facts are needed to individuate them"
    - "A list of objects and properties doesn't determine which properties are instantiated by which objects; only structured facts (objects-having-properties) do that"
    - "Facts provide a more parsimonious ontology than both objects and properties combined"
    - "Modern physics has shown that facts, not objects, are the fundamental constituents of reality"
  answer: 1
  explanation: "Armstrong's point is that ontology cannot stop at cataloguing objects (Socrates) and properties (wisdom) floating independently. Even a complete inventory of both leaves open the question: is Socrates wise? The answer requires something that binds an object to a property — a fact, or state of affairs: Socrates's being wise. This structured entity is what necessitates the truth of 'Socrates is wise.' Without facts as additions to ontology, the connection between objects and properties would be left unexplained, and truth would 'float free' of the world."

- question: "A philosopher argues: 'The truthmaker for "there are no unicorns" is just the collection of all actually existing things — since none of them is a unicorn, the proposition is true.' What is the strongest objection to this proposal?"
  type: multiple-choice
  options:
    - "This proposal is circular because it uses the truth of the proposition to define its truthmaker"
    - "Any specific collection of existing things could in principle coexist with a unicorn somewhere, so no collection of particular existing entities necessitates the absence of unicorns"
    - "The collection would be too large to constitute a single entity that could serve as a truthmaker"
    - "This is a nominalist proposal, and nominalism is false"
  answer: 1
  explanation: "The truthmaker necessitation principle requires that if the truthmaker exists, the proposition cannot be false. The problem with 'all existing things' is that facts about particular existing things are compossible with the existence of additional things — including unicorns. No matter how thorough your list of existing things, the existence of that list doesn't, by itself, preclude something additional existing elsewhere. This is why negative existentials are the hardest case for truthmaker theory: you need something like a 'totality fact' — a special fact that what exists is all there is — to block the possibility of additional entities. But totality facts are ontologically controversial."

- question: "In truthmaker theory, 'facts' are simply true propositions expressed in different words — the fact that snow is white just is the true proposition 'Snow is white.'"
  type: true-false
  answer: false
  explanation: "This is the central misconception truthmaker theory is designed to correct. Facts in Armstrong's sense are worldly entities — constituents of reality, not linguistic or representational items. A fact (Socrates's being wise) exists in the world; a proposition ('Socrates is wise') is the representational item that the fact makes true. They belong to different ontological categories: facts are in the world, propositions are about the world. Conflating them makes truthmaker theory trivial ('what makes P true? The fact that P') and collapses the correspondence relation that gives the theory its point."

- question: "The truthmaker necessitation principle entails that if a truthmaker for a proposition exists, that proposition cannot possibly be false."
  type: true-false
  answer: true
  explanation: "This is precisely what 'necessitation' means in this context. The relation between a truthmaker and its proposition is not mere coexistence or correlation — the truthmaker's existence logically entails the proposition's truth. There is no possible world in which the fact (Socrates's being wise) exists but the proposition 'Socrates is wise' is false. This strong modal connection is what distinguishes truthmaking from weaker relations like 'being evidence for' or 'being correlated with.' It is also what makes negative truths so difficult: if the truthmaker for 'there are no unicorns' existed while a unicorn also existed, the truthmaker would have failed to necessitate the proposition."

- question: "Why do negative truths like 'there are no unicorns' pose a special problem for truthmaker maximalism? What solution has been proposed, and what makes it ontologically expensive?"
  type: short-answer
  answer: "Positive truths like 'Socrates is wise' have natural truthmakers: the fact of Socrates's instantiating wisdom. Negative truths resist this treatment because there is no positive entity whose existence necessitates the absence of unicorns. Any specific existing thing (a rock, a horse, a person) could coexist with a unicorn — its existence alone doesn't preclude unicorns existing elsewhere. The proposed solution is a totality fact: a special global fact that what currently exists is all there is, and nothing else. This 'that's all' fact would preclude unicorns by ruling out the existence of additional entities. But totality facts are ontologically expensive: they must somehow be a single entity that quantifies over all existents, which is hard to individuate, seems of a radically different type from ordinary particular facts, and may be more mysterious than the negative truths it is meant to explain."
  explanation: "This problem motivates positions that retreat from truthmaker maximalism — accepting that every truth needs a truthmaker — toward more modest views requiring truthmakers only for positive, particular truths. The difficulty with negative truths is one of the most productive pressure points in contemporary metaphysics."
```

## Explainer

The truthmaker project begins with a simple intuition: truth cannot "float free" of the world. If a proposition is true, there must be something in reality that makes it true — something that accounts for its truth rather than merely correlating with it. From your study of ontological categories, you know the landscape of what kinds of things might exist. From universals and particulars, you know how properties and objects relate. Truthmaker theory ties these together by asking: what in the ontological inventory *grounds* true propositions?

The classic answer identifies **truthmakers** with **facts** (or **states of affairs**) — structured entities that bind objects and properties together. Armstrong's key insight was that the world is not just a collection of floating objects and properties. If we list the object Socrates and the property wisdom, that doesn't yet tell us whether Socrates is wise. What tells us is the **fact**: Socrates's being wise — a structured entity in which Socrates instantiates wisdom. This fact, if it exists, *necessitates* the truth of "Socrates is wise." The **truthmaker necessitation principle** holds that if a truthmaker exists, it cannot fail to make its proposition true. The proposition doesn't merely coexist with the truthmaker; the truthmaker's existence entails the proposition's truth.

The intuitive picture quickly generates puzzles. Consider **negative truths**: "there are no unicorns." What is the truthmaker for this? No particular unicorn exists to serve that role. No specific fact about existing things in isolation does it — any such fact could coexist with a unicorn somewhere else. **Totality facts** are one proposed solution: a special fact that what exists is *all* that exists — a "that's all" fact that precludes unicorns. But totality facts are ontologically costly: they seem to require a global fact over all particulars, which is hard to individuate and arguably more mysterious than what we started with. **Universal generalizations** ("all ravens are black") pose the same difficulty.

These puzzles motivate a debate about **truthmaker maximalism** — the view that every truth has a truthmaker — versus more modest positions that require truthmakers only for positive, particular truths. From your study of universals, you'll recognize how ontological options interact here: if we accept immanent universals (properties as constituents shared across instances), facts can have universals as constituents alongside particulars, giving a rich inventory for truthmakers. Nominalists, who reject universals, must construct truthmakers from particulars alone — **tropes** (particularized property instances, like *this* redness of *this* rose) are one option. Truthmaker theory thus functions as a unifying pressure on all of metaphysics: whatever ontology you endorse, it must generate truthmakers for all the truths you affirm.

