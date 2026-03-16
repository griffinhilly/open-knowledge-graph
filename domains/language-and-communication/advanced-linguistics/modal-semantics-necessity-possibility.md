---
id: modal-semantics-necessity-possibility
title: 'Modal Semantics: Necessity and Possibility'
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: montague-semantics
  type: hard
- id: modal-logic-intro
  type: hard
tags:
- semantics
- modality
- possible-worlds
stage: advanced
status: draft
---

# Modal Semantics: Necessity and Possibility

## Core Idea
Modal expressions are analyzed using possible-worlds semantics: 'necessarily P' is true if P holds in all possible worlds; 'possibly P' if P holds in some possible world. This framework elegantly explains how modals interact with negation and quantifiers ('It's not necessary that everyone attends' differs in truth conditions from 'Everyone must not attend'), resolving ambiguities through formal structure.

## Explainer

From Montague semantics, you know how to compute the truth conditions of sentences compositionally — building the meaning of a complex expression from the meanings of its parts using typed lambda calculus. From modal logic, you know the algebraic framework: a Kripke model with a set of possible worlds and an accessibility relation, where □P (necessity) means P is true in all accessible worlds and ◇P (possibility) means P is true in at least one. Modal semantics for natural language is the project of bringing these two frameworks together — applying possible-worlds reasoning to the modals that appear in ordinary speech, like *must*, *might*, *can*, *should*, *necessarily*, and *possibly*.

The first important move is recognizing that natural language modals are not uniform. **Epistemic modality** concerns what is possible or necessary given what is known: "She must be home — her lights are on" doesn't assert metaphysical necessity but the speaker's evidential commitment. **Deontic modality** concerns obligations and permissions: "You must report any income over $50,000" says nothing about what is physically necessary but what is required by law or rule. **Dynamic modality** concerns abilities and dispositions: "She can run a four-minute mile" reports a capacity. The same word (*must*, *can*) shifts meaning across these flavors; the possible-worlds framework handles this by varying what the accessibility relation represents — epistemic necessity ranges over worlds compatible with the speaker's knowledge; deontic necessity ranges over worlds compatible with the relevant rules or norms.

**Kratzer's restrictor analysis** (the dominant modern account) refines this further. Rather than treating a modal like *must* as simply "in all accessible worlds," Kratzer argues that modals operate on two contextual parameters: a **modal base** (a set of propositions restricting the relevant worlds — e.g., what is known, what the laws require) and an **ordering source** (a set of propositions ranking those worlds by some standard of normality or ideality). "You must leave" in a deontic context is evaluated against worlds where relevant rules are satisfied, ranked by how closely they approximate ideal compliance. This two-parameter structure explains why deontic and epistemic modals can differ in their projection behavior and why sentences like "It might be that you must leave" are coherent.

The power of the framework becomes clearest in **scope interactions with negation and quantifiers**. Consider: "It's not necessary that everyone attends" — here negation takes wide scope over necessity, yielding ¬□(∀x. attends(x)), which means it's not the case that all worlds have universal attendance. Contrast "Everyone must not attend" — parsed as ∀x.□(¬attends(x)), which says for each person, in all relevant worlds, they don't attend. These have very different truth conditions: the first is compatible with some worlds where everyone attends; the second prohibits attendance for each individual. Getting scope interactions right is one of the main motivations for doing modal semantics formally rather than informally — intuitions about these sentences are unreliable, but compositional derivation gives determinate answers.
