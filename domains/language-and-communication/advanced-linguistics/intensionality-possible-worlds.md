---
id: intensionality-possible-worlds
title: Intensionality and Possible Worlds Semantics
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: montague-semantics
  type: hard
- id: modal-semantics-necessity-possibility
  type: hard
builds-toward:
- de-re-de-dicto-distinction
tags:
- intensionality
- possible-worlds
- modality
stage: advanced
status: draft
---

# Intensionality and Possible Worlds Semantics

## Core Idea
Intensional expressions like modals, belief verbs, and conditionals cannot be evaluated purely in the actual world; their truth conditions depend on possible worlds. The meaning of an intensional expression is an intension—a function from possible worlds to extensions. 'It is possible that it rains' is true if there exists a possible world where it rains, even if it is not raining in the actual world.

## How It's Best Learned
Represent modal and intensional statements using possible-worlds models, assigning truth values relative to different world states. Examine how the truth of intensional statements depends on accessibility relations between worlds.

## Common Misconceptions
- Intensional operators do not merely express uncertainty; they quantify over possible worlds with specific accessibility properties.
- Not all apparent intensionality requires possible-worlds analysis; some may be pragmatic or epistemically grounded.

## Explainer

From your work with Montague semantics, you know that meanings can be treated compositionally as functions: a sentence's meaning is built from the meanings of its parts, with each part denoting something in a model. In standard extensional semantics, a noun phrase denotes a set of individuals, a verb phrase denotes a property, and a sentence denotes a truth value — true or false relative to the actual world. This works well for "The cat is on the mat." But it breaks down for "It is possible that the cat is on the mat" or "Alice believes the cat is on the mat." These are **intensional contexts**, where the truth of the whole does not depend only on what is actually true.

The problem becomes vivid with substitution. In purely extensional semantics, if "the morning star" and "the evening star" both denote the planet Venus, then replacing one with the other in any sentence should preserve truth. But "John believes the morning star is a planet" can be true while "John believes the evening star is a planet" is false — if John doesn't know they're the same object. The two expressions have the same **extension** (they pick out the same individual in the actual world) but different **intensions** (they pick it out via different descriptions, and may pick out different things in other possible worlds). Intensional semantics distinguishes between the two by making meanings functions from possible worlds to extensions: an **intension** is a function from possible worlds to an extension, not just an extension.

A **possible world** is a complete way the world could have been — a maximally consistent description of a state of affairs. Modal operators quantify over them: "Necessarily P" means P is true in all accessible possible worlds; "Possibly P" means P is true in at least one. The **accessibility relation** between worlds determines which worlds count as "possible" relative to a given world — and different kinds of modality (epistemic, deontic, metaphysical) correspond to different accessibility relations. From your prerequisite work on modal semantics, you know this framework; intensionality extends it from modals to the full range of operators that create opaque contexts.

**Propositional attitude verbs** like *believe*, *want*, *hope*, and *fear* are then analyzed as quantifying over worlds compatible with the subject's mental states. "Alice believes P" is true if P is true in all worlds compatible with what Alice believes — which may exclude some actual facts and include some counterfactual ones. This explains the morning star/evening star asymmetry: Alice's belief worlds may include the morning star being a planet without including the evening star being a planet if she hasn't connected the two. Intensionality is thus not a quirk of a few special constructions — it is pervasive in natural language, appearing in modals, belief verbs, conditionals, and desire predicates, all receiving a unified treatment through possible-worlds semantics.
